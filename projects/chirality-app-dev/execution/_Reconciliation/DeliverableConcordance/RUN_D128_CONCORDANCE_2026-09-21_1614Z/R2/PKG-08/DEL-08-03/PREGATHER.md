# PREGATHER — DEL-08-03 Pipeline Category and Task Scope Dispatch

- **Run:** RUN_D128_CONCORDANCE_2026-09-21_1614Z (R2, PKG-08). Worker: TASK pre-gather (read-only).
- **Basis:** frozen tree at `00115c719`. All paths repo-relative.
- **Deliverable folder:** `projects/chirality-app-dev/execution/PKG-08_Agent_Suite_Pipeline_Dispatch_and_Subagent_Governance/1_Working/DEL-08-03_Pipeline_Category_and_Task_Scope_Dispatch/` (below: `DEL/`).
- **Scope:** evidence location only. No dispositions, alignment judgments or CauseTags.

## Method

- CLAIM_INDEX rows for DEL-08-03: 40 units (3 SEC, 37 CLM; **0 REM**). SubItems: CLM-019 → `AC-001`; CLM-026 → `VER-001` (both single-item).
- HINTS/DEL-08-03.csv: 654 hit rows (+`#END`), 40 ClaimKeys. Summarised by path/token with python3 counts. Top hit paths: `deliverables-route.test.ts` 87, `scripts/harness-section9-manifest.json` 81 (vocabulary echo, not code), `pipeline-surface.test.ts` 63, `lib/workspace/filesystem.ts` 44, `deliverable-contracts.test.ts` 35, `pipeline-dispatch-contract.test.ts` 32, `pipeline-surface.tsx` 25.
- Greps in the frozen tree: `pipeline-surface|pipeline-dispatch-contract|task-scope` importers; `DECOMP_OPTIONS|enabled: false|KNOWLEDGE_TYPES|useDeliverables|sanitizeTaskSelection`; `KNOWLEDGE_TYPE_BUCKETS|buildKnowledgeTypeOptions|detectKnowledgeMarkerFile`; `/api/project/deliverables`, `/api/working-root/scope` callers; `executionAuthorized|delegate_agent|K-SUBAGENT|approvalRef|sealed` in frontend `src/lib` and runtime `packages/*/src`, `tests`; `WovenDialogueRoute legacy`; test `describe/it` names.
- Evidence pack used: `REACHABILITY.csv`, `TOUCHED_PATHS.csv`, `DECISION_HITS.csv` (59 rows for DEL-08-03), `REFERENCE_HASHES.csv`, `D-APP-127_APPLICATION_MAP.csv`.
- **TOUCHED_PATHS:** no row names any `projects/chirality-app-dev/frontend/**` path, and none of the runtime files cited below. No citation here is TOUCHED. The post-release basis for every citation below is the frozen basis.

## Module key (REACH copied from REACHABILITY.csv)

