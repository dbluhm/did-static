"""Terms Table for DID Static Method."""

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

ENC_TERMS = {term: index for index, term in enumerate(TERMS)}

DEC_TERMS = {index: term for index, term in enumerate(TERMS)}
