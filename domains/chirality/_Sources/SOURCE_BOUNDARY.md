# Chirality Domain Source Boundary

## Status

This source boundary defines the current admitted corpus for
`domains/chirality/` after source-boundary cleanup.

## Source Model

The source corpus is manifest-referenced. Files are not copied into
`_Sources/`; instead, `_Sources/Source_Manifest.csv` records live repository
paths, authority roles, inclusion state, archive state, and expected SHA-256
hashes.

Catalog outputs use `@repo/<RepoRelPath>` as the artifact path. The source
catalog validator resolves these paths through the repository root and verifies
the recorded hashes.

## Included In V1

- Root framing and bootstrap documents.
- Root governance documents under `docs/`.
- Agent instruction contracts under `agents/`.
- Repo-native skill contracts under `skills/`.
- Tool registry and retrieval documentation.
- Repo-local export summary documentation under `exports/chirality-app/`
  (`README.md` and `export-report.md`).

## Excluded In V1

- `projects/`
- `frontend/`
- existing `domains/`
- `examples/`
- `.archive/`
- generated export staging
- dependency folders, caches, and build outputs
- non-governance code internals

## Retired From Active V1

- `SRC-FRONTEND-*` (`HX001`..`HX009`) rows for `frontend/README.md`
  and `frontend/docs/...` are retired from active V1 indexing and
  atomization. Their prefixes remain reserved in
  `_Decomposition/Source_Decomp_Prefix_Map.csv` for traceability only.
- Active frontend work is outside this Chirality source boundary under
  `projects/chirality-app-dev/`, which remains excluded by the `projects/`
  rule.
- `.archive/frontend/` is archive evidence only and is not admitted as
  replacement source truth.
- `SRC-AGENTS-AGENT-DELIVERABLE-TASK` (`AG013`) is retired from
  active V1 indexing and atomization because
  `agents/AGENT_DELIVERABLE_TASK.md` has been archived as obsolete. Its
  prefix remains reserved for traceability only. Any existing Batch 2 setup
  package that still selects `AG013` is stale and must be regenerated or
  explicitly amended before worker fan-out resumes.
- Eleven root/governance sources accepted into the original Batch 1 scope are
  retired from active V1 because their live repo files are now archived or
  removed:
  `SRC-CLAUDE` (`RT003`), `SRC-INIT` (`RT004`),
  `SRC-DOCS-CONTRACT` (`DG001`),
  `SRC-DOCS-DBM-AGENT-INSTRUCTION-ARCHITECTURE` (`DG002`),
  `SRC-DOCS-DIRECTIVE` (`DG003`), `SRC-DOCS-PLAN` (`DG004`),
  `SRC-DOCS-PRD-CANDIDATE` (`DG005`),
  `SRC-DOCS-SE-DESIGN-ANALYSIS` (`DG006`),
  `SRC-DOCS-SPEC` (`DG007`), `SRC-DOCS-TYPES` (`DG008`), and
  `SRC-DOCS-WHAT-IS-AN-AGENT` (`DG009`). Their prefixes remain reserved
  for prior-boundary traceability only.
- The accepted Batch 1 ledger and review companions for those eleven sources
  remain historical prior-boundary evidence. They must not be treated as
  current active-boundary truth unless the operator explicitly accepts
  carry-forward or regenerates/rebaselines Batch 1 for the current manifest.

## Downstream Status

The current active file-level manifest has 225 rows. Gate 2 Phase 2 closure accepts a 110-source-unit normalization surface: active Batch 1 carry-forward source units, Batch 2 agent contracts, Batch 3 governance/thesis context, Batch 4 grouped skill-pack sources, Batch 5 work-surface registry sources, and Batch 6 license. Retired Batch 1 rows remain historical prior-boundary evidence only. Category registers, knowledge-type registers, hypergraph snapshots, and publication packages remain out of scope until later gates close. `Gate2_Source_Unit_Register.csv` is the accepted Phase 3 source-unit authority; `Source_Manifest.csv` remains file-level source-admission authority.
