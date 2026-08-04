# Activation — D-APP-88 helper bundle resume R3

- RunID: `APPDEV_DAPP88_HELPER_BUNDLE_RESUME_R3_2026-08-04`
- InstanceID: `WI-PKG09-DAPP88-R3`
- Parent: App `HELP_HUMAN`
- Role: `WORKING_ITEMS`
- Package: `PKG-09 Validation, Packaging, Security and Release`
- Selected deliverable: `DEL-09-04 macOS DMG Packaging and Instruction Root Integrity`
- Representation: `SOW_V1`
- Git basis: `cdc76a1d398231267f1379e7143b4de27abaa01b`
- Branch: `codex/app-dapp88-evaluation-resume-20260804`
- Authority: D-APP-88 Option B ruling and packet.
- Accepted dependency: Root TM-ROOT-112 `G2 + C1 + F1` repair accepted at exact product hashes recorded in `ROOT_EVIDENCE_FITNESS.md`.
- Frozen predecessor: D-APP-88 R2 handoff/manager return and reconstructable candidate-source evidence; R2 remains accepted only as `BLOCKED/PARTIAL` diagnostic evidence.
- Profile: `projects/chirality-app-dev/software-workflow.json`.
- Objective: evaluate the accepted Root repair against the exact R2 blocker; rebuild a source-aligned distinct Electron helper from the frozen R2 evidence only if that dependency is fit; run every D-APP-88 package/live/validation conjunct; obtain fresh adversarial verification; reconcile DEL-09-04 only on proven acceptance.
- Work posture: serialized evidence fitness → bounded source implementation → package/live/full validation → fresh read-only adversarial verification → manager fan-in.
- Integration owner: this `WORKING_ITEMS` instance.
- Explicit limitation: Node 22.19 remains unexecuted and cannot be claimed as covered.
- Downstream rider: only if D-APP-88 implementation is accepted, report that TM-APP-036's mandatory non-blocking D-APP-86 parity-rerun rider has fired; do not execute the parity rerun in this instance.

## Write boundary

Allowed writes are limited to:

- `projects/chirality-app-dev/frontend/**`;
- `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity/**`;
- this run root; and
- `projects/chirality-app-dev/plans/PLAN_COMPLETION_LOG.md` only if required for truthful closeout.

No App decision register, Task Management register, loop receipt, other deliverable/package, Root runtime/docs, Piping/PEC/domain-engine, PRD/decomposition/SCOPE_CHANGE, or Git write is authorized. D-APP-89 rollback state, D-APP-91 planning-only scope, all six D-APP-81 UNKNOWN relations, and every hard fence remain operative.
