# Chirality App-Dev Domain Source Boundary

## Status

Initial source boundary for `domains/chirality-app-dev/`, defined at Phase 1
(Gate 1) of a fresh DOMAIN_DECOMP decomposition. Awaiting Gate 1 acceptance.

## Source Model

The source corpus is **manifest-referenced** and lives in a **sibling
repository**. Files are not copied into `_Sources/`; instead
`_Sources/Source_Manifest.csv` records source-repo-relative paths, source
groups, authority roles, inclusion/atomization state, and expected SHA-256
hashes.

- **Source repo root:** `projects/chirality-app-dev/` (relative to the chirality
  monorepo root). Catalog outputs use `@repo/<RepoRelPath>` and resolve through
  this root via `--repo-root`.
- **Pack root:** `domains/chirality-app-dev/` (in the chirality monorepo).
- Shared agents/skills/tools resolve against the monorepo root.

`IncludeInIndex=YES` admits a file to the retrieval catalog. `AtomizeInV1=YES`
additionally admits it to Phase-2 atomization (atoms minted into the Domain
Ledger). A file may be `IncludeInIndex=YES, AtomizeInV1=NO` (retrieval-visible
but not atomized).

## Included In V1

**Atomized (`AtomizeInV1=YES`):**

- `AGENTS.md` — root agent-operating governance (one source).
- `docs/*.md` — product and specification handbooks (one source per file).
- `execution/` deliverables — each `1_Working/DEL-XX-YY_*/` folder's
  **knowledge-type docs, matched by basename suffix** (`*Datasheet.md`,
  `*Specification.md`, `*Guidance.md`, `*Procedure.md` — i.e. the canonical four
  plus nested `Packet_Datasheet`/`Packet_Specification`/`Packet_Procedure`/
  `Case_Datasheet`), grouped into **one source unit per deliverable** (53 units,
  238 component files; component-map provenance to original `@repo` files). Meta
  docs and non-KT files are **not admitted** (see Excluded In V1).
- `execution/` governance — `_Reconciliation/`, `_ScopeChange/`,
  `_Coordination/`, `_Decomposition/` software-decomposition docs, and PKG-level
  framing docs, grouped by folder/artifact.
- `frontend/` prose — `frontend/docs/**` and other non-generated markdown.
- `frontend/src/**` (+ `electron/`, `scripts/`, top-level config) — the
  TypeScript/React application source, grouped into **one** atomized source unit
  (`SRC-FRONTEND-SRC`; 147 component files, `COMPONENT_MAP` provenance). Each
  component file becomes one section in the grouped pack.

**Index-only (`IncludeInIndex=YES, AtomizeInV1=NO`):**

- `docs/MANIFEST.json` and similar structured (non-prose) sidecars.

## Excluded In V1

- `execution/` **process logs** — `_run_records/TASK_RUN_*.md`, `RUN_SUMMARY.md`,
  `Decision_Log.md` (~350 files). Process provenance; not admitted to the
  manifest at all (neither atomized nor indexed) by operator direction.
- `execution/` **deliverable meta + non-KT docs** — the 6 meta docs per
  deliverable (`_SEMANTIC`, `_SEMANTIC_LENSING`, `_CONTEXT`, `_DEPENDENCIES`,
  `_REFERENCES`, `_STATUS`), `CONTROL`/`README`, and non-KT packet docs
  (`Packet_QA`, `Packet_Rationale`, `Packet_Contract`, `SCOPE_CHANGE_INIT`).
  Only KT-suffix docs are admitted (operator direction; OI-009 = suffix-match,
  so nested `Packet_Datasheet`/`Specification`/`Procedure` and `Case_Datasheet`
  ARE admitted).
- `execution/**` `*.csv`, `*.json`, `*.py` data matrices and scripts.
- `execution/**/.archive/`, `**/0_References/_Archive/`, `.DS_Store`, `.pyc`.
- Generated / vendored frontend output: `frontend/dist/` (incl. the packaged
  `Chirality.app` bundle), `frontend/node_modules/`, `frontend/.next/`,
  `frontend/dist-electron/`, `frontend/.chirality/`, all `*.map`.
- Repo top-level `.archive/`, `.github/`, `init/`, `plans/`, `provenance/`
  (archived by operator), and `chirality-app-dev.zip`.

## Source Groups

| SourceGroup | AuthorityRole | Atomize | Notes |
|---|---|---|---|
| `ROOT_DOCS` | ROOT_AUTHORITY | YES | `AGENTS.md` |
| `PRODUCT_DOCS` | PRODUCT_AUTHORITY | YES | `docs/*.md` |
| `EXECUTION_DELIVERABLE` | DELIVERABLE_AUTHORITY | YES (grouped) | KT-suffix docs per deliverable (`*Datasheet/*Specification/*Guidance/*Procedure.md`) |
| `EXECUTION_GOVERNANCE` | GOVERNANCE_AUTHORITY | YES (grouped) | reconciliation / scope-change / coordination / decomp docs |
| `FRONTEND_DOCS` | FRONTEND_AUTHORITY | YES | frontend prose docs |
| `FRONTEND_SRC` | FRONTEND_CODE | YES (1 grouped unit) | TypeScript/React source, grouped into `SRC-FRONTEND-SRC` |

## Downstream Status

Phase 2 atomization, category registers, knowledge-type registers, retrieval
catalog, and publication packages are out of scope until later gates close.
`Source_Manifest.csv` is the file-level source-admission authority; the
per-deliverable grouping into source units is recorded by the intake adapter
and surfaced in `Intake_Telemetry.csv` and the dispatch plans.
