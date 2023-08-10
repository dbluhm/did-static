import json
from typing import Any, Dict, List, TypeVar, Union, cast
from multiformats import multibase, multicodec
from msgpack import packb, unpackb

TERMS = [
    "@context",
    "Bls12381G1Key2020",
    "Bls12381G2Key2020",
    "DIDCommMessaging",
    "EcdsaSecp256k1VerificationKey2019",
    "Ed25519VerificationKey2018",
    "Ed25519VerificationKey2020",
    "JsonWebKey2020",
    "PgpVerificationKey2021",
    "RsaVerificationKey2018",
    "X25519KeyAgreementKey2019",
    "X25519KeyAgreementKey2020",
    "accept",
    "alsoKnownAs",
    "assertionMethod",
    "authentication",
    "capabilityDelegation",
    "capabilityInvocation",
    "controller",
    "https://w3id.org/security/suites/ed25519-2020/v1",
    "https://w3id.org/security/suites/x25519-2020/v1",
    "https://www.w3.org/ns/did/v1",
    "id",
    "keyAgreement",
    "publicKeyBase58",
    "publicKeyJwk",
    "publicKeyMultibase",
    "routingKeys",
    "service",
    "serviceEndpoint",
    "type",
    "verificationMethod",
]

ENC_TERMS = {term: index.to_bytes(1) for index, term in enumerate(TERMS)}

DEC_TERMS = {index.to_bytes(1): term for index, term in enumerate(TERMS)}


T = TypeVar("T", bound=Union[Dict[Any, Any], List[Any], Any])


def _decode_doc_keys(document: Dict[str, Any]):
    if "verificationMethod" in document:
        for vm in document["verificationMethod"]:
            if "publicKeyMultibase" in vm:
                vm["publicKeyMultibase"] = multibase.decode(vm["publicKeyMultibase"])


def _encode_doc_keys(document: Dict[str, Any]):
    if "verificationMethod" in document:
        for vm in document["verificationMethod"]:
            if "publicKeyMultibase" in vm:
                vm["publicKeyMultibase"] = multibase.encode(vm["publicKeyMultibase"], "base58btc")


def _term_replace(terms: Dict[Any, Any], value: T) -> T:
    if isinstance(value, dict):
        return cast(
            T, {terms.get(k, k): _term_replace(terms, v) for k, v in value.items()}
        )
    if isinstance(value, list):
        return cast(T, [_term_replace(terms, v) for v in value])

    return terms.get(value, value)


def _encode_terms(value: T) -> T:
    return _term_replace(ENC_TERMS, value)


def _decode_terms(value: T) -> T:
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


def encode(document: dict) -> str:
    index = _generate_index(document)
    #_decode_doc_keys(document)
    if index:
        document = _term_replace({v: k for k, v in index.items()}, document)
        document[255] = index
    document = _encode_terms(document)
    document_bytes = packb(document)
    wrapped = multicodec.wrap("messagepack", cast(bytes, document_bytes))
    encoded = multibase.encode(wrapped, "base58btc")
    return f"did:static:{encoded}"


def decode(did: str) -> dict:
    encoded = did.split(":", 2)[2]
    wrapped = multibase.decode(encoded)
    _, document_bytes = multicodec.unwrap(wrapped)
    document = unpackb(document_bytes, strict_map_key=False)
    if 255 in document:
        document = _term_replace(document.pop(255), document)
    document = _decode_terms(document)
    #_encode_doc_keys(document)
    return document


if __name__ == "__main__":
    doc = {
        "@context": [
            "https://www.w3.org/ns/did/v1",
            "https://w3id.org/security/suites/x25519-2020/v1",
            "https://w3id.org/security/suites/ed25519-2020/v1",
        ],
        "verificationMethod": [
            {
                "id": "#6LSqPZfn",
                "type": "X25519KeyAgreementKey2020",
                "publicKeyMultibase": "z6LSqPZfn9krvgXma2icTMKf2uVcYhKXsudCmPoUzqGYW24U",
            },
            {
                "id": "#6MkrCD1c",
                "type": "Ed25519VerificationKey2020",
                "publicKeyMultibase": "z6MkrCD1csqtgdj8sjrsu8jxcbeyP6m7LiK87NzhfWqio5yr",
            },
        ],
        "authentication": ["#6MkrCD1c"],
        "assertionMethod": ["#6MkrCD1c"],
        "keyAgreement": ["#6LSqPZfn"],
        "capabilityInvocation": ["#6MkrCD1c"],
        "capabilityDelegation": ["#6MkrCD1c"],
        "service": [
            {
                "id": "#didcommmessaging-0",
                "type": "DIDCommMessaging",
                "serviceEndpoint": "didcomm://queue",
                "accept": ["didcomm/v2"],
                "routingKeys": [],
            }
        ],
    }
    encoded = encode(doc)
    print(encoded)
    decoded = decode(encoded)
    print(decoded)
    print("Encoded:", len(encoded), "Decoded:", len(json.dumps(decoded)))
