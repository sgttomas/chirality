# Chirality App-Dev Domain Decomposition

Package role: working surface

Status: **Gate 6 — Publish: PUBLICATION ASSEMBLED, AWAITING TERMINAL HUMAN
ACCEPTANCE.** Gates 1, 1.5-S, 2, 2.5, 3, 4, and 5 are CLOSED and ACCEPTED. The
final integrity validator passes clean (0 CRITICAL / 0 MAJOR). On the operator
acceptance statement — *"This domain decomposition is the accepted basis for
downstream work."* — this becomes the accepted basis and Gate 6 closes.

Gate chain (all ACCEPTED): **Gate 1** (`GATE1_ACCEPT_20260616_R2`) — manifest-backed
intake, 467 rows / 96 source units. **Gate 1.5-S** — skeleton review closed
(3,056 → 2,967 in-scope sections). **Gate 2** (`GATE2_ACCEPT_20260616`) — Phase-2
atomization complete: `Atomic_Domain_Ledger.csv` (**11,809 atoms**; IN 11,140 /
OUT 107 / TBD 562) + `Vocabulary_Map.csv` (844 terms); 96 atom-review HTML surfaces.
**Phase 2.5** — source catalog `SRCIDX_20260616T043733Z` (validate PASS; dense V2
embeddings BAAI/bge-base-en-v1.5) + BM25 + TOC priors. **Gate 3**
(`GATE3_ACCEPT_20260616`) — 16 flat faithful-to-author categories (PKG-00..10 1:1 +
5 cross-cutting); 11,140 IN each assigned one Category; ratification 16/16
`CLUSTER_COHERENT`, 0 blocking. **Gate 4** (`GATE4_ACCEPT_20260616`) — 59
knowledge-kind Knowledge Types + 279 per-deliverable Subjects; every IN atom carries
one KTY + Subject; ratification 59/59 `CLUSTER_COHERENT`, 0 blocking. **Gate 5**
(`GATE5_ACCEPT_20260616`) — section coverage attested; structural invariants pass
(UnassignedINUnits=0, UnitsWithoutKTY=0); 987 cov-empty in-scope sections attested
scaffold-for-fill (OI-014).

**Documented deferred caveats** (operator-ruled at Gate 6, published as part of the
accepted basis, not closure blockers): **OI-011** corpus drift (22 files re-stamped
to HEAD; re-atomization deferred to a future scope-change amendment) and **OI-013**
562 TBD-scope atoms (recorded as a deferred open issue; IN decomposition complete).
**Objectives layer omitted by design** per Deviation A — `annex_objectives.csv` is
header-only (0 objectives); principles are absorbed into Guidance/Playbook KTYs.

### Gate 6 — Publish (PUBLICATION ASSEMBLED)

Final published artifact for downstream agents. Heavy machine-truth lives in the
companion registers; this document is the concise control surface over them.

- **Domain Ledger** (required): `Domain_Ledger_Gate4_KTY_Draft.csv` — authoritative
  (11,809 atoms; every IN atom carries CategoryID + primary KnowledgeType + Subject).
  Published annex `annex_domain_ledger.csv` is the canonical ledger projection for the
  integrity validator / downstream. Phase-2 base ledger: `Atomic_Domain_Ledger.csv`.
- **Coverage & Telemetry** (required): `Gate5_Coverage_Telemetry.{json,csv}` (status
  `ACCEPTED_GATE5`), `Section_Coverage_Register.csv`, `Source_Coverage_Summary.csv`.
- **Vocabulary Map** (required): `Vocabulary_Map.csv` — 844 canonical terms.
- **Categories / Knowledge Types / Subjects**: `Category_Register.csv` (16),
  `Knowledge_Type_Register.csv` (59), `Knowledge_Subject_Register.csv` (279).
- **Decision / change log** (required): see *Decision Log / Change Log* below.
- **Companion Inventory** (required): `Companion_Inventory.csv` — full file-level
  inventory (see *Companion Inventory* below).
- **Objectives**: omitted by design (Deviation A); `annex_objectives.csv` header-only.
- **Integrity**: `validate_domain_decomposition_integrity.py` → **PASS** (0 CRITICAL /
  0 MAJOR / 0 MINOR); all six annexes resolve, coverage telemetry reconciles.
- **Review surfaces**: 96 per-source structure/atom-review HTML (`source_review_html/`,
  `atom_review_html/`) + 92 coverage-review HTML in final state; sidecar history retained.
