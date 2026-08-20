# Sealed TASK brief — fresh N1 software review

- RequestedBy: `WORKING_ITEMS`
- RunID: `APPDEV_PACKAGED_SECURITY_PROOF_2026-08-20`
- ParentInstanceID: `WI-PKG09-PACKAGED-SECURITY-01`
- ChildInstanceID: `A2-PKG09-PACKAGED-SECURITY-REVIEW-01`
- PackageID: `PKG-09`
- DeliverableIDs: `DEL-09-06`, `DEL-09-04`
- WorkingRoot: `{REPO_ROOT}/projects/chirality-app-dev`
- ScopePath: `{WORKING_ROOT}/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-06_Network_Key_Attachment_and_Renderer_Security_Checks`
- TaskSkill: `software-code-review`
- ApplyEdits: `false`
- AllowedWriteTargets: `[]`
- PROFILE_PATH: `{WORKING_ROOT}/software-workflow.json`
- ImplementationBrief: this RunID's `LAUNCH_BRIEF_IMPLEMENTER.md`.
- AcceptedBasis: `357a58b56726feba49507534159c3fbc4656b818`, D-APP-97 C1, both selected `SOW_V1` contracts, and the frozen graph v1.
- DiffBasis: `FROZEN_DIFF_MANIFEST.md`, exactly 47 subject paths, aggregate identity `eeabad67107add91cea891b03c63d89c940244155d1d240082223119de80983c`.
- VerificationEvidence: `N1_CHECKS.json`, `IMPLEMENTER_RETURN.md`, `STATUS_IMPLEMENTER.json`, the DEL-09-06 proof package, DEL-09-04 derivative pointer, and the TASK run record, all frozen by exact hash.
- APP-HOLD: immediate reviewer-dispatch preflight `ALLOW`; both targets `CLEAR / NOT_HELD`; register SHA-256 `e7408516cb32ad4414f246b594bdc64a088773d7fd6e1c6629e2184c4ac82f7f`; scan fingerprint `00ebfe65174eaf28332dba6c3b1da8f8034b29d91d596bf4543865087f7da1c2`.

## Objective

Perform a fresh, independent, filesystem-read-only software review over 100%
of the frozen N1 product-source diff and complete evidence subject. Determine
whether the bounded proof implementation is correct, secure, contained,
truthfully evidenced, and valid to land as partial engineering progress while
packaged-security acceptance remains failed on the held credential-precedence
defect.

The known production defect is not writable or remediable here:
`SafeStorageCredentialStore.get('anthropic')` resolves
`CHIRALITY_ANTHROPIC_API_KEY` before `ANTHROPIC_API_KEY`. Agent 0 disposition
is `RECORD/HOLD scope widening`; repair belongs to DEL-02-05 R03 / DEL-04-05
RQ-001. Treat it as an accepted blocker only if the candidate records it
truthfully, keeps both Remaining items open, and does not mask it with a false
pass.

## Required review

1. Recompute all 47 file hashes and the aggregate identity before semantic review.
2. Review all nine frozen product-source paths in full against the accepted basis, tracing behavior through relevant callers/contracts/tests. Pay particular attention to process cleanup, socket/path isolation, packaged daemon authentication, credential lifecycle, secret redaction, TCP parsing/classification, renderer proof signals, fail-closed logic, CI command ordering, and unsigned/no-live-credential fences.
3. Review all 38 evidence/control subject files for internal consistency, parseability, attempt history, exact source/artifact identity, command/result truth, secret hygiene, and calibrated claims.
4. Confirm focused/full/typecheck/build/APP-HOLD/self-check/secret/network/dist/instruction-root/packaged-host evidence supports the stated results and no required host proof is inferred or deferred.
5. Confirm the source network proof refactor does not silently weaken provider enforcement and that its narrower renderer-egress claim is accurately separated from focused provider-policy evidence.
6. Confirm the expected-failure precedence test is an executable blocker record, not a waiver, and cannot become an unnoticed permanent bypass.
7. Confirm no production Electron/runtime/provider, dependency/lockfile, status/memory, lifecycle/Approval-SHA, signing/notarization/distribution, provider-scope, real-credential, owner-machine, RunAtLoad, decision/register, shared receipt/log, root-governance, or foreign-loop write occurred.
8. Report actionable findings with exact file/line, impact, evidence, and remediation direction. Distinguish candidate defects from the already-held production blocker.

## Return contract

Return `PASS | PASS_WITH_FINDINGS | FAIL`, exact hash/coverage results, product
and evidence assessment, actionable findings, accepted blocker treatment,
residual risks, write/tool compliance, and manager recommendation. `PASS`
requires zero actionable candidate finding and 100% frozen coverage. Do not
edit any file, create a TASK run record, stage, commit, push, open a PR, run a
release action, remediate, or delegate. The manager will persist your native
return and status after completion.
