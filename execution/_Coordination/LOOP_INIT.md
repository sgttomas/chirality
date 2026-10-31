# Chirality library development entry

The owner accepted [the Library PRD](../../docs/PRD.md) on 2026-10-31.
It defines the product objectives, scope, requirements and acceptance criteria
for maintaining the library through its own contents, including its execution.
Read [Root AGENTS.md](../../AGENTS.md) for authority, the working cycle and Git
conventions. Initialization selects no undertaking.

## Current basis

The pre-library packages, decomposition, scope changes and coordination records
have been removed. The recovery reference is in
[projects/FROZEN.md](../../projects/FROZEN.md#pre-library-root-execution).
No new decomposition, deliverables or dependency bindings have been established.

For the next authorized undertaking, use the PRD as source intent for the
library's `project-decomp` workflow. Decomposition establishes the packages and
deliverables through its applicable review and acceptance. `project-setup` then
materializes accepted scope under `execution/PKG-nn/DEL-nn-nn/` with
`ScopeOfWork.md`, `deliverable.yaml` and `Work/`. Inspect the selected methods and
tools against the current locality convention before using them. Old execution
records are historical inputs only, not a backlog or an instruction to resume.

## Consumers and boundaries

App v4 and SWBPIPE independently consume shared material. Each project owns its
adoption and product work; coordinate affected interfaces through its current
Agent 0 as directed in AGENTS.md. A library revision does not force adoption.
Preserve original source identities and historical references when changing
shared material. The repository's Git grant reaches only Chirality Root.

App v3, Runtime and PEC remain frozen. `_DomainEngines/` changes only under a
steer covering that scope. Private information stays outside this public
repository. Acceptance, issuance and release remain owner acts.

## Verification

For new localities, use `python3 -m tools.deliverables --project . check`;
query affected needs for the actual undertaking. Structural results and path
presence do not establish suitability or acceptance.

For tool changes, inspect selection with
`python3 tools/run_affected_tests.py --dry-run`, then omit `--dry-run` to execute
the affected checks. After workflow package changes, rebuild the index with
`python3 tools/validation/build_workflow_index.py`; `--check` checks currency.
[CI selection](../../docs/CI_SELECTION.md) describes hosted verification and the
required `harness` result. Reuse applicable evidence and broaden checks for a
concrete uncovered concern.