| Key | Path | REACH | Notes (reach facts) |
|---|---|---|---|
| PS | `projects/chirality-app-dev/frontend/src/components/pipeline/pipeline-surface.tsx` | LIVE | chain `src/app/chat/page.tsx>…/shell/loop-shell.tsx>…/shell/tertiary-sidebar-tabs.tsx>pipeline-surface.tsx`. Also imported by `src/app/pipeline/pipeline-client.tsx` via `LoopTertiaryShell` (LIVE). Both routes pass the loop shell as `legacy` to `WovenDialogueRoute`, which does `void legacy;` and renders only `WovenDialogueShell` (`src/components/woven-dialogue/woven-dialogue-route.tsx:16-19`). The static import makes it LIVE, but the element is never rendered. |
| PDC | `projects/chirality-app-dev/frontend/src/lib/pipeline/pipeline-dispatch-contract.ts` | TEST_ONLY | imported only by `pipeline-dispatch-contract.test.ts` and `pkg08-compatibility-boundaries.test.ts`. PS does **not** import it; PS keeps its own local option arrays. |
| TS | `projects/chirality-app-dev/frontend/src/lib/workspace/task-scope.ts` | LIVE | chain `src/app/layout.tsx>…/workspace/deliverables-provider.tsx>task-scope.ts`; also imported by PS |
| DP | `projects/chirality-app-dev/frontend/src/components/workspace/deliverables-provider.tsx` | LIVE | fetches `/api/project/deliverables` at :117-118. `useDeliverables` at :171. |
| FS | `projects/chirality-app-dev/frontend/src/lib/workspace/filesystem.ts` | LIVE | chain `src/app/api/project/deliverables/route.ts>filesystem.ts` |
| RD | `projects/chirality-app-dev/frontend/src/app/api/project/deliverables/route.ts` | LIVE | entry; `GET` → `scanProjectDeliverables` |
| RS | `projects/chirality-app-dev/frontend/src/app/api/working-root/scope/route.ts` | LIVE | entry; `GET` → `scanProjectScopes`. Its only non-test caller is `workbench-surface.tsx:212`. |
| WB | `projects/chirality-app-dev/frontend/src/components/workbench/workbench-surface.tsx` | LIVE | same shell chain as PS (tertiary-sidebar-tabs) |
| WP | `projects/chirality-app-dev/frontend/src/components/woven-dialogue/work-projection.tsx` | TEST_ONLY | `WorkProjection` :14 |
| CP | `projects/chirality-app-dev/frontend/src/components/woven-dialogue/coordination-panel.tsx` | LIVE | Agents view renders "Native work in current chat" (:68-69) from harness events |
| WR | `projects/chirality-app-dev/frontend/src/components/woven-dialogue/woven-dialogue-route.tsx` | LIVE | see PS note |
| SG | `projects/chirality-app-dev/frontend/src/lib/harness/subagent-governance.ts` | LEGACY_ONLY | `evaluateSubagentGovernance` :196 |
| MD | `projects/chirality-app-dev/frontend/src/lib/harness/managed-delegation.ts` | LEGACY_ONLY | — |
| TD | `projects/chirality-runtime/packages/contracts/src/harness/tool-descriptor.ts` | LIVE | `delegate_agent` descriptor :635-636 |

## Test key (VERIFICATION_INDEX counts in brackets)

- T-PS `projects/chirality-app-dev/frontend/src/__tests__/components/pipeline-surface.test.ts` [5]: :63 "renders operative category controls, TASK split selectors, and disabled coming-soon options"; :83 "renders valid TASK knowledge-type deep links with required target deliverables"; :116 "resets stale TASK knowledge-target deep links during initial render"; :150 "requires approval SHA and locks actor choice to HUMAN for human-gated transitions"; :184 "keeps approval SHA optional and submission active for ordinary transitions".
- T-TS `…/__tests__/lib/task-scope-selection.test.ts` [6]: :9 "builds pkg::id deliverable keys"; :15 "normalizes KNOWLEDGE_TYPES mode only when marker is enabled"; :22 "clears stale deliverable keys when scan results no longer include the key"; :43 "resets KNOWLEDGE_TYPES selection when the decomposition marker is absent"; :69 "clears stale knowledge-type target keys that no longer resolve to deliverables"; :95 "preserves valid knowledge-type target keys".
- T-PDC `…/__tests__/lib/pipeline-dispatch-contract.test.ts` [5]: :21 "preserves the exact DECOMP/PREP/TASK/AUDIT taxonomy and option states"; :54 "returns inert data for an admitted deliverable-scoped TASK intent"; :88 "rejects disabled options without hiding them"; :113 "requires exact recorded scope and a target for knowledge-type TASK intent"; :146 "preserves persona, matrix, and unknown query parameters while patching Pipeline intent".
- T-B08 `…/__tests__/lib/pkg08-compatibility-boundaries.test.ts` [3]: :28 "does not turn Pipeline presentation state into delegation authority" (asserts `executionAuthorized` false; no `delegate_agent`/`approvalRef`/`writeTargets` keys, :41-46); also :10, :16.
- T-DR `…/__tests__/api/project/deliverables-route.test.ts` [5]: :146 "returns deliverables, knowledge marker metadata, and knowledge type mappings"; :200 "returns marker disabled when no decomposition marker is present"; :224 "returns additive deliverable contract findings for incomplete document kits"; :308 "never infers an authorized migration from a normal project route scan"; :344 "returns typed accessibility failures for missing project roots".
- T-WP `…/__tests__/components/woven-dialogue-work-projection.test.tsx` [3]: :11 "renders an honest empty state instead of synthesizing work from dialogue"; :19 "renders only supplied evidence with visible authority, provenance, and currency"; :57 "discloses unrecorded optional evidence without inferring assignments or status".
- T-WDS `…/__tests__/components/woven-dialogue-shell.test.tsx` [28]: :156 "only mounts Dialogue even with historical %s surface input" (asserts no `data-pipeline-surface`, :164).
- Not found: no test file references `/api/working-root/scope` (grep of `src/__tests__`).

