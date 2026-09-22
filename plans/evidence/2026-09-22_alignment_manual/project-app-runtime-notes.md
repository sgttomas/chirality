# App and Runtime operational-entry findings

Date: 2026-09-22. Prepared by TASK /root/project_coverage_manager/app_runtime_review for WORKING_ITEMS /root/project_coverage_manager, under HELP_HUMAN /root. Mechanism: actual Codex delegated-harness-native collaboration child; role and write restrictions are instruction-asserted on a host with unrestricted filesystem access. No child delegation occurred.

This is a bounded documentation investigation, not adoption, project acceptance, implementation activation or release. The supplied repository basis is 9b7ac5fb3c7f06cec35f24de8ebba8331bb95ac8 from the undertaking BRIEF. No Git commands, remote refresh, package installation, project guard execution, build, test suite, live App trial or account operation was performed. Findings describe the checked-out files read during this run. Exact source hashes and read scopes are in project-app-runtime-sources.json. Commands below are verified recipes, not claimed passing executions.

## 1. App: enter through the live loop, then the selected undertaking

An ordinary App development entry resolves the checkout root, reads Root AGENTS.md, the actually invoked role, project AGENTS.md and the thin launcher, then follows the live loop. The launcher selects HELP_HUMAN; a delegated TASK remains TASK under its own brief rather than becoming Agent 0 by reading the launcher. [A1, G1]

~~~sh
REPO_ROOT=$(git rev-parse --show-toplevel)
cd "$REPO_ROOT"
# Read AGENTS.md and agents/AGENT_HELP_HUMAN.md for a fresh HELP_HUMAN entry.
# Read projects/chirality-app-dev/AGENTS.md.
# Follow projects/chirality-app-dev/init/dev-loop-init-prompt.md.
# Read projects/chirality-app-dev/loop/LOOP_INIT.md and its current graph.
~~~

At this snapshot, LOOP_INIT points to:

    projects/chirality-app-dev/execution/_Coordination/AgentRuns/HELP-HUMAN-APP-20260921-CONCORDANCE/WORK_GRAPH.json

That pointer locates the September 21 whole-corpus concordance undertaking. It does not select a fresh development phase, lift the separately recorded development pause, or switch the existing undertaking to the new bounded-reconciliation method. Read its owner directions, pinned method/basis, linked phase cursor and actual decision records. App's September 22 adoption expressly preserves those existing run gates. [A2, A3]

The current frontier is unusually important for the manual: D-APP-130 accepts the R4 decision book and its 25 packets as the R5 basis; R4 is complete, but no packet ruling or repair is authorized by that record. R5 opens with the owner's packet rulings, transcribed to their own record and merged before repair dispatch. Only then follows a repair manifest and bounded tranches; Runtime code routes to Runtime, shared governance to Root. The graph still has older node/blocker text saying activation awaits merge and completed owner gates retain blocker strings. Use the graph for discovery and cross-check the later ruling/register; do not infer that every node string is current authorization. [A4]

The September 22 D-GOV-44 notice is also bounded: this run keeps its pinned kernel Revision 1/workflow bytes; a later D-APP-131 owner rider is anticipated. D-GOV-44 does not rule an App packet, repair a deliverable or amend the App run's accepted basis. Future activations can pin the new shared method under their own authority. [A5]

For general App work, follow these live locations:

| Need | Root-relative location and interpretation |
| --- | --- |
| Recurrent procedure and current graph | projects/chirality-app-dev/loop/LOOP_INIT.md; graph state and recovery belong in the graph or its linked results. |
| Requirements and decomposition | projects/chirality-app-dev/docs/PRD.md and execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md beneath the same project; use applicable accepted scope amendments. These are entry pointers, not bodies audited in this task. |
| Deliverable scope and work | projects/chirality-app-dev/execution/PKG-*/1_Working/DEL-*/ScopeOfWork.md, _STATUS.md Remaining, MEMORY.md and dependency records. The graph does not replace these sources. |
| Decisions | projects/chirality-app-dev/execution/_Coordination/_DECISIONS/_REGISTER.md and the actual applicable decision/owner-direction record. |
| Dependency basis | projects/chirality-app-dev/execution/_Reconciliation/DepClosure/_LATEST.md; currently names CLOSURE_SCC-DECOMPOSE-SCA-APP-010_2026-09-05_1034. Resolve the accepted snapshot and local dependencies before dispatch. |
| Scope changes | projects/chirality-app-dev/execution/_ScopeChange/_LATEST.md; its state and later overlays have their own purpose and do not independently authorize implementation. |
| Reconciliation/reference binding | projects/chirality-app-dev/execution/_Reconciliation/References/AUTHORITY_CORPUS.json and reconcile_authority_corpus.py; current declared corpus is v23. |
| Durable undertaking evidence | projects/chirality-app-dev/execution/_Coordination/AgentRuns/<run>/ or the owning deliverable's _run_records/ and linked artifacts; keep one canonical copy. |

