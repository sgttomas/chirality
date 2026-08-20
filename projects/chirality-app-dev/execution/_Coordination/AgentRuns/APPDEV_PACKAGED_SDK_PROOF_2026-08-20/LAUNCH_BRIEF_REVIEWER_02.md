# Sealed Agent 2 brief — correction review 02

- RequestedBy: `WORKING_ITEMS`
- RunID: `APPDEV_PACKAGED_SDK_PROOF_2026-08-20`
- ParentInstanceID: `WI-PKG09-DEL0904-PACKAGED-SDK-01`
- ChildInstanceID: `A2-DEL0904-PACKAGED-SDK-REVIEW-02`
- PackageID: `PKG-09`
- DeliverableIDs: `DEL-09-04`
- ScopePath: `{WORKING_ROOT}/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity`
- WorkingRoot: `{REPO_ROOT}/projects/chirality-app-dev`
- TaskSkill: `software-code-review`
- ApplyEdits: `false`
- AcceptedBasis: `d8c47d9fbc459b32c053c844be0fa789fd1ffab2`, D-APP-97 C1, APP-HOLD review preflight `ALLOW` required.
- DiffBasis: `FROZEN_DIFF_MANIFEST_V2.md`; verify all 23 file hashes and aggregate identity `94bc56814f74ae7ed23da008869fda278c5a814c7b13cae65ac9f85ce0e8d545` before substantive review.
- CorrectionBasis: `AMENDMENT_01_EOF_WHITESPACE.md`; compare the corrected candidate to the staged predecessor and verify the only byte changes to previously reviewed files are ten final-empty-line deletions.
- AllowedWriteTargets: `[]`. Read-only; do not create a TASK run record or modify index/worktree state.
- AllowedTools: read/search; Git read-only status/diff/show; hashing; read-only software-workflow scope/check-selection tools permitted by the skill.
- Objective: review 100% of all 23 corrected frozen subject files for correctness, scope, evidence integrity, whitespace closure, claim calibration, preserved product behavior, and unchanged fences.
- AcceptanceCriteria:
  1. All 23 hashes and aggregate candidate identity match exactly.
  2. Correction is limited to the ten named EOF blank-line deletions plus the amendment record; product/workflow/test/DEL-state bytes remain identical to the previously reviewed candidate.
  3. No stale v1 identity or first-review claim is used as current closeout proof; v2 manifest and this review govern correction closeout.
  4. The complete corrected candidate remains correct against D-APP-97 and the original implementation acceptance criteria, with external macOS/G4 proof still owed.
  5. Report actionable findings with exact file/line and remediation. Verdict is `PASS` only with no actionable findings.
- EXCLUSIONS: no edits, remediation, delegation, commit/push/PR/merge, release/lifecycle act, or external-proof inference.
- ExpectedReturn: PASS/FAIL; preflight; 23-path hash/coverage evidence; correction-boundary evidence; product/fence assessment; findings; manager recommendation.
