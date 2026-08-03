# SCA-004 Gate 5 Run Summary

## Result

SCA-004 is executed and validated as a scope-change-only successor. PEC
SOFTWARE_DECOMP revision 1.4 records D-PEC-78 O-A: SOW-077 is `IN` and maps
reciprocally to `PKG-01 → DEL-01-06 → OBJ-004`; SOW-094's implementation
basis is reconciled; DEL-01-06 is modified in place; OI-003 is retained and
resolved. Stable IDs, topology, source, lifecycle, dependency edges, envelope,
phase, name, and path are unchanged.

## Fixed state fields

| Field | Value |
|---|---|
| `DecompositionTruthState` | `COMPLETE` |
| `DerivativePackageState` | `INCOMPLETE` — Lane B surfaces remain stale |
| `ContentRemediationState` | `NOT_REQUIRED` |
| `DownstreamRerunState` | `FROZEN` — no downstream repair authorized |
| `MetadataAlignmentState` | `NOT_STARTED` — 63 contexts and 64 references remain to re-pin |
| `AuditState` | `WARNINGS` — 0 blockers; one unchanged unrelated DEL-08-02 warning |
| `ReadyForNextPhase` | `NO` |
| `ClosureVerdict` | `CLOSED_FOR_SCOPE_CHANGE_ONLY` |

## Authoritative writes

| Surface | Postimage SHA-256 | Result |
|---|---|---|
| `execution/_Decomposition/SOFTWARE_DECOMP.md` | `7cca5cdbb1ba4bd866391abf00998bc80f587a23505a6f5b6bceb8df48b65c81` | revision 1.4 exact approved prose |
| `execution/_Decomposition/ScopeLedger.csv` | `2103afa279bc7df8e75f830326462d7575cf69a403ee7ef07880e0e9fe969e25` | only SOW-077/SOW-094 rows changed |
| `execution/_Decomposition/Deliverables.csv` | `49f904488a7402e2124359b59b2fc0df9103bef39ee53a5ce8b74f7dc6cc6b72` | only DEL-01-06 row changed |
| DEL-01-06 `_CONTEXT.md` | `24f357cc9746b1b0b24991995ed72067062dba9ce7b098b472a5d6eed2db94b2` | exact approved semantic/provenance mirror |

`ContextBudgetQA.csv`, `Companion_Inventory.csv`, DEL-01-06 `_STATUS.md`, all
source/tests, all dependencies, all SOW contracts, the accepted SPEC, and all
foreign-loop surfaces reproduce their preimages.

## Validation

- Pre-change authoritative hashes: 7/7 exact guards PASS, including context
  and pointers.
- Successor assertions: 94 rows; `72 IN / 14 OUT / 8 TBD`; 11 packages; 64
  deliverables; six objectives; PKG-01=8; OBJ-004=11; DEL-01-06 reciprocal;
  zero unassigned IN rows; 11 IN rows without objective; envelopes S28/M34/L2.
- Strict decomposition registers: 64 / 254 / zero findings.
- Dependency closure: 119 execution edges / zero SCCs / zero bidirectional
  pairs; same two zero-edge nodes.
- Post-change audit:
  `execution/_Evaluation/DecompCoverage/COV_SCA004_POSTCHANGE_2026-08-03_1442/`;
  0 blockers / 1 unchanged warning / 69 info.
- Audit `coverage_summary.json` and `Post_Change_Coverage.json` are byte
  identical at SHA-256
  `0d3ec0a827fabe564e677702eb2964899b3c1087943984183647050b0470d9ec`.
- Pre-change coverage remains byte-identical at SHA-256
  `183c6d94372d8ae93054f6dea8d46ebc378f41521f70f2add46af10c647c2813`.
- Header-only cumulative supersession map: SHA-256
  `9b62e98744d517fcc12fde63fe6cbc69925815dc111908bf7c7db455be81fcb9`;
  D-PEC-78 resolves an open question and supersedes no admitted fact.

## Downstream boundary

No downstream contract, reference, dependency, SPEC, map, lifecycle, source,
Task Management, or foreign-loop repair is part of Gate 5. Every stale surface
and its separately gated owner/rerun is enumerated in `Handoff_State.md`.

Recommended CHANGE message: `scope: SCA-004 — accept PEC decomposition revision 1.4`.
