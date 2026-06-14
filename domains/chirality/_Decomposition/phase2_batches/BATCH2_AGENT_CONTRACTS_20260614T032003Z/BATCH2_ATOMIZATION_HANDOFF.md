# Batch 2 Atomization Handoff - Agent Contracts

Package role: snapshot / handoff artifact

BatchID: `BATCH2_AGENT_CONTRACTS_20260614T032003Z`

Status: GATE2_ACCEPTED_IN_PHASE2_CLOSURE

Generated UTC: 2026-06-14T05:07:20Z

## Accepted Upstream Snapshot

- Gate 1 acceptance snapshot: `domains/chirality/_Decomposition/gate_snapshots/GATE1_20260614T005942Z`
- Batch 1 Gate 2 acceptance snapshot: `domains/chirality/_Decomposition/gate_snapshots/GATE2_BATCH1_20260614T023234Z` (prior-boundary evidence only for active reuse)
- Source manifest SHA-256: `acd2fd88ff66be89b33d5cde05ab15cbcb584adea2fd25e661d9ea9eb0f64b04`
- Setup package: `domains/chirality/_Decomposition/phase2_batches/BATCH2_AGENT_CONTRACTS_20260614T032003Z/BATCH2_SETUP.md`

## Gate 2 Closure

Accepted in `domains/chirality/_Decomposition/gate_snapshots/GATE2_PHASE2_20260614T204403Z` by human approval on 2026-06-14. This batch is included in canonical `Atomic_Domain_Ledger.csv` and `Vocabulary_Map.csv`; the batch-scoped ledger remains supporting evidence.

## Fan-Out / Fan-In Summary

| Metric | Value |
|---|---:|
| Selected sources | 36 |
| Dispatch units | 36 |
| Per-unit atom CSVs | 36 |
| Per-unit vocabulary CSVs | 36 |
| Raw worker atom rows | 7772 |
| Raw IN rows | 7760 |
| Raw OUT rows | 4 |
| Raw TBD rows | 8 |
| Raw vocabulary rows | 1229 |
| Per-source ledgers | 36 |
| Merged atom ledger rows | 7770 |
| Deduped duplicate hash rows | 2 |
| Merged IN rows | 7758 |
| Merged OUT rows | 4 |
| Merged TBD rows | 8 |
| Merged vocabulary terms | 968 |
| Multi-source vocabulary terms | 137 |
| Atom-review HTML files | 36 |
| Unresolved Corrects refs | 0 |

## Outputs

- Dispatch run log: `domains/chirality/_Decomposition/phase2_batches/BATCH2_AGENT_CONTRACTS_20260614T032003Z/Dispatch_Run_Log.csv`
- Batch validation: `domains/chirality/_Decomposition/phase2_batches/BATCH2_AGENT_CONTRACTS_20260614T032003Z/Validation_Checks.csv`
- Batch-scoped atom ledger: `domains/chirality/_Decomposition/phase2_batches/BATCH2_AGENT_CONTRACTS_20260614T032003Z/BATCH2_Atomic_Domain_Ledger.csv`
- Batch-scoped vocabulary map: `domains/chirality/_Decomposition/phase2_batches/BATCH2_AGENT_CONTRACTS_20260614T032003Z/BATCH2_Vocabulary_Map.csv`
- Per-source ledgers root: `domains/chirality/_Decomposition/per_source_ledgers/BATCH2_AGENT_CONTRACTS_20260614T032003Z/`
- Per-source vocabulary seeds root: `domains/chirality/_Decomposition/vocabulary_seeds/BATCH2_AGENT_CONTRACTS_20260614T032003Z/`
- Atom-review HTML root: `domains/chirality/_Decomposition/source_review_html/`

## Closure Verdict

- Regenerated Batch 2 setup: CLOSED / SETUP_READY_REGENERATED.
- Batch 2 Phase 2 atomization fan-out: COMPLETE; all 36 dispatch units have valid atom and vocabulary CSV outputs.
- Batch 2 per-source and cross-source merge: COMPLETE; batch-scoped outputs only.
- Batch 2 Gate 2: CLOSED / GATE2_ACCEPTED.
- Global `Atomic_Domain_Ledger.csv` and `Vocabulary_Map.csv`: UPDATED by the Phase 2 Gate 2 closure merge; Batch 2 rows are included in the canonical accepted ledger and vocabulary.

## Known Review Items

- Merged Batch 2 ledger contains 8 `TBD` atom rows requiring Gate 2 review.
- `SRC-AGENTS-AGENT-SOFTWARE-DECOMP` was recovered after a stuck isolated worker by writing only the two dispatch-brief output CSVs from the same bounded source slice; it passed the same schema/hash/SourceRef QA.
- Active Batch 1 reuse remains blocked by OI-012 until explicit carry-forward or rebaseline.

## Gate 2 Acceptance Needed

Gate 2 accepted in `domains/chirality/_Decomposition/gate_snapshots/GATE2_PHASE2_20260614T204403Z`. Prior acceptance prompt was:

> The Batch 2 atom boundaries, IN/OUT/TBD classifications, source bindings, and vocabulary choices are accepted as decomposition truth for the active 36-source agent-contract batch.

## Rerun Requirements

- If any selected agent instruction source changes, rebuild the source catalog, regenerate affected skeleton/dispatch companions, rebuild this batch setup, and rerun affected atomization units.
- If the source manifest changes, recompute the manifest SHA, rebuild the catalog and BM25 index, and decide whether this Batch 2 handoff remains usable or must be rebaselined.
- Gate 3 category/KTY assignment may consume the canonical accepted Phase 2 ledger after the Phase 2.5 refresh.
