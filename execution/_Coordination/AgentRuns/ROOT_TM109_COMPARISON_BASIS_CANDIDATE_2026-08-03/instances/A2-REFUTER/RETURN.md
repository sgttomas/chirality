# A2-REFUTER return — TM109-A identity/provenance envelope candidate

Status: `COMPLETED — INDEPENDENT REFUTATION EVIDENCE ONLY; NOT ACCEPTANCE`

RunID: `ROOT_TM109_COMPARISON_BASIS_CANDIDATE_2026-08-03`

Parent: `HELPS_HUMANS`

Repository basis: `88e7590d3664d4f1daf91bed2a8899bda0748b92`

## Verdict

`PASS_WITH_NONBLOCKING_FINDINGS`

No concrete breach of the signed TM109-A scope and no defect that prevents
later exact semantic review was found. The frozen candidate remains an
identity/provenance carrier only; it does not define or imply generic equality,
mapping, normalization, tolerance evaluation, conformance, compatibility,
engineering meaning, privacy meaning, professional meaning, or human-review
meaning.

One repairable documentary mismatch exists in `FIELD_INVENTORY.csv`: reused
identity/reference/hash subfields are not fully inventoried, and three optional
array properties are described as `zero-or-more` even though the schema
requires at least one item whenever those properties are present. The schema
itself is unambiguous, so this does not prevent exact semantic review, but the
inventory should be repaired before package freezing.

Completion of this return is read-only refutation evidence. It is not semantic
acceptance, implementation authority, conformance, compatibility, or reliance
authority.

## Launch hash verification

All frozen inputs matched the sealed launch brief before inspection:

| File | Expected and observed SHA-256 | Result |
|---|---|---|
| `ENVELOPE_CANDIDATE.md` | `154f408e1daaff8462eac76a03c7a95e27e1a9eb7e17173e85c4ed8b4b080d41` | PASS |
| `ENVELOPE_SCHEMA_CANDIDATE.json` | `64e475fed163c668300a8d5b8291748a490fa661f22b29bdf08c8d1d368c144d` | PASS |
| `FIELD_INVENTORY.csv` | `cc53cce5b7d9c8013a6ec074ddbf0c9d8575f22f2e29c6d506d8d74c6615b7a7` | PASS |
| `COMPATIBILITY_ADJACENCY.md` | `694142cc3bd2d60f1f5d71f132923cda4e218fd47914d9c859750ac79f33e98c` | PASS |
| `CONFORMANCE_AND_NEGATIVE_CASES.md` | `fcd9e978ba7f6263492cbe0358fc49bd319fd34d633874429f3709912d414de7` | PASS |
| `OPEN_DECISIONS.md` | `753224dd99b055c516cea3a81480e19a66c65a975bb35a1fddbaafc663e2deb9` | PASS |
| `NEXT_HUMAN_ACCEPTANCE_FORM.md` | `cd3a45d409a140cc27a2fd5d0b7333c79540b49d788117625f2eca10c9619c77` | PASS |
| `instances/A2-AUTHOR/RETURN.md` | `0f70c310e84e8f58ddde0ba5520ec620a3cf67f457843c270e6c5370762800f8` | PASS |

`git rev-parse HEAD` returned the sealed repository basis exactly. No moving
candidate was inspected.

## Findings

### RF-109-01 — nonblocking — field inventory does not fully mirror reused shapes

Evidence:

- `FIELD_INVENTORY.csv` rows 28-29 summarize `VersionedIdentity.version` and
  `.hash` through wildcard paths, but there is no reusable
  `VersionedIdentity.id` row for diagnostic source, provenance source,
  claimant, or caller identities.
- Rows 34-35 summarize reusable opaque-reference version/hash properties but
  do not inventory the reusable `OpaqueGovernedReference.id` path applicable
  to evidence and provenance references.
- Rows 29 and 35 name reused `HashDescriptor` objects but do not inventory
  their conditional `algorithm`, `canonicalizationMethodId`, `payloadScopeId`,
  and `digest` subfields. Only basis and subject hash descendants are expanded
  at rows 6-9 and 14-17.
