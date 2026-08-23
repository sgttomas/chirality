# SCA-004 closed-confirmed handoff

Status: `CLOSED_CONFIRMED_PROPAGATION_PENDING`

## Four-state handoff

| State | Value |
|---|---|
| Accepted upstream state | R1-C accepts Gate 1; R2-A accepts Gate 2; R3-A approves the exact Gate-3 bytes; R3-B approves the propagation plan with CONDITION R3-B-1; R4-A approves the append/result identities; R5-A authorizes the corrected second Gate-5 attempt; R6-A confirms Gate 5; R6-B approves the pointer with three named fills; R6-C authorizes the recorded Git-effect/reference backfill. |
| Authoritative truth state | `COMPLETE_CONFIRMED` — the seven live revision-1.3 surfaces equal R4-A exactly and are the accepted current basis. `_LATEST.md` identifies SCA-004 revision 1.3 under R6-B. |
| Derivative package state | `CURRENT_FOR_SCOPE_CHANGE_CLOSURE` — rehearsal, applied validator, application record, post-Gate5 AUDIT_DECOMP backcheck, and pointer are current. Folder/context/dependency/estimate/schedule/graph propagation remains stale and deferred. |
| Closure / next state | `CLOSED_CONFIRMED_PROPAGATION_PENDING`; SCA-004 Gates 1–5 are complete. Later propagation proceeds only through separately gated owning workflows. |

## Fixed state fields

| Field | Value |
|---|---|
| AmendmentID | `SCA-004` |
| DecompositionTruthState | `COMPLETE` — exact approved bytes applied and confirmed by owner R6-A |
| DerivativePackageState | `INCOMPLETE` — Gate-5 closure evidence current; later propagation derivatives stale/deferred |
| ContentRemediationState | `NOT_REQUIRED` |
| DownstreamRerunState | `FROZEN` pending later separately owned propagation acts |
| MetadataAlignmentState | `NOT_REQUIRED` |
| AuditState | `NON_BLOCKING_PASS` — applied validator 65/65; post-Gate5 backcheck PASS |
| ReadyForNextPhase | `NO` |
| ClosureVerdict | `CLOSED_CONFIRMED_PROPAGATION_PENDING` |

## Applied live identities

| Surface | Applied revision-1.3 SHA-256 |
|---|---|
| Working surface | `546b6e4c58278e2bee3f68fa5b4079b0862543ef03f87c154be545948a6c4986` |
| Deliverable register | `2cdf1e689f57459acacb56d7aa7824ec7bb4b1cba0d04a1daacc9f086062bfba` |
| Scope ledger | `63e6fa6b800490201ba0880e5b21dd69f44365bc3a7bf5788d9d53adc3ec7417` |
| Objective register | `b65da0f8e4ac5bc6fc1478eb6849cf9e7d5b8fa58be1d95c0963d83d430af27f` |
| Forward trace | `9fcfa2a5d4f33cacf23d2ef2a9d4465335ecbbfe544ec653370afcb25ae90a4f` |
| Reverse trace | `750aed6cd7891653b99ec9b04000b939dc999dc3260305dbd532ff743a57b438` |
| Coverage telemetry | `bdd6bc08d20c57666c03cc8f0c297cd4c000feb0150d4f2c327a263d483ecf0c` |

Topology is 53 deliverables, PKG-02=12, PKG-04=11, 6 packages, 104 scope
items, 7 objectives, 85 forward rows, and 59 reverse units, with zero
unmapped IN items, unsupported objectives, or untraced reverse units.

## Current evidence

| Evidence | Result |
|---|---|
| `Gate_5_Rehearsal_Record.md` | Stage A PASS: R3-A 7/7 + R4-A 7/7 + applied validator PASS 65/65, zero failures |
| `Gate_5_Applied_Validation.json` | Live applied state PASS 65/65, zero failures |
| `Gate_5_Application_Record.md` | Exact before→after identities, commands, authority, closure lane, derivative disposition, and recorded Git-effect/reference backfill |
| `Evidence/AUDIT_DECOMP_POST_GATE5/coverage_summary.json` | PASS for applied package; Gate-1 baseline preserved |
| `execution/_ScopeChange/_LATEST.md` | SCA-004 revision 1.3 pointer applied under R6-B with exactly three named fills |

## Held bindings

All ten DEL-02-06 compatibility objects remain `HELD_UNAVAILABLE`. The
accepted JSON stays SHA-256
`e5ae4e874bdace43720db082a9bd1ae3ff81b9e731264c65039b02d7f720467c`.
The exact ten binding paths and states are cited at
`Impact_Assessment.md:83` through `Impact_Assessment.md:92`.

## Derivative-package status

| Package/surface | State | Next required action |
|---|---|---|
| Seven live decomposition surfaces | `CURRENT_ACCEPTED_REVISION_1.3` | Preserve as read-only accepted basis |
| Gate-5 rehearsal/application/validation/backcheck package | `CURRENT` | Preserve as SCA-004 closure evidence |
| PREPARATION INIT ×7 | `STALE_NOT_MATERIALIZED` | Later PROJECT_SETUP/PREPARATION acts |
| DEL-02-06 `_CONTEXT.md` mirror | `STALE` | Later approved edit |
| Dependencies, estimates, schedule | `STALE` | Later owning workflows after folders/SOWs |
| `WORK_GRAPH.json` / `DAG.md` and `AUDIT_DEP_CLOSURE` | `STALE_FOR_APPLIED_TOPOLOGY` | Re-derive/rerun after folders are live |
| `_LATEST.md` | `CURRENT_SCA-004_REVISION_1.3` | Preserve; no further pointer act required for SCA-004 closure |

## Remaining propagation work

1. PREPARATION INIT ×7 through later PROJECT_SETUP/PREPARATION acts.
2. DEL-02-06 `_CONTEXT.md` edit list through its separately approved act.
3. Dependency extraction after folders are live.
4. Estimate snapshot and schedule after accepted SOWs and dependencies.
5. `WORK_GRAPH.json` / `DAG.md` re-derivation after folders are live.
6. `AUDIT_DEP_CLOSURE` after graph re-derivation.

## Blockers

1. TM-ROOT-106 remains an unchanged G1 blocker; no pin change.
2. TM-ROOT-122 remains an unchanged G1 blocker; no pin change.
3. All ten DEL-02-06 bindings remain `HELD_UNAVAILABLE`; no hold is lifted.

## Rerun requirements

- Before any downstream propagation consumes the accepted basis, rehash all
  seven live surfaces against R4-A and rerun `validate_gate5_applied.py`.
- Do not run the pre-application `validate_gate5_package.py` against the live
  applied state; its revision-1.2 assertions are intentionally inapplicable.
- Do not initiate folders, SOWs, dependencies, estimates, schedule, graph,
  implementation, runtime/tool, App, hold-lift, cutover, release,
  publication, or reliance work without its separately accepted authority.

## Next owner

Separately authorized propagation owners through HELP_HUMAN. SCA-004 is
closed and confirmed; this handoff does not itself authorize propagation.