Sources: [A2, A6, A7]. The loop requires recovery against actual branch/worktree/evidence, checking whether interrupted workers or checks still own files/resources before reassignment. A completed graph stays selected until another undertaking is chosen; it supplies no authority to start a new phase. [A2]

APP-HOLD-1 remains mandatory before reliance, dispatch, CHECKING promotion or accepted-dependency consumption, irrespective of entry path. From the App root, use the actual operation and declared entry path:

~~~sh
python3 execution/_Scripts/app_hold.py check --operation <operation> --entry-path <declared-entry-path> --target <DEL-ID>
~~~

The only operation values are reliance, dispatch, checking-promotion and accepted-dependency-consumption. Repeat --target for additional targets. The registered integrity check is:

~~~sh
python3 execution/_Scripts/app_hold.py scan --require-register-match
~~~

The inspected register currently contains only its header. That observation does not replace an execution-time scan/check or eliminate separately named owner/dependency gates. DEL-09-07's structural/bootstrap and initialization exceptions are historical and retired; do not revive them from old guard compatibility code. [A8]

App does not require a separate new session narrative, handoff or loop receipt when the graph/results already carry continuation facts. Existing receipts and their integrity validator remain historical; before using an old receipt as a recovery cursor, the live loop requires the repository-root command below. Other selected workflows retain their own evidence contracts. [A2, A3]

~~~sh
python3 tools/validation/validate_app_dev_loop_receipts.py --repo-root .
~~~

## 2. Runtime: read the acceptance overlays before the old handoff text

Runtime's live entry remains projects/chirality-runtime/AGENTS.md then loop/LOOP_INIT.md; there is no Runtime init/ directory in the inspected tree. Load the actual invoked Root role, then read:

1. projects/chirality-runtime/execution/_Coordination/MIGRATION_ACCEPTANCE_2026-09-06.md, including its final D-GOV-43 supersession.
2. projects/chirality-runtime/docs/PRD_AUTHORITY.md, docs/PRD.md and execution/_Decomposition/_AUTHORITY.md; the former includes the later reading/re-hash overlay.
3. projects/chirality-runtime/execution/_Coordination/HANDOFF_STATE.md in full, especially the final September 12 supersession.
4. projects/chirality-runtime/README.md and execution/_Coordination/NOTICE_2026-09-12_ROOT_D-GOV-43_CODEX_HOST_REPLATFORM.md.
5. The applicable current brief, deliverable-local status/history and the packet overlays under execution/_Coordination/AgentRuns/RUNTIME_DGOV43_HOLD_CLOSURE_20260912/, especially PRD_REVISION.md and Impact_Assessment.md.

Sources: [R1–R4]. The loop also points at its newest receipt for continuity. The newest observed receipt is September 6; it is history interpreted through the later handoff/authority overlays, not a current supplier/conformance or nine-hold work queue. [R5]

The Runtime loop's published discovery recipe, from the repository root, is:

~~~sh
REPO_ROOT=$(git rev-parse --show-toplevel)
cd "$REPO_ROOT"
git fetch origin
git status --short --branch
git rev-parse HEAD origin/main
git rev-list --left-right --count HEAD...origin/main
python3 tools/practitioner_harness/harness.py status --project runtime
python3 tools/practitioner_harness/harness.py drift --project runtime
rg -n '^#|^##|^###' projects/chirality-runtime/loop/LOOP_RECEIPTS.md
rg -n 'Current State|Remaining|Depends|HELD' projects/chirality-runtime/execution/PKG-*/1_Working/DEL-*/_STATUS.md
~~~

