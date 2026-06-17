# Chirality Piping Domain Decomposition

Package role: working surface

Status: **Gate 6 — Publish: ACCEPTED** (token `GATE6_ACCEPT_20260617`, snapshot
`gate_snapshots/GATE6_PUBLISH_20260617T162204Z`, 2026-06-17T16:22:04Z). **DOMAIN_DECOMP for `chirality-piping`
is COMPLETE** — all six gates CLOSED and ACCEPTED. The operator confirmed:
*"Accepted."* The final integrity validator passes clean (0 CRITICAL / 0 MAJOR /
0 MINOR).

Gate chain (all ACCEPTED): **Gate 1** — manifest-backed intake, 884 manifest rows /
**158** atomizable source units (+38 index-only schema files). **Gate 1.5-S** —
skeleton review closed (5,035 → 4,924 in-scope sections; 111 OUT pack-boilerplate).
**Gate 2** — Phase-2 atomization complete: `Atomic_Domain_Ledger.csv` (**21,912
atoms**; IN 21,256 / OUT 147 / TBD 509) + `Vocabulary_Map.csv` (1,812 terms).
**Phase 2.5** — source catalog `SRCIDX_20260617T014930Z` (dense V2 embeddings
BAAI/bge-base-en-v1.5 + BM25 + TOC priors). **Gate 3** — **30** faithful-to-author
categories (18 author packages PKG-00..17 → CAT-001..018 1:1 + 12 cross-cutting
CAT-019..030); 21,256 IN each assigned one Category; ratification **30/30
`CLUSTER_COHERENT`**, 0 blocking; 943 misassignment candidates `RESOLVED_SOURCE_ROUTING`.
**Gate 4** — **98** knowledge-kind Knowledge Types + **630** Subjects; every IN atom
carries one primary KTY + Subject; ratification **98/98 `CLUSTER_COHERENT`**, 0
blocking; 99 candidates `RESOLVED_SOURCE_ROUTING`. **Gate 5** — section coverage
attested; structural invariants pass (UnassignedINUnits=0, UnitsWithoutKTY=0); 1,402
cov-empty in-scope sections attested scaffold-for-fill (OI-024).

**Documented deferred caveats** (published as part of the accepted basis, not
closure blockers): **509 TBD-scope atoms** (OI-025; recorded as a deferred open
issue — IN decomposition complete) and **147 OUT atoms** (out of scope by author
disposition). **Objectives layer omitted by design** per Deviation A —
`annex_objectives.csv` is header-only (0 objectives); principles are absorbed into
Guidance/Playbook KTYs.

### Gate 6 — Publish (PUBLICATION ASSEMBLED)

Final published artifact for downstream agents. Heavy machine-truth lives in the
companion registers; this document is the concise control surface over them.

- **Domain Ledger** (required): `Domain_Ledger_Gate4_KTY_Draft.csv` — authoritative
  (21,912 atoms; every IN atom carries CategoryID + primary KnowledgeType + Subject).
  Published annex `annex_domain_ledger.csv` is the canonical ledger projection for the
  integrity validator / downstream. Phase-2 base ledger: `Atomic_Domain_Ledger.csv`.
- **Coverage & Telemetry** (required): `Gate5_Coverage_Telemetry.{json,csv}` (status
  `ACCEPTED_GATE5`), `Section_Coverage_Register.csv`, `Source_Coverage_Summary.csv`.
- **Vocabulary Map** (required): `Vocabulary_Map.csv` — 1,812 canonical terms.
- **Categories / Knowledge Types / Subjects**: `Category_Register.csv` (30),
  `Knowledge_Type_Register.csv` (98), `Knowledge_Subject_Register.csv` (630).
- **Decision / change log** (required): see *Decision Log / Change Log* below.
- **Companion Inventory** (required): `Companion_Inventory.csv` — full file-level
  inventory (see *Companion Inventory* below).
- **Objectives**: omitted by design (Deviation A); `annex_objectives.csv` header-only.
- **Integrity**: `validate_domain_decomposition_integrity.py` → **PASS** (0 CRITICAL /
  0 MAJOR / 0 MINOR); all six annexes resolve, coverage telemetry reconciles.
