# Decision Log — COV_D101_POSTSETUP_2026-09-26_1651

## Decisions

| Ref | Decision | Rationale |
|---|---|---|
| D-1 | Audit `ALL`. Sections bound by heading text with no ambiguity: `Objectives` → prefix, `## 3. Objectives (Phase 3)` line 337; `Packages` → prefix, `## 4. Packages (Phase 4)` line 376; `Deliverables` → prefix, `## 5. Deliverables (Phase 5)` line 402; `Scope Ledger` → exact, `## 6. Scope Ledger` line 542. Check 7 resolves objectives from the `ScopeLedger.csv` `ObjectiveIDs` column. The companion inventory names four authoritative registers; they are bound as machine truth, and the §2/§3/§4/§5/§7 tables are compared against them. | Contract Variant Section Binding and SOFTWARE rule; method Step 0.2. |
| D-2 | The audited basis is the working tree of worktree `pec-d101-act` at HEAD `43b60687b2f3a2176358d00e4f24a8a6ca08ba33`. The brief names `fcc1cd26b…` as HEAD. The worktree had since gained `43b60687b` (the commit adding this brief) and two uncommitted run-root files: `checks/COMMANDS.txt` (modified) and `checks/40_preflight_dispatch_V.out` (untracked). `git diff --name-only 62230fa46 HEAD` lists only run-root paths, so the product bytes are those the brief describes. Every audited product input was hashed at the start and re-hashed after emission, with the same results (`QA_Report.md` command 24). | `git log`, `git status`, `git diff`, re-hash. |
| D-3 | Create the snapshot folder with `bash tools/scaffolding/create_snapshot_folder.sh projects/pec/execution/_Evaluation/DecompCoverage COV D101_POSTSETUP` from the worktree root, as the brief requires, and use the printed path `…/COV_D101_POSTSETUP_2026-09-26_1651`. The script's shebang is `zsh`; it ran under `bash` without error. `scaffold_tool_root.sh` was skipped because the tool root exists. | Brief parameter table; contract Outputs. |
| D-4 | Number findings `COV-001…COV-078` sequentially within this run. `PrePost_Comparison.md` maps every prior ID to `CARRIED` (same severity and identical text), `CHANGED`, `RESOLVED` or `NEW`. Carried Check-6 IDs shift by −2 because the two prior Check-2 rows are resolved. | Brief; contract Issue Log Schema. |
| D-5 | `overall_status = WARNINGS`, `closure_readiness = WARN`, from the counts 0 BLOCKER / 3 WARNING. The 2 `EXPECTED_CONSEQUENCE` findings are counted in `issues_expected_consequence` only. | Method Step 13; contract Finding classification. |
| D-6 | Apply `EXPECTED_CONSEQUENCE` only to a condition whose ordinary severity is BLOCKER or WARNING and that an accepted decision explains, with that decision in `DecisionRef`. INFO observations explained by a decision stay INFO and leave `DecisionRef` empty. | Contract EC rule and schema; prior run D-6. |
| D-7 | **Attribution classes** (brief): `EXPECTED_CONSEQUENCE` rows name `D-PEC-101`. Every other row is `PRE-EXISTING`. No row is `DEFECT`. This run found no defect in the D-PEC-101 bytes: all 161 paths equal their tabled postimages; validator, closure, mirror, quote, anchor, context and reference checks all pass. The two new Check-6 INFO rows for the new folders are consequences of D-PEC-101 but INFO-grade (D-6). The per-row class is in the scratch `issue_index.json` and in `PrePost_Comparison.md`. | Brief ("Classify each finding …"). |
| D-8 | COV-077 is `EXPECTED_CONSEQUENCE` under D-PEC-101, not a Check-10 failure. `_Decomposition/_LATEST.md` says the two deliverables have "no folders yet", which is now false, and both pointers and the SCA-006 state fields call B1/B2/B3/B7 open. That would be WARNING-grade because it could mislead. D-PEC-101 expressly leaves both pointers and the SCA-006 folder unopened and puts the Lane B closeout in its run root's `HANDOFF_STATE.md`. The surfaces understate the evidence, so the contract's "no later phase or cleaner closure" test passes. The missing `HANDOFF_STATE.md` is reported to the manager; it is part of the act's records, not a product gap. | Method Step 10; D-PEC-101 Administrative grant. |
| D-9 | COV-076 (`_COORDINATION.md` Notes line) is `EXPECTED_CONSEQUENCE` citing the D-PEC-101 ruling question 4 (a). The ruling authorizes HELP_HUMAN to replace these exact lines in the act's PR after the verifier passes K1. That verdict exists (`VERIFIER_VERDICT_01.md`), but the replacement is not in the audited tree. | Ruling text; `_COORDINATION.md` hash equals the ruling's preimage. |
| D-10 | COV-075 (`remaining-loop`) stays INFO and is marked CHANGED. D-PEC-96 has since been ruled and applied, so the basis statement is stale against live `loops.json`. The basis text itself anticipates that migration "under its own ruling", and the owner carried the text knowingly at checkpoint 3 (Q-CP3-1 (a), recorded in `_Decomposition/_LATEST.md`). A reader following SOW-094 is pointed to the ruling. This is a judgement: a reviewer who reads "declares … now" as able to mislead amendment work could raise it to WARNING. No accepted decision explains the stale text as intended, so it would then be a plain WARNING, not `EXPECTED_CONSEQUENCE`. | Method Step 9 ("WARNING when it could mislead amendment work"). |
| D-11 | Record XRG-013 (26) as one Check-8 INFO row (COV-072), newly measured. The method's Check 8 reads IN rows only and passes. D-GOV-48 is a later Root rule that in-flight decompositions do not adopt retroactively. The owner defers action, and D-PEC-101 forbids action on these warnings. §7 `UnassignedScopeItems (IN without package) 0` is stated under the edition revision 1.6 adopted. Under D-GOV-48's definition it would be 26. | D-GOV-48 notice; D-PEC-101 Limits. |
| D-12 | Two tools changed bytes since the prior run. The register validator is now `869df1d5…57ee` (was `a1544dc4…`) and adds XRG-013. The closure tool is now `2b8de3cb…a9adc` (was `6305a61c…`) and reads the union of CSV rows and declared sections. Outputs remain comparable: the EXECUTION edge count is CSV-based (127 = 127 ACTIVE EXECUTION rows), and the closure summary equals the D-PEC-101 run root's. The audit method edition is unchanged. | Tool hashes; prior Decision_Log D-22. |
| D-13 | Resolve the prior COV-079, COV-084 and COV-085 to the SCA-006 checkpoint-3 acceptance, A5 and A6, not to D-PEC-101. Resolve COV-086 because SCA-005 is now historical and complete; for such a snapshot the method raises no finding, and stale-conservative content in an immutable historical snapshot is not active truth. | Method Step 10; `_ScopeChange/_LATEST.md`. |
| D-14 | COV-078 records SCA-006's missing `AdjustedAuditState` as INFO edition drift. The field entered the scope-change contract in `0d7d5da61`. SCA-006's `Brief.md` binds contract edition `4453a719…4d02`, which lacks it (verified by hashing historical editions). In-flight method bases keep their authority until transitioned. | `projects/pec/AGENTS.md` ("In-flight method bases retain their own authority"); git history. |
| D-15 | Test quote currency for ACTIVE `EXECUTION` rows by exact substring of the cited file (127/127). The 138 ACTIVE `ANCHOR` rows carry structured assertion quotes (D-PEC-62 convention) and are checked semantically against the registers (138/138 true). | Prior run D-14. |
| D-16 | `artifact_presence_pct` = 3 found / 68 declared = 4.4118; `context_fidelity_pct` over 68 matched folders. Matrix conventions as the prior run: retired `ObjectivesMapped 0/0`, otherwise `{resolvable}/{max(declared,1)}`; `IssueCount` counts rows whose `EntityID` names the deliverable explicitly. | Prior run D-16. |
| D-17 | Build `audit_structure.py`'s `--inventory` from the bound `Deliverables.csv` (68 units, all with live folders; the plan-§B1 fallback path is no longer used). `inventory.json` and `structure.json` are kept in this folder. | Contract deterministic inputs. |
| D-18 | Reuse the prior run's scratch scripts: `supp.py` and `anchorcheck.py` unchanged; `census.py` unchanged; `mkinventory.py` changed only in its docstring; `deps3.py` extended to `deps4.py` (D-PEC-101 selectors, mirror invariant, trace coverage, uniqueness). New: `refcheck.py` (covers bullets, re-pin tails), `postcheck.py` (161 postimages), `emit2.py`, `deltatable2.py`. | Comparability. |
| D-19 | Paired reads: DEL-01-03 `MEMORY.md` is byte-identical to the prior run's paired read (`44b360c5…dae6`), and its note is carried. DEL-01-06 `MEMORY.md` (new under D-PEC-96) was read in full. It holds only the header and an empty Runs table, so it adds no caveat. Whether it should carry a D-PEC-96 row is outside this audit. | Prior run paired-read practice. |
| D-20 | Do not update any `_LATEST.md`, and make no recommendation about the audit pointer or any lifecycle state. | Brief; contract. |

