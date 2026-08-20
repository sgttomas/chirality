# Sealed TASK brief — N1 packaged-security implementation

- RequestedBy: `WORKING_ITEMS`
- RunID: `APPDEV_PACKAGED_SECURITY_PROOF_2026-08-20`
- ParentInstanceID: `WI-PKG09-PACKAGED-SECURITY-01`
- ChildInstanceID: `A2-PKG09-PACKAGED-SECURITY-IMPLEMENT-01`
- PackageID: `PKG-09`
- DeliverableIDs: `DEL-09-06`, `DEL-09-04`
- WorkingRoot: `{REPO_ROOT}/projects/chirality-app-dev`
- ScopePath: `{WORKING_ROOT}/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-06_Network_Key_Attachment_and_Renderer_Security_Checks`
- TaskSkill: `software-bounded-implementation`
- ApplyEdits: `true`
- PROFILE_PATH: `{WORKING_ROOT}/software-workflow.json`
- AcceptedBasis: repository/branch basis `357a58b56726feba49507534159c3fbc4656b818`; D-APP-97 C1; both selected `SOW_V1` contracts at decomposition basis `7b0be4d8772a16e5a4774a17988479587d00acca`; frozen plan/graph v1 in this RunID root.
- APP-HOLD: dispatch preflight immediately before launch is `ALLOW`; both targets `CLEAR / NOT_HELD`; register SHA-256 `e7408516cb32ad4414f246b594bdc64a088773d7fd6e1c6629e2184c4ac82f7f`; scan fingerprint `00ebfe65174eaf28332dba6c3b1da8f8034b29d91d596bf4543865087f7da1c2`.

## Objective

Build and execute the smallest coherent packaged-artifact network,
key-attachment, and renderer-security proof. On passing evidence, close only
DEL-09-06's open D-APP-97 R4-P49 Remaining scope and DEL-09-04 REQ-009 /
R4-P49 packaged-security residual. Use the existing security controls and
proofs where sound; add or modify only proof/packaging scripts, automated
tests, or unsigned CI integration necessary to make the packaged proof real,
repeatable, fail-closed, and evidence-bearing.

## Dependencies

DEL-09-06 is the proof producer and DEL-09-04 the dependent packaged-security
consumer. Preserve this one-node relationship. Do not create or execute a
second engineering node.

## Declared reads

The frozen plan/graph; governing agent/TASK/skill/profile contracts; D-APP-97;
both deliverables' SOW/status/context/memory/references/dependencies,
assessments, and relevant evidence; `.github/workflows/desktop-release-template.yml`; `frontend/package.json`; relevant packaging config, `frontend/scripts/**`, `frontend/electron/**`, `frontend/src/lib/**`, and tests; Git read-only identity/diff/status/history.

## AllowedWriteTargets

- `{REPO_ROOT}/.github/workflows/desktop-release-template.yml` only if bounded unsigned CI proof integration is necessary.
- `{WORKING_ROOT}/frontend/scripts/**` only for packaged security proof, packaging proof, evidence aggregation, or verification behavior.
- `{WORKING_ROOT}/frontend/src/__tests__/**` only for focused proof/security/workflow regressions.
- `{WORKING_ROOT}/frontend/package.json` only if an explicit non-release proof command alias is necessary.
- `{WORKING_ROOT}/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-06_Network_Key_Attachment_and_Renderer_Security_Checks/Evidence/Packaged_Security_Proof_2026-08-20/**`
- `{WORKING_ROOT}/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-06_Network_Key_Attachment_and_Renderer_Security_Checks/_STATUS.md`
- `{WORKING_ROOT}/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-06_Network_Key_Attachment_and_Renderer_Security_Checks/MEMORY.md`
- `{WORKING_ROOT}/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-06_Network_Key_Attachment_and_Renderer_Security_Checks/_run_records/**`
- `{WORKING_ROOT}/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity/Evidence/Packaged_Security_Proof_2026-08-20/**`
- `{WORKING_ROOT}/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity/_STATUS.md`
- `{WORKING_ROOT}/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity/MEMORY.md`
- `{WORKING_ROOT}/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity/_run_records/**`
- `{WORKING_ROOT}/execution/_Coordination/AgentRuns/APPDEV_PACKAGED_SECURITY_PROOF_2026-08-20/IMPLEMENTER_RETURN.md`
- `{WORKING_ROOT}/execution/_Coordination/AgentRuns/APPDEV_PACKAGED_SECURITY_PROOF_2026-08-20/STATUS_IMPLEMENTER.json`
- `{WORKING_ROOT}/execution/_Coordination/AgentRuns/APPDEV_PACKAGED_SECURITY_PROOF_2026-08-20/N1_CHECKS.json`

