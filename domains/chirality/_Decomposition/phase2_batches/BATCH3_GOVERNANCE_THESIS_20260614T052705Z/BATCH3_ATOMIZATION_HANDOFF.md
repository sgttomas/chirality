# Batch 3 Atomization Handoff - Governance Thesis Context

Package role: snapshot / handoff artifact

BatchID: `BATCH3_GOVERNANCE_THESIS_20260614T052705Z`

Status: GATE2_ACCEPTED_IN_PHASE2_CLOSURE

Completed UTC: 2026-06-14T06:05:00Z

## Scope

- Selected sources: `22` active governance/thesis context rows (`DG010-DG031`).
- Dispatch units: `23`.
- Standalone glossary source `SRC-DOCS-THESIS-GLOSSARY` / `DG030` produced one dispatch output successfully.
- Batch 2 is Gate-2 accepted in the Phase 2 closure snapshot.

## Output Summary

- Per-unit atom CSVs: `23`
- Per-unit vocabulary CSVs: `23`
- Raw worker atom rows: `4007` (`IN=3967`, `OUT=4`, `TBD=36`)
- Raw vocabulary rows: `1040`
- Per-source ledgers: `22`
- Batch-scoped merged atom rows: `4006` (`IN=3966`, `OUT=4`, `TBD=36`)
- Deduped duplicate hash rows: `1`
- Batch-scoped vocabulary terms: `766`
- Unresolved `Corrects` references: `0`
- Atom-review HTML files rendered: `22`

## Primary Artifacts

- `domains/chirality/_Decomposition/phase2_batches/BATCH3_GOVERNANCE_THESIS_20260614T052705Z/BATCH3_SETUP.md`
- `domains/chirality/_Decomposition/phase2_batches/BATCH3_GOVERNANCE_THESIS_20260614T052705Z/Batch_Source_Register.csv`
- `domains/chirality/_Decomposition/phase2_batches/BATCH3_GOVERNANCE_THESIS_20260614T052705Z/Dispatch_Unit_Register.csv`
- `domains/chirality/_Decomposition/phase2_batches/BATCH3_GOVERNANCE_THESIS_20260614T052705Z/Dispatch_Run_Log.csv`
- `domains/chirality/_Decomposition/phase2_batches/BATCH3_GOVERNANCE_THESIS_20260614T052705Z/Validation_Checks.csv`
- `domains/chirality/_Decomposition/phase2_batches/BATCH3_GOVERNANCE_THESIS_20260614T052705Z/BATCH3_Atomic_Domain_Ledger.csv`
- `domains/chirality/_Decomposition/phase2_batches/BATCH3_GOVERNANCE_THESIS_20260614T052705Z/BATCH3_Vocabulary_Map.csv`
- `domains/chirality/_Decomposition/dispatch_outputs/BATCH3_GOVERNANCE_THESIS_20260614T052705Z/`
- `domains/chirality/_Decomposition/per_source_ledgers/BATCH3_GOVERNANCE_THESIS_20260614T052705Z/`
- `domains/chirality/_Decomposition/vocabulary_seeds/BATCH3_GOVERNANCE_THESIS_20260614T052705Z/`

## Validation

- Worker output QA: PASS.
- Per-source merge: PASS.
- Cross-source merge: PASS.
- Vocabulary merge: PASS.
- Atom-review HTML render: PASS.
- Global `Atomic_Domain_Ledger.csv` and `Vocabulary_Map.csv` were not overwritten.

## Gate State

Batch 3 Gate 2 is accepted in the Phase 2 closure snapshot. The Batch 3 atoms and vocabulary are accepted decomposition truth for the active governance/thesis context batch DG010-DG031.

## Remaining Blockers

- Batch 3 contains `36` merged TBD rows carried into accepted Phase 2 truth for Phase 3 governance handling.
- Batch 2 is Gate-2 accepted in the Phase 2 closure snapshot.
- Active Batch 1 carry-forward is accepted only for the nine active source units recorded in `Gate2_Source_Unit_Register.csv`.

## Gate 2 Closure

Accepted in `domains/chirality/_Decomposition/gate_snapshots/GATE2_PHASE2_20260614T204403Z` by human approval on 2026-06-14. This batch is included in canonical `Atomic_Domain_Ledger.csv` and `Vocabulary_Map.csv`; the batch-scoped ledger remains supporting evidence.
