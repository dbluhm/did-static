# Static DID Method

#### Example DID:
```
did:static:z5pU4iAPY5v6yrYBMmKjWANNaEdMeV7So7Hor8aynbHpJ47zj3DX6CqjQUAqjHiu4jr6HWFuNzjGcyHzJw3oUfcx5umudmV5H3mArhV4B3ibRgT1dN9H6XifZpaUFuZpeYx8SroRXKncvZhhaBRXBBQ36emZYZ9GuFuqR8C2F5p7ZGGnWiMFqbWckNq1wbbBUxMn4aowDRmcYUKAqZ3VCELRtmoz6PRkMDLo4ZR8Yvo3wwosphukawM2MkNyB1V3aimpAtGG8uiMvShR4Mm2rXn89DAE2u92jNwg2GZ4sCp5xp1tAyAusqUp9f4cbzKQSGsB7RreAVN7Wcox7dvjFUGpDsBEfQ7XbryZmMUfSJ8VPfRB9qhDaLBWF
```

#### Example Input to `encode()`

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
- Encoded: 388 bytes
- Decoded: 769 bytes

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
