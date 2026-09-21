# PREGATHER — DEL-02-02 (Work/Agents Coordination, Workbench, and Pipeline UX; applied name: Right-Panel Coordination, Workflows, and Proposal UX)

- Run: `RUN_D128_CONCORDANCE_2026-09-21_1614Z`, R2 PKG-02 pre-gather (TASK, Type 2). Evidence locations only: no dispositions, no alignment judgments, no CauseTags.
- Basis: frozen tree at `00115c719`. Deliverable folder `projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-02_Workbench_and_Pipeline_Selection_UX/` (`ScopeOfWork.md` 36,998 B; `_STATUS.md` 17,461 B).
- Units indexed in `R1_INVENTORY/CLAIM_INDEX.csv` for DEL-02-02: **38** (SEC 5, CLM 28, REMTXT 2, REM 3). All 38 are covered below, in index order.
- Units with `NO_CANDIDATES` (no code or test candidate; decision records may still be listed): **14**. They are SEC-5, CLM-001, CLM-002, CLM-004, CLM-006, CLM-007, CLM-008, CLM-015, CLM-016, CLM-017, CLM-021, CLM-022, CLM-028 and REMTXT-2.
- Method:
  1. Read SoW L1–520 and `_STATUS.md` in full.
  2. Summarized `HINTS/DEL-02-02.csv` (596 data rows) per ClaimKey, token and path with python3. Most hits are generic path tokens (`docs/PRD.md`, `_CONTEXT.md`, `DECOMP` …) in unrelated tests and scripts (`harness-section9-manifest.json`, `deliverables-route.test.ts`, `run-dapp52-live-llm-demo.ts`). They were used only as a starting point.
  3. Grepped `EVIDENCE_PACK/REACHABILITY.csv`, `TOUCHED_PATHS.csv` and `DECISION_HITS.csv`.
  4. Traced the static imports and the render path from `frontend/src/app/{page,chat/page,pipeline/page,workbench/page}.tsx` through `woven-dialogue-route.tsx` and `woven-dialogue-shell.tsx`.
  5. Grepped the importers of each candidate symbol under `frontend/src` and `frontend/electron`, excluding `__tests__`.
  6. Listed test `it(` case names in the candidate test files.
  7. Ran a light grep of the decision register.
  8. Did not read or search `projects/chirality-runtime/execution/**`, `R0_CALIBRATION/**` or other R2 folders.
- TOUCHED_PATHS: none of the 26 touched paths is a frontend path. Only runtime packages, docs and exports appear there. **No candidate below carries a `TOUCHED(...)` mark.**

## Candidate bundles (defined once, cited by ID in the unit sections)

All paths are repo-relative. `REACH=` is copied from `EVIDENCE_PACK/REACHABILITY.csv`. `SYMBOL-REACH` records facts found by import and render tracing at `00115c719`.

**Render-path fact (applies to WB, PL, DA, TS, QI).**
- `projects/chirality-app-dev/frontend/src/components/woven-dialogue/woven-dialogue-route.tsx:12 WovenDialogueRoute` executes `void legacy;` (L18) and always returns `<WovenDialogueShell defaultSurface=…/>`. The `legacy` prop is never rendered.
- `woven-dialogue-shell.tsx:77 WovenDialogueShell(_props)` ignores `defaultSurface` and hard-codes `data-woven-surface="dialogue"` (L822).
- `LoopShell` (`app/chat/page.tsx`), `PortalLoopShell` (`app/page.tsx`) and `LoopTertiaryShell` (`app/workbench/workbench-client.tsx:12`, `app/pipeline/pipeline-client.tsx:12`) are therefore constructed only as unrendered `legacy` props.
- `shell/tertiary-sidebar-tabs.tsx:7 createTertiarySidebarTabs` (the only non-test importer of `PipelineSurface` and `WorkbenchSurface`) is called only inside those three legacy shells.
- The `/workbench` and `/pipeline` URL routes exist and render the same Woven dialogue shell.

- **[WB] Workbench surface**
  - `projects/chirality-app-dev/frontend/src/components/workbench/workbench-surface.tsx`, REACH=LIVE (chain `app/chat/page.tsx>shell/loop-shell.tsx>shell/tertiary-sidebar-tabs.tsx>…`). SYMBOL-REACH: module LIVE via import only; `WorkbenchSurface` is not rendered from any entry point (searched `workbench-surface`, `createTertiarySidebarTabs`, `LoopShell|LoopTertiaryShell|PortalLoopShell` under `frontend/src`; the only render sites are the unrendered `legacy` props).
  - Symbols:
    - `:66 normalizeAgent`
    - `:74 WorkbenchLifecycleTransitionForm`
    - `:173 WorkbenchSurface`
    - `:176-178` query reads `agent`, `row` (default `NORMATIVE`) and `column` (default `GUIDING`)
    - `:263-264` fetch status and dependencies
    - `:292 transitionEnabled = canAgentTransitionLifecycle(agent)`
    - `:297 requiresApprovalSha`
    - `:385-394` SHA guard and HUMAN actor lock
    - `:415` "Active Agent Context"
    - `:441` "Deliverable Contracts (Read-Only)"
    - `:480-486` empty or no-data states
    - `:592` folded Documents block
- **[PL] Pipeline surface**
  - `projects/chirality-app-dev/frontend/src/components/pipeline/pipeline-surface.tsx`, REACH=LIVE (same chain as WB). SYMBOL-REACH: module LIVE via import only; `PipelineSurface` and `PipelineLifecycleTransitionForm` are not rendered from any entry point (same search as WB).
  - Symbols:
    - `:28 OperativeCategory`
    - `:53 CATEGORY_ORDER`
    - `:70 DECOMP_OPTIONS` (options with an `enabled` flag)
    - `:109 normalizeCategory`
    - `:122 renderOptionLabel` ("(coming soon)")
    - `:126 PipelineLifecycleTransitionForm`
    - `:230 PipelineSurface`
    - `:242/340 sanitizeTaskSelection` use
    - `:295-307` reset on `projectRoot` change
    - `:436-470` scope-scan effect
    - `:589 submitScaffold`
    - `:635/658/681/836` DECOMP, PREP, TASK and AUDIT cards
    - `:686` "Task agent"
    - `:807` "KNOWLEDGE_TYPES scope mode is unavailable…"
    - `:869` "Execution Root Scaffold"
    - `:1001` "Deliverable Contracts"
    - `:511/541/562` approval-SHA guard