## Decision key (DECISION_HITS.csv, DEL-08-03; register `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/_REGISTER.md`)

D-APP-19 (_STATUS :5,:18), D-APP-36 (run record), D-APP-38 (SoW :160,:175,:313,:359,:509,:525,:526,:559,:576,:578,:580; register :53), D-APP-54 (_STATUS :18; register :69), D-APP-55, D-APP-56 (SoW :117,:190,:192,:246,:328,:330; register :71), D-APP-70 (RULING), D-APP-74 (_REFERENCES :50; RULING; register :89 Woven/Coordination Panel IA), D-APP-79/81/82 (RULING), D-APP-108 (SoW :53, _STATUS :34; register :123 SCA-APP-010 seating), D-APP-109 (_STATUS :35; RULING `D-APP-109_RULING_SCA_APP_010_HELD_EDGES_AND_CONTEXT_ALIGNMENT_2026-09-05.md:51`; register :124). All RULED. No D-GOV hits. D-APP-127 (register :152): the application map shows `Revised=NO` for all five DEL-08-03 carriers.

---

## Units (index order)

### DEL-08-03#SEC-1 — Current responsibility (SoW :29)
- Gist: DEL-08-03 owns presentation-neutral DECOMP/PREP/TASK/AUDIT semantics. The Pipeline presentation is retired from the active shell, with code retained, and there is no active consumer.
- Code: PDC:1 `PipelineCategory`, :10 `PIPELINE_CATEGORY_ORDER`, :17 `PIPELINE_CATEGORY_OPTIONS`, :120 `validatePipelineDispatchIntent` REACH=TEST_ONLY; PS:28 `OperativeCategory`, :53 `CATEGORY_ORDER` REACH=LIVE (see PS note); WR:16-19 `WovenDialogueRoute` (`void legacy`) REACH=LIVE.
- Tests: T-PDC :21; T-WDS :156.
- Decisions: D-APP-108, D-APP-109, D-APP-74.

### DEL-08-03#SEC-2 — Current acceptance obligations (SoW :45)
- Gist: three obligations: semantics stay presentation-neutral and owned here; the Pipeline presentation is retired (code retained); no consumer may infer plans or tasks from prose.
- Code: as SEC-1; WP:14 `WorkProjection` REACH=TEST_ONLY; CP:68 REACH=LIVE.
- Tests: T-PDC :21, :54; T-WDS :156; T-WP :11, :19.
- Decisions: D-APP-108, D-APP-74.

### DEL-08-03#SEC-3 — Seating and rulings (SoW :51)
- Gist: D-APP-108 seated no remaining items. WI-056..060 were written; DEP-023/024 await the dependency-extract pass. No lifecycle act is implied.
- Code: NO_CANDIDATES (documentary). Searched: HINTS (1 row), DECISION_HITS.
- Decisions: D-APP-108 (register :123), D-APP-109 (register :124; its RULING records the dependency re-extraction per `_STATUS.md` 2026-09-05 history).

### DEL-08-03#CLM-001 — Datasheet heading (SoW :63)
- Gist: section heading only.
- NO_CANDIDATES (heading; HINTS 1 row).

### DEL-08-03#CLM-002 — Identification (SoW :68)
- Gist: identification table: decomposition variant/revision/path, PKG-08, UX_UI_SLICE, ResponsibleParty TBD.
- NO_CANDIDATES in code. Documentary check targets: `DEL/_CONTEXT.md`, decomposition path `projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` (SoW front-matter cites v3_2@dbd812a52).