- **Snapshot**: `gate_snapshots/GATE6_PUBLISH_<UTC>/` (+ `_LATEST_GATE6.md`) — written
  on terminal acceptance.

**What changed since the last revision (Gate 5 → Gate 6):** reconciled Gate-5
coverage telemetry to `ACCEPTED_GATE5` (status/revision re-stamped, `ObjectiveCount=0`
added, OI-id corrected); brought `Validation_Checks.csv` current with the Gate 2–6
closure record; added the canonical published annex layer (`annex_domain_ledger.csv`,
`annex_objectives.csv`); regenerated `Companion_Inventory.csv` (4 → 1,685 rows);
ruled OI-011 and OI-013 as documented deferred publish caveats. No decomposition
content changed — publish is assembly + finalization only.

### Gate 5 — Coverage & Telemetry (ACCEPTED)

- **Coverage** (`tools/decomp/build_gate5_coverage.py`, reusable-as-is, via pack-local
  shim `_adapter/gate5_make_source_register.py`): per-section IN/OUT/TBD atom counts +
  density class. 3,046 in-scope sections; density cov-empty 987 / cov-low 2 /
  cov-mid 381 / cov-high 1,676. `Section_Coverage_Register.csv`,
  `Source_Coverage_Summary.csv`, `Gate5_Coverage_Telemetry.{json,csv}`.
- **Structural invariants pass**: `UnassignedINUnits=0`, `UnitsWithoutKnowledgeTypeMapping=0`,
  `UnitsWithoutSubjectMapping=0`.
- **Zero-coverage attestation** (`_adapter/gate5_classify_coverage.py`, operator decision
  machine-classify + bulk-attest): the 987 cov-empty in-scope sections classified —
  376 STRUCTURAL_COMPONENT_HEADER, 368 EMPTY_STUB_SCAFFOLD, 124 OUT_TBD_ONLY, 60
  TEMPLATE_SUBSECTION, 59 GENUINE_GAP_CANDIDATE (leaf, >8 source lines). All attested
  **scaffold-for-fill**; none re-dispatched (OI-014). `Gate5_ZeroCoverage_Classification.csv`,
  `Gate5_GenuineGap_Shortlist.csv`.
- **Snapshot**: `gate_snapshots/GATE5_COVERAGE_20260616T163302Z/` (+ `_LATEST_GATE5.md`).

### Gate 4 — Knowledge Types & Subjects (ACCEPTED)

- **KTY axis = knowledge-kind (author doc-types).** CAT-001..011 (PKG deliverables)
  → 4 KTYs each: Datasheet→Reference, Specification, Guidance, Procedure (1:1 with
  persona canonical schemas). CAT-012..016 → content-kind KTYs. **59 KTYs**,
  `Knowledge_Type_Register.csv`. **Subjects = per-deliverable** (279), per-source/
  per-frontend-module for cross-cutting; `Knowledge_Subject_Register.csv`
  (`CoversUnits` populated, sum 11,140).
- **Assignment**: deterministic source-routing (`_adapter/gate4_assign.py`) — doc-kind
  + deliverable from each atom's `@repo` path; cross-cutting by SourceDoc. 11,140 IN
  atoms each → one primary KTY + Subject (100%; 0 unmapped). Ledger
  `Domain_Ledger_Gate4_KTY_Draft.csv` (`Gate4AssignmentStatus=ACCEPTED_GATE4`).
  **Lossless** — `UnitStatement`/`ContentHash`/`CategoryID` unchanged, no splits.
- **Binding ratification** (`_adapter/gate4_ratify.py`, dense index
  `SRCIDX_20260616T043733Z`): nearest-centroid cohesion computed **within each parent
  category**; **59/59 `CLUSTER_COHERENT`, 0 blocking**, own-centroid cosine median
  0.71–0.78, within-category cohesion 0.65–0.84. `KTY_Scope_Ratification.csv`.
- **Misassignment**: 49 candidates (0.4%, within-category prose adjacency) →
  `RESOLVED_SOURCE_ROUTING` (`G4BR-001`), 0 open. `KTY_Assignment_Findings.csv`.
- `IntendedUsers`/`WhenUsed` left `TBD` (persona allowance, operator-directed);
  `CanonicalSchema` set per KTY.
