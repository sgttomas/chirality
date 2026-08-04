# Validation report — TM109-A identity/provenance envelope candidate

- RunID: `ROOT_TM109_COMPARISON_BASIS_CANDIDATE_2026-08-03`
- Manager: `HELPS_HUMANS`
- Repository basis and final `HEAD`: `88e7590d3664d4f1daf91bed2a8899bda0748b92`
- Ruling transcript SHA-256: `66b967008f67934b08383291e68ef0af9923463d749cac9dbe7a74090e9cbb06`
- Post-refutation semantic-package SHA-256: `2cec641d89ef45a1e920c77c5ea99a8e5d26c7102b43d89cc65ab2eca949e489`
- Verdict: `PASS — STRUCTURAL/CALIBRATION VALIDATION; SEMANTIC ACCEPTANCE PENDING`

## Fan-in and repair

The author returned seven candidate artifacts and a durable return. The fresh
read-only refuter verified all eight frozen author hashes and returned
`PASS_WITH_NONBLOCKING_FINDINGS` at SHA-256
`1a2afa6b3304181203e124b9c430635b1cc37bedadf445cd6204cd609ecbbecb`.
Its sole repair request, RF-109-01, was applied to `FIELD_INVENTORY.csv`:

- optional non-empty arrays now say `absent-or-one-or-more`; and
- reusable `VersionedIdentity`, `OpaqueGovernedReference`, and their
  `HashDescriptor` descendants are explicitly inventoried.

The repaired inventory SHA-256 is
`d64635e66836d55b6c918e71d70c672ea27998e2dd52a50dbbafefba38be2929`.
No schema or substantive envelope field changed after refutation.

## Deterministic results

| Check | Result |
|---|---|
| Signed ruling transcript against declared SHA-256 | PASS — exact |
| All evidence-manifest inputs except the known live-register path | PASS — 18/18 exact current bytes |
| Launch-time live-register blob at repository basis | PASS — `git show 88e7590d...:REGISTER.csv` hashes to `1b963493...44f` |
| Current register drift | EXPECTED — sibling Task Management applied the signed ruling after launch; not consumed as candidate semantics |
| JSON parse and draft identifier | PASS — draft 2020-12 candidate parses |
| Schema root/object closure, local refs, required fields, activity `anyOf`, and explicit outcomes | PASS |
| CSV parse/header/row width/unique paths | PASS — 62 data rows |
| Inventory/schema required, optional, conditional, reused-shape, and optional-array agreement | PASS after RF-109-01 repair |
| Candidate example JSON parse and bounded shape assertions | PASS |
| Post-refutation manifest: six semantic files against listed hashes | PASS — 6/6 exact |
| Post-refutation manifest SHA-256 | PASS — `2cec641d...e489` |
| Human acceptance form package-hash binding | PASS — exact hash in all four response templates and package line |
| Stale post-refutation placeholders | PASS — none |
| Boundary vocabulary: equality, mapping, normalization, tolerance, solver/rule, engineering, privacy, professional, human review, compatibility, implementation | PASS — explicit preserved/prohibited fences |
| Root runtime / App / Piping adjacency separation | PASS |
| Structural and negative cases, including identical-envelope inference | PASS |
| `git diff --check` for this RunID | PASS |
| Write containment | PASS — all carrier writes are inside this RunID |
| Git preservation | PASS — no stage, commit, push, reset, merge, or branch act by this carrier; `HEAD` unchanged |

## Schema-validator boundary

No installed general draft-2020-12 validator was available. Author, refuter,
and manager independently parsed the schema and exercised its used keywords,
local references, representative positive instances, and negative cases. This
is adequate structural preparation evidence, not selection of an
authoritative validator. `OD109-15` correctly preserves validator/version and
format-assertion selection for a later human-gated contract/implementation
act.

## Authority and claim calibration

- The output is a non-authoritative candidate governed record.
- Structural validity means only that bytes fit the candidate carrier shape.
- `INCOMPATIBLE` remains a claimant-asserted consumer-local label, not a Root
  or cross-consumer compatibility computation.
- Matching IDs, versions, hashes, opaque references, timestamps, outcomes, or
  entire envelopes support no generic match, conform, or compatible claim.
- Unit/tolerance references remain opaque; Piping and all consumers retain
  equality, mapping, normalization, solver/rule, engineering, privacy,
  professional, and human-review semantics.
- Acceptance of the prepared design option would not authorize implementation,
  affected-client use, lifecycle, release, publication, or reliance.

No register, notice, App/Piping, lifecycle, source, test, decomposition, or Git
effect was taken by this carrier.