### DEL-08-03#CLM-003 — Attributes (SoW :86)
- Gist: lists scope, exclusions, anticipated artifacts, and the TYPES §4.4 vocabularies: categories, TASK scope modes, the 10 knowledge-type options, disabled-option meaning.
- Code: PDC:1-2 types; PS:70 `DECOMP_OPTIONS`, :77 `PREP_OPTIONS`, :84 `TASK_AGENT_OPTIONS`, :94 `AUDIT_OPTIONS` (the `enabled:false` entries are BASE, ESTIMATING, SCHEDULING, ESTIMATES, SCHEDULES) REACH=LIVE. TS:1 `TaskScopeMode` REACH=LIVE. FS:142 `KnowledgeTypeOption` type, :214 `KNOWLEDGE_TYPE_BUCKETS` (ids include scope-of-work, datasheet, specification, guidance, procedure, dependencies, references, context, status, …) REACH=LIVE.
- Vocabulary source: `projects/chirality-app-dev/docs/TYPES.md:176-179`.
- Tests: T-PDC :21; T-PS :63; T-DR :146.
- Decisions: D-APP-108 (retirement context).

### DEL-08-03#CLM-004 — Conditions (SoW :105)
- Gist: conditions from PRD FR-011/012/013/049 and SPEC §17.2. Scope API at `/api/project/deliverables`; presentation owned by DEL-02-02; work projection must not convert prose; DEL-08-05 keeps child records.
- Code: PS:633-856 category cards; :704-719 scope-mode select; :771-807 knowledge target and marker-unavailable message REACH=LIVE. TS:18 `normalizeTaskScopeMode`, :29 `sanitizeTaskSelection` REACH=LIVE. RD `GET`, FS:1156 `scanProjectDeliverables`, :1051 `detectKnowledgeMarkerFile` REACH=LIVE. DP:117 fetch REACH=LIVE. WP:14 REACH=TEST_ONLY.
- Tests: T-PS :63, :83, :116; T-TS all; T-DR :146, :200; T-WP :11.
- Decisions: D-APP-56 (R4-P21 cited, SoW :117), D-APP-74.

### DEL-08-03#CLM-005 — Construction (SoW :123)
- Gist: component table naming PS, FS, and T-PS / T-TS / T-DR as the implementing and test paths.
- Code: PS (REACH=LIVE, see note); FS REACH=LIVE. Named test files all exist (VERIFICATION_INDEX).
- Tests: T-PS, T-TS, T-DR.
- Decisions: none specific.

### DEL-08-03#CLM-006 — Implementation Slots (SoW :139)
- Gist: slot table: the category option source is local arrays in `pipeline-surface.tsx`; `pipeline-surface.tsx` consumes the scan data; fixtures are T-DR and T-TS.
- Code: PS:70-102 local arrays REACH=LIVE; PS:231-232 `useDeliverables()` → DP:117 `/api/project/deliverables` REACH=LIVE. Parallel option source PDC:17 `PIPELINE_CATEGORY_OPTIONS` REACH=TEST_ONLY; the slot table does not name it.
- Tests: T-PS :63; T-DR :146; T-TS :22, :43, :69.

### DEL-08-03#CLM-007 — Dependency Edge Snapshot (SoW :153)
- Gist: `_DEPENDENCIES.md` anchors, interfaces and a downstream handoff. Satisfaction is TBD; the consumer target is TBD.
- NO_CANDIDATES in code. Check targets: `DEL/_DEPENDENCIES.md` (D-APP-38 at :86, :96), `DEL/Dependencies.csv` (D-APP-38 :10); D-APP-109 re-extraction (per `_STATUS.md` history 2026-09-05).
- Decisions: D-APP-38, D-APP-109.

### DEL-08-03#CLM-008 — References (SoW :164)
- Gist: REF-001..007 and DECOMP reference table. REF-006 (PRD) is described as current under D-APP-38.
- NO_CANDIDATES in code. REFERENCE_HASHES.csv, DEL-08-03: CONTRACT, PRD and SPEC each have `RecordedVerdict=MATCH`, `Match=NO` (cite `HASH-RECOMPUTE@00115c719`). REF-007 is an absolute user-home path in the SoW text (SoW :176).
- Decisions: D-APP-38 (register :53).

