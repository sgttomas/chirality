# Chirality Piping (OpenPipeStress) Domain Pack

Domain shell for the OpenPipeStress engineering application's own knowledge,
decomposed from the live development repository `projects/chirality-piping/`.

This domain pack treats that live repository as the source of truth. Like the
`domains/chirality-app-dev/` pack, intake is **retrieval-first**:
`_Sources/Source_Manifest.csv` admits selected repo files by path and SHA-256,
and the source catalog stores `@repo/...` references instead of copying source
files into this domain pack.

**Cross-repo note.** This pack lives in the chirality monorepo at
`domains/chirality-piping/` while its sources live in the sibling tree
`projects/chirality-piping/`. `@repo/<RepoRelPath>` therefore resolves against
`projects/chirality-piping/` (pass it as `--repo-root` to the source-catalog
and validation tools). Shared agents/skills/tools resolve against the monorepo
root via `canonical_shared_roots`.

Initial scope (V1) — the project's governance, product/spec, execution, and
implementation surface:

- **Root governance** — `AGENTS.md`, `README.md`, `CONTRIBUTING.md`,
  plus `governance/*.md` policy. (`INIT.md` is a bootstrap launcher — excluded.)
- **`docs/**/*.md`** — product/spec handbooks (PRD, SPEC, TYPES, CONTRACT,
  DIRECTIVE, architecture, security, theory, guides) — atomized per file.
- **`execution/PKG-*/1_Working/DEL-*/`** — the project's prior
  software-decomposition: 101 deliverables, each admitting its knowledge-type
  docs by basename suffix (`Datasheet`/`Specification`/`Guidance`/`Procedure`),
  grouped into one source unit per deliverable.
- **`execution/_Decomposition/` + `execution/_ScopeChange/`** — software-
  decomposition method and scope-change governance docs, grouped by folder.
- **Source code** — `core/` (Python+Rust), `apps/` (TypeScript+Rust), `tests/`,
  `tools/`, `validation/` — each top-level folder grouped into one atomized
  source unit (code-aware pack markdown; one section per file).

Index-only (`IncludeInIndex=YES`, not atomized): `schemas/*.{yaml,json}` domain
models, `api/api_boundary_contract.yaml`, and `docs/MANIFEST.json`.

Out of scope for V1: process-log provenance (`TASK_RUN_*`, `RUN_SUMMARY`,
`Decision_Log`, `Brief`, `_REVIEW`, and deliverable meta docs `_SEMANTIC*`,
`_CONTEXT`, `_DEPENDENCIES`, `_REFERENCES`, `_STATUS`, `MEMORY`); the
non-knowledge execution governance folders (`_DAG`, `_Aggregation`,
`_Evaluation`, `_Reconciliation`, `_Coordination`, `_Change`); `fixtures/` test
data; `examples/`; CSV/JSON data matrices and lock files; generated/vendored
output (`node_modules/`, `*/target/`, `apps/desktop/dist/`, `.pytest_cache/`);
and the repo's `.archive/`, `.github/`, `init/`, `plans/`, `provenance/`.

Generated local indexes under `_LocalIndexes/` are derived, rebuildable, and
ignored by git except for the README and placeholder.
