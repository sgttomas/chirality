# Sealed execution brief — D-APP-92 Option A

Status: `SEALED v1 — NO COMMAND MAY DEVIATE`

## Identity

- RequestedBy: App `HELP_HUMAN`
- RunID: `APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04`
- ParentInstanceID: `WI-PKG09-DAPP92-A`
- ChildInstanceID: `A2-DAPP92-A-IMPLEMENT-01`
- Role: fresh ephemeral Agent 2; no delegation
- WorkingRoot: `projects/chirality-app-dev`
- ScopePath: `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity`

## Objective and non-objectives

Execute one exact uninstrumented helper reconstruction and sealed replay using
out-of-process tracing only. Bind the first ordinary authenticated post-GUI
SIGTERM to exact process/socket/owner/descriptor/time evidence and locate the
earliest supported native/App lifecycle seam. Do not add callback/product
logging; do not implement a remedy; do not weaken the first-signal gate; do not
change Root semantics; do not access credentials; do not perform release,
distribution, reliance, Git, foreign-loop, Task Management, or governance work.

## Frozen inputs

- D-APP-92 packet/ruling identities in `ACTIVATION.md`.
- R3 source candidate hashes in `manifests/SOURCE_MANIFEST.md`.
- Exact R2 candidate source directory:
  `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source`.
- D-APP-89 baseline pre-reconstruction hashes and unchanged package-lock in
  `manifests/SOURCE_MANIFEST.md`.
- Runtime root: `/private/tmp/chirality-dapp92-option-a-20260804`.
- Isolated HOME: `/private/tmp/chirality-dapp92-option-a-20260804/home`.
- Isolated userData/store: `/private/tmp/chirality-dapp92-option-a-20260804/user`.
- No owner HOME, keychain, LaunchAgent, login event, or credential value.

## Execution protocol

1. Run only commands already marked `AUTHORIZED_UNPRIVILEGED` in
   `COMMAND_REGISTER.md`, in ascending ID order unless an explicit dependency
   says otherwise.
2. Tool discovery and input hash checks are read-only. Stop on any mismatch.
3. Reconstruct exactly the 12 source surfaces from the frozen candidate; do not
   change `package-lock.json`; prove candidate hashes before build.
4. Use the accepted ordinary-copy dependency substrate and exact Root package
   projections only after their identities reproduce. No install or network.
5. Build/package exact Electron 43.2.0 uninstrumented bits and bind package
   identity/topology/hashes before launch.
6. Seal and follow `manifests/REPLAY_MANIFEST.md`: explicit stale-owner setup/
   recovery, helper launch, helper-to-GUI delay, authenticated public project
   registration without reading or printing token values, GUI contact,
   contact-to-signal delay, snapshots, exact first SIGTERM, bounded 0.1-second
   polls, evidence freeze, and cleanup.
7. Native tracing is out-of-process. Product callback logging or source
   instrumentation is prohibited.
8. If the selected trace attach/launch requires elevation, debugger permission,
   entitlement, GUI automation, persistent security change, signing identity,
   or admin authority, do not invoke it. Freeze all preparation evidence,
   restore source/runtime state, and return the exact command-level request.
9. Raw evidence may retain only public identifiers, paths, process IDs, times,
   event/symbol names, result codes, and redacted state. No token, keychain item,
   API key, secret, credential value, memory dump, environment dump, or process
   argument surface that may expose credentials may be captured.
10. Restore all 7 pre-existing product files to their frozen hashes; remove all
    5 additions, generated packages, dependency projections, runtime trees,
    sockets/owners, and known processes. Prove cleanup before return.

## Stop conditions

Stop on input drift, any unenumerated command/tool/argument/target, any need to
inspect credentials, any changed replay timing/snapshot sequence, any special
authority requirement, any unrelated dirty overlap, or any inability to prove
rollback. No persistent entitlement, SIP/security posture, signing, or broad
admin change is an available recovery action.

## Required return

Return command ledger status, source/package/dependency/identity manifests,
sealed transcript and deviations, process/socket/owner/descriptor/timing and
first-signal evidence, raw trace or exact approval stop, supported-versus-
unknown causal matrix, redaction report, cleanup/rollback proof, runtime
telemetry, limitations, and terminal `PASS_DIAGNOSTIC`, `CONFIRMED_BLOCKER`, or
`HELD_FOR_COMMAND_APPROVAL`. This return cannot itself accept implementation.
