# W10 and support-document independent semantic review

Verdict: **CHANGES REQUESTED — final affected backcheck required**. Review date 2026-09-22. Reviewer: fresh native delegated TASK `/root/app_record_repair_manager/review_10_docs`, parent `/root/app_record_repair_manager`; no delegation and no production writes. Exact model/effort is host attribution, not independently exposed here. Host filesystem permissions remain the enforcement boundary. This file is the sole review write.

## Scope and binding

Basis HEAD `1b5adbf50142a4c01c454c62a31dfcdc60da1894`. Complete PKG-10 diff: five SoWs and their 25 support carriers; all 104 changed CLM blocks and five output-matrix sections. Also all eight WEXT support files (BUILD_AND_RELEASE, VALIDATION_STRATEGY, RELEASE_QUALITY_GATES, RELEASE_QUALITY_RUNBOOK, BOUNDARY_REVIEW_CHECKLISTS, reliance_boundary_register, adding_a_tool, decision register), 151 W10 residual keys and 41 WEXT dispositions. Parent separately reviews decomposition/navigation/reverse ownership, including WEXT SOW-079.1/.2 and SOW-080 carrier correctness. Their disposition routing was inspected here, not their excluded production diff.

Parent explicitly extended this review to the limited App `docs/DIRECTIVE.md` settled D-GOV-43/A2/D-APP-127 propagation. Its full changed semantics were checked against the ruled items and supplement; no new semantic finding. Human/project authority, ordinary instruction integrity, domain controls, secret protection, qualification gaps and affected-check reuse remain. No Root instruction amendment is inferred.

Snapshot binding: 39 production files. SHA-256 of exact scoped `git diff -- <sorted files>` bytes: `d7d4595ee06b41b689fe38f974c17913b9e01d407b4b6f8fead7afdadbe05d9d`. SHA-256 of sorted `SHA256 + two spaces + repository-relative path + newline` manifest: `f48988126bd7df5af4fd020fcbbb0d6308e19072a590ca474e0d6ba56cdc2a8a`. Individual hashes appear below. These bind the inspected state, not future manager edits. W10/WEXT manifest hashes at this observation:

- `W10_CHANGES.csv`: `82b3066762bbf798f867f680c001dabb0717f04c75db2aa2e7d5b9b10db8e59e`
- `W10_ROWS.csv`: `ac8b12429b59380d23d6c433717913d2bfbb149ecd016178bd39fe676299e15c`
- `WEXT_CHANGES.csv`: `f5febe94aca9a788d9e8c31ecfd45799005dd964fc5d92d11280fff55901616e`
- `WEXT_ROWS.csv`: `aa7ecb4ed46c086fb29ed323937b4c7ee29d9c6f62d57544618cde069a401893`

## Findings and repair state

1. **OPEN, P2 — preserve D-APP-62 qualification.** DEL-10-01 `_DEPENDENCIES.md` deleted its complete 2026-07-18 scoped-interpretation addendum while retaining the earlier `_SEMANTIC.md` non-consumption note. That ruling distinguishes dependency-extraction evidence from legitimate semantic-lensing consumption. Restore the exact dated addendum or its complete scoped meaning and ruling reference. Sent to author_10 and manager; no reviewer fix.
2. **RESOLVED on inspected current bytes, P2 — packaging command truth.** BUILD_AND_RELEASE and VALIDATION_STRATEGY previously said pack/dist build inputs and that pack is unconditionally unsigned. `package.json` scripts and `pack-electron.mjs` require prebuilt inputs and apply the signing environment to both targets. Manager now states prebuilt packaging, unsigned default/supplied signing identity, and explicit preparation prerequisites. Source inspection backchecks this; no package execution or signing result was claimed.
3. **OPEN, P2 — final D-APP-38 narration and hashes.** All five PKG-10 `_REFERENCES.md` current-observation paragraphs still say ExpectedSHA256 remains unchanged, while manager synchronization changes those values. Correct the final current-state description, preserve the author's earlier bounded-history distinction, and refresh overlapping W10/D38 manifests. Parent reports an authorized App DIRECTIVE propagation and planned final v25 synchronization; this review does not claim that pending application/recomputation occurred. Preserve retired DEL-09-07 reference bytes and disclose historical mismatches rather than claiming every row passes.
4. **OPEN, P2 — actionable generic-core task locator.** DEL-10-04 `_STATUS.md` points OpenPipeStress-specific descriptors/catalog entries at generic `contracts/src/harness/domain-profile.ts`, where none exist. Actual descriptor and constant profile_id are in `contracts/src/harness/tool-descriptor.ts` around 821–832, with related tool names/generated catalog. Correct the locator; retain FR-114 and the generic type as comparison basis. Sent to author_10 and manager.
5. **RESOLVED on inspected current bytes, P2 — target versus qualification.** RB-ENGINE now says Codex is the sole MVP engine and qualification target, avoiding the prior unsupported “sole qualified MVP engine” assertion. Its remaining checks and unknown results stay visible.