No other file is writable. In particular, `package-lock.json`, production
Electron/runtime/provider implementation, decisions/registers, shared
receipts/completion logs, lifecycle/Approval-SHA surfaces, root governance,
and foreign loops are not writable.

## Checks and proof surfaces

Run focused regressions, full frontend Vitest, applicable frontend and
Electron typecheck, registered build, secret scan, network policy,
instruction-root integrity, unsigned desktop pack/dist, and the actual
packaged proof. Also run APP-HOLD integrity, software change-scope validation,
and diff/whitespace checks before return. Use the accepted profile helpers for
registered checks and retain one normalized `N1_CHECKS.json` summary.

Where packaging, Electron, process/network capture, or keychain access is
blocked by the sandbox, request escalation for the exact command and run it
yourself in-session. A sandbox denial is not a pass, waiver, or environment
class. Park with `HOST_RERUN_REQUIRED` only if the escalation request itself
is declined, recording that exact declined command. PR CI is allowed only for
registered checks or the bounded unsigned artifact proof integrated by this
node; it does not silently replace required host proof.

## AcceptanceCriteria

1. A freshly built unsigned macOS artifact is identity-bound and the proof exercises packaged bytes, not a repository-dev substitute.
2. Packaged network evidence is fail-closed and shows zero non-allowlisted outbound TCP, the required blocked renderer diagnostic/probe signal, and separate provider/renderer enforcement without provider expansion.
3. Key evidence covers accepted precedence/storage and proves no key leakage into logs, events, summaries, tracked files, or retained artifacts; renderer policy metadata cannot leak credential, query, or userinfo material.
4. Attachment evidence covers server-side path/type/symlink/readability and byte-budget enforcement, partial-failure continuation, total-failure `ATTACHMENT_FAILURE`, and failed-send retry preservation.
5. All named focused/full/build/secret/network/instruction-root/unsigned package/packaged-proof checks pass with stable evidence tied to the artifact and source revision.
6. Remove the two exact Remaining residuals only after proof passes. Preserve both `IN_PROGRESS` states, Checking Approval SHA, unrelated Remaining items, F-APP-2, and all non-claims.
7. Every changed path is within the whitelist and the final return names exact evidence, host commands/results, blockers, reruns, and residual risks.

## EXCLUSIONS

No signing, notarization, distribution/publication, release claim, provider
expansion, real credential use, lifecycle transition, Checking Approval SHA
change, owner-machine daemon deployment, login-time `RunAtLoad`, decision or
register edit, dependency/lockfile/pin change, foreign-loop/root-governance
change, commit, push, PR, merge, or delegation. If a required remedy is
outside proof/packaging/test/CI glue, return the blocker; do not widen scope.

## ExpectedReturn

Persist a complete TASK run record, `N1_CHECKS.json`,
`IMPLEMENTER_RETURN.md`, and final `STATUS_IMPLEMENTER.json`. Return
`SUCCESS | FAILED | FAILED_INPUTS`, exact changes and evidence, every command
and surface, write containment, acceptance mapping, deliverable effects,
blockers/reruns, derivative status, and manager recommendation. Do not
delegate.
