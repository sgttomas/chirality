# D-PEC-74 — First actual P1 source slice

**Status:** RULED — O-A; DEL-08-02 CHECKING / EXACT BYTES ACCEPTED / LATER P1 CLOSED

**DecisionID:** D-PEC-74

**Date presented:** 2026-08-01

**Owner:** Ryan Tufts

**Owning loop:** PEC

**Presentation basis:** `5830546ab0912100f0f5b0c4b51ba788e5b9fb5a`

**Decision packet:**
`../D-PEC-74_FIRST_P1_SOURCE_SLICE_2026-08-01/PACKET.md`

**Structural precedent:** the exact-path, separate production/review/owner-gate
convention used by `D-PEC-72_p1_entry_foundation_slice.md`, narrowed here to
one selected P1 root and its first source-tree/profile fence.

## Question

Which exact dependency-lawful root should open PEC v2's first actual P1
source-production slice?

## Options

### O-A — DEL-08-02 API-contract canary (recommended)

Select only DEL-08-02, create the new projects/pec/v2/ tree with a PEC-local
JSON Schema draft-2020-12 API v1 contract and standard-library additive
compatibility tests, and create the exact registered-check profile at
projects/pec/software-workflow.json stated in the packet.

This is the smallest root aligned with the owner-selected PEC hexagonal style
and typed-contract intent. It does not select a service implementation
language, transport, server, store, runtime integration, or cross-loop
contract.

### O-B — DEL-01-06 local-loop-registry canary

Select only DEL-01-06, create the same v2 tree and profile roots, and implement
the P1 one-loop local registry default plus Python standard-library loader and
tests at the exact paths in the packet.

This is also an S-sized DAG root and gives directed bootstrap an early locator,
but commits PEC's first service module to Python before the language-neutral
API contract exists. OI-003's long-term registry home/shape remains open.

### O-C — Amend

State a different exact root/set, tree, profile, path, check, gate, or rollback
condition. Consequential amendments require packet revision before execution.

### O-D — Defer or decline

Leave all 29 P1 deliverables `INITIALIZED`; create no v2 source tree or profile;
keep `F-PEC-1` closed over source work.

## Common fence

The exact path lists, exact O-A/O-B profile JSON, allowed acts, prohibited
paths, verification, owner gates, bootstrap relationship, rollback, and
failure isolation are normative for this decision in the linked packet.

Until an option is ruled, this record creates no source authority. Under an
executable ruling, `F-PEC-1` opens only for that option's exact paths. No
artifact acceptance, lifecycle transition, `ISSUED`, later P1 node, release,
merge, professional reliance, or architecture mandate outside PEC is inferred.

## Recommendation

Rule **O-A**. DEL-08-02 is `INITIALIZED`, Context Envelope S, and a raw-DAG
root. It opens a typed, versioned PEC capability boundary without server,
store, transport, authentication, runtime-client, or cross-loop implementation.

## Owner ruling

Owner ruling recorded verbatim (2026-08-01, in-session, Ryan Tufts):

```text
D-PEC-74: O-A.
```

This selects only DEL-08-02 and opens only O-A's exact source-tree, profile,
run-record, and coordination paths under the packet's checks, rollback, human
gates, and non-effects. The frozen activation authority is
`../D-PEC-74_FIRST_P1_SOURCE_SLICE_2026-08-01/O-A_ACTIVATION_AUTHORITY_2026-08-01.md`.

Recording the ruling is not production. At this authority checkpoint no O-A
source path or profile exists, no deliverable-local file has changed, and no
artifact acceptance, lifecycle transition, `ISSUED`, later P1 node, release,
merge, professional reliance, or architecture mandate outside PEC is inferred.

## Production outcome — 2026-08-01

WORKING_ITEMS executed only the frozen O-A activation. The version-1 JSON
Schema contract, standard-library compatibility tests, three fixtures, exact
software-workflow profile, and two authorized deliverable run records now
exist. Both registered checks pass; the additive fixture passes, while the
removal and meaning-change fixtures fail with located explanations. Exact
hashes and validation evidence are recorded in
`../D-PEC-74_FIRST_P1_SOURCE_SLICE_2026-08-01/EXECUTION_HANDOFF.md`.

## Final review and acceptance outcome — 2026-08-01

PR #455 merged the Gate 1–2 SELF_CHECK evidence from exact source
`d99bf2ef923d640d956718b113f86c4755f837de`. The exact five-item checklist
records AC-001 through AC-005 satisfied and zero findings. Under the verbatim
final ruling in
`../D-PEC-74_FIRST_P1_SOURCE_SLICE_2026-08-01/DEL0802_FINAL_ACCEPTANCE_RULING_2026-08-01.md`,
the owner separately:

1. approved the lifecycle-only `INITIALIZED → CHECKING` Gate 5 transition
   under the recorded review-entry override;
2. confirmed AC-005's `DEL-08-02 → OBJ-001` attribution with its recorded
   `MEDIUM` confidence while leaving `OBJ-001;OBJ-004` and the full consumer
   set considered but unadopted; and
3. accepted only the exact schema, compatibility-test, and three fixture
   hashes recorded in the execution handoff.

DEL-08-02 is `CHECKING`, not `ISSUED`. No later P1 node, release, professional
reliance, or architecture mandate outside PEC is authorized. Any successor
source slice remains separately owner-packet-gated.
