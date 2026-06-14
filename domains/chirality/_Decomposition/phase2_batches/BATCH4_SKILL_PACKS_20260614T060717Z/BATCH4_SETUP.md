# Batch 4 Setup - Skill Packs

Package role: snapshot / handoff artifact

BatchID: `BATCH4_SKILL_PACKS_20260614T060717Z`

Status: GATE2_ACCEPTED_IN_PHASE2_CLOSURE

Generated UTC: 2026-06-14T06:07:39Z

## Accepted Upstream Snapshot

- Gate 1 acceptance snapshot: `domains/chirality/_Decomposition/gate_snapshots/GATE1_20260614T005942Z`
- Source manifest: `domains/chirality/_Sources/Source_Manifest.csv`
- Source manifest SHA-256: `86891c8d0b7be3aef68b3a32bd32284069c505ea2ef64161c9cfd3155e1d8574`
- Current source catalog snapshot: `domains/chirality/_LocalIndexes/_LATEST.md`
- Batch 2 status at setup: GATE2_ACCEPTED_IN_PHASE2_CLOSURE
- Batch 3 status at setup: GATE2_ACCEPTED_IN_PHASE2_CLOSURE
- Source-copy policy: `source_files_copied=false`

## Scope

Batch 4 is the authorized grouped Phase 2 atomization batch for active skill contracts. It groups each `skills/<name>/` directory as one source and groups `skills/README.md` plus `skills/SKILL_TEMPLATE.md` as one skill-system meta-contract source. `LICENSE.md` is outside Batch 4 scope and is accepted separately in Batch 6.

| SourceDocID | Prefix | Grouped RepoRelPath | Lines | Sections | Dispatch Units |
|---|---|---|---:|---:|---:|
| `SRC-SKILLPACK-META` | `SKP000` | `skills/{README.md,SKILL_TEMPLATE.md}` | 311 | 32 | 1 |
| `SRC-SKILLPACK-CONTENT-DIGEST` | `SKP001` | `skills/content-digest/` | 302 | 52 | 1 |
| `SRC-SKILLPACK-DBM-CONCORDANCE-SEED` | `SKP002` | `skills/dbm-concordance-seed/` | 601 | 45 | 1 |
| `SRC-SKILLPACK-DBM-CONCORDANCE-VERIFY` | `SKP003` | `skills/dbm-concordance-verify/` | 299 | 39 | 1 |
| `SRC-SKILLPACK-DBM-DRAFT-REVIEW` | `SKP004` | `skills/dbm-draft-review/` | 461 | 50 | 1 |
| `SRC-SKILLPACK-DBM-POSTAUTHOR-CONCORDANCE` | `SKP005` | `skills/dbm-postauthor-concordance/` | 385 | 48 | 1 |
| `SRC-SKILLPACK-DBM-PUBLISH` | `SKP006` | `skills/dbm-publish/` | 526 | 47 | 1 |
| `SRC-SKILLPACK-DBM-SECTION-PUBLISH` | `SKP007` | `skills/dbm-section-publish/` | 630 | 59 | 1 |
| `SRC-SKILLPACK-DECOMPOSITION-PACKAGE-REVIEW` | `SKP008` | `skills/decomposition-package-review/` | 506 | 46 | 1 |
| `SRC-SKILLPACK-DELIVERABLE-CONSISTENCY` | `SKP009` | `skills/deliverable-consistency/` | 242 | 29 | 1 |
| `SRC-SKILLPACK-DEPENDENCY-EXTRACT` | `SKP010` | `skills/dependency-extract/` | 616 | 69 | 1 |
| `SRC-SKILLPACK-DOMAIN-DOCUMENTS` | `SKP011` | `skills/domain-documents/` | 905 | 71 | 1 |
| `SRC-SKILLPACK-DOMAIN-PROSE-VALIDATE` | `SKP012` | `skills/domain-prose-validate/` | 413 | 47 | 1 |
| `SRC-SKILLPACK-DOMAIN-SOURCE-ATOMIZE` | `SKP013` | `skills/domain-source-atomize/` | 530 | 54 | 1 |
| `SRC-SKILLPACK-DRAWING-EXTRACT-PAGE` | `SKP014` | `skills/drawing-extract-page/` | 983 | 97 | 1 |
| `SRC-SKILLPACK-DRAWING-TITLEBLOCK-PAGE` | `SKP015` | `skills/drawing-titleblock-page/` | 256 | 34 | 1 |
| `SRC-SKILLPACK-EQUATION-BBOX-DETECT` | `SKP016` | `skills/equation-bbox-detect/` | 481 | 54 | 1 |
| `SRC-SKILLPACK-EQUATION-FLAG-INTERPRET` | `SKP017` | `skills/equation-flag-interpret/` | 434 | 49 | 1 |
| `SRC-SKILLPACK-EQUIPMENT-COSTING-EXTRACT` | `SKP018` | `skills/equipment-costing-extract/` | 405 | 53 | 1 |
| `SRC-SKILLPACK-EQUIPMENT-EXTRACT` | `SKP019` | `skills/equipment-extract/` | 349 | 48 | 1 |
| `SRC-SKILLPACK-ESTIMATE-PREP` | `SKP020` | `skills/estimate-prep/` | 998 | 101 | 1 |
| `SRC-SKILLPACK-ESTIMATE-SNAPSHOT` | `SKP021` | `skills/estimate-snapshot/` | 521 | 68 | 1 |
| `SRC-SKILLPACK-FOUR-DOCUMENTS` | `SKP022` | `skills/four-documents/` | 444 | 46 | 1 |
| `SRC-SKILLPACK-KTY-CONTENT-REMEDIATE` | `SKP023` | `skills/kty-content-remediate/` | 612 | 57 | 1 |
| `SRC-SKILLPACK-KTY-METADATA-ALIGN` | `SKP024` | `skills/kty-metadata-align/` | 482 | 47 | 1 |
| `SRC-SKILLPACK-LENS-REGISTER` | `SKP025` | `skills/lens-register/` | 699 | 78 | 1 |
| `SRC-SKILLPACK-PANDID-VALVE-SYMBOL-INSTANCE` | `SKP026` | `skills/pandid-valve-symbol-instance/` | 102 | 12 | 1 |
| `SRC-SKILLPACK-PANDID-VALVE-TILE` | `SKP027` | `skills/pandid-valve-tile/` | 290 | 36 | 1 |
| `SRC-SKILLPACK-PDF2MD` | `SKP028` | `skills/pdf2md/` | 310 | 37 | 1 |
| `SRC-SKILLPACK-PDF2MD-FOLIO-EXTRACT` | `SKP029` | `skills/pdf2md-folio-extract/` | 438 | 44 | 1 |
| `SRC-SKILLPACK-PDF2MD-PAGE` | `SKP030` | `skills/pdf2md-page/` | 391 | 45 | 1 |
| `SRC-SKILLPACK-PDF2MD-PAGE-ASSETS` | `SKP031` | `skills/pdf2md-page-assets/` | 526 | 50 | 1 |
| `SRC-SKILLPACK-PDF2MD-PAGE-FULL` | `SKP032` | `skills/pdf2md-page-full/` | 511 | 47 | 1 |
| `SRC-SKILLPACK-PROPOSAL-FORMAT` | `SKP033` | `skills/proposal-format/` | 266 | 38 | 1 |
| `SRC-SKILLPACK-SCC-RESOLUTION-CASE` | `SKP034` | `skills/scc-resolution-case/` | 223 | 26 | 1 |
| `SRC-SKILLPACK-SCOPE-CHANGE-PACKET` | `SKP035` | `skills/scope-change-packet/` | 249 | 25 | 1 |
| `SRC-SKILLPACK-SEMANTIC-LENSING` | `SKP036` | `skills/semantic-lensing/` | 259 | 35 | 1 |
| `SRC-SKILLPACK-SEMANTIC-MATRIX-BUILD` | `SKP037` | `skills/semantic-matrix-build/` | 864 | 89 | 1 |