- **[DA] Deliverable API client**
  - `projects/chirality-app-dev/frontend/src/lib/workspace/deliverable-api.ts`, REACH=LIVE (chain `…tertiary-sidebar-tabs.tsx>pipeline-surface.tsx>deliverable-api.ts`). SYMBOL-REACH: its only non-test importers are `pipeline-surface.tsx` and `workbench-surface.tsx`, neither of which is rendered. The consumed routes `projects/chirality-app-dev/frontend/src/app/api/working-root/deliverable/{status,status/transition,dependencies}/route.ts` are REACH=LIVE as API entry points. No rendered UI caller of those three routes was found (searched `working-root/deliverable/` in non-test `src`; the other hit, `shell/document-view.tsx`, uses `deliverable/content`).
  - Symbols:
    - `:8 HUMAN_GATE_TARGETS` (CHECKING, ISSUED)
    - `:9 LIFECYCLE_TRANSITION_AGENTS` (CHANGE, WORKING_ITEMS)
    - `:135 nextLifecycleTargets`
    - `:139 requiresApprovalShaForTarget`
    - `:143 canAgentTransitionLifecycle`
    - `:186 summarizeDependencyRows`
    - `:214 fetchDeliverableStatus`
    - `:226 transitionDeliverableStatus`
    - `:242 fetchDeliverableDependencies`
- **[TS] Task-scope helpers**
  - `projects/chirality-app-dev/frontend/src/lib/workspace/task-scope.ts`, REACH=LIVE (chain `app/layout.tsx>components/workspace/deliverables-provider.tsx>task-scope.ts`). SYMBOL-REACH: `deliverables-provider.tsx:13` imports only `buildDeliverableCompositeKey`. `normalizeTaskScopeMode` and `sanitizeTaskSelection` are imported only by `pipeline-surface.tsx`, which is not rendered.
  - Symbols: `:1 TaskScopeMode`, `:14 buildDeliverableCompositeKey`, `:18 normalizeTaskScopeMode`, `:29 sanitizeTaskSelection`.
- **[QI] Pipeline dispatch contract**
  - `projects/chirality-app-dev/frontend/src/lib/pipeline/pipeline-dispatch-contract.ts`, REACH=TEST_ONLY.
  - Symbols: `:111 normalizePipelineCategory`, `:120 validatePipelineDispatchIntent`, `:246 mergePipelineQueryParameters`.
  - SYMBOL-REACH: TEST_ONLY; no non-test importer.
- **[RT] Legacy routes and shells**
  - `projects/chirality-app-dev/frontend/src/app/workbench/page.tsx` and `…/workbench-client.tsx:7`, REACH=LIVE.
  - `projects/chirality-app-dev/frontend/src/app/pipeline/page.tsx` and `…/pipeline-client.tsx:7`, REACH=LIVE.
  - `projects/chirality-app-dev/frontend/src/components/shell/loop-tertiary-shell.tsx`, `…/loop-shell.tsx`, `…/portal-loop-shell.tsx` and `…/tertiary-sidebar-tabs.tsx`, REACH=LIVE.
  - `projects/chirality-app-dev/frontend/src/components/portal/agent-matrix.tsx`, REACH=LIVE.
  - SYMBOL-REACH: the route pages render `WovenDialogueRoute`. The loop and tertiary shells and `AgentMatrix` are constructed only as unrendered `legacy` props.
- **[SH] Woven dialogue shell and right panel**
  - `projects/chirality-app-dev/frontend/src/components/woven-dialogue/woven-dialogue-shell.tsx`, REACH=LIVE. SYMBOL-REACH: rendered from `app/chat/page.tsx`, `app/page.tsx`, `app/workbench/page.tsx` and `app/pipeline/page.tsx` through `WovenDialogueRoute`.
    - Symbols: `:77 WovenDialogueShell`, `:101 coordinationView ('session'|'agents')`, `:369 buildRecordedAgentHierarchy(...)`, `:408 returnToPrimaryDialogue`, `:424` reads only the `agent` query param, `:560 guardRecordedSessionSelection`, `:822 data-woven-surface="dialogue"`, `:997 <RightPanel>`, `:1019 <CoordinationPanel>`, `:1024 <SelectedSessionReplayLens … onReturnToPrimary>`.
  - `…/woven-dialogue/right-panel.tsx:20`, REACH=LIVE. Tabs are Files, Plan, Workflows, Agents and Activity. `:190` Workflows view renders `MethodLibraryView`. SYMBOL-REACH: rendered from SH:997.
- **[AG] Agents coordination**
  - `projects/chirality-app-dev/frontend/src/components/woven-dialogue/coordination-panel.tsx:24 CoordinationPanel`, REACH=LIVE. SYMBOL-REACH: rendered from SH:1019.
    - `:38/68` shows native children derived from events.
    - `:80` renders `AgentsProjection`.
  - `…/woven-dialogue/agents-projection.tsx:109 AgentsProjection`, REACH=LIVE. SYMBOL-REACH: rendered from `coordination-panel.tsx:80`.
    - `:30 recordedAgentLabel`
    - `:34 relationshipLabel`
    - `:45 SessionCard`
  - `projects/chirality-app-dev/frontend/src/lib/woven-dialogue/recorded-agent-hierarchy.ts:126 buildRecordedAgentHierarchy`, REACH=LIVE. SYMBOL-REACH: called at SH:369.
    - `:12 'UNKNOWN'`
    - `:50 currencyFromEvidence`
    - `:201` conflicting-session currency
  - `…/lib/woven-dialogue/guarded-session-selection.ts`, REACH=LIVE. SYMBOL-REACH: `guardRecordedSessionSelection` is called at SH:560.
    - `:59 guardRecordedSessionSelection`
    - `:159 returnToPrimaryDialogue`
  - `…/components/woven-dialogue/selected-session-replay-lens.tsx:328 SelectedSessionReplayLens`, REACH=LIVE. SYMBOL-REACH: rendered at SH:1024.
  - `…/lib/woven-dialogue/operator-projection.ts`, REACH=LIVE (via `selected-session-replay.ts`). SYMBOL-REACH: not checked.
  - `…/lib/woven-dialogue/contracts.ts`, REACH=UNREACHED (type-only import). SYMBOL-REACH: not checked.
- **[WP] Work projection**
  - `projects/chirality-app-dev/frontend/src/components/woven-dialogue/work-projection.tsx:14 WorkProjection`, REACH=TEST_ONLY. SYMBOL-REACH: no non-test importer.
