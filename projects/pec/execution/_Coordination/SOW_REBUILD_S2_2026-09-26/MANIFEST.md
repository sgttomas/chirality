# D-PEC-100 act — manifest

Run root `projects/pec/execution/_Coordination/SOW_REBUILD_S2_2026-09-26/`,
undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`, work-graph node S2 (the act),
2026-09-26.

## Actors and delegation

| Actor | Role | Mechanism | Model (host-reported) | Scope |
|---|---|---|---|---|
| Manager | WORKING_ITEMS (Type 1) under HELP_HUMAN, `Workflow: chirality-root:bundled:workflow:scope-of-work` (authoring discipline already applied at preparation: `MODE=INIT`, `STATUS_POLICY=NO_STATUS_TOUCH`, `DECOMP_VARIANT=SOFTWARE`; independent `MODE=VERIFY` at the act) | Claude Code subagent (`pec-manager`) launched by HELP_HUMAN; own git worktree `.claude/worktrees/pec-d100-act` on branch `claude/pec-d100-act` from fresh `origin/main` `bdae9d66b` | `claude-opus-5-5` (high effort per steer; instruction-asserted) | run root, act, verification, records, PR, return |
| Verifier | TASK (Type 2), fresh read-only `pec-reviewer`, `MODE=VERIFY` plus basis, byte identity, Part B fidelity, containment | harness-native descendant (Agent tool, `subagent_type=pec-reviewer`, `model=opus`, `run_in_background=false`), agent id `a552c84c639784606` | `claude-opus-5-5` (host-reported by the verifier) | read-only; returned the `VERIFIER_VERDICT_01.md` text, saved verbatim by the manager |

Enforcement limits: role identity and write boundaries are instruction-asserted; the
host enforces only its own permissions. The verifier ran in the manager's worktree
and reported no writes; containment was checked with `git status` / `git diff`. The
host's Write tool refused paths in this worktree (a hook binds it to the session's
original worktree), so the manager wrote run-root files with shell commands inside
its own worktree, the one the caller instructed it to create.

## Instruction and authority sources relied on (origin, SHA-256)

| Source | SHA-256 |
|---|---|
| Brief `S2A_D100_SOW_ACT.md` (session scratchpad `acts/`; copied to `AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/briefs/`) | `818d9526e089befaba48360360b2138a511c6b8ba8982586fae81148abf54e58` |
| Root `AGENTS.md` (`CLAUDE.md` imports it; `CLAUDE.md` `336cc4fb…ab49`) | `c8ce87ef342902cb081bc659b26fc9a4edda1b6dba513814e5cb1e14e0b1dffd` |
| `projects/pec/AGENTS.md` | `df9196d152a01afe59b388111ae0a14381b4ad74f280e95f9c44a1eaee925eb8` |
| `agents/AGENT_WORKING_ITEMS.md` | `9ae4bea25bd95750a6878a9d53fbbbd7cd058d72c652a36baf4aa90601799665` |
| `_DECISIONS/D-PEC-100_RULING_2026-09-26.md` | `13690e20e6ef94468045fd5b4b97110a1e4aefc09ffefbbc9746447fa86f729b` |
| `_DECISIONS/D-PEC-100_s2_sow_rebuild_proposal_2026-09-26.md` (the specification) | `39c4331e083b28e34c1a9c0913247924e7a1cb4141a270e60c7dcd04dfcee25b` |
| `_DECISIONS/_REGISTER.md` at `bdae9d66b` (row `D-PEC-100` `RULED A / B CONFIRMED / M / EFFECTIVE ON MERGE`) | `c3e8c5dea954b2f9d9355fe18518b3bfbe59a3e896eac77022e219ff80eab4ad` |
| Bound act script `PEC_SOW_REBUILD_S2_PREP_2026-09-26/apply_s2p.py` (and the run-root copy) | `42dc95532fdb39a308f59cf86e2bee73f8cf4f17808e403f42adcb308fc03d20` |
| Prep `SHA256SUMS` (source of the 28 copied files' hashes) | see `evidence/runroot_copy.sha256` |
| `D-PEC-99_REMAINING_RETIREMENT_2026-09-26/EXHIBIT_MOVED_ITEMS.md` (pinned) | `69b646f8481fe39a12b811d8078ed14a4c49622d9a8ab566d87f83683044f45e` |
| `ACTIVE_RELIANCE_HOLDS.csv` / `execution/_Scripts/pec_reliance_hold.py` | `f877d9316c7da76218399838aa6b69f1bb51bbd3e59b5b1d19b31f69ad741cbc` / `b1712e4b6e9f1476c577afd9170a4dd078beaa95878fa5f3b6c46a17b548cd0e` |
| `docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md` | `26c8254aaf2e2894e7d32096ec1e0d71b3ad881c1445094945031be19741433c` |

## Method files

Workflow `chirality-root:bundled:workflow:scope-of-work`, resolved from
`workflows/index.json` (`2bfa2c5f…fdb3`); no project (`.chirality/workflows`) or user
(`~/.chirality/workflows`) workflow of that name exists. At `bdae9d66b`:
`WORKFLOW.md` `84dadde4c573b1d3d9ecd65e1e1be12efee1a95299b4115806c02e9c9cdebc2b`,
`execution.json` `4ad8b7eb…a26d`, `resources/brief.md` `1696cd9a…92bc`,
`resources/checks.md` `44ab41ace2fb14549ef0268c357ced42e798d97b01a325d62a60226767adf188`,
`resources/tools.md` `fbd07771…6cc7`, `resources/representation-migration.md`
`698957a5…3e3c3` (hashed only). The manager did not re-author content; the verifier
loaded `WORKFLOW.md` and `checks.md` for `MODE=VERIFY`. Tools (equal to the proposal's
pins): `validate_scope_of_work.py` `f0f10590…fecfe`, `derive_review_checklist.py`
`bfb64dc9…0109`, `check_boundary_owner_resolution.py` `22ef57e0…ae16a`, `common.py`
`61a34722…0389`, `id_catalog.json` `7a1f8a12…757`.

## Commits (branch `claude/pec-d100-act`, base `bdae9d66b`)

`117215d8e` run root, bound script copy, preconditions, dispatch preflight;
`23e065e4f` the act (seven replacements, pre-act baselines, rely preflight);
`eea486f48` verification outputs; `55786c0ca` verifier verdict 01; then the run-root
records and the return. PR #979.

## Product writes (the act)

| Path (under `projects/pec/execution/`) | Preimage | Postimage |
|---|---|---|
| `PKG-01_Service_Core_Store/1_Working/DEL-01-01_Record_tier_schema_entity_model/ScopeOfWork.md` | `43f1f57a…0170` | `14be02f5fd5b2ece8e0b0588320d1ec770e497dc23d1d6b7a5768e4a55a98b88` |
| `PKG-01_Service_Core_Store/1_Working/DEL-01-06_Loop_registry_local_config_default/ScopeOfWork.md` | `5fdcfd96…2fa8` | `2053fb65abc24b75c2526a78aa4bd4b64a1e6ead11dd7ac2d5131cd736eb177e` |
| `PKG-02_File_Truth_Parsers/1_Working/DEL-02-03_Receipts_ledger_parser_per_loop_grammars/ScopeOfWork.md` | `c3e7928c…d872` | `c8bb9f1bb64d1772aff1be7ab9ef67e3e873bf708074639aa6096ec5ae7b294b` |
| `PKG-02_File_Truth_Parsers/1_Working/DEL-02-04_Run_evidence_JSON_parser/ScopeOfWork.md` | `bdb4eea0…cb87` | `18183769b8b514335921e006a6c1827ccccf7cbd5fe678522d1bffe302ed37b1` |
| `PKG-02_File_Truth_Parsers/1_Working/DEL-02-05_Dependency_register_parser/ScopeOfWork.md` | `192df47d…907e` | `0b2d571494c7e324e95ebb11e0272346a9f96cf8f4f62635c71355dee25ffd92` |
| `PKG-02_File_Truth_Parsers/1_Working/DEL-02-06_Workplan_LOOP_INIT_parser/ScopeOfWork.md` | `c8ca6292…bec8` | `53d99682795a2181b8074df41f3456d3f35c510c4257f6eb8d5b9920c7282928` |
| `PKG-02_File_Truth_Parsers/1_Working/DEL-02-07_adapter_yaml_feed_manifest_consumer/ScopeOfWork.md` | `d044499a…2559` | `3d1220872c55bc5a33b5f659cb465b83d6bd69177d48c68534c82358539f18fb` |

## Run-root files (SHA-256; this file excluded)

`.gitattributes` exempts `evidence/**` (verbatim command output) from whitespace
checks; see `VALIDATION.md` (N2).

| File | SHA-256 |
|---|---|
| `.gitattributes` | `7120788a77a314eb0e1c754325ac83ca5c9477e2d75faa6eccdbcfbaa77053e9` |
| `HANDOFF_STATE.md` | `2c664a7270fd1c14256904771fc7bb0716576379a4205583d8b7c64bc23135b5` |
| `VALIDATION.md` | `6388c13d79dbe639fa03db4c64282037f1cb4aed91717f1826db32888cfd86b0` |
| `VERIFIER_VERDICT_01.md` | `b0e6cb7d43d14c8d36d9483bef206620e9b6a5d9083178ddcf890fcee86fed8f` |
| `apply_s2p.py` | `42dc95532fdb39a308f59cf86e2bee73f8cf4f17808e403f42adcb308fc03d20` |
| `boundary_DEL-01-01.json` | `cabfc56bbc056df5f4d4d172020054faf7ee99f2a6e3591e8b4df98e9303479c` |
| `boundary_DEL-01-06.json` | `937b96d63c8e1563c091e0cb048749f11818c727e5c23541d906b2394fe2b553` |
| `boundary_DEL-02-03.json` | `606c962d12dcc513963fcd32a523492741909093a3dd5c1fcc0d7597329ceebd` |
| `boundary_DEL-02-04.json` | `fcfe942cbb2bbd68091008e647b81f9aeecc6d97ed67542758defdde30c54821` |
| `boundary_DEL-02-05.json` | `69e069d03b9fec9f8f92a45929d38178056c1c0253d6aea1e108af26f8797125` |
| `boundary_DEL-02-06.json` | `68359991eff400d2c8708b1e50ed05f77e2c51f14da8abe525ad75ec34f3b4bd` |
| `boundary_DEL-02-07.json` | `c789e72f050c1b710dd944cccec681b694009ee73943d9b2e639a2d95d5bd9a2` |
| `candidates/projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-01_Record_tier_schema_entity_model/ScopeOfWork.md` | `14be02f5fd5b2ece8e0b0588320d1ec770e497dc23d1d6b7a5768e4a55a98b88` |
| `candidates/projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-06_Loop_registry_local_config_default/ScopeOfWork.md` | `2053fb65abc24b75c2526a78aa4bd4b64a1e6ead11dd7ac2d5131cd736eb177e` |
| `candidates/projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-03_Receipts_ledger_parser_per_loop_grammars/ScopeOfWork.md` | `c8bb9f1bb64d1772aff1be7ab9ef67e3e873bf708074639aa6096ec5ae7b294b` |
| `candidates/projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-04_Run_evidence_JSON_parser/ScopeOfWork.md` | `18183769b8b514335921e006a6c1827ccccf7cbd5fe678522d1bffe302ed37b1` |
| `candidates/projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-05_Dependency_register_parser/ScopeOfWork.md` | `0b2d571494c7e324e95ebb11e0272346a9f96cf8f4f62635c71355dee25ffd92` |
| `candidates/projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-06_Workplan_LOOP_INIT_parser/ScopeOfWork.md` | `53d99682795a2181b8074df41f3456d3f35c510c4257f6eb8d5b9920c7282928` |
| `candidates/projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-07_adapter_yaml_feed_manifest_consumer/ScopeOfWork.md` | `3d1220872c55bc5a33b5f659cb465b83d6bd69177d48c68534c82358539f18fb` |
| `check_sibling_ids.py` | `e8c0f2bddbc443cd3a5e7f0c2c96c270e626c1d8e4612a061e0cf37f8e099a91` |
| `checklist_DEL-01-01.json` | `b78dbeef1f70bb22822e910a7259ccdf39d76aa1c2af374a784f1bcde28ac827` |
| `checklist_DEL-01-06.json` | `964b543533ea3166b61a80424b04adc91c03914c61d88eb0f8b964e50bcff2aa` |
| `checklist_DEL-02-03.json` | `04392472eefaf4afb72110b33b1412029bac3c5b541c4cfd5be13da2cc8d55f0` |
| `checklist_DEL-02-04.json` | `2c2324f0a58065965351f38005737778a5511a15a93f238596d3e3f73ec34854` |
| `checklist_DEL-02-05.json` | `b035ea4a324f6ec373c147fb4ddbd49be268410e114bfac42052fc2c11e74534` |
| `checklist_DEL-02-06.json` | `d989b1f33e95a47515fc52d5934e507c9d131f3a0e723707c98798c1f7228982` |
| `checklist_DEL-02-07.json` | `6c181371af560abfc99302e464100031fbc70f92dced4be5a61bdd6f7bfc548d` |
| `claims/DEL-01-01.json` | `ddbb395592b4b60f4fbb0d00bbee89a4053f3004d7ff696b2034cdec65d6d246` |
| `claims/DEL-01-06.json` | `3e260ccb30e41efb085d89e0c71d36397aefe6df47a3325680118818eb5782e9` |
| `claims/DEL-02-03.json` | `6c62f538223a31ed04b40f000ec6ecd5e3f24f9b8d6cac75c2be2f67b5f1b143` |
| `claims/DEL-02-04.json` | `109283e45b0e43364a3c323967f6f30e82422a128947c6a7b707eda725249aad` |
| `claims/DEL-02-05.json` | `4cb1e2aa0f08b98c7aa2da5bd1d6f18aa31f2ba0c86de8d1726b42556a3f78d5` |
| `claims/DEL-02-06.json` | `8e66b4419724cfa38296662cd7b420f50474f758259fbb3746856a791c4f16f6` |
| `claims/DEL-02-07.json` | `80e1141ee976bc030f485501111c6c1554eda2167da5a918f697654a7a95c7b9` |
| `evidence/apply_check_only.out` | `4a4204498477b18f012855b7a2e6c17144d4981700870cca174369d5edf889ef` |
| `evidence/apply_run.out` | `cfb568201b071460e1f4347be02d93a7babd312772fc5802a413e6cbfb82e715` |
| `evidence/harness_pre.out` | `7350fa50cf2469948efcccbebfd8bd568c3a053a9162a75ba93f199b3b46d69e` |
| `evidence/post/before_after_identity.out` | `4883aa15ba7c083dc1ef08ed3592ead387a503b666f45b06a86ee2aa087b7f16` |
| `evidence/post/boundary_DEL-01-01.out` | `49cfc3091641c156f1941706ddbd36a6c3acd02c846ced7d7338d13a5673c4ed` |
| `evidence/post/boundary_DEL-01-06.out` | `b7a61b521636e278cb7f172db7b3ae6ece52b9e7d36a08a1a9d516e8470777cc` |
| `evidence/post/boundary_DEL-02-03.out` | `83ac49ee0d6752be69e4f54ee29974ce8f6689de20797aeef16d5a5ffc7d8bf4` |
| `evidence/post/boundary_DEL-02-04.out` | `f2b611c93ba1106d7e91ff1df4648418cf838eb85336d5d0a11acf94d9a6a1e0` |
| `evidence/post/boundary_DEL-02-05.out` | `4cb17f87b5c966436624ad92e74ba6933293cffd54eac02b4564cc2846b95703` |
| `evidence/post/boundary_DEL-02-06.out` | `ae1a1df7453bcabedcf1c0285a19a9c90fbf3c193f001cf561e764e5f2ccd4b2` |
| `evidence/post/boundary_DEL-02-07.out` | `7c51d5693700f084a4b4903e38b81500cc66eb6d5019fd9a82ee13b7284e6fed` |
| `evidence/post/boundary_summary.out` | `bcfd0581af3418958f9d5e49fadaa992e88a63e275023f7df2ec2ffab22b876e` |
| `evidence/post/checklist_DEL-01-01.out` | `8c64e733e830b48e137a7a2e2ac3d447b51932e62cab2080d134b89b772aa928` |
| `evidence/post/checklist_DEL-01-06.out` | `5a1ffa241bb5121afc985bfd2e110166673a19c64798d292990ce2d77a25d15a` |
| `evidence/post/checklist_DEL-02-03.out` | `caaa678335ce5a86c5329ad335d890b60b5f24f587217471e80bc0317328566c` |
| `evidence/post/checklist_DEL-02-04.out` | `f620d06c12aa525fbbba2f664eed960e692d4f4075ff0c06dfb5a5205c5e0132` |
| `evidence/post/checklist_DEL-02-05.out` | `e12401648b1cf74d06f707978770856495117245603ef403569d209a2c6ab7c0` |
| `evidence/post/checklist_DEL-02-06.out` | `bc16c75f4ba3260363da04d72c34b18f18940cb0093720a5b3199ed61fd969e7` |
| `evidence/post/checklist_DEL-02-07.out` | `07a065b6d88f1cc13a9671b16d6a7f90172d723e947b9fc1c921f7a5afee8fd6` |
| `evidence/post/checklist_compare.out` | `629c79e8763516bf417cd7af5a48321ab9f3f02a58bbcf131ed7c10e8304259f` |
| `evidence/post/checklist_rerun_DEL-01-01.json` | `b78dbeef1f70bb22822e910a7259ccdf39d76aa1c2af374a784f1bcde28ac827` |
| `evidence/post/checklist_rerun_DEL-01-01.out` | `d652cfeef382eb20fc110db41f514e43dcd1dc551158174a2b57e61fc06aec21` |
| `evidence/post/checklist_rerun_DEL-01-06.json` | `964b543533ea3166b61a80424b04adc91c03914c61d88eb0f8b964e50bcff2aa` |
| `evidence/post/checklist_rerun_DEL-01-06.out` | `d8edc28666be967659a6fc23ff0ed6fa574a545b537d0f866694085e6a4a2fec` |
| `evidence/post/checklist_rerun_DEL-02-03.json` | `04392472eefaf4afb72110b33b1412029bac3c5b541c4cfd5be13da2cc8d55f0` |
| `evidence/post/checklist_rerun_DEL-02-03.out` | `28b4b2e769cfd12dde623e2c96d6b20fd8ac15ad54b402495cd9653b12d51d1a` |
| `evidence/post/checklist_rerun_DEL-02-04.json` | `2c2324f0a58065965351f38005737778a5511a15a93f238596d3e3f73ec34854` |
| `evidence/post/checklist_rerun_DEL-02-04.out` | `f7d2477f4232de71d3d64b8ea14fc297c77694625651a99215d7ecf9811fb33f` |
| `evidence/post/checklist_rerun_DEL-02-05.json` | `b035ea4a324f6ec373c147fb4ddbd49be268410e114bfac42052fc2c11e74534` |
| `evidence/post/checklist_rerun_DEL-02-05.out` | `fcd6dc856fdcf06d2eaecb0812d5265f5f82a8cf2f49be16659a3e6e449699df` |
| `evidence/post/checklist_rerun_DEL-02-06.json` | `d989b1f33e95a47515fc52d5934e507c9d131f3a0e723707c98798c1f7228982` |
| `evidence/post/checklist_rerun_DEL-02-06.out` | `584927afbca625aba47fba34790fe448f8af0529ff79d7b8594c1ef92438642a` |
| `evidence/post/checklist_rerun_DEL-02-07.json` | `6c181371af560abfc99302e464100031fbc70f92dced4be5a61bdd6f7bfc548d` |
| `evidence/post/checklist_rerun_DEL-02-07.out` | `65b9d0defef61074d559df5dc3cc5a17c5357bbdee23d4a70f2de721f2ea5d98` |
| `evidence/post/containment.out` | `a6ec4d386a98c3bff77bf5972a75271b36c346b2ed51b25b2532d719fde3822d` |
| `evidence/post/harness_post.out` | `7350fa50cf2469948efcccbebfd8bd568c3a053a9162a75ba93f199b3b46d69e` |
| `evidence/post/lifecycle.out` | `54350ca4209130569674d96fd85cb415d59b06e935b6c479af920d55bc2eebcc` |
| `evidence/post/qa21_hand_resolution.out` | `cae9575715bc802a4e795908d425214d837f23b00b21ef6506a9c70307ea4073` |
| `evidence/post/quotes.out` | `a9f593929441b263b8427f32db598853ba941dfb19894c8ae38decd4d3aa9056` |
| `evidence/post/receipts_post.out` | `cc7bd5297782fd9b24f67e0384073fa4d907404c9b7f3914ebb5bfd5db63b80e` |
| `evidence/post/scan_external_quotes.out` | `b0c21f2107e375fb8278c6640bc737aa81c14b851f5ad89cedf476d947431b03` |
| `evidence/post/sibling_ids.out` | `630c7dacde191a607808e98927b2922c0bffda22fe5bb5784c9334c09451d82f` |
| `evidence/post/state_claims.out` | `2248867cb623a25797d07724ea035679f54edb5895989db965cae709f19405b4` |
| `evidence/post/strict_post.out` | `9d8648e3b23d9189ca0c518cafba644224e81df5211654c5b3c6e0b34ad61890` |
| `evidence/post/validate_DEL-01-01.out` | `adb10153e33d5ba559ac651312abacf4d3159ef7b9c3a6b0204ca82c7cd91e59` |
| `evidence/post/validate_DEL-01-06.out` | `5686ef173c2ff52bf78fb8817bcb4ea6ec66cef37f34f617f712eb15a7cdffcc` |
| `evidence/post/validate_DEL-02-03.out` | `81582f2426bed6e6d643010abfc4ee884860693a861c0a2697f9acda80e0474e` |
| `evidence/post/validate_DEL-02-04.out` | `072fe53765ea1048b80c7bcc21a5a447e4cff936de54f8d664573d6276e25ec7` |
| `evidence/post/validate_DEL-02-05.out` | `cb836508c16554657bc2576b51db3a2428ed39bea9c59dffe781785dab64ab49` |
| `evidence/post/validate_DEL-02-06.out` | `07d163aba3134047b15dcd2fa6cf88938d888d2f94615f17e30a259549b038ca` |
| `evidence/post/validate_DEL-02-07.out` | `41b49836a3898b68b412cb46a7a54566c23f50c392c804de21020844e986940c` |
| `evidence/post/whitespace.out` | `7b85953a6e1ed71d3374e5e6b81af1fb73ac79b210e63d2bf93c5b0bf48ee86c` |
| `evidence/preconditions.out` | `d187b0bd80cc534bb68ae408908a47e3a2aa1aaf061a26a28ff57cc0ff6cb88c` |
| `evidence/receipts_pre.out` | `cc7bd5297782fd9b24f67e0384073fa4d907404c9b7f3914ebb5bfd5db63b80e` |
| `evidence/reliance_dispatch.out` | `9e86925605568fa279e15864772d5e3764f67e01637dd4538d2c8cf2d51d6898` |
| `evidence/reliance_rely.out` | `bf8840203c73da92de959fd8ef2d8ab5eea27650dc0519484bc06115ba4c7f71` |
| `evidence/rerun_bdae9d66b/SUMMARY.out` | `fb0b69ab39f97507af47e3b69101a9088e25f6f521c9641de0e40760f5a251d3` |
| `evidence/rerun_bdae9d66b/apply.out` | `aac43a2f50d8bd147166a00747cb1863c5e7b286f6848da4d0c39552e4be4bf6` |
| `evidence/rerun_bdae9d66b/apply_checkonly.out` | `6b6b4e8de96d984ce97ce1a2c96ce38111ec2e794a1f0061ece8dbaa5a5ee22d` |
| `evidence/rerun_bdae9d66b/apply_rerun.out` | `f95b67146606f4ab827ff388ce2530a02ac525303d187d62a9c40014ae80b012` |
| `evidence/rerun_bdae9d66b/boundary_DEL-01-01.json` | `cabfc56bbc056df5f4d4d172020054faf7ee99f2a6e3591e8b4df98e9303479c` |
| `evidence/rerun_bdae9d66b/boundary_DEL-01-01.out` | `7c5d2476d933ec16818c66c3e9c6c7faf6acfd04d1b1cf6732615357fad70df1` |
| `evidence/rerun_bdae9d66b/boundary_DEL-01-06.json` | `937b96d63c8e1563c091e0cb048749f11818c727e5c23541d906b2394fe2b553` |
| `evidence/rerun_bdae9d66b/boundary_DEL-01-06.out` | `ac5003792ed9e6c5447b261f995068fd684d5f62047e2231ce2086ece376ed68` |
| `evidence/rerun_bdae9d66b/boundary_DEL-02-03.json` | `606c962d12dcc513963fcd32a523492741909093a3dd5c1fcc0d7597329ceebd` |
| `evidence/rerun_bdae9d66b/boundary_DEL-02-03.out` | `ac5003792ed9e6c5447b261f995068fd684d5f62047e2231ce2086ece376ed68` |
| `evidence/rerun_bdae9d66b/boundary_DEL-02-04.json` | `fcfe942cbb2bbd68091008e647b81f9aeecc6d97ed67542758defdde30c54821` |
| `evidence/rerun_bdae9d66b/boundary_DEL-02-04.out` | `ac5003792ed9e6c5447b261f995068fd684d5f62047e2231ce2086ece376ed68` |
| `evidence/rerun_bdae9d66b/boundary_DEL-02-05.json` | `69e069d03b9fec9f8f92a45929d38178056c1c0253d6aea1e108af26f8797125` |
| `evidence/rerun_bdae9d66b/boundary_DEL-02-05.out` | `ac5003792ed9e6c5447b261f995068fd684d5f62047e2231ce2086ece376ed68` |
| `evidence/rerun_bdae9d66b/boundary_DEL-02-06.json` | `68359991eff400d2c8708b1e50ed05f77e2c51f14da8abe525ad75ec34f3b4bd` |
| `evidence/rerun_bdae9d66b/boundary_DEL-02-06.out` | `b05ac54a0bcf789687436e98145c87ca2c58536946c885974d01d37c3d5c442a` |
| `evidence/rerun_bdae9d66b/boundary_DEL-02-07.json` | `c789e72f050c1b710dd944cccec681b694009ee73943d9b2e639a2d95d5bd9a2` |
| `evidence/rerun_bdae9d66b/boundary_DEL-02-07.out` | `a94aaa055c40d8982e5dee6867e3e3333f0ec406c99dc00945aa75c1e4613b9b` |
| `evidence/rerun_bdae9d66b/check_sibling_ids.out` | `4b3140902da4e9465c1fbe0a58b62f2407833c603482b6cfa9b1c85d5ed06fa8` |
| `evidence/rerun_bdae9d66b/checklist_DEL-01-01.json` | `b78dbeef1f70bb22822e910a7259ccdf39d76aa1c2af374a784f1bcde28ac827` |
| `evidence/rerun_bdae9d66b/checklist_DEL-01-01.out` | `19eaf43821a7660ec323a87c8457bf74823beb296c39f5e01aa8a683aa50f061` |
| `evidence/rerun_bdae9d66b/checklist_DEL-01-06.json` | `964b543533ea3166b61a80424b04adc91c03914c61d88eb0f8b964e50bcff2aa` |
| `evidence/rerun_bdae9d66b/checklist_DEL-01-06.out` | `19eaf43821a7660ec323a87c8457bf74823beb296c39f5e01aa8a683aa50f061` |
| `evidence/rerun_bdae9d66b/checklist_DEL-02-03.json` | `04392472eefaf4afb72110b33b1412029bac3c5b541c4cfd5be13da2cc8d55f0` |
| `evidence/rerun_bdae9d66b/checklist_DEL-02-03.out` | `19eaf43821a7660ec323a87c8457bf74823beb296c39f5e01aa8a683aa50f061` |
| `evidence/rerun_bdae9d66b/checklist_DEL-02-04.json` | `2c2324f0a58065965351f38005737778a5511a15a93f238596d3e3f73ec34854` |
| `evidence/rerun_bdae9d66b/checklist_DEL-02-04.out` | `19eaf43821a7660ec323a87c8457bf74823beb296c39f5e01aa8a683aa50f061` |
| `evidence/rerun_bdae9d66b/checklist_DEL-02-05.json` | `b035ea4a324f6ec373c147fb4ddbd49be268410e114bfac42052fc2c11e74534` |
| `evidence/rerun_bdae9d66b/checklist_DEL-02-05.out` | `19eaf43821a7660ec323a87c8457bf74823beb296c39f5e01aa8a683aa50f061` |
| `evidence/rerun_bdae9d66b/checklist_DEL-02-06.json` | `d989b1f33e95a47515fc52d5934e507c9d131f3a0e723707c98798c1f7228982` |
| `evidence/rerun_bdae9d66b/checklist_DEL-02-06.out` | `19eaf43821a7660ec323a87c8457bf74823beb296c39f5e01aa8a683aa50f061` |
| `evidence/rerun_bdae9d66b/checklist_DEL-02-07.json` | `6c181371af560abfc99302e464100031fbc70f92dced4be5a61bdd6f7bfc548d` |
| `evidence/rerun_bdae9d66b/checklist_DEL-02-07.out` | `19eaf43821a7660ec323a87c8457bf74823beb296c39f5e01aa8a683aa50f061` |
| `evidence/rerun_bdae9d66b/containment.out` | `06ff3c9e815256a291c6aa2bb5b674c925bb98afa8e9a2efb678cfe25aac5c0f` |
| `evidence/rerun_bdae9d66b/harness_post.out` | `7350fa50cf2469948efcccbebfd8bd568c3a053a9162a75ba93f199b3b46d69e` |
| `evidence/rerun_bdae9d66b/harness_pre.out` | `7350fa50cf2469948efcccbebfd8bd568c3a053a9162a75ba93f199b3b46d69e` |
| `evidence/rerun_bdae9d66b/receipts_post.out` | `d707cee0741011b22b5b28b755aa420bc808cc00b856c3c60ea7ad541ecc41ea` |
| `evidence/rerun_bdae9d66b/receipts_pre.out` | `db60699cacf92a1119be5dba0e2f93c2a80c59b17b91d86ef530581b609ad58f` |
| `evidence/rerun_bdae9d66b/scan_external_quotes.out` | `ef67b22d67d2aacd18646cf27bf8494ee2e15a0a2ae050942cf3f35c5f24cfdf` |
| `evidence/rerun_bdae9d66b/strict_post.out` | `9d8648e3b23d9189ca0c518cafba644224e81df5211654c5b3c6e0b34ad61890` |
| `evidence/rerun_bdae9d66b/strict_pre.out` | `9d8648e3b23d9189ca0c518cafba644224e81df5211654c5b3c6e0b34ad61890` |
| `evidence/rerun_bdae9d66b/test_apply_s2p.out` | `2a1aba9ee8a7b1558fde630341efca981d0d1ef7f2ed62e8e1408647a35019ca` |
| `evidence/rerun_bdae9d66b/validate_DEL-01-01.out` | `710a79f5bc8a8d3041928a3a4512502d20780fcb44a55bb470beecc8664e01d5` |
| `evidence/rerun_bdae9d66b/validate_DEL-01-06.out` | `55352be04f6b66c65764b6114dfaf6689df191c3a24e5006c4de9602b575fca5` |
| `evidence/rerun_bdae9d66b/validate_DEL-02-03.out` | `ecbff50b99d01145c95df55ae52e1b05abf374b10659fa6d35956a9d715fbaeb` |
| `evidence/rerun_bdae9d66b/validate_DEL-02-04.out` | `19e5a94891f72d438a4a3de3bb68ca538c18519094dce656c43d2152fa7c38ec` |
| `evidence/rerun_bdae9d66b/validate_DEL-02-05.out` | `69dc9771ac32914a9d66aac7d8f65e921ec7266f7df14eb70fc2ecd65ef8d9d0` |
| `evidence/rerun_bdae9d66b/validate_DEL-02-06.out` | `8cc54c402ba04d48bb017174c3c4d7c6d8b4ed78c5cb14cc73e184a40541091b` |
| `evidence/rerun_bdae9d66b/validate_DEL-02-07.out` | `588d4ba671ae26e8e8daef0034487fb6639171a75e667772b47b6ebd53a29b59` |
| `evidence/rerun_bdae9d66b/verify_quotes.out` | `fec4367f2a0a459d3f27c7d962336878b68b5c6fc572e1c76358740ad7bba230` |
| `evidence/rerun_bdae9d66b/verify_state_claims.out` | `9be3c4105ae46cc2dba9aa67c0bb211e4b5df0a62f36c17538c53ae155b67c65` |
| `evidence/rerun_bdae9d66b/whitespace.out` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `evidence/runroot_copy.sha256` | `4990ec8db6f9c05fa446d56e74462b2b3f54b779119b87e86bd1c8c3d68e5e74` |
| `evidence/runroot_copy_check.out` | `41b39d4adfc495153c03cd3e9d68c0a941f4838d618f9cee28d9d218822dea64` |
| `evidence/strict_pre.out` | `9d8648e3b23d9189ca0c518cafba644224e81df5211654c5b3c6e0b34ad61890` |
| `qa21_hand_resolution.py` | `4c7549918a25e4e5db4f7b79cdbdd4c2888092a7459f2d1895120d49cec1e11f` |
| `quotes/DEL-01-01.json` | `09fc921c778f18131d65e2e7a5f53a881a400cccd10649557ac9f34d5a10fe67` |
| `quotes/DEL-01-06.json` | `024ebef1aa76f961da3e473a2dce70de1d081674a1187a68599757d68fe301bc` |
| `quotes/DEL-02-03.json` | `5e01475e37e2e8478cb9b9ba340f224a2def01df6ce569c8a51ca1fe7a9d2c9c` |
| `quotes/DEL-02-04.json` | `de5e414b289bed94bc9fbcd64e0fa5855f282b1522961ec6aa91833e2e314d5b` |
| `quotes/DEL-02-05.json` | `e844696567cccacfcbb1717ae37d9cc87b2b81ac738516a5182cdbb092f841c0` |
| `quotes/DEL-02-06.json` | `807606b4e146b344f1305fbe1fd68511777866ac3b86cd9b578d73da9d77a81d` |
| `quotes/DEL-02-07.json` | `e3c7d46ae340e2756dfe817d8406a58c8d8cc3edcfe1ef2b23c086639b6c6ac1` |
| `run_s2p_checks.sh` | `6b2845d91b53de8089c1986b3e72cffbac064ff418c908fb4d24939289a5b8e7` |
| `scan_external_quotes.py` | `e11fa9ada53490a23e66da4374d8a38b29a90f8ee0904d77ea5355c9584e94b8` |
| `test_apply_s2p.py` | `d8f2b4220fea24a4252d708f7be16482d285fbcc65cdf8f83dfa9861943ec61c` |
| `verify_s2p_quotes.py` | `be74a06c74457256e12f0573837f8d35e41ee276d76b2e0dc660c376598854af` |
| `verify_s2p_state_claims.py` | `eb85c15f24ed79b9234a2ab3dd746bbaaa499ea7566bd99efa2e061d87dd8545` |
