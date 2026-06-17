# Chirality Piping (OpenPipeStress) Domain Source Boundary

## Status

Initial source boundary for `domains/chirality-piping/`, defined at Phase 1
(Gate 1) of a fresh DOMAIN_DECOMP decomposition. Awaiting Gate 1 acceptance.

## Source Model

The source corpus is **manifest-referenced** and lives in a **sibling
repository**. Files are not copied into `_Sources/`; instead
`_Sources/Source_Manifest.csv` records source-repo-relative paths, source
groups, authority roles, inclusion/atomization state, and expected SHA-256
hashes.

- **Source repo root:** `projects/chirality-piping/` (relative to the chirality
  monorepo root). Catalog outputs use `@repo/<RepoRelPath>` and resolve through
  this root via `--repo-root`.
- **Pack root:** `domains/chirality-piping/` (in the chirality monorepo).
- Shared agents/skills/tools resolve against the monorepo root.

`IncludeInIndex=YES` admits a file to the retrieval catalog. `AtomizeInV1` is
NOT a manifest column; it is derived from `SourceGroup` by the intake adapter
(`run_intake.py`). A file may be `IncludeInIndex=YES, AtomizeInV1=NO`
(retrieval-visible but not atomized).

## Included In V1

**Atomized (`AtomizeInV1=YES`):**

- **`AGENTS.md`, `README.md`, `CONTRIBUTING.md`** — root agent-operating
  / project governance (one source each). `governance/*.md` policy docs.
- **`docs/**/*.md`** — product and specification handbooks (one source per file):
  PRD, SPEC, TYPES, CONTRACT, DIRECTIVE, PLAN, INTENT, `architecture/**`,
  `security/**`, `theory/**`, guides, validation_manual, and `_ScopeChange/`
  PRD versions. Process-log basenames (below) are excluded even under `docs/`.
- **`execution/PKG-*/1_Working/DEL-*/`** deliverables — each deliverable folder's
  **knowledge-type docs, matched by basename suffix** (`Datasheet.md`,
  `Specification.md`, `Guidance.md`, `Procedure.md`), grouped into **one source
  unit per deliverable** (101 units; component-map provenance to original
  `@repo` files). Meta docs and non-KT files are **not admitted** (see Excluded).
- **`execution/_Decomposition/` + `execution/_ScopeChange/`** — software-
  decomposition method (`SOFTWARE_DECOMP.md`) and scope-change governance docs,
  grouped by folder. Process-log basenames excluded.
- **Source code** — `core/`, `apps/`, `tests/`, `tools/`, `validation/` — each
  top-level folder grouped into **one** atomized source unit
  (`SRC-CODE-<FOLDER>`). Admitted extensions: `.py .rs .ts .tsx .js .jsx .mjs
  .cjs .css .scss .html .toml .md`. Each component file becomes one section in
  the grouped pack (code bodies are indented in the pack markdown so source-code
  comment lines are not misparsed as Markdown headings; `.md` components retain
  their heading structure).

**Index-only (`IncludeInIndex=YES, AtomizeInV1=NO`):**

- `schemas/*.{yaml,json}` — 36 canonical domain data models (structured, not
  prose; atomized poorly by the heading-based tooling).
- `api/api_boundary_contract.yaml` — external API contract.
- `docs/MANIFEST.json` — docs manifest sidecar.

## Excluded In V1

- **Process logs** (anywhere) — `TASK_RUN_*.md`, `RUN_*.md`, `PREPARATION_RUN_*`,
  `RUN_SUMMARY.md`, `Decision_Log.md`, `Brief.md`, `Handoff_State.md`,
  `ACCEPTANCE_RECORD.md`, `APPROVAL_RECORD.md`, `PROPOSAL_RECORD.md`,
  `Review_Summary.md`, `QA_Report.md`, `_REVIEW.md`, and any file whose name
  contains `NEXT_INSTANCE` or `NEXT_SESSION` (inter-session coordination /
  handoff docs). Not admitted to the manifest at all (neither atomized nor
  indexed).
