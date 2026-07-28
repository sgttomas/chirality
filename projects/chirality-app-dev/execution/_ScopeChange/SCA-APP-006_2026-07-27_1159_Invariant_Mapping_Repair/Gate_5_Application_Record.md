# SCA-APP-006 Gate 5 Application Record

**Date:** 2026-07-27

**Accepted source basis:** `main@9fa2f82ac4b9e55873bcd7cd99ca042a4456fea2`

**Isolated checkout:** `/private/tmp/chirality-sca-app006-gate5-qLM30R`

**State:** `CLOSED_FOR_SCOPE_CHANGE_ONLY`

## Preflight

- Accepted Gate-3 artifact manifest reproduced: `PASS`.
- Accepted Gate-4 artifact manifest reproduced: `PASS`.
- Gate-4 validator against the isolated basis: `PASS`.
- All governed source paths are byte-identical between the accepted Gate-3
  basis and Gate-5 source basis: `PASS`.
- Worktree was clean at the accepted basis before application: `PASS`.

## Exact authoritative content writes

| Surface | Preimage SHA-256 | Applied SHA-256 |
|---|---|---|
| `projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | `69b3110c26cb0b435ced4144845282bf6905cde4c0474b21282b9a1806984946` | `dd6027b4bc6861aac801c8777c76606326c952b75761f8dd082e5e341f1e5c83` |
| `projects/chirality-app-dev/execution/_Decomposition/contract_invariant_coverage_register.csv` | `ABSENT` | `84d6fe0008c5ef210f8e70e583bb45251bf3170c01a5bbaea0c7bf752b88f5a1` |
| `projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-05_API_Key_UI_and_Runtime_Feedback/_CONTEXT.md` | `f2014974e133f6392c590b1149c64bd40af4b5fed28c3eb97fe8c573bce6d4e9` | `904d29af0e98a438b5e963822dd285ced684bb1fbbb0c7ebf5d45233f4579c66` |
| `projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-02_SdkOptionsBuilder_and_Settings_Isolation/_CONTEXT.md` | `b267d93e79d400aea4b3fb70d7c6786a340259ca0b3f0dde706902e9de266baf` | `305b4bf3f650508293af9c34256ea4066489f50bc8e9f1dc855918ef561c58cd` |
| `projects/chirality-app-dev/execution/PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/DEL-06-02_SDK_Read_Tool_Surface_and_Tool_Validation/_CONTEXT.md` | `1aac02d9b1c9d0f0181e99b91f6337ff8dc1e72fc4f08a48cdfb3faacf1836a0` | `055b5384dbfcbe9e195ba447b9f859dc1f06d0c8f220d78357c62721e17311d6` |
| `projects/chirality-app-dev/execution/PKG-06_Permissioned_Tools_MCP_and_Hooks/1_Working/DEL-06-03_Initial_Chirality_MCP_Read_Tools/_CONTEXT.md` | `4e21b4f477cc2ac566896d47ea43f8ef17689d970aeb0517261574b6e87b76cf` | `d084845c45a369736af9f1667d2773f2e45839ec924baf4f54945692f73e79bf` |
| `projects/chirality-app-dev/execution/PKG-07_Filesystem_Execution_Lifecycle_and_Dependencies/1_Working/DEL-07-01_Working_Root_Validation_and_Instruction_Root_Protection/_CONTEXT.md` | `a4740756db1379f79a7c1df94d41023dd82d02abbd759a0fccd8dfd760edd9c5` | `8c3a38899b3664bd7ec15e7b613ac6a0ccdbe09760c29077f135cc434ee76a87` |
| `projects/chirality-app-dev/execution/PKG-07_Filesystem_Execution_Lifecycle_and_Dependencies/1_Working/DEL-07-06_Reference_Hash_and_Snapshot_Conventions/_CONTEXT.md` | `09ae4f6686482137524862110eee46fadecc6d6b865a2d04e3661a03bd6aadc1` | `c65e22a18a345ee171c8f6df968efe072c30e59749311a2e8c6f1f42bacf5f4c` |
| `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity/_CONTEXT.md` | `25993eb5d2e86f6e168aecb8a480c533ad04719ae7c466ac261b9401e087d98d` | `1b4d01dc1c83103ac60e8b772e48ba064ffbc59435ba2ebd452fd28eae0926b3` |

## Preserved boundaries

No ScopeOfWork, contract pin, APP-HOLD-1, product/runtime implementation,
dependency, estimate, schedule, lifecycle, release, or Git action was
performed.

## Owner confirmation and closure

The owner confirmed the validated post-change state verbatim in
`Gate_5_Owner_Confirmation.md`. SCA-APP-006 is closed
`CLOSED_FOR_SCOPE_CHANGE_ONLY`. The accepted authoritative content and
post-change audit are current; CHANGE is the next owner for a separately
authorized bounded Git closeout.

## Post-change validation

- Deterministic Gate-5 state validator: `PASS`.
- Full AUDIT_DECOMP snapshot:
  `execution/_Evaluation/DecompCoverage/COV_SCA_APP_006_POSTCHANGE_2026-07-27_161852_2026-07-27_1622/`.
- Audit result: `WARNINGS` with 0 blockers, 55 warnings, and 1 information
  finding.
- Topology and coverage: 10/10 packages, 51/51 deliverables, 78 scope-ledger
  rows, 10/10 objectives, and 51/51 contexts aligned.
- Companion register: 81 unique invariant IDs across 48 families; `PASS`.
- Package shape and active SCA snapshot/handoff honesty: `PASS`.
