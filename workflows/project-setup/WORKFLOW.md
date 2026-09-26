---
name: project-setup
description: Initialize an accepted project workspace and coordinate its selected setup and estimation phases.
---

# project-setup

Initialize an accepted project workspace and coordinate its selected setup and estimation phases.

WORKING_ITEMS coordinates this undertaking and assigns bounded contributions to TASK.
Selection does not launch setup or change roles. HELP_HUMAN may coordinate a
request for this workflow, but execution routes to an eligible WORKING_ITEMS
instance with actual host permissions and a run-specific brief.

## Method

1. Inspect accepted decomposition, existing workspace state, coordination representation, and activation scope.
2. Apply the `preparation` skill, then dispatch the selected production, semantic, dependency (`dependency-extract`, then `audit-dep-closure`), or domain workflows as bounded stages.
3. Sequence dependent work from accepted outputs; route SCCs to `scc-resolution-case` and keep cycle-participating edges non-gating until their owning decisions resolve them. Project-DAG construction and acceptance has no bundled workflow yet and runs under an authorized ad hoc plan with human acceptance.
4. Prepare estimation inputs and schedule-basis decisions where selected, then validate setup evidence and hand off current derivatives and blockers.

Apply accepted defaults and carry authorized preparation forward on agent
initiative. Present human decisions only after the relevant proposal and checks
are ready; deterministic quality evidence routes repair work and does not add a
prompt by itself.

## Resources

Load [inputs, modes, and output contracts](resources/contract.md) when framing the assignment. Use [the detailed method](resources/method.md) for the current stage. Resolve tool commands against the declared tool root.

For an activated package’s subsequent production, load [package activation and production](resources/package-activation.md). Software implementations additionally use [software activation](resources/software-activation.md).
