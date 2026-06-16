# Chirality App-Dev Domain Decomposition

Package role: working surface

Status: **Gate 1 (Phase 1 Intake) ACCEPTED** (operator sign-off 2026-06-16;
acceptance token `GATE1_ACCEPT_20260616`). Next: Gate 1.5-S skeleton review.
Phase 2 atomization has not started.

Generated UTC: 2026-06-16T00:49:19Z

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
- **Accepted manifest:** `domains/chirality-app-dev/_Sources/Source_Manifest.csv`
- **Source manifest SHA-256:** `a9296fa7d27be114a0514d62c669c8f226e9f1f8cdb06a542d4cc4af6c044456`
- **Source catalog snapshot:** not built (Phase 2.5; after Gate 2).

## Intake Summary

| Metric | Value |
|---|---:|
| Manifest file rows | 836 |
| — atomizable component files | 835 |
| — index-only files | 1 |
| Atomizable **source units** | 96 |
| Index-only files (`docs/MANIFEST.json`) | 1 |
| Skeletons generated | 96 |
| Structure review HTML generated | 96 |
| Section-node CSVs generated | 96 |
| Generated grouped pack-markdown files | 80 |
| Total sections | 7,996 |
| In-scope sections (heuristic) | 7,996 |
| Dispatch units | 162 |
| Oversized dispatch units | 0 |
| Skeleton/render failures | 0 |

## Group Telemetry

| SourceGroup | Units | Components | Source Lines | Sections | Dispatch Units | Atomize |
|---|---:|---:|---:|---:|---:|:--|
| `EXECUTION_DELIVERABLE` | 53 | 607 | 57,097 | 6,932 | 107 | YES (grouped per deliverable) |
| `EXECUTION_GOVERNANCE` | 26 | 65 | 4,411 | 468 | 27 | YES (grouped per folder) |
| `FRONTEND_SRC` | 1 | 147 | 45,073 | 201 | 11 | YES (one grouped code unit) |
| `PRODUCT_DOCS` | 12 | 12 | 4,694 | 369 | 13 | YES (per file) |
| `FRONTEND_DOCS` | 3 | 3 | 344 | 19 | 3 | YES (per file) |
| `ROOT_DOCS` | 1 | 1 | 96 | 7 | 1 | YES (per file) |
| **Atomizable total** | **96** | **835** | **111,715** | **7,996** | **162** | |
| `docs/MANIFEST.json` | — | 1 | — | — | — | NO (index-only) |

## Source-Unit Grouping Policy

- **Per-file** source units: `AGENTS.md`, each `docs/*.md`, each frontend prose
  doc. SourceRef mode `REPO_LINE`.
- **Grouped** source units (SourceRef mode `COMPONENT_MAP`): each
  `execution/.../1_Working/DEL-XX-YY_*/` deliverable (its ~10 substantive docs +
  any nested sub-packets) is one source unit (53 units); execution governance
  folders (`_Reconciliation`, `_ScopeChange`, `_Coordination`, `_Decomposition`,
  PKG-level framing) are grouped by immediate parent directory (26 units); and
  all of `frontend/src` (+ `electron`, `scripts`, config) is one grouped code
  unit `SRC-FRONTEND-SRC` (147 component files → one section per file).
- Grouped units write a generated pack markdown under `source_pack_markdown/`
  (a worker/review substrate only — component headings demoted, `## Component:`
  separators). The `source_components` map in each grouped asset manifest carries
  per-component generated→source line offsets so Phase-2 atoms cite original
  `@repo` component files.

## SourceRef Adapter Policy

Two accepted SourceRef forms for Phase 2 atomization:

```text
# per-file (REPO_LINE):
@repo/<RepoRelPath>:L####|domains/chirality-app-dev/_Decomposition/source_review_html/<SourceUnitID>.html#<SectionID>

# grouped (COMPONENT_MAP): atoms cite the original component file, resolved
# through source_components in the grouped asset manifest:
@repo/<component RepoRelPath>:L####|domains/chirality-app-dev/_Decomposition/source_review_html/<SourceUnitID>.html#<SectionID>
```

## Gate 1.5 Asset Surface Policy

The corpus is markdown-only with empty asset manifests; per-kind asset surfaces
(equations / figures / tables / images / folios) and the 1.5-P prose-validate
prefilter are **N/A**. Gate 1.5 reduces to **1.5-S skeleton review** on the
structure-mode HTML under `source_review_html/`.

## Frontend & Process-Log Disposition