These commands are quoted for the manual, not executed in this investigation. The practitioner harness parser has a runtime alias and implements status/drift. Its reports are generated views, not authority. A status-only scan must also read retirement history and governing overlays; all seven Runtime status headers remain INITIALIZED even though six carriers are retired in place. [R1, R4, R6, T1]

Runtime migration acceptance and effective product ownership remain accepted. D-GOV-43/A2 later changes the architecture to an application-owned Runtime service, closes nine obsolete held bindings, retires DEL-02-07 through DEL-02-12 in place, and revises DEL-02-06 through packet notes. The lifecycle vocabulary has no retirement state, so the status headers remain INITIALIZED. The frozen PRD, seven-carrier register and SOW bytes are deliberately preserved because Root pins them. The hold-closure packet explicitly records that _ScopeChange/_LATEST.md and MIGRATION_APPLICATION.md are unchanged; the pointer still naming SCA-003 is therefore not proof that SCA-004 did not occur. [R2–R4, R6]

Do not confuse closure by a ruling that retires the obsolete purpose with empirical satisfaction of the old held act. The hold map explicitly says no such named act was performed and none is now required for those retired bindings; the Tier-0 R16-B relationship remains separately disposed. These changes do not imply a new product release, operational registration, client adoption or lifecycle acceptance. [R4, R6]

Runtime's September 22 local-work-graph notice is intake only: the receiving loop decides whether/when to adopt or package the shared methods, and the notice leaves its accepted instruction basis, current graph, product guidance and method selection unchanged. Do not copy App's new no-receipt rule into Runtime. Runtime LOOP_INIT still requires actual checks and a durable project handoff under the governing run's own closeout contract; it explicitly claims no automatic Runtime receipt validator. [R1, R7]

Runtime's stable layouts are:

| Need | Root-relative location |
| --- | --- |
| Product source | projects/chirality-runtime/packages/contracts/src, core/src, daemon/src, client/src and cli/src. The daemon package name is retained although production hosting is now application-owned. |
| Compatibility source | projects/chirality-runtime/packages/engine-claude and engine-pi-omlx remain referenced by the current TypeScript build; their presence does not establish MVP qualification. |
| Tests | projects/chirality-runtime/tests/ and package-local tests; vitest.config.ts excludes execution/** because frozen evidence is not the executable test inventory. |
| Build output | Package-local dist/; for example core/tsconfig.json sets rootDir src and outDir dist. |
| Governed work | projects/chirality-runtime/execution/PKG-02_Runtime_Product/1_Working/DEL-*/ and their contracts/status/dependencies, read through current overlays. |
| Authority and evidence | projects/chirality-runtime/execution/_Decomposition/, _ScopeChange/, _Coordination/AgentRuns/ and owning deliverable records. |

Sources: [R1, R4, R8, T2]. The README identifies App as the only production consumer; Piping and local-model integration are deferred, and PEC compatibility remains unverified rather than an MVP prerequisite. Runtime owns sessions/turns/transport/delegation and the stock Codex child; client projects retain their UI/integration and client acceptance. [R3, R8]

## 3. Verified development command surface

Both package manifests require Node >=22.19.0. The App README recommends building Runtime before installing/running the frontend and rebuilding Runtime after changes before frontend integration tests. This exact source recipe is supported by both maintained manifests and the README: [T2, T3]

~~~sh
# From the repository root
cd projects/chirality-runtime
npm ci
npm run build
cd ../chirality-app-dev/frontend
npm ci
npm run dev
~~~

App's dev script starts Next on port 3000 and Electron together. Its source is frontend/src/ for UI/routes, frontend/electron/ for native lifecycle/hosting, frontend/packages/ for shared contracts, frontend/scripts/ for build/verification, and frontend/src/__tests__/ for tests. App's product guidance is projects/chirality-app-dev/instructions/AGENTS.md; the repository development instructions are projects/chirality-app-dev/AGENTS.md. Their applicability differs. [A1, T3]

