# Sealed TASK brief — N1 remediation 01

- RequestedBy: `WORKING_ITEMS`
- RunID: `APPDEV_PACKAGED_SECURITY_PROOF_2026-08-20`
- ParentInstanceID: `WI-PKG09-PACKAGED-SECURITY-01`
- ChildInstanceID: `A2-PKG09-PACKAGED-SECURITY-REMEDIATION-01`
- PackageID: `PKG-09`
- DeliverableIDs: `DEL-09-06`, `DEL-09-04`
- WorkingRoot: `{REPO_ROOT}/projects/chirality-app-dev`
- ScopePath: `{WORKING_ROOT}/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-06_Network_Key_Attachment_and_Renderer_Security_Checks`
- TaskSkill: `software-bounded-implementation`
- ApplyEdits: `true`
- PROFILE_PATH: `{WORKING_ROOT}/software-workflow.json`
- AcceptedBasis: repository basis `357a58b56726feba49507534159c3fbc4656b818`; frozen N1 candidate identity `eeabad67107add91cea891b03c63d89c940244155d1d240082223119de80983c`; R1 `FAIL` in `REVIEWER_RETURN.md`.
- APP-HOLD: immediate remediation-dispatch preflight `ALLOW`; both targets `CLEAR / NOT_HELD`; register SHA-256 `e7408516cb32ad4414f246b594bdc64a088773d7fd6e1c6629e2184c4ac82f7f`; scan fingerprint `00ebfe65174eaf28332dba6c3b1da8f8034b29d91d596bf4543865087f7da1c2`.

## Objective

Remediate only R1's five actionable proof-glue/evidence findings, rerun every
affected/full/host proof surface, and return a corrected candidate for a new
fresh review. Preserve all prior failure attempts and frozen records; issue
versioned remediation evidence rather than rewriting history.

## Required remediation

1. Source renderer-egress proof: enumerate the complete Electron descendant
   process tree including renderer/network-service children; capture those
   PIDs; fail closed when capture is unusable rather than accepting empty
   `lsofExitCode: 1`; add a regression that proves child traffic is observed;
   rerun with usable capture evidence and calibrate renderer/provider claims.
2. Packaged credential proof: scan complete daemon/GUI streams and emitted
   artifacts after credential store/status/remove and stream closure for the
   generated fixture; re-query oMLX after Anthropic store and remove; add
   negative regressions for an operation-time leak and cross-provider mutation.
3. Packaged cleanup: propagate cleanup failure, record confirmed GUI and
   daemon shutdown, and require cleanup confirmation in the final PASS
   predicate/summary with regression coverage.
4. Source credential fence: scrub all inherited provider credential variables
   before launching child processes; use only unmistakable non-secret fixtures
   when the proof requires a value; add regression coverage.
5. Attempt-history calibration: preserve the first source attempt, explicitly
   record that it started Electron with the owner's default user-data path and
   that no pre/post filesystem audit exists; retract the global no-owner-write
   claim for that attempt. All credited reruns must isolate user data from
   process start.

## AllowedWriteTargets

- `{WORKING_ROOT}/frontend/scripts/run-network-policy-proof.mjs`
- `{WORKING_ROOT}/frontend/scripts/run-packaged-security-proof.mjs`
- `{WORKING_ROOT}/frontend/src/__tests__/scripts/run-network-policy-proof.test.ts`
- `{WORKING_ROOT}/frontend/src/__tests__/scripts/run-packaged-security-proof.test.ts`
- `{WORKING_ROOT}/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-06_Network_Key_Attachment_and_Renderer_Security_Checks/Evidence/Packaged_Security_Proof_2026-08-20/Remediation_01/**`
- `{WORKING_ROOT}/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-06_Network_Key_Attachment_and_Renderer_Security_Checks/_run_records/**`
- `{WORKING_ROOT}/execution/_Coordination/AgentRuns/APPDEV_PACKAGED_SECURITY_PROOF_2026-08-20/REMEDIATION_RETURN_01.md`
- `{WORKING_ROOT}/execution/_Coordination/AgentRuns/APPDEV_PACKAGED_SECURITY_PROOF_2026-08-20/STATUS_REMEDIATION_01.json`
- `{WORKING_ROOT}/execution/_Coordination/AgentRuns/APPDEV_PACKAGED_SECURITY_PROOF_2026-08-20/REMEDIATION_CHECKS_01.json`

No prior evidence, implementer/reviewer record, workflow, package/config,
production Electron/runtime/provider, lockfile, deliverable status/memory,
shared surface, governance, or foreign-loop file is writable.

## Checks and host proof

Run focused source/packaged proof regressions first, then all affected and full
frontend tests, typecheck, build, APP-HOLD integrity, mandated mise-Python root
self-check, secret scan, source network proof, fresh unsigned `desktop:dist`,
instruction-root integrity, and fresh packaged-host proof. Request exact host
escalation yourself for packaging/Electron/process/network/keychain surfaces;
do not infer a pass or downgrade a denial. Retain all remediation attempts
below `Remediation_01/` and persist normalized results.

## Acceptance and exclusions

All five R1 findings must be demonstrably closed, all checks must pass, all
writes must be contained, and the return must preserve the separate accepted
API-key precedence blocker. Do not edit `frontend/electron/api-key-storage.ts`
or any production security/runtime behavior. Do not remove Remaining items or
change lifecycle/Approval SHA. No dependency/lockfile/pin, live credential,
provider expansion, signing/notarization/distribution/publication, release,
owner-machine, RunAtLoad, decision/register, shared receipt/log, root
governance, commit, push, PR, merge, or delegation act.

## ExpectedReturn

Persist a new TASK run record, `REMEDIATION_CHECKS_01.json`,
`REMEDIATION_RETURN_01.md`, and final `STATUS_REMEDIATION_01.json`. Return
`SUCCESS | FAILED | FAILED_INPUTS`, exact changed paths, per-finding closure,
commands/evidence, host results, write containment, accepted blocker,
residuals/reruns, and manager recommendation. Do not delegate.