- **[WF] Workflows**
  - `projects/chirality-app-dev/frontend/src/components/woven-dialogue/workflows-view.tsx:7 WorkflowsView`, REACH=TEST_ONLY. Its fetch of `/api/working-root/workflow` is at `:13`.
  - `…/woven-dialogue/workflow-detail.tsx`, REACH=TEST_ONLY.
  - SYMBOL-REACH: no non-test importer of either.
  - `…/woven-dialogue/method-library-view.tsx:69 MethodLibraryView`, REACH=LIVE. SYMBOL-REACH: rendered from `right-panel.tsx:190`.
  - `…/woven-dialogue/workflow-draft-review.tsx:9 WorkflowDraftReview`, REACH=LIVE. SYMBOL-REACH: reached through `method-library-view`; render not checked.
  - `projects/chirality-app-dev/frontend/src/lib/shell/workflow-library.ts:38 groupWorkflowLibrary`, REACH=LIVE. SYMBOL-REACH: not checked.
  - `projects/chirality-app-dev/frontend/src/app/api/working-root/workflow/route.ts:7 GET`, REACH=LIVE (API entry, GET only). SYMBOL-REACH: its only UI fetcher, `workflows-view.tsx`, is TEST_ONLY.
  - `…/workflow/workflow-store.ts`, REACH=LIVE. Symbols: `:11 validateWorkflowName`, `:34 .chirality/workflows/${name}`, `:50 listWorkflowFiles`, `:83 readWorkflowFile`.
  - `…/workflow/workflow-read-contract.ts`, REACH=UNREACHED.
  - `projects/chirality-app-dev/frontend/src/lib/workspace/governed-workflow.ts`, REACH=TEST_ONLY. SYMBOL-REACH: no non-test importer.
    - `:85 validateGovernedWorkflow`
    - `:136 parseGovernedWorkflow`
    - `:212 nextWorkflowGate`
    - `:219 advanceWorkflowAtGate`
    - `:230 bindWorkflowContent`
    - `:236 workflowSourceCurrency`
  - `projects/chirality-app-dev/frontend/src/app/api/working-root/workflow-drafts/route.ts` and `workflow-draft-store.ts`, REACH=LIVE.
- **[PC] Proposal card**: no `ProposalCard`, `proposal-card` or `proposal.*` consumer was found in non-test `frontend/src`. The only hit is a comment at `projects/chirality-app-dev/frontend/src/lib/woven-dialogue/woven-workspace-state.ts:532`. `projects/chirality-runtime/packages/contracts/src/harness/operation-proposal.ts` is REACH=LIVE; SYMBOL-REACH: not checked.
- **[RL] Role and posture labels**
  - `projects/chirality-app-dev/frontend/src/lib/consent/hosted-engine-consent-port.ts`, REACH=LIVE. Symbols: `:42 PRODUCT_POSTURE_LABEL = 'Opt-in Preview'`, `:188 ROLE_NOT_MECHANICALLY_ENFORCED_LABEL`, `:23` K-ROLE-2 comment on Agent 0/1/2. The labels are consumed by the DEL-02-05 settings surface `components/settings/account-consent-settings.tsx` (REACH=LIVE). SYMBOL-REACH: no use in the woven-dialogue right-panel or agents components (searched both label strings and "Who is working" in non-test `src`; "Who is working" has no hit).
  - `projects/chirality-app-dev/frontend/src/lib/harness/managed-delegation.ts:301` and `…/subagent-governance.ts:223` carry Agent 0/1/2 delegation text, REACH=LEGACY_ONLY.

**Test bundles** (test file :: case, all under `projects/chirality-app-dev/frontend/src/__tests__/`).
- **T-WB** `components/workbench-surface.test.ts`:
  - :41 "renders unsupported agents as read-only while preserving matrix context"
  - :59 "mounts the folded Documents block inside the Workbench surface"
  - :68 "keeps the Documents block mounted for read-only agents"
  - :82 "requires approval SHA and locks actor choice to HUMAN for human-gated transitions"
  - :110 "keeps the approval SHA optional for non-human-gated transitions"
- **T-PL** `components/pipeline-surface.test.ts`:
  - :63 "renders operative category controls, TASK split selectors, and disabled coming-soon options"
  - :83 "renders valid TASK knowledge-type deep links with required target deliverables"
  - :116 "resets stale TASK knowledge-target deep links during initial render"
  - :150 "requires approval SHA and locks actor choice to HUMAN …"
  - :184 "keeps approval SHA optional and submission active for ordinary transitions"
- **T-TS** `lib/task-scope-selection.test.ts`:
  - :9 "builds pkg::id deliverable keys"
  - :15 "normalizes KNOWLEDGE_TYPES mode only when marker is enabled"
  - :22 "clears stale deliverable keys …"
  - :43 "resets KNOWLEDGE_TYPES selection when the decomposition marker is absent"
  - :69 "clears stale knowledge-type target keys …"
  - :95 "preserves valid knowledge-type target keys"
- **T-DA** `lib/workspace-deliverable-api.test.ts`:
  - :70 "summarizes blocker-subset rows …"
  - :128 "returns allowed forward lifecycle targets per state"
  - :134 "flags approvalSha requirements for human-gated targets"
  - :141 "limits lifecycle transition controls to approved agents"
  - :148 "loads lifecycle status snapshots from working-root contracts route"
  - :177 "throws typed client errors …"
  - :202 "sends transition payloads …"
  - :245 "loads dependency register snapshots …"
  - Also `api/working-root/deliverable-contracts.test.ts` (case names not listed).
- **T-QI** `lib/pipeline-dispatch-contract.test.ts`:
  - :21 "preserves the exact DECOMP/PREP/TASK/AUDIT taxonomy and option states"
  - :54 "returns inert data for an admitted deliverable-scoped TASK intent"
  - :88 "rejects disabled options without hiding them"
  - :113 "requires exact recorded scope and a target for knowledge-type TASK intent"
  - :146 "preserves persona, matrix, and unknown query parameters while patching Pipeline intent"
- **T-RT** route tests. Both files mock `WovenDialogueShell` to echo `defaultSurface` (route test L6-10; loop-tertiary test L5-9):
  - `components/woven-dialogue-route.test.tsx`: :13 "renders Woven Dialogue by default"; `it.each(['workbench','pipeline'])` "opens /%s in the continuing conversation surface"; :31 "does not expose the retired execution surface through a legacy route prop".
  - `components/loop-tertiary-routes.test.ts`: :14 "opens the Workbench deep link in the continuing conversation"; :22 "opens the Pipeline deep link …".
