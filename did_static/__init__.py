from abc import ABC, abstractmethod
import json
from copy import deepcopy
from typing import Any, Dict, List, TypeVar, Union, cast, overload
from multiformats import multibase, multicodec, multihash
from msgpack import packb, unpackb

from .terms import DEC_TERMS, ENC_TERMS

VERSION = 0

VERSION_KEY = 0x01
DOC_KEY = 0x02
INDEX_KEY = 0x03

T = TypeVar("T")
K = TypeVar("K")
V = TypeVar("V")


def _decode_doc_keys(document: Dict[str, Any]):
    if "verificationMethod" in document:
        for vm in document["verificationMethod"]:
            if "publicKeyMultibase" in vm:
                vm["publicKeyMultibase"] = multibase.decode(vm["publicKeyMultibase"])


def _encode_doc_keys(document: Dict[str, Any]):
    if "verificationMethod" in document:
        for vm in document["verificationMethod"]:
            if "publicKeyMultibase" in vm:
                vm["publicKeyMultibase"] = multibase.encode(
                    vm["publicKeyMultibase"], "base58btc"
                )


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
    if isinstance(value, dict):
        return {terms.get(k, k): _term_replace(terms, v) for k, v in value.items()}
    if isinstance(value, list):
        return [_term_replace(terms, v) for v in value]

    return terms.get(value, value)


def _encode_terms(value: dict) -> dict:
    return _term_replace(ENC_TERMS, value)


def _decode_terms(value: dict) -> dict:
    return _term_replace(DEC_TERMS, value)


def _generate_index(value: Dict[str, Any]) -> Dict[int, str]:
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
    if INDEX_KEY in bundle:
        document = _term_replace(bundle.pop(INDEX_KEY), document)
    document = _decode_terms(document)
    # _encode_doc_keys(document)
    return document


def _make_absolute(ident: str, value: dict) -> dict:
    """Recursively make all relative identifiers absolute."""
    value = deepcopy(value)
    def __make_absolute(value: T) -> T:
        if isinstance(value, dict):
            if "id" in value and value["id"].startswith("#"):
                relative = value["id"]
                value["id"] = f"{ident}#{relative}"
            for v in value.values():
                _make_absolute(ident, v)
        if isinstance(value, list):
            for v in value:
                _make_absolute(ident, v)
        return value

    return __make_absolute(value)


class DocVisitor(ABC):
    """Visitor class for manipulating the document."""
    def __init__(self, document: dict):
        self.document = document

    def visit_verification_method(self, value: dict):
        """Visit a verification method."""
        return value

    def visit_service(self, value: dict):
        """Visit a service."""
        return value

    def visit_value_with_id(self, value: dict):
        """Visit a value with an id."""
        return value

    def visit_verification_relationship_ref(self, value: str):
        """Visit a verification relationship."""
        return value

    def visit_verification_relationship_embedded(self, value: dict):
        """Visit an embedded verification method."""
        return value

    def visit_authentication_ref(self, value: str):
        """Visit an authentication relationship."""
        return value

    def visit_authentication_embedded(self, value: dict):
        """Visit an embedded authentication relationship."""
        return value

    def visit_key_agreement_ref(self, value: str):
        """Visit a key agreement relationship."""
        return value

    def visit_key_agreement_embedded(self, value: dict):
        """Visit an embedded key agreement relationship."""
        return value

    def visit_assertion_method_ref(self, value: str):
        """Visit an assertion method relationship."""
        return value

    def visit_assertion_method_embedded(self, value: dict):
        """Visit an embedded assertion method relationship."""
        return value

    def visit_capability_delegation_ref(self, value: str):
        """Visit a capability delegation relationship."""
        return value

    def visit_capability_delegation_embedded(self, value: dict):
        """Visit an embedded capability delegation relationship."""
        return value

    def visit_capability_invocation_ref(self, value: str):
        """Visit a capability invocation relationship."""
        return value

    def visit_capability_invocation_embedded(self, value: dict):
        """Visit an embedded capability invocation relationship."""
        return value

    def visit(self):
        """Visit the document."""
        vms = []
        for value in self.document["verificationMethod"]:
            value = self.visit_value_with_id(value)
            value = self.visit_verification_method(value)
            vms.append(value)
        self.document["verificationMethod"] = vms

        services = []
        for value in self.document["service"]:
            value = self.visit_value_with_id(value)
            value = self.visit_service(value)
            services.append(value)
        self.document["service"] = services

        authentication = []
        for value in self.document["authentication"]:
            if isinstance(value, str):
                value = self.visit_verification_relationship_ref(value)
                value = self.visit_authentication_ref(value)
            if isinstance(value, dict):
                value = self.visit_value_with_id(value)
                value = self.visit_verification_relationship_embedded(value)
                value = self.visit_authentication_embedded(value)
            authentication.append(value)
        self.document["authentication"] = authentication

        key_agreement = []
        for value in self.document["keyAgreement"]:
            if isinstance(value, str):
                value = self.visit_verification_relationship_ref(value)
                value = self.visit_key_agreement_ref(value)
            if isinstance(value, dict):
                value = self.visit_value_with_id(value)
                value = self.visit_verification_relationship_embedded(value)
                value = self.visit_key_agreement_embedded(value)
            key_agreement.append(value)
        self.document["keyAgreement"] = key_agreement

        assertion_method = []
        for value in self.document["assertionMethod"]:
            if isinstance(value, str):
                value = self.visit_verification_relationship_ref(value)
                value = self.visit_assertion_method_ref(value)
            if isinstance(value, dict):
                value = self.visit_value_with_id(value)
                value = self.visit_verification_relationship_embedded(value)
                value = self.visit_assertion_method_embedded(value)
            assertion_method.append(value)
        self.document["assertionMethod"] = assertion_method

        capability_delegation = []
        for value in self.document["capabilityDelegation"]:
            if isinstance(value, str):
                value = self.visit_verification_relationship_ref(value)
                value = self.visit_capability_delegation_ref(value)
            if isinstance(value, dict):
                value = self.visit_value_with_id(value)
                value = self.visit_verification_relationship_embedded(value)
                value = self.visit_capability_delegation_embedded(value)
            capability_delegation.append(value)
        self.document["capabilityDelegation"] = capability_delegation

        capability_invocation = []
        for value in self.document["capabilityInvocation"]:
            if isinstance(value, str):
                value = self.visit_verification_relationship_ref(value)
                value = self.visit_capability_invocation_ref(value)
            if isinstance(value, dict):
                value = self.visit_value_with_id(value)
                value = self.visit_verification_relationship_embedded(value)
                value = self.visit_capability_invocation_embedded(value)
            capability_invocation.append(value)
        self.document["capabilityInvocation"] = capability_invocation

        return self.document


def decoded_to_resolved(did: str, document: dict) -> dict:
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
    ident_hash = multibase.encode(multihash.digest(ident_bytes, "sha2-256"), "base58btc")
    document["alsoKnownAs"] = ["did:hash:" + ident_hash]
    document = decoded_to_resolved(did, document)
    return document


def resolve_hash_for_static(did: str) -> dict:
    """Resolve a did:hash document from a did:static DID."""
    document = decode(did)
    codec, ident_bytes = multicodec.unwrap(multibase.decode(did[11:]))
    ident_hash = multibase.encode(multihash.digest(ident_bytes, "sha2-256"), "base58btc")
    did_hash = "did:hash:" + ident_hash
    document["alsoKnownAs"] = [did]
    document["id"] = did_hash
    return decoded_to_resolved(did_hash, document)