## Sources relied on (path and SHA-256)

Paths are repository-relative (worktree `pec-d101-act`).

### Instructions and method

| Source | SHA-256 |
|---|---|
| `AGENTS.md` | `c8ce87ef342902cb081bc659b26fc9a4edda1b6dba513814e5cb1e14e0b1dffd` |
| `projects/pec/AGENTS.md` | `df9196d152a01afe59b388111ae0a14381b4ad74f280e95f9c44a1eaee925eb8` |
| `agents/AGENT_TASK.md` | `1a13a5b00b3ce01ff8519efe6b46bcbe0cd6a5b7985e24282fa7efa2c57c8fb7` |
| `workflows/audit-decomp/WORKFLOW.md` | `7ba6291c836973a6af0aeb81d56d60ede89466c3d006673d7ef07f09b984246b` |
| `workflows/audit-decomp/resources/contract.md` | `704929c7c006a20a5fbe3fc903d4f172e2edb4c6a451c4b6db40506b40004e75` |
| `workflows/audit-decomp/resources/method.md` | `51a0c69b389d0c641f88e8faa7bebbc2b3650518eede8882436853c583308827` |
| `workflows/scope-change/resources/contract.md` (Check 10 artifact set and state fields) | `e78efea4eadfd6afede5fb9008818cb2e8a34a6a8bd1d0a976bf857e8369e264` |
| `docs/SPEC.md` (§1, §12.2 only) | `bc19361ac0cded1b88e3ce8243ff91631afbdb322139d9e8855a77a3d73ad3d1` |
| `…/REV16_CURRENCY_SETUP_D101_2026-09-26/child_briefs/T_V_AUDIT.md` (this brief) | `d9e3f4e76b72823ff0a4c464683d232a45ca979e759f3b17e3c3632662d66194` |
| `…/AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/briefs/K14A_D101_ACT.md` (parent brief; hash only) | `b253797178dfb4b117491d5d056120a23e2b2538485fa83119c5e4851961d2ec` |

