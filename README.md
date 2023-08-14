# Static DID Method

`did:static` is a statically resolvable DID method. The DID itself, plus the
application of some encoding/decoding rules, _is_ the DID Document. The encoding
rules will generally do a pretty good job of compressing an average DID Document.
However, `did:static`DIDs will still be pretty long. To address this in
situations where DID size can be problematic, `did:static` DIDs always resolve to
documents containing an `alsoKnownAs` to a `did:hash` DID. This DID is a hash
of the `did:static` (or rather, over the bytes encoded in the method specific
identifier). The `did:hash` DID should be considered an alias to the
`did:static` DID. The DID itself is not independently resolvable but for users
who want to be able to use the shorthand of a `did:static`, they should store a
mapping from the `did:hash` DID to the `did:static` DID. Read more in [Also
Known As](#also-known-as).

#### Example DID:
```
did:static:z6Szgfc8oKodkFz5URq5eNRNW7ZPUq5gwQcF9CDA9TMD7SSq2dgaBNpArJ4bzkXDTAHTydL7imPge541AGNFCEZc4f7dLvKFVRwrdFUiSDJykUmLh1GHUxfcYKxvtUDKsSPVDKnJjUHhPbRTEeFKTQdxsyUc4rqSXREX1tGGeJ6DeGq3GgJ1vAf3b92727rfgiZDBtNYMKz3uJp932p8nt9RkdKMaeGk9x5v3ia4nHQwnCWDkm488wVT4GTkpkdZUxkgtKnudiLP3BAhsoaDJo7r9V1iZXGKLLqKsQYVpaUshi6riamno2TphNbJxYjDgeYGp2BoYhyYDUEb
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

- **Encode options:** replace terms: False, index: False, flatten keys: False
    - **Encoded (including `did:static:`):** 904
    - **Decoded (plain json string, no whitespace):** 732
    - **Decoded (plain json string, with whitespace):** 769
    - **Decoded Base 58 (json string, no whitespace):** 1000
    - **Decoded Base 64 url (json string, no whitespace):** 976
    - **Compression (encoded / decoded b64):** 92.62%
- **Encode options:** replace terms: False, index: False, flatten keys: True
    - **Encoded (including `did:static:`):** 866
    - **Decoded (plain json string, no whitespace):** 732
    - **Decoded (plain json string, with whitespace):** 769
    - **Decoded Base 58 (json string, no whitespace):** 1000
    - **Decoded Base 64 url (json string, no whitespace):** 976
    - **Compression (encoded / decoded b64):** 88.73%
- **Encode options:** replace terms: False, index: True, flatten keys: False
    - **Encoded (including `did:static:`):** 882
    - **Decoded (plain json string, no whitespace):** 732
    - **Decoded (plain json string, with whitespace):** 769
    - **Decoded Base 58 (json string, no whitespace):** 1000
    - **Decoded Base 64 url (json string, no whitespace):** 976
    - **Compression (encoded / decoded b64):** 90.37%
- **Encode options:** replace terms: False, index: True, flatten keys: True
    - **Encoded (including `did:static:`):** 844
    - **Decoded (plain json string, no whitespace):** 732
    - **Decoded (plain json string, with whitespace):** 769
    - **Decoded Base 58 (json string, no whitespace):** 1000
    - **Decoded Base 64 url (json string, no whitespace):** 976
    - **Compression (encoded / decoded b64):** 86.48%
- **Encode options:** replace terms: True, index: False, flatten keys: False
    - **Encoded (including `did:static:`):** 369
    - **Decoded (plain json string, no whitespace):** 732
    - **Decoded (plain json string, with whitespace):** 769
    - **Decoded Base 58 (json string, no whitespace):** 1000
    - **Decoded Base 64 url (json string, no whitespace):** 976
    - **Compression (encoded / decoded b64):** 37.81%
- **Encode options:** replace terms: True, index: False, flatten keys: True
    - **Encoded (including `did:static:`):** 331
    - **Decoded (plain json string, no whitespace):** 732
    - **Decoded (plain json string, with whitespace):** 769
    - **Decoded Base 58 (json string, no whitespace):** 1000
    - **Decoded Base 64 url (json string, no whitespace):** 976
    - **Compression (encoded / decoded b64):** 33.91%
- **Encode options:** replace terms: True, index: True, flatten keys: False
    - **Encoded (including `did:static:`):** 347
    - **Decoded (plain json string, no whitespace):** 732
    - **Decoded (plain json string, with whitespace):** 769
    - **Decoded Base 58 (json string, no whitespace):** 1000
    - **Decoded Base 64 url (json string, no whitespace):** 976
    - **Compression (encoded / decoded b64):** 35.55%
- **Encode options:** replace terms: True, index: True, flatten keys: True
    - **Encoded (including `did:static:`):** 309
    - **Decoded (plain json string, no whitespace):** 732
    - **Decoded (plain json string, with whitespace):** 769
    - **Decoded Base 58 (json string, no whitespace):** 1000
    - **Decoded Base 64 url (json string, no whitespace):** 976
    - **Compression (encoded / decoded b64):** 31.66%

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
      "id": "did:static:z6Szgfc8oKodkFz5URq5eNRNW7ZPUq5gwQcF9CDA9TMD7SSq2dgaBNpArJ4bzkXDTAHTydL7imPge541AGNFCEZc4f7dLvKFVRwrdFUiSDJykUmLh1GHUxfcYKxvtUDKsSPVDKnJjUHhPbRTEeFKTQdxsyUc4rqSXREX1tGGeJ6DeGq3GgJ1vAf3b92727rfgiZDBtNYMKz3uJp932p8nt9RkdKMaeGk9x5v3ia4nHQwnCWDkm488wVT4GTkpkdZUxkgtKnudiLP3BAhsoaDJo7r9V1iZXGKLLqKsQYVpaUshi6riamno2TphNbJxYjDgeYGp2BoYhyYDUEb#6LSqPZfn",
      "type": "X25519KeyAgreementKey2020",
      "publicKeyMultibase": "z6LSqPZfn9krvgXma2icTMKf2uVcYhKXsudCmPoUzqGYW24U",
      "controller": "did:static:z6Szgfc8oKodkFz5URq5eNRNW7ZPUq5gwQcF9CDA9TMD7SSq2dgaBNpArJ4bzkXDTAHTydL7imPge541AGNFCEZc4f7dLvKFVRwrdFUiSDJykUmLh1GHUxfcYKxvtUDKsSPVDKnJjUHhPbRTEeFKTQdxsyUc4rqSXREX1tGGeJ6DeGq3GgJ1vAf3b92727rfgiZDBtNYMKz3uJp932p8nt9RkdKMaeGk9x5v3ia4nHQwnCWDkm488wVT4GTkpkdZUxkgtKnudiLP3BAhsoaDJo7r9V1iZXGKLLqKsQYVpaUshi6riamno2TphNbJxYjDgeYGp2BoYhyYDUEb"
    },
    {
      "id": "did:static:z6Szgfc8oKodkFz5URq5eNRNW7ZPUq5gwQcF9CDA9TMD7SSq2dgaBNpArJ4bzkXDTAHTydL7imPge541AGNFCEZc4f7dLvKFVRwrdFUiSDJykUmLh1GHUxfcYKxvtUDKsSPVDKnJjUHhPbRTEeFKTQdxsyUc4rqSXREX1tGGeJ6DeGq3GgJ1vAf3b92727rfgiZDBtNYMKz3uJp932p8nt9RkdKMaeGk9x5v3ia4nHQwnCWDkm488wVT4GTkpkdZUxkgtKnudiLP3BAhsoaDJo7r9V1iZXGKLLqKsQYVpaUshi6riamno2TphNbJxYjDgeYGp2BoYhyYDUEb#6MkrCD1c",
      "type": "Ed25519VerificationKey2020",
      "publicKeyMultibase": "z6MkrCD1csqtgdj8sjrsu8jxcbeyP6m7LiK87NzhfWqio5yr",
      "controller": "did:static:z6Szgfc8oKodkFz5URq5eNRNW7ZPUq5gwQcF9CDA9TMD7SSq2dgaBNpArJ4bzkXDTAHTydL7imPge541AGNFCEZc4f7dLvKFVRwrdFUiSDJykUmLh1GHUxfcYKxvtUDKsSPVDKnJjUHhPbRTEeFKTQdxsyUc4rqSXREX1tGGeJ6DeGq3GgJ1vAf3b92727rfgiZDBtNYMKz3uJp932p8nt9RkdKMaeGk9x5v3ia4nHQwnCWDkm488wVT4GTkpkdZUxkgtKnudiLP3BAhsoaDJo7r9V1iZXGKLLqKsQYVpaUshi6riamno2TphNbJxYjDgeYGp2BoYhyYDUEb"
    }
  ],
  "authentication": [
    "did:static:z6Szgfc8oKodkFz5URq5eNRNW7ZPUq5gwQcF9CDA9TMD7SSq2dgaBNpArJ4bzkXDTAHTydL7imPge541AGNFCEZc4f7dLvKFVRwrdFUiSDJykUmLh1GHUxfcYKxvtUDKsSPVDKnJjUHhPbRTEeFKTQdxsyUc4rqSXREX1tGGeJ6DeGq3GgJ1vAf3b92727rfgiZDBtNYMKz3uJp932p8nt9RkdKMaeGk9x5v3ia4nHQwnCWDkm488wVT4GTkpkdZUxkgtKnudiLP3BAhsoaDJo7r9V1iZXGKLLqKsQYVpaUshi6riamno2TphNbJxYjDgeYGp2BoYhyYDUEb#6MkrCD1c"
  ],
  "assertionMethod": [
    "did:static:z6Szgfc8oKodkFz5URq5eNRNW7ZPUq5gwQcF9CDA9TMD7SSq2dgaBNpArJ4bzkXDTAHTydL7imPge541AGNFCEZc4f7dLvKFVRwrdFUiSDJykUmLh1GHUxfcYKxvtUDKsSPVDKnJjUHhPbRTEeFKTQdxsyUc4rqSXREX1tGGeJ6DeGq3GgJ1vAf3b92727rfgiZDBtNYMKz3uJp932p8nt9RkdKMaeGk9x5v3ia4nHQwnCWDkm488wVT4GTkpkdZUxkgtKnudiLP3BAhsoaDJo7r9V1iZXGKLLqKsQYVpaUshi6riamno2TphNbJxYjDgeYGp2BoYhyYDUEb#6MkrCD1c"
  ],
  "keyAgreement": [
    "did:static:z6Szgfc8oKodkFz5URq5eNRNW7ZPUq5gwQcF9CDA9TMD7SSq2dgaBNpArJ4bzkXDTAHTydL7imPge541AGNFCEZc4f7dLvKFVRwrdFUiSDJykUmLh1GHUxfcYKxvtUDKsSPVDKnJjUHhPbRTEeFKTQdxsyUc4rqSXREX1tGGeJ6DeGq3GgJ1vAf3b92727rfgiZDBtNYMKz3uJp932p8nt9RkdKMaeGk9x5v3ia4nHQwnCWDkm488wVT4GTkpkdZUxkgtKnudiLP3BAhsoaDJo7r9V1iZXGKLLqKsQYVpaUshi6riamno2TphNbJxYjDgeYGp2BoYhyYDUEb#6LSqPZfn"
  ],
  "capabilityInvocation": [
    "did:static:z6Szgfc8oKodkFz5URq5eNRNW7ZPUq5gwQcF9CDA9TMD7SSq2dgaBNpArJ4bzkXDTAHTydL7imPge541AGNFCEZc4f7dLvKFVRwrdFUiSDJykUmLh1GHUxfcYKxvtUDKsSPVDKnJjUHhPbRTEeFKTQdxsyUc4rqSXREX1tGGeJ6DeGq3GgJ1vAf3b92727rfgiZDBtNYMKz3uJp932p8nt9RkdKMaeGk9x5v3ia4nHQwnCWDkm488wVT4GTkpkdZUxkgtKnudiLP3BAhsoaDJo7r9V1iZXGKLLqKsQYVpaUshi6riamno2TphNbJxYjDgeYGp2BoYhyYDUEb#6MkrCD1c"
  ],
  "capabilityDelegation": [
    "did:static:z6Szgfc8oKodkFz5URq5eNRNW7ZPUq5gwQcF9CDA9TMD7SSq2dgaBNpArJ4bzkXDTAHTydL7imPge541AGNFCEZc4f7dLvKFVRwrdFUiSDJykUmLh1GHUxfcYKxvtUDKsSPVDKnJjUHhPbRTEeFKTQdxsyUc4rqSXREX1tGGeJ6DeGq3GgJ1vAf3b92727rfgiZDBtNYMKz3uJp932p8nt9RkdKMaeGk9x5v3ia4nHQwnCWDkm488wVT4GTkpkdZUxkgtKnudiLP3BAhsoaDJo7r9V1iZXGKLLqKsQYVpaUshi6riamno2TphNbJxYjDgeYGp2BoYhyYDUEb#6MkrCD1c"
  ],
  "service": [
    {
      "id": "did:static:z6Szgfc8oKodkFz5URq5eNRNW7ZPUq5gwQcF9CDA9TMD7SSq2dgaBNpArJ4bzkXDTAHTydL7imPge541AGNFCEZc4f7dLvKFVRwrdFUiSDJykUmLh1GHUxfcYKxvtUDKsSPVDKnJjUHhPbRTEeFKTQdxsyUc4rqSXREX1tGGeJ6DeGq3GgJ1vAf3b92727rfgiZDBtNYMKz3uJp932p8nt9RkdKMaeGk9x5v3ia4nHQwnCWDkm488wVT4GTkpkdZUxkgtKnudiLP3BAhsoaDJo7r9V1iZXGKLLqKsQYVpaUshi6riamno2TphNbJxYjDgeYGp2BoYhyYDUEb#didcommmessaging-0",
      "type": "DIDCommMessaging",
      "serviceEndpoint": "didcomm://queue",
      "accept": [
        "didcomm/v2"
      ],
      "routingKeys": []
    }
  ],
  "id": "did:static:z6Szgfc8oKodkFz5URq5eNRNW7ZPUq5gwQcF9CDA9TMD7SSq2dgaBNpArJ4bzkXDTAHTydL7imPge541AGNFCEZc4f7dLvKFVRwrdFUiSDJykUmLh1GHUxfcYKxvtUDKsSPVDKnJjUHhPbRTEeFKTQdxsyUc4rqSXREX1tGGeJ6DeGq3GgJ1vAf3b92727rfgiZDBtNYMKz3uJp932p8nt9RkdKMaeGk9x5v3ia4nHQwnCWDkm488wVT4GTkpkdZUxkgtKnudiLP3BAhsoaDJo7r9V1iZXGKLLqKsQYVpaUshi6riamno2TphNbJxYjDgeYGp2BoYhyYDUEb",
  "alsoKnownAs": [
    "did:hash:zQmYo5LVNawAdSah8d2inFWFhvCg3eqPiddkzdYx1umJtUx"
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
      "id": "did:hash:zQmYo5LVNawAdSah8d2inFWFhvCg3eqPiddkzdYx1umJtUx#6LSqPZfn",
      "type": "X25519KeyAgreementKey2020",
      "publicKeyMultibase": "z6LSqPZfn9krvgXma2icTMKf2uVcYhKXsudCmPoUzqGYW24U",
      "controller": "did:hash:zQmYo5LVNawAdSah8d2inFWFhvCg3eqPiddkzdYx1umJtUx"
    },
    {
      "id": "did:hash:zQmYo5LVNawAdSah8d2inFWFhvCg3eqPiddkzdYx1umJtUx#6MkrCD1c",
      "type": "Ed25519VerificationKey2020",
      "publicKeyMultibase": "z6MkrCD1csqtgdj8sjrsu8jxcbeyP6m7LiK87NzhfWqio5yr",
      "controller": "did:hash:zQmYo5LVNawAdSah8d2inFWFhvCg3eqPiddkzdYx1umJtUx"
    }
  ],
  "authentication": [
    "did:hash:zQmYo5LVNawAdSah8d2inFWFhvCg3eqPiddkzdYx1umJtUx#6MkrCD1c"
  ],
  "assertionMethod": [
    "did:hash:zQmYo5LVNawAdSah8d2inFWFhvCg3eqPiddkzdYx1umJtUx#6MkrCD1c"
  ],
  "keyAgreement": [
    "did:hash:zQmYo5LVNawAdSah8d2inFWFhvCg3eqPiddkzdYx1umJtUx#6LSqPZfn"
  ],
  "capabilityInvocation": [
    "did:hash:zQmYo5LVNawAdSah8d2inFWFhvCg3eqPiddkzdYx1umJtUx#6MkrCD1c"
  ],
  "capabilityDelegation": [
    "did:hash:zQmYo5LVNawAdSah8d2inFWFhvCg3eqPiddkzdYx1umJtUx#6MkrCD1c"
  ],
  "service": [
    {
      "id": "did:hash:zQmYo5LVNawAdSah8d2inFWFhvCg3eqPiddkzdYx1umJtUx#didcommmessaging-0",
      "type": "DIDCommMessaging",
      "serviceEndpoint": "didcomm://queue",
      "accept": [
        "didcomm/v2"
      ],
      "routingKeys": []
    }
  ],
  "alsoKnownAs": [
    "did:static:z6Szgfc8oKodkFz5URq5eNRNW7ZPUq5gwQcF9CDA9TMD7SSq2dgaBNpArJ4bzkXDTAHTydL7imPge541AGNFCEZc4f7dLvKFVRwrdFUiSDJykUmLh1GHUxfcYKxvtUDKsSPVDKnJjUHhPbRTEeFKTQdxsyUc4rqSXREX1tGGeJ6DeGq3GgJ1vAf3b92727rfgiZDBtNYMKz3uJp932p8nt9RkdKMaeGk9x5v3ia4nHQwnCWDkm488wVT4GTkpkdZUxkgtKnudiLP3BAhsoaDJo7r9V1iZXGKLLqKsQYVpaUshi6riamno2TphNbJxYjDgeYGp2BoYhyYDUEb"
  ],
  "id": "did:hash:zQmYo5LVNawAdSah8d2inFWFhvCg3eqPiddkzdYx1umJtUx"
}
```