## Independent coverage and checks

- Own APP-HOLD reliance preflight ran before production consumption: all five DEL-10-01..05 ALLOW; operation `reliance`, entry `TASK:APP_RECORD_CLOSEOUT:review_10_docs`, exit 0. Register SHA `d289b248a900122b012ae540b9b197feae3adbe264bf181f3d46556c500f320c`; scan SHA `68b88e611cd7b0ebfa61dc15aa1e3910a01da286ea7e0d9212ef46ea2b1ac675`. This is selection evidence, not acceptance.
- Independently parsed HEAD/current level-2/3 section boundaries: exactly 104 changed CLM units, exact key-set equality with W10_CHANGES, all 208 old/new complete-block hashes match. All ten output-matrix old/new hashes match. Whole-file hashes require refresh after the pending repairs and manager D38 application; no final whole-manifest PASS is asserted.
- All 151 original residual keys and every original field reproduce unchanged from R5/RESIDUALS/DEL-10-*.csv. Current counts: 124 REPAIRED, 23 DELIVERY_TASK, four DEFERRED_SCOPE. Reviewed every disposition against actual changed claims or surviving tasks. The four REGISTER deferrals concern evidence-anchor/Notes/LastSeen metadata; they are explicitly administrative, not product implementation or a new human decision. Parent can repair them within an authorized metadata reconciliation; they do not erase any formal prerequisite.
- WEXT has 41 unique keys: 36 REPAIRED, four DELIVERY_TASK, one historical no-rewrite disposition. D125 items 1/4/5 remain specific contracts/integration work. Three generated-catalog keys retain a concrete generator applicability-label task plus regeneration-equality validation; generator-owned output is unchanged. D99 historical bulk discrepancy is retained with no invented old retention reason; no assertion that the original discrepancy never happened.
- All five formal Dependencies.csv files equal HEAD byte-for-byte. All five SoW frontmatters, lifecycle states, Checking Approval SHAs and History sections are unchanged (20 direct comparisons). Current descriptive dependency summaries preserve DEP-10-02-005, DEP-10-03-004, DEP-10-04-004, Option-C and staged activation subjects.
- Checked existing ADOPTED OpenPipeStress/PEC profiles and individual applicable schema hooks; inapplicable/TBD hooks remain explicit. Checked current TYPES section 11.2 at HEAD: constant proposal-only status already exists; no repair author is credited with adding it. Checked canonical domain type/descriptor sources, retained domain test cases, application-tool catalog validation/unregistered-call rejection, and the absent App application-tool registration search. Those reads establish source facts only.
- Checked package commands, packaging-input/signing branches, release-quality in-process Section9/premerge reuse, network-proof output defaults, and catalog regeneration equality test. No product tests were run by this reviewer. Manager-reported 24 passing compatibility tests cannot establish live actor enforcement, domain quarantine, redaction, instruction protection, or Codex composition.
- Release documents distinguish prior candidate-specific 3.0.0/3.0.1 authority and owner testimony from absent result artifacts; no signing, notarization, native result or release recertification follows. Source/code availability never substitutes for authority. Domain ownership, staged integration, accountable human acts, structural redaction and ordinary instruction integrity survive the lifted wording.

## Return boundary

The substantive review is complete on the snapshot bound here; final approval remains withheld for findings 1/3/4 and affected whole-file manifest binding. Backcheck the repairs, final D38 narration/hash application, and any later changed claims before a PASS. The parent's full-tranche re-extraction and registered checks remain additional work. This review is neither implementation completion nor lifecycle acceptance, release readiness, certification or professional reliance.

## Supplied/read origins

Root AGENTS was supplied in context; current file hash below records its repository origin. TASK/App AGENTS and selected `bundled:chirality-root/reconciliation` entrypoint/contract/R5–R6 method were read deliberately. No other role was activated. Ruling/source hashes are evidence identity, not new acceptance.