- **Snapshot**: `gate_snapshots/GATE4_KTY_20260616T161222Z/` (+ `_LATEST_GATE4.md`);
  proposal `gate4_kty/GATE4_KTY_PROPOSAL_20260616T155613Z/`.

### Gate 3 — Categories (ACCEPTED)

- **Categories**: 16 flat (`CAT-001..016`), reconciled from the cross-source TOC.
  The 11 author packages `PKG-00..10` preserved 1:1 as `CAT-001..011`; 5
  cross-cutting categories — product requirements/architecture (`CAT-012`),
  dev-process/build/release (`CAT-013`), coordination/scope-change governance
  (`CAT-014`), decomposition/reconciliation/closure (`CAT-015`), frontend source +
  harness docs (`CAT-016`). Register: `Category_Register.csv`.
- **Assignment**: deterministic author **source-routing** (`_adapter/gate3_assign.py`,
  rules `G3BR-001..007`); every IN atom inherits the category owning its
  author-placed PKG/source group. 11,140 IN assigned (one each); 562 TBD + 107 OUT
  uncategorized. **Lossless** — `UnitStatement`/`ContentHash` unchanged, no splits.
  Ledger: `Domain_Ledger_Gate3_Category_Draft.csv` (status `ACCEPTED_GATE3`).
- **Binding ratification** (`_adapter/gate3_ratify.py`, dense V2 index
  `SRCIDX_20260616T043733Z`, BAAI/bge-base-en-v1.5): primary signal =
  nearest-centroid cohesion; **16/16 `CLUSTER_COHERENT`, 0 blocking**, own-centroid
  cosine median 0.71–0.77 (~7.5× the 1/16 random baseline). Scope-query cosine +
  BM25 retained as diagnostics (0.75 human-gated, `G3BR-012`).
  `Category_Scope_Ratification.csv`.
- **Misassignment**: 330 candidates (3%; nearest centroid a different category by
  margin) — all semantic adjacency (spec/record near the feature it references),
  **RESOLVED_SOURCE_ROUTING** (operator-confirmed), 0 open.
  `Category_Assignment_Findings.csv`.
- **Snapshot**: `gate_snapshots/GATE3_CATEGORIES_20260616T153015Z/` (+ pointer
  `_LATEST_GATE3.md`); proposal `gate3_categories/GATE3_CATEGORY_PROPOSAL_20260616T074441Z/`.

### Phase 2.5 — Source catalog + retrieval (COMPLETE)

- **Catalog**: `tools/source_catalog/build_source_database.py --repo-root
  projects/chirality-app-dev --source-manifest …` → snapshot
  `_LocalIndexes/snapshots/SRCIDX_20260616T043733Z`; **validate PASS** (0
  blockers, 0 warnings). 319 `IncludeInIndex=YES` rows (all markdown).
- **BM25**: `tools/retrieval/build_source_index.py --no-embeddings` (lexical
  only; dense deferred). Smoke-tested OK.
- **TOC priors**: `tools/decomp/build_toc_priors.py` over 96
  `*_skeleton.reviewed.json` → `cross_source_toc_matrix.{md,csv}`.
- **Decisions logged this phase**:
  - **OI-010** — catalog tool v1 only BM25-chunks markdown; the 147 `frontend/src`
    code files + `docs/MANIFEST.json` set `IncludeInIndex=NO` (catalog-metadata
    only). Frontend code stays retrieval-covered via its grouped-unit atoms
    (ledger is chunked as `DECOMPOSITION_LEDGER_CSV`).
  - **OI-011** — live repo drifted to merge `bcb74dc09` after intake; 22 admitted
    files re-stamped to current. Re-atomization of the ~6 substantive drifted docs
    + grouped `SRC-FRONTEND-SRC` unit + admission of new files (D-APP-09/10,
    Closure_Acceptance_Audit, Dependency_Closure_Report) **deferred to a
    scope-change pass before Gate 6**.
  - **OI-012** — latent catalog-rebuild collision: snapshot-embedded ledger/
    section-node CSVs collide on `chunk_id`; worked around by excluding
    `gate_snapshots/` during the build; tool fix recommended.
- **Snapshot**: `gate_snapshots/PHASE2_5_20260616T044500Z/` (+ pointer
  `_LATEST_PHASE2_5.md`); telemetry `Phase2_5_Telemetry.json`.

