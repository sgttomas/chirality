# Chirality App-Dev Domain Decomposition

Package role: working surface

Status: **Gate 1 RE-ACCEPTED** (token `GATE1_ACCEPT_20260616_R2`); **Gate 1.5-S
skeleton review closed**. **Phase 2 atomization COMPLETE** — all 96 source units
/ 115 dispatch units atomized (individual-agent fan-out, ≤20 parallel), merged to
`Atomic_Domain_Ledger.csv` (**11,809 atoms**) + `Vocabulary_Map.csv` (844 terms);
96 atom-review HTML surfaces rendered. **Next: Gate 2** (binding atom review).

Generated UTC: 2026-06-16T01:24:25Z

DOMAIN_DECOMP agent persona; 6-gate methodology (Intake → Normalize → Categories
→ Knowledge Types → Coverage → Publish). This document is the concise control
surface; heavy machine-truth lives in the companion registers (see Companion
Inventory).

## Source Model

This domain pack decomposes the live development repository
`projects/chirality-app-dev/` and uses **manifest-backed** live repo files as
source truth. Source files are **not copied** into `_Sources/`; companions point
back to `@repo/<RepoRelPath>`.

- **Source repo root:** `projects/chirality-app-dev/` — `@repo/...` resolves
  here (cross-repo; differs from the `chirality` self-domain).
- **Pack root:** `domains/chirality-app-dev/` (chirality monorepo). Shared
  agents/skills/tools resolve against the monorepo root.
- **Accepted manifest:** `domains/chirality-app-dev/_Sources/Source_Manifest.csv` (467 rows)
- **Source manifest SHA-256:** `24fccecae56e01b4fbf3110fb700c80cb711ba456b73de6fd6a4d14d7e2aecd9`
- **Source catalog snapshot:** not built (Phase 2.5; after Gate 2).

## Intake Summary

| Metric | Value |
|---|---:|
| Manifest file rows | 467 |
| — atomizable component files | 466 |
| — index-only files | 1 |
| Atomizable **source units** | 96 |
| Index-only files (`docs/MANIFEST.json`) | 1 |
| Skeletons generated | 96 |
| Structure review HTML generated | 96 |
| Section-node CSVs generated | 96 |
| Generated grouped pack-markdown files | 80 |
| Total sections | 3,056 |
| In-scope sections (heuristic) | 3,056 |
| Dispatch units | 108 |
| Oversized dispatch units | 0 |
| Skeleton/render failures | 0 |

## Group Telemetry

| SourceGroup | Units | Components | Source Lines | Sections | Dispatch Units | Atomize |
|---|---:|---:|---:|---:|---:|:--|
| `EXECUTION_DELIVERABLE` | 53 | 238 | 19,019 | 1,992 | 53 | YES (KT docs by suffix, grouped) |
| `EXECUTION_GOVERNANCE` | 26 | 65 | 4,411 | 468 | 27 | YES (grouped per folder) |
| `FRONTEND_SRC` | 1 | 147 | 45,073 | 201 | 11 | YES (one grouped code unit) |
| `PRODUCT_DOCS` | 12 | 12 | 4,694 | 369 | 13 | YES (per file) |
| `FRONTEND_DOCS` | 3 | 3 | 344 | 19 | 3 | YES (per file) |
| `ROOT_DOCS` | 1 | 1 | 96 | 7 | 1 | YES (per file) |
| **Atomizable total** | **96** | **466** | **73,637** | **3,056** | **108** | |
| `docs/MANIFEST.json` | — | 1 | — | — | — | NO (index-only) |

## Deliverable Admission Rule (revised at reopen; OI-009 = suffix-match)

Each `execution/.../1_Working/DEL-XX-YY_*/` deliverable admits its **knowledge-type
docs by basename suffix** — anything ending in `Datasheet.md`, `Specification.md`,
`Guidance.md`, or `Procedure.md`. This keeps the canonical four per deliverable
**and** nested `Packet_Datasheet`/`Packet_Specification`/`Packet_Procedure`/
`Case_Datasheet` docs in the PKG-00 closure deliverables (238 component files
across 53 units; 51 deliverables keep 4, DEL-00-01 keeps 11, DEL-00-02 keeps 23).
**Not admitted:** the six meta docs per deliverable (`_SEMANTIC`,
`_SEMANTIC_LENSING`, `_CONTEXT`, `_DEPENDENCIES`, `_REFERENCES`, `_STATUS`),
non-KT packet docs (`Packet_QA`/`Packet_Rationale`/`Packet_Contract`/
`SCOPE_CHANGE_INIT`), and `CONTROL`/`README`. Re-admitting the nested packets
reintroduces byte-identical duplicates in DEL-00-02 → handled by OI-006 Option A
(ContentHash dedup at the Gate-2 merge).