### Audited decomposition package, PRD and pointers

| Source | SHA-256 |
|---|---|
| `projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md` (revision 1.6 `current_basis`) | `9374c21fb87b02e5f842af9407caf65690d73f3067f86ce6c7dba0a3a7908eb1` |
| `…/_Decomposition/ScopeLedger.csv` | `1d24a4b86f05dc6fd57028c08e202d33f9f317b148821f9c61246c6e91ee916e` |
| `…/_Decomposition/Deliverables.csv` | `94ee5d182ae99092324505a72bf2f3b0581f85c0bae6c693214cfef709179805` |
| `…/_Decomposition/ContextBudgetQA.csv` | `93b0bb075a0e83d3219e6293303c3feaa432e693e7255569d4e522ea42434c7c` |
| `…/_Decomposition/Companion_Inventory.csv` | `1597ceec7af45f33fe348d46429cc3f82042db5dbd6a083903ae04c7bf908662` |
| `projects/pec/docs/PRD.md` (v2.4) | `ae49b8065698f003001b2183f550b814cded5cd5ea06f940b81dd5c287483fbe` |
| `…/_Decomposition/_LATEST.md` (read only) | `768ae4c4286b50737d323f6c5a1c6cdcb8247f67fb65822679443bbb76eea771` |
| `…/_ScopeChange/_LATEST.md` (read only) | `7a2fd074173b2098d657286d1c9955adca632e6674e17198ffbf0f3df2586e5f` |
| `…/_Evaluation/DecompCoverage/_LATEST.md` (read only; not updated) | `f8469f88ad503ef79f436df3595cf34fd5d9ce624390fa836720227a7eda9dea` |
| `…/_Coordination/_COORDINATION.md` (Notes L225–227) | `95ebe344ee894f5f69d8b6c3067db9ecbaa4f67786afc3f7d27c920d11d8a90c` |
| `projects/pec/v2/config/loops.json` (feed profiles only) | `fd342b4f29edf3bece24a8d785b4a03d1a60158e62227753e4e1fa03529f53d7` |
| DEL-01-03 `MEMORY.md` / DEL-01-06 `MEMORY.md` (paired reads) | `44b360c57b934c585befe2cf6a0741199d4cc4ac6b8fc64c04f7be33b88bdae6` / `035ecb8686d72b18eb680531e1239ab4b2df4f5ae1b70811f6e4d667ccf30a3f` |
| Twelve K1-created files (DEL-08-06, DEL-10-13) | each equals its proposal postimage (`QA_Report.md` command 14) |

### Decisions and act records