- **Review surfaces**: per-source structure/atom-review HTML (`source_review_html/`,
  `atom_review_html/`); Gate-5 coverage-review HTML deferred (operator-approved skip).
- **Snapshot**: `gate_snapshots/GATE6_PUBLISH_<UTC>/` (+ `_LATEST_GATE6.md`) — written
  on terminal acceptance.

### Gate 5 — Coverage & Telemetry (ACCEPTED)

- **Coverage** (`tools/decomp/build_gate5_coverage.py`, reusable-as-is, via pack-local
  shim `_adapter/gate5_make_source_register.py` + skip-missing-doc wrapper
  `_adapter/gate5_build_coverage.py`): per-section IN/OUT/TBD atom counts + density
  class. 158 sources; **5,035 sections** (all in-scope); density cov-empty 1,402 /
  cov-low 3 / cov-mid 875 / cov-high 2,755. **3,633 sections carry IN atoms.**
- **Structural invariants pass**: `UnassignedINUnits=0`, `UnitsWithoutKnowledgeTypeMapping=0`.
- **Zero-coverage attestation** (`_adapter/gate5_classify_coverage.py`): the 1,402
  cov-empty in-scope sections classified — 581 STRUCTURAL_COMPONENT_HEADER, 560
  EMPTY_STUB_SCAFFOLD, 139 OUT_TBD_ONLY, 76 TEMPLATE_SUBSECTION, 46 GENUINE_GAP_CANDIDATE.
  All attested **scaffold-for-fill** (RESOLVE_SCAFFOLD_FOR_FILL); none re-dispatched
  (OI-024). `Gate5_ZeroCoverage_Classification.csv`, `Gate5_GenuineGap_Shortlist.csv`.
- **Snapshot**: `gate_snapshots/GATE5_COVERAGE_20260617T160317Z/` (token
  `GATE5_ACCEPT_20260617`; + `_LATEST_GATE5.md`); proposal
  `gate5_coverage/GATE5_COVERAGE_PROPOSAL_20260617T153653Z/`.

### Gate 4 — Knowledge Types & Subjects (ACCEPTED)

- **KTY axis = knowledge-kind.** The 18 deliverable categories CAT-001..018
  (PKG-00..17) → 4 KTYs each: Datasheet→Reference, Specification, Guidance,
  Procedure (1:1 with persona canonical schemas; 72 KTYs). The 12 cross-cutting
  categories CAT-019..030 → content-kind KTYs (26 KTYs). **98 KTYs**,
  `Knowledge_Type_Register.csv`. **Subjects** = per-deliverable (deliverable cats),
  per-source-doc (doc cats), per-source-directory (the 5 code cats) — **630**,
  `Knowledge_Subject_Register.csv` (`CoversUnits` populated, sum 21,256).
- **Assignment**: deterministic source-routing (`_adapter/gate4_assign.py`) — doc-kind
  + deliverable from each atom's `@repo` path; cross-cutting by SourceDoc / directory.
  21,256 IN atoms each → one primary KTY + Subject (100%; 0 unmapped; 0 empty KTYs).
  Ledger `Domain_Ledger_Gate4_KTY_Draft.csv` (`Gate4AssignmentStatus=ACCEPTED_GATE4`).
  **Lossless** — `UnitStatement`/`ContentHash`/`CategoryID` unchanged (0 diffs over all
  21,912 rows), no splits.
- **Binding ratification** (`_adapter/gate4_ratify.py`, dense index
  `SRCIDX_20260617T014930Z`): nearest-centroid cohesion computed **within each parent
  category**; **98/98 `CLUSTER_COHERENT`, 0 blocking**, own-centroid cosine median
  0.749 (range 0.713–0.784), within-category cohesion median 0.716.
  `KTY_Scope_Ratification.csv`.
- **Misassignment**: 99 candidates (0.47%, within-category prose adjacency) →
  `RESOLVED_SOURCE_ROUTING` (`G4BR-001`), 0 open. `KTY_Assignment_Findings.csv`.
- `IntendedUsers`/`WhenUsed` left `TBD` (persona allowance); `CanonicalSchema` set per KTY.
- **Snapshot**: `gate_snapshots/GATE4_KTY_20260617T153218Z/` (token
  `GATE4_ACCEPT_20260617`; + `_LATEST_GATE4.md`); proposal
  `gate4_kty/GATE4_KTY_PROPOSAL_20260617T152804Z/`.