- **T-AG** agents and coordination tests:
  - `components/agents-projection.test.tsx`: :87 "shows recorded agent type, persona, and human-readable tree relationships"; :98 "omits unknown type and persona without inferring either"; :107 "uses plain relationship-unavailable language for detached agents"; :117 "does not expose runtime, provenance, identifier, evidence, or diagnostic metadata"; :125 "keeps refresh and error access, including the loading guard"; :164 "preserves selected and disabled session selection …".
  - `lib/recorded-agent-hierarchy.test.ts`: :5 "builds hierarchy edges only from exact recorded parentSessionId values"; :39 "retains exact unresolved parent identifiers …"; :59 "keeps cyclic parentage inspectable …"; :82 "does not infer role, status, parentage, model, or currency …"; :101 "marks duplicate session records conflicting …".
  - Also `lib/guarded-session-selection.test.ts`, `lib/operator-projection.test.ts` and `components/native-coordination.test.tsx` (case names not listed).
- **T-SH** shell and right-panel tests:
  - `components/woven-dialogue-shell.test.tsx`: :169 "preserves controller identity and focusable composer through replay, panel controls, resize, and return"; :233 "… while primary stays mounted"; :316 "continues a compatible v3 replay in the mounted primary dialogue and leaves legacy replay read-only".
  - `components/woven-right-panel.test.tsx`: :103 "… redirects a saved Skills view to Workflows".
- **T-WP** `components/woven-dialogue-work-projection.test.tsx`: :11 "renders an honest empty state instead of synthesizing work from dialogue"; :19 "renders only supplied evidence with visible authority, provenance, and currency"; :57 "discloses unrecorded optional evidence without inferring assignments or status".
- **T-WF** workflow tests:
  - `components/woven-workflows.test.tsx` (4 cases on list, open, stale-folder abort, errors and retry, and safe Markdown).
  - `api/working-root-workflow.test.ts`: :31 "is GET only and a missing workflow directory stays empty without creating it"; :35 "lists actual file metadata and opens exact bytes with hash and no inferred workflow state"; plus 5 containment and limit cases.
  - `lib/governed-workflow.test.ts`: :36 "round trips a derivative roadmap with source metadata …"; :110 "advances only at the next human gate, with attribution …"; :131 "cannot advance a roadmap without a human gate"; :137 "binds a detached copy …"; :150 "reports source currency without rewriting either source".
  - Also `components/method-library-view.test.tsx`, `components/workflow-draft-review.test.tsx`, `api/working-root/workflow-drafts*.test.ts` and `lib/workflow-library.test.ts`.

**Deliverable-local evidence records** (frozen tree, deliverable `_run_records/`):
- `T1_MERGED_RECONCILIATION_2026-09-06.md`
- `TASK_RUN_2026-09-05_T1_SHELL_RETIREMENT.md`
- `WORKFLOWS_READ_ONLY_2026-09-06.md`
- `RIGHT_PANEL_HOST_SATISFACTION_2026-09-06.md`
- `R6_WOVEN_REDESIGN_2026-07-24.md`
- `R7_UI_COMPAT_NAVIGATOR_2026-08-02.md`
- `R8_DAPP86_PACKAGED_WORKBENCH_PIPELINE_2026-08-03.md`
- `TASK_RUN_2026-07-19_DAPP56_R4_P28_pipeline_transition_render.md`
- `R5_DAPP56_DECISION_APPLICATION_2026-07-12.md`

The ADQ-13 note is `projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/Evidence_ADQ-13_UI_Specs_Render_Tests.md`, which exists. The PR #323 merge `403f228f4` resolves in the frozen git history.

**Decision hits** (`DECISION_HITS.csv`, DEL-02-02). DELIVERABLE-source IDs:

| Decision | State |
|---|---|
| D-APP-19 | RULED |
| D-APP-28 | RULED |
| D-APP-30 | RULED |
| D-APP-31 | RULED |
| D-APP-36 | RULED |
| D-APP-38 | RULED |
| D-APP-54 | RULED |
| D-APP-55 | RULED |
| D-APP-56 | RULED |
| D-APP-64 | RULED |
| D-APP-74 | RULED |
| D-APP-81 | RULED |
| D-APP-84 | RULED |
| D-APP-86 | RULED |
| D-APP-88 | RULED |
| D-APP-96 | RULED |
| D-APP-108 | RULED |
| D-APP-109 | RULED |
| D-APP-110 | RULED |
| D-APP-111 | RULED |

REGISTER and RULING sources:
- D-APP-55 (REGISTER, RULED)
- D-APP-96 (REGISTER and RULING `D-APP-96_RULING_ALL_SESSIONS_PRESENTATION_2026-08-17.md`, RULED)
- D-APP-117 (REGISTER L133, **AWAITING_RULING**; names DEL-02-02 Desktop presentation as separate)
- RULING-source IDs: D-APP-56, D-APP-70, D-APP-74, D-APP-79, D-APP-81, D-APP-82, D-APP-86, D-APP-109 and D-APP-110

No D-GOV hits.

## Units

### DEL-02-02#SEC-1 — SCA-APP-004 current responsibility (SoW L26)
- Gist: presents recorded plans/tasks and agents/sessions with provenance; re-hosts Workbench and Pipeline around the dialogue; preserves deep-link intent and disabled states; presentation only.
- Code:
  - Work: [WP] REACH=TEST_ONLY.
  - Agents: [AG] REACH=LIVE, rendered.
  - Workbench and Pipeline: [WB] and [PL] REACH=LIVE, not rendered; [RT].
  - Deep-link intent: [QI] REACH=TEST_ONLY. SH:424 reads only `agent`.
  - Replay composition: SH:1024 and AG `SelectedSessionReplayLens`, rendered.
- Tests: T-WP, T-AG, T-WB, T-PL, T-QI, T-RT, T-SH.
- Decisions: D-APP-56, D-APP-74 (context), D-APP-86, D-APP-96, D-APP-108.

### DEL-02-02#SEC-2 — SCA-APP-004 acceptance obligations 1–6 (SoW L53)
- Gist: Work shows only admitted records with provenance; Agents shows canonical parentage; states disclosed; Workbench and Pipeline preserve intent and guards; replay lens with return; tests prove no authoring.
- Code:
  - Obligation 1: [WP] TEST_ONLY.
  - Obligations 2–3: [AG] `recorded-agent-hierarchy.ts:12,50,201`.
  - Obligation 4: [PL], [WB], [QI] and [DA].
  - Obligation 5: AG `guarded-session-selection.ts:59,159`; SH:408,560,1024.
  - Obligation 6: test bundles below.
- Tests: T-WP :11/:19/:57; T-AG; T-PL; T-WB; T-QI; T-SH :169/:316.
- Decisions: D-APP-36 (render bar), D-APP-56, D-APP-86.

