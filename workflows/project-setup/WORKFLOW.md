---
name: project-setup
description: Initialize an accepted project workspace and coordinate its selected setup and estimation phases, or set up the amended scope incrementally after an accepted scope change.
---

# project-setup

Initialize an accepted project workspace and coordinate its selected setup and estimation phases. After an accepted scope change, set up only the amended scope.

WORKING_ITEMS coordinates this undertaking and assigns bounded contributions to TASK.
Selection does not launch setup or change roles. HELP_HUMAN may coordinate a
request for this workflow, but execution routes to an eligible WORKING_ITEMS
instance with actual host permissions and a run-specific brief.

## Modes and inputs

The setup mode is inferred from workspace state at session entry and confirmed
in the proposal; a brief may name it.

- `INITIAL` — first setup of an accepted decomposition (Functions 1–2). Inputs:
  the accepted decomposition, the human-confirmed coordination representation
  and dependency tracking mode, and the selected activation scope.
- `INCREMENTAL` — setup of the amended scope after an accepted `scope-change`
  amendment has been applied (Function 5). Inputs: the accepted amendment
  snapshot named by `_ScopeChange/_LATEST.md`, its accepted action register
  (`Amendment_Actions.csv`, or the register its group-2
  `ACCEPTED_MANIFEST.csv` names), `Propagation_Plan.md` and `Handoff_State.md`;
  the amended decomposition; the existing `_COORDINATION.md`, whose
  representation and tracking mode are reused rather than re-asked; and the
  agent-owned, append-only `_Coordination/SETUP_LOG.md`, whose adoption
  baseline excludes amendments accepted before the project adopted this mode.

An amendment still in progress is applied first through `scope-change`; this
workflow sets up the amended scope only after its checkpoint group 3 is
accepted. `audit-scope-closure` is the post-acceptance closure check of that
setup.

## Method

1. Inspect accepted decomposition, existing workspace state, coordination representation, `_ScopeChange/` state, and activation scope, and infer the mode.
2. Apply the `preparation` skill, then dispatch the selected production, semantic, dependency (`dependency-extract`, then `audit-dep-closure`), or domain workflows as bounded stages. In `INCREMENTAL` mode, scaffold only added entities, preserve existing folders, IDs, content and lifecycle state, route modified `SOW_V1` deliverables to `scope-of-work` `MODE=REVISE` (held for the human at `CHECKING` or `ISSUED`), rerun dependency stages only for the affected deliverables and their neighbours, record the run in `SETUP_LOG.md`, and propose `audit-scope-closure`.
3. Sequence dependent work from accepted outputs; route SCCs to `scc-resolution-case` and keep cycle-participating edges non-gating until their owning decisions resolve them. When the project needs an accepted DAG, hand its construction and acceptance to `project-dag`.
4. Prepare estimation inputs and schedule-basis decisions where selected, then validate setup evidence and hand off current derivatives and blockers.

Apply accepted defaults and carry authorized preparation forward on agent
initiative. Present human decisions only after the relevant proposal and checks
are ready; deterministic quality evidence routes repair work and does not add a
prompt by itself.

## Resources

Load [inputs, modes, and output contracts](resources/contract.md) when framing the assignment. Use [the detailed method](resources/method.md) for the current stage. Resolve tool commands against the declared tool root.

For an activated package’s subsequent production, load [package activation and production](resources/package-activation.md). Software implementations additionally use [software activation](resources/software-activation.md).
