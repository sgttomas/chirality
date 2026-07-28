---
run_id: PEC_SOW_V22_SCA003_RECON_2026-07-28
wave_id: W1
phase: R2_DISCOVERY
status: frozen
created: 2026-07-28
authority: D-PEC-69
source_commit: 404e47c16a88e7ffdc6d1fc5fac61ebb6864211e
---

# W1 — affected-contract claim discovery

## Objective

Read-only claim-level concordance of the execution-time candidate population
against PRD v2.2, SOFTWARE_DECOMP revision 1.3, D-PEC-67/-68/-69 and SCA-003.
No production contract may be edited during this wave.

## Population and disjoint outputs

| Deliverable | Contract |
|---|---|
| DEL-00-01 | `PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-01_v2_first_ADRs_core_isolation_carried_postures/ScopeOfWork.md` |
| DEL-03-06 | `PKG-03_Reconciliation_Parity/1_Working/DEL-03-06_Rebuild_performance_bounds/ScopeOfWork.md` |
| DEL-04-01 | `PKG-04_Orientation_Services/1_Working/DEL-04-01_Loop_orientation_return/ScopeOfWork.md` |
| DEL-04-02 | `PKG-04_Orientation_Services/1_Working/DEL-04-02_Delta_service_since_SHA/ScopeOfWork.md` |
| DEL-08-01 | `PKG-08_API_Access/1_Working/DEL-08-01_Unix_socket_server_token_scoped_access/ScopeOfWork.md` |
| DEL-08-03 | `PKG-08_API_Access/1_Working/DEL-08-03_Compact_citation_bearing_response_format/ScopeOfWork.md` |
| DEL-08-04 | `PKG-08_API_Access/1_Working/DEL-08-04_Orientation_latency_budget_p95_100_ms/ScopeOfWork.md` |
| DEL-10-01 | `PKG-10_Validation_Measurement/1_Working/DEL-10-01_Step_0_cost_baseline_pre_P1/ScopeOfWork.md` |
| DEL-10-10 | `PKG-10_Validation_Measurement/1_Working/DEL-10-10_Directed_bootstrap_self_ingest_validation/ScopeOfWork.md` |
| DEL-10-11 | `PKG-10_Validation_Measurement/1_Working/DEL-10-11_Parity_metric_DriftFindings_per_reconcile/ScopeOfWork.md` |

Each worker owns only:

- `<DEL>_claims.csv`;
- `<DEL>_notes.md`;
- `<DEL>_baseline_validation.json`;
- `<DEL>_consistency.json`;
- `<DEL>_boundary.json`;
- `<DEL>_checklist.json`.

All are under this `WAVES/W1/` directory.

## Claim-ledger schema

```text
ClaimRowID,DeliverableID,ContractPath,Section,LocalID,ClaimClass,ClaimText,AcceptedSourceRefs,Disposition,RepairNeeded,RepairInstruction,SourceState,Notes
```

Every bold local definition (`OUT|CLM|REQ|AC|VER|AX|TBD|CON-NNN`) receives
exactly one row. `ClaimText` is exact single-line text with Markdown emphasis
removed only around the ID. Dispositions use `CONVENTIONS.md`.

## Worker method

1. Read root/project instructions, AGENT_TASK, `scope-of-work` and
   `deliverable-consistency` skill contracts.
2. Reproduce the contract and `_STATUS.md` hashes.
3. Run the four deterministic read-only checks into the worker's own outputs.
4. Extract every local claim definition and compare relevant meaning to the
   frozen accepted sources.
5. Mark only true PRD v2.2/SCA-003 incompatibilities
   `DOCUMENTED_DIFFERENTLY` with a minimal repair instruction.
6. Specifically detect retired ADR-014 allocation, self-polling, forced
   session-start/mode-transition contact, forced injection, external cadence,
   receiving-loop duty/conformance, or P2 use-as-gate claims.
7. Return counts, hashes, exact changed-claim candidate set and any
   `AUTHORITY_CONFLICT`/`UNKNOWN`.

The active hold permits historical read-only inspection and exact correction
preparation only. No reliance, promotion, production dispatch or consumption.