### DEL-02-02#SEC-3 — SCA-APP-010 current responsibility (SoW L80)
- Gist: right panel presents "Who is working" with Agent 0/1/2 role entry, the Workflows view and forms, and a proposal card; Workbench/Pipeline retired from the shell (code, routes and tests retained); Work unmounted.
- Code:
  - Right panel: [SH] `right-panel.tsx:20`, where the tab label is "Agents"; "Who is working" has no hit.
  - Coordination: [AG].
  - Workflows: [WF], where `MethodLibraryView` is rendered and `WorkflowsView` is TEST_ONLY.
  - Proposal card: [PC], no candidate.
  - Role entry and posture labels: [RL], consumed by the DEL-02-05 settings surface only.
  - Retirement: [RT] plus the render-path fact.
  - Work: [WP] TEST_ONLY.
  - Hint `projects/chirality-runtime/packages/contracts/src/delegated.ts` (REACH=LIVE; SYMBOL-REACH: not checked).
- Tests: T-RT (the `woven-dialogue-route` "does not expose the retired execution surface…" case), T-AG, T-WF, T-SH; `components/account-consent-settings*.test.ts` for the labels (hint hits).
- Decisions: D-APP-108 (seating), D-APP-109, D-APP-110, D-APP-111.

### DEL-02-02#SEC-4 — SCA-APP-010 acceptance obligations 1–6 (SoW L107)
- Gist: dialogue invariant with Workbench/Pipeline unmounted but routes reachable (Q3); Who-is-working provenance; Workflows view with list/open/follow/create/bind, currency and gate advance; proposal card is human-act only; presentation-only ownership; split trigger.
- Code:
  - Obligation 1: render-path fact; [RT]; SH:822.
  - Obligation 2: [AG]. The agents-projection test at :117 asserts provenance and evidence metadata are *not* exposed.
  - Obligation 3: [WF]. `governed-workflow.ts:219,236` is TEST_ONLY; `workflow/route.ts` is GET only.
  - Obligation 4: [PC], none.
  - Obligations 5–6: documentary.
- Tests: T-RT, T-AG, T-WF (the governed-workflow cases at :110/:131/:137/:150), T-SH.
- Decisions: D-APP-108 (Q3, Q10–Q16), D-APP-109, D-APP-110.

### DEL-02-02#SEC-5 — Seating and rulings (SoW L116)
- Gist: V3-03 and V3-04 seated under D-APP-108; ruled Q3, Q10–Q16; writes WI-006 to WI-010 performed; DEP-003 and DEP-004 await the dependency pass.
- NO_CANDIDATES (code/tests). Searches: ClaimKey hint row empty; documentary unit.
- Decisions: D-APP-108, D-APP-109 (dependency re-extract, per `_STATUS.md` History 2026-09-05). Run folder `execution/_Coordination/AgentRuns/APP_SCA_APP_010_SEATING_2026-09-04/` is named in the SoW; not read.

### DEL-02-02#CLM-001 — Datasheet header and D-APP-38 PRD MATCH note (SoW L128)
- Gist: datasheet title; notes REF-006 `docs/PRD.md` is MATCH under D-APP-38; older mismatch wording is history.
- NO_CANDIDATES (code/tests). Hints were `verify-version-identity.mjs` and `harness-section9-manifest.json`, which are token noise. `EVIDENCE_PACK/REFERENCE_HASHES.csv` is the check location for the hash recompute (not opened here).
- Decisions: D-APP-38, D-APP-56.

### DEL-02-02#CLM-002 — Identification table (SoW L135)
- Gist: DEL-02-02 identity fields: name, PKG-02, SOFTWARE_DECOMP v3.2, UX_UI_SLICE, envelope M, ResponsibleParty TBD, OPEN at authoring.
- NO_CANDIDATES (code/tests). Hint hits are generic `DeliverableID`/`PackageID` tokens in unrelated tests. The applied name differs in the SCA-APP-010 section (SoW L86) and `_STATUS.md` History 2026-09-04.
- Decisions: D-APP-108 (display-name change).

### DEL-02-02#CLM-003 — Attributes table (SoW L153)
- Gist: Workbench as a right-sidebar/deep-link form with query context and contract checks; Pipeline categories, TASK split selectors, disabled options and stale reset.
- Code:
  - Workbench: [WB] :176-178, :292, :441.
  - Pipeline: [PL] :53, :70, :122, :681-807.
  - Scope helpers: [TS] :18, :29. [DA] :139, :143.
  - Routes: [RT].
  - All WB, PL and the TS helpers are unrendered, per the bundle notes.
- Tests: T-WB, T-PL, T-TS, T-DA, T-QI.
- Decisions: D-APP-28, D-APP-31, D-APP-108 (retirement).

### DEL-02-02#CLM-004 — Conditions (SoW L168)
- Gist: P0/P1 priorities; scope includes UI, excludes runtime internals; PRD MATCH note; stale dispatch package-label warning.
- NO_CANDIDATES (code/tests). Hints were `deliverables-route.test.ts` and `harness-section9-manifest.json`, which are token noise.
- Decisions: D-APP-38.

### DEL-02-02#CLM-005 — Construction (SoW L180)
- Gist: Workbench context UI and contract checks, Pipeline category and TASK selectors, and stale-selection tests are the construction items.
- Code: [WB] :173, :415; [DA] :143, :139; [PL] :53, :681; [TS] :29. All WB and PL are unrendered.
- Tests: T-WB, T-DA, T-PL, T-TS.
- Decisions: D-APP-28.

### DEL-02-02#CLM-006 — References list (SoW L193)
- Gist: lists deliverable-local files, decomposition sections, and PRD, TYPES, SPEC and CONTRACT sections as references.
- NO_CANDIDATES (code/tests). Documentary. Hints were `harness-section9-manifest.json` noise.
- Decisions: none specific.

### DEL-02-02#CLM-007 — D-APP-56 R5 P45 reconciliation (SoW L207)
- Gist: UPD-107 notes the nine-row derivative register exists; dependency extraction is outside this UX slice.
- NO_CANDIDATES (code/tests). Hint row empty. The deliverable `Dependencies.csv` (29,221 B) exists in the frozen folder.
- Decisions: D-APP-56; D-APP-109 (later re-extract).

### DEL-02-02#CLM-008 — Specification heading (SoW L215)
- Gist: heading only: "Specification: DEL-02-02 Workbench and Pipeline Selection UX".
- NO_CANDIDATES (code/tests). Hint row empty.

