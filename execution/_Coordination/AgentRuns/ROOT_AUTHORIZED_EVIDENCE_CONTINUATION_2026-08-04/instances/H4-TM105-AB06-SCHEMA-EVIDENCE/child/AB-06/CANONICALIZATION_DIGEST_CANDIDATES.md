# Canonicalization and digest candidates

Status: `NON_AUTHORITATIVE_INCOMPLETE_CANDIDATE`

No serialization, canonicalization, digest algorithm, cryptographic profile,
domain separation, agility rule, payload scope, text encoding, correctness,
identity, equality, compatibility, migration, or support policy is selected.
Every selection field remains exact `TBD`; unsupported owner/vendor facts are
`UNKNOWN`.

## Current evidence

- `sha256(value: string | Buffer)` hashes the bytes supplied to Node and emits
  lowercase hex (`runtime/packages/core/src/fs.ts:53-55`).
- `atomicWriteJson` hashes nowhere itself and writes
  `JSON.stringify(value, null, 2) + LF`; `appendJsonLine` writes compact
  `JSON.stringify(value) + LF` (`runtime/packages/core/src/fs.ts:10-36`). These
  are two different current serializations, neither an accepted canonical
  profile.
- Auth tokens, project manifests, runtime fingerprints, brief/return records,
  artifact metadata and accepted package manifests carry SHA-256-shaped
  strings, but their payload scopes and byte construction vary
  (`auth-registry.ts:52-74`; `project-registry.ts:37-58`;
  `harness/types.ts:179-196`; `agent1-run-coordinator.ts:58-98`;
  `transcript-replay.ts:18-28`).
- TM109 accepts a four-part `HashDescriptor` only inside its bounded
  identity/provenance envelope. Algorithm, canonicalization method, payload
  scope, and digest remain opaque there; no equality or correctness follows
  (`FIELD_INVENTORY.csv`, `basis.canonicalHash.*`; TM109 `AUTHORITY_RECORD.md`).
- Accepted DEL compatibility bytes require exact hashes in a future complete
  binding manifest within DEL stewardship/recovery/compatibility scope. That
  does not select a common TM105 serialization or cryptographic policy
  (`ROOT_COMPATIBILITY_CONTRACT_CANDIDATE_V2.md`, “Compatibility binding
  record”; H2 AB-09 `RETURN.md` CN-08).

## Compared alternatives

| Alternative | Byte basis | Evidence-supported benefit | Unresolved cost/risk | Required later selections |
|---|---|---|---|---|
| Opaque original bytes | The exact pre-existing byte sequence; no reserialization | Preserves source bytes and avoids inventing a canonicalizer; adjacent to DEL byte-preservation and immutable-manifest practices in their own scope | Producers must define byte boundaries; semantically equivalent encodings remain byte-distinct; transport/storage transformations can alter bytes; text encodings are not normalized | Payload boundary/scope, acquisition API, retention, media/encoding metadata, algorithm, domain separation, authenticity, migration |
| UTF-8 JSON plus later-selected canonicalization profile | A later normative profile transforms a typed JSON value to UTF-8 bytes | Fits current JSON-facing contracts and can support independent implementations if every number/string/key/duplicate/member rule is frozen | Current pretty JSON and JSONL are not canonical; Unicode, number, negative zero, duplicate keys, member order, escaping, unsupported values, and schema evolution are unresolved | Exact JSON data model, validator/schema version, canonical profile/version, UTF-8 rules, payload scope, algorithm, domain separation, agility and version negotiation |
| Typed binary plus later-selected profile | A later schema and binary encoding/profile produce bytes | Can make types and field numbers explicit and may avoid some JSON ambiguities | No binary family/profile is present in declared evidence; unknown-field retention, canonical map order, default omission, schema registry, language libraries and migration are unproved | Binary family/version, schema ID, deterministic profile, unknown/default behavior, payload scope, algorithm, domain separation, cross-language and migration suite |

No alternative is preferred. `OPAQUE_ORIGINAL_BYTES` is not a claim that
original bytes are authentic or semantically correct. A JSON profile is not
selected by current `JSON.stringify`. A typed binary profile is a bounded
alternative only, not evidence that a binary dependency or platform is
available.

## Digest-reference structure

The structural vector separates:

- `alternative` and `payloadReference`;
- optional `algorithmId`;
- JSON `canonicalizationProfileId` or `binaryProfileId` only for their named
  alternatives;
- `payloadScopeId`, `domainSeparationId`, and `digestText`; and
- `allSelectionFieldsStatus: "TBD"`.

Names are opaque references, not endorsed values. The schema rejects a
canonicalization/binary profile claim on the opaque-original-bytes
alternative, and requires the relevant profile placeholder on the JSON/binary
alternatives. This validates structural separation only.

## Cross-language and migration evidence still required

A later sealed tranche must supply exact bytes plus expected digests for:
empty values; nested objects; key-order permutations; non-ASCII and combining
characters; escaped control characters; integers at each language-safe bound;
fractions, exponent forms and negative zero if permitted; absent/null/default
fields; arrays; unknown fields; duplicate-key rejection; invalid UTF-8;
schema-version changes; profile-version changes; algorithm agility;
domain/payload-scope separation; and old/new reader behavior. It must bind
each producing language/library/version and compare raw bytes before hashes.

The neutral vectors in this package deliberately use `TBD` rather than
invented digest text. They are schema vectors, not cryptographic golden values.
The no-TBD successor and byte gate remain ineligible under the owner transcript.