| Source | SHA-256 |
|---|---|
| `…/_DECISIONS/D-PEC-101_rev16_currency_setup_proposal_2026-09-26.md` | `7ad176063b10b4cb3093bc9c1d5c6efbab83fcdb5e6a059e6122c466fd095a25` |
| `…/_DECISIONS/D-PEC-101_RULING_2026-09-26.md` | `baa4fc09525aaef89cdb519b934b00c90e699a2111a5c604f906fc5ed2edba28` |
| `…/_DECISIONS/_REGISTER.md` (rows D-PEC-95…101) | `9fd06376771146a326ce1dd6c6efa25c45a344f26bdff5ca0e5770b9306c7858` |
| `…/_DECISIONS/D-PEC-96_RULING_2026-09-26.md` | `852057f0ff6989e0b1180232424ff9fd8de434b3345c1d6c775e76b8defb399e` |
| `…/_DECISIONS/D-PEC-98_RULING_2026-09-26.md` (register row read; file hashed) | `039dc7e2d11db5e7e4ad46be18d2261302b37070f18737d8e794e22c08cd8361` |
| `…/_Coordination/NOTICE_2026-09-26_PACKAGE_HOME_D-GOV-48.md` | `15ea36ee295661d1832871dbbad8e9bac541ed12fcc36690ffd4f9d6ca7be8e6` |
| `…/REV16_CURRENCY_SETUP_D101_2026-09-26/VERIFIER_VERDICT_01.md` (existence and verdict line only) | `73b23f359687318b7a2a56e98c53d966dc3f72a85dce19bc8efffce6a54d005c` |
| `…/REV16_CURRENCY_SETUP_D101_2026-09-26/closure/closure_summary.json` | `7ed1553aa1cb2314ac2df1d9bde45c53e2b64d3e8a46a46e1dea3cfedbec6fdd` |
| `…/_ScopeChange/checkpoint_snapshots/SCA-006_GROUP-3_2026-09-26/DECISION.md` | `22aad7eb09958370e7bf8b3d06eff56e8bf459f9b8c56f8cbaad2c3384036bc6` |

### Active SCA-006 snapshot (`projects/pec/execution/_ScopeChange/SCA-006_2026-09-25_1912/`)

| File | SHA-256 |
|---|---|
| `Brief.md` | `205a46c04f2db6d34bead78db3064a02ff9d9d66a5e54fa9ff06b5c6314a1831` |
| `RUN_SUMMARY.md` | `6c627456471fe175f63e1070a7243301a4c92c0a9a107a7a8d39b6b8a689b92b` |
| `Handoff_State.md` | `598a92e025399a128fd1dc4a4841f0574ccea9c21fb0368e5e0488e729b61f8e` |
| `Post_Change_Coverage.json` (= prior run `coverage_summary.json`) | `b9a068c078ba6ca4daf5d6129c2823141cae787f7770068e1d70644b13a09cf0` |
| `Supersession_Map.csv` | `010ce5c423530123f923413dbfad03ce70fc0ba0c072ee7726f7718847caab92` |

### Prior run (comparison basis; `…/_Evaluation/DecompCoverage/COV_SCA006_POSTCHANGE_2026-09-26_0051/`)

| File | SHA-256 |
|---|---|
| `coverage_summary.json` | `b9a068c078ba6ca4daf5d6129c2823141cae787f7770068e1d70644b13a09cf0` |
| `Decomp_Coverage_IssueLog.csv` | `37f4f6dc730cebfec173ca965c5afe00b5c506afbec5cb67f4f1e498087026d3` |

### Tools (repository, run read-only)

| Tool | SHA-256 |
|---|---|
| `tools/scaffolding/create_snapshot_folder.sh` (run once) | `7db42ee6963dbe8306047dc5afbeb911be7fecdd92b05a239987be05c8d95640` |
| `tools/evaluation/audit_structure.py` | `d37ffbd040ace47ea990fd6fbb0911ea073358303a40ac32b3b7d7b111ecdb3f` |
| `tools/evaluation/audit_common.py` (imported) | `c610cb5b427610a9be94d59fb8ad8c050c4955c91e69525e277957351464e8c2` |
| `tools/validation/validate_decomposition_registers.py` | `869df1d5484603016e030d9e3c6619077925806b8db553da00add82dcb9157ee` |
| `tools/coordination/analyze_dep_closure.py` | `2b8de3cbd2439ba1234aadf10e07348c4e2d30dd73da66cd0d88774e417a9adc` |
| `projects/pec/execution/_Scripts/pec_reliance_hold.py` | `b1712e4b6e9f1476c577afd9170a4dd078beaa95878fa5f3b6c46a17b548cd0e` |
| `projects/pec/execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv` (header only) | `f877d9316c7da76218399838aa6b69f1bb51bbd3e59b5b1d19b31f69ad741cbc` |

Scratch script and output hashes are in `QA_Report.md` §"Scratch artifacts".