### DEL-02-02#CLM-009 — Scope (SoW L220)
- Gist: covers Workbench agent/row/column context, read-only contract summaries, Pipeline categories, TASK split selectors and stale reset; excludes runtime internals, dependency extraction and dispatch governance.
- Code: [WB], [DA], [PL], [TS], all unrendered or helper-only.
- Tests: T-WB, T-DA, T-PL, T-TS.
- Decisions: D-APP-56 R4-P35 (SOW-007 split, see CLM-028); D-APP-108 (later retirement).

### DEL-02-02#CLM-010 — Requirements REQ-001..REQ-011 (SoW L241)
- Gist: query context with defaults; loop-first matrix routing; contract API summaries; lifecycle controls gated by agent and approval SHA; four categories with disabled options; TASK split and scope modes; stale reset; UI state non-authoritative.
- Code by requirement:

| Requirement | Code |
|---|---|
| REQ-001 | [WB] :66, :176-178, :415 |
| REQ-002 | [RT] `agent-matrix.tsx` (unrendered legacy prop); `projects/chirality-app-dev/frontend/src/lib/portal/agent-matrix-cells.ts` and `agent-matrix-launch.ts`, both REACH=TEST_ONLY |
| REQ-003 | [DA] :214, :242; [WB] :263-264 |
| REQ-004 | [DA] :9, :143, :8, :139; [WB] :292, :385-394 |
| REQ-005 | [PL] :53, :70, :122 |
| REQ-006 | [PL] :681-686 |
| REQ-007 | [TS] :1, :18; [PL] :807 |
| REQ-008 | [TS] :29; [PL] :295-307, :436-470 |
| REQ-009 | [PL] :122; [QI] :120 |
| REQ-010 | [DA] |
| REQ-011 | [WB] :480-486; [DA] :186 |

- Tests: T-WB, T-DA, T-PL, T-TS, T-QI. Also `lib/agent-matrix-cells.test.ts` and `lib/agent-matrix-launch.test.ts` (REQ-002).
- Decisions: D-APP-28, D-APP-30, D-APP-31, D-APP-108.

### DEL-02-02#CLM-011 — Standards (SoW L260)
- Gist: applies TYPES §4 vocabulary, PRD FR-007..FR-013, SPEC §17.2 workspace API, and CONTRACT §1.7 invariants.
- Code: [DA] consumes `api/working-root/deliverable/{status,dependencies}` routes (REACH=LIVE, no rendered UI caller). [PL] and [TS] carry the vocabulary.
- Tests: T-DA; `api/working-root/deliverable-contracts.test.ts`.
- Decisions: none specific.

### DEL-02-02#CLM-012 — Verification table (SoW L272)
- Gist: maps REQ-001..REQ-011 to tests: workbench-surface, workspace-deliverable-api, pipeline-surface and task-scope-selection test files.
- Code: see CLM-010.
- Tests (named files exist): T-WB, T-DA, T-PL, T-TS. The matrix-routing tests are named as owned with DEL-02-01/DEL-08-02 (`lib/agent-matrix-*.test.ts`).
- Decisions: D-APP-36.

### DEL-02-02#CLM-013 — Documentation (SoW L290)
- Gist: anticipated artifacts are Workbench/Pipeline implementation and tests, stale tests, contract-boundary evidence, the disabled-option notes, and the ADQ-13 evidence note.
- Code: [WB], [PL], [TS], [DA]; disabled-option registry at [PL] :70 and [QI].
- Tests: T-WB, T-PL, T-TS, T-DA.
- Records: `Evidence_ADQ-13_UI_Specs_Render_Tests.md` (exists).
- Decisions: D-APP-56 (SOW-007 ruling).

### DEL-02-02#CLM-014 — D-APP-56 PIPELINE surface amendment, AC-001 (SoW L305)
- Gist: assigns Pipeline Execution Root Scaffold and contract/transition panels to DEL-02-02; requires a Pipeline transition render test at the D-APP-36 bar; AC-001 preserves legacy content.
- Code: [PL] :126 `PipelineLifecycleTransitionForm`, :589 `submitScaffold`, :869, :1001 (unrendered). The scaffold API is `projects/chirality-app-dev/frontend/src/app/api/harness/scaffold/**` (REACH not looked up).
- Tests: T-PL :150, :184; `api/harness/scaffold-route.test.ts` (hint).
- Record: `_run_records/TASK_RUN_2026-07-19_DAPP56_R4_P28_pipeline_transition_render.md`; `_STATUS.md` History 2026-07-19.
- Decisions: D-APP-56 (R4-P28), D-APP-36.

### DEL-02-02#CLM-015 — Procedure heading (SoW L315)
- Gist: heading only.
- NO_CANDIDATES (code/tests). Hint row empty.

### DEL-02-02#CLM-016 — Procedure purpose (SoW L320)
- Gist: defines steps to produce and verify the slice without expanding into runtime internals, dependency extraction or PKG-08 dispatch.
- NO_CANDIDATES (code/tests). Hint row empty. Documentary.

### DEL-02-02#CLM-017 — Prerequisites (SoW L327)
- Gist: accepted working root, accessible source corpus, status/dependencies available; upstream and downstream dependencies TBD.
- NO_CANDIDATES (code/tests). Hints were path-token noise. Dependency state is in the frozen deliverable `Dependencies.csv` and `_DEPENDENCIES.md`.
- Decisions: D-APP-109, D-APP-110 (dependency register).

### DEL-02-02#CLM-018 — Steps 1–7 (SoW L338)
- Gist:
  1. Confirm scope.
  2. Workbench query context and sidebar form.
  3. Contract summaries via APIs and `canAgentTransitionLifecycle`, with approval SHA.
  4. Pipeline categories.
  5. TASK split selectors.
  6. Stale reset.
  7. No `Dependencies.csv` writes.
- Code: [WB] :176-178, :292; [DA] :143, :139; [PL] :53, :681, :807, :295-307; [TS] :29.
- Tests: T-WB, T-DA, T-PL, T-TS.
- Decisions: D-APP-28.

### DEL-02-02#CLM-019 — Verification checks (SoW L387)
- Gist: expected results for query context, matrix routing, contract summaries, contract boundary, categories, TASK selectors, stale reset and the project-truth boundary.
- Code: as CLM-010. Matrix routing is at [RT] `agent-matrix.tsx` (unrendered) and `lib/portal/agent-matrix-*.ts` (TEST_ONLY).
- Tests: T-WB, T-DA, T-PL, T-TS, T-QI, `lib/agent-matrix-*.test.ts`.
- Decisions: D-APP-28, D-APP-30, D-APP-31.

