# Static DID Method

#### Example DID:
```
did:static:z5pU4iAPY5v6yrYBMmKjWANNaEdMeV7So7Hor8aynbHpJ47zj3DX6CqjQUAqjHiu4jr6HWFuNzjGcyHzJw3oUfcx5umudmV5H3mArhV4B3ibRgT1dN9H6XifZpaUFuZpeYx8SroRXKncvZhhaBRXBBQ36emZYZ9GuFuqR8C2F5p7ZGGnWiMFqbWckNq1wbbBUxMn4aowDRmcYUKAqZ3VCELRtmoz6PRkMDLo4ZR8Yvo3wwosphukawM2MkNyB1V3aimpAtGG8uiMvShR4Mm2rXn89DAE2u92jNwg2GZ4sCp5xp1tAyAusqUp9f4cbzKQSGsB7RreAVN7Wcox7dvjFUGpDsBEfQ7XbryZmMUfSJ8VPfRB9qhDaLBWF
```

#### Example Input Document to `encode()`

```json
{
  "@context": [
    "https://www.w3.org/ns/did/v1",
    "https://w3id.org/security/suites/x25519-2020/v1",
    "https://w3id.org/security/suites/ed25519-2020/v1"
  ],
  "verificationMethod": [
    {
      "id": "#6LSqPZfn",
      "type": "X25519KeyAgreementKey2020",
      "publicKeyMultibase": "z6LSqPZfn9krvgXma2icTMKf2uVcYhKXsudCmPoUzqGYW24U"
    },
    {
      "id": "#6MkrCD1c",
      "type": "Ed25519VerificationKey2020",
      "publicKeyMultibase": "z6MkrCD1csqtgdj8sjrsu8jxcbeyP6m7LiK87NzhfWqio5yr"
    }
  ],
  "authentication": [
    "#6MkrCD1c"
  ],
  "assertionMethod": [
    "#6MkrCD1c"
  ],
  "keyAgreement": [
    "#6LSqPZfn"
  ],
  "capabilityInvocation": [
    "#6MkrCD1c"
  ],
  "capabilityDelegation": [
    "#6MkrCD1c"
  ],
  "service": [
    {
      "id": "#didcommmessaging-0",
      "type": "DIDCommMessaging",
      "serviceEndpoint": "didcomm://queue",
      "accept": [
        "didcomm/v2"
      ],
      "routingKeys": []
    }
  ]
}
```

#### Size Stats

- Encode options: replace terms: False index: False flatten keys: False
    - Encoded (including `did:static:`): 904
    - Decoded (plain json string, no whitespace): 732
    - Decoded (plain json string, with whitespace): 769
    - Decoded Base 58 (json string, no whitespace): 1000
    - Decoded Base 64 url (json string, no whitespace): 976
    - Compression (encoded / decoded b64): 0.9262295081967213
- Encode options: replace terms: False index: False flatten keys: True
    - Encoded (including `did:static:`): 866
    - Decoded (plain json string, no whitespace): 732
    - Decoded (plain json string, with whitespace): 769
    - Decoded Base 58 (json string, no whitespace): 1000
    - Decoded Base 64 url (json string, no whitespace): 976
    - Compression (encoded / decoded b64): 0.8872950819672131
- Encode options: replace terms: False index: True flatten keys: False
    - Encoded (including `did:static:`): 852
    - Decoded (plain json string, no whitespace): 732
    - Decoded (plain json string, with whitespace): 769
    - Decoded Base 58 (json string, no whitespace): 1000
    - Decoded Base 64 url (json string, no whitespace): 976
    - Compression (encoded / decoded b64): 0.8729508196721312
- Encode options: replace terms: False index: True flatten keys: True
    - Encoded (including `did:static:`): 814
    - Decoded (plain json string, no whitespace): 732
    - Decoded (plain json string, with whitespace): 769
    - Decoded Base 58 (json string, no whitespace): 1000
    - Decoded Base 64 url (json string, no whitespace): 976
    - Compression (encoded / decoded b64): 0.8340163934426229
- Encode options: replace terms: True index: False flatten keys: False
    - Encoded (including `did:static:`): 369
    - Decoded (plain json string, no whitespace): 732
    - Decoded (plain json string, with whitespace): 769
    - Decoded Base 58 (json string, no whitespace): 1000
    - Decoded Base 64 url (json string, no whitespace): 976
    - Compression (encoded / decoded b64): 0.3780737704918033
