# Batch 5 Setup - Work Surface Registry

Package role: snapshot / handoff artifact

BatchID: `BATCH5_WORK_SURFACE_REGISTRY_20260614T191710Z`

Status: GATE2_ACCEPTED_IN_PHASE2_CLOSURE

Generated UTC: 2026-06-14T19:19:15Z

## Accepted Upstream State

- Gate 1 acceptance snapshot: `domains/chirality/_Decomposition/gate_snapshots/GATE1_20260614T005942Z`
- Source manifest: `domains/chirality/_Sources/Source_Manifest.csv`
- Source manifest SHA-256 after admitting Batch 5 WSR rows: `6d9ea9bf796ab83a0e0e01fc5d0d24e095fcb6ce0bf6a6739d4f50fa0296509e`
- Current source catalog snapshot before the post-Batch5 rebuild: `domains/chirality/_LocalIndexes/_LATEST.md`
- Batch 2 status: GATE2_ACCEPTED_IN_PHASE2_CLOSURE
- Batch 3 status: GATE2_ACCEPTED_IN_PHASE2_CLOSURE
- Batch 4 status: GATE2_ACCEPTED_IN_PHASE2_CLOSURE
- Source-copy policy: `source_files_copied=false`

## Scope

Batch 5 is the human-directed work-surface registry atomization batch. It admits four registry Markdown files that describe the live organization and execution surfaces under `domains/` and `projects/` at high level. It intentionally captures structure, boundaries, workflow relationships, and review flags rather than app implementation detail or archived material.

| SourceDocID | Prefix | RepoRelPath | Lines | Sections | Dispatch Units |
|---|---|---|---:|---:|---:|
| `SRC-WSR-DOMAINS-CHIRALITY` | `WSR001` | `domains/chirality/_Decomposition/work_surface_registry/WSR-DOMAINS-CHIRALITY.md` | 82 | 11 | 1 |
| `SRC-WSR-DOMAINS-PIPING-DESIGN` | `WSR002` | `domains/chirality/_Decomposition/work_surface_registry/WSR-DOMAINS-PIPING-DESIGN.md` | 80 | 11 | 1 |
| `SRC-WSR-PROJECTS-CHIRALITY-APP-DEV` | `WSR003` | `domains/chirality/_Decomposition/work_surface_registry/WSR-PROJECTS-CHIRALITY-APP-DEV.md` | 98 | 11 | 1 |
| `SRC-WSR-PROJECTS-CHIRALITY-PIPING` | `WSR004` | `domains/chirality/_Decomposition/work_surface_registry/WSR-PROJECTS-CHIRALITY-PIPING.md` | 113 | 11 | 1 |

## SourceRef Policy

Batch 5 uses normal manifest-backed repo SourceRefs:

```text
@repo/<RepoRelPath>:L####|domains/chirality/_Decomposition/source_review_html/<SourceDocID>.html#<SectionID>
```

Each rendered brief carries `SOURCE_REF_BASE` from `Source_Decomp_Prefix_Map.csv`.

## Explicit Exclusions

- Archived and retired material remains strictly ignored.
- Vendor, build, cache, generated decomposition batches, local indexes/snapshots, and implementation details outside each work-surface boundary remain excluded.
- Project-specific knowledge domain decomposition remains deferred to future project-domain decompositions; Batch 5 captures only the monorepo work-surface organization around those projects.
- `LICENSE.md` is outside Batch 5 scope and is accepted separately in Batch 6.

## Generated Companions

- `Batch_Source_Register.csv` - authoritative companion register for selected Batch 5 source scope.
- `Dispatch_Unit_Register.csv` - authoritative companion register for per-unit brief/output paths.
- `Validation_Checks.csv` - setup and later worker QA / merge / render validation register.
- `domains/chirality/_Decomposition/dispatch_briefs/BATCH5_WORK_SURFACE_REGISTRY_20260614T191710Z` - one INIT-TASK brief per dispatch unit.
- `domains/chirality/_Decomposition/dispatch_outputs/BATCH5_WORK_SURFACE_REGISTRY_20260614T191710Z` - prepared disjoint output directories for worker CSVs.
- `domains/chirality/_Decomposition/per_source_ledgers/BATCH5_WORK_SURFACE_REGISTRY_20260614T191710Z` - reserved per-source merge output root.
- `domains/chirality/_Decomposition/vocabulary_seeds/BATCH5_WORK_SURFACE_REGISTRY_20260614T191710Z` - reserved per-source vocabulary seed output root.

## Worker Boundary

Workers must read only their assigned registry markdown `LINE_START..LINE_END`, cite the registry file with `SOURCE_REF_BASE`, write only their two allowed CSV targets, and return a valid `RUN_STATUS`.

## Closure Verdict

- Batch 5 setup: CLOSED / SETUP_READY.
- Batch 5 Phase 2 atomization: CLOSED / QA_PASS.
- Batch 5 Gate 2 normalization: CLOSED / ACCEPTED by Phase 2 closure.
- Batch 2, Batch 3, and Batch 4 are Gate-2 accepted in the Phase 2 closure snapshot.