- **Deliverable meta + non-KT docs** — `_SEMANTIC.md`, `_SEMANTIC_LENSING.md`,
  `_CONTEXT.md`, `_DEPENDENCIES.md`, `_REFERENCES.md`, `_STATUS.md`, `MEMORY.md`,
  and any non-KT-suffix deliverable file. Only the four canonical KT-suffix docs
  are admitted per deliverable.
- **Non-knowledge execution governance** — `execution/_DAG/`, `_Aggregation/`,
  `_Evaluation/`, `_Reconciliation/`, `_Coordination/`, `_Change/` (process
  provenance / roll-ups). Only `_Decomposition/` and `_ScopeChange/` are admitted.
- **`_LATEST.md`** pointer files (everywhere).
- **`fixtures/`** test data; **`examples/`**; `docs/_Registers/*.csv` and other
  `*.csv` / data `*.json` matrices; `Cargo.lock` / lock files; `*.pyc`, `*.map`,
  `*.wasm`, `*.tsbuildinfo`, `.gitignore`, `.DS_Store`.
- **Generated / vendored output** — `node_modules/`, `*/target/`,
  `apps/desktop/dist/`, `dist-electron/`, `.next/`, `.chirality/`,
  `__pycache__/`, `.pytest_cache/`.
- Repo top-level `.archive/`, `.github/`, `.claude/`, `init/`, `plans/`,
  `provenance/`; `INIT.md` (session-bootstrap launcher, no domain knowledge);
  `LICENSE.md`; `package.json` / `package-lock.json` / `requirements-dev.txt`.
  `_run_records/`, `_Archive/`, `0_References/` segments anywhere.

## Source Groups

| SourceGroup | AuthorityRole | Prefix | Atomize | Notes |
|---|---|---|---|---|
| `ROOT_DOCS` | ROOT_AUTHORITY | RT | YES (per-file) | `AGENTS.md`, `README.md`, `CONTRIBUTING.md` |
| `PRODUCT_DOCS` | PRODUCT_AUTHORITY | PD | YES (per-file) | `docs/**/*.md` + `governance/*.md` |
| `EXECUTION_DELIVERABLE` | DELIVERABLE_AUTHORITY | ED | YES (grouped per deliverable) | KT-suffix docs per `DEL-*` (101 units) |
| `EXECUTION_GOVERNANCE` | GOVERNANCE_AUTHORITY | EG | YES (grouped per folder) | `execution/_Decomposition/`, `execution/_ScopeChange/**` |
| `CODE_CORE` | CODE_AUTHORITY | CC | YES (1 grouped unit) | `core/` Python+Rust solver/domain engine |
| `CODE_APPS` | CODE_AUTHORITY | CA | YES (1 grouped unit) | `apps/` TypeScript+Rust Tauri desktop GUI |
| `CODE_TESTS` | CODE_AUTHORITY | CT | YES (1 grouped unit) | `tests/` Python test suites |
| `CODE_TOOLS` | CODE_AUTHORITY | CL | YES (1 grouped unit) | `tools/` Python automation |
| `CODE_VALIDATION` | CODE_AUTHORITY | CV | YES (1 grouped unit) | `validation/` benchmark harness + docs |
| `SCHEMAS` | SCHEMA_AUTHORITY | — | NO (index-only) | `schemas/*`, `api/*`, `docs/MANIFEST.json` |

## Downstream Status

Phase 2 atomization, category registers, knowledge-type registers, retrieval
catalog, and publication packages are out of scope until later gates close.
`Source_Manifest.csv` is the file-level source-admission authority; the
per-deliverable / per-code-folder grouping into source units is recorded by the
intake adapter and surfaced in `Intake_Telemetry.csv` and the dispatch plans.
