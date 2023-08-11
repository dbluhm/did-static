from typing import Any, Dict, TypeVar, cast, overload
from multiformats import multibase, multicodec, multihash
from msgpack import packb, unpackb

from .terms import DEC_TERMS, ENC_TERMS
from .visitor import DocVisitor

VERSION = 0

VERSION_KEY = 0x00
DOC_KEY = 0x01
INDEX_KEY = 0x02

T = TypeVar("T")
K = TypeVar("K")
V = TypeVar("V")


def _decode_doc_keys(document: Dict[str, Any]):
    """Decode the keys in the document.

    This is an optional step that results in smaller encoded size since we
    prevent encoding the keys multiple times.
    """

    class Decoder(DocVisitor):
        def visit_verification_method(self, value: dict) -> dict:
            if "publicKeyMultibase" in value:
                value["publicKeyMultibase"] = multibase.decode(
                    value["publicKeyMultibase"]
                )
            return value

        def visit_verification_relationship_embedded(self, value: dict):
            return self.visit_verification_method(value)

    return Decoder(document).visit()


def _encode_doc_keys(document: Dict[str, Any]):
    """Encode the keys in the document.

    This is an optional step that reverses the decode step. Doing this
    encode/decode step results in smaller encoded size since we prevent
    encoding the keys multiple times.
    """

    class Encoder(DocVisitor):
        def visit_verification_method(self, value: dict) -> dict:
            if "publicKeyMultibase" in value:
                value["publicKeyMultibase"] = multibase.encode(
                    value["publicKeyMultibase"], "base58btc"
                )
            return value

        def visit_verification_relationship_embedded(self, value: dict):
            return self.visit_verification_method(value)

    return Encoder(document).visit()


@overload
def _term_replace(terms: Dict[K, V], value: K) -> V:
    ...


@overload
def _term_replace(terms: Dict[Any, Any], value: dict) -> dict:
    ...


@overload
def _term_replace(terms: Dict[Any, Any], value: list) -> list:
    ...


def _term_replace(terms: Dict[Any, Any], value: Any) -> Any:
    """Replace values in a dictionary with the value looked up in terms."""
    if isinstance(value, dict):
        return {terms.get(k, k): _term_replace(terms, v) for k, v in value.items()}
    if isinstance(value, list):
        return [_term_replace(terms, v) for v in value]

    return terms.get(value, value)


def _encode_terms(value: dict) -> dict:
    """Replace the long form of terms with the shorthand from the terms table."""
    return _term_replace(ENC_TERMS, value)


def _decode_terms(value: dict) -> dict:
    """Replace shorthands from the terms table with the long form."""
    return _term_replace(DEC_TERMS, value)


def _generate_index(value: Dict[str, Any]) -> Dict[int, str]:
    """Generate an index of all ids in the document.

    This is an optional step that can slightly optimize the size of the encoded
    document when referencing the same key from multiple verification
    relationships, etc.

    It does so by creating a map of all ids to their index in the document. Then
    the encoding method will use this index to replace the id where it's used.
    The index is included in the bundle for decoding.
    """
    index = []

    def __generate_index(value: Any):
        if isinstance(value, dict):
            for k, v in value.items():
                if k == "id" and isinstance(v, str) and v not in index:
                    index.append(v)
                __generate_index(v)
        if isinstance(value, list):
            for v in value:
                __generate_index(v)

    __generate_index(value)
    return {i: v for i, v in enumerate(index)}


def encode(document: Dict[str, Any]) -> str:
    """Encode a static DID from a document."""
    bundle = {}
    bundle[VERSION_KEY] = VERSION
    index = _generate_index(document)
    # _decode_doc_keys(document)
    if index:
        bundle[INDEX_KEY] = index
        document = _term_replace({v: k for k, v in index.items()}, document)
    document = _encode_terms(document)
    bundle[DOC_KEY] = document
    bundle_bytes = packb(bundle)
    wrapped = multicodec.wrap("messagepack", cast(bytes, bundle_bytes))
    encoded = multibase.encode(wrapped, "base58btc")
    return f"did:static:{encoded}"


def decode(did: str) -> dict:
    """Decode static DID."""
    encoded = did.split(":", 2)[2]
    wrapped = multibase.decode(encoded)
    _, bundle_bytes = multicodec.unwrap(wrapped)
    bundle = unpackb(bundle_bytes, strict_map_key=False)
    document = cast(dict, bundle.pop(DOC_KEY))
    version = bundle.pop(VERSION_KEY)
    assert version == 0
    if INDEX_KEY in bundle:
        document = _term_replace(bundle.pop(INDEX_KEY), document)
    document = _decode_terms(document)
    # _encode_doc_keys(document)
    return document


def decoded_to_resolved(did: str, document: dict) -> dict:
    """Add DID and controller to verification methods and relationships."""

    class Visitor(DocVisitor):
        def visit_verification_method(self, value: dict):
            value["controller"] = did
            return value

        def visit_verification_relationship_embedded(self, value: dict):
            value["controller"] = did
            return value

        def visit_value_with_id(self, value: dict):
            if value["id"].startswith("#"):
                value["id"] = f"{did}{value['id']}"
            return value

        def visit_verification_relationship_ref(self, value: str):
            if value.startswith("#"):
                return f"{did}{value}"

    document = Visitor(document).visit()
    return document


def resolve(did: str) -> dict:
    """Resolve static DID to document."""
    if not did.startswith("did:static:"):
        raise ValueError("Invalid DID")

    document = decode(did)
    document["id"] = did
    codec, ident_bytes = multicodec.unwrap(multibase.decode(did[11:]))
    ident_hash = multibase.encode(
        multihash.digest(ident_bytes, "sha2-256"), "base58btc"
    )
    document["alsoKnownAs"] = ["did:hash:" + ident_hash]
    document = decoded_to_resolved(did, document)
    return document


def resolve_hash_for_static(did: str) -> dict:
    """Resolve a did:hash document from a did:static DID."""
    document = decode(did)
    codec, ident_bytes = multicodec.unwrap(multibase.decode(did[11:]))
    ident_hash = multibase.encode(
        multihash.digest(ident_bytes, "sha2-256"), "base58btc"
    )
    did_hash = "did:hash:" + ident_hash
    document["alsoKnownAs"] = [did]
    document["id"] = did_hash
    return decoded_to_resolved(did_hash, document)