## Source-Unit Grouping Policy

- **Per-file** source units: `AGENTS.md`, each `docs/*.md`, each frontend prose
  doc. SourceRef mode `REPO_LINE`.
- **Grouped** source units (SourceRef mode `COMPONENT_MAP`): each deliverable
  (its KT docs → one unit, 53 units); execution governance folders grouped by
  immediate parent directory (26 units); and all of `frontend/src` (+ `electron`,
  `scripts`, config) as one grouped code unit `SRC-FRONTEND-SRC` (147 files).
- Grouped units write a generated pack markdown under `source_pack_markdown/`
  (worker/review substrate only). The `source_components` map in each grouped
  asset manifest carries per-component generated→source line offsets so Phase-2
  atoms cite original `@repo` component files.

## SourceRef Adapter Policy

```text
# per-file (REPO_LINE):
@repo/<RepoRelPath>:L####|domains/chirality-app-dev/_Decomposition/source_review_html/<SourceUnitID>.html#<SectionID>
# grouped (COMPONENT_MAP) — atoms cite the original component, resolved via source_components:
@repo/<component RepoRelPath>:L####|domains/chirality-app-dev/_Decomposition/source_review_html/<SourceUnitID>.html#<SectionID>
```

## Gate 1.5 Asset Surface Policy

Markdown-only corpus with empty asset manifests; per-kind asset surfaces
(equations/figures/tables/images/folios) and the 1.5-P prose-validate prefilter
are **N/A**. Gate 1.5 reduces to **1.5-S skeleton review** on the structure-mode
HTML under `source_review_html/`.

## Gate 1.5-S Skeleton Review (CLOSED)

Machine-assisted pre-pass (`_adapter/review_15s.py`) produced
`*_skeleton.reviewed.json` + reviewed dispatch plans for all 96 units (0
failures). The deliverable knowledge-type-doc trim was applied at **admission**
(Gate 1), so 1.5-S only marks out-of-scope the generated `# Source Pack`
boilerplate headers (80 grouped units) and governance `_LATEST.md` pointers (9).
Result: **3,056 → 2,967 in-scope sections** (89 OUT), **104 reviewed dispatch
units**. Register: `Gate1.5_Skeleton_Review.csv`; telemetry:
`Gate1.5_Review_Telemetry.json`. Reviewed skeletons are the Phase-2 input.

## Phase 2 Pilot (EXECUTED — awaiting reassessment)

Runner: **individual agents, pilot only** (operator decision). Batch
`BATCHP_PILOT_DOCS_20260616T022706Z`. Groups: ROOT_DOCS (1) + PRODUCT_DOCS (14
dispatch units over 13 files; PRD split into 2) + FRONTEND_DOCS (3) = **17
dispatch units**. All `TASK + domain-source-atomize`, all per-file `REPO_LINE`.

- Per-unit atom CSVs: `dispatch_outputs/<batch>/<SourceUnitID>/UNIT-*_atoms.csv`
- Briefs: `dispatch_briefs/<batch>/` (built with alias map
  `_adapter/brief_source_ref_map.csv` so `SOURCE_REF_BASE` resolves by unit id —
  the shared brief tool keys on `SourceDocID`/`SourceName`, not our `SourceUnitID`).
- Per-source ledgers: `per_source_ledgers/<batch>/` (16 ledgers, stable
  `HBA-<prefix>-NNNNN` IDs).
- Pilot ledger: `Atomic_Domain_Ledger.PILOT.csv` (**2,098 atoms**; IN 2,078 /
  OUT 14 / TBD 6; 0 unresolved Corrects, no prefix collisions).
