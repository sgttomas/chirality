# Decision Log — COV_SCA006_POSTCHANGE_2026-09-26_0051

## Decisions

| Ref | Decision | Rationale |
|---|---|---|
| D-1 | Audit `ALL`. Sections bound by heading text with no ambiguity: `Objectives` → prefix, `## 3. Objectives (Phase 3)` line 337; `Packages` → prefix, `## 4. Packages (Phase 4)` line 376; `Deliverables` → prefix, `## 5. Deliverables (Phase 5)` line 402; `Scope Ledger` → exact, `## 6. Scope Ledger` line 542. Check 7 resolves objectives from the `ScopeLedger.csv` `ObjectiveIDs` column. The companion inventory names four authoritative registers; they are bound as machine truth and the §3/§4/§5/§7 tables are compared against them. | Contract Variant Section Binding and SOFTWARE rule; method Step 0.2. |
| D-2 | The audited basis is the committed tree at `5e0169f5e` (branch `claude/pec-sca006-cp3-execution`). The manager committed `5e0169f5e` (A5 `Supersession_Map.csv`, C3 evidence) during this run; HEAD was `39a9768c8` when this run started. That commit touched only `_ScopeChange/SCA-006_2026-09-25_1912/Supersession_Map.csv` and `CP3_EVIDENCE/c3_*`; no audited decomposition, register, PRD, `_CONTEXT.md`, `_REFERENCES.md`, `_STATUS.md`, SOW or `Dependencies.csv` changed. Every audited input was re-hashed after the outputs were emitted and equals the values recorded here (`QA_Report.md` command 24). The only working-tree entry is this folder. | `git log`, `git status`, re-hash. |
| D-3 | Create the folder with `mkdir` under the exact name the brief fixes (`…_2026-09-26_0051`, the dispatch minute). `tools/scaffolding/create_snapshot_folder.sh` does only `mkdir -p` of `{PREFIX}_{LABEL}_{date +%Y-%m-%d_%H%M}`; run at 00:57 it would have produced a different name than the brief's. `scaffold_tool_root.sh` skipped: the tool root exists. The folder did not exist before (verified). | Brief output path; script read in full. |
| D-4 | Number findings `COV-001…COV-086` sequentially within this run; map every baseline ID to its disposition and new ID in `PrePost_Comparison.md`. Carried Check-6 IDs shift by +4 (two new Check-1 rows and two new Check-2 rows precede them). | Contract Issue Log Schema. |
| D-5 | `overall_status = WARNINGS`, `closure_readiness = WARN`, from the counts 0 BLOCKER / 3 WARNING. The 12 `EXPECTED_CONSEQUENCE` findings are counted in `issues_expected_consequence` only. | Method Step 13 enums; contract Finding classification. |
| D-6 | Apply `EXPECTED_CONSEQUENCE` only to a condition whose ordinary severity is BLOCKER or WARNING and that an accepted decision explains, with that decision in `DecisionRef`. An INFO observation explained by a decision stays INFO, names the decision in its description, and leaves `DecisionRef` empty (schema: "empty otherwise"). Consequently the baseline's INFO rows tagged `[EXPECTED_CONSEQUENCE]` (DEL-02-08/09 artifacts, retired Check-7 rows, closure-tool isolated units) remain INFO here. | Contract: EC "marks a condition that would otherwise be a BLOCKER or WARNING"; Issue Log Schema. Methodology change from the baseline, whose edition had no EC severity and used description tags. |
| D-7 | Ordinary severities for the SCA-006 derivative-currency conditions under the current method's Step 9 rule ("INFO severity (WARNING when it could mislead amendment work)"): the two stale EvidenceQuotes (evidence a dependency reader relies on is not verbatim), the 63 context provenance blocks and 66 reference packets (they name revision 1.5 as `current_basis` and PRD v2.3 as the source corpus; against the audited candidate poststate that directs readers to superseded sources, which plan §B4 forbids quoting), the three anticipatory A2 provenance tails (they claim revision 1.6 `current_basis` before acceptance) and the dependency registers' missing traces for SOW-097..100 are each WARNING-grade and therefore `EXPECTED_CONSEQUENCE` under `D-PEC-97`. Pre-acceptance, the revision-1.5 statements are literally true of the accepted basis; this is stated in each row. | Current method Step 9; contract EC rule; brief item 2. |
| D-8 | Keep INFO for: SOW currency (COV-081; byte state only, SOW text not audited, baseline severity); the SCA-005 handoff residual (COV-086; a historical snapshot explicitly superseded for current state by `_COORDINATION.md` item 14 and the pointers, and it claims less closure than the evidence, which Check 10 allows); the `remaining-loop` observation (COV-083; no accepted decision has changed the basis). | Method Step 10 criteria; D-6. |
| D-9 | The brief permits, but does not require, `EXPECTED_CONSEQUENCE` with `DecisionRef = D-PEC-95` for conditions explained by D-PEC-95's accepted state. Not used: the resolved baseline findings (COV-068/069/072 and the pointer part of COV-073) produce no row, and the one residual D-PEC-95 explains (COV-086) is INFO-grade, below the EC threshold (D-6). `D-PEC-95` is cited in COV-086's description, in `coverage_summary.json` `baseline_dispositions`, and in `PrePost_Comparison.md`. | Contract EC threshold; brief item 1 ("you may"). |
| D-10 | Read Check 8 as folder-backed, as the prior runs did (baseline D-6; POSTCHANGE COV-070/071): SOW-099 and SOW-100 resolve at declaration level but not to folders, so each is a WARNING-grade finding and `EXPECTED_CONSEQUENCE` under plan §B1. | Consistency with the prior runs. |
| D-11 | Record OBJ-001's two folderless supporters as one Check-7 INFO row (COV-068). The method has no condition for partial folder backing; the zero-support WARNING does not fire. | Prior POSTCHANGE COV-068/069 precedent. |
| D-12 | Place derivative-currency and dependency-topology observations under Check 9 (`EntityType=DERIVATIVE_SURFACE`), as the current method directs for observations no check owns. The baseline placed them under Check 10 (its D-9). Snapshot and handoff findings stay under Check 10. Check 9's verdict stays `SKIPPED` (not variant-owned). | Current method Step 9 "Other derivative-currency observations". Methodology change. |
| D-13 | Run `tools/evaluation/audit_structure.py` with `--inventory` built from the bound `Deliverables.csv` (68 units). Existing units use their live folders; DEL-08-06 and DEL-10-13 use the expected folder paths plan §B1 records, so the tool reports them as declared-but-missing. Both `inventory.json` and `structure.json` are kept in this folder. The tool's two workspace-level issues (package folders lack `0_References/`, `2_Checking/`, `3_Issued/`; tool roots `_Aggregation/`, `_Estimates/`, `_Sources/` absent) are recorded as Check-1 INFO rows: pre-existing, first measured because this method edition requires the tool, and docs/SPEC.md §12.2 makes those subfolders SHOULD. Its per-unit result for the 34 no-contract folders (`production_format` state `INVALID` with no issue raised, because they are `OPEN` or `RETIRED` with no production) equals the census's `NONE`. | Contract deterministic inputs; method Step 0.5. |
| D-14 | Test quote currency for ACTIVE `EXECUTION` rows by exact substring of the cited file. The 132 ACTIVE `ANCHOR` rows carry structured assertion quotes (D-PEC-62 convention) and are checked semantically against the registers instead (132/132 true). | Baseline D-12. |
| D-15 | Treat the retired `_CONTEXT.md` rendering `(none — retired under SCA-005)` as equal to the blank register cells; keep retired artifact absences at INFO without escalation. | Baseline D-7, D-8. |
| D-16 | `artifact_presence_pct` = 3 found / 68 declared = 4.4118 (66 matched folders); `context_fidelity_pct` over the 66 matched folders. Matrix `ObjectivesMapped`: retired `0/0`, otherwise `{resolvable}/{max(declared,1)}`; folderless rows are `FolderExists=False`, `ContextMatch=MISSING`, `ArtifactCoverage=0/1`, `LifecycleState=UNKNOWN`. `IssueCount` counts issue rows whose `EntityID` names the deliverable explicitly (bulk `DEL-*` rows are not counted per deliverable). | Baseline D-17, D-18; prior POSTCHANGE matrix; baseline matrix counts. |
| D-17 | Record the plan-§B2 anchor gap (COV-080) as `EXPECTED_CONSEQUENCE` although the brief's expected list names only B1, B3 and B7: the workflow directs classifying findings explained by an accepted decision as `EXPECTED_CONSEQUENCE`, and accepted plan §B2 lists exactly these TRACES rows (A-24, A-25, A-30, A-32) as open dependency-extract work. It is flagged to the manager. | WORKFLOW.md step 3; plan §B2. |
| D-18 | Record the pre-acceptance pointers and front matter (COV-084) and the mid-A5 candidate snapshot (COV-085) as `EXPECTED_CONSEQUENCE` under `D-PEC-97` plan §A6 / §A1 and §A5 / §C5: each would be WARNING-grade (a pointer's basis-integrity hashes no longer equal the working surface; an incomplete snapshot), and the plan designs both states. | Brief item 2 (last bullet); prior POSTCHANGE COV-073/075 precedent. |
| D-19 | Do not raise the difference between the live decomposition (`3ef0412a…9b29`) and the accepted CP2 candidate (`4eed1247…2d62`). `diff` shows only front-matter lines 5, 7 and 8, the §7 revision date and the DL-21 date: the pre-acceptance lines and acceptance-date slots the plan's hash rule covers. The four registers and the PRD are byte-identical to their candidates. Exact slot verification is the manager's C1/C3. | `QA_Report.md` command 17. |
| D-20 | Do not update any `_LATEST.md`, and make no recommendation about the audit pointer or any lifecycle state. | Brief; contract "Pointer moves belong to the manager". |
| D-21 | Reuse the baseline's scratch scripts where basis-independent: `supp.py` and `anchorcheck.py` unchanged; `census.py` adapted only to make provenance and reference buckets revision-agnostic and to capture PRD versions and `current_basis` claims; `deps2.py` adapted to `deps3.py` (D-PEC-93-specific selectors replaced; baseline-19, B3 and SOW-cited row probes added). New: `mkinventory.py`, `emit.py`, `deltatable.py`, viewers. | Determinism and comparability. |
| D-22 | The register validator (`590d9aa3…` → `a1544dc4…`) and closure tool (`fe546d0f…` → `6305a61c…`) changed bytes since the baseline. Their outputs remain comparable: the closure summary is byte-identical to the baseline's, and the validator reports the same families and denominators plus the two expected DRB-008 rows. | Tool hashes in the source table. |

## Sources relied on (path and SHA-256)

Paths are repository-relative unless marked scratch.

### Instructions and method

| Source | SHA-256 |
|---|---|
| `AGENTS.md` | `c8ce87ef342902cb081bc659b26fc9a4edda1b6dba513814e5cb1e14e0b1dffd` |
| `projects/pec/AGENTS.md` | `4400c4e97d5c9dfeda7a9a764b204ed14784c687e55e81bb04875323b6c7139c` |
| `agents/AGENT_TASK.md` | `1a13a5b00b3ce01ff8519efe6b46bcbe0cd6a5b7985e24282fa7efa2c57c8fb7` |
| `workflows/audit-decomp/WORKFLOW.md` | `7ba6291c836973a6af0aeb81d56d60ede89466c3d006673d7ef07f09b984246b` |
| `workflows/audit-decomp/resources/contract.md` | `704929c7c006a20a5fbe3fc903d4f172e2edb4c6a451c4b6db40506b40004e75` |
| `workflows/audit-decomp/resources/method.md` | `51a0c69b389d0c641f88e8faa7bebbc2b3650518eede8882436853c583308827` |
| `docs/SPEC.md` (§1, §12.2 only) | `5900b4dedb84dfe1a3c51abc350c3bfd57e7b61554d73ce675cebdf42e3c99ba` |

### Audited decomposition package, PRD and pointers

| Source | SHA-256 |
|---|---|
| `projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md` (revision 1.6, pre-acceptance) | `3ef0412a99812885e247bc4e9726fe005ce3446372f609c47274b6ad25b29b59` |
| `projects/pec/execution/_Decomposition/ScopeLedger.csv` | `1d24a4b86f05dc6fd57028c08e202d33f9f317b148821f9c61246c6e91ee916e` |
| `projects/pec/execution/_Decomposition/Deliverables.csv` | `94ee5d182ae99092324505a72bf2f3b0581f85c0bae6c693214cfef709179805` |
| `projects/pec/execution/_Decomposition/ContextBudgetQA.csv` | `93b0bb075a0e83d3219e6293303c3feaa432e693e7255569d4e522ea42434c7c` |
| `projects/pec/execution/_Decomposition/Companion_Inventory.csv` | `1597ceec7af45f33fe348d46429cc3f82042db5dbd6a083903ae04c7bf908662` |
| `projects/pec/docs/PRD.md` (v2.4) | `ae49b8065698f003001b2183f550b814cded5cd5ea06f940b81dd5c287483fbe` |
| `projects/pec/execution/_Decomposition/_LATEST.md` (read only) | `626feaafa213c3fe4995640a42a0a7606a1bd89a200ebf2e588afd4209a212dd` |
| `projects/pec/execution/_ScopeChange/_LATEST.md` (read only) | `e92b3b16a48cd72288c8b6eddc08d62e3e79e0c9bec521864ee7d5484a307d24` |
| `projects/pec/execution/_Evaluation/DecompCoverage/_LATEST.md` (read only; not updated) | `2b43dc3bb34163ae51067f6176ebf235430b59aa668890c1e65d7cc9d3cf1450` |
| `projects/pec/execution/_Coordination/_COORDINATION.md` (item 14) | `a6a188823bfdd1c5acfff1a6e9b51e6e3bf54e5f7d015493d426227de7eb644c` |
| A2 mirrors: DEL-04-03 / DEL-08-01 / DEL-08-03 `_CONTEXT.md` | `b28ada4674662515ed7f975cb59c1ee2c2f9cac3c4bcf0d919ced22af79a7b22` / `74b12e7358a71000b8cd544f2db8a736289e7ca4b1e3f94dbadbf98154292d22` / `95fa815a31a38e59c001dd3596bc47053508cd3ff59c9d3eae67d64ba9d037b5` (each equals its plan §A2 postimage) |
| DEL-01-03 `MEMORY.md` (paired read; non-authoritative) | `44b360c57b934c585befe2cf6a0741199d4cc4ac6b8fc64c04f7be33b88bdae6` |
| `projects/pec/v2/config/loops.json` (feed-profile presence only) | `4ce07ad061abd222acabb2afe0f619fdc840b4cc11d31e49f1dff8fcc299d32e` |

### Decisions

| Source | SHA-256 |
|---|---|
| `projects/pec/execution/_Coordination/_DECISIONS/_REGISTER.md` (rows D-PEC-95, 96, 97) | `2db244bda2c3f8905af5ae5e430712e38450a6d42bf149fb9f79e0ce0fdd21e7` |
| `…/_DECISIONS/D-PEC-95_RULING_2026-09-25.md` | `51dceb7136c24c1dea2f68c2338f66781de17fb2b63a8caf8bc719dd5a4e2beb` |
| `…/_DECISIONS/D-PEC-95_revision_1_5_currency_proposal_2026-09-25.md` | `9137d3872329cea5093f61fb6c4150121e4ffcc2abe900ca88e7339049064b22` |
| `…/_Coordination/CURRENCY_REV15_D95_2026-09-25/HANDOFF_STATE.md` / `MANIFEST.md` | `87dc9884fcf7f2dba0e19ab6edc14fab37b831970e88bdce745caee1890559d9` / `e04793158c4baec5934ffbeba21dd179a80752c8c62275b45e01136fa17d7ff3` |
| `…/_DECISIONS/D-PEC-96_AMEND_DIRECTION_2026-09-26.md` | `c506732e947b6b294642829aa76d8a11134eb37c1a90b6ebd35c12a47c34d3b2` |
| `…/_ScopeChange/checkpoint_snapshots/SCA-006_GROUP-2_2026-09-25/DECISION.md` | `30aebd162e98cdc91923468852af6833feda84c3a3d9d3efe252dc8a87abf989` |
| `…/SCA-006_GROUP-2_2026-09-25/ACCEPTED_MANIFEST.csv` / `Handoff_State.md` | `b95634899a48ed081711cc75478c6e8b7a23cbcb1e36cd25a323e82a9c62bc52` / `2c2aba062303598d5f4bf9a8963e41c7bf143259e96321123251c6fbe3c489c7` |
| `…/checkpoint_snapshots/SCA-006_GROUP-2_AMENDMENT-1_2026-09-26/DECISION.md` | `15720eb1d25ade4e7cb5d62765824634318e0e956129a6e6c3ad30cdaf74777e` |
| `…/_ScopeChange/SCA-006_GROUP-2_AUTHORIZED.md` | `3231d7e122d0a1a89de70ea6591ad644479628ff1fa50eb29cd822018c71998b` |

### Candidate SCA-006 snapshot (`projects/pec/execution/_ScopeChange/SCA-006_2026-09-25_1912/`)

| File | SHA-256 |
|---|---|
| `Brief.md` | `205a46c04f2db6d34bead78db3064a02ff9d9d66a5e54fa9ff06b5c6314a1831` |
| `Impact_Assessment.md` | `93253b7d016de041b2295307af5564808fdc3d9a4e392f1cf92892363fecb691` |
| `Amendment_Preview.md` | `737af0e690688be00c479d1a5e54f2fa82b2c4e25e777abbe07670836473ecf4` |
| `Propagation_Plan.md` | `f95d00d154610d44a37d4aeabfae3fff29aac6c0a0c016bb1241810ebc87d7d8` |
| `Amendment_Actions.csv` | `c5f90801989ee9948ccdd375917ba052fdb5838183e387ed373d8c7c2b824891` |
| `Amendment_Actions_CP2.csv` | `d901b432b9401dca0478a2ff73015273c387d29a1149ae66f5c6fbb2162fc1de` |
| `Supersession_Delta.csv` | `e69f97814294ccd993fceff12cdf992623156c33ca4993adb103b61774e5977b` |
| `Supersession_Map.csv` (committed during this run) | `010ce5c423530123f923413dbfad03ce70fc0ba0c072ee7726f7718847caab92` |
| `Pre_Change_Coverage.json` | `b7b432a2b9e9ae13a911c7193b02776e64cd07e247135b3c98caf77882f4128d` |
| `PRD_V2_4_SUCCESSOR_DIFF.md` | `a743a5273c66dc679a99888c4dc2b865a318dab64fcaaa7768ecb71f35696a4c` |
| `AGENTS_MD_CANDIDATE_DIFF.md` / `AGENTS_MD_AMENDMENT1_DIFF.md` | `7c57a1b2c02c872fae6f778beeddf7f812809d469b504e34d1e6f79bbb48a158` / `317e79187acf656f771e3962f265c74b2eecfc49d45b291080d20c723b42dcf4` |
| `Decision_Log.md` | `893c14ad1546e21fb1700dc231e7fa018b2933f65e5c8fd238c10675157355b7` |
| `Handoff_State.md` | `a5f80525405f9b95c70bcff8a10a22f5109ca11b3af65b2616cbd68d6ed98f1e` |
| `Post_Change_Coverage.json`, `RUN_SUMMARY.md` | NOT_FOUND (A5 pending) |

### Accepted predecessor SCA-005 (`projects/pec/execution/_ScopeChange/SCA-005_2026-09-23_2139/`)

All 14 files equal the hashes the baseline recorded (`Brief.md` `aaf2821b…`, `Impact_Assessment.md` `0bcbe9bd…`, `Amendment_Preview.md` `ad48cc56…`, `Propagation_Plan.md` `50cd0b1d…`, `Amendment_Actions.csv` `5c4ae053…`, `Amendment_Actions_CP2.csv` `7bb3bada…`, `Supersession_Delta.csv` `cb2a3585…`, `Supersession_Map.csv` `4ca705ba…`, `Pre_Change_Coverage.json` `61163c96…`, `Post_Change_Coverage.json` `912610ff…`, `PRD_V2_3_SUCCESSOR_DIFF.md` `153a4ded…`, `Decision_Log.md` `09f99fb1…`, `Handoff_State.md` `a86ae910d0c9ae7bf20a7ebb47de3edb345d1a6067cb1988fc04d5c1d213328a`, `RUN_SUMMARY.md` `e9a0224ec0152bba75c78b84e2c9abe7a5996014eec602b46de4fe3153c1e518`), with `CP2_CANDIDATE/` present. `git diff --name-only 995af4f36 HEAD` over the folder is empty.

### Baseline run (comparison basis; `projects/pec/execution/_Evaluation/DecompCoverage/COV_SCA005_POSTSETUP_2026-09-25_1606/`)

| File | SHA-256 |
|---|---|
| `Brief.md` | `327f37d916cd511e42ec4f2af66e1fb7362ff822edfd3f6cfa2e9f7e643e8c97` |
| `Decision_Log.md` | `5f250cdb61a860f2bf509465c33e8e73f9ce063cbc1267e5fd7c6b7deeede170` |
| `Decomp_Coverage_IssueLog.csv` | `3e93aaf3784545ca777ab620598522d9a4ce4cd0eaf3bf9ad9d34ebf57505850` |
| `Decomp_Coverage_Matrix.csv` | `328118f62d82eb3db62b0c5f0bcec0802b83a3219c136ce9b561df741526c5fa` |
| `Decomp_Coverage_Report.md` | `7b3b586a79b83eb9955f5171c75b4c37c747e9966b2e2bb6a6a23e5bf467ac34` |
| `PrePost_Comparison.md` | `76181ac5bbbc30ac139e08726cd8eb7deb7cc7de7ec1644101e46d10496a5657` |
| `QA_Report.md` | `1774cb0ff215a5ea4e1feb7406b5a6ad9e710a998977ac6a10798707500b6c64` |
| `RUN_SUMMARY.md` | `b30751377f0c94bad336590645e3ecb90ed1579b3722fc62ebf9f8e868006311` |
| `coverage_summary.json` (= SCA-006 `Pre_Change_Coverage.json`) | `b7b432a2b9e9ae13a911c7193b02776e64cd07e247135b3c98caf77882f4128d` |

### Tools (repository, run read-only)

| Tool | SHA-256 |
|---|---|
| `tools/evaluation/audit_structure.py` | `d37ffbd040ace47ea990fd6fbb0911ea073358303a40ac32b3b7d7b111ecdb3f` |
| `tools/evaluation/audit_common.py` (imported) | `c610cb5b427610a9be94d59fb8ad8c050c4955c91e69525e277957351464e8c2` |
| `tools/validation/validate_decomposition_registers.py` | `a1544dc45656f0687600d03aa33e4665ff57ecce038610f843990333e1afb691` |
| `tools/coordination/analyze_dep_closure.py` | `6305a61ca79adee93da09a8e5cb7ca27c16e9e1f89a37f52218617cd29fbfbf2` |
| `tools/scaffolding/create_snapshot_folder.sh` (read, not run; D-3) | `2a01157959d7ac8fe55cd621c43ef61118b83370778f3f24cf54a4641fd1c361` |
| `projects/pec/execution/_Scripts/pec_reliance_hold.py` | `b1712e4b6e9f1476c577afd9170a4dd078beaa95878fa5f3b6c46a17b548cd0e` |
| `projects/pec/execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv` (header only) | `f877d9316c7da76218399838aa6b69f1bb51bbd3e59b5b1d19b31f69ad741cbc` |

### Scratch scripts and outputs (session scratchpad `cov_sca006/`, outside the repository)

Hashes are listed in `QA_Report.md` §"Scratch artifacts".
