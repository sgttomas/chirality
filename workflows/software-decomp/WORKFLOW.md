---
name: software-decomp
description: Organize software intent into cohesive work domains and implementable bounded contexts.
---

# software-decomp

Organize software intent into cohesive work domains and implementable bounded contexts.

WORKING_ITEMS coordinates this undertaking and assigns bounded contributions to TASK.

This package implements the grouped-checkpoint Chirality v3 edition of
`docs/DECOMPOSITION_STANDARD.md` (commit `9b005c23a`, 2026-09-09). An in-flight
project keeps the edition it adopted; nothing is retrofitted.

## Method

1. Record the accepted basis identity and accepted portions, then extract atomic scope, objectives, dependencies, and unresolved decisions from that accepted software intent.
2. Define flat Packages and Deliverables, judging semantic coupling and verification demands.
3. Specify each Context Envelope, artifact, interface, acceptance condition, and source mapping, and prepare checks before each grouped human checkpoint.
4. Preserve stable IDs through three checkpoint groups: basis; proposed structure with findings; and audited final acceptance for downstream use.

## Resources

Load [inputs, modes, and output contracts](resources/contract.md) when framing the assignment. Use [the detailed method](resources/method.md) for the current stage. Resolve tool commands against the declared tool root.