### DEL-02-02#CLM-020 — Records (SoW L403)
- Gist: names the implementation and test files as record locations; Guidance.md rulings TBD; `Dependencies.csv` intentionally not produced.
- Code (named files exist): `workbench-surface.tsx` [WB], `pipeline-surface.tsx` [PL], `deliverable-api.ts` [DA].
- Tests: T-WB, T-DA, T-PL, T-TS.
- The deliverable `Dependencies.csv` exists in the frozen folder, which is a checkable fact against "not produced". `Guidance.md` was not found in the deliverable folder listing.
- Decisions: D-APP-56 (UPD-107).

### DEL-02-02#CLM-021 — D-APP-56 R5 P45 reconciliation, VER-001 (SoW L418)
- Gist: repeats UPD-107 register note. VER-001 calls for schema validation, source mapping, parity, checklist derivation, render stability and human review.
- NO_CANDIDATES (code/tests). Hint row empty.
- Decisions: D-APP-56; D-APP-86 (parity instrument, context).

### DEL-02-02#CLM-022 — Guidance heading and PRD note (SoW L428)
- Gist: guidance heading with the D-APP-38 PRD MATCH note.
- NO_CANDIDATES (code/tests). Hints were token noise.
- Decisions: D-APP-38.

### DEL-02-02#CLM-023 — Guidance purpose (SoW L435)
- Gist: keep Workbench/Pipeline selection coherent from matrix to personas or operative categories: preserve context, show choices, prevent stale selections, UI state subordinate.
- Code: [WB], [PL], [TS] (unrendered or helper-only); [RT].
- Tests: T-WB, T-PL, T-TS.
- Decisions: D-APP-28, D-APP-108.

### DEL-02-02#CLM-024 — Principles (SoW L444)
- Gist: preserve route context; explicit operative selection; disabled over hidden; reset stale selections; UI local state non-authoritative.
- Code: [WB] :176-178; [PL] :53, :122; [TS] :29; [QI] :120, :246; [DA].
- Tests: T-WB, T-PL, T-TS, T-QI (:88 "rejects disabled options without hiding them").
- Decisions: D-APP-28, D-APP-30.

### DEL-02-02#CLM-025 — Considerations (SoW L455)
- Gist: SOW-007 ownership overlap; contract summaries depend on APIs; KNOWLEDGE_TYPES selectable only with a marker; PRD MATCH; ADQ-13 evidence.
- Code: [TS] :18 `normalizeTaskScopeMode`; [PL] :807; [DA] :214, :242.
- Tests: T-TS :15, :43; T-PL :83.
- Record: `Evidence_ADQ-13_UI_Specs_Render_Tests.md`.
- Decisions: D-APP-56 (R4-P35), D-APP-38.

### DEL-02-02#CLM-026 — Trade-offs (SoW L466)
- Gist: visible disabled options; local persistence only if non-authoritative; selector display here and dispatch in PKG-08; defaults with visible resolved context.
- Code: [PL] :122; [QI] (TEST_ONLY); [WB] :415; [DA].
- Local persistence candidate: `projects/chirality-app-dev/frontend/src/lib/woven-dialogue/woven-workspace-state.ts`, REACH=LIVE. SYMBOL-REACH: not checked.
- Tests: T-PL, T-WB, T-QI; `lib/woven-workspace-state.test.ts`.
- Decisions: D-APP-56 (R4-P35).

### DEL-02-02#CLM-027 — Examples (SoW L478)
- Gist: NORMATIVE cell sets live-loop persona context; OPERATIVE cell opens Pipeline; TASK shows split controls; root change resets; unsupported option disabled.
- Code:
  - Matrix: [RT] `agent-matrix.tsx` (unrendered legacy prop); `lib/portal/agent-matrix-launch.ts` (TEST_ONLY).
  - Persona context: SH:424 reads `agent`. The persona-picker in `shell/persona-picker.tsx` is REACH=LIVE; SYMBOL-REACH: rendered in `LoopShell` (unrendered); not checked elsewhere.
  - Pipeline: [PL] :681, :295-307, :122.
- Tests: T-PL, T-TS, `lib/agent-matrix-launch.test.ts`.
- Decisions: D-APP-28, D-APP-30.

### DEL-02-02#CLM-028 — Conflict table (SoW L491)
- Gist: CONFLICT-001 stale package label; CONFLICT-002 PRD hash status; CONFLICT-003 SOW-007 ownership, ruled under D-APP-56 R4-P35 (split ratified). 001 and 002 show human ruling TBD.
- NO_CANDIDATES (code/tests). Documentary. Hints were path-token noise.
- Decisions: D-APP-56 (R4-P35); D-APP-38 (PRD MATCH).