- Rows 13, 43, and 44 describe `subjects[].subjectHashes`,
  `diagnostics[].affectedSubjectIds`, and
  `diagnostics[].evidenceReferences` as `zero-or-more`. The schema makes each
  property optional but applies `minItems: 1` when present
  (`ENVELOPE_SCHEMA_CANDIDATE.json` lines 159-165, 253-265). The exact
  cardinality is therefore absent-or-one-or-more, not a present empty array.

Impact:

The authoritative candidate shape remains determinable from the JSON Schema,
and the prose carrier accurately describes the reused shapes. Consequently the
defect does not prevent later exact semantic review. It does make the field
inventory incomplete as an independent required/optional/conditional
companion and could mislead a reviewer or fixture author about empty optional
arrays.

Recommended in-scope repair:

Expand reusable identity, opaque-reference, and hash-descriptor descendants in
`FIELD_INVENTORY.csv`, or introduce explicit type-qualified wildcard rows that
cover every reuse. Change the three optional-array cardinalities to state
`absent-or-one-or-more` (or an equally exact convention). Reparse the CSV and
recompute all frozen/package hashes after repair.

### RF-109-02 — informational — no installed draft-2020-12 validator

Neither Python `jsonschema` nor a locally installed Ajv 2020 module was
available. Lockfiles mention Ajv, but no corresponding `node_modules` package
was installed. No dependency was installed and no validator was elevated into
semantic authority. This is already preserved as open decision `OD109-15` and
is not a preparation defect.

A read-only mechanical checker independently exercised the candidate keywords
used here (`$ref`, `type`, `required`, `additionalProperties`, `minItems`,
`minLength`, `enum`, `format`, `items`, and `anyOf`). That evidence is reported
below and does not select a validator or format-assertion profile.

## Refutation-question assessment

| Question | Result | Evidence and assessment |
|---|---|---|
| 1. Identity/provenance-only field scope | PASS | Every schema field is an identity, opaque reference, claimant-asserted outcome/diagnostic, evidence, provenance, or timestamp carrier. Diagnostic severity remains a carried label with no generic precedence. |
| 2. Required field coverage | PASS | Basis ID/version/four-part hash; subject ID/version/hashes; consumer/operation/tool/sandbox/policy identities; opaque unit/tolerance refs; outcome/diagnostics/evidence/provenance; claimant/caller/timestamps; and `MISSING`, `INCOMPATIBLE`, `BUDGET_EXHAUSTED` are represented. |
| 3. Inventory/schema agreement | PASS WITH NONBLOCKING FINDING | Top-level required/optional/conditional shape agrees, but RF-109-01 identifies incomplete reused-subfield expansion and three imprecise optional-array cardinalities. |
| 4. JSON Schema and instances | PASS TO INSTALLED EXTENT | JSON parses; `$schema` names draft 2020-12; all local refs resolve; keyword/meta-shape checks pass; representative positive and negative instances behave as specified. No installed general validator was available. |
| 5. Canonical-hash boundary | PASS | `ENVELOPE_CANDIDATE.md` lines 53-66 and schema lines 101-124 require four described parts while selecting no algorithm/canonicalization/scope value and denying equality from digest text. |
| 6. Consumer-local semantics | PASS | The purpose fence, opaque-reference section, difference matrix, open-decision exclusions, and acceptance template preserve equality, mapping, normalization, units/dimensions, tolerances, solver/rule, engineering, privacy, professional, and human-review meaning locally. |
| 7. Cross-consumer inference attack | PASS | No example, enum, adjacency statement, or option authorizes a cross-consumer match/conform/compatibility inference. `INCOMPATIBLE` is repeatedly identified as claimant-asserted under consumer-local rules. |
| 8. Root/App/Piping separation and support | PASS | `COMPATIBILITY_ADJACENCY.md` separates the three surfaces. Root source hashes and cited vocabulary/gaps match; App strict replay fields are supported by D-APP-84 R1; Piping section 6 and E-11/E-13/E-18/E-19 support the local comparison boundary. |
| 9. Structural and inference attacks | PASS | Cases cover identical envelopes; matching four-part hashes; opaque unit/tolerance refs; sandbox/policy/tool claims; evidence; claimant; timestamp; and specific Piping/App/Root inference attacks N-16/N-17/N-18. |
| 10. Human interface | PASS | The form is unsigned, contains unresolved post-refutation hash placeholders, supplies bounded accept/return/defer/decline options, and expressly stops before implementation and prohibited effects. |
| 11. Authority, drift, containment, Git | PASS | Evidence classes and hashes are calibrated. The current register differs after sibling ruling application, while `git show 88e7590d...:REGISTER.csv` reproduces the manifest hash exactly. The author return discloses this post-intake drift. This refuter wrote only this return and did not alter Git. |

