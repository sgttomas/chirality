# Independent facade retirement review

Date: 2026-09-22. Reviewer: fresh native Codex TASK `/root/retirement_review`, parent `/root`. Skill: repository `.agents/skills/software-code-review/SKILL.md`. This reviewer did not implement the candidate and wrote only this review. No delegation, installation, product mutation, Git mutation or broad test run. Host permissions are actual filesystem limits; this read-only product scope is an instruction constraint, not a separate sandbox. Codex supplies the engine; exact serving model/effort identity is not exposed in this child record.

## Verdict

**Suitable for parent fan-in and final registered checks; no unresolved actionable source findings.** This is source review, not a test-pass claim, owner acceptance, deliverable issuance or release. Base: `008ef6a4e370822c65eb26ddd792752b4267c7ab`, branch `codex/retire-harness-contract-facade-20260922`. The exact reviewed current bytes and deletions are bound below.

## Finding repaired and independently backchecked

**F1 [P1] Fresh-checkout export required the deleted facade directory.** Initial `exports/chirality-app/export_public.py:62` retained `packages` in `DESKTOP_DIRS`; `build_stage` requires every listed directory before staging and copies each one. Deleting the only tracked package means a fresh checkout has no `frontend/packages` directory. An empty local directory masked the failure. Parent removed the obsolete allowlist entry, removed the residual empty directory and regenerated locally. Reviewer inspected the exact one-line fix and independently confirmed the directory is absent, allowlist membership excludes it and the resulting generated inventory matches current sources. Existing `tools/validation/test_public_export_profile.py` calls `build_stage` and checks the retained Desktop/Runtime surfaces; no test weakening or new expectation is needed. Parent must run that affected test with final checks. **Resolved at source.**

## Scope and contract review

- The owner's parent-supplied current direction expressly retires the old facade and its support/tests. The ruling records one owner act, not independent fabricated App and Root votes or owner code review. D-APP-116/117/119, P-01, D-APP-48 successor identity and unrelated conformance/lifecycle work remain unresolved. Historical D-APP-118 HOLD and D-APP-89 rollback evidence are retained as historical records.
- All 14 deleted package files were private compatibility metadata or simple re-exports. The deleted parameterized test checked only facade/canonical identity; the removed guard required exactly those 13 test probes and the facade source tree. Their purpose is explicitly retired. Canonical Runtime export definitions, behavior/conformance tests, App catalog equality test, packaged dependency boundary and release-quality evaluator remain unchanged. The release-quality script still invokes its evaluator.
- Independent parsed comparisons confirm package.json changes only remove workspaces, the facade guard script and its release-quality prefix. The lockfile changes only remove the workspace field and two obsolete package/link entries. No dependency version or unrelated metadata churn.
- Independent tracked executable/config searches found no live facade import, alias, dependency or script invocation outside frozen evidence. The remaining PEC references are comments; `tools/coordination/validate_harness_contract_pull.py` reads historical files with `git show` at the supplied commit and merely checks the historical command string. Author census and all authored after-hashes were checked; no mismatches. External/untracked/dynamically constructed clients are outside the proven census, as the ruling and author return explicitly acknowledge.
- Runtime's sole source change is the catalog source-label string. The generator uses the same canonical package renderer as the retained catalog equality test. Current App contract/reliance source locators resolve to existing Runtime sources. Nearby old SDK narratives are explicitly not claimed reconciled by this narrow change.
- DEL-03-01 SOW/Remaining, current work graph and decision register correctly record retirement application while preserving other obligations and lifecycle/Checking Approval SHA. The register retains the historical packet and links the new ruling. The application item remains pending review/check completion at this snapshot.
- Export inventory includes 19 files already present at the base plus current hashes, and removes the 16 retired files, for 1,713 total files. Independent read-only reconstruction of current allowlisted membership found no missing/extra rows; all mapped source/projection bytes and all stage size/hash rows matched; report counts matched and boundary scan returned no findings. Generated init content was inspected through the unchanged generator; filtered workflow index bytes were recomputed. This local inventory refresh creates no publication or new export scope. Removing the now-empty Desktop packages root is necessary retirement wiring.

## Checks observed by this reviewer

