import json
from did_static import encode, decode, resolve, resolve_hash_for_static

def test_encode_decode():
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
    print(json.dumps(resolve(encoded), indent=2))
    print(json.dumps(resolve_hash_for_static(encoded), indent=2))