## Deterministic checks and command results

| Check | Result |
|---|---|
| Candidate and author-return SHA-256 values against launch brief | PASS — 8/8 exact |
| Repository `HEAD` against sealed basis | PASS — `88e7590d3664d4f1daf91bed2a8899bda0748b92` |
| Signed ruling, decision interface, Piping/App evidence, Piping E-11/E-13/E-18/E-19, Root compatibility candidates, and Root runtime source hashes against manifest | PASS |
| Current live register against intake manifest hash | EXPECTED POST-INTAKE DRIFT — current `c0b61ca5c6ddab44c8ea782997d5f1108e2ee7959d546220284a02c2ce0a3dbe`; sealed-basis blob `1b9634934d35de8facc32dcb1881bd61a2559b1b4fa72b6da9cee21a6b06144f` exact |
| JSON parse | PASS |
| Local draft/meta-shape and `$ref` resolution check | PASS |
| CSV parse/header/row-width | PASS — expected 7-column header; 52 data rows |
| Candidate example parse and structural check | PASS |
| Positive variations | PASS — operation-only example, tool-only, both operation/tool, multiple subject hashes, and each explicit `MISSING`/`INCOMPATIBLE`/`BUDGET_EXHAUSTED` status |
| Negative variations | PASS — all 14 derived cases rejected: incomplete basis, digest-only hash, empty subjects, missing subject ID, no activity ID, missing sandbox, undeclared property, rule-shaped unit ref, unknown status, empty evidence, empty provenance, incomplete provenance, missing claimant, malformed timestamp |
| Trailing whitespace in seven candidate artifacts | PASS |
| Write containment | PASS — only `instances/A2-REFUTER/RETURN.md` written by this refuter |

The local mechanical checker is test evidence only. It is not an adopted JSON
Schema validator, format profile, or semantic authority.

## Boundary and claim-fence assessment

The strongest adversarial readings fail:

- equal IDs, versions, four-part hash text, reference text, timestamps, or
  whole-envelope bytes do not imply semantic equality;
- structural validity does not imply that evidence exists, hashes recompute,
  identities resolve, a tool was authorized, a sandbox contained execution, or
  an outcome is true;
- `SUCCEEDED` does not establish conformance, engineering acceptance, human
  acceptance, or reliance;
- `INCOMPATIBLE` does not establish Root-wide or cross-consumer incompatibility;
- the carrier does not satisfy Root runtime preflight/binding, App parity or
  resume, or Piping comparison contracts; and
- later acceptance of these exact design bytes would still not authorize
  implementation, lifecycle, release, publication, or affected-client use.

No candidate text was found that reasonably reverses those fences.

## Residual human decisions

All `OD109-01` through `OD109-16` choices remain unresolved. In particular,
the accountable human must still decide the exact field requirements, outcome
vocabulary, validator/version and date-time assertion behavior, trust/evidence
profile, extension/evolution policy, and whether to accept, return, defer, or
decline the final post-refutation exact bytes.

Before that interface is presented, HELPS_HUMANS should disposition
RF-109-01, freeze the resulting package, compute its exact package hash, and
replace every placeholder in `NEXT_HUMAN_ACCEPTANCE_FORM.md`. No implementation
tranche may begin from this return.