- Encode options: replace terms: True index: False flatten keys: True
    - Encoded (including `did:static:`): 331
    - Decoded (plain json string, no whitespace): 732
    - Decoded (plain json string, with whitespace): 769
    - Decoded Base 58 (json string, no whitespace): 1000
    - Decoded Base 64 url (json string, no whitespace): 976
    - Compression (encoded / decoded b64): 0.3391393442622951
- Encode options: replace terms: True index: True flatten keys: False
    - Encoded (including `did:static:`): 317
    - Decoded (plain json string, no whitespace): 732
    - Decoded (plain json string, with whitespace): 769
    - Decoded Base 58 (json string, no whitespace): 1000
    - Decoded Base 64 url (json string, no whitespace): 976
    - Compression (encoded / decoded b64): 0.32479508196721313
- Encode options: replace terms: True index: True flatten keys: True
    - Encoded (including `did:static:`): 279
    - Decoded (plain json string, no whitespace): 732
    - Decoded (plain json string, with whitespace): 769
    - Decoded Base 58 (json string, no whitespace): 1000
    - Decoded Base 64 url (json string, no whitespace): 976
    - Compression (encoded / decoded b64): 0.2858606557377049

As visible in these stats, it's important to use the `replace_terms` encoding
option to see a significant overall reduction in size. The other options offer
additional reduction in size but the difference is less significant. In all
cases, `did:static` is still smaller than just base64 url encoding the
document.

#### Resolved Doc

