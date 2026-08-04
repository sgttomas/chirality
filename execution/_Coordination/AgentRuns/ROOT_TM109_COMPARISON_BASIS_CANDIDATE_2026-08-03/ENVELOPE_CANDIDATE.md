# TM109-A identity/provenance envelope candidate

Status: `NON-AUTHORITATIVE CANDIDATE — PREPARATION COMPLETE; SEMANTICS NOT ACCEPTED`

Candidate label: `chirality.identity-provenance-envelope/candidate-2026-08-03`

Repository basis: `88e7590d3664d4f1daf91bed2a8899bda0748b92`

Preparation authority: the signed `TM-ROOT-109 TM109-A` ruling in
`OWNER_RULING_TRANSCRIPT_2026-08-03.md`, SHA-256
`66b967008f67934b08383291e68ef0af9923463d749cac9dbe7a74090e9cbb06`.

## Non-authority and purpose fence

These bytes are a first exact candidate. They are not an accepted contract,
do not authorize implementation, and cannot support reliance. A later
accountable-human semantic-acceptance act over frozen exact bytes is required
before any implementation proposal may be prepared.

The envelope records identity and provenance only. It neither performs nor
authorizes equality, mapping, normalization, tolerance evaluation, semantic
comparison, conformance, or compatibility. It does not establish that any two
subjects, runs, consumers, operations, tools, sandboxes, policies, unit
systems, tolerance profiles, results, or envelopes match.

Piping and every other consumer retain locally all equality, mapping,
normalization, tolerances, solver/rule meaning, engineering meaning, privacy,
professional-boundary, and human-review semantics. `unitSystemReference` and
`toleranceProfileReference` are opaque governed references. Their presence,
absence, or identical spelling has no generic semantic effect.

## Candidate carrier shape

An envelope conforming structurally to the companion candidate schema has:

1. one comparison or evaluation `basis` with an ID, version, and described
   canonical hash;
2. one or more `subjects`, each with an ID and optionally a version and
   described hashes;
3. the identities of the consumer, sandbox, and policy, plus at least one of
   the operation or tool;
4. optional opaque unit-system and tolerance-profile references;
5. one carrier-level outcome label, diagnostics, evidence references, and
   provenance records;
6. claimant and caller identities; and
7. one timestamp.

All objects are closed against undeclared properties. Structural validity
means only that the carrier has the selected shape. It is not evidence that a
referenced object exists, that a digest is correct, that an outcome is true,
or that a consumer may make a comparison or compatibility claim.

## Hash descriptor

Every hash is a four-part description:

- `algorithm`: an opaque algorithm identifier;
- `canonicalizationMethodId`: an opaque identifier for the method used to
  produce canonical bytes;
- `payloadScopeId`: an opaque identifier for the exact payload scope; and
- `digest`: the resulting digest text.

This candidate deliberately does not choose JSON Canonicalization Scheme,
SHA-256, SHA-512, raw bytes, Unicode normalization, or any other canonical
serialization or digest algorithm. Identical digest text without exact,
consumer-accepted agreement on all four parts cannot establish equality.

## Identity objects

`consumerIdentity`, `operationIdentity`, `toolIdentity`, `sandboxIdentity`,
`policyIdentity`, `claimant`, and `caller` use the same minimal
versioned-identity carrier: required `id`, optional `version`, and optional
described `hash`. Reuse of the shape does not merge the meanings of those
identities.

At least one of `operationIdentity` or `toolIdentity` is required. This permits
an operation-only, tool-only, or operation-plus-tool record without inventing
generic operation/tool equivalence.

## Subjects

Each subject requires `subjectId`. `subjectVersion` and `subjectHashes` are
optional because the carrier must be able to report `MISSING` without
fabricating identity material. A consumer may impose stronger local
requirements. The generic schema does not decide which hash, version, or
combination is sufficient to identify a Piping model/run, an App session, or a
Root runtime artifact.

Array order is carriage order only. The schema defines no set equality,
pairing, left/right meaning, primary subject, or mapping relation.

## Opaque consumer-owned references

`unitSystemReference` and `toleranceProfileReference` reuse an opaque governed
reference shape: required `id`, optional `version`, optional described `hash`.
The generic envelope never dereferences them and never evaluates dimensional,
conversion, normalization, or tolerance rules. Consumers decide whether a
reference is known, admissible, current, suitable, or sufficient.

## Outcome and diagnostics

`outcome.status` is limited in this candidate to:

`SUCCEEDED`, `FAILED`, `DENIED`, `CANCELLED`, `INTERRUPTED`, `PARTIAL`,
`MISSING`, `INCOMPATIBLE`, and `BUDGET_EXHAUSTED`.

The last three ensure that missing identity material, consumer-declared
incompatibility, and budget exhaustion can be carried explicitly. These are
labels asserted by the identified claimant/caller under consumer-local rules.
The generic schema does not define their truth conditions, precedence,
retryability, terminality, engineering significance, or compatibility
meaning. In particular, `INCOMPATIBLE` is not a Root-computed cross-consumer
judgment.

Each diagnostic has a required `code` and `message`, with optional `severity`,
`sourceIdentity`, `affectedSubjectIds`, and `evidenceReferences`. Codes and
messages remain consumer-defined. The generic schema does not establish a
diagnostic taxonomy or turn a diagnostic into a professional or human ruling.

## Evidence, provenance, claimant, and caller

Top-level `evidenceReferences` are governed-reference carriers. Each
`provenance` record identifies a source and one or more evidence references;
an optional record timestamp may state when that provenance record was made.
Neither the schema nor an envelope validates external evidence.

`claimantCaller.claimant` identifies who or what asserts the envelope's
outcome and diagnostic content. `claimantCaller.caller` identifies who or what
requested or caused the recorded operation/tool activity. Identity does not
confer authorization, professional standing, approval, or acceptance.

## Candidate example

This example is structurally illustrative only. Its IDs and digests are
invented and it asserts no compatibility:

```json
{
  "basis": {
    "id": "consumer.example/basis",
    "version": "draft-7",
    "canonicalHash": {
      "algorithm": "example.digest.algorithm",
      "canonicalizationMethodId": "consumer.example/c14n-method",
      "payloadScopeId": "consumer.example/basis-payload",
      "digest": "invented-digest"
    }
  },
  "subjects": [
    {
      "subjectId": "subject-left",
      "subjectVersion": "17"
    },
    {
      "subjectId": "subject-right",
      "subjectHashes": [
        {
          "algorithm": "example.digest.algorithm",
          "canonicalizationMethodId": "consumer.example/c14n-method",
          "payloadScopeId": "consumer.example/subject-payload",
          "digest": "invented-subject-digest"
        }
      ]
    }
  ],
  "consumerIdentity": { "id": "consumer.example" },
  "operationIdentity": { "id": "consumer.example/compare-operation" },
  "sandboxIdentity": { "id": "sandbox-run-42" },
  "policyIdentity": { "id": "consumer.example/policy", "version": "3" },
  "unitSystemReference": { "id": "consumer.example/unit-system/SI" },
  "toleranceProfileReference": { "id": "consumer.example/tolerance/profile-9" },
  "outcome": { "status": "INCOMPATIBLE" },
  "diagnostics": [
    {
      "code": "CONSUMER_DEFINED_REASON",
      "message": "The consumer reports an incompatibility under its local rules.",
      "affectedSubjectIds": ["subject-left", "subject-right"]
    }
  ],
  "evidenceReferences": [
    { "id": "consumer.example/evidence/receipt-123" }
  ],
  "provenance": [
    {
      "sourceIdentity": { "id": "consumer.example/comparison-engine", "version": "5" },
      "evidenceReferences": [
        { "id": "consumer.example/evidence/receipt-123" }
      ]
    }
  ],
  "claimantCaller": {
    "claimant": { "id": "consumer.example/comparison-engine", "version": "5" },
    "caller": { "id": "consumer.example/user-or-service-identity" }
  },
  "timestamp": "2026-08-03T18:00:00Z"
}
```

The example's `INCOMPATIBLE` label is a consumer assertion. Another consumer
may not understand it, may reject its basis, or may reach a different result.
Even an exact byte-for-byte duplicate of this envelope supplies no generic
proof that the subjects are equal, conformant, or compatible.

## Companion artifacts

- `ENVELOPE_SCHEMA_CANDIDATE.json` — parseable JSON Schema candidate;
- `FIELD_INVENTORY.csv` — required/optional and opacity inventory;
- `COMPATIBILITY_ADJACENCY.md` — Root/App/Piping adjacency and differences;
- `CONFORMANCE_AND_NEGATIVE_CASES.md` — structural cases and forbidden claims;
- `OPEN_DECISIONS.md` — unresolved human semantic choices; and
- `NEXT_HUMAN_ACCEPTANCE_FORM.md` — bounded no-effect owner-return interface.

