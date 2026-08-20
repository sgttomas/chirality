# Sealed Agent 2 brief — fresh independent review

- RequestedBy: `WORKING_ITEMS`
- RunID: `APPDEV_PACKAGED_SDK_PROOF_2026-08-20`
- ParentInstanceID: `WI-PKG09-DEL0904-PACKAGED-SDK-01`
- ChildInstanceID: `A2-DEL0904-PACKAGED-SDK-REVIEW-01`
- PackageID: `PKG-09`
- DeliverableIDs: `DEL-09-04`
- ScopePath: `{WORKING_ROOT}/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity`
- WorkingRoot: `{REPO_ROOT}/projects/chirality-app-dev`
- TaskSkill: `software-code-review`
- ApplyEdits: `false`
- ImplementationBrief: `{WORKING_ROOT}/execution/_Coordination/AgentRuns/APPDEV_PACKAGED_SDK_PROOF_2026-08-20/LAUNCH_BRIEF_IMPLEMENTER.md`
- AcceptedBasis: `d8c47d9fbc459b32c053c844be0fa789fd1ffab2`, D-APP-97 C1, frozen graph/activation, APP-HOLD review preflight must be `ALLOW`.
- DiffBasis: `{WORKING_ROOT}/execution/_Coordination/AgentRuns/APPDEV_PACKAGED_SDK_PROOF_2026-08-20/FROZEN_DIFF_MANIFEST.md`; verify all 13 hashes before review, then review 100% of those frozen paths against the accepted basis, including each new file in full.
- VerificationEvidence: implementer return, normalized registered-check JSON, TASK run record, focused test/YAML/Bash/G4/receipt/corpus evidence described there. Actual macOS package proof and committed candidate-range G4 are intentionally owed and must not be inferred.
- PROFILE_PATH: `{WORKING_ROOT}/software-workflow.json`
- AllowedWriteTargets: `[]` (read-only). Do not create a deliverable TASK run record; runtime launch/status/terminal return are the durable record.
- AllowedTools: read/search, Git read-only diff/status/show, hash verification, and read-only software-workflow scope/check-selection tools allowed by the skill. Do not edit, install, run release/publish actions, access credentials, or execute the actual packaged app.
- Objective: independently review the entire frozen diff for correctness, failure modes, ordering, evidence integrity, security/fence preservation, test adequacy, write containment, G4 manifest correctness, and truthful pre-CI deliverable state.
- AcceptanceCriteria:
  1. Confirm every frozen hash matches before substantive review; mismatch is blocking and returns `FAIL`.
  2. Trace both verifier invocations and prove the mounted invocation can only occur after read-only attach and before detach/cleanup, with a mounted Resources root distinct from the staged root.
  3. Confirm fail-closed JSON checks require `status: pass` and `proofMode: scripted-no-live-provider`, and both retained summaries are uploaded/named in aggregate evidence.
  4. Confirm the verifier remains unchanged and no live provider/network, credential, signing/notarization, distribution/publication, release, dependency/lockfile, lifecycle/Checking Approval SHA, owner-machine, or foreign-loop behavior is introduced.
  5. Review test strength against regressions in path distinction, mount ordering, output retention, proof-mode validation, existing artifact gates, and no-publication posture.
  6. Review all coordination/deliverable evidence for claim calibration: external macOS execution and candidate-range G4 remain REQUIRED/owed, R4-P49 Remaining stays open, DEL-09-04 remains IN_PROGRESS.
  7. Return only actionable findings with exact file/line, impact, evidence, and remediation. Final verdict is `PASS` only with no actionable findings; otherwise `FAIL` and manager serializes remediation/re-review.
- EXCLUSIONS: no edits, no remediation, no delegation, no lifecycle/release/acceptance claim, no commit/push/PR/merge, no external package proof inference.
- ExpectedReturn: verdict; hash/coverage statement; actionable findings; evidence assessment; residual external risk; write-scope/fence assessment; manager fan-in recommendation.