1. APP-HOLD reliance preflight from the App root: `python3 execution/_Scripts/app_hold.py check --operation reliance --entry-path native-codex/TASK/retirement_review --target DEL-03-01 --target DEL-01-02` — exit 0; ALLOW for both, no active holds. Register SHA-256 `d289b248a900122b012ae540b9b197feae3adbe264bf181f3d46556c500f320c`; scan fingerprint `ee0147b1eb9ccabc3c55eef91dc5c8747e776e244688533370cae9970ba62249`.
2. `tools/software_workflow/validate_change_scope.py` on the whole working diff plus untracked run/ruling files — PASS with named retirement frontend paths, one Runtime renderer, current carrier/decision/graph, local exports and run evidence allowed. The later exporter fix is the explicitly reviewed necessary export wiring above.
3. Read-only package/lock structural comparisons, authored after-hash recomputation, executable/config consumer search and export current-source/stage/manifest checks — pass as described above. These checks executed as short Python or Git read commands in the native tool transcript; no production files were changed.

Parent owns the final App/Runtime build, typecheck, tests, premerge, harness and affected export checks. Installs were reported passing by the parent but are not independently attested here as final validation. Missing final evidence is a pending execution step, not a source defect or new human decision.

## Later candidate handling

Appending truthful check results, integration identifiers and the actual reviewer return to RECORD; marking this one application complete in its current graph/Remaining after checks; and binding retained logs are anticipated closeout changes. Parent must request targeted review of those final record claims/affected paths so review covers the merging candidate. Any further source/package/export change requires affected source rereview and invalidated checks. This review cannot approve unknown future bytes.

## Actual supplied origins

The parent supplied the bounded review brief, allowed output, base, user retirement excerpt, known pending gates and subsequent fix notifications as conversation context. Host/system instructions and skill catalog were supplied by the host; this report does not invent filesystem hashes for them. The following actual repository instructions and authority/entry sources were deliberately read; historical Runtime text was interpreted with its appended D-GOV-43 supersession. No additional role was activated and no workflow was selected.

| Source | SHA-256 |
|---|---|
| `AGENTS.md` | `1bb670ca339a990b153cf033dac2d8e29ca71bdea0accee4200e6dd1feed3d57` |
| `agents/AGENT_TASK.md` | `1a13a5b00b3ce01ff8519efe6b46bcbe0cd6a5b7985e24282fa7efa2c57c8fb7` |
| `.agents/skills/software-code-review/SKILL.md` | `06c27b1be5cfbd9e638570918a8f837d8439c8073c40d3ef708e53874f95570a` |
| `projects/chirality-app-dev/AGENTS.md` | `abb4ff48987b427015ef412874aef8651e028fbc62c49fc3e53a3a9b755b015f` |
| `projects/chirality-app-dev/loop/LOOP_INIT.md` | `1fddcbeb42eec6ec0975014ffb7ce3c47b567e309816064178570688b327f682` |
| `projects/chirality-runtime/AGENTS.md` | `ca1b305c1fbc3ebc83e3718c6b2122170bbab3c1d1f616f744d0339f2a84691d` |
| `projects/chirality-runtime/loop/LOOP_INIT.md` | `890ed040fd518c2448450583727f159d6059e9bdfed8d532b3209d3130600569` |
| `projects/chirality-runtime/execution/_Coordination/MIGRATION_ACCEPTANCE_2026-09-06.md` | `70684ba0b6e6d04037f252f10eef35a2ca78d6cf41477678807ec59826a9004a` |
| `projects/chirality-runtime/execution/_Coordination/HANDOFF_STATE.md` | `bde49a8449b9a1941e4870b2e888103716f27ee1e10789d5d3e73e28c6bfbacb` |
| `projects/chirality-runtime/docs/PRD_AUTHORITY.md` | `81459c2d08e7c1c2b0e3f2d1078c35188c828bd1eff0e1592c180dec1c201808` |
| `projects/chirality-runtime/docs/PRD.md` | `ec2837e50ae89d1aa333f8bef20ec483f0e7bb0ccfbec56633e354dfd81f4e68` |
| `projects/chirality-app-dev/software-workflow.json` | `97b6717a5991549367aa098629fbd7140bce7c7c226a15ef9419c0c3397f65e9` |

## Reviewed candidate bytes

SHA-256 is current worktree content; `DELETED` means absent with exact preimage retained in the base commit. These are the complete tracked diff and new ruling/author/coordination records at source-review return, excluding this self-referential review.