| Working directory | Exact command | Current declared execution |
| --- | --- | --- |
| projects/chirality-runtime | npm run typecheck | tsc -b --pretty false |
| projects/chirality-runtime | npm test | vitest run |
| projects/chirality-runtime | npm run build | tsc -b |
| projects/chirality-app-dev/frontend | npm run typecheck | Frontend and Electron tsc checks, both --noEmit --incremental false |
| projects/chirality-app-dev/frontend | npm test | vitest run |
| projects/chirality-app-dev/frontend | npm run build | next build with telemetry disabled, then build:electron |
| projects/chirality-app-dev/frontend | npm run harness:validate:premerge | scripts/validate-harness-premerge.mjs; requires a reachable harness API |
| Repository root | python3 tools/practitioner_harness/harness.py self-check | Repo practitioner-harness surface audit |
| Repository root | python3 -m pytest -q tools/practitioner_harness | Practitioner-harness tests |
| projects/chirality-app-dev | python3 execution/_Scripts/app_hold.py scan --require-register-match | Registered App hold/register-integrity check |

Sources: [A8, T1–T4]. Static verification parsed both package manifests and both software-workflow.json profiles, resolved every registered check's cwd and command target, and confirmed seven App checks and two Runtime checks are structurally resolvable. No profile command ran. Runtime registers typecheck and unit as always checks; App registers harness-self-check and app-hold-integrity as always checks plus path-sensitive bindings. App AGENTS additionally requires the repo self-check and practitioner pytest for every tranche at closeout, and product-source typecheck/tests/build/premerge plus the fresh read-only TASK + software-code-review path. A profile is not permission to omit a separate governing requirement. [A1, T4]

Premerge details matter: the profile owns a Next dev service on an automatic port, with CHIRALITY_HARNESS_PROVIDER=stub and telemetry disabled; it injects HARNESS_BASE_URL into the check. A bare npm premerge invocation does not start that service. The harness README documents HARNESS_BASE_URL and HARNESS_PROJECT_ROOT. Stop an independently running dev server before build/package/premerge unless the selected command owns its lifecycle; avoid competing .next writers. The premerge script's stable summary is frontend/artifacts/harness/section8/latest/summary.json; Section 9 has its own sibling summary. [T4–T6]

Packaging is a separate scoped undertaking. Useful executable names are instruction-root:prepare, runtime:build, build, desktop:prepare, desktop:pack, desktop:dist, desktop:verify-dependencies, desktop:verify-codex-pin and instruction-root:integrity, all in the frontend manifest. desktop:pack and desktop:dist consume built/staged inputs; they do not build those inputs. desktop:prepare chains staging, Runtime build, App build and packing, but the additional package verifiers are separate script names. pack-electron.mjs explicitly checks built Electron/Runtime bundles, staged instruction manifest and .next/BUILD_ID, and passes --publish never. Signing is disabled unless an explicit signing identity is supplied. These command capabilities do not authorize signing, notarization, distribution or publication. [T3, T7]

Relevant App output locations, all relative to the repository root, are projects/chirality-app-dev/frontend/.next/, projects/chirality-app-dev/frontend/dist-electron/, projects/chirality-app-dev/frontend/dist-runtime/, projects/chirality-app-dev/frontend/dist/ and projects/chirality-app-dev/frontend/artifacts/harness/. Governance evidence belongs with the undertaking or deliverable; generated test/build output is derivative evidence, not lifecycle or release acceptance. Native-host behavior needs native evidence, and required unavailable evidence remains HOST_RERUN_REQUIRED rather than a waived pass. [A1, T5, T7]

## 4. Authority/adoption and stale-launcher cautions to carry into the manual