### DEL-08-03#CLM-009 — Pass 3 Disposition Notes (SoW :180)
- Gist: B-001/B-002 were converted into implementation slots and the dependency snapshot.
- NO_CANDIDATES (method note; HINTS 1 row).

### DEL-08-03#CLM-010 — D-APP-56 R5 P45 reconciliation (SoW :190)
- Gist: UPD-134 states that the extracted derivative dependency register exists and is live.
- NO_CANDIDATES in code. Check targets: `DEL/Dependencies.csv`, `DEL/_run_records/TASK_RUN_2026-07-12_DAPP56_R5_P45.md`, `DEL/_run_records/R5_DAPP56_DECISION_APPLICATION_2026-07-12.md`.
- Decisions: D-APP-56.

### DEL-08-03#CLM-011 — Specification heading (SoW :198)
- Gist: section heading. The Output matrix maps OUT-001 to CLM-011.
- NO_CANDIDATES (heading).

### DEL-08-03#CLM-012 — Scope (SoW :203)
- Gist: in scope: category selection, disabled options, TASK split selectors, dynamic scope, reset, tests, contextual-consumer parity. Out of scope: SDK mechanics, Type 2 bridge, Coordination Panel presentation, lifecycle, and related items.
- Code: PS as CLM-004 REACH=LIVE. PDC:246 `mergePipelineQueryParameters` REACH=TEST_ONLY. PS also contains a lifecycle transition form: PS:126 `PipelineLifecycleTransitionForm`, `transitionDeliverableStatus` import :17, submit ~:567, and harness scaffold call :607 `scaffoldHarnessExecutionRoot` (REACH=LIVE).
- Tests: T-PS :63, :150, :184; T-PDC; T-WP.
- Decisions: D-APP-74, D-APP-108.

### DEL-08-03#CLM-013 — Requirements (SoW :231)
- Gist: REQ-001..016 (not in the SubItems column). They cover categories, options, disabled, split TASK, scope modes, target, reset, doc-kit buckets, vocabulary, active-root scan, governance, tests, neutrality, projection, status separation and non-ownership.
- Per REQ:
  - REQ-001/002/003: PS:633-856 cards/selects with `disabled={!option.enabled}` (:648, :671, :695, :849), arrays :70-102 REACH=LIVE; PDC:17, :149 `OPTION_DISABLED` REACH=TEST_ONLY. T-PS :63; T-PDC :21, :88.
  - REQ-004/005/006: PS:687 (TASK agent select), :704-719 (scope mode), :771-790 (target) REACH=LIVE; PDC:194 `TARGET_DELIVERABLE_REQUIRED`, :202 `TARGET_DELIVERABLE_NOT_RECORDED` REACH=TEST_ONLY. T-PS :63, :83; T-PDC :113; T-TS :15.
  - REQ-007: PS:299-306 reset on `projectRoot`, :329-337 reset on `scopeError`, :339+ `sanitizeTaskSelection` effect REACH=LIVE; TS:29 REACH=LIVE. T-TS :22, :43, :69, :95; T-PS :116.
  - REQ-008/009: FS:214 `KNOWLEDGE_TYPE_BUCKETS`, :1015 `buildKnowledgeTypeOptions`, :1020-1021 scope-of-work filter REACH=LIVE. T-DR :146, :224.
  - REQ-010: DP:117-118 → RD → FS:1156 REACH=LIVE; `normalizeProjectRoot` FS:309. T-DR :146, :344.
  - REQ-011: PDC:69, :228 `executionAuthorized: false` REACH=TEST_ONLY; SG:196 REACH=LEGACY_ONLY; MD REACH=LEGACY_ONLY; TD:635 `delegate_agent` REACH=LIVE. T-B08 :28; T-PDC :54; `projects/chirality-runtime/tests/runtime-v3-api.test.ts :: preserves TASK identity and sealed scope through a deferred method stop` (:602).
  - REQ-012: T-PS, T-TS, T-DR as above.
  - REQ-013: PDC REACH=TEST_ONLY is not imported by PS or WB. WB (LIVE) has no category/taskScope symbols (grep). T-PDC :146; T-WDS :156.
  - REQ-014: WP:14 REACH=TEST_ONLY; CP:68 REACH=LIVE. T-WP :11, :19, :57.
  - REQ-015/016: PS:126 lifecycle form REACH=LIVE; T-PS :150, :184; T-DR :308.