- Pilot vocab: `Vocabulary_Map.PILOT.csv` (174 canonical terms).
- Atom-review HTML (Gate-2 surface): `atom_review_html/<batch>/<SourceUnitID>.html` (16/16).
- Telemetry: `Phase2_Pilot_Telemetry.json`.
- Independent QA over all 17 per-unit CSVs: 0 problems (header, `sha1[:12]`
  ContentHash, SectionID∈targets, MD line∈range, monotonic LocalSeq, `@repo` refs).
- 6 TBD atoms surfaced for Gate-2 rulings (5 in VALIDATION_STRATEGY §6 open
  decisions; 1 in RELEASE_QUALITY_GATES re D-APP-01/02 Pi ruling).

## Phase 2 Atomization (COMPLETE) — Gate 2 pending

Runner: **individual agents, ≤20 parallel**, staged by group with QA + per-source
merge barriers between groups (operator decision). All grouped units validated the
`COMPONENT_MAP` SourceRef path before fan-out (DEL-01-01 line-offset mapping
verified against original `@repo` files).

| Group | Batch | Units | Atoms |
|---|---|---:|---:|
| ROOT+PRODUCT_DOCS+FRONTEND_DOCS (pilot) | `BATCHP_PILOT_DOCS_20260616T022706Z` | 16 src / 17 disp | 2,098 |
| EXECUTION_DELIVERABLE | `BATCH1_DELIVERABLE_20260616T025537Z` | 53 / 53 | 6,685 |
| EXECUTION_GOVERNANCE | `BATCH2_GOVERNANCE_20260616T031703Z` | 26 / 23 | 1,536 |
| FRONTEND_SRC | `BATCH3_FRONTENDSRC_20260616T032850Z` | 1 / 11 | 1,490 |
| **Final ledger (cross-source, deduped)** | — | **96 / 104** | **11,809** |

- **Final ledger:** `Atomic_Domain_Ledger.csv` — 11,809 atoms, unique
  `HBA-<prefix>-NNNNN` IDs (0 dup), 0 ContentHash mismatches, 0 unresolved
  Corrects; **IN 11,140 / TBD 562 / OUT 107**; 92 source docs (4 governance
  parent-dir containers are header-only, content in dated subfolders).
- **Vocabulary:** `Vocabulary_Map.csv` — 844 canonical terms (104 seed files).
- **Gate-2 surfaces:** `atom_review_html/<batch>/<SourceUnitID>.html` (96 files,
  atom-review mode).
- **Per-source ledgers:** `per_source_ledgers/<batch>/` (96).
- **Telemetry:** `Phase2_Final_Telemetry.json`, `Phase2_Pilot_Telemetry.json`.
- **Snapshot:** `gate_snapshots/PHASE2_20260616T033617Z/` (pointer
  `gate_snapshots/_LATEST_PHASE2.md`).
- Independent QA after every group: 0 problems (header, `sha1[:12]` ContentHash,
  SectionID∈targets, MD line∈range, monotonic LocalSeq, `@repo` refs; grouped
  units additionally verified citing only in-unit component files).
- Pack-local drivers: `_adapter/phase2_run.py` (group briefs),
  `_adapter/phase2_merge.py` (group QA+merge+HTML), `_adapter/brief_source_ref_map.csv`
  (alias map so the shared brief tool resolves `SOURCE_REF_BASE` by SourceUnitID).
- **562 TBD atoms** carried for Gate-2 ruling (mostly deliverable open items:
  unassigned ResponsibleParty, declared-but-unextracted dependencies, the
  recurring PRD `HASH_MISMATCH` source-state warning, and conflict-table rows).

## Frontend & Excluded Disposition

- `frontend/src/**` (+ `electron`, `scripts`, config; 147 files) is **atomized**
  as a single grouped source unit `SRC-FRONTEND-SRC` (`COMPONENT_MAP`).
- **Excluded entirely** (not indexed): `execution/` process logs (~350 files);
  deliverable meta docs + non-KT files; `execution` CSV/JSON/scripts; ~2.2 GB
  generated/vendored frontend output; repo `.archive/`, `.github/`, `init/`,
  `plans/`, `provenance/`, the `.zip`.
- `docs/MANIFEST.json` is the only index-only file (`Index_Only_Register.csv`).

## References

