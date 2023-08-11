import json
import pytest
from did_static import encode, decode, resolve, resolve_hash_for_static


DOC = {
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


def test_encode_decode():
    encoded = encode(DOC)
    decoded = decode(encoded)
    assert decoded == DOC


def test_resolve():
    encoded = encode(DOC)
    print(json.dumps(resolve(encoded), indent=2))


def test_resolve_hash_for_static():
    encoded = encode(DOC)
    print(json.dumps(resolve_hash_for_static(encoded), indent=2))


@pytest.mark.parametrize(
    ("replace_terms", "index", "flatten_keys"),
    [
        (False, False, False),
        (False, False, True),
        (False, True, False),
        (False, True, True),
        (True, False, False),
        (True, False, True),
        (True, True, False),
        (True, True, True),
    ],
)
def test_compression(replace_terms, index, flatten_keys):
    def _report_compression(encoded):
        decoded = decode(encoded)
        encoded_len = len(encoded)
        decoded_len = len(json.dumps(decoded, separators=(",", ":")))
        print(
            "Encoded:",
            encoded_len,
            "Decoded:",
            decoded_len,
        )
        print("Compression:", encoded_len / decoded_len)

    print(
        "replace terms:", replace_terms, "index:", index, "flatten keys:", flatten_keys
    )
    _report_compression(
        encode(DOC, replace_terms=replace_terms, index=index, flatten_keys=flatten_keys)
    )