- Decisions: D-APP-56 (REQ-010 R4-P21), D-APP-74, D-APP-108.

### DEL-08-03#CLM-014 — Standards (SoW :255)
- Gist: vocabulary standards from TYPES §4.4, PRD §8.2, SPEC §17.2 and CONTRACT §1.8.
- Code: PDC:1-2, TS:1, FS:142 (see CLM-003). Doc: `projects/chirality-app-dev/docs/TYPES.md:176-179`.
- Tests: T-PDC :21.
- Decisions: D-APP-38.

### DEL-08-03#CLM-015 — Verification (SoW :270)
- Gist: maps the REQs to verification approaches: UI/unit selector tests, reset fixtures, discovery tests, scope API, governance guards, cross-surface regression, projection tests.
- Tests: as the CLM-013 per-REQ list. No cross-surface test exercises PS and a second live consumer together (grep of importers: PS is mocked in T-WDS only).
- Decisions: none specific.

### DEL-08-03#CLM-016 — Documentation (SoW :288)
- Gist: expected artifacts list. Scope-scan evidence is named as `/api/working-root/scope` (the requirements name `/api/project/deliverables`).
- Code: RS REACH=LIVE, called only by WB:212. RD/DP REACH=LIVE used by PS. No test references `/api/working-root/scope`.
- Tests: T-DR; T-PS; T-TS; T-B08 :28; T-WP.

### DEL-08-03#CLM-017 — Source State (SoW :307)
- Gist: STATE-001 says PRD is current under D-APP-38 and `_REFERENCES.md` records REF-006 as MATCH.
- Evidence: REFERENCE_HASHES.csv DEL-08-03 PRD `RecordedVerdict=MATCH`, `Match=NO` (`HASH-RECOMPUTE@00115c719`). Check `DEL/_REFERENCES.md`.
- Decisions: D-APP-38.

### DEL-08-03#CLM-018 — Pass 3 Disposition Notes (SoW :316)
- Gist: F-001 and X-001..003 were incorporated as REQ-011 proof threshold, option sources, doc-kit discovery and disabled-option evidence.
- NO_CANDIDATES (method note). Related evidence: see CLM-013 REQ-002/003/008/011.

### DEL-08-03#CLM-019 — D-APP-56 R5 P45 reconciliation + AC-001 (SoW :328; SubItems AC-001)
- Gist: repeats UPD-134. AC-001 lists: dispatch contract, Pipeline/contextual-consumer selector tests, discovery fixtures, dynamic scope/disabled handling, governance guards, Work-projection non-authority.
- AC-001 candidates: PDC REACH=TEST_ONLY + T-PDC; T-PS; T-DR; T-TS; T-B08 :28; WP REACH=TEST_ONLY + T-WP. Contextual-consumer: none found beyond T-WDS :156.
- Decisions: D-APP-56.

### DEL-08-03#CLM-020 — Procedure heading (SoW :338)
- NO_CANDIDATES (heading).

### DEL-08-03#CLM-021 — Purpose (SoW :343)
- Gist: the procedure produces and verifies selector tests, knowledge-type discovery and disabled-option handling.
- Tests: T-PS :63; T-DR :146; T-PDC :88.

### DEL-08-03#CLM-022 — Prerequisites (SoW :350)
- Gist: prerequisites are available: decomposition entry, metadata files, TYPES/PRD/SPEC, and `_DEPENDENCIES.md` rows (satisfaction TBD).
- NO_CANDIDATES in code. Check targets: `DEL/` file listing (all named files present at basis: `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_SEMANTIC.md`, `_STATUS.md`); REFERENCE_HASHES (PRD `Match=NO`).
- Decisions: D-APP-38.

