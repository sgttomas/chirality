# Sealed TASK author brief v1
PURPOSE: Implement DEL02-04-V3-01 additive workspace-state fields only.
RequestedBy: WORKING_ITEMS PKG02
CHIRALITY_INSTRUCTION_ROOT: {REPO_ROOT}
WorkingRoot: {REPO_ROOT}/projects/chirality-app-dev
ScopePath: {WORKING_ROOT}/execution/_Coordination/AgentRuns/APP_LOOP_SHELL_2026-09-05/iteration-03/instances/pkg02_fields/author
TaskSkill: software-bounded-implementation
PackageID: PKG-02
DeliverableIDs: [DEL-02-04]
ApplyEdits: true
PROFILE_PATH: {WORKING_ROOT}/software-workflow.json
Objective: Complete only additive convenience-state field contract within two source files.
AcceptedBasis: root/project AGENTS; agents/AGENT_TASK.md; software skill contracts; docs/SOFTWARE_WORKFLOW_PROFILE.md; DEL02-04 ScopeOfWork.md controlling SCA-APP-010 section and _STATUS.md Remaining; iteration-03 INPUT_IDENTITIES.json, IMPLEMENTATION_PLAN_APPROVED_v2.md and preserved IMPLEMENTATION_PLAN_DRAFT_v1.md; manager RATIONALE_v1.md; target spec section12 and section5.10; committed dependency015 and CI basis.
AllowedWriteTargets:
 - {WORKING_ROOT}/frontend/src/lib/woven-dialogue/woven-workspace-state.ts
 - {WORKING_ROOT}/frontend/src/__tests__/lib/woven-workspace-state.test.ts
 - {ScopePath}/**
AllowedTools: bounded file editors/read-only shell; repository software_workflow helpers; APP-HOLD tool; focused existing frontend-test command npm test -- src/__tests__/lib/woven-workspace-state.test.ts only (parent-authorized specialization of registered frontend-test).
RuntimeOverrides: instruction root explicitly declared above; delegated-harness-native; role instruction-asserted; no delegation. Exact serving model ID unavailable; record only actual known identity.
Tasks:
 - Normalize TASK, load actual shell/skill, run APP-HOLD dispatch/reliance for DEL-02-04 before effect. Parent preflight is additional evidence, not a substitute.
 - Inspect existing module/test/callers. Implement approved plan exactly, preserving old exported API compatibility within the two-file fence. New normalized return type may coexist with backward-compatible accepted input type if necessary; no caller edits. Report true conflict instead of broadening.
 - New views files|workflows|agents|activity|settings. Width keys additionally document/session; valid finite clamp280..2000, missing keys absent. Defaults empty/null/false. Missing view maps legacy agents→agents else files; invalid-present→files.
 - Add rightPanelExpanded, preExpandState, openDocumentPath, chatTitles(cap500), chatPins/chatArchived/chatGroups/groupsCollapsed(cap200), knownRoots(cap50), chatRung(cap500; optional ref/declined cap200). Field shapes as target section12. All new reference identities bounded2048, reject invalid/oversized values; preserve meaningful path/identity whitespace, trim labels. Legacy readReference/readReferenceArray and old-field behavior unchanged. Opaque keys including __proto__/constructor must behave as own data without prototype pollution or inherited lookups.
 - knownRoots valid ISO timestamps, dedup paths by newest timestamp and sort newest first. Missing field only seeds chirality.projectRoot once and persists observation timestamp/decision; explicit empty or invalid-present suppress reimport. Keep old key. Isolate read/write failures, retain valid current state. No network/filesystem verification or authority from hints. Never persist activeChatRoot.
 - Clear new document/chat fields on project clear including titles/rungs/groupsCollapsed; retain app roots/layout/theme/legacy attribution. Preserve original schema/key/migration/theme-writer precedence. Record rollback limitation: old writer can discard new fields.
AcceptanceCriteria:
 - Existing typed callers remain compatible; no source outside two-file fence.
 - Meaningful tests old-v1 migration; absent vs invalid-present; new/legacy precedence; all width classes; malformed data/prototype keys; bounds/dedup/eviction; project clearing; one-time seed and storage exceptions; normalized roundtrip; no activeChatRoot; legacy behavior and theme preservation.
 - Run focused test with actual output JSON, select affected checks and validate scope; parent runs globals after freeze. No global typecheck/build/full suite concurrently.
ExpectedOutputs: TASK run record; author RETURN.md, COMMANDS.json exact commands/cwd/exit/output, SOURCE_MANIFEST.json, changed paths and partial residuals. Freeze product after return. No anticipated PASS.
ExpectedReturn: implemented paths/hashes, tests actual outcome, rationale or deviations, scope proof, blockers and residuals.
EXCLUSIONS: all other product files; dependency files; deliverable carrier records (manager owns); Root; UI/Activity strip/view; runtime/provider/network/install; lifecycle/pointers/owner acts; git index/commit/push; child delegation. No temp writes outside own ScopePath. Drafts and manager evidence read-only. No UI render or full-item closure claim.
