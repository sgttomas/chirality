# Corrected frozen candidate manifest v2

- FrozenAt: `2026-08-20T05:12Z`
- AcceptedBasis: `d8c47d9fbc459b32c053c844be0fa789fd1ffab2`
- SupersedesForCloseout: `FROZEN_DIFF_MANIFEST.md` and the first reviewer PASS, solely because amendment 01 changed ten record EOF byte identities.
- SubjectPathCount: `23`
- CandidateIdentitySHA256: `94bc56814f74ae7ed23da008869fda278c5a814c7b13cae65ac9f85ce0e8d545`
- IdentityMethod: SHA-256 of the bytewise path-sorted 23 lines emitted as `<file-sha256><two spaces><repo-relative-path><newline>`.
- ReviewContract: verify all hashes and the aggregate identity, then review 100% of all 23 corrected subject files against the accepted basis. `FROZEN_DIFF_MANIFEST_V2.md`, `LAUNCH_BRIEF_REVIEWER_02.md`, `STATUS_REVIEW_CORRECTION_01.json`, and later reviewer/manager closeout records are after-freeze review-control evidence, not subject bytes.
- CorrectionBoundary: compared with the previously reviewed candidate, only ten named AgentRuns files lose one final empty line and `AMENDMENT_01_EOF_WHITESPACE.md` is added. Product/workflow/test/deliverable-state bytes are unchanged.

| SHA-256 | Corrected frozen subject path |
|---|---|
| `24642cf7d2d8c1a7aed555eea9afae9d6be120b7bdbad2a2560cc551d2423109` | `.github/workflows/desktop-release-template.yml` |
| `bcfaeacc87f377fb8c344f3a2e43b0ce38723b4798d91323e31bceeca4e0b0db` | `docs/governance_harness/tranche_manifests/APP-DEL0904-PACKAGED-SDK-CI-20260820.yaml` |
| `0770139129eba0f5b815aeaedef821e5307e9f6436210c3c7adc1d0bfffddcf3` | `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity/MEMORY.md` |
| `fd4c72e51cf7f59e92229500d7d4ce27e0c7a4372f4881113a7c1cbd1768ef36` | `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity/_STATUS.md` |
| `8035234b088d8b8ccf13ca4a61166635490e1f00fabd1d74f7b0508a7de572d4` | `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity/_run_records/TASK_RUN_2026-08-20_0404.md` |
| `3ea37dcb9665be18351f69ed7acbd1fc1d8dd90adb731bacadc9ced4eb86fa39` | `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity/_run_records/TASK_RUN_2026-08-20_0404_CHECKS.json` |
| `bb391db9653a3e596ff2efb4581d044171694e7c311d7bb976c9df14396b80ed` | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_PACKAGED_SDK_PROOF_2026-08-20/ACTIVATION.md` |
| `ff39cb916cc30d1592ef3ddd46ac02c614b063108a215c8190e64e5b7d3583e7` | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_PACKAGED_SDK_PROOF_2026-08-20/AMENDMENT_01_EOF_WHITESPACE.md` |
| `bbe00676708bf02cf9e9fa7da4cf8a0dc5baac1ec5f94159bd80e0620d77f09b` | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_PACKAGED_SDK_PROOF_2026-08-20/FROZEN_DIFF_MANIFEST.md` |
| `9f851356e33ec34693839eb6990d5e2a2c479c7d34c52a016410c5cd7d25aeba` | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_PACKAGED_SDK_PROOF_2026-08-20/HANDOFF_STATE.md` |
| `885cf6eaa579b94f8d0213dcc580690d2fc10be5b577eae71d14427f1a474ddc` | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_PACKAGED_SDK_PROOF_2026-08-20/IMPLEMENTER_RETURN.md` |
| `be076c67514d25207aeb586d8d672e8c3417c151a761c2306f8b5660556f390d` | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_PACKAGED_SDK_PROOF_2026-08-20/LAUNCH_BRIEF_IMPLEMENTER.md` |
| `adb7f6cce1a8dd487d4c926e06890a58acade27ed7063f279b5292da2258451c` | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_PACKAGED_SDK_PROOF_2026-08-20/LAUNCH_BRIEF_REVIEWER.md` |
| `3a2179939237f8c6d4996fd824b51c3f24c6c896dfdafeaa5d77c5f3657cda75` | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_PACKAGED_SDK_PROOF_2026-08-20/MANAGER_RETURN.md` |
| `0174abb2171879e30645f0aa3d92f473eda894abd9119949cd73105765680473` | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_PACKAGED_SDK_PROOF_2026-08-20/MANAGER_VALIDATION.md` |
| `1b6db8da6feae8a92a35ee272111224deadb2cd0a760e268faf25b5047c9a9e0` | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_PACKAGED_SDK_PROOF_2026-08-20/REVIEWER_RETURN.md` |
| `c930aa83900679b64e5a46f3a01dc2924aee98db59a4c060186c4d82ba409f5d` | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_PACKAGED_SDK_PROOF_2026-08-20/STATUS.json` |
| `1f053c7017685d0c1bb00e62f204004acb701ee2940cee4558717347e87bf559` | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_PACKAGED_SDK_PROOF_2026-08-20/STATUS_IMPLEMENTER.json` |
| `1753759244f85207eafbd89cd8c4dabf47b6b5d473e35cb690b7d640b1280045` | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_PACKAGED_SDK_PROOF_2026-08-20/STATUS_MANAGER.json` |
| `f961bb983daa314fcf06e53dab29fe9eb742195a1adf748944cf74f238f2f9b1` | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_PACKAGED_SDK_PROOF_2026-08-20/STATUS_REVIEW.json` |
| `4bab819fdb95810ea93c832c787ce9c979edb78ade72777f3b2f3c4bc608b993` | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_PACKAGED_SDK_PROOF_2026-08-20/STATUS_REVIEW_COMPLETE.json` |
| `12453e2ea60b0f48fca8e035d1a7397a0986b6a41bb8fde09d082c7ad4272427` | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_PACKAGED_SDK_PROOF_2026-08-20/WORK_GRAPH.md` |
| `f0dc042d2699e5e0942fdb47d6917d7f67b38c72321799ed5bed5bba282e0cd0` | `projects/chirality-app-dev/frontend/src/__tests__/scripts/desktop-release-workflow.test.ts` |
