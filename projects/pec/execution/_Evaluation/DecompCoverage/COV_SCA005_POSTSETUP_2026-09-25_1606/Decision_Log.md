# Decision Log — COV_SCA005_POSTSETUP_2026-09-25_1606

## Decisions

| Ref | Decision | Rationale |
|---|---|---|
| D-1 | Audit `ALL`. Sections are bound by heading text, and no rank was ambiguous: `Packages` → prefix match, `## 4. Packages (Phase 4)` at line 364; `Deliverables` → prefix match, `## 5. Deliverables (Phase 5)` at line 390; `Scope Ledger` → exact match, `## 6. Scope Ledger` at line 528; `Objectives` → prefix match, `## 3. Objectives (Phase 3)` at line 325. Check 7 resolves objectives from the `ScopeLedger.csv` `ObjectiveIDs` column. | Brief; the contract's Variant Section Binding and SOFTWARE rule. |
| D-2 | The audited basis is the committed tree at `995af4f36` (the D-PEC-93 act on `origin/main` `04e04da00`). The audited paths are clean against HEAD. The only other working-tree entry, `_Coordination/PROJECT_SETUP_SCA005_A4_B3_2026-09-25/checks/07_diff_check.out`, was untracked before this run started (mtime 16:04, before this folder existed at 16:06), was not written by this run, and is not an audited path. | Brief `EXPECTED_SOURCE_SNAPSHOT`; `git status` evidence in `QA_Report.md`. |
| D-3 | Create the snapshot folder only with `bash tools/scaffolding/create_snapshot_folder.sh projects/pec/execution/_Evaluation/DecompCoverage COV SCA005_POSTSETUP`, from the worktree root. The script's shebang is `#!/bin/zsh`; the brief's `bash` invocation works because it uses only POSIX parameter expansion, `date` and `mkdir -p`. Skip `scaffold_tool_root.sh`: the tool root exists. | Brief. |
| D-4 | Number findings sequentially within this run (contract Issue Log Schema), and map every prior ID to its disposition in `PrePost_Comparison.md`. From DEL-03-01 onward the Check-6 IDs coincide with the prior run's; before it they shift by 2 (the two cleared Check-2 blockers). | The contract requires `COV-{NNN}` sequential within the run. The mapping keeps the brief's prior-ID questions answerable. |
| D-5 | Set `overall_status = WARNINGS` and `closure_readiness = WARN` literally from the counts (0 / 3 / 70). The brief's expected "overall_status WARN" corresponds to the method enum value `WARNINGS` for `overall_status` and to `WARN` for `closure_readiness`. | Method Step 13 enums (`OK|WARNINGS|BLOCKERS`; `PASS|WARN|FAIL`). No severity override. |
| D-6 | Read Check 8 as folder-backed, as the prior run did (its D-6). SOW-095 and SOW-096 now resolve to existing folders, so no Check-8 finding remains. | Consistency with the prior run; method cross-reference to Check 2. |
| D-7 | Treat the retired `_CONTEXT.md` rendering `(none — retired under SCA-005)` as equal to the blank register cells. | Prior D-7; accepted A2 postimage. |
| D-8 | Keep the four retired deliverables' absent artifact sets at `INFO` (no escalation), and their Check-7 by-design rows at `INFO`. | Prior D-8 and D-9; unchanged basis. |
| D-9 | Log dependency, provenance, reference, SOW and handoff currency observations as Check-10 `DERIVATIVE_SURFACE` or `HANDOFF_STATE` `INFO` rows. None of the 12 checks owns them, and the `CheckNumber` enum admits no new value. | Prior D-10 precedent. |
| D-10 | Record the closure tool's six isolated units as one Check-10 `INFO` row (COV-071), `EXPECTED_CONSEQUENCE`. The tool labels `isolated_units` `WARNING`, but the tool is supplementary and not one of the 12 checks; the prior run likewise kept closure-tool results out of the severity count (its D-19). The hub `WARNING` (DEL-03-01, degree 25) stays in `QA_Report.md` only. | Brief ("reported as expected"); plan §C4; D-PEC-93 proposal topology. |
| D-11 | Record evidence-quote currency as a Check-10 `INFO` row (COV-072), `PRE-EXISTING`. The method assigns no severity to quote currency; `INFO` follows D-9. The 19 rows and their evidence files are byte-identical to the prior audited state, so the condition predates D-PEC-93 and is not attributed to it. | Brief (record at the method's severity, not as caused by the act); D-PEC-93 ruling Q4 (carried residual). |
| D-12 | Test quote currency only for `EXECUTION` rows by verbatim substring. The 132 ACTIVE `ANCHOR` rows carry structured assertion quotes by the D-PEC-62 convention (`PackageID PKG-xx`, `DeliverableIDs include DEL-xx-yy`), which are not meant to be verbatim spans; they were checked semantically against the registers instead (132/132 true). | A naive substring test flags all 132 anchors; that would misreport a convention as staleness. |
| D-13 | Mark prior COV-072 (the "40, not 42" count defect) `RESOLVED`. The accepted `Propagation_Plan.md` bytes still say 40 and are immutable, but every current handoff surface now carries 42: SCA-005 `RUN_SUMMARY.md` records the evidence correction (lines 201–210) and its B1 row says 42; `Handoff_State.md` and `_ScopeChange/_LATEST.md` say 42; the D-PEC-93 proposal uses 42. No surface still understates the stale population. | Method Step 10 tests handoff honesty; the correction is recorded where the method looks. |
| D-14 | Mark prior COV-073 (pointers name revision 1.4), COV-074 (SCA-004 pointer fields stale), COV-075 (SCA-005 mid-A5) and COV-076 (anticipatory `current_basis` claim) `RESOLVED`: A6 moved both pointers to revision 1.5 / SCA-005 at checkpoint-3 acceptance; the live decomposition equals `dc2b8479…9660` with `status: current_basis`; the SCA-005 snapshot holds every C5 artifact. | Observed pointer and snapshot state; group-3 `DECISION.md`. |
| D-15 | Record the post-act staleness of the SCA-005 handoff surfaces and both `_LATEST.md` pointers as one `INFO` row (COV-073), `EXPECTED_CONSEQUENCE`. They understate the state (A4 folders `NOT_CREATED`, B3 stale, `AuditState BLOCKED`), which the method allows; they claim no cleaner state. | D-PEC-93 "Administrative grant" (records not opened; closeout in the run root `HANDOFF_STATE.md`). |
| D-16 | Do not raise an issue for the SCA-005 `Handoff_State.md` C5 hash rows for `RUN_SUMMARY.md` (`e3480b78…196a`) and `Decision_Log.md` (`85676c53…4d7b`), which differ from the live bytes (`e9a0224e…e518`, `09f99fb1…a6e`). The same file's checkpoint-3 amendment paragraph states the live values, and its top hash table carries the live `Decision_Log.md` value. It is a documentary lag inside the file, not a cleaner-state claim. Disclosed in `QA_Report.md`. | Method Step 10 criteria; evidence in `QA_Report.md`. |
| D-17 | `artifact_presence_pct` = 3 found / 66 declared = 4.5455; with 66 matched folders the declared and folder bases now coincide. | Prior D-15 basis rule. |
| D-18 | Matrix `ObjectivesMapped` for retired rows is `0/0`; active rows use `{resolvable}/{max(declared,1)}`, as before. | Comparability with the prior run. |
| D-19 | Formal comparison mode (Step 12) runs against `COV_SCA005_POSTCHANGE_2026-09-25_1344`. The result is in `PrePost_Comparison.md`. | `PRIOR_RUN_LABEL` supplied. |
| D-20 | Do not update `_Evaluation/DecompCoverage/_LATEST.md`, and make no recommendation about it or about any lifecycle state. | Sealed brief; D-PEC-93 gives the pointer decision to the manager. |
| D-21 | Reuse the prior run's census script (`census.py`, prior SHA-256 `adf18d93…3425`) with only its docstring changed; its checks are basis-independent. New scratch scripts cover the dependency registers, anchor assertions and D-PEC-93 postimages. | Determinism and comparability with the prior run. |

## Sources relied on (path and SHA-256)

Paths are relative to the repository root unless marked scratch.

### Instructions and method

| Source | SHA-256 |
|---|---|
| `AGENTS.md` | `c8ce87ef342902cb081bc659b26fc9a4edda1b6dba513814e5cb1e14e0b1dffd` |
| `projects/pec/AGENTS.md` | `46689c36d5379029a34a5c5d26f109445e338fca82b86e590826bcbc39ad3846` |
| `agents/AGENT_TASK.md` | `1a13a5b00b3ce01ff8519efe6b46bcbe0cd6a5b7985e24282fa7efa2c57c8fb7` |
| `workflows/audit-decomp/WORKFLOW.md` | `4aaa7e10990ddd1b769ba09da78a03f9f491a6b6f3be6df08a1a8de93c26e3e6` |
| `workflows/audit-decomp/resources/contract.md` | `70a5abebc8ff34826415e1566715373a322baded2939325b5b73828d78401a0c` |
| `workflows/audit-decomp/resources/method.md` | `97df84022ccbec434aea9745296b93b6e549ef840acc0ca9df0a215e634d79c2` |

### Decisions and parameter source

| Source | SHA-256 |
|---|---|
| `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-93_project_setup_sca005_a4_b3_proposal_2026-09-25.md` | `46470575625522398fa47d0a39aa09d2b4d252dd89c083ba317f9e577f489422` |
| `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-93_RULING_2026-09-25.md` | `ffb0b58293d868e1d7ddf61d2958a6b18ca73fa0c36da077f5309a8782153709` |
| `projects/pec/execution/_ScopeChange/checkpoint_snapshots/SCA-005_GROUP-3_2026-09-25/DECISION.md` | `35c211a604cb7a05d3fca5cec86fe6bb297a095ad6aa7c5efa72b2cd1599f673` |
| `projects/pec/execution/_ScopeChange/checkpoint_snapshots/SCA-005_GROUP-3_2026-09-25/Handoff_State.md` | `3bc026cb9bfc877e55625d117185e2db51f48ebb209b9198f0bc4641cde66d82` |
| `projects/pec/execution/_ScopeChange/checkpoint_snapshots/SCA-005_GROUP-3_2026-09-25/ACCEPTED_MANIFEST.csv` | `1eb20bc9d9cd9b37b205e6d0e29a4392b9b6fb165f57c756e76fcf912fd13dc7` |

### Audited decomposition package and pointers

| Source | SHA-256 |
|---|---|
| `projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md` | `dc2b84791454ac888e692bfa507221f5d4a588c63bb8ab5005cc00343b119660` |
| `projects/pec/execution/_Decomposition/ScopeLedger.csv` | `83152a94d91c75da1205f98aec712f901529af4da562f02f5f1124b3ba3fd9df` |
| `projects/pec/execution/_Decomposition/Deliverables.csv` | `b8628fc4c7b32b66eae373e19eb943ccaa866125e79119172b82614a01d3d65a` |
| `projects/pec/execution/_Decomposition/ContextBudgetQA.csv` | `2a1941050d06e5e07f6cde629d0abf0c2d80acde1983139e6c1918cfca9eb0df` |
| `projects/pec/execution/_Decomposition/Companion_Inventory.csv` | `7c8a24a868ff03415c4440055dc099aaf7e2d87cca8dc0267e77d1a676976ef8` |
| `projects/pec/execution/_Decomposition/_LATEST.md` | `1f2cdcba31b3db2fd8818b16202d2bbc89c3f4a20702a962d133a73e10f556b6` |
| `projects/pec/execution/_ScopeChange/_LATEST.md` | `a2b5b789d996d52aa43c86419c9a4f02d1aa01f438f1616f3d51921e34f84268` |
| `projects/pec/execution/_Evaluation/DecompCoverage/_LATEST.md` (read only; not updated) | `0084d218b6106482dbf3f73933d44de5ed43c15b8515b48c70b098c985df7432` |
| `projects/pec/docs/PRD.md` (v2.3) | `fff27a66cd23c758cf50609ee028c58f4fb643f23ee7f6f801eb2362dfffdc32` |

### Active SCA-005 snapshot (`projects/pec/execution/_ScopeChange/SCA-005_2026-09-23_2139/`)

| File | SHA-256 |
|---|---|
| `Brief.md` | `aaf2821bb99deb4ff8b640f5e8584338ebd5fc2d95c5c00dd1e2bd136ac43d50` |
| `Impact_Assessment.md` | `0bcbe9bdced43fa887a859497b3edd197242a0eea8fa3a41fab7147b358239bf` |
| `Amendment_Preview.md` | `ad48cc5621d796a662addc03640a32f7f4cdafbf627ad6fda3f60bdede65ebe4` |
| `Propagation_Plan.md` | `50cd0b1d91ea25cc8ecba28ce649278b376fb952feec09e007a26ca5bbf91350` |
| `Amendment_Actions.csv` | `5c4ae0532eb65ea83d0529a9f6395da392ae2bf5b254cfb6b2de49e4fbff2be2` |
| `Amendment_Actions_CP2.csv` | `7bb3bada88ed20adccab6a4077d77d2d7702f03637db230d88f862dea2a09987` |
| `Supersession_Delta.csv` | `cb2a3585a7d75a76c101c30777175ea683079aab0ff74e7ce7783bb55ce89a06` |
| `Supersession_Map.csv` | `4ca705ba090cafb9a74870a0095be490c1d507149767dac32ec52879c487240c` |
| `Pre_Change_Coverage.json` | `61163c96924e6dfb1f3fa6d1449b523c7280e808c92005cc77d64096858b5d9f` |
| `Post_Change_Coverage.json` | `912610ff55e7e53788cb07c972a5a27afe5e246ecadb042932d57776cc0c4deb` |
| `PRD_V2_3_SUCCESSOR_DIFF.md` | `153a4dedb4551102ffe20c26a4dd7d4d4dba9138b28ce47f2e0889925197eba2` |
| `Decision_Log.md` | `09f99fb175c0b81c23b4f680babd04272a8e1e4126887f30582d7a072bb95a6e` |
| `Handoff_State.md` | `a86ae910d0c9ae7bf20a7ebb47de3edb345d1a6067cb1988fc04d5c1d213328a` |
| `RUN_SUMMARY.md` | `e9a0224ec0152bba75c78b84e2c9abe7a5996014eec602b46de4fe3153c1e518` |

### D-PEC-93 act evidence (read only)

| Source | SHA-256 |
|---|---|
| `projects/pec/execution/_Coordination/PROJECT_SETUP_SCA005_A4_B3_2026-09-25/gen_d93.py` | `cfae005258659c55915d0e9e2a8566399c3c84a95ede8e567205fecaea08d6c2` (equals the ruling's bound generator) |
| `projects/pec/execution/_Coordination/PROJECT_SETUP_SCA005_A4_B3_2026-09-25/closure/closure_summary.json` | `bd73806c98e82455f6abfe66aeeee38623cd24f2e48ed102bb2689934bbc187a` |
| the 31 D-PEC-93 product paths | each equal to its proposal postimage; option-A aggregate `c4525add6b621d16523ad7567410b96f1864683cf93fd0d03c3f43954a79727a` |

### Prior run (comparison basis; `projects/pec/execution/_Evaluation/DecompCoverage/COV_SCA005_POSTCHANGE_2026-09-25_1344/`)

| File | SHA-256 |
|---|---|
| `Brief.md` | `c39a0d1d3091d632800b8e50c4984d1f60af2bea3f5e75779ee4bb62e3370e8f` |
| `Decision_Log.md` | `514bec98187a30210f72026bc6cbda1ef2d0af738b97ef0af7158e616cfc61ec` |
| `Decomp_Coverage_IssueLog.csv` | `e4a9633a7df410c416826d944eb6bc4f41cd6bfb36cf248c9c5ed31aba46af5c` |
| `Decomp_Coverage_Matrix.csv` | `e80b958b9aac7c0db0e9d4155298535f9cb7192096318806baf2f9a4ae447cad` |
| `Decomp_Coverage_Report.md` | `30ba94c63d0d8bacc175229a1f1e63416d9058a99b8e7ff5d7ce61a00fdeed0c` |
| `PrePost_Comparison.md` | `a288b3285cc53fb129825e5835137748ca40e55244dc3a5c0e81fad58c820432` |
| `QA_Report.md` | `b00455b3eb21c307362d1691e84a24affbb32b570fe91cfec981fcaa9379fde9` |
| `RUN_SUMMARY.md` | `b56645edc909fda426f9aeda38de2fcb30c7aa35d83f5504cd6b5d8bdbd03b07` |
| `coverage_summary.json` | `912610ff55e7e53788cb07c972a5a27afe5e246ecadb042932d57776cc0c4deb` |

### Tools (repository, run read-only)

| Tool | SHA-256 |
|---|---|
| `tools/scaffolding/create_snapshot_folder.sh` | `2a01157959d7ac8fe55cd621c43ef61118b83370778f3f24cf54a4641fd1c361` |
| `projects/pec/execution/_Scripts/pec_reliance_hold.py` | `b1712e4b6e9f1476c577afd9170a4dd078beaa95878fa5f3b6c46a17b548cd0e` |
| `projects/pec/execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv` (header only) | `f877d9316c7da76218399838aa6b69f1bb51bbd3e59b5b1d19b31f69ad741cbc` |
| `tools/validation/validate_decomposition_registers.py` | `590d9aa368c84230533d84819c53e52b441f48904f602446ec174f68cfe08818` |
| `tools/coordination/analyze_dep_closure.py` | `fe546d0f18aac3ab44866d55d6e6ca39c2b6d323ee0355e923b01106a1698ccd` |

### Scratch scripts and outputs (session scratchpad `cov_postsetup/`, outside the repository)

| File | SHA-256 |
|---|---|
| `census.py` (prior `adf18d93…3425`, docstring changed) | `7dd1f65a95cc7499f6f3b85f1334d846cd6c12962d8243e3bb8a427d3fe01eb6` |
| `census.json` (identical under `PYTHONHASHSEED=0` and `=1`) | `046afd1f2862559d29e273f8b93faea4b299865bb7f1d2fe127b1d9964a22056` |
| `supp.py` (unchanged from the prior run) | `cb6ad2fac1a7ae451025ee59909f2357efd00b3b25f6275d824fe570cee4c674` |
| `deps2.py` (dependency registers, quote currency, mirrors) | `80f3d369a9614d71580b523afc38222b925e792506b14fedab3f8a1267ba1ef2` |
| `deps2.json` | `d5502153a27474c13a57b8e4146a656463d7d4d0d338668a40d11df98a69ad59` |
| `anchorq.py` (anchor-quote inspection) | `a14675a3bfe1b8f3b074db84587d3d2e6f1f90f8699201c2c7df6afcd996688d` |
| `anchorcheck.py` (anchor assertions vs registers) | `bd586053b93f3497480f819d96dd9ceb24ff17308a1528e27d9a7acab4abd82d` |
| `posthash.py` (D-PEC-93 postimage table) | `3ca848807cd0334c6030f769491b67d228c95b6e23fde66147e053bb2137d2a3` |
| `emit.py` (issue log, matrix, summary) | `1e870fb15fafd339faba3cc115f7d6314574b57aadcfb80aaa652eadd4b6db44` |
| `mapcheck.py` (prior-to-new ID mapping check) | `2b10a2c890a678c25532fab9b0d5ec3bbd86cbf19795a695e2171a27e1734920` |
| `deltatable.py` (per-finding delta table in `PrePost_Comparison.md`) | `877ff38180fed61de92dfcd1d2dbebb542fa5d656af6a7822eb89d9c7ca852b0` |
| `show.py` (census viewer) | `0820920a43efc7be0fbd4ea60576716f3a602e95673eafd09af19b79a28dbe60` |
| `issue_index.json` (classification and prior-ID index) | `345d901cbcb42b429a0f2cae3a74fadc20dbe3bd855b5b4f0391d4819524ff40` |
| `validator.out` | `01f2ba761dd5b30742901190c2b9a6b39504becfcf68bf760bde08e5e121210c` |
| `depclosure/closure_summary.json` (= `closure.out`) | `bd73806c98e82455f6abfe66aeeee38623cd24f2e48ed102bb2689934bbc187a` |
