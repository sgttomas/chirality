# Local work graph methods — implementation and review

Basis: `379df923927d157be3ebb51d8a1dcf783d970112`. Owner: Ryan Tufts. Integration: HELP_HUMAN `/root`.

## Authorization and scope

Owner direction in this task, 2026-09-22, transcribed verbatim:

> You may open the PR and merge when the CI goes green.  Select the appropriate level of CI for this.

This follows the owner's review and revision of the two workflow drafts,
App/Piping LOOP_INIT replacements and companion instruction changes. Earlier
clarification selected "Infer and clarify material gaps". Source integration
is authorized; no product work, run activation, lifecycle acceptance or release
is initiated by this tranche.

The methods are registered in Root's bundled library as
`chirality-root:bundled:workflow:construct-local-work-graph` and
`chirality-root:bundled:workflow:bounded-reconciliation`. They use specialist
navigation categories Plan & organize and Review & check, leaving central/Core
membership unchanged. The authoring basis is the bundled create-workflow method.
The reviewed draft bytes remain local to the original task; maintained packages
are committed at `workflows/` and do not depend on those drafts or ZIPs.

## Integration with current main

The draft basis was `00115c719`; current main contains the separately activated
App/Piping September 21 whole-corpus reconciliation graphs. Both entry pointers
now locate those graphs instead of App `none` / the older Piping UI graph.
Existing phase cursors, pinned methods and owner gates remain operative.
The newly merged D-GOV-44 claim-granularity rule is reflected in the bounded
method: requirements and stable scope remain distinct from mechanism detail.
No in-flight run is silently re-pinned or switched to the new method.

The companion changes relocate substantive checks/fences into the owning
project AGENTS files, preserve historical evidence citations and receipt
validation, and distinguish pointer maintenance from behavioral instruction
amendments. Notices route to App, Piping, Runtime and PEC.

## Verification and independent review

Validation is recorded against the actual candidate in the PR. Required local
coverage comprises workflow metadata/catalog/discovery, instruction entrypoints,
agent contracts, routed practitioner-harness/validation/workflow-runtime tests,
self-check, App hold-register integrity and G0–G4. Product source and build
configuration are untouched, so product-profile build and native witnesses are
not newly required locally. Existing hosted path-selection policies still
apply; no bypass label, check waiver or CI policy change is part of this work.

Independent final-candidate review and final validation: pending before push.
