# Batch 3 Setup - Governance Thesis Context

Package role: snapshot / handoff artifact

BatchID: `BATCH3_GOVERNANCE_THESIS_20260614T052705Z`

Status: GATE2_ACCEPTED_IN_PHASE2_CLOSURE

Generated UTC: 2026-06-14T05:27:05Z

Atomization Completed UTC: 2026-06-14T06:05:00Z

## Accepted Upstream Snapshot

- Gate 1 acceptance snapshot: `domains/chirality/_Decomposition/gate_snapshots/GATE1_20260614T005942Z`
- Source manifest: `domains/chirality/_Sources/Source_Manifest.csv`
- Source manifest SHA-256: `7a1779039ef680e13646c73ab15dbab21c74f82c888d5b3d357721b3fe9c1bb4`
- Current source catalog snapshot: `domains/chirality/_LocalIndexes/snapshots/SRCIDX_20260614T050727Z`
- Batch 2 status at setup: GATE2_ACCEPTED_IN_PHASE2_CLOSURE
- Source-copy policy: `source_files_copied=false`

## Scope

Batch 3 is the authorized Phase 2 atomization batch for active governance/thesis context sources `DG010` through `DG031`. It is independent of Batch 2 Gate 2 closure: Batch 2 is Gate-2 accepted in the Phase 2 closure snapshot.

| SourceDocID | Prefix | RepoRelPath | Sections | In-scope Sections | Dispatch Units |
|---|---|---|---:|---:|---:|
| `SRC-DOCS-RUBRICS-AUDIT-AGENT` | `DG010` | `docs/rubrics/AUDIT_AGENT.md` | 65 | 65 | 1 |
| `SRC-DOCS-TEMPLATES-MEMORY-TEMPLATE` | `DG011` | `docs/templates/MEMORY_TEMPLATE.md` | 6 | 6 | 1 |
| `SRC-DOCS-THESIS-00-FRONT-MATTER` | `DG012` | `docs/thesis/00_front_matter.md` | 3 | 3 | 1 |
| `SRC-DOCS-THESIS-01-INTRODUCTION` | `DG013` | `docs/thesis/01_introduction.md` | 6 | 6 | 1 |
| `SRC-DOCS-THESIS-02-LITERATURE-REVIEW` | `DG014` | `docs/thesis/02_literature_review.md` | 47 | 47 | 2 |
| `SRC-DOCS-THESIS-03-PHILOSOPHICAL-FRAMEWORK` | `DG015` | `docs/thesis/03_philosophical_framework.md` | 21 | 21 | 1 |
| `SRC-DOCS-THESIS-04-ARCHITECTURE` | `DG016` | `docs/thesis/04_architecture.md` | 39 | 39 | 1 |
| `SRC-DOCS-THESIS-05-EPISTEMIC-ARCHITECTURE` | `DG017` | `docs/thesis/05_epistemic_architecture.md` | 18 | 18 | 1 |
| `SRC-DOCS-THESIS-06-PROFESSIONAL-PRACTICE` | `DG018` | `docs/thesis/06_professional_practice.md` | 44 | 44 | 1 |
| `SRC-DOCS-THESIS-07-SE-DESIGN-ANALYSIS` | `DG019` | `docs/thesis/07_se_design_analysis.md` | 47 | 47 | 1 |
| `SRC-DOCS-THESIS-08-IMPLEMENTATION` | `DG020` | `docs/thesis/08_implementation.md` | 29 | 29 | 1 |
| `SRC-DOCS-THESIS-09-DISCUSSION` | `DG021` | `docs/thesis/09_discussion.md` | 22 | 22 | 1 |
| `SRC-DOCS-THESIS-10-CONCLUSION` | `DG022` | `docs/thesis/10_conclusion.md` | 6 | 6 | 1 |
| `SRC-DOCS-THESIS-README` | `DG023` | `docs/thesis/README.md` | 5 | 5 | 1 |
| `SRC-DOCS-THESIS-APPENDIX-A-INVARIANT-CATALOG` | `DG024` | `docs/thesis/appendix_a_invariant_catalog.md` | 5 | 5 | 1 |
| `SRC-DOCS-THESIS-APPENDIX-C-APEGA-MAPPING` | `DG025` | `docs/thesis/appendix_c_apega_mapping.md` | 12 | 12 | 1 |
| `SRC-DOCS-THESIS-APPENDIX-D-FRAMEWORK-S` | `DG026` | `docs/thesis/appendix_d_framework_s.md` | 15 | 15 | 1 |
| `SRC-DOCS-THESIS-BIGGER-PICTURE-CHIRALITY-PRD-AMENDMENT-DOMAIN-ENGINE-INTEGRATION` | `DG027` | `docs/thesis/bigger-picture/CHIRALITY_PRD_Amendment_Domain_Engine_Integration.md` | 49 | 49 | 1 |
| `SRC-DOCS-THESIS-BIGGER-PICTURE-CHIRALITY-OPENPIPESTRESS-BIGGER-PICTURE-DEVELOPMENT-PLAN` | `DG028` | `docs/thesis/bigger-picture/Chirality_OpenPipeStress_Bigger_Picture_Development_Plan.md` | 179 | 179 | 1 |
| `SRC-DOCS-THESIS-BIGGER-PICTURE-CHIRALITY-OPENPIPESTRESS-INTEGRATION-PLAN` | `DG029` | `docs/thesis/bigger-picture/Chirality_OpenPipeStress_Integration_Plan.md` | 67 | 67 | 1 |
| `SRC-DOCS-THESIS-GLOSSARY` | `DG030` | `docs/thesis/glossary.md` | 1 | 1 | 1 |
| `SRC-DOCS-THESIS-REFERENCES` | `DG031` | `docs/thesis/references.md` | 10 | 10 | 1 |

