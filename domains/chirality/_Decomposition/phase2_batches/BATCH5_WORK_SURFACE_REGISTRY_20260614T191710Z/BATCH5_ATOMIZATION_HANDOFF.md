# Batch 5 Atomization Handoff - Work Surface Registry

Package role: snapshot / handoff artifact

BatchID: `BATCH5_WORK_SURFACE_REGISTRY_20260614T191710Z`

Status: GATE2_ACCEPTED_IN_PHASE2_CLOSURE

Completed UTC: 2026-06-14T19:27:53Z

## Scope

- Selected sources: `4` work-surface registry Markdown files under `domains/chirality/_Decomposition/work_surface_registry/`.
- Dispatch units: `4`.
- Source grouping policy: each WSR document is one source with prefixes `WSR001`..`WSR004`.
- Archived material, vendor/build/cache output, generated batches, local indexes/snapshots, and implementation detail outside each work-surface boundary remain excluded.
- `LICENSE.md` remains deferred and was not selected.

## Output Summary

- Per-unit atom CSVs: `4`
- Per-unit vocabulary CSVs: `4`
- Raw worker atom rows: `250` (`IN=248`, `OUT=0`, `TBD=2`)
- Raw vocabulary rows: `117`
- Per-source ledgers: `4`
- Batch-scoped merged atom rows: `250` (`IN=248`, `OUT=0`, `TBD=2`)
- Deduped duplicate hash rows: `0`
- Batch-scoped vocabulary terms: `109`
- Multi-source vocabulary terms: `5`
- Unresolved `Corrects` references: `0`
- Atom-review HTML files rendered: `4`

## TBD Rows

- `HBA-WSR003-00038` / `SRC-WSR-PROJECTS-CHIRALITY-APP-DEV` / `@repo/domains/chirality/_Decomposition/work_surface_registry/WSR-PROJECTS-CHIRALITY-APP-DEV.md:L38|domains/chirality/_Decomposition/source_review_html/SRC-WSR-PROJECTS-CHIRALITY-APP-DEV.html#SEC-WSR003-0005` - `frontend/` is separated from `execution/` because source and tests are implementation truth while execution packages and deliverable folders carry decomposition, lifecycle, and evidence authority.
- `HBA-WSR004-00066` / `SRC-WSR-PROJECTS-CHIRALITY-PIPING` / `@repo/domains/chirality/_Decomposition/work_surface_registry/WSR-PROJECTS-CHIRALITY-PIPING.md:L85|domains/chirality/_Decomposition/source_review_html/SRC-WSR-PROJECTS-CHIRALITY-PIPING.html#SEC-WSR004-0010` - The project has a review flag for tension between older PRD Free and open-source wording and current source-available noncommercial PolyForm licensing.

## Primary Artifacts

- `domains/chirality/_Decomposition/phase2_batches/BATCH5_WORK_SURFACE_REGISTRY_20260614T191710Z/BATCH5_SETUP.md`
- `domains/chirality/_Decomposition/phase2_batches/BATCH5_WORK_SURFACE_REGISTRY_20260614T191710Z/BATCH5_ATOMIZATION_HANDOFF.md`
- `domains/chirality/_Decomposition/phase2_batches/BATCH5_WORK_SURFACE_REGISTRY_20260614T191710Z/Dispatch_Run_Log.csv`
- `domains/chirality/_Decomposition/phase2_batches/BATCH5_WORK_SURFACE_REGISTRY_20260614T191710Z/BATCH5_Atomic_Domain_Ledger.csv`
- `domains/chirality/_Decomposition/phase2_batches/BATCH5_WORK_SURFACE_REGISTRY_20260614T191710Z/BATCH5_Vocabulary_Map.csv`
- `domains/chirality/_Decomposition/dispatch_outputs/BATCH5_WORK_SURFACE_REGISTRY_20260614T191710Z/`
- `domains/chirality/_Decomposition/per_source_ledgers/BATCH5_WORK_SURFACE_REGISTRY_20260614T191710Z/`
- `domains/chirality/_Decomposition/vocabulary_seeds/BATCH5_WORK_SURFACE_REGISTRY_20260614T191710Z/`

## Validation

- Worker output QA: PASS.
- Per-source merge: PASS.
- Cross-source merge: PASS.
- Vocabulary merge: PASS.
- Atom-review HTML render: PASS.
- Global `Atomic_Domain_Ledger.csv` and `Vocabulary_Map.csv` were not overwritten.

## Gate State

Batch 5 Gate 2 is ACCEPTED in `domains/chirality/_Decomposition/gate_snapshots/GATE2_PHASE2_20260614T204403Z`. Prior acceptance prompt was:

> The Batch 5 atom boundaries, IN/TBD classifications, source bindings, and vocabulary choices are accepted as decomposition truth for the work-surface registry batch WSR001-WSR004, with archived material and LICENSE.md remaining deferred/excluded.

## Remaining Blockers

- Batch 5 contains `2` merged TBD rows requiring Gate 2 review.
- Batch 2 is Gate-2 accepted in the Phase 2 closure snapshot.
- Batch 3 is Gate-2 accepted in the Phase 2 closure snapshot.
- Batch 4 is Gate-2 accepted in the Phase 2 closure snapshot.
- Active Batch 1 reuse remains governed by OI-012 until explicit carry-forward or rebaseline.

## Gate 2 Closure

Accepted in `domains/chirality/_Decomposition/gate_snapshots/GATE2_PHASE2_20260614T204403Z` by human approval on 2026-06-14. This batch is included in canonical `Atomic_Domain_Ledger.csv` and `Vocabulary_Map.csv`; the batch-scoped ledger remains supporting evidence.