Generated UTC: 2026-06-16T01:24:25Z · Gate 6 publication revision: 2026-06-16

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
- **Source manifest SHA-256 (live HEAD, re-stamped OI-011):** `e9000e97e04b2e913a3ea70d421765350456ffcde4e8fd20e12d1cf963d6e491`
- **Source catalog snapshot:** `_LocalIndexes/snapshots/SRCIDX_20260616T043733Z` (Phase 2.5; validate PASS).

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

See `Companion_Inventory.csv` — full file-level inventory of the package (**1,685
rows**, regenerated at Gate 6 by `_adapter/gate6_build_companion_inventory.py`).
Columns: `Filename`, `PackageRole`, `Description`. PackageRole breakdown:
**615 authoritative companion register**, **772 derived publication artifact**,
**283 snapshot / handoff artifact**, **14 pack-local adapter (tooling)**, **1 working
surface**. Covers all register classes from Phases 1–5: ledgers + annexes, category/
KTY/subject registers, ratifications + findings, vocabulary map, coverage telemetry +
section register, per-source skeletons / section-nodes / asset-manifests / review HTML
/ pack markdown, dispatch plans/briefs/outputs, per-source ledgers, TOC matrix, open
issues, validation checks, and the gate snapshot chain with `_LATEST_*` pointers.

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
| `OI-010` | RESOLVED_INDEX_METADATA | 148 non-md rows set index-metadata-only; frontend code stays covered via its atoms. |
| `OI-011` | DEFERRED_PUBLISH_CAVEAT | Corpus drift (22 files re-stamped to HEAD); re-atomization deferred to a future scope-change amendment. |
| `OI-012` | OPEN_TOOLING | Latent catalog-rebuild chunk_id collision vs gate_snapshots/; authorized shared-tool fix recommended. |
| `OI-013` | DEFERRED_PUBLISH_CAVEAT | 562 TBD-scope atoms uncategorized; recorded as a deferred open issue (IN decomposition complete). |
| `OI-014` | ACCEPTED_SCAFFOLD_FOR_FILL | 987 cov-empty in-scope sections attested scaffold-for-fill; none re-dispatched. |

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
| DEC-008 | 2026-06-16 | **Gate 3 accepted.** 16 flat faithful-to-author categories by deterministic source-routing; binding dense ratification 16/16 `CLUSTER_COHERENT`; 562 TBD deferred (OI-013). |
| DEC-009 | 2026-06-16 | **Gate 4 accepted.** KTY axis = knowledge-kind (author doc-types), 59 KTYs; subjects per-deliverable, 279; ratification 59/59 `CLUSTER_COHERENT`. |
| DEC-010 | 2026-06-16 | **Gate 5 accepted.** Machine-classify + bulk-attest coverage; 987 cov-empty in-scope sections attested scaffold-for-fill (OI-014); none re-dispatched. |
| DEC-011 | 2026-06-16 | **Gate 6 publish.** OI-011 (corpus drift) and OI-013 (562 TBD) ruled documented deferred caveats in the accepted basis (future scope-change amendments). Objectives omitted per Deviation A. Canonical published annex layer added; companion inventory regenerated; integrity validator PASS. |

## Gate 6 — Publication & Final Acceptance

DOMAIN_DECOMP for `chirality-app-dev` is assembled and published. All upstream
gates (1, 1.5-S, 2, 2.5, 3, 4, 5) are CLOSED and ACCEPTED; the final integrity
validator passes clean (0 CRITICAL / 0 MAJOR / 0 MINOR). The required published
sections are present — Domain Ledger, Coverage & Telemetry, Vocabulary Map,
Categories / Knowledge Types / Subjects, Decision/Change Log, and Companion
Inventory — and the per-source review surfaces are in final state.

Two documented deferred caveats are carried as part of the accepted basis (future
scope-change amendments, not closure blockers): **OI-011** (corpus drift;
re-atomization deferred) and **OI-013** (562 TBD-scope atoms). The Objectives layer
is omitted by design (Deviation A); `annex_objectives.csv` is header-only.

**Awaiting the operator's terminal acceptance statement:** *"This domain
decomposition is the accepted basis for downstream work."* On confirmation, the
Gate 6 publish snapshot `gate_snapshots/GATE6_PUBLISH_<UTC>/` (acceptance record,
publication manifest with SHA-256s, readiness packet, handoff state) and the
`_LATEST_GATE6.md` pointer are written, and DOMAIN_DECOMP is complete.