### Gate 3 — Categories (ACCEPTED)

- **Categories**: 30, reconciled from the cross-source TOC. The 18 author packages
  `PKG-00..17` preserved 1:1 as `CAT-001..018`; 12 cross-cutting categories
  `CAT-019..030` (product requirements/architecture, dev-process/build/release/
  validation, IP/security/privacy, guides/examples, decomposition records,
  scope-change governance, repo operating posture, and the five code bodies —
  core/apps/tests/tools/validation). Register: `Category_Register.csv`.
- **Assignment**: deterministic author **source-routing** (`_adapter/gate3_assign.py`,
  rules `G3BR-001..007`); every IN atom inherits the category owning its
  author-placed PKG/source group. 21,256 IN assigned (one each); 509 TBD + 147 OUT
  uncategorized. **Lossless** — `UnitStatement`/`ContentHash` unchanged, no splits.
  Ledger: `Domain_Ledger_Gate3_Category_Draft.csv`.
- **Binding ratification** (`_adapter/gate3_ratify.py`, dense V2 index
  `SRCIDX_20260617T014930Z`, BAAI/bge-base-en-v1.5): primary signal =
  nearest-centroid cohesion; **30/30 `CLUSTER_COHERENT`, 0 blocking**, own-centroid
  cosine median 0.71–0.77. Scope-query cosine + BM25 retained as diagnostics
  (0.75 human-gated, `G3BR-012`). `Category_Scope_Ratification.csv`.
- **Misassignment**: 943 candidates (nearest centroid a different category by margin)
  — all semantic adjacency, **RESOLVED_SOURCE_ROUTING** (operator-confirmed, `G3BR-006`),
  0 open. `Category_Assignment_Findings.csv`.
- **Proposal**: `gate3_categories/GATE3_CATEGORY_PROPOSAL_20260617T050539Z/`.

### Phase 2.5 — Source catalog + retrieval (COMPLETE)

- **Catalog**: `tools/source_catalog/build_source_database.py --repo-root
  projects/chirality-piping --source-manifest …Source_Manifest.index.csv` → snapshot
  `_LocalIndexes/snapshots/SRCIDX_20260617T014930Z` (36,263 chunks: 21,912 LEDGER_ATOM,
  10,159 SECTION_NODE, 4,192 MARKDOWN_SECTION).
- **Dense index**: `_adapter/gate3_build_index.py` (length-sorted batching wrapper over
  `tools/retrieval/build_source_index.py`, 3.6× faster on this M3; embeddings identical)
  — embeddings (36263,768) float32, L2-normalized, `index_builds` READY. BM25 + catalog
  built by the shared tool unchanged.
- **TOC priors**: `tools/decomp/build_toc_priors.py` over 158 reviewed skeletons →
  `cross_source_toc_matrix.{md,csv}` (197,916 alignment pairs).

Generated UTC: 2026-06-17 · Gate 6 publication revision: 2026-06-17

DOMAIN_DECOMP agent persona; 6-gate methodology (Intake → Normalize → Categories
→ Knowledge Types → Coverage → Publish). This document is the concise control
surface; heavy machine-truth lives in the companion registers (see Companion
Inventory).

## Source Model

This domain pack decomposes the live software project
`projects/chirality-piping/` (the OpenPipeStress piping-stress-analysis
application) and uses **manifest-backed** live repo files as source truth.
Source files are **not copied** into `_Sources/`; companions point back to
`@repo/<RepoRelPath>`.

- **Source repo root:** `projects/chirality-piping/` — `@repo/...` resolves here
  (cross-repo; differs from the `chirality` self-domain).
- **Pack root:** `domains/chirality-piping/` (chirality monorepo). Shared
  agents/skills/tools resolve against the monorepo root.
- **Accepted manifest:** `domains/chirality-piping/_Sources/Source_Manifest.csv` (884 rows)
- **Source manifest SHA-256:** `db0eb6efdc56db7a137a6e00ef42c9ace4ab46da3fd85b94d53208ee57734bf7`
- **Source catalog snapshot:** `_LocalIndexes/snapshots/SRCIDX_20260617T014930Z` (Phase 2.5).