### DEL-08-03#CLM-023 — Steps (SoW :365)
- Gist: nine steps: locate UI, map vocabulary, verify categories/options/disabled, TASK split, dynamic scope via `/api/working-root/scope`, reset, governance boundary, tests, contextual consumers.
- Code: as CLM-013 per REQ; step 5 → RS REACH=LIVE (WB:212 caller) vs DP/RD REACH=LIVE (PS path); step 7 → PDC:69 REACH=TEST_ONLY, SG:196 REACH=LEGACY_ONLY; step 9 → WR:16-19 REACH=LIVE, WP REACH=TEST_ONLY.
- Tests: as CLM-013.

### DEL-08-03#CLM-024 — Verification (SoW :424)
- Gist: nine checks: category, option-list, disabled, TASK split, target, scope API (`/api/working-root/scope`), bucket discovery, reset, governance review.
- Tests: T-PS :63, :83, :116; T-PDC :21, :88, :113; T-TS :15-:95; T-DR :146, :200; T-B08 :28. Scope API check: no test for RS.

### DEL-08-03#CLM-025 — Records (SoW :441)
- Gist: records to maintain, including tests, fixtures, scope-API evidence, governance review and implementation notes naming component/test paths (owner TBD).
- Code/tests: see Test key. Implementation-note records: NO_CANDIDATES found in `DEL/` beyond the SoW slot table (CLM-006). Searched `DEL/_run_records/` names: R5_DAPP56…, TASK_RUN_…P45, R6_WOVEN_REDESIGN_2026-07-24.

### DEL-08-03#CLM-026 — Pass 3 Disposition Notes + VER-001 (SoW :459; SubItems VER-001)
- Gist: F-002, F-003 and D-002 were incorporated. VER-001 is a test inventory review with named category, TASK scope, discovery, disabled and reset fixtures.
- VER-001 candidates: T-PS (5 cases), T-TS (6), T-PDC (5), T-DR (5); VERIFICATION_INDEX counts in the Test key.

### DEL-08-03#CLM-027 — Guidance heading (SoW :473)
- NO_CANDIDATES (heading).

### DEL-08-03#CLM-028 — Purpose (SoW :478)
- Gist: keeps the PIPELINE dispatch surface aligned with the agent architecture, without turning UI selection into runtime authority. Operators see lanes, scope, buckets and disabled variants.
- Code: PS REACH=LIVE (not rendered; see note); PDC:69 REACH=TEST_ONLY.
- Tests: T-B08 :28; T-WDS :156.
- Decisions: D-APP-108.

### DEL-08-03#CLM-029 — Principles (SoW :487)
- Gist: principles: canonical vocabulary, explicit categories, separate task and scope selection, deliverable-bound knowledge mode, visible-disabled unsupported options, no authority expansion.
- Code: PS:28 local `OperativeCategory` type vs PDC:1 `PipelineCategory` (TEST_ONLY), vs TYPES `DisabledOption` (PS uses `Option.enabled`, :30). TS:1. FS:142.
- Tests: T-PDC :21, :88; T-PS :63; T-TS :43, :69; T-B08 :28.

### DEL-08-03#CLM-030 — Considerations (SoW :501)
- Gist: prefer source-derived vocabulary, clear stale selections on root change, the four-document kit comes first, metadata buckets only with canonical labels, and REF-006 is current.
- Code: FS:214-260 bucket ids/labels (includes a `scope-of-work` bucket not in the TYPES list; filtered at :1020-1021 by flag) REACH=LIVE; PS:299-306 REACH=LIVE.
- Tests: T-DR :146; T-TS :22.
- Evidence: REFERENCE_HASHES PRD `Match=NO`.
- Decisions: D-APP-38.

### DEL-08-03#CLM-031 — Boundary Rationale (SoW :512)
- Gist: Pipeline dispatch expresses intent only. Runtime authority stays with TASK/Type 2 checks (write scope, sealed context, no ghost inputs, fail-closed).
- Code: PDC:67-69 `PipelineDispatchIntent.executionAuthorized: false` REACH=TEST_ONLY; SG:196 REACH=LEGACY_ONLY; TD:635 REACH=LIVE (runtime delegate tool descriptor).
- Tests: T-B08 :28; T-PDC :54; `projects/chirality-runtime/tests/runtime-v3-api.test.ts` :602.
- Decisions: none specific (the governance rows are owned by DEL-08-05 / other PKG-08 deliverables).