- `domains/chirality-app-dev/_Sources/Source_Manifest.csv` — file-level source admission (467 rows).
- `domains/chirality-app-dev/_Sources/SOURCE_BOUNDARY.md` — source boundary.
- `domains/chirality-app-dev/_Decomposition/Source_Decomp_Prefix_Map.csv` — source-unit map.
- `domains/chirality-app-dev/_Decomposition/Source_Unit_Component_Map.csv` — grouped-unit provenance.
- `domains/chirality-app-dev/_Decomposition/Intake_Telemetry.{csv,json}` — intake telemetry.
- `domains/chirality-app-dev/_Decomposition/Index_Only_Register.csv` — index-only files.

## Companion Inventory

See `Companion_Inventory.csv` for the full file-level inventory of the canonical
working package (manifest, boundary, prefix/component maps, telemetry, per-unit
skeletons / dispatch plans / asset manifests / structure HTML / section-node
CSVs / pack markdown, open issues, validation checks).

## Open Issues

See `Open_Issues_Register.csv`.

| IssueID | Status | Issue |
|---|---|---|
| `OI-001` | RESOLVED_GATE_1 | frontend/src (147 files) atomized as one grouped unit `SRC-FRONTEND-SRC`. |
| `OI-002` | ACCEPTED_GATE_1 | ~350 process logs excluded entirely (not indexed). |
| `OI-003` | AWAITING_GATE_1 | REVISED: deliverable admits KT docs by suffix (238 files, 53 units); meta/non-KT not admitted. |
| `OI-004` | ACCEPTED_GATE_1 | Gate 1.5 reduces to 1.5-S (asset surfaces N/A). |
| `OI-005` | RECORDED | Cross-repo: @repo resolves against projects/chirality-app-dev. |
| `OI-006` | ACCEPTED_OPTION_A | DEL-00-02 nested duplicate packets re-admitted under suffix-match; ContentHash dedup at Gate-2 merge. |
| `OI-007` | ACCEPTED_STAGE_PHASE_2 | 96 units / 3,056 sections / 108 dispatch units — stage Phase-2 atomization. |
| `OI-008` | ACCEPTED_GATE_1 | All admitted sections default in-scope; refine at Gate 1.5-S. |
| `OI-009` | RESOLVED_SUFFIX_MATCH | Deliverable KT docs admitted by suffix; DEL-00-01→11, DEL-00-02→23 components. |

## Decision Log / Change Log

| DecisionID | Date | Decision |
|---|---|---|
| DEC-001 | 2026-06-15 | New domain pack at `domains/chirality-app-dev/` decomposing sibling repo `projects/chirality-app-dev/`; manifest-backed, no source files copied. |
| DEC-002 | 2026-06-15 | V1 boundary: include `AGENTS.md`, `docs/`, `execution/`, `frontend/`; exclude other top-level folders and ~2.2 GB generated/vendored frontend output. |
| DEC-003 | 2026-06-15 | `frontend/src` code (147 files) atomized as ONE grouped source unit `SRC-FRONTEND-SRC` (OI-001). |
| DEC-004 | 2026-06-15 | `execution` markdown only (CSV/JSON/scripts excluded); process logs excluded entirely. |
| DEC-005 | 2026-06-15 | Execution grouped per deliverable (53) and per governance folder (26); docs/root/frontend-prose per file. |
| DEC-006 | 2026-06-16 | **Gate 1 reopened.** Deliverable source admission trimmed to knowledge-type docs; meta docs + non-KT files excluded from admission — operator direction. |
| DEC-007 | 2026-06-16 | Deliverable admission uses basename **suffix-match** (OI-009): nested `Packet_*`/`Case_*` KT docs admitted in DEL-00-01/02. Manifest 467 rows; in-scope sections 3,056. |

## Gate 1 Confirmation Packet — RE-ACCEPTED

Gate 1 was re-accepted by the operator on 2026-06-16 (token
`GATE1_ACCEPT_20260616_R2`): the revised manifest-backed source set (deliverables
admit KT docs by suffix; 467 manifest rows / 466 atomizable components / 96
source units), the per-deliverable/per-folder grouping plus the grouped
frontend-source unit, the excluded process logs / meta docs and index-only
`docs/MANIFEST.json`, the 96-unit skeleton inventory, and the structure-mode
review HTMLs are accepted as the intended chirality-app-dev DOMAIN_DECOMP intake.
All Gate-1 open decisions resolved (OI-009 = suffix-match).

Next gate: **Gate 1.5-S** skeleton review (asset sub-gates N/A). Phase 2
atomization is staged per OI-007.
