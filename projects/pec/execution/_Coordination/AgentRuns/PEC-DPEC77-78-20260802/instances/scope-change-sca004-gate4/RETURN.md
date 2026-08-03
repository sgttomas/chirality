# SCOPE_CHANGE return — SCA-004 Gate 4 propagation plan

Status: `COMPLETE — AWAITING OWNER GATE 4 APPROVAL`  
Manager: `SCOPE_CHANGE`  
RunID: `PEC-DPEC77-78-20260802`  
InstanceID: `scope-change-sca004-gate4`  
AmendmentID: `SCA-004`

## Result

The bounded Gate 4 propagation plan is complete and validated against the
approved Gate 3 preview SHA-256
`4a473ca087ba4f0fa63cc98432165ec46a819a36f22c9ab44f3c98778dae245f`.
It executes no write. Gate 5 is not open.

Plan:
`projects/pec/execution/_ScopeChange/SCA-004_2026-08-02_2325/Propagation_Plan.md`

## Exact hashes

| File | SHA-256 |
|---|---|
| `Propagation_Plan.md` | `f63d45eb6c56bd5396e71ddce5c84cbd088aa2eb876864f06039b299336757f2` |
| `Amendment_Actions.csv` | `c896ac99f495a5eb8afd0bcae10dd1e21c58abed93658a580507353e7c22b7d6` |
| `Gate4_Plan_Validation.md` | `5a653bbb7288d4913e5bfaac661b9bc9339db010c4c939d69ef7fedd0543893a` |
| `Gate4_Handoff.md` | `552a9e2f1d128d0a1b3948c9c9e68b541328168571dad47df5fd88f210fc0389` |

## Amendment action register

The register contains exactly five sequential `MODIFY` rows:

| Action | Entity | Later Gate 5 direct effect |
|---|---|---|
| A001 | SOW-077 | Exact TBD→IN, lineage, open-flag and D-PEC-78 postimage in decomposition/ledger |
| A002 | SOW-094 | Exact DecisionRef/Notes reconciliation only |
| A003 | DEL-01-06 | Exact description/coverage change plus one context mirror |
| A004 | OI-003 | Preserved resolved row and telemetry reconciliation |
| A005 | SCA-004 trace | Revision/history, snapshot evidence and conditional active pointers |

All `SupersessionBindingPresent` values are `NO`; D-PEC-78 answers an open
PRD question rather than overriding an admitted fact.

## Complete write-owner and rerun matrix

| Population | Classification | Owner | Gate 4 disposition |
|---|---|---|---|
| `SOFTWARE_DECOMP.md` | `DIRECT_EDIT` | SCOPE_CHANGE | Later Gate 5 exact approved postimage |
| `ScopeLedger.csv` SOW-077/SOW-094 | `DIRECT_EDIT` | SCOPE_CHANGE | Later Gate 5 exact row replacements |
| `Deliverables.csv` DEL-01-06 | `DIRECT_EDIT` | SCOPE_CHANGE | Later Gate 5 exact row replacement |
| DEL-01-06 `_CONTEXT.md` | `DIRECT_EDIT` | SCOPE_CHANGE | Later Gate 5 exact `CoversScopeItems`, description and provenance mirror; status frozen |
| `ContextBudgetQA.csv`, `Companion_Inventory.csv` | `NO_CHANGE` | none | Prove byte identity |
| SCA-004 evidence, supersession map, post-change coverage, handoff/run summary | `RECOMPUTE` | SCOPE_CHANGE | Later Gate 5 after validation |
| Decomposition/SCA pointers | `RECOMPUTE` | SCOPE_CHANGE | Conditional on complete snapshot/validation |
| post-change DecompCoverage snapshot/pointer | `RECOMPUTE` | AUDIT_DECOMP | New immutable later Gate 5 audit |
| remaining 63 `_CONTEXT.md` provenance blocks | `NO_CHANGE` in SCA Gate 5 | PROJECT_SETUP later | Separately routed re-pin |
| all 64 `_REFERENCES.md` packets | `NO_CHANGE` in SCA Gate 5 | PROJECT_SETUP/reference owner later | Separately routed re-pin |
| DEL-01-06 SOW-077 requirement anchor | `NO_CHANGE` in SCA Gate 5 | dependency-extract / PROJECT_SETUP later | Add one non-gating anchor; preserve execution graph |
| DEL-01-06/02-07/03-01/04-01 contracts | `NO_CHANGE` in SCA Gate 5 | WORKING_ITEMS + artifact gates later | Contract-currency review and successor acceptance |
| DEL-00-03 accepted SPEC | `NO_CHANGE` in SCA Gate 5 | DEL-00-03 owning workflow later | Separate artifact amendment/review/acceptance |
| README, STATUS, coordination map, standing PEC workplan | `NO_CHANGE` in SCA Gate 5 | HELP_HUMAN / loop-maintenance owner later | Ordinary current-map refresh |
| source/tests, lifecycle, Task Management, decisions, receipts, historical evidence, foreign loops | `NO_CHANGE` | none | Frozen |

The plan enumerates the exact 63-context and 64-reference populations by
package/deliverable ID and records exact paths/hashes for the anchor, four
contracts, accepted SPEC, and four PEC map surfaces.

## Later Gate 5 validation contract

- Verify every accepted preimage hash before the first write.
- Enforce exact changed-path, row, and field containment.
- Run strict decomposition-register validation with zero errors/warnings.
- Confirm dependency closure remains 119 execution edges / 0 SCCs /
  0 bidirectional pairs.
- Confirm `72 IN / 14 OUT / 8 TBD`, 11 packages, 64 deliverables, six
  objectives, PKG-01 count 8, DEL-01-06 coverage `SOW-077;SOW-094`, OBJ-004
  count 11, and unchanged Context Envelopes.
- Produce a new immutable post-change AUDIT_DECOMP snapshot with no blocker.
- Complete SCA-004 evidence and verify all hashes/pointers before closure.
- If successful and owner-accepted, close only for SCOPE_CHANGE; all
  downstream obligations remain explicitly open and `ReadyForNextPhase=NO`.

## Containment validation

- `Amendment_Actions.csv`: schema `PASS`, five rows.
- Context population: 64 total = one proposed direct mirror + 63 downstream
  provenance re-pins.
- Reference population: 64 downstream re-pins.
- Paired DEL-01-06 `_STATUS.md`/memory read: `PASS`; lifecycle is
  `INITIALIZED`, and no sibling memory file exists.
- All five authoritative preimage hashes remain unchanged.
- `git diff --check`: `PASS`.
- No live decomposition, companion register, pointer, metadata, reference,
  dependency, contract, SPEC, source, lifecycle, Task Management, decision,
  receipt, audit/snapshot, or foreign surface was written by this Gate 4 act.

## Exact owner Gate 4 question

**Do you approve this SCA-004 propagation plan for later Gate 5 execution?**