- `AGENTS.md` — `1bb670ca339a990b153cf033dac2d8e29ca71bdea0accee4200e6dd1feed3d57`
- `agents/AGENT_TASK.md` — `1a13a5b00b3ce01ff8519efe6b46bcbe0cd6a5b7985e24282fa7efa2c57c8fb7`
- `projects/chirality-app-dev/AGENTS.md` — `abb4ff48987b427015ef412874aef8651e028fbc62c49fc3e53a3a9b755b015f`
- `workflows/reconciliation/WORKFLOW.md` — `75948a77e7ee3ebd9cd9d8a2089c9aff75ca76b49d87260793e6fbdd152fa380`
- `workflows/reconciliation/resources/contract.md` — `36eb3a4454e384fae7ea3e5d60dda2f9d63e9b7c2e7758c40048f00cb422b2fb`
- `workflows/reconciliation/resources/method.md` — `f1c8f54909c0ae4341d53391cb4a96fe377dfc1f167c00b1159d15eab079ea16`
- `docs/governance_harness/_DECISIONS/D-GOV-43_codex_host_replatform.md` — `08bef1e22715b4962e365ec3dce8a0cd66a212ea79cdc21a33ffa818f05f5899`
- `docs/governance_harness/_DECISIONS/D-GOV-43_supplement_topology_A2.md` — `fa3756ad3bdf02104da47fc5ba697b4f96d8a02029f008b32bd96a094ec46cb2`
- `docs/governance_harness/_PROPOSALS/D-GOV-43_2026-09-11_codex_host_replatform/D-GOV-43.proposed.md` — `5afadb4ac0d33c26d188abbd86508de31dd08a027bd7858005273a11eab784cc`
- `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-118_PACKET_FACADE_RETIREMENT_2026-09-05.md` — `8eb3f39185a879d67fceb5c031bc292f8e24eac7cc2d85c70124d10663fe0411`
- `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-118_RULING_FACADE_RETIREMENT_2026-09-22.md` — `9cd9da4d7de3e2d4bd04fa7c3a3c5a92edd9041e56f0c66cac2b374239dcb747`
- `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-127_RULING_APPLICATION_D-GOV-43_CODEX_HOST_REPLATFORM_A2_2026-09-12.md` — `211ce2d25fde94c2c88c7b688a530e697b1b923efffaaaf18f39db414f494c19`
- `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-131_APPLICATION_R5_R6_AGENT0_2026-09-22.md` — `37a3dd3798af7c8d8ce5ea21b2b5d9dac22b452c8473c260fbafbb5a219de097`
- `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-132_RULING_P01_AND_AGENT0_DISPOSITIONS_2026-09-22.md` — `d52dd0f59913961312572ff41dadc37cb203efc8838b408277b2b4a61048c8a3`

## Inspected production hash manifest