```json
{
  "@context": [
    "https://www.w3.org/ns/did/v1",
    "https://w3id.org/security/suites/x25519-2020/v1",
    "https://w3id.org/security/suites/ed25519-2020/v1"
  ],
  "verificationMethod": [
    {
      "id": "did:static:z5pU4iAPY5v6yrYBMmKjWANNaEdMeV7So7Hor8aynbHpJ47zj3DX6CqjQUAqjHiu4jr6HWFuNzjGcyHzJw3oUfcx5umudmV5H3mArhV4B3ibRgT1dN9H6XifZpaUFuZpeYx8SroRXKncvZhhaBRXBBQ36emZYZ9GuFuqR8C2F5p7ZGGnWiMFqbWckNq1wbbBUxMn4aowDRmcYUKAqZ3VCELRtmoz6PRkMDLo4ZR8Yvo3wwosphukawM2MkNyB1V3aimpAtGG8uiMvShR4Mm2rXn89DAE2u92jNwg2GZ4sCp5xp1tAyAusqUp9f4cbzKQSGsB7RreAVN7Wcox7dvjFUGpDsBEfQ7XbryZmMUfSJ8VPfRB9qhDaLBWF#6LSqPZfn",
      "type": "X25519KeyAgreementKey2020",
      "publicKeyMultibase": "z6LSqPZfn9krvgXma2icTMKf2uVcYhKXsudCmPoUzqGYW24U",
      "controller": "did:static:z5pU4iAPY5v6yrYBMmKjWANNaEdMeV7So7Hor8aynbHpJ47zj3DX6CqjQUAqjHiu4jr6HWFuNzjGcyHzJw3oUfcx5umudmV5H3mArhV4B3ibRgT1dN9H6XifZpaUFuZpeYx8SroRXKncvZhhaBRXBBQ36emZYZ9GuFuqR8C2F5p7ZGGnWiMFqbWckNq1wbbBUxMn4aowDRmcYUKAqZ3VCELRtmoz6PRkMDLo4ZR8Yvo3wwosphukawM2MkNyB1V3aimpAtGG8uiMvShR4Mm2rXn89DAE2u92jNwg2GZ4sCp5xp1tAyAusqUp9f4cbzKQSGsB7RreAVN7Wcox7dvjFUGpDsBEfQ7XbryZmMUfSJ8VPfRB9qhDaLBWF"
    },
    {
      "id": "did:static:z5pU4iAPY5v6yrYBMmKjWANNaEdMeV7So7Hor8aynbHpJ47zj3DX6CqjQUAqjHiu4jr6HWFuNzjGcyHzJw3oUfcx5umudmV5H3mArhV4B3ibRgT1dN9H6XifZpaUFuZpeYx8SroRXKncvZhhaBRXBBQ36emZYZ9GuFuqR8C2F5p7ZGGnWiMFqbWckNq1wbbBUxMn4aowDRmcYUKAqZ3VCELRtmoz6PRkMDLo4ZR8Yvo3wwosphukawM2MkNyB1V3aimpAtGG8uiMvShR4Mm2rXn89DAE2u92jNwg2GZ4sCp5xp1tAyAusqUp9f4cbzKQSGsB7RreAVN7Wcox7dvjFUGpDsBEfQ7XbryZmMUfSJ8VPfRB9qhDaLBWF#6MkrCD1c",
      "type": "Ed25519VerificationKey2020",
      "publicKeyMultibase": "z6MkrCD1csqtgdj8sjrsu8jxcbeyP6m7LiK87NzhfWqio5yr",
      "controller": "did:static:z5pU4iAPY5v6yrYBMmKjWANNaEdMeV7So7Hor8aynbHpJ47zj3DX6CqjQUAqjHiu4jr6HWFuNzjGcyHzJw3oUfcx5umudmV5H3mArhV4B3ibRgT1dN9H6XifZpaUFuZpeYx8SroRXKncvZhhaBRXBBQ36emZYZ9GuFuqR8C2F5p7ZGGnWiMFqbWckNq1wbbBUxMn4aowDRmcYUKAqZ3VCELRtmoz6PRkMDLo4ZR8Yvo3wwosphukawM2MkNyB1V3aimpAtGG8uiMvShR4Mm2rXn89DAE2u92jNwg2GZ4sCp5xp1tAyAusqUp9f4cbzKQSGsB7RreAVN7Wcox7dvjFUGpDsBEfQ7XbryZmMUfSJ8VPfRB9qhDaLBWF"
    }
  ],
  "authentication": [
    "did:static:z5pU4iAPY5v6yrYBMmKjWANNaEdMeV7So7Hor8aynbHpJ47zj3DX6CqjQUAqjHiu4jr6HWFuNzjGcyHzJw3oUfcx5umudmV5H3mArhV4B3ibRgT1dN9H6XifZpaUFuZpeYx8SroRXKncvZhhaBRXBBQ36emZYZ9GuFuqR8C2F5p7ZGGnWiMFqbWckNq1wbbBUxMn4aowDRmcYUKAqZ3VCELRtmoz6PRkMDLo4ZR8Yvo3wwosphukawM2MkNyB1V3aimpAtGG8uiMvShR4Mm2rXn89DAE2u92jNwg2GZ4sCp5xp1tAyAusqUp9f4cbzKQSGsB7RreAVN7Wcox7dvjFUGpDsBEfQ7XbryZmMUfSJ8VPfRB9qhDaLBWF#6MkrCD1c"
  ],
  "assertionMethod": [
    "did:static:z5pU4iAPY5v6yrYBMmKjWANNaEdMeV7So7Hor8aynbHpJ47zj3DX6CqjQUAqjHiu4jr6HWFuNzjGcyHzJw3oUfcx5umudmV5H3mArhV4B3ibRgT1dN9H6XifZpaUFuZpeYx8SroRXKncvZhhaBRXBBQ36emZYZ9GuFuqR8C2F5p7ZGGnWiMFqbWckNq1wbbBUxMn4aowDRmcYUKAqZ3VCELRtmoz6PRkMDLo4ZR8Yvo3wwosphukawM2MkNyB1V3aimpAtGG8uiMvShR4Mm2rXn89DAE2u92jNwg2GZ4sCp5xp1tAyAusqUp9f4cbzKQSGsB7RreAVN7Wcox7dvjFUGpDsBEfQ7XbryZmMUfSJ8VPfRB9qhDaLBWF#6MkrCD1c"
  ],
  "keyAgreement": [
    "did:static:z5pU4iAPY5v6yrYBMmKjWANNaEdMeV7So7Hor8aynbHpJ47zj3DX6CqjQUAqjHiu4jr6HWFuNzjGcyHzJw3oUfcx5umudmV5H3mArhV4B3ibRgT1dN9H6XifZpaUFuZpeYx8SroRXKncvZhhaBRXBBQ36emZYZ9GuFuqR8C2F5p7ZGGnWiMFqbWckNq1wbbBUxMn4aowDRmcYUKAqZ3VCELRtmoz6PRkMDLo4ZR8Yvo3wwosphukawM2MkNyB1V3aimpAtGG8uiMvShR4Mm2rXn89DAE2u92jNwg2GZ4sCp5xp1tAyAusqUp9f4cbzKQSGsB7RreAVN7Wcox7dvjFUGpDsBEfQ7XbryZmMUfSJ8VPfRB9qhDaLBWF#6LSqPZfn"
  ],
  "capabilityInvocation": [
    "did:static:z5pU4iAPY5v6yrYBMmKjWANNaEdMeV7So7Hor8aynbHpJ47zj3DX6CqjQUAqjHiu4jr6HWFuNzjGcyHzJw3oUfcx5umudmV5H3mArhV4B3ibRgT1dN9H6XifZpaUFuZpeYx8SroRXKncvZhhaBRXBBQ36emZYZ9GuFuqR8C2F5p7ZGGnWiMFqbWckNq1wbbBUxMn4aowDRmcYUKAqZ3VCELRtmoz6PRkMDLo4ZR8Yvo3wwosphukawM2MkNyB1V3aimpAtGG8uiMvShR4Mm2rXn89DAE2u92jNwg2GZ4sCp5xp1tAyAusqUp9f4cbzKQSGsB7RreAVN7Wcox7dvjFUGpDsBEfQ7XbryZmMUfSJ8VPfRB9qhDaLBWF#6MkrCD1c"
  ],
  "capabilityDelegation": [
    "did:static:z5pU4iAPY5v6yrYBMmKjWANNaEdMeV7So7Hor8aynbHpJ47zj3DX6CqjQUAqjHiu4jr6HWFuNzjGcyHzJw3oUfcx5umudmV5H3mArhV4B3ibRgT1dN9H6XifZpaUFuZpeYx8SroRXKncvZhhaBRXBBQ36emZYZ9GuFuqR8C2F5p7ZGGnWiMFqbWckNq1wbbBUxMn4aowDRmcYUKAqZ3VCELRtmoz6PRkMDLo4ZR8Yvo3wwosphukawM2MkNyB1V3aimpAtGG8uiMvShR4Mm2rXn89DAE2u92jNwg2GZ4sCp5xp1tAyAusqUp9f4cbzKQSGsB7RreAVN7Wcox7dvjFUGpDsBEfQ7XbryZmMUfSJ8VPfRB9qhDaLBWF#6MkrCD1c"
  ],
  "service": [
    {
      "id": "did:static:z5pU4iAPY5v6yrYBMmKjWANNaEdMeV7So7Hor8aynbHpJ47zj3DX6CqjQUAqjHiu4jr6HWFuNzjGcyHzJw3oUfcx5umudmV5H3mArhV4B3ibRgT1dN9H6XifZpaUFuZpeYx8SroRXKncvZhhaBRXBBQ36emZYZ9GuFuqR8C2F5p7ZGGnWiMFqbWckNq1wbbBUxMn4aowDRmcYUKAqZ3VCELRtmoz6PRkMDLo4ZR8Yvo3wwosphukawM2MkNyB1V3aimpAtGG8uiMvShR4Mm2rXn89DAE2u92jNwg2GZ4sCp5xp1tAyAusqUp9f4cbzKQSGsB7RreAVN7Wcox7dvjFUGpDsBEfQ7XbryZmMUfSJ8VPfRB9qhDaLBWF#didcommmessaging-0",
      "type": "DIDCommMessaging",
      "serviceEndpoint": "didcomm://queue",
      "accept": [
        "didcomm/v2"
      ],
      "routingKeys": []
    }
  ],
  "id": "did:static:z5pU4iAPY5v6yrYBMmKjWANNaEdMeV7So7Hor8aynbHpJ47zj3DX6CqjQUAqjHiu4jr6HWFuNzjGcyHzJw3oUfcx5umudmV5H3mArhV4B3ibRgT1dN9H6XifZpaUFuZpeYx8SroRXKncvZhhaBRXBBQ36emZYZ9GuFuqR8C2F5p7ZGGnWiMFqbWckNq1wbbBUxMn4aowDRmcYUKAqZ3VCELRtmoz6PRkMDLo4ZR8Yvo3wwosphukawM2MkNyB1V3aimpAtGG8uiMvShR4Mm2rXn89DAE2u92jNwg2GZ4sCp5xp1tAyAusqUp9f4cbzKQSGsB7RreAVN7Wcox7dvjFUGpDsBEfQ7XbryZmMUfSJ8VPfRB9qhDaLBWF",
  "alsoKnownAs": [
    "did:hash:zQmcpMXmeNv7gV2aSAky3LuLg6Zb357PTwgkYibghdWYNs9"
  ]
}
```