### DEL-02-02#REMTXT-1 — Remaining prose: implemented and evidenced (_STATUS L12)
- Gist: asserts Work/Agents projections (PR #323 `403f228f4`), the Workbench/Pipeline re-host, the Artifacts fold into Workbench Documents, and coordination presentation are implemented and evidenced; D-APP-96 accepted "All sessions (N)"; no presentation residual.
- Code:
  - Work: [WP] TEST_ONLY.
  - Agents: [AG] LIVE, rendered.
  - Workbench and Pipeline re-host: [WB] and [PL], LIVE but unrendered after the V3-03 retirement (`_STATUS.md` History 2026-09-05 and 2026-09-06).
  - Documents fold: [WB] :592 (unrendered).
  - "All sessions (N)": `projects/chirality-app-dev/frontend/src/components/woven-dialogue/navigator.tsx`, REACH=LIVE. SYMBOL-REACH: not checked.
- Tests: T-WP, T-AG, T-WB :59/:68; `components/woven-dialogue-navigator.test.tsx`.
- Records: `_run_records/R6_WOVEN_REDESIGN_2026-07-24.md`, `R7_UI_COMPAT_NAVIGATOR_2026-08-02.md`, `R8_DAPP86_PACKAGED_WORKBENCH_PIPELINE_2026-08-03.md`.
- Decisions: D-APP-96, D-APP-86, D-APP-74 (context).

### DEL-02-02#REMTXT-2 — Mandatory non-blocking rerun trigger (_STATUS L21)
- Gist: if a later accepted D-APP-88 distinct-helper implementation lands, rerun the D-APP-86 packaged parity instrument.
- NO_CANDIDATES (code/tests). Hint row empty.
- Decisions: D-APP-88 (DELIVERABLE hit, RULED), D-APP-86. Trigger status can be checked in the App decision register rows for D-APP-88 and D-APP-86.

### DEL-02-02#REM-1 — DEL-02-02-V3-01 (_STATUS L25)
- Gist: Work/Agents presentation of managed and native descendant records with source, authority-class, responsible-reference, currency and evidence labels from recorded evidence.
- Gate suffix, verbatim: `NOT_SELECTABLE_UNTIL: DEL-08-05-V3-01 landed (recorded managed/native descendant records exist to present)`
- Gate status check: `projects/chirality-app-dev/execution/PKG-08_Agent_Suite_Pipeline_Dispatch_and_Subagent_Governance/1_Working/DEL-08-05_Subagent_Child_Run_Records_and_Artifacts/_STATUS.md` L11. DEL-08-05-V3-01 is listed there as a Remaining item with its own `NOT_SELECTABLE_UNTIL` gate.
- Code (current presentation): [AG] `coordination-panel.tsx:38,68-77` (native children from events); `agents-projection.tsx:109`; `recorded-agent-hierarchy.ts:126,50`. The agents-projection test at :117 asserts provenance and evidence metadata are *not* shown. Role and posture labels: [RL] (unseated here per the item text).
- Tests: T-AG; `components/native-coordination.test.tsx`.
- Decisions: D-APP-117 (AWAITING_RULING; names DEL-02-02 Desktop as separate), D-APP-108.

### DEL-02-02#REM-2 — DEL-02-02-V3-02 (_STATUS L33)
- Gist: live descendant/status presentation.
- Gate suffix, verbatim: `NOT_SELECTABLE_UNTIL: Root API v2 and event schema v2 acceptance routed to App (Root DEL-02-10) and DEL-08-04-V3-01 landed`
- Gate status checks:
  - `projects/chirality-app-dev/execution/PKG-08_Agent_Suite_Pipeline_Dispatch_and_Subagent_Governance/1_Working/DEL-08-04_Type_2_Subagent_Governance_Bridge/_STATUS.md` L17 (DEL-08-04-V3-01 listed as Remaining).
  - For the Root DEL-02-10 routed notice: the App gates on DEL-08-05 (L11) and DEL-08-04 (L17) cite "accepted DEL-02-07 and DEL-02-10 returns routed to App". A routed-notice record was not located on the App side (App `_Coordination` non-AgentRuns grep not completed).
- Code: [AG] (current, non-live presentation).
- Tests: T-AG.
- Decisions: D-APP-117 (AWAITING_RULING, context).

### DEL-02-02#REM-3 — DEL-02-02-V3-04 (_STATUS L42)
- Gist: Workflows view, roadmap, New workflow form, library and bind, derived rung, proposal card, and the K-PATH-2-contained workflow read/write route (T3 part).
- Gate suffix, verbatim: `NOT_SELECTABLE_UNTIL: DEL-02-02-V3-03 landed; DEL-07-03-V3-01 landed`
- Gate status checks:
  - V3-03: this deliverable's `_STATUS.md` History 2026-09-06 (removed after PR733 merge `8e649eaa5…`); `_run_records/T1_MERGED_RECONCILIATION_2026-09-06.md`.
  - DEL-07-03-V3-01: `projects/chirality-app-dev/execution/PKG-07_Filesystem_Execution_Lifecycle_and_Dependencies/1_Working/DEL-07-03_Deliverable_Metadata_and_Document_Kit_Contracts/_STATUS.md` L27 (History 2026-09-06: removed from Remaining, PR #733 merged `8e649eaa5…`).
  - Partial slice: `_STATUS.md` History 2026-09-06 (read-only GET/list slice); `_run_records/WORKFLOWS_READ_ONLY_2026-09-06.md`.
- Code:
  - Rendered: [WF] `method-library-view.tsx:69` and `workflow-draft-review.tsx:9`.
  - TEST_ONLY: `workflows-view.tsx:7` and `workflow-detail.tsx`.
  - `api/working-root/workflow/route.ts:7` is GET only, with no write handler found; `workflow-store.ts:34,50,83`.
  - `governed-workflow.ts:219,230,236` (advance, bind, currency) is TEST_ONLY.
  - Proposal card: [PC], none.
- Tests: T-WF.
- Decisions: D-APP-108 (Q10–Q16), D-APP-109.

## Cross-cutting

Recurring modules (unit counts approximate, by citation):

| Module | REACH | Units | Symbol reach |
|---|---|---|---|
| `components/pipeline/pipeline-surface.tsx` [PL] | LIVE | ~17 | Not rendered |
| `components/workbench/workbench-surface.tsx` [WB] | LIVE | ~16 | Not rendered |
| `lib/workspace/deliverable-api.ts` [DA] | LIVE | ~13 | Importers only WB and PL; its target API routes are LIVE entries with no rendered UI caller |
| `lib/workspace/task-scope.ts` [TS] | LIVE | ~12 | Only `buildDeliverableCompositeKey` is used from a rendered path; the selection helpers are PL-only |
| `components/woven-dialogue/{coordination-panel,agents-projection}.tsx` and `lib/woven-dialogue/recorded-agent-hierarchy.ts` [AG] | LIVE | ~7 | Rendered |
| `lib/pipeline/pipeline-dispatch-contract.ts` [QI] | TEST_ONLY | ~6 | — |
| `app/{workbench,pipeline}/*` and `components/shell/{loop,loop-tertiary,portal-loop}-shell.tsx` [RT] | LIVE | ~6 | Routes render the Woven shell; the loop shells are unrendered `legacy` props |

Live-versus-legacy split: no candidate module for this deliverable is LEGACY_ONLY, except the Agent 0/1/2 delegation strings in `lib/harness/managed-delegation.ts` and `subagent-governance.ts`.

The material split is **rendered versus not rendered**:
- **Rendered:** the Woven shell, right panel, coordination/agents projection, replay lens, method library and workflow-draft review.
- **LIVE-tagged but not rendered:** the entire Workbench and Pipeline presentation ([WB], [PL]) and its helpers ([DA]'s transition and SHA helpers; [TS]'s sanitize and normalize). The only path is `createTertiarySidebarTabs` inside `legacy` props that `WovenDialogueRoute` discards (`void legacy`).
- **TEST_ONLY:** Work projection, WorkflowsView and WorkflowDetail, governed-workflow roadmap logic, and the Pipeline dispatch contract.
- **Not found:** proposal card.

Route tests (T-RT) mock `WovenDialogueShell` to echo `defaultSurface`. The real shell ignores that prop and emits `data-woven-surface="dialogue"` (SH:822).

The SCA-APP-004 and older CLM units (Workbench/Pipeline behaviour) therefore map almost entirely to unrendered or TEST_ONLY code. The SCA-APP-010 units map partly to rendered code (AG, method library) and partly to TEST_ONLY or absent code (WorkflowsView, governed-workflow, proposal card).
#END
