# Fresh-project assumptions in the three promoted Core workflows

Separate report requested with the Core / Specialist / Project Specific
navigation directive (Ryan Tufts, 2026-09-12). Scope: read `task-management`,
`review`, and `reconciliation` (each `WORKFLOW.md` plus `resources/contract.md`
and `resources/method.md`) and report where they assume artifacts or tools a
fresh App project does not have. Nothing below was rewritten; the directive
asked for a report, not body changes.

Reference point for "fresh project": a folder chosen in the App with no
`execution/` tree, no registers, no decomposition, and only the packaged
instruction root (`scripts/prepare-packaged-instruction-root.mjs`, `TOOL_FILES`)
as the tool root.

## task-management ("Manage tasks")

- Requires an existing per-loop Action Item register (contract K-TM-1 through
  K-TM-6, "closure-capable schema" with `Status` and `Disposition`). A fresh
  project has no register and the workflow does not say how to create one.
- The mandatory federation preflight discovers "tracked registers in the
  sanctioned Root, project, domain" trees and prefers the `taskmgmt federation`
  helper. That helper is not in the packaged tool root, and a fresh project has
  no federation to discover; the contract's `COMPLETE` / partial readings assume
  at least one canonical register exists.
- Cites PRD sections (§5.5, §6.2, §14) and a Root receipt (Receipt 89) as the
  authority for its constraints. Those are Root documents; they are not part of
  the App's project context and are not needed to run the method, but the text
  reads as if the operator can open them.
- Method step 1 ("Inspect the owning loop's action register, federation
  coverage, and accepted control state") therefore has nothing to inspect on a
  fresh project. Expected first-run behaviour: the agent should report that no
  register exists and propose creating one, rather than failing the preflight.

## review ("Review results")

- Assumes the deliverable production contract: `Datasheet.md`,
  `Specification.md`, `Guidance.md`, `Procedure.md`, `ScopeOfWork.md`,
  `Dependencies.csv`, `_CONTEXT.md`, `_STATUS.md`, and the
  `{EXECUTION_ROOT}/_Evaluation/Reviews/` snapshot root. None exist on a fresh
  project; the contract declares itself project-generic but the generic case is
  still "a Chirality execution tree".
- `DECOMPOSITION_PATH` is discovered from `{EXECUTION_ROOT}/_Decomposition/`;
  the method handles absence with `SKIP` (filesystem-only review), which is the
  correct fresh-project path.
- Format basis `SOW_V1` requires `tools/scope_of_work/derive_review_checklist.py`
  bound to a validated `ScopeOfWork.md`. That tool is not in the packaged tool
  root (`TOOL_FILES` carries `scope_of_work/common.py` only), so SOW-mode review
  cannot run inside the App; `LEGACY_FOUR_DOC` mode has no tool dependency.
- Gate 5 and snapshot steps call `tools/scaffolding/create_snapshot_folder.sh`,
  `tools/scaffolding/update_latest_pointer.sh`, and `write_status.sh` with a
  ruling path and approval SHA resolved from `_harness/adapter.yaml`. Only
  `write_status.sh` is packaged; the adapter file does not exist on a fresh
  project.
- Dispatches TASK with the `audit-decomp` workflow when a decomposition exists;
  that workflow is bundled, so the dependency is satisfied when the precondition
  is.

## reconciliation ("Check project status")

- Contract precondition "Activation before dispatch": a project decision
  register must contain the activating decision. A fresh project has no decision
  register, so the workflow cannot start as written.
- Requires a frozen accepted basis: accepted decomposition, decision register,
  and current dependency pointer. On a fresh project all three are absent.
- Package sizing constants are project-specific ("2,053 frozen legacy source
  lines", ignored-path allowlists) and read as carried over from the project
  where the method was developed rather than as parameters.
- The output contract (RUN_BASIS.md, DELIVERABLE_INVENTORY.csv,
  IMPLEMENTATION_SURFACES.csv, VERIFICATION_INDEX.csv, claims and verification
  files per deliverable) presumes a deliverable corpus with `_STATUS.md`
  `## Remaining` sections.
- Step R2 runs "the registered deterministic harness" for validation members;
  the App's packaged tool root ships the software-workflow check runners but
  not a project harness registration.

## Summary

| Workflow | Runs on a fresh project as written | Blocking assumption |
|---|---|---|
| task-management | No | Existing Action Item register and federation preflight |
| review | Partly (LEGACY_FOUR_DOC mode, decomposition SKIP) | Deliverable file set; SOW mode needs an unbundled tool |
| reconciliation | No | Activating decision in a decision register; frozen basis |

None of these findings changes the accepted navigation direction. They are
candidates for a later Root instruction tranche (bootstrapping paths for an
empty project, or packaging the missing tools), which is outside this
refinement's scope and is not proposed here as a change.
