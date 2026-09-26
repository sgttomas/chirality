# D-PEC-98 act — manifest

Run root `projects/pec/execution/_Coordination/SOW_INIT_D98_2026-09-26/`,
undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`, work-graph node S3, 2026-09-26.

## Actors and delegation

| Actor | Role | Mechanism | Model (host-reported) | Scope |
|---|---|---|---|---|
| Manager | WORKING_ITEMS (Type 1) under HELP_HUMAN, `Workflow: chirality-root:bundled:workflow:scope-of-work` (`MODE=INIT`, `STATUS_POLICY=NO_STATUS_TOUCH`, `DECOMP_VARIANT=SOFTWARE`, `RENDER_HTML=false`) | Claude Code subagent (`pec-manager`) launched by HELP_HUMAN | `claude-opus-5-5` (high effort per steer; instruction-asserted) | re-pin, act, verification, run-root records, return |
| Verifier | TASK (Type 2), fresh read-only `pec-reviewer`, `MODE=VERIFY` | harness-native descendant (Agent tool, `run_in_background=false`), agent id `ae6e7d06829aa10cb` | `claude-opus-5-5` | read-only; returned `VERIFIER_VERDICT_01.md` text, saved verbatim |
| Status TASK | TASK (Type 2), generic shell `pec-task`, no workflow | harness-native descendant, agent id `aefbd55f9a569717d` | `claude-opus-5-5` | write targets exactly the two `_STATUS.md`; returned `S_TASK_RETURN.md` text, saved verbatim |

Enforcement limits: role identity and write boundaries are instruction-asserted;
the host enforces only its own permissions. Children ran in the same worktree;
containment was checked afterwards with `git status` / `git diff`.

## Instruction and authority sources relied on (origin, SHA-256)

| Source | SHA-256 |
|---|---|
| Brief `S3A_D98_SOW_ACT.md` (session scratchpad `acts/`; copied to `AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/briefs/`) | `d9a013489faac17c9a9f2ef90c0f5039e061ab098d8bde0e43defc7b65486291` |
| Root `AGENTS.md` (`CLAUDE.md` imports it; `CLAUDE.md` `336cc4fb…ab49`) | `c8ce87ef342902cb081bc659b26fc9a4edda1b6dba513814e5cb1e14e0b1dffd` |
| `projects/pec/AGENTS.md` | `4400c4e97d5c9dfeda7a9a764b204ed14784c687e55e81bb04875323b6c7139c` |
| `agents/AGENT_WORKING_ITEMS.md` | `9ae4bea25bd95750a6878a9d53fbbbd7cd058d72c652a36baf4aa90601799665` |
| `_DECISIONS/D-PEC-98_RULING_2026-09-26.md` | `039dc7e2d11db5e7e4ad46be18d2261302b37070f18737d8e794e22c08cd8361` |
| `_DECISIONS/D-PEC-98_first_sows_del_02_08_02_09_proposal_2026-09-26.md` (revision 2) | `92b6f1a223f5cb6fffc399f16e5e4e63cf5d8aa8f391981d3afcb9f4027a3e40` |
| `_DECISIONS/_REGISTER.md` (row `D-PEC-98` `RULED A + S + M / EFFECTIVE ON MERGE`) | `4306bd1094204552e3f5af448f1afb5928d57d58dc52775bdfee250972b70cf4` |
| SCA-006 group-3 `ACCEPTED_MANIFEST.csv` / `DECISION.md` read for the revision-1.6 wording | `d2f24792…fe12` / read at `189f205ff` |
| `docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md` | `26c8254aaf2e2894e7d32096ec1e0d71b3ad881c1445094945031be19741433c` |
| `ACTIVE_RELIANCE_HOLDS.csv` / `execution/_Scripts/pec_reliance_hold.py` | `f877d931…41cbc` / `b1712e4b…cd0e` |

## Method files loaded

Loaded at `189f205ff` (the edition the proposal binds):
`workflows/scope-of-work/WORKFLOW.md` `d616865a5cbfa84b47fd509d2910826106db57473543a86d067ddc3edf6fbd8b`,
`resources/brief.md` `a082f1afac4eac22c0225f79191006358c6cb4508bd94f7dc2111594e8045145`,
`resources/tools.md` `2bbb55ccc68e2ab8bedfe9d2b766770b449a5119dc2cb1313cd5b5f5e3010f3f`,
`resources/checks.md` `fbb2c8ebdee578ad9ce9b36f17fadd1013f10d470142921ce18855ee174576b8`
(`execution.json` `4ad8b7eb…a26d` hashed, not needed; `representation-migration.md` not loaded).
Resolution: `workflows/index.json` (`78cbc404…2b3c` at `189f205ff`); no project
(`.chirality/workflows`) or user (`~/.chirality/workflows`) workflow of that name exists.
At `6b48b6f26` (Root PR #955) the tree carries `WORKFLOW.md` `84dadde4c573b1d3d9ecd65e1e1be12efee1a95299b4115806c02e9c9cdebc2b`,
`brief.md` `1696cd9a…92bc`, `tools.md` `fbd07771…6cc7`, `checks.md` `44ab41ac…f188`; the manager read
the diff (REVISE mode only; INIT text and items 1–21 unchanged). Tools
(unchanged throughout): `validate_scope_of_work.py` `f0f10590…fecfe`,
`derive_review_checklist.py` `bfb64dc9…0109`, `check_boundary_owner_resolution.py`
`22ef57e0…ae16a`, `common.py` `61a34722…0389`, `id_catalog.json` `7a1f8a12…757`;
`tools/scaffolding/write_status.sh` `1857ad59…97bc`.

## Commits

Base `origin/main` `6b48b6f26ed3e9ef60fde1c7d2289843bd1aea25` (cut at `189f205ff`,
fast-forwarded before the act). Commits on `claude/pec-d98-first-sows-act`: the act
(`af1a3c74b`), verification outputs (`d6feee9eb`), verifier verdict (`1e4088623`),
add-on S (`9354647df`), then the closeout records and the return.

## Run-root files (SHA-256; this file excluded)

| File | SHA-256 |
|---|---|
| `.gitattributes` | `ef9d42c8a496258d48ff8c53cbbdaa324e582ee4cd9ca3939b90f645b2fe068a` |
| `HANDOFF_STATE.md` | `3f33d44ec498c50cab0c4f0a1ac7b4d6914c72bd035ae0d226c3008c2bf3982c` |
| `REPIN.md` | `7ea1b1391d3275a4f4384a4da840e5b6e88d29e060d8ffc04523218cbd6e08c8` |
| `REPIN_WORDDIFF.txt` | `d67bc0991ddaec149d9c7b41dc61e43a7f4f15e76ea52ea556e57d06cc66ed61` |
| `S_TASK_RETURN.md` | `623dd9dae9f5431c9cfb9192d2d86966829b28d56f0ad6fe53316dc2dc7389c7` |
| `VALIDATION.md` | `e3aefa71ee0f9eec2e4756188495f713ac2234e3e63a12de85d95bcc9efc8771` |
| `VERIFIER_VERDICT_01.md` | `e1741788c3b58d67aa226368ffce5c125362acdd19689b93fdb4933f109b6561` |
| `apply_d98.py` | `0a28d05d7d285596497a98306f4327909fd3817ac8403f66a1b64f7c86d29343` |
| `boundary_DEL-02-08.json` | `c7afa8dd05e9af4276713c76be02c1d79ef88987ded77f958dda38d0359c5061` |
| `boundary_DEL-02-09.json` | `dc7beacce6bac692e7bc42d6fbbb8186b24cb22619584f18a9fe9e1381c6a0c5` |
| `candidates/projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-08_Work_graph_parser/ScopeOfWork.md` | `2319661b3225aa8c48ca4a82423e0459e806373fccb67985c4c7536a843fdd26` |
| `candidates/projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-09_MEMORY_run_index_parser/ScopeOfWork.md` | `eab18e17a41f9ca979a932cc0dc2ba4dea590340e4e3a8a404ffd5f3013b6f5e` |
| `checklist_DEL-02-08.json` | `dd05939ddda99d5030ab42dbde77c24171c0a4c20bebddc3860254645248048c` |
| `checklist_DEL-02-09.json` | `0ca3f3ad6220598cb16fe63e1b345d4fd5bc36a0afbdbe0f6c1c26d6cd4a8c2a` |
| `evidence/apply_check_only.out` | `d0e9ed81ebf8a3e566616224e65724b930bc5c9f08f9d0e030ad050b631bb97d` |
| `evidence/apply_run.out` | `c2a8e1dee9991e38e9f3488ce5ca74b8730a87032a4acc915596e646360e4a05` |
| `evidence/at_189f205ff/harness_pre.exit` | `32a83c8fb5936821c6f7a53e1060acd95a069db205a12de12935cc41ec2b0f64` |
| `evidence/at_189f205ff/harness_pre.out` | `77bd6506e73e5e5e89efd1c14824746198b6b58bf6aad9793c7ca673b02e0b63` |
| `evidence/at_189f205ff/quotes_precandidate_repin.out` | `bf81e8e5b23e7ecaea2be031429f367486112873535f358d50efc659f31962d3` |
| `evidence/at_189f205ff/receipts_pre.exit` | `038f954f7f0e857ccef59bc26e15cc90f5694b7b45c79130b730306265b62f1d` |
| `evidence/at_189f205ff/receipts_pre.out` | `7d7e12206130a6dce0ac79b5569c2d4db57e28050da022895a2c9263ea6dfeb2` |
| `evidence/at_189f205ff/reliance_dispatch.out` | `7fed374078b027e5d45c0f53f2b45718d83b184dfece26dfb16812cc021d43f5` |
| `evidence/at_189f205ff/repin_quotes.out` | `c0d05ef6cc116f1dc68987ebb96c89b7cf1e42fc4b5c48dba3b3ec5bf19fe3da` |
| `evidence/at_189f205ff/state_pre_repin.out` | `f3c48dc38ed36eaeb231f0d4a3d6392ec134a18ec947c6e7510d6129bcc00016` |
| `evidence/at_189f205ff/strict_pre.exit` | `8ec2560d0a8efbc35efc1102086cbd712fb767096823ed2ddbb20df25e7d96b6` |
| `evidence/at_189f205ff/strict_pre.out` | `8e65c4dab42895c7cac0b9344b5025897c365d960049a7e3394e9a8b1015013e` |
| `evidence/harness_pre.out` | `f07a573833127ebd157988a37e34e2fe999ea17851751339bb35c113906d4af0` |
| `evidence/post/boundary_DEL-02-08.out` | `f8cedb5811cc944c230c590c05af09a08baab64c4269df661925d10c78011782` |
| `evidence/post/boundary_DEL-02-09.out` | `8504c7219ff47ade6214e3b0a5e6310ce75a83a1029b9534d42954964cb7f606` |
| `evidence/post/checklist_DEL-02-08.out` | `e9e596662ca3be77e74642e5a3a9fa2ab097796da933a0bf6cf9ef6f73c93bd1` |
| `evidence/post/checklist_DEL-02-09.out` | `606c8bed7e1476ff89b6f8317ad6bdb1dbaa1aba4b4252ffa4affbb9023bb55f` |
| `evidence/post/checklist_repin_equivalence.out` | `9bbd7b2bbb473bfad5af28225a9a744588dfe49ec8ab2884c830fcd25767d962` |
| `evidence/post/checklist_rerun_DEL-02-08.out` | `62bc652f6b5130d6ee427f7247417c118b281a41fb9500c25dcac9efe53b94df` |
| `evidence/post/checklist_rerun_DEL-02-09.out` | `ade16f726fbde77bec0d72cfeb09fcacb7f823881ebc10efac4661051297047a` |
| `evidence/post/containment.out` | `7ffb6592df0699c83c703fc6a8e77241776ecbe1e417501385cbe748cea2a173` |
| `evidence/post/harness_post.out` | `53fed78fac98ec66960b22277eca398a5d7655e985b295e4e0c67ec05e7b2dd2` |
| `evidence/post/lifecycle.out` | `28346f6691e939e526f39e330d837c9b9336ca9bfb252935fbb391d1316ccbf6` |
| `evidence/post/qa21_hand_resolution.out` | `d070f46fa33e4385d3755b0d403104afd0dd653a20471f76870c645b6aeaeebd` |
| `evidence/post/quotes.out` | `f48238f0f5bde191871905afe9049d39b27f6eb8132fd2fd0ddfdb72998ed32a` |
| `evidence/post/receipts_post.out` | `84d324f1a0d3dc3e07f0ebbc07bc6a40194cf3f72b70861d94976605d0f9cb20` |
| `evidence/post/reliance_rely.out` | `faa427b2f1ca0f5fdd98ed545a27a1f05dd043ed8a2ebe84d18f6644d41968a5` |
| `evidence/post/state_claims.out` | `90970705bb230ae1c7711274a1da649f60d3cff0f3fd18e217a66b752d3c5f36` |
| `evidence/post/strict_post.out` | `43cdb7ce7b240d6deff710beefc9f56f230c4e61772d4fbb34eadb072523db55` |
| `evidence/post/validate_DEL-02-08.out` | `74bd290b8ba38b65a2e3f080afb541a1aa504f3114889f33d1847787d4888418` |
| `evidence/post/validate_DEL-02-09.out` | `c10f17f9182ade7e87cd5a36dc5167a1d3b76decd1bb68284f332e066a29dd50` |
| `evidence/post/validate_json_DEL-02-08.out` | `c75f050cb0c60e0425bd660b92fed23899992cad7e559f7fb9f4db7d3c127798` |
| `evidence/post/validate_json_DEL-02-09.out` | `d69521838581e2d3259eddeb1d6f7672d1fd2d9b1ada1f613be3f76a9ddb1e3b` |
| `evidence/post/whitespace.out` | `b9dbcf62e0ceaf96a2af9236ed7921ce84a1b09a99b1330096d645a26072be7b` |
| `evidence/post_S/harness_postS.out` | `e5a3e07ada1a22f153e12dc8e92fd695045d016aebec9df780eef4abecd4bff5` |
| `evidence/post_S/lifecycle_postS.out` | `84037baf55fd5cd0d00e50fdac7730f0650e458f283c1ef90c36871a7fc852f9` |
| `evidence/post_S/receipts_postS.out` | `9dd2516156a0a1621f3bf46d090ed77f347c0b39d8c6f50e865edac285ef2f0f` |
| `evidence/post_S/reliance_rely_status.out` | `40e4212df5c49db2e35acefa65de4f1a2b5377b165eeddbdd482840d3dccac09` |
| `evidence/post_S/strict_postS.out` | `5194a9412143f055e0decffdaf100387e5c09c85c85b43af20ed0386d085394d` |
| `evidence/post_S/validate_postS_DEL-02-08.out` | `ce18c0724fd5c7c180bb57d749f624a3a778dc04200c54f566682aff057443f5` |
| `evidence/post_S/validate_postS_DEL-02-09.out` | `d1f86649c66fa135c6c78ecb3a5d14a7fe6c19f4a894ff719d9996fdf18ef37e` |
| `evidence/receipts_pre.out` | `5ec75367bf915025afb31a565eb25f18ece1184f6ced90a4136a2e23c53e0309` |
| `evidence/reliance_dispatch.out` | `48e75e675c6c62e36f1999b60ecffc90c094e5b38c36c4fb68d8a7a7cdc4c423` |
| `evidence/repin_quotes.out` | `b32fff3cd4b0ae8ad209d2dd3e808ade4a1a584a2ce88611638b441ba7f7a384` |
| `evidence/repin_state_claims.out` | `a24b23d2230e0c04170ab082637f9d91cda4e9019fe750ad1fba3dc8b814c17a` |
| `evidence/strict_pre.out` | `21a7c655dab767c11a31979e743182fa21fa4cc2c07f4efce8b6a474108f59a4` |
| `evidence/test_apply_d98.out` | `f13b940f4749220f47a68386c09fa36f01d0c42b7027fe8da874311940602cc1` |
| `repin_candidates.py` | `479eb8f1d6148876aa092d0a0868092229aaaa67f2422fc18b5fbb8b8be4265b` |
| `run_d98_checks.sh` | `abc20da2d6fa8e3a590997ef6b15848449869fa23dd492ef5c41c110e9793b8d` |
| `test_apply_d98.py` | `ad7dce86b07d5c0fd36fb4ed46324b40be4d30559be2b0c18d258ffcc3e79a7a` |
| `verify_d98_quotes.py` | `9cadc2c44359c9ea2d4d20c6a95122e9be02cf221612032f0c5bf6a06cadb745` |
| `verify_d98_state_claims.py` | `65059ce21309dea7ba945db562353c7d45884e6f3bf77aad3b51b244309e835f` |