## Intake Summary

| Metric | Value |
|---|---:|
| Manifest file rows | 884 |
| Atomizable **source units** | 158 |
| Index-only files (schemas) | 38 |
| Skeletons generated | 158 |
| Total sections | 5,035 |
| In-scope sections (Gate-1.5-S) | 4,924 (111 OUT) |
| Dispatch units | 204 |
| Skeleton/render failures | 0 |

## Group Telemetry

| SourceGroup | Units | Components | Sections | Dispatch Units | Atomize |
|---|---:|---:|---:|---:|:--|
| `EXECUTION_DELIVERABLE` | 101 | 404 | 3,344 | 101 | YES (4 KT docs/deliverable, grouped) |
| `PRODUCT_DOCS` | 44 | 44 | 728 | 44 | YES (per file) |
| `EXECUTION_GOVERNANCE` | 5 | 9 | 90 | 6 | YES (grouped per folder) |
| `ROOT_DOCS` | 3 | 3 | 21 | 3 | YES (per file) |
| `CODE_CORE` | 1 | 156 | 239 | 18 | YES (one grouped code unit) |
| `CODE_APPS` | 1 | 103 | 225 | 21 | YES (one grouped code unit) |
| `CODE_TESTS` | 1 | 69 | 70 | 5 | YES (one grouped code unit) |
| `CODE_TOOLS` | 1 | 7 | 10 | 1 | YES (one grouped code unit) |
| `CODE_VALIDATION` | 1 | 51 | 308 | 5 | YES (one grouped code unit) |
| **Atomizable total** | **158** | **846** | **5,035** | **204** | |
| `schemas/*` (index-only) | — | 38 | — | — | NO (catalog-metadata only) |

## References

- `domains/chirality-piping/_Sources/Source_Manifest.csv` — file-level source admission (884 rows).
- `domains/chirality-piping/_Sources/SOURCE_BOUNDARY.md` — source boundary.
- `domains/chirality-piping/_Decomposition/Source_Decomp_Prefix_Map.csv` — source-unit map.
- `domains/chirality-piping/_Decomposition/Source_Manifest.index.csv` — markdown-only index manifest.
- `domains/chirality-piping/_Decomposition/Intake_Telemetry.{csv,json}` — intake telemetry.

## Companion Inventory

See `Companion_Inventory.csv` — full file-level inventory of the package,
regenerated at Gate 6 by `_adapter/gate6_build_companion_inventory.py`. Columns:
`Filename`, `PackageRole`, `Description`. Covers all register classes from
Phases 1–5: ledgers + annexes, category/KTY/subject registers, ratifications +
findings, vocabulary map, coverage telemetry + section register, per-source
skeletons / section-nodes / asset-manifests / review HTML / pack markdown,
dispatch plans, TOC matrix, open issues, validation checks, and the gate
snapshot chain with `_LATEST_*` pointers.

## Open Issues

See `Open_Issues_Register.csv`.

| IssueID | Status | Issue |
|---|---|---|
| `OI-001` | ACCEPTED_GATE_1 | Live code (~330 files) admitted as five grouped atomized units (core/apps/tests/tools/validation). |
| `OI-002` | ACCEPTED_GATE_1 | Process logs + deliverable meta docs excluded entirely (not indexed). |
| `OI-003` | ACCEPTED_GATE_1 | Deliverable admits 4 canonical KT docs by suffix (101 units, 404 components). |
| `OI-004` | ACCEPTED_GATE_1 | Execution governance restricted to `_Decomposition/` + `_ScopeChange/` (5 grouped units). |
| `OI-005` | ACCEPTED_GATE_1 | schemas (38) admitted index-only; fixtures excluded. |
| `OI-006` | RECORDED | Cross-repo: `@repo` resolves against `projects/chirality-piping`. |
| `OI-007` | ACCEPTED_GATE_1 | Gate 1.5 reduces to 1.5-S (asset surfaces N/A). |
| `OI-008` | ACCEPTED_STAGE_PHASE_2 | 158 units / 5,035 sections / 204 dispatch units staged. |
| `OI-009` | ACCEPTED_GATE_1 | All admitted sections default in-scope; refined at Gate 1.5-S (111 OUT). |
| `OI-010` | RESOLVED_GATE_1 | `INIT.md` session launcher excluded (no decomposable knowledge). |
| `OI-024` | ACCEPTED_SCAFFOLD_FOR_FILL | 1,402 cov-empty in-scope sections attested scaffold-for-fill; none re-dispatched. |
| `OI-025` | DEFERRED_PUBLISH_CAVEAT | 509 TBD-scope atoms uncategorized; recorded as a deferred open issue (IN decomposition complete). |