## Generated Companions

- `Batch_Source_Register.csv` - authoritative companion register for selected Batch 3 source scope.
- `Dispatch_Unit_Register.csv` - authoritative companion register for per-unit brief/output paths.
- `Validation_Checks.csv` - setup and later worker QA / merge / render validation register.
- `Dispatch_Run_Log.csv` - per-dispatch-unit run counts and output status.
- `BATCH3_ATOMIZATION_HANDOFF.md` - atomization completion handoff and Gate 2 acceptance state.
- `BATCH3_Atomic_Domain_Ledger.csv` - batch-scoped merged atom ledger; global `Atomic_Domain_Ledger.csv` was not overwritten by this batch.
- `BATCH3_Vocabulary_Map.csv` - batch-scoped merged vocabulary map; global `Vocabulary_Map.csv` was not overwritten by this batch.
- `domains/chirality/_Decomposition/dispatch_briefs/BATCH3_GOVERNANCE_THESIS_20260614T052705Z/` - one INIT-TASK brief per dispatch unit.
- `domains/chirality/_Decomposition/dispatch_outputs/BATCH3_GOVERNANCE_THESIS_20260614T052705Z/` - prepared disjoint output directories for worker CSVs.
- `domains/chirality/_Decomposition/per_source_ledgers/BATCH3_GOVERNANCE_THESIS_20260614T052705Z/` - reserved per-source merge output root.
- `domains/chirality/_Decomposition/vocabulary_seeds/BATCH3_GOVERNANCE_THESIS_20260614T052705Z/` - reserved per-source vocabulary seed output root.

## SourceRef Policy

All rendered briefs include the accepted manifest-backed runtime override:

```text
SOURCE_REF_BASE: @repo/<RepoRelPath>:L####|domains/chirality/_Decomposition/source_review_html/<SourceDocID>.html#<SectionID>
```

## Worker Boundary

Workers must read only their assigned `LINE_START..LINE_END`, write only their two allowed CSV targets, and return a valid `RUN_STATUS`. The authorized fan-out covers exactly `DG010-DG031`, producing 23 dispatch-unit outputs.

## Closure Verdict

- Batch 3 setup: CLOSED / SETUP_READY.
- Batch 3 Phase 2 atomization: COMPLETE / QA_PASS (`raw_atoms=4007`, `merged_atoms=4006`, `vocab_terms=766`).
- Batch 3 Gate 2 normalization: CLOSED / ACCEPTED.
- Batch 2 is Gate-2 accepted in the Phase 2 closure snapshot.

## Rerun Requirements

- If any selected source file changes, update the source manifest, rebuild the source catalog and BM25 index, regenerate affected companions, then regenerate this batch setup.
- If `tools/decomp/build_atomization_brief.py`, `Source_Decomp_Prefix_Map.csv`, or `skills/domain-source-atomize/` changes before worker completion, regenerate all briefs and re-run setup validation.
- After worker fan-out, update `Dispatch_Unit_Register.csv` with run status and counts before per-source merge.

## Remaining Blockers

- Batch 3 Gate 2 is accepted in the Phase 2 closure snapshot; Batch 3 atoms are promoted into canonical Phase 2 truth.
- Batch 2 is Gate-2 accepted in the Phase 2 closure snapshot.