| Path | SHA-256 / state |
|---|---|
| `execution/_Coordination/AgentRuns/HELP-HUMAN-20260922-FACADE-RETIREMENT/RECORD.md` | `d02a71a90ac8248b2c98d1a6c98ceb67a8c5f12b09bfc1cda581e378dc9045c8` |
| `exports/chirality-app/export-manifest.csv` | `ae29447e6b4f5f260dc4dd63d92600f421f8e1da79b83fb14183d5d3ab3d36ca` |
| `exports/chirality-app/export-report.md` | `550ca1575ebad0ee73c473134416ad32765d738d80cf9948fb9570a53dac1516` |
| `exports/chirality-app/export_public.py` | `04edaba77d986594df9768ab68f4986404382bb71d9e4e1c74dc2a27a46c8619` |
| `projects/chirality-app-dev/docs/harness/reliance_boundary_register.md` | `0076edce776bcc503127d3b7a5ee4bad0c691e9b41c6ef5d049ebefdcf09b7f5` |
| `projects/chirality-app-dev/execution/PKG-03_Runtime_Engine_Contract_and_Turn_Lifecycle/1_Working/DEL-03-01_AgentEnginePort_and_Engine_Conformance_Suite/ScopeOfWork.md` | `da103cc8b94c794c3956965a19dfaa58c55cc9be25376c9bedd2ba0a6fd6e102` |
| `projects/chirality-app-dev/execution/PKG-03_Runtime_Engine_Contract_and_Turn_Lifecycle/1_Working/DEL-03-01_AgentEnginePort_and_Engine_Conformance_Suite/_STATUS.md` | `728c749f67a5e2e7d05e9a6894b45679de83f01150a153052e645882c87eefc8` |
| `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP-FACADE-RETIREMENT-20260922/AUTHOR_RETURN.md` | `0d6352f26c30bc67c7e4ce496977863b4c728c83c9749f81b095456bc684c9e1` |
| `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP-FACADE-RETIREMENT-20260922/SOURCES.json` | `1cd364a91dc39e3e5d2b22b59c3cf3177c5c1d52c84027435f90358a0dce2a1b` |
| `projects/chirality-app-dev/execution/_Coordination/AgentRuns/HELP-HUMAN-APP-20260921-CONCORDANCE/WORK_GRAPH.json` | `94ab3528300761d8fc1e0a7313f24956de4ecf7bd66029b6b224dc7155969ba0` |
| `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-118_RULING_FACADE_RETIREMENT_2026-09-22.md` | `9cd9da4d7de3e2d4bd04fa7c3a3c5a92edd9041e56f0c66cac2b374239dcb747` |
| `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/_REGISTER.md` | `fb8f584760e8845b2f136866ea3c163b8d3212bdb36988ed2f389c37e9d29865` |
| `projects/chirality-app-dev/frontend/docs/harness/runtime_engine_contract.md` | `daefba04a41591252ec974c9deebb18c27a1adf1e6258aa98a02280e6ca89bf6` |
| `projects/chirality-app-dev/frontend/docs/harness/tool_catalog.md` | `566e8c0262a266c18d6a420d829e89d9c1524b2c9979303f9a57971e7564fefa` |
| `projects/chirality-app-dev/frontend/package-lock.json` | `12a4003b155a3d458dc7bd009dc4964e0f48b0920d0e326973840ed0a4e8f9e6` |
| `projects/chirality-app-dev/frontend/package.json` | `7987224a03e8b1c0f055ad9dc022c77e5084c666e1098ad3ffd41dfa11636d69` |
| `projects/chirality-app-dev/frontend/packages/harness-contract/package.json` | `DELETED` |
| `projects/chirality-app-dev/frontend/packages/harness-contract/src/agent-engine-port.ts` | `DELETED` |
| `projects/chirality-app-dev/frontend/packages/harness-contract/src/domain-profile.ts` | `DELETED` |
| `projects/chirality-app-dev/frontend/packages/harness-contract/src/engine-conformance.ts` | `DELETED` |
| `projects/chirality-app-dev/frontend/packages/harness-contract/src/errors.ts` | `DELETED` |
| `projects/chirality-app-dev/frontend/packages/harness-contract/src/event-schema.ts` | `DELETED` |
| `projects/chirality-app-dev/frontend/packages/harness-contract/src/index.ts` | `DELETED` |
| `projects/chirality-app-dev/frontend/packages/harness-contract/src/mcp/tool-names.ts` | `DELETED` |
| `projects/chirality-app-dev/frontend/packages/harness-contract/src/operation-proposal.ts` | `DELETED` |
| `projects/chirality-app-dev/frontend/packages/harness-contract/src/sdk-version.ts` | `DELETED` |
| `projects/chirality-app-dev/frontend/packages/harness-contract/src/tool-catalog.ts` | `DELETED` |
| `projects/chirality-app-dev/frontend/packages/harness-contract/src/tool-descriptor.ts` | `DELETED` |
| `projects/chirality-app-dev/frontend/packages/harness-contract/src/transcript-replay.ts` | `DELETED` |
| `projects/chirality-app-dev/frontend/packages/harness-contract/src/types.ts` | `DELETED` |
| `projects/chirality-app-dev/frontend/scripts/assert-harness-contract-deps.mjs` | `DELETED` |
| `projects/chirality-app-dev/frontend/scripts/generate-tool-catalog.mjs` | `52a62332ecbac6900ab55e92b9d0127dda1c544690b4699b74dc801aa5c36fe2` |
| `projects/chirality-app-dev/frontend/src/__tests__/lib/harness-contract-rollback.test.ts` | `DELETED` |
| `projects/chirality-runtime/packages/contracts/src/harness/tool-catalog.ts` | `b6afb395559889ea350e47079e7fb62f33bb75140dd75f002a00471f45432ee5` |