| Trap | Correct reading and evidence |
| --- | --- |
| App NEXT_INSTANCE_PROMPT.md says its replacement is init/init-prompt.md and newest WORKPLAN_*.md; body revives June autonomous queues, old providers and CHANGE handoffs. | Its own banner and live _LATEST mark it historical. The current launcher is init/dev-loop-init-prompt.md, with LOOP_INIT and the selected graph. Do not revive the old queues or recreate NEXT_INSTANCE_STATE.md. [A2, A6, H1] |
| App graph carries old activation/gate blocker strings and a historical Claude/Opus topology. | Later D-APP-130 controls the current R5 frontier. The old topology records that run, not a model mandate for this Codex task or a general compulsory manager roster. App AGENTS delegates model direction per session and does not require a package-per-manager roster. [A1, A4] |
| A Root method notice appears in a project. | Inspect the notice's actual disposition. App's September 22 notice applies its loop changes but preserves the existing whole-corpus method; Runtime's equivalent is intake only. September 9 notices themselves explicitly do not adopt/repin/qualify/release either product. [A3, R7, H2] |
| App AGENTS workflow-authoring paragraph says write canonical packages and refresh the catalog. | The current product guide and September 13 Runtime notice specify draft-review-registration first: .chirality/workflow-drafts/<name>/WORKFLOW.md, human review and Register workflow; .chirality/workflows remains execution storage. Root AGENTS agrees. Do not teach catalog refresh alone as the current App creation path. [G1, H3] |
| App authority-corpus notices mention v20/v21 or say no drift. | These are dated assertions. The inspected current corpus declares v23. The September 19 notice records known CONTRACT/SPEC/PRD drift for later reconciliation, also carried by the selected graph. This investigation did not recompute current drift or authorize bump/apply. [A3, A7] |
| Runtime PRD or registers say GATE3_REVIEW_NOT_ACCEPTED; handoff/coordination say seven carriers, nine holds and daemon/private supplier work. | Migration acceptance establishes later ownership; D-GOV-43 supersession plus the SCA-004 packet revises their reading. Frozen wrappers/registers/SOWs remain preserved and source-qualified; later overlays do not silently repin another contract. [R2–R6] |
| Runtime _ScopeChange/_LATEST is SCA-003; newest receipt is September 6. | Those preserved records are not the complete current authority chain. Impact_Assessment explicitly explains why Root-pinned pointers/bytes were not rewritten. Read September 12 overlays and the actual current brief. [R4–R6] |
| Runtime HANDOFF says future merges need new owner direction; historical receipts say no self-merge. | Root standing Git authority and the live Runtime loop supersede per-merge defaults within authorized scope after actual-candidate CI and independent review. Explicit holds still prevail; Git is not product acceptance. This task itself has no Git authority under its narrower brief. [G1, R1, R5] |
| App BUILD_AND_RELEASE §3 says Node >=20. | The live frontend and Runtime manifests require >=22.19.0. Prefer the maintained executable manifests and surface the discrepancy. [T2, T3, T5] |
| App build command table says desktop:pack builds; it also carries older release/provider prose. | The current manifest and pack script require prebuilt inputs. The guide itself says scripts/manifests prevail on implementation discrepancies; §8.1 retires the old Stage 9–13 supplier packaging spine. [T3, T5, T7] |
| Retained agentsdk/Pi scripts or tests imply supported release engines. | The harness README explicitly identifies agentsdk scripts and Anthropic proof as compatibility history, not MVP evidence. Runtime may retain compatibility packages while Codex remains the sole App MVP engine. [A1, R8, T6] |
| Passing tests, source merge, package build, initialized status, graph done or migration accepted means acceptance/release. | Keep evidence, source-control integration, owner acceptance, lifecycle issuance, client adoption and release acts distinct. Existing App release history does not authorize another release. [A1, R1, R4, T5] |

The current implementation boundary is App -> application-owned Runtime service -> stock Codex App Server; ordinary users do not start a separate daemon. Runtime package names containing daemon and old evidence do not revive LaunchAgents, second sockets, supplier admission or retired conformance gates. [A1, R3, R8, T3]

## 5. Gaps and verification limits

- Current App corpus drift was located in explicit live navigation/notice records, not freshly recomputed. No reference corpus was bumped or applied.
- No actual Git/GitHub state was refreshed or checked, so the documentary merge references and supplied repository basis are cited as recorded facts, not a fresh remote-state claim.
- No complete source-level architecture audit, test execution, packaging trial, owner-live acceptance check or exhaustive notice-history audit was performed. Maintained manifests and relevant script excerpts verify command spelling, cwd, declared behavior and prerequisites only.
- Source inventories were bounded to current entry files, shallow package/test listings and explicit links. One early filename discovery was too broad and produced truncated historical path listings; no historical run trees were read wholesale. Subsequent discovery followed live pointers.
- Application code and inherited scope may require additional contract/decision reads for an actual implementation brief. A general manual should tell agents where to recover those exact warrants, not freeze today's queue or imply new work is authorized.