```text
300842788439654754d7194aa4f0b335c09a2c5510deb8a157ed0d9ac21de2d9  projects/chirality-app-dev/docs/BOUNDARY_REVIEW_CHECKLISTS.md
c78c97a06608fe5b281d15d12972086ea698dfda0ae94e619e266702ed968e32  projects/chirality-app-dev/docs/BUILD_AND_RELEASE.md
a07418a7b1bb7919d7f9e495e42e81f1b47a0a389cab9dbd3909cb81c992bcc1  projects/chirality-app-dev/docs/DIRECTIVE.md
b4cb2219166558688cbe18504fe5776a4200aac7fb1c6ad239ee4d8a27e62e08  projects/chirality-app-dev/docs/RELEASE_QUALITY_GATES.md
be544a2c29dc6b1994d989252fcef93e3bb85ac101ba6881ee26502f9e20e368  projects/chirality-app-dev/docs/RELEASE_QUALITY_RUNBOOK.md
4c61ab5b58805564ff3ff5ec864cf12ede400bdcb01c5c7d6df0304ecb36229e  projects/chirality-app-dev/docs/VALIDATION_STRATEGY.md
efbe0fde26c17e20d5d3b06bde7ade8d881c4b9b6e1d8666dd6aacd592acb0d7  projects/chirality-app-dev/docs/harness/reliance_boundary_register.md
d1fb862e61a64cff8113f7d95a42a066b2b888fedfe1ec1aa170072f5971a0c0  projects/chirality-app-dev/execution/PKG-10_Domain_Engine_Future_Boundary/1_Working/DEL-10-01_DomainEngineProfile_Contract_Draft/MEMORY.md
b0bad5b9255bf6b6e8c5db389ad791f2f5615e0ae83b9ac756eda00152c427d8  projects/chirality-app-dev/execution/PKG-10_Domain_Engine_Future_Boundary/1_Working/DEL-10-01_DomainEngineProfile_Contract_Draft/ScopeOfWork.md
c21bdb57effdae90beb153c268b17e153e1a4ec1d82caed97085f7668e65059e  projects/chirality-app-dev/execution/PKG-10_Domain_Engine_Future_Boundary/1_Working/DEL-10-01_DomainEngineProfile_Contract_Draft/_CONTEXT.md
2813dfd12658cac89513d46d5b29d9aa8dacb1517bf3992922fa017c2c52128e  projects/chirality-app-dev/execution/PKG-10_Domain_Engine_Future_Boundary/1_Working/DEL-10-01_DomainEngineProfile_Contract_Draft/_DEPENDENCIES.md
6660aed3e9ec6603f999e0490c77838b84611f2f705ea57360383be3b389ad43  projects/chirality-app-dev/execution/PKG-10_Domain_Engine_Future_Boundary/1_Working/DEL-10-01_DomainEngineProfile_Contract_Draft/_REFERENCES.md
b0df9614460f4a5dadc70d4816a1788085419e06d441cd6c4e7d3d575775cf0a  projects/chirality-app-dev/execution/PKG-10_Domain_Engine_Future_Boundary/1_Working/DEL-10-01_DomainEngineProfile_Contract_Draft/_STATUS.md
8000cb4fc0c9611cfcbe792c32f1dee9cf4bdfbeb09bc28dae200705ebe9e21c  projects/chirality-app-dev/execution/PKG-10_Domain_Engine_Future_Boundary/1_Working/DEL-10-02_Protected_Path_and_Proposal_Path_Policy/MEMORY.md
aad0173fc51acb2cef7f755678653e53c855f50b3b7fc51148b66323c93baef3  projects/chirality-app-dev/execution/PKG-10_Domain_Engine_Future_Boundary/1_Working/DEL-10-02_Protected_Path_and_Proposal_Path_Policy/ScopeOfWork.md
62261c6a37e0856c1c95ee27d853115be52df7467c5fa6b2890742327de69350  projects/chirality-app-dev/execution/PKG-10_Domain_Engine_Future_Boundary/1_Working/DEL-10-02_Protected_Path_and_Proposal_Path_Policy/_CONTEXT.md
56f20123f918fca9f466d53e01453f9c36021a41051beb53341837455f8afad8  projects/chirality-app-dev/execution/PKG-10_Domain_Engine_Future_Boundary/1_Working/DEL-10-02_Protected_Path_and_Proposal_Path_Policy/_DEPENDENCIES.md
63f5fa5ed0e190839fe2c17ec998c22e6b88f6970e3b00cf848d95372d40474c  projects/chirality-app-dev/execution/PKG-10_Domain_Engine_Future_Boundary/1_Working/DEL-10-02_Protected_Path_and_Proposal_Path_Policy/_REFERENCES.md
ae83cc59e6db1e5b4b3a45d171687053ea93e18e6ec85404fc3f2258aeef0e7d  projects/chirality-app-dev/execution/PKG-10_Domain_Engine_Future_Boundary/1_Working/DEL-10-02_Protected_Path_and_Proposal_Path_Policy/_STATUS.md
ab8e94aba834934b7c512a7155172b2f27707fd7f7f322b74487b5053ffad347  projects/chirality-app-dev/execution/PKG-10_Domain_Engine_Future_Boundary/1_Working/DEL-10-03_OperationProposal_Record_and_Human_Gate_Workflow/MEMORY.md
2423f6e874b415aa3f503b0cec52d7deb75de3286bee3fd6551a6206245d9ae6  projects/chirality-app-dev/execution/PKG-10_Domain_Engine_Future_Boundary/1_Working/DEL-10-03_OperationProposal_Record_and_Human_Gate_Workflow/ScopeOfWork.md
63e8d893485b69a5c5606213e2a7ccf385afe99554860008b3cbef3f09fac0c1  projects/chirality-app-dev/execution/PKG-10_Domain_Engine_Future_Boundary/1_Working/DEL-10-03_OperationProposal_Record_and_Human_Gate_Workflow/_CONTEXT.md
e2561642d920987c7b7c78b34ee7bbe9d08bc1db78708a99616e829652ec9917  projects/chirality-app-dev/execution/PKG-10_Domain_Engine_Future_Boundary/1_Working/DEL-10-03_OperationProposal_Record_and_Human_Gate_Workflow/_DEPENDENCIES.md
a6250034da2af14a62c9b99bd04ca797ef04d13a40368b07065e3fbff9b6e8ef  projects/chirality-app-dev/execution/PKG-10_Domain_Engine_Future_Boundary/1_Working/DEL-10-03_OperationProposal_Record_and_Human_Gate_Workflow/_REFERENCES.md
b2bd8fe9a34530cc2e93a69b30096bc926395cd8dbd6a42407f49dcd491e28eb  projects/chirality-app-dev/execution/PKG-10_Domain_Engine_Future_Boundary/1_Working/DEL-10-03_OperationProposal_Record_and_Human_Gate_Workflow/_STATUS.md
da08bfebf7576167c04d1b634e180212c6cbc0beac3da22525a84ae3e48fa128  projects/chirality-app-dev/execution/PKG-10_Domain_Engine_Future_Boundary/1_Working/DEL-10-04_Domain_Profile_Validation_and_OpenPipeStress_Fixture/MEMORY.md
0b64bdf6b3a6d038333351b98c08ce3a8a968e21083cc1b5a7ca4679bfd07177  projects/chirality-app-dev/execution/PKG-10_Domain_Engine_Future_Boundary/1_Working/DEL-10-04_Domain_Profile_Validation_and_OpenPipeStress_Fixture/ScopeOfWork.md
7354d43be83acc426d3b6608e8fec1fbc2588221ffba1bf7b2293eb6dedbd7f6  projects/chirality-app-dev/execution/PKG-10_Domain_Engine_Future_Boundary/1_Working/DEL-10-04_Domain_Profile_Validation_and_OpenPipeStress_Fixture/_CONTEXT.md
cdf095c6f32a80bdc08a95896ffb597780886b6f12072f096d7c912f5223b487  projects/chirality-app-dev/execution/PKG-10_Domain_Engine_Future_Boundary/1_Working/DEL-10-04_Domain_Profile_Validation_and_OpenPipeStress_Fixture/_DEPENDENCIES.md
45d63e34badb3715f20d1b54c31831f3112a7043b7a2f7c56f8780279b0c3b29  projects/chirality-app-dev/execution/PKG-10_Domain_Engine_Future_Boundary/1_Working/DEL-10-04_Domain_Profile_Validation_and_OpenPipeStress_Fixture/_REFERENCES.md
d894b25428cab4f63d4a1e4e11964b965b7b7620f4c5717b3d8a3c6aa9c241ba  projects/chirality-app-dev/execution/PKG-10_Domain_Engine_Future_Boundary/1_Working/DEL-10-04_Domain_Profile_Validation_and_OpenPipeStress_Fixture/_STATUS.md
6e1810e118f0d00dd7b72e3fbec1c0977bf9fbee4d127e0e0b9e89b6786ba4a3  projects/chirality-app-dev/execution/PKG-10_Domain_Engine_Future_Boundary/1_Working/DEL-10-05_Domain_Boundary_Notices_and_Solver_Truth_Separation/MEMORY.md
0969cadbba3cfdd0fe56267c570cbd6de2c2877935b950ad6ed9a4d7ea6a1732  projects/chirality-app-dev/execution/PKG-10_Domain_Engine_Future_Boundary/1_Working/DEL-10-05_Domain_Boundary_Notices_and_Solver_Truth_Separation/ScopeOfWork.md
9bb7eac5b926113154b281a9c4541c8c57e9d417605b24c8d77a624bda7f9207  projects/chirality-app-dev/execution/PKG-10_Domain_Engine_Future_Boundary/1_Working/DEL-10-05_Domain_Boundary_Notices_and_Solver_Truth_Separation/_CONTEXT.md
e2a3c24f683fe7578152e4c824acbfef8440765f0f820894d3f02f47c2f672e6  projects/chirality-app-dev/execution/PKG-10_Domain_Engine_Future_Boundary/1_Working/DEL-10-05_Domain_Boundary_Notices_and_Solver_Truth_Separation/_DEPENDENCIES.md
3e89bd38dc90821f82a2f7c0548da273169b770fb2b3b4fe426d08d2540c7b89  projects/chirality-app-dev/execution/PKG-10_Domain_Engine_Future_Boundary/1_Working/DEL-10-05_Domain_Boundary_Notices_and_Solver_Truth_Separation/_REFERENCES.md
46e95f414b445b6f078ec68481e17c5992d080b7c94aa45e7f226df8e0a8737e  projects/chirality-app-dev/execution/PKG-10_Domain_Engine_Future_Boundary/1_Working/DEL-10-05_Domain_Boundary_Notices_and_Solver_Truth_Separation/_STATUS.md
c0096fffd2c38488d2e58ce6125609ab483566869f9b9424d805556678fb3ab8  projects/chirality-app-dev/execution/_Coordination/_DECISIONS/_REGISTER.md
70419b190bdfa84dbc9c1acae2d434485894e4664c02808bfd33ef67f884cead  projects/chirality-app-dev/frontend/docs/harness/adding_a_tool.md
```
