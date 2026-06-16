# Chirality App-Dev Domain Pack

Domain shell for the Chirality desktop application's own knowledge, decomposed
from the live development repository `projects/chirality-app-dev/`.

This domain pack treats that live repository as the source of truth. Like the
`domains/chirality/` self-domain, intake is **retrieval-first**:
`_Sources/Source_Manifest.csv` admits selected repo files by path and SHA-256,
and the source catalog stores `@repo/...` references instead of copying source
files into this domain pack.

**Cross-repo note.** Unlike the `chirality` self-domain (where the pack and its
sources shared one repository), this pack lives in the chirality monorepo at
`domains/chirality-app-dev/` while its sources live in the sibling tree
`projects/chirality-app-dev/`. `@repo/<RepoRelPath>` therefore resolves against
`projects/chirality-app-dev/` (pass it as `--repo-root` to the source-catalog
and validation tools). Shared agents/skills/tools still resolve against the
monorepo root via `canonical_shared_roots`.

Initial scope (V1) is the app's governance, execution-planning, and frontend
surface:

- `AGENTS.md` — root agent-operating governance.
- `docs/*.md` — product/spec handbooks (PRD, SPEC, TYPES, PLAN, …).
- `execution/**` — the app's prior software-decomposition: 53 deliverables
  (each admitting its knowledge-type docs by basename suffix — `*Datasheet`,
  `*Specification`, `*Guidance`, `*Procedure` — grouped into one source unit),
  plus reconciliation / scope-change / coordination governance. Heading-bearing
  markdown only.
- `frontend/` — the TypeScript/React app source, grouped into one atomized
  source unit (`SRC-FRONTEND-SRC`), plus its prose docs (atomized per file).

Out of scope for V1: process-log provenance (`_run_records/TASK_RUN_*`,
`RUN_SUMMARY`, `Decision_Log`, ~350 files) is excluded entirely — neither
atomized nor indexed; CSV/JSON data matrices and Python scripts under
`execution/`; the ~2.2 GB of generated
and vendored frontend output (`dist/`, `node_modules/`, `.next/`,
`dist-electron/`, `.chirality/`, source maps, the packaged `.app` bundle); and
the repo's `.archive/`, `.github/`, `init/`, `plans/`, `provenance/`, and the
bundled `.zip`.

Generated local indexes under `_LocalIndexes/` are derived, rebuildable, and
ignored by git except for the README and placeholder.