### DEL-08-03#CLM-032 — Human Ruling Path (SoW :519)
- Gist: REF-006 source state and PRD-derived wording are both resolved by D-APP-38 (and ADQ-12).
- NO_CANDIDATES in code. REFERENCE_HASHES PRD `Match=NO`.
- Decisions: D-APP-38 (register :53).

### DEL-08-03#CLM-033 — Trade-offs (SoW :529)
- Gist: trade-off table: keep disabled variants visible, clear aggressively on reset, use canonical bucket terms, keep UI dispatch as intent only.
- Code: PS:70-102 `enabled:false` entries; PS:299-306; FS:214; PDC:69.
- Tests: T-PS :63; T-TS :22; T-B08 :28.

### DEL-08-03#CLM-034 — Examples (SoW :541)
- Gist: four scenarios: knowledge mode without a deliverable, root change clears selection, disabled future AUDIT variant, a doc-kit folder detected as buckets.
- Code: PS:771-807 REACH=LIVE; PDC:194 REACH=TEST_ONLY; PS:94 `AUDIT_OPTIONS` (ESTIMATES, SCHEDULES disabled); FS:214-240 (`Datasheet.md` matcher :227).
- Tests: T-PS :83; T-PDC :113; T-TS :22, :69; T-DR :146.

### DEL-08-03#CLM-035 — Conflict Table (SoW :553)
- Gist: CONFLICT-001: the former PRD source-state warning is resolved by D-APP-38.
- NO_CANDIDATES in code. REFERENCE_HASHES PRD `Match=NO`.
- Decisions: D-APP-38.

### DEL-08-03#CLM-036 — Assumptions (SoW :562)
- Gist: OBJ-001/007 relevance comes from the decomposition. Component and test paths are TBD until confirmed.
- Evidence: component/test paths are named elsewhere in the SoW (CLM-005/006) and exist at basis (PS, T-PS, T-TS, T-DR).

### DEL-08-03#CLM-037 — Pass 3 Disposition Notes (SoW :570)
- Gist: A-001, D-001 and E-002 are resolved by D-APP-38. C-001 and E-001 were incorporated as rationale.
- NO_CANDIDATES (method note).
- Decisions: D-APP-38.

---

## Cross-cutting (reach facts only)

- **Recurring modules:** PS `pipeline-surface.tsx` (REACH=LIVE; ~20 units), PDC `pipeline-dispatch-contract.ts` (REACH=TEST_ONLY; ~15), FS `lib/workspace/filesystem.ts` (REACH=LIVE; ~10), TS `lib/workspace/task-scope.ts` (REACH=LIVE; ~9), DP/RD `/api/project/deliverables` path (REACH=LIVE; ~7), WP `work-projection.tsx` (REACH=TEST_ONLY; ~6).
- **Live versus legacy split:**
  - PS is LIVE in the static map through `loop-shell`/`tertiary-sidebar-tabs` and `pipeline-client`. At both entry points the loop shell is only the `legacy` prop, which `WovenDialogueRoute` discards (`woven-dialogue-route.tsx:18`). T-WDS :156 asserts that no pipeline surface mounts.
  - PDC holds the presentation-neutral contract (`executionAuthorized:false`, disabled/target validation) and is TEST_ONLY. PS duplicates the option lists locally and does not import PDC.
  - The Work projection component is TEST_ONLY. The live Coordination Panel shows native harness-event work.
  - Subagent-governance enforcement in the frontend (`subagent-governance.ts`, `managed-delegation.ts`) is LEGACY_ONLY. The live delegation surface is the runtime `delegate_agent` descriptor (`tool-descriptor.ts`, LIVE).
  - Scope scan: the PS/DP path uses `/api/project/deliverables` (LIVE, tested by T-DR). `/api/working-root/scope` is LIVE, called only by `workbench-surface.tsx:212`, and untested.
- **Post-release:** no cited path appears in TOUCHED_PATHS.csv.
- **D-APP-127:** all DEL-08-03 carriers `Revised=NO`.
- **No REM units**, so there are no gate suffixes to quote.

#END
