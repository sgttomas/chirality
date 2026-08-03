# SCA-004 Gate 5 Handoff State

## Accepted successor and closure

| Field | Value |
|---|---|
| Active amendment snapshot | `projects/pec/execution/_ScopeChange/SCA-004_2026-08-02_2325/` |
| Authoritative successor | PEC SOFTWARE_DECOMP revision 1.4, SHA-256 `7cca5cdbb1ba4bd866391abf00998bc80f587a23505a6f5b6bceb8df48b65c81` |
| Upstream authority | D-PEC-78 O-A plus owner-confirmed SCA-004 Gates 1–5 |
| Audit evidence | `COV_SCA004_POSTCHANGE_2026-08-03_1442`; 0 blockers / 1 unchanged warning |
| Closure verdict | `CLOSED_FOR_SCOPE_CHANGE_ONLY` |
| Ready for next phase | `NO` |

The canonical decomposition and its directly owned companion/context mirror
are current. Derivative closure remains incomplete by design. Gate 5 itself
authorizes none of the reruns below.

## Active direct surfaces

| Surface | Classification | Status | Evidence |
|---|---|---|---|
| `execution/_Decomposition/SOFTWARE_DECOMP.md` | `DIRECT_EDIT` | `CURRENT` | SHA-256 `7cca5cdbb1ba4bd866391abf00998bc80f587a23505a6f5b6bceb8df48b65c81` |
| `execution/_Decomposition/ScopeLedger.csv` | `DIRECT_EDIT` | `CURRENT` | SHA-256 `2103afa279bc7df8e75f830326462d7575cf69a403ee7ef07880e0e9fe969e25` |
| `execution/_Decomposition/Deliverables.csv` | `DIRECT_EDIT` | `CURRENT` | SHA-256 `49f904488a7402e2124359b59b2fc0df9103bef39ee53a5ce8b74f7dc6cc6b72` |
| `execution/_Decomposition/ContextBudgetQA.csv` | `NO_CHANGE` | `CURRENT_UNCHANGED` | SHA-256 `5c8d30994a99611b7023f8ac0995ee9a8efa0d2992f3c1a2683f4d2f9e8e2bef` |
| `execution/_Decomposition/Companion_Inventory.csv` | `NO_CHANGE` | `CURRENT_UNCHANGED` | SHA-256 `18793e150c537371f80d659af2784674d42bac0de37bf7128e484774a557ec23` |
| DEL-01-06 `_CONTEXT.md` | `DIRECT_EDIT` | `CURRENT` | SHA-256 `24f357cc9746b1b0b24991995ed72067062dba9ce7b098b472a5d6eed2db94b2` |
| SCA-004 snapshot | `RECOMPUTE` | `CURRENT` | complete Gate 2–5 package |
| post-change DecompCoverage snapshot | `RECOMPUTE` | `CURRENT_WITH_WARNING` | one unchanged DEL-08-02 artifact-location warning |

## Stale derivative surfaces and separately gated reruns

| Population / surface | Current state | Owner | Required separately gated action |
|---|---|---|---|
| Remaining 63 deliverable `_CONTEXT.md` provenance blocks | `STALE_REPIN_REQUIRED` | PROJECT_SETUP / approved metadata-pointer workflow | Re-pin accepted basis to revision 1.4 without changing semantic fields; validate all 63 exact paths |
| All 64 deliverable `_REFERENCES.md` packets | `STALE_REPIN_REQUIRED` | PROJECT_SETUP / reference owner | Re-pin accepted decomposition/SCA basis to revision 1.4/SCA-004; validate population and hashes |
| DEL-01-06 `Dependencies.csv` | `STALE_ANCHOR_REFRESH_REQUIRED` | dependency-extract / PROJECT_SETUP | Add one non-gating `ANCHOR / TRACES_TO_REQUIREMENT` row for SOW-077; rerun strict registers and prove topology remains 119/0/0 |
| DEL-01-06 `ScopeOfWork.md` | `STALE_REBUILD_REQUIRED` | WORKING_ITEMS + REVIEW/owner artifact gates | Add SOW-077 trace; replace OI-003-open claims; preserve ports/adapters and future-production gates; derive six exact AC rows; review and re-accept successor bytes |
| DEL-02-07 `ScopeOfWork.md` | `STALE_REVIEW_REQUIRED` | WORKING_ITEMS + ordinary artifact gates | Replace only OI-003-undecided premise; preserve in-process interface boundary |
| DEL-03-01 `ScopeOfWork.md` | `STALE_REVIEW_REQUIRED` | WORKING_ITEMS + ordinary artifact gates | Replace OI-003-undecided premise; preserve TBD-005 and dependency edges |
| DEL-04-01 `ScopeOfWork.md` | `STALE_REVIEW_REQUIRED` | WORKING_ITEMS + ordinary artifact gates | Replace OI-003-open premise without inventing a DEL-01-06 execution dependency |
| DEL-00-03 accepted `artifacts/v2/SPEC.md` | `STALE_REVIEW_REQUIRED` | DEL-00-03 owning workflow + REVIEW/owner exact-byte gate | Amend only the present-tense all-OI-open claim; historical accepted bytes remain valid history |
| `projects/pec/README.md` | `STALE_POINTER_OR_MAP_NOTE` | HELP_HUMAN / PEC loop maintenance | Refresh only present-current basis/open-decision prose |
| `projects/pec/docs/STATUS.md` | `STALE_POINTER_OR_MAP_NOTE` | HELP_HUMAN / PEC loop maintenance | Refresh only present-current basis/open-decision prose |
| `projects/pec/execution/_Coordination/_COORDINATION.md` | `STALE_POINTER_OR_MAP_NOTE` | HELP_HUMAN / PEC loop maintenance | Refresh only present-current basis/open-decision prose |
| `_DomainEngines/pec/WORKPLAN_2026-07-24_pec_coordination_plane.md` | `STALE_POINTER_OR_MAP_NOTE` | HELP_HUMAN / PEC loop maintenance | Refresh only present-current basis/open-decision prose; preserve historical owner intent |

## Explicitly current or excluded

- All source and tests, lifecycle files, Task Management registers, decisions,
  receipts, prior snapshots, and foreign-loop surfaces are unchanged.
- Historical review, acceptance, and SCA evidence remains historical; it is
  not regenerated to look revision-1.4-native.
- No estimate or schedule rerun is required by SCA-004 itself.
- `ContentRemediationState = NOT_REQUIRED`; this SOFTWARE amendment has no
  DOMAIN KTY remediation lane.

## Required handoff states

| Field | Value |
|---|---|
| `DecompositionTruthState` | `COMPLETE` |
| `DerivativePackageState` | `INCOMPLETE` |
| `ContentRemediationState` | `NOT_REQUIRED` |
| `DownstreamRerunState` | `FROZEN` |
| `MetadataAlignmentState` | `NOT_STARTED` |
| `AuditState` | `WARNINGS` |
| `ReadyForNextPhase` | `NO` |

Next owners are PROJECT_SETUP, dependency-extract/PROJECT_SETUP,
WORKING_ITEMS plus the named artifact gates, DEL-00-03's owning workflow, and
HELP_HUMAN loop maintenance. None is dispatched by this handoff.