## Final closeout backcheck — 2026-09-22

**PASS: complete current candidate is independently reviewed with no unresolved blocking findings; suitable for commit/push and required hosted CI.** This addendum supersedes the earlier pending-local-check assessment. Actual merge remains conditional on the required CI and unchanged reviewed candidate. No owner code review, final product conformance, issuance or release is claimed.

Parent supplied a bounded follow-up to review the final RECORD, DEL-03-01 Remaining/MEMORY, graph and actual check evidence. Reviewer reused the same role/skill and instruction basis; no further instructions, workflow, delegation or product writes were introduced. Recomputed the prior review's content hashes: only RECORD, _STATUS and current graph changed; MEMORY is the additional closeout carrier. All reviewed product/package/export/generated bytes and author/ruling source evidence remained identical.

The final records close only the owner-ruled facade application and its routing. Other conformance and successor-identity residuals, D-APP-116/117/119, P-01, lifecycle and Checking Approval SHA remain open/unchanged. Graph correctly says applied and locally checked pending integration. HISTORY/MEMORY scope matches the observed removal and local checks.

Observed final release-quality summary is pass, each command exitCode 0, with releaseClaim false. Retained stdout confirms 221 passed files plus one skipped file, 2,272 passed tests plus four existing skipped tests. Section 8 reports eight passed checks; Section 9 sixteen passed checks. Runtime stdout confirms 42 files / 407 tests passed. Python's original run confirms 384 passes including export tests; final carrier/practitioner backcheck confirms 379 passes. App build output completes its renderer, Electron and Runtime bundling; unsigned package log reports signed:false, dependency and Codex-pin PASS and 370 instruction files with bundle integrity pass. Secret scan's final retained log reports pass / zero blocked findings. Self-check retains INFO14, NOT_APPLICABLE1, REVIEW4, WARN123 with no BLOCK. These are independent inspections of parent-executed evidence, not duplicate execution by this reviewer.

Package `sourceCompleteness.status=needs_remediation` for KG-001 tools registry/examples is preserved distinctly from successful byte integrity. Earlier failed wrapper summaries remain failures: initial Section 8 boot-taxonomy check failed; canonical-long attempt had full-test/Section 9 failure while premerge passed; final short canonical temporary-root execution passes without source/test changes. The exact final disposable integration driver is retained as run evidence, not a maintained product fixture. D-APP-48 and D-30 JSON bytes independently match the base; their distinct source commits (55a066fdff6877d8aa2a49ce08a545ac98872848 versus ee290e22a8c19d46fb8004114d2ede55b805fba4) support preserving the combined historical consumption mismatch instead of claiming it fixed.

A closeout evidence-retention gap was reported during review: the first record relied on ignored latest artifacts and temporary logs. Parent resolved it by retaining the canonical raw witnesses, final and failed-attempt summaries and integration driver under `validation/` and linking them from RECORD. Reviewer compared retained copies with their actual source files byte-for-byte, then waited for the final practitioner and secret-scan logs to finish and freeze. The sorted hashes below bind those exact retained bytes. Existing absolute paths inside raw evidence record the original host; this addendum supplies stable repository-relative locators. No new product evidence acceptance or human gate is introduced.

### Final changed closeout files

These hashes supersede their earlier table entries; MEMORY is newly covered here.

| Path | SHA-256 |
|---|---|
| `execution/_Coordination/AgentRuns/HELP-HUMAN-20260922-FACADE-RETIREMENT/RECORD.md` | `41e2967dc87f380e1e5419ca93b2d6f44d9807a2032a0c30e9d614bde059572f` |
| `projects/chirality-app-dev/execution/PKG-03_Runtime_Engine_Contract_and_Turn_Lifecycle/1_Working/DEL-03-01_AgentEnginePort_and_Engine_Conformance_Suite/_STATUS.md` | `38e308468573402f2c20148c61824b1ac81ad1d54e0c0e6a5e97ee0cec511d48` |
| `projects/chirality-app-dev/execution/PKG-03_Runtime_Engine_Contract_and_Turn_Lifecycle/1_Working/DEL-03-01_AgentEnginePort_and_Engine_Conformance_Suite/MEMORY.md` | `6c0ebb5324e37a7413b9da0af691fba81cb9ce5526ed2b2cf8eb10c6787f7c4a` |
| `projects/chirality-app-dev/execution/_Coordination/AgentRuns/HELP-HUMAN-APP-20260921-CONCORDANCE/WORK_GRAPH.json` | `40e504bb78e9fa0d5fc73404b0df53b14c20b7a664da486d4419da1ad895448b` |

