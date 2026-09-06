# Independent whole-candidate revision 10 review

RUN_STATUS: SUCCESS
SourceVerdict: PASS
ActionableFindings: none
FullItemStatus: PARTIAL
ControlSurface: MERGED
TaskProfile: NONE
TaskSkill: software-code-review
ScopePath: /Users/ryan/.codex/worktrees/85d6/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_LOOP_SHELL_2026-09-05/iteration-04/instances/pkg02_t3/recovery-reviewer-v10
ResolvedSkillPath: /Users/ryan/.codex/worktrees/85d6/chirality/skills/software-code-review
ResolvedSkillVersion: 1
ResolvedTaskProfileRequirement: NONE
CompanionFiles: BRIEF_SCHEMA.md (found), TOOL_POLICY.md (found), QA_CHECKS.md (found)
AllowedTools: sealed read/bash, bounded reviewer evidence; read-only Git; scope/check-selection helpers and explicit APP-HOLD checks.
RuntimeOverrides: source read-only; current output directory is ScopePath. Original author/reviewer briefs supply CHIRALITY_INSTRUCTION_ROOT={REPO_ROOT}; environment absence already calibrated in v9. Same actual independent reviewer resumed; no implementer context.
ToolsUsed: zsh cat/sed/rg; read-only git rev-parse/show; python3 inline identity/diff/evidence processing; python3 tools/software_workflow/validate_change_scope.py; python3 tools/software_workflow/select_affected_checks.py; python3 execution/_Scripts/app_hold.py; python3 recovery-reviewer-v10/recompute.py.
ToolPolicyCompliance: PASS. No source/global/build/native/browser/server/provider/network/Git mutation, process control or descendant/sibling communication. Initial author RETURN read raced its appearance; subsequent actual RETURN read succeeded. Evidence-only changes.
WriteAuthorization: EXPLICIT_BRIEF_TEXT — recovery-reviewer-v10/** only.

## Whole-source identity, coverage and basis

Manifest SHA-256 c88cce09a9ad4ea9c9f822d5f410b26e1f04e7c02067ff1398ecf6bcacc807e4; full diff JSON SHA-256 d9e0d2e8ba11f47ddeab5ca236bc612a519a3840a5ceab0bf07c30cd7a226772. All 18 current byte identities match at initial and final checks. Independently regenerated all 18 full diff entries against base 239c8f2a53397f88f16e3d56ecbba9af83829246: 15 nonempty, 3 empty, every string matches. Exact set equals AUTHOR_SOURCE_INVENTORY_v2, with the previously authorized reconnect-test addition. Scope and affected-check helpers pass. Fresh dispatch/reliance and final reliance APP-HOLD all ALLOW/exit 0.

Coverage is 100% of the whole frozen source/diff, with calibrated reuse: the two changed files were fully reread now; all 16 unchanged files were fully directly read by this same independent reviewer during v9 in this retained context. Their exact bytes and complete base diff were reverified, their operative regions/test assertions reread, and their behavior reconsidered as a whole against the hydration failure/repair. This is not a claim of 18 new complete text reads in this turn, nor reliance on a prior PASS without source inspection. COVERAGE.json identifies each file and provenance. Prior full review return SHA is b8601823189d3e08109edc1a9110c2434ea5dfa80f990d1197681289881bb1af, pinned in UPSTREAM_PINS.json.

Root/App AGENTS, TASK/skill/companions, profile, actual SOW/Remaining, author brief, v8/v9 history, desktop repair/finding, D64/D108 and amendments remain read in this review context. New reads include complete hydration amendment, actual native failed result, production capability diagnostic, actual author return/test outputs, current FileTreePanel/test and WorkspaceProvider. Original native error strings lack stack/time; separate diagnostic provides them. No parent global result is presumed.

## Source assessment

No actionable finding. FileTreePanel.tsx lines 93–96 and 276–280 fix the specific SSR/native-first-client structural mismatch without changing WorkspaceProvider. Provider starts projectRoot and errorMessage at null but calculates native picker capability from window during render. Previously that true/false difference removed the fallback paragraph and changed disabled on the first native client render. The new local mounted=false is identical on server and first client; both outputs retain disabled chooser and fallback paragraph. The passive effect then enables the chooser only when the real capability exists. It never invokes chooseProjectRoot on mount, affects no provider/account policy and requires no suppressHydrationWarning or error suppression. Browsers without a picker retain fallback after mounting. Collapse/reopen or Refresh remounts may briefly show the deterministic fallback until the effect; file/root state and polling remain unchanged.

The complete new test file keeps its prior file-click, legacy inert-file, directory toggle, chooser, arrow focus and separate footer/list assertions. Its new first-client test deliberately captures the synchronous host tree before passive effects and compares complete rendered markup to SSR; then flushes effects and verifies enabled native callback. The browser test preserves disabled/fallback after mount. afterEach resets changed mocked capability/root and chooser calls. Author command npm test -- src/__tests__/components/file-tree-panel.test.tsx passed 5/5, exit 0; actual FOCUSED_TEST.json plus stdout/stderr consumed, not rerun. This test proves the targeted initial structure and effect behavior, not actual production hydration.

Whole candidate reconsidered: RightPanel and Navigator instantiate FileTreePanel in both locations, so the local fix covers both native first-render trees while retaining the three-row header/body/footer layout. RightPanel future-view fallback, file/document breadcrumbs, native menu payloads, clipboard generations and guarded parent metadata remain source-coherent. Woven shell's primary ChatPanel mount, replay/live-turn selection guards, reconnect list/reload behavior, per-view widths and expansion restoration remain unchanged. Desktop real-plus controls still have full accessible names, 42px controls/56px rails, generated-plus suppression and scoped visible ink; stacked text reentry and auto compact extent stay intact. No globalCSS/state-module edit occurred.

The retained full API/IPC candidate remains coherent: lexical/canonical/instruction-root and narrow .git checks, regular-file descriptor binding/inode rechecks, truthful error paths, bounded text input, streamed uncapped PDF, separately bounded images, nosniff/attachment handling and read-only GET. Electron registration is after rendererOrigin, uses actual sender authorization and explicit native actions, with descriptor cleanup and handler removal. DocumentView retains legacy calls, target-keyed asynchronous results, safe Markdown/local links, bounded JSON/CSV and img-only SVG. Browser-only PDF frame behavior and native capability false remain intentionally distinct. Source/test changes introduce no dependency, schema/migration, generated artifact, shared provider, policy, Root or ownership modification.

## Residuals and handoff

The actual native-v9-host result is FAIL with two React418 entries despite successful action entries; it does not prove Quick Look visual display. The separate production diagnostic recorded zero baseline errors and one418 with an inert native capability, consistent with the source mismatch. NATIVE_HYDRATION_AMENDMENT_v10.json SHA db4e62098166ffcd12d02fde281cf6432d8aad11be564b8a81d9fc1bf1c4bea7 records owned cleanup and bounded repair. Those failed historical artifacts remain unchanged.

Parent must rerun actual production hydration with and without desktop capability, then actual isolated native Office/PDF/default-app/Finder behavior with display and cleanup evidence. Current required global/build/premerge/browser geometry/visible-affordance/integrated/exact-source CI gates and A1 restage remain parent-owned. Source PASS does not assert their outcomes. Desktop/stacked layouts and primary identity still require actual proof under the new build; earlier failures cannot be retroactively made PASS.

D108 native in-panel PDF remains unresolved under unchanged frame policy; the truthful default-app fallback remains partial under the accepted bounded amendment, not a policy or owner waiver. Native final pathname races and decoded-image resource bounds remain disclosed residuals, not newly accepted. Menu-only Reveal placement does not establish duplicate handoff-card placement completeness. Full T3/package/lifecycle/CheckingSHA/dependency/pointer/acceptance remains held.

## D64 decision

OwnerStandingApproval: D-APP-64 §3 through parent sealed review activation.
AgentJudgment: SELECT_AND_ADVANCE
SelectedOutcome: whole frozen v10 source PASS; source repair addresses the identified hydration mismatch; advance to required parent current checks/proof with full-item partial status.
JudgedBy: TASK Agent2 /root/pkg02_finish/desktop_reopen_reviewer; actual reused independent reviewer.
OwnerCaseSelection: NONE
RejectedAlternatives: review only two paths; treat old PASS as current acceptance; mask418; change shared WorkspaceProvider; infer native display from callbacks; waive PDF or prior visual failures. Each exceeds scope or evidence.
RationaleArtifact: /Users/ryan/.codex/worktrees/85d6/chirality/projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_LOOP_SHELL_2026-09-05/iteration-04/instances/pkg02_t3/recovery-reviewer-v10/REVIEW_RETURN.md
IndependentVerifier: this actual independent full-candidate source judgment complete; parent governed refutation and current actual browser/native/integrated/CI still pending; no COMMIT-SAFE claimed.
EffectStatus: HELD
PreservedGates: D64 §5.1 classes1–10/F-APP1–5, exact18source/scope, APP-HOLD, registered global/build/premerge/render/native/integrated/exact-source CI and A1restage; no owner/lifecycle/CheckingSHA/dependency/pointer/Root/provider/policy/release/merge/external-commitment/protected-data effect or waiver.
DraftEffects: new bounded reviewer evidence only; product frozen and governed acceptance held.
Ontology: SSR/first-client structure, postmount capability, native action and visible native display are separate properties.
Epistemology: actual complete-source provenance, exact hashes/diff and targeted structural test warrant source PASS; historical failure and current source do not establish repaired runtime success.
Praxeology: immutable review plus parent global checks may overlap on frozen bytes; parent follows with actual production hydration/native proof and gated fan-in. Any source drift invalidates current identity-based reliance.
Axiology: preserve native folder access and recoverable UI with truthful browser fallback, independent verification and unchanged authority/policy.

Attribution: Codex desktop native descendant; GPT-6 model family as declared by current session instructions; exact serving model/provider identifiers unavailable, not invented. No substitution observed. delegated-harness-native TASK Agent2, instruction-asserted/role not mechanically enforced; no descendants.
Outputs: REVIEW_RETURN.md, COVERAGE.json, IDENTITY_START.json, IDENTITY_FINAL.json, SCOPE_CHECK.json, CHECK_SELECTION.json, APP_HOLD_dispatch.json, APP_HOLD_reliance.json, APP_HOLD_reliance_final.json, RECOMPUTE_RESULT.json, COMMANDS.json, UPSTREAM_PINS.json, RUNTIME_ATTRIBUTION.json, recompute.py, EVIDENCE_INVENTORY.json and _run_records/TASK_RUN_2026-09-06_review_v10.md.
AppliedChanges: bounded review evidence only.
ProposedChanges: none.
MISSING: current parent production hydration/native/visual/global/integrated/CI proof and full native inline PDF fulfillment.
NEEDS_HUMAN_RULING: none for bounded review; existing proposals remain parent-owned.
DEPENDENCY_NOTES: derivative evidence package; accepted SOW/Remaining/D108 remain authority, exact v10 source manifest/full diff are reviewed snapshot. No new cycle discovered or dependency acceptance performed.
HandoffState: SOURCE_PASS / FULL_ITEM_PARTIAL / GOVERNED_EFFECT_HELD. Recompute using read-only recompute.py; source drift requires review renewal. Parent owns remaining gates and closure. No full T3 acceptance.
