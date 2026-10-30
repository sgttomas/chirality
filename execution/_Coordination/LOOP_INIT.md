# Chirality Root development entry

Chirality is the shared library of roles, workflows, tools and tool-use
instructions that its products and projects consume. With App v4 and SWBPIPE
in their own repositories, Root builds the parts of Chirality that serve that
role (owner, 2026-10-30: "I want App v4 and SWBPIPE to adopt the same practice
of a shared library for workflows, tools, and skills." and "start a fresh
execution and build the parts of Chirality that will be useful for its
role."). The library PRD that will govern this work has not yet been written;
until the owner accepts it, the conversation supplies each undertaking.

Work from the repository root. Read local `AGENTS.md` for the working cycle,
records, verification and the standing Git grant. Root maintains `AGENTS.md`,
`agents/`, `workflows/`, `.agents/skills/`, shared `tools/`,
`.github/workflows/` and the technical references in `docs/`. Locate the
affected shared component and its consumers; Root is not a standing audit or
backlog.

The current `execution/` is the pre-library decomposition: PKG-01 to PKG-06
in phase folders, with `_Decomposition/`, `_ScopeChange/` and the records in
`_Coordination/`. `CURRENT_WORKPLAN.md` and `HANDOFF_STATE.md` there are
historical, not current pointers or handoffs. None of it is a backlog. It
keeps its layout until it is archived by tag under the library PRD; new
deliverables then use the `PKG-nn/DEL-nn-nn/` convention with `Work/` in local
`AGENTS.md`. Check structure with:

```sh
python3 -m tools.deliverables --project . check
```

## Consumers

App v4 and SWBPIPE, listed with their standing in `AGENTS.md`, each name this
library in their own `AGENTS.md`, consult its roles and workflows, and carry
copies of some shared tools. A change to a shared
component identifies the consumers it affects and the shared revision they
would adopt. Change local consumers in the same PR and check the actual
connecting path. Consumers adopt through independently reviewable changes in
their own repositories, coordinated with their Agent 0s; a library change
never forces adoption, and the standing Git grant does not reach their
repositories. Do not send propagation notices or update unaffected consumers.

## Build and verification

For affected tool tests, run `python3 tools/run_affected_tests.py --dry-run`
to inspect selection, then omit `--dry-run` to execute it. Selection uses
`tools/tools-test-routing.json`; broaden only for a concrete uncovered concern.
After workflow package changes, rebuild with
`python3 tools/validation/build_workflow_index.py`; `--check` checks currency
without rebuilding. Hosted selection and the single required `harness` result
are described in `docs/CI_SELECTION.md`.

## Hard boundaries

- Acceptance, issuance and release are the owner's acts. Completed work,
  checks, reviews and merges do not record or imply them.
- App v3, Runtime and PEC are frozen. `projects/FROZEN.md` describes recovery,
  and recovery does not reactivate them or make them maintenance targets.
- `_DomainEngines/` and any project's product work change only under a steer
  covering that scope.
- This repository is public. Credentials and private or proprietary data stay
  out of it, and the required secret and private-term checks apply.

Keep instructions specific to actions, boundaries and useful entry points.
Consolidate duplicate duties rather than adding explanations around them.
Recover historical material through Git or archive tags when needed; restoring
an old procedure does not make it binding again.
