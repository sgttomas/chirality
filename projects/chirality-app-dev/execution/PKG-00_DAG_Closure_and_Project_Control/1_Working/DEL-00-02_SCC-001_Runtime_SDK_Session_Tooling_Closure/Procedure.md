# Procedure: DEL-00-02 SCC-001 Runtime SDK Session Tooling Closure

## Purpose

Define the operational workflow for producing SCC-001 control records from the accepted DepClosure snapshot without mutating dependency edges during this four-document generation task.

## Prerequisites

- Current accepted upstream snapshot: `execution/_Reconciliation/DepClosure/CLOSURE_POST_ID_CANONICALIZATION_2026-05-24_1431/`.
- Required evidence files:
  - `Evidence/scc_summary.csv`
  - `Evidence/bidirectional_pairs.csv`
  - `SCC_Triage_Workbook.csv`
  - `Dependency_Closure_Report.md`
- `RUN_SUMMARY.md`
- DEL-00-02 remains a control deliverable with no `Dependencies.csv`.
- Access to owning product deliverable dependency registers and cited source evidence is required before any future row decision can be accepted; access owner/acquisition path remains TBD / HumanRuling.

Sources: `_REFERENCES.md`, `_DEPENDENCIES.md`, `DAG_CLOSURE_CONTROL.md` (Workflow), `SCC_Triage_Workbook.csv` (RecommendedAction).

## Steps

1. Confirm the accepted upstream DepClosure snapshot path from `_REFERENCES.md` and `DAG_CLOSURE_CONTROL.md`.
2. Read `Dependency_Closure_Report.md` and `RUN_SUMMARY.md` to confirm strict FULL_GRAPH remains CYCLIC and blocker-subset remains ACYCLIC.
3. Read `Evidence/scc_summary.csv` and extract only the SCC-001 node set.
4. Read `Evidence/bidirectional_pairs.csv` and select the 12 pairs whose nodes are both in the SCC-001 node set.
5. Create the focused SCC-001 ruling workbook using the current bidirectional-pair evidence and the `SCC_Triage_Workbook.csv` directive. The workbook output path/name is TBD; until a human or approved workflow chooses a path, use a proposed record name of `SCC-001_Ruling_Workbook.csv` inside the DEL-00-02 control records without treating that proposal as authoritative.
6. For each workbook row, identify the owning product dependency row(s) and cited evidence source(s).
7. Classify each edge using the triage categories from `SCC_Triage_Workbook.csv`: hard sequencing, interface evidence, downstream handoff, duplicate reciprocal evidence, already satisfied, or co-development-only.
8. Convert each classification into an allowed existing dependency-schema action only when source evidence supports it. Otherwise mark the row `TBD` or `NEEDS_HUMAN_RULING`.
9. Apply accepted row changes only in the owning product deliverable registers, not in DEL-00-02.
10. Run a new DepClosure scan after accepted row changes.
11. Record the follow-up snapshot path, strict SCC verdict, remaining blockers, and handoff state in DEL-00-02 control records.

## Verification

| Check | Expected Result |
|---|---|
| DEL-00-02 dependency register check | No `Dependencies.csv` exists in this folder. |
| Snapshot alignment | `_REFERENCES.md` and `DAG_CLOSURE_CONTROL.md` point to the same accepted DepClosure snapshot before workbook generation. |
| SCC node fidelity | Workbook SCC-001 nodes match `Evidence/scc_summary.csv`. |
| Bidirectional pair fidelity | Workbook input pairs are drawn from `Evidence/bidirectional_pairs.csv`; SCC-002 pair is excluded from SCC-001 rulings. |
| Source-grounding | Each proposed dependency row decision cites the owning row and supporting source evidence. |
| Schema discipline | No new dependency type or schema value is introduced. |
| Closure evidence | Follow-up DepClosure reports `scc_count = 0` and strict FULL_GRAPH acyclic before project-wide blocker state is reportable. |
| Follow-up snapshot record | Records include the immutable follow-up DepClosure snapshot path and strict FULL_GRAPH result after accepted row changes. |

## Records

- Focused SCC-001 ruling workbook.
- Minimum workbook columns: `PairID`, `NodeA`, `NodeB`, `OwningRegisterPath`, `DependencyID`, `CurrentDependencyType`, `CurrentStatus`, `EvidenceCitation`, `TriageClassification`, `AllowedSchemaAction`, `Ruling`, `HumanRuling`, `RemainingBlockerStatus`, `Notes`.
- Per-row decision records with owning register path, dependency ID, source citation, ruling, and remaining blocker status.
- Product-register diffs for any accepted row changes.
- New immutable DepClosure snapshot, including the snapshot path and strict FULL_GRAPH result.
- Handoff state naming accepted upstream snapshot, derivative-package status, closure verdict, rerun requirements, and remaining blockers.

## Pass 3 Disposition

| ItemID | Disposition | Evidence |
|---|---|---|
| F-002 | Converted to TBD / HumanRuling. | Prerequisites now state that access owner/acquisition path for product registers and cited evidence remains unresolved; `_CONTEXT.md` has ResponsibleParty TBD. |
| D-001 | Incorporated with TBD authority boundary. | Steps and Records now define a proposed workbook name and minimum columns while preserving the authoritative output path/name as TBD. |
| E-001 | Incorporated. | Verification and Records now require recording the follow-up DepClosure snapshot path and strict FULL_GRAPH result; supported by `DAG_CLOSURE_CONTROL.md` Acceptance Condition and `Dependency_Closure_Report.md` Ruling. |