## Evidence citations

All paths below are relative to the repository root; line numbers refer to the bytes hashed in the companion JSON.

- G1: AGENTS.md, “Roles” lines 17–34, “Skills and workflows” lines 79–97 and 116–130, “Execution and governance” lines 157–177 and 229–242; agents/AGENT_TASK.md lines 5–33; plans/evidence/2026-09-22_alignment_manual/BRIEF.md lines 3–20.
- A1: projects/chirality-app-dev/AGENTS.md, “Path Anchors” lines 14–21, “Active Roles” lines 31–46, “Skills, Workflows, and Context” lines 48–99, “Execution attribution” lines 101–123, “Project-Wide Execution Discipline” lines 125–179, “Work graph continuity and bounded reconciliation” lines 181–210, “Development boundaries” lines 212–246, “Development checks and evidence” lines 249–285, “Closeout And Git Discipline” lines 346–365, “Shared Runtime Boundary” lines 368–389.
- A2: projects/chirality-app-dev/init/dev-loop-init-prompt.md lines 1–15; projects/chirality-app-dev/loop/LOOP_INIT.md lines 1–111.
- A3: projects/chirality-app-dev/execution/_Coordination/NOTICE_2026-09-19_APP_LOOP_WORKGRAPH.md lines 9–31; NOTICE_2026-09-19_LOOP_CLARIFICATIONS.md lines 10–22; NOTICE_2026-09-22_ROOT_LOCAL_WORK_GRAPH_METHODS.md lines 14–25 in the same directory.
- A4: projects/chirality-app-dev/execution/_Coordination/AgentRuns/HELP-HUMAN-APP-20260921-CONCORDANCE/WORK_GRAPH.json lines 3–16, 43–75, 112–144; projects/chirality-app-dev/execution/_Coordination/_DECISIONS/_REGISTER.md lines 153–155; D-APP-130_RULING_R4_GATE_RUN_D128_2026-09-22.md in that directory, “Recorded outcome” and “Consequences” lines 25–56.
- A5: projects/chirality-app-dev/execution/_Coordination/NOTICE_2026-09-22_ROOT_D-GOV-44_CONCORDANCE_CLAIM_GRANULARITY.md lines 3–11.
- A6: projects/chirality-app-dev/execution/_Coordination/_LATEST.md lines 3–27 and 51–82; _COORDINATION.md in that directory lines 3–15, 21–30 and 45–117.
- A7: projects/chirality-app-dev/execution/_Reconciliation/DepClosure/_LATEST.md lines 1–2; projects/chirality-app-dev/execution/_Reconciliation/_LATEST.md lines 1–12; projects/chirality-app-dev/execution/_ScopeChange/_LATEST.md lines 3–44; projects/chirality-app-dev/execution/_Reconciliation/References/AUTHORITY_CORPUS.json lines 2–16 and 377–394; _README.md beside it lines 23–67.
- A8: projects/chirality-app-dev/AGENTS.md, “APP-HOLD-1 Reliance Preflight” lines 310–344; projects/chirality-app-dev/execution/_Scripts/app_hold.py argument parser lines 955–965; projects/chirality-app-dev/execution/_Coordination/APP_HOLD_REGISTER.csv line 1.
- R1: projects/chirality-runtime/AGENTS.md lines 1–7; projects/chirality-runtime/loop/LOOP_INIT.md lines 3–34.
- R2: projects/chirality-runtime/execution/_Coordination/MIGRATION_ACCEPTANCE_2026-09-06.md lines 3–24; projects/chirality-runtime/docs/PRD_AUTHORITY.md lines 3–7 and 34–50; projects/chirality-runtime/execution/_Decomposition/_AUTHORITY.md lines 3–7.
- R3: projects/chirality-runtime/execution/_Coordination/HANDOFF_STATE.md lines 3–23; projects/chirality-runtime/execution/_Coordination/NOTICE_2026-09-12_ROOT_D-GOV-43_CODEX_HOST_REPLATFORM.md lines 3–43.
- R4: projects/chirality-runtime/execution/_Coordination/AgentRuns/RUNTIME_DGOV43_HOLD_CLOSURE_20260912/PRD_REVISION.md lines 3–39; Impact_Assessment.md beside it lines 7–46.
- R5: projects/chirality-runtime/loop/LOOP_RECEIPTS.md, Receipts 1–3, lines 3–25; projects/chirality-runtime/execution/_Coordination/_COORDINATION.md lines 3–10.
- R6: projects/chirality-runtime/execution/_Decomposition/HOLD_SUCCESSOR_MAP.csv lines 2–11; RUNTIME_DELIVERABLE_REGISTER.csv beside it lines 1–8; projects/chirality-runtime/execution/_ScopeChange/_LATEST.md lines 3–12; each projects/chirality-runtime/execution/PKG-02_Runtime_Product/1_Working/DEL-02-06* through DEL-02-12*/_STATUS.md lines 3–9.
- R7: projects/chirality-runtime/execution/_Coordination/NOTICE_2026-09-22_ROOT_LOCAL_WORK_GRAPH_METHODS.md lines 14–24.
- R8: projects/chirality-runtime/README.md, “Architecture” lines 16–51, “Development” lines 72–85, “Packages” lines 87–102, “Retirement note” lines 104–123 and “Reference” lines 125–137; projects/chirality-runtime/docs/PRD.md “Purpose and ownership” lines 7–9, read with R2/R4.
- T1: tools/practitioner_harness/harness.py lines 39–43, 76–87 and 190–208; tools/practitioner_harness/README.md “Write posture” lines 65–79 and “Tests” starting at line 543.
- T2: projects/chirality-runtime/package.json lines 6–23; software-workflow.json lines 5–25; tsconfig.json lines 3–10; vitest.config.ts lines 3–7; packages/core/tsconfig.json lines 2–8; packages/daemon/package.json lines 2–5 and 28–30.
- T3: projects/chirality-app-dev/README.md lines 13–28 and 30–63; projects/chirality-app-dev/frontend/package.json lines 11–46, 49–54, 95–97 and 109–150; bounded source/test filename inventory.
- T4: projects/chirality-app-dev/software-workflow.json lines 5–42; projects/chirality-runtime/software-workflow.json lines 5–35.
- T5: projects/chirality-app-dev/docs/BUILD_AND_RELEASE.md “Authority Boundary” lines 17–27, “Current Baseline” lines 31–43, “Local Command Map” lines 47–68, “Evidence Bundles” lines 78–92, “Artifact Locations” lines 94–113 and “Packaging Procedure” lines 127–162; projects/chirality-app-dev/docs/VALIDATION_STRATEGY.md lines 11–27, 40–61, 78–92 and 102–135; projects/chirality-app-dev/docs/RELEASE_QUALITY_GATES.md lines 13, 128–135 and 152.
- T6: projects/chirality-app-dev/frontend/docs/harness/README.md lines 3–13, 17–43, 51–78 and 94–104; projects/chirality-app-dev/frontend/scripts/validate-harness-premerge.mjs lines 125–150.
- T7: projects/chirality-app-dev/frontend/scripts/pack-electron.mjs lines 9–34, 64–94, 102–139 and 177–195; frontend/package.json lines 38–43 under the same project.
- H1: projects/chirality-app-dev/execution/_Coordination/NEXT_INSTANCE_PROMPT.md, historical banner lines 3–9, historical entry lines 11–27, historical execution rules lines 86–98; current replacement described by A2/A6.
- H2: projects/chirality-app-dev/execution/_Coordination/NOTICE_2026-09-09_CHIRALITY_V3_ROLE_SKILL_WORKFLOW_ADOPTION.md lines 10–19; projects/chirality-runtime/execution/_Coordination/NOTICE_2026-09-09_CHIRALITY_V3_ROLE_SKILL_WORKFLOW_ADOPTION.md lines 10–19. September 10 method/engine notices were also read; App's later top revision explicitly supersedes the former bundled-only skill restriction, while the Runtime copy remains a dated coordination notice.
- H3: projects/chirality-app-dev/AGENTS.md lines 78–81; projects/chirality-app-dev/instructions/AGENTS.md “Help useful methods endure” lines 122–138; projects/chirality-runtime/execution/_Coordination/NOTICE_2026-09-13_WORKFLOW_DRAFT_REVIEW.md lines 3–5; Root AGENTS.md lines 121–130.