- `frontend/src/**` (+ `electron`, `scripts`, config; 147 files) is **atomized**
  as a single grouped source unit `SRC-FRONTEND-SRC` (`AtomizeInV1=YES`,
  `COMPONENT_MAP` provenance) per operator direction — one section per component
  file (201 sections, 11 dispatch units).
- `execution/` process logs (`_run_records/TASK_RUN_*`, `RUN_SUMMARY`,
  `Decision_Log`; ~350 files) are **excluded entirely** (not indexed) by
  operator direction.
- `docs/MANIFEST.json` is the only index-only file (`Index_Only_Register.csv`).

## References

- `domains/chirality-app-dev/_Sources/Source_Manifest.csv` — file-level source admission.
- `domains/chirality-app-dev/_Sources/SOURCE_BOUNDARY.md` — source boundary.
- `domains/chirality-app-dev/_Decomposition/Source_Decomp_Prefix_Map.csv` — source-unit map.
- `domains/chirality-app-dev/_Decomposition/Source_Unit_Component_Map.csv` — grouped-unit provenance.
- `domains/chirality-app-dev/_Decomposition/Intake_Telemetry.{csv,json}` — intake telemetry.
- `domains/chirality-app-dev/_Decomposition/Index_Only_Register.csv` — index-only files.

## Companion Inventory

See `Companion_Inventory.csv` (566 entries) for the full file-level inventory of
the canonical working package (manifest, boundary, prefix/component maps,
telemetry, per-unit skeletons / dispatch plans / asset manifests / structure
HTML / section-node CSVs / pack markdown, open issues, validation checks).

## Open Issues

See `Open_Issues_Register.csv`. Gate-1 rulings awaiting human confirmation:

| IssueID | Status | Issue |
|---|---|---|
| `OI-001` | RESOLVED_GATE_1 | frontend/src (147 files) atomized as one grouped unit `SRC-FRONTEND-SRC` (operator direction). |
| `OI-002` | ACCEPTED_GATE_1 | ~350 process logs excluded entirely (not indexed). |
| `OI-003` | ACCEPTED_GATE_1 | execution grouped per-deliverable (53) + governance per-folder (26). |
| `OI-004` | ACCEPTED_GATE_1 | Gate 1.5 reduces to 1.5-S (asset surfaces N/A). |
| `OI-005` | RECORDED | Cross-repo: @repo resolves against projects/chirality-app-dev. |
| `OI-006` | ACCEPTED_OPTION_A | DEL-00-02 byte-identical duplicate Packet_* trees; Option A — rely on ContentHash dedup at Gate-2 merge. |
| `OI-007` | OPEN_FOR_GATE_2 | 95 units / 7,795 sections — stage Phase-2 atomization in batches. |
| `OI-008` | RECORDED | All sections defaulted in-scope; refine at Gate 1.5-S. |

## Decision Log / Change Log

| DecisionID | Date | Decision |
|---|---|---|
| DEC-001 | 2026-06-15 | New domain pack created at `domains/chirality-app-dev/` decomposing the sibling repo `projects/chirality-app-dev/`; manifest-backed, no source files copied. |
| DEC-002 | 2026-06-15 | V1 boundary: include `AGENTS.md`, `docs/`, `execution/`, `frontend/`; exclude other top-level folders and ~2.2 GB generated/vendored frontend output. |
| DEC-003 | 2026-06-15 | `frontend/src` code (147 files) atomized as ONE grouped source unit `SRC-FRONTEND-SRC` — operator direction (OI-001; revised from an initial index-only proposal). |
| DEC-004 | 2026-06-15 | `execution` markdown only (CSV/JSON/scripts excluded); process logs excluded entirely (not indexed) — operator direction. |
| DEC-005 | 2026-06-15 | Execution grouped per deliverable (53) and per governance folder (26); docs/root/frontend-prose per file. |

## Gate 1 Confirmation Packet — ACCEPTED

Gate 1 was accepted by the operator on 2026-06-16 (token
`GATE1_ACCEPT_20260616`), including: the revised manifest-backed source set; the
per-deliverable (53) / per-governance-folder (26) grouping plus the single
grouped frontend-source unit `SRC-FRONTEND-SRC`; the excluded process logs and
index-only `docs/MANIFEST.json`; the 96-unit skeleton inventory; the
structure-mode review HTMLs; and OI-006 Option A (rely on ContentHash dedup).

Next gate: **Gate 1.5-S** skeleton review (asset sub-gates N/A). Phase 2
atomization remains gated behind Gate 1.5 and is staged per OI-007.