## SourceRef Policy

Batch 4 uses grouped-source component maps. Generated pack markdown is a worker/review substrate only. Atom SourceRefs must cite original repo component files:

```text
@repo/<component RepoRelPath>:L####|domains/chirality/_Decomposition/source_review_html/<SourceDocID>.html#<SectionID>
```

The line conversion map lives in each grouped source asset manifest under `source_components`; briefs include `SOURCE_REF_MODE: COMPONENT_MAP`.

## Generated Companions

- `Batch_Source_Register.csv` - authoritative companion register for selected Batch 4 grouped source scope.
- `Dispatch_Unit_Register.csv` - authoritative companion register for per-unit brief/output paths.
- `Validation_Checks.csv` - setup and later worker QA / merge / render validation register.
- `domains/chirality/_Decomposition/source_pack_markdown/BATCH4_SKILL_PACKS_20260614T060717Z/` - generated grouped markdown substrates.
- `domains/chirality/_Decomposition/dispatch_briefs/BATCH4_SKILL_PACKS_20260614T060717Z/` - one INIT-TASK brief per dispatch unit.
- `domains/chirality/_Decomposition/dispatch_outputs/BATCH4_SKILL_PACKS_20260614T060717Z/` - prepared disjoint output directories for worker CSVs.
- `domains/chirality/_Decomposition/per_source_ledgers/BATCH4_SKILL_PACKS_20260614T060717Z/` - reserved per-source merge output root.
- `domains/chirality/_Decomposition/vocabulary_seeds/BATCH4_SKILL_PACKS_20260614T060717Z/` - reserved per-source vocabulary seed output root.

## Worker Boundary

Workers must read only assigned generated markdown `LINE_START..LINE_END`, use `ASSET_MANIFEST_PATH.source_components` to cite original repo component lines, write only their two allowed CSV targets, and return a valid `RUN_STATUS`.

## Closure Verdict

- Batch 4 setup: CLOSED / SETUP_READY.
- Batch 4 Phase 2 atomization: CLOSED / QA_PASS.
- Batch 4 Gate 2 normalization: CLOSED / ACCEPTED by Phase 2 closure.
- Batch 2 and Batch 3 are Gate-2 accepted in the Phase 2 closure snapshot.