## Decision Log / Change Log

| DecisionID | Date | Decision |
|---|---|---|
| DEC-001 | 2026-06 | Domain pack at `domains/chirality-piping/` decomposing sibling repo `projects/chirality-piping/` (OpenPipeStress); manifest-backed, no source files copied. |
| DEC-002 | 2026-06 | V1 boundary: `AGENTS/CONTRIBUTING/README`, `docs/`, `execution/_Decomposition`+`_ScopeChange`, and code (`core/apps/tests/tools/validation`); process logs + deliverable meta excluded; schemas index-only; fixtures excluded. |
| DEC-003 | 2026-06 | Code (~330 files) atomized as five grouped source units, one per top-level code folder (OI-001). |
| DEC-004 | 2026-06 | Deliverable admission = 4 canonical KT docs by basename suffix (101 units, 404 components); governance grouped per folder; docs/root per file (OI-003/OI-004). |
| DEC-005 | 2026-06 | **Gate 2 accepted.** Phase-2 atomization complete: 21,912 atoms (IN 21,256 / OUT 147 / TBD 509); 1,812 vocabulary terms. |
| DEC-006 | 2026-06-16 | **Gate 3 accepted.** 30 faithful-to-author categories (18 PKG 1:1 + 12 cross-cutting) by deterministic source-routing; binding dense ratification 30/30 `CLUSTER_COHERENT`; 943 candidates `RESOLVED_SOURCE_ROUTING`; 509 TBD deferred (OI-025). |
| DEC-007 | 2026-06-17 | **Gate 4 accepted.** KTY axis = knowledge-kind (98 KTYs); subjects per-deliverable/source/directory (630); ratification 98/98 `CLUSTER_COHERENT`; 99 candidates `RESOLVED_SOURCE_ROUTING`. |
| DEC-008 | 2026-06-17 | **Gate 5 accepted.** Machine-classify + bulk-attest coverage; 1,402 cov-empty in-scope sections attested scaffold-for-fill (OI-024), incl. all 46 genuine-gap candidates; none re-dispatched. |
| DEC-009 | 2026-06-17 | **Gate 6 publish.** OI-025 (509 TBD) ruled a documented deferred caveat in the accepted basis. Objectives omitted per Deviation A. Canonical published annex layer added; companion inventory regenerated; integrity validator PASS (0/0/0). |

## Gate 6 — Publication & Final Acceptance

DOMAIN_DECOMP for `chirality-piping` is assembled and PUBLISHED. All upstream
gates (1, 1.5-S, 2, 2.5, 3, 4, 5) are CLOSED and ACCEPTED; the final integrity
validator passes clean (0 CRITICAL / 0 MAJOR / 0 MINOR). The required published
sections are present — Domain Ledger, Coverage & Telemetry, Vocabulary Map,
Categories / Knowledge Types / Subjects, Decision/Change Log, and Companion
Inventory.

One documented deferred caveat is carried as part of the accepted basis (a future
scope-change amendment, not a closure blocker): **OI-025** (509 TBD-scope atoms).
The Objectives layer is omitted by design (Deviation A); `annex_objectives.csv` is
header-only.

**Accepted** by the operator on 2026-06-17: *"Accepted."* The Gate 6 publish snapshot
`gate_snapshots/GATE6_PUBLISH_20260617T162204Z/` (acceptance record, publication manifest with
SHA-256s, readiness packet, handoff state, register copies, integrity report) and the
`_LATEST_GATE6.md` pointer are written. **DOMAIN_DECOMP is complete.** Downstream work
and any amendment to this basis require an explicit scope-change cycle.