#### Also Known As

The resolution of a did:static DID includes an `alsoKnownAs` for a `did:hash`
value. This value is the multihash sha2-256, multibase base58btc of the decoded
bytes from the method specific identifier of `did:static`. See the `resolve()`
method implementation for more details on generation.

This `did:hash` value should be treated as an alias for the full `did:static`
value. "Resolving" a `did:hash` value should be done by looking up the
`did:static` value it accompanied, decoding the value, and inserting
`did:hash`.

##### Example `did:hash` Resolved Doc

```json
{
  "@context": [
    "https://www.w3.org/ns/did/v1",
    "https://w3id.org/security/suites/x25519-2020/v1",
    "https://w3id.org/security/suites/ed25519-2020/v1"
  ],
  "verificationMethod": [
    {
      "id": "did:hash:zQmcpMXmeNv7gV2aSAky3LuLg6Zb357PTwgkYibghdWYNs9#6LSqPZfn",
      "type": "X25519KeyAgreementKey2020",
      "publicKeyMultibase": "z6LSqPZfn9krvgXma2icTMKf2uVcYhKXsudCmPoUzqGYW24U",
      "controller": "did:hash:zQmcpMXmeNv7gV2aSAky3LuLg6Zb357PTwgkYibghdWYNs9"
    },
    {
      "id": "did:hash:zQmcpMXmeNv7gV2aSAky3LuLg6Zb357PTwgkYibghdWYNs9#6MkrCD1c",
      "type": "Ed25519VerificationKey2020",
      "publicKeyMultibase": "z6MkrCD1csqtgdj8sjrsu8jxcbeyP6m7LiK87NzhfWqio5yr",
      "controller": "did:hash:zQmcpMXmeNv7gV2aSAky3LuLg6Zb357PTwgkYibghdWYNs9"
    }
  ],
  "authentication": [
    "did:hash:zQmcpMXmeNv7gV2aSAky3LuLg6Zb357PTwgkYibghdWYNs9#6MkrCD1c"
  ],
  "assertionMethod": [
    "did:hash:zQmcpMXmeNv7gV2aSAky3LuLg6Zb357PTwgkYibghdWYNs9#6MkrCD1c"
  ],
  "keyAgreement": [
    "did:hash:zQmcpMXmeNv7gV2aSAky3LuLg6Zb357PTwgkYibghdWYNs9#6LSqPZfn"
  ],
  "capabilityInvocation": [
    "did:hash:zQmcpMXmeNv7gV2aSAky3LuLg6Zb357PTwgkYibghdWYNs9#6MkrCD1c"
  ],
  "capabilityDelegation": [
    "did:hash:zQmcpMXmeNv7gV2aSAky3LuLg6Zb357PTwgkYibghdWYNs9#6MkrCD1c"
  ],
  "service": [
    {
      "id": "did:hash:zQmcpMXmeNv7gV2aSAky3LuLg6Zb357PTwgkYibghdWYNs9#didcommmessaging-0",
      "type": "DIDCommMessaging",
      "serviceEndpoint": "didcomm://queue",
      "accept": [
        "didcomm/v2"
      ],
      "routingKeys": []
    }
  ],
  "alsoKnownAs": [
    "did:static:z5pU4iAPY5v6yrYBMmKjWANNaEdMeV7So7Hor8aynbHpJ47zj3DX6CqjQUAqjHiu4jr6HWFuNzjGcyHzJw3oUfcx5umudmV5H3mArhV4B3ibRgT1dN9H6XifZpaUFuZpeYx8SroRXKncvZhhaBRXBBQ36emZYZ9GuFuqR8C2F5p7ZGGnWiMFqbWckNq1wbbBUxMn4aowDRmcYUKAqZ3VCELRtmoz6PRkMDLo4ZR8Yvo3wwosphukawM2MkNyB1V3aimpAtGG8uiMvShR4Mm2rXn89DAE2u92jNwg2GZ4sCp5xp1tAyAusqUp9f4cbzKQSGsB7RreAVN7Wcox7dvjFUGpDsBEfQ7XbryZmMUfSJ8VPfRB9qhDaLBWF"
  ],
  "id": "did:hash:zQmcpMXmeNv7gV2aSAky3LuLg6Zb357PTwgkYibghdWYNs9"
}
```
