# Sealed TASK brief — fresh corrected-candidate review 02

- RequestedBy: `WORKING_ITEMS`
- RunID: `APPDEV_PACKAGED_SECURITY_PROOF_2026-08-20`
- ParentInstanceID: `WI-PKG09-PACKAGED-SECURITY-01`
- ChildInstanceID: `A2-PKG09-PACKAGED-SECURITY-REVIEW-02`
- PackageID: `PKG-09`
- DeliverableIDs: `DEL-09-06`, `DEL-09-04`
- WorkingRoot: `{REPO_ROOT}/projects/chirality-app-dev`
- ScopePath: `{WORKING_ROOT}/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-06_Network_Key_Attachment_and_Renderer_Security_Checks`
- TaskSkill: `software-code-review`
- ApplyEdits: `false`
- AllowedWriteTargets: `[]`
- PROFILE_PATH: `{WORKING_ROOT}/software-workflow.json`
- ImplementationBrief: `LAUNCH_BRIEF_REMEDIATION_01.md`, with the original implementer brief and R1 return as predecessor context.
- AcceptedBasis: `357a58b56726feba49507534159c3fbc4656b818`, D-APP-97 C1, both selected `SOW_V1` contracts, frozen graph v1.
- DiffBasis: `FROZEN_DIFF_MANIFEST_V2.md`; exactly 88 reconstructed subject paths; aggregate identity `db85316f5f5d711e4aa3b248368c62e5448c01b6716fc2b284075dc0754f8bc4`.
- VerificationEvidence: original N1 records/evidence, R1 `FAIL`, all Remediation_01 evidence, `REMEDIATION_CHECKS_01.json`, `REMEDIATION_RETURN_01.md`, `STATUS_REMEDIATION_01.json`, and both TASK records.
- APP-HOLD: immediate review-02 dispatch preflight `ALLOW`; both targets `CLEAR / NOT_HELD`; register SHA-256 `e7408516cb32ad4414f246b594bdc64a088773d7fd6e1c6629e2184c4ac82f7f`; scan fingerprint `00ebfe65174eaf28332dba6c3b1da8f8034b29d91d596bf4543865087f7da1c2`.

## Objective

Perform a new fresh, independent, filesystem-read-only review over 100% of the
corrected 88-path candidate. Verify the ten product paths in full, every
original/remediation evidence and control path, and exact closure of all five
R1 findings. Decide whether the proof implementation is valid to land as
partial engineering progress while the accepted production precedence
blocker remains open and both deliverable Remaining items remain unchanged.

## Required review

1. Reconstruct the exact 88-path subject, verify its aggregate identity, and review all ten product paths plus all 78 evidence/control paths.
2. Recheck each R1 finding: usable full Electron descendant capture with observed renderer-child TCP and fail-closed capture predicate; credential/provider env scrub; post-operation/post-stream credential/artifact scanning; post-mutation oMLX isolation; cleanup propagation/confirmed shutdown in PASS; calibrated owner-user-data attempt history.
3. Verify source attempts 1–2 fail for retained reasons and attempt 3 passes with 4/4 usable snapshots, descendants, child TCP, blocked probe, and zero non-allowlisted egress.
4. Verify packaged remediation proof passes with fresh identity `3da8cbbbd5cd543dce0c400975cf42b2bdfadd0b8dc6ccd61aab6489c38acee5`, complete fixture scan, provider isolation, confirmed GUI/daemon shutdown, stream closure, and temp cleanup.
5. Verify focused/full/typecheck/build/harness/APP-HOLD/self-check/secret/dist/instruction-root/scope/diff evidence and all claim calibration/non-claims.
6. Confirm the expected precedence failure remains self-expiring and cannot be read as waiver/closure. Confirm no Remaining, status, memory, lifecycle/Approval-SHA, production runtime, lockfile, shared, governance, release, credential, owner-machine, or foreign-loop write.
7. Report only actionable candidate findings with exact location, impact, evidence, and remediation direction. The already-held production blocker is not a candidate finding if truthfully preserved.

## Return contract

Return `PASS | PASS_WITH_FINDINGS | FAIL`; exact identity/coverage; per-finding
closure; product/evidence/check assessment; accepted blocker treatment;
actionable findings; residual risk; write/tool compliance; manager
recommendation. `PASS` requires 100% coverage and zero actionable candidate
finding. Do not write any file or TASK record, remediate, stage, commit, push,
open a PR, run release actions, or delegate. The manager persists the native
return/status.
