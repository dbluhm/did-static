import json
from base64 import urlsafe_b64encode
from multiformats import multibase
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
def test_encode_decode(replace_terms, index, flatten_keys):
    encoded = encode(
        DOC, replace_terms=replace_terms, index=index, flatten_keys=flatten_keys
    )
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
        decoded_len_no_whitespace = len(json.dumps(decoded, separators=(",", ":")))
        decoded_len = len(json.dumps(decoded))
        decoded_len_b58 = (
            len(
                multibase.encode(
                    json.dumps(decoded, separators=(",", ":")).encode(), "base58btc"
                )
            )
            - 1
        )
        decoded_len_b64 = len(
            urlsafe_b64encode(json.dumps(decoded, separators=(",", ":")).encode())
        )
        print("    - **Encoded (including `did:static:`):**", encoded_len)
        print(
            "    - **Decoded (plain json string, no whitespace):**",
            decoded_len_no_whitespace,
        )
        print("    - **Decoded (plain json string, with whitespace):**", decoded_len)
        print(
            "    - **Decoded Base 58 (json string, no whitespace):**", decoded_len_b58
        )
        print(
            "    - **Decoded Base 64 url (json string, no whitespace):**",
            decoded_len_b64,
        )
        print(
            "    - **Compression (encoded / decoded b64):**",
            "{:.2%}".format(encoded_len / decoded_len_b64),
        )

    print()
    print(
        f"- **Encode options:** replace terms: {replace_terms}, "
        f"index: {index}, flatten keys: {flatten_keys}"
    )
    _report_compression(
        encode(DOC, replace_terms=replace_terms, index=index, flatten_keys=flatten_keys)
    )
