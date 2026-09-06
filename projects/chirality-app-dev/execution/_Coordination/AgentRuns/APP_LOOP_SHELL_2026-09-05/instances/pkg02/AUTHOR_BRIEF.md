# Sealed TASK implementation brief v1

RequestedBy: WORKING_ITEMS / pkg02, activated by HELP_HUMAN after selection COMMIT-SAFE.
RunID: APP_LOOP_SHELL_2026-09-05
ParentInstanceID: pkg02
ChildInstanceID: pkg02/author
PackageID: PKG-02
DeliverableIDs: DEL-02-02 (Remaining DEL-02-02-V3-03 only)
TaskSkill: software-bounded-implementation
ApplyEdits: true
RuntimeClass: delegated-harness-native; role instruction-asserted; no Agent 2 delegation.

Resolve REPO_ROOT through git rev-parse --show-toplevel; WORKING_ROOT is projects/chirality-app-dev beneath it. ScopePath is this brief's sibling author directory. PROFILE_PATH is WORKING_ROOT/software-workflow.json.

## Objective and accepted basis

Implement T1 centre invariance and retirement only. Read root and project AGENTS, AGENT_TASK, skill and companion files, live deliverable _STATUS/ScopeOfWork/Dependencies, D-APP-108 Q3, accepted DepClosure CLOSURE_SCC-DECOMPOSE-SCA-APP-010_2026-09-05_1034, and pinned plans/shell-redesign_2026-09-04/04_IMPLEMENTATION_PLAN.md (e25fbe82f675e9f282803599a497ab24c6aab3f763b1e7f6db97042fed1117bb) T1. SOW controlling Gate-5 contract and live Remaining govern over historical clauses. Depends none for V3-03. Parent's run base is 044a009e215e08b69c9e0887da424938a34aafcb.

Keep the primary dialogue always visibly mounted, same controller identity and focusable composer. Remove focused Workbench/Pipeline mounts. Put existing replay lens into interim Session view beside the primary, with Agents view available; opening replay opens the coordination panel. Unmount WorkProjection, retaining component and empty-source test. Navigator shows Dialogue and flat updatedAt-sorted recorded sessions, including historical surface annotations, with no Workbench/Pipeline entries or mode chevrons. Keep compatibility state readers and old types unchanged; active-shell writers record dialogue. Retired route clients wrap WovenDialogueRoute: return their existing legacy slot for a non-dialogue defaultSurface so /workbench and /pipeline remain functional by URL. No route-file edits.

## DeclaredReads and AllowedTools

Read pertinent project components, tests, state/replay contracts, governing docs and helper sources; git diff/status. Local read/edit/bash tools and software_workflow scope/check helpers. No installs, network, provider use, release, git mutation or delegation. APP-HOLD-1 dispatch preflight before work. Parent owns global checks: do not run npm test/typecheck/build/premerge/release-quality. Focused test command may run only after manager confirms dependencies ready: npm exec vitest run src/__tests__/components/woven-dialogue-viewport.test.tsx src/__tests__/components/woven-dialogue-shell.test.tsx src/__tests__/components/woven-dialogue-route.test.tsx src/__tests__/components/woven-dialogue-navigator.test.tsx src/__tests__/components/woven-dialogue-controls.test.tsx (and new bounded woven-dialogue tests). Preserve canonical command/output/exit in author records. This focused command is explicitly authorized by the owning T1 validation contract.

## AllowedWriteTargets

Relative to WORKING_ROOT:
- frontend/src/components/woven-dialogue/dialogue-viewport.tsx
- frontend/src/components/woven-dialogue/woven-dialogue-shell.tsx
- frontend/src/components/woven-dialogue/woven-dialogue-route.tsx
- frontend/src/components/woven-dialogue/navigator.tsx
- frontend/src/components/woven-dialogue/coordination-panel.tsx
- frontend/src/__tests__/components/woven-dialogue-*.test.tsx except woven-dialogue-work-projection.test.tsx (retain unchanged)
- execution/_Coordination/AgentRuns/APP_LOOP_SHELL_2026-09-05/instances/pkg02/author/**

EXCLUSIONS: all other writes; Root; IPC/harness/runtime/semantic replay/state libraries; legacy route files; WorkProjection; full T3 switcher, workflow, new expand feature; CSS retirement cleanup; lifecycle/Remaining state and parent/global evidence writes. Report needed scope amendment, do not infer it.

## AcceptanceCriteria and ExpectedReturn

Component tests prove no focused surface or retired navigation/mount, primary never hidden or replaced under replay selection/return and existing resize/collapse-expand, recorded sessions remain selectable with streaming guards, retired URL wrappers render their retained surfaces. Preserve transient replay errors/loading/disclosure and no inferred authority/parentage. Tests must exercise shell transitions, not merely static viewport props. Browser proof is manager-owned after author freezes.

Return changed-file list, behavioral rationale, focused evidence (or precise dependency blocker), write-scope validation against this list, exact residual risks, required follow-ups and model attribution only if exposed. Put run record under author/_run_records. Do not claim acceptance, final gate PASS, merge or issuance. Return terminal then stop writing so manager can freeze 100% diff for fresh independent reviewer.