### Retained check evidence

Paths are relative to this run; SHA-256 independently recomputed by reviewer after final freeze.

| Path | Bytes | SHA-256 |
|---|---:|---|
| `validation/app-build.log` | 7984 | `1349cecdd91b3614efe241708e30f2372cc46a0d8bf735b71e182316bda4a9d2` |
| `validation/app-hold.json` | 41375 | `04c529681fdb0534522b440adee25c21165f66298c82a762abde1dbde30472b2` |
| `validation/final-practitioner.log` | 511 | `eb4df97191df51e86547e381d2ac2e303ccda541dde76daaeaf8d00e051f3d7b` |
| `validation/full_test.stderr.log` | 283 | `2b464252c80ee39b52b6acff638aab089d761efad9d20dcbf2f213f596ad89e6` |
| `validation/full_test.stdout.log` | 26496 | `08d9eeb518275f1b00bc5c41ba74cbe0811d42b04f20d2a403cfa104aa65bdf4` |
| `validation/instruction-root-integrity-summary.json` | 126750 | `4bbea6ce240605aeeb287af8366c3539e9706421a3658d0586f809c14437d464` |
| `validation/integration-check.py` | 3933 | `eaf60615b95f656643ba43967b721d6002f9800b32f87614fbb7c1da3fda3561` |
| `validation/pack.log` | 8370 | `1bc79af237b6b702d80abd263fba62a25cb8c0e0e5b88fb06ba906f4eb43a85e` |
| `validation/premerge.stderr.log` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `validation/premerge.stdout.log` | 846 | `6934fd7ce45caa5b540578c0a785e701ba86d225aa749560b8897c6afbd44880` |
| `validation/python-tests.log` | 511 | `cecf57a0ab3fd8e430340a634e31419b3fc9368b71941143f097993c02ed3abe` |
| `validation/release-quality-canonical-long.json` | 4339 | `ee2a2ea6ad97fe389df6fe670c09ce5ab6978d57c41948d3a7291402b1e84eba` |
| `validation/release-quality-initial.json` | 4401 | `21272659ae9b1635773566862db94930c099a2b8a7aa312944e0e7090b389a50` |
| `validation/release-quality-summary.json` | 4295 | `4a9d8f356f66b26124c2ea0a3ba93cc73a02bf4f3f0fdbfca6f6c866f0c629e0` |
| `validation/release-quality.log` | 29689 | `ca873f0c00d8c0b14c5f599bbbcb09c86eb1a2d6b4c8ef8d8f4c8295db7b0c3c` |
| `validation/runtime-tests.log` | 7346 | `3ad3d42c52910e5ce57443675f583bdc606685946ffbad56ddd51a4e96cd3a6f` |
| `validation/secret-scan.log` | 332 | `19758b85181f92ed7a1749707860ffeff03afaddf85169fbee2ee0af6fee0e1d` |
| `validation/section8-canonical-long.json` | 1958 | `a637e40c358dd94b85cdb6a91576a65e9451959ac6e566cefb3b9e9438a610cf` |
| `validation/section8-initial.json` | 1850 | `024ff8c7959fc12c906eda37cfd597d425f2c0bf70617f4d7b253d188dd0d68b` |
| `validation/section8-summary.json` | 1958 | `ced2478b27f98110c60c747cb049da3bd7be8175fc9553f451479180321cd87e` |
| `validation/section9-summary.json` | 20941 | `74b721754970a105cd323313adbbc9ad5ff8973ad907e31b2191e8905173b6ff` |
| `validation/section9.stderr.log` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `validation/section9.stdout.log` | 1516 | `6230f136ccf5096dc37a35e948cc12eabf2c15b8808fa73dc16eb7b50f9b9535` |
| `validation/self-check.log` | 44885 | `f6f7fa3e2ad661c881c90508b3b4a7ba232e91eac225ffcfa7b2d00e6327974a` |
| `validation/typecheck.stderr.log` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `validation/typecheck.stdout.log` | 136 | `6bfb0613ee629233a3fdf0cc140d4589eade8427aa3243493eee1e88321da6d8` |
