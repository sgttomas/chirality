# Independent complete candidate review

Verdict: **CHANGES REQUIRED**. Three actionable P2 findings remain. This is independent engineering review, not owner acceptance, native qualification, or publication approval.

Reviewer: fresh TASK / Type 2, gpt-6-astra high, delegated-harness-native child `/root/candidate_independent_review` of `/root`; no delegation. Parent invoked the owner's bounded expert-review exception. Read/write limits were instruction-asserted within the host's actual permissions, not mechanically proved.

## Reviewed subject and coverage

Repository: `/Users/ryan/.codex/worktrees/chirality-ui-refinement-packaged-20260912/chirality`.
Frozen diff: `6ac4055690e20ddffd6aa5fff58a8e7ddd3c072f` → `4031c6c54f76760baaaf3d92e2db83819ce3a8ac`.

Reviewed all **98 changed/new files**, including actual product diffs, connecting callers and state/error paths, tests, instruction changes, workflow body/catalog/schema/index/validator changes, tranche manifest, routed notices, briefs, and returns. The coverage manifest below is the exact Git changed-file inventory. Later parent run records and this independent launch brief are not added to the frozen candidate. Author reports and test totals were read as evidence claims; they did not substitute for source review.

Main paths traced: App steering client → API → session router → scoped Runtime client → daemon journal/state check → delegated live worker → supervisor/native request; native notifications → event journal/replay → live and resumed transcript/activity; pending requests → shared subscriptions → inline/background cards and answer prevalidation; retained project binding, hydration and session-owner recovery; method catalog refresh, selection identity, quiet Plan refresh, retained document roots and rejected-send restoration.

## Findings

### F1 — P2: supported legacy native approvals have no actionable UI

Location: `projects/chirality-app-dev/frontend/src/components/shell/request-card.tsx:234–238`.

When Runtime lists `execCommandApproval` or `applyPatchApproval`, the new live reader recognizes approval only by the `/requestApproval` suffix. `classifyServerRequestMethod` returns either legacy method name unchanged (`src/lib/shell/harness-event-views.ts:329–334`), so the final allowlist removes the row. Meanwhile `PermissionRequests` now filters out every approval with `requestId`, removing the former actionable presentation too (`components/shell/permission-requests.tsx`, final return). Runtime explicitly retains both methods in `APPROVAL_REQUEST_METHODS` (`projects/chirality-runtime/packages/daemon/src/codex-supervisor.ts:35`) and emits their requestId-bearing permission events in `packages/core/src/delegated-engine-adapter.ts:296–313`.

Impact: a supported server request can remain waiting with neither an approval card nor a Needs answer indication; the user cannot approve or deny it through the new interface. This is a regression in the retained full-protocol compatibility path, not a claim that the modern v2 journey necessarily emits a legacy request.

Correction: classify every supported approval method consistently with Runtime before filtering, preserving one actionable card. Add focused coverage for both legacy methods in live inline and attention projections, including resolution/removal.

### F2 — P2: late steering receipt confirmation is unreachable from the App

Location: `projects/chirality-app-dev/frontend/src/components/shell/chat-panel.tsx:1306–1326` (especially the unknown-draft guard and unconditional new operation ID).

Trigger: the initial steering call records/returns unknown, then the matching native `userMessage.clientId` echo becomes durable after that call's final journal read. `NativeSteering.execute` checks such later evidence only when called again with the identical request (`projects/chirality-runtime/packages/daemon/src/native-steering.ts:68–80`). No event-driven reconciliation follows the initial return. The App never repeats that request: its only call generates a fresh operation ID, it disables the same unknown draft, and its receipt state omits `expectedTurnId`. Reopening reconstructs the last `codex.steer` status (`chat-panel.tsx:676–681`); raw userMessage echoes do not update this status in the App or transcript reducer. Thus the implemented Runtime reconciliation branch has no UI caller for this case.

Impact: an input that is now provably received remains unconfirmed in live/reopened UI, with the matching draft permanently blocked from Send even after the turn ends. Users cannot resolve the receipt through ordinary App controls. The existing Runtime test confirms the same-ID reconciliation capability; the App test only verifies that unknown disables the button, so it misses this integration gap.

Correction: retain/recover the full original request identity and provide a safe receipt refresh/reconciliation path, or reconcile on matching durable echo. Reconciliation must reuse the existing operation ID and expected turn and never dispatch the text again. Verify late echo after unknown, renderer reload, turn completion, and absence of confirming evidence; absence must stay unknown.

### F3 — P2: an unhealthy unrelated binding blocks uncached session-owner lookup

Location: `projects/chirality-app-dev/frontend/src/lib/runtime-client/daemon-harness-port.ts:437–446`.

Trigger: retain verified A then B; A later develops manifest drift or becomes inaccessible; request an uncached historical/native-child session owned by healthy B. The router probes retained ports in insertion order. `RuntimeDaemonHarnessPort.getSession` first calls `requireConfiguredProject` (`runtime-daemon-harness-port.ts:253–259,631–647`), so A fails with WORKING_ROOT_CONFLICT/WORKING_ROOT_INACCESSIBLE before its session lookup. The router rethrows every error except SESSION_NOT_FOUND and never checks B or invokes the existing authoritative `resolveSessionPort` fallback.

Impact: a valid B history/child request fails because a previously visited unrelated project is unhealthy. This applies to all session-routed operations while ownership is uncached and undermines the cross-folder isolation repair. Known-owner operations should still fail on their own project's drift; that enforcement is correct.

Correction: resolve authoritative ownership without requiring all unrelated cached projects to be healthy, or distinguish non-owning probe failures while preserving authorization/manifest validation of the actual owner. Do not weaken Runtime scope checks or reinterpret the actual owner's denial as success. Add a controlled A-drift/B-uncached regression and assert that B is used only after its own successful verification.

## Nonblocking limits and observations

- Native child observation ending with the primary turn is explicitly disclosed; missing later child evidence is not treated as completion. That bounded design is not an additional defect here.
- Only supplied reasoning summaries are selected for ordinary activity rendering; the new summary path excludes native reasoning content. Native message boundaries and completed snapshots share a reducer across live/replay.
- Workflow source identity, canonical package shape, optional role compatibility, the authoring pointer, catalog generation, and routed coordination remain consistent in the reviewed changes. Package build/discovery and real authoring/reuse remain parent checks.
- Rotating remembered-folder discovery can take roughly 245 seconds at the declared 50-root bound, plus request latency. The implementation return already records this polling limit. No broader notification architecture is demanded by this review.
- Real user journeys, stock-supplier behavior, account interaction, full suites/builds, and visual/focus behavior were not executed by this reviewer. Missing live proof remains unqualified. The parent is performing those checks separately.

## Verification and boundary

Source/Git inspection only; no product edits, Git mutations, full tests, builds, live UI/API/model/account operations, protected-state reads, or self-repair. This return is the sole write target. Focused existing tests were inspected rather than rerun, avoiding the parent's concurrent suites and shared build outputs. Findings are supported by concrete control flow and established interfaces; none is presented as a newly executed live reproduction.

APP-HOLD-1 review reliance check ran successfully at candidate HEAD for DEL-02-01, DEL-02-02, DEL-02-04, DEL-03-01, DEL-03-03: ALLOW, all CLEAR/NOT_HELD, no active holds. Entry `APP_V3_USER_JOURNEYS_20260912:INDEPENDENT_CANDIDATE_REVIEW`; register SHA-256 `d289b248a900122b012ae540b9b197feae3adbe264bf181f3d46556c500f320c`; scan fingerprint `0954ed105705301ccab40f3b6bcaed1fce542bc4f961055d40cc121b91b5dc29`.

Supplied instruction/brief origins and SHA-256:

- `AGENTS.md`: `c3fb6dbe394c168f75f12e761fce47b80a81ab9ae1bd41cfb0d28dd1e4003352`
- `projects/chirality-app-dev/AGENTS.md`: `3b1c1ffdc5d99b035bb08164cc3b6e1425e57431c89d22902f6ba88cbb3adb79`
- `projects/chirality-runtime/AGENTS.md`: `ca1b305c1fbc3ebc83e3718c6b2122170bbab3c1d1f616f744d0339f2a84691d`
- `agents/AGENT_TASK.md`: `1a13a5b00b3ce01ff8519efe6b46bcbe0cd6a5b7985e24282fa7efa2c57c8fb7`
- `.agents/skills/software-code-review/SKILL.md`: `06c27b1be5cfbd9e638570918a8f837d8439c8073c40d3ef708e53874f95570a`
- Campaign `briefs/INDEPENDENT_CANDIDATE_REVIEW.md`: `855bfbbebf77fb9dfa716dfc7cfa2e73457083fe36d0a69bb1b373d734c194ed`

## Handoff

Review work is complete; candidate fan-in is **not PASS** while F1–F3 remain unresolved. This is a derivative review of the two named immutable Git snapshots, not authoritative decomposition or owner acceptance. Parent owns disposition, separate-author fixes, focused regressions, independent re-review of the changed candidate, consolidated checks, remaining native journeys and qualified release handoff. No authority pointer moved. A changed candidate requires review of the repairs and their affected integration paths; prior source findings are not cleared merely by passing unrelated suites.

## Exact changed-file coverage manifest

- `AGENTS.md`
- `docs/governance_harness/tranche_manifests/APP-JOURNEYS-CORE-WORKFLOW-20260913.yaml`
- `projects/chirality-app-dev/AGENTS.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/JOURNEY_RESULTS.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/NATIVE_INTERACTIONS_PROPOSAL.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/PLAN.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/RUN_LOG.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/briefs/CHAT_ATTENTION_IMPLEMENTATION.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/briefs/CORE_WORKFLOW_REVIEW.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/briefs/CREATE_WORKFLOW.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/briefs/CROSS_FOLDER_SESSION_DIAGNOSIS.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/briefs/CROSS_FOLDER_SESSION_REPAIR.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/briefs/EARLY_ARTIFACT_REVIEW.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/briefs/EXPERIENCE_DESIGN.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/briefs/FIXTURE_AUTHORING.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/briefs/LIBRARY_UI_REPAIR.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/briefs/NATIVE_APP_IMPLEMENTATION.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/briefs/NATIVE_INTERACTIONS_PROPOSAL.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/briefs/NATIVE_PROTOCOL_MAPPING.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/briefs/NATIVE_RUNTIME_IMPLEMENTATION.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/briefs/UI_SOURCE_TRIAGE.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/returns/CHAT_ATTENTION_IMPLEMENTATION.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/returns/CROSS_FOLDER_SESSION_DIAGNOSIS.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/returns/CROSS_FOLDER_SESSION_REPAIR.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/returns/DESIGN_FAN_IN.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/returns/EARLY_ARTIFACT_REVIEW.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/returns/NATIVE_APP_FOCUSED_TESTS.txt`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/returns/NATIVE_APP_IMPLEMENTATION.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/returns/NATIVE_APP_REJECTED_SEND_TESTS.txt`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/returns/NATIVE_PROTOCOL_MAPPING.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/returns/NATIVE_RUNTIME_IMPLEMENTATION.md`
- `projects/chirality-app-dev/execution/_Coordination/NOTICE_2026-09-13_CORE_WORKFLOW_AUTHORING.md`
- `projects/chirality-app-dev/frontend/electron/main.ts`
- `projects/chirality-app-dev/frontend/src/__tests__/api/harness/daemon-proxy-boundary.test.ts`
- `projects/chirality-app-dev/frontend/src/__tests__/api/harness/fake-daemon-harness-port.ts`
- `projects/chirality-app-dev/frontend/src/__tests__/api/harness/turn-route-attachments.test.ts`
- `projects/chirality-app-dev/frontend/src/__tests__/components/chat-panel-folder-binding.test.tsx`
- `projects/chirality-app-dev/frontend/src/__tests__/components/chat-panel-turn-attach.test.tsx`
- `projects/chirality-app-dev/frontend/src/__tests__/components/live-session-requests.test.tsx`
- `projects/chirality-app-dev/frontend/src/__tests__/components/method-library-view.test.tsx`
- `projects/chirality-app-dev/frontend/src/__tests__/components/native-coordination.test.tsx`
- `projects/chirality-app-dev/frontend/src/__tests__/components/right-panel-method-refresh.test.tsx`
- `projects/chirality-app-dev/frontend/src/__tests__/components/woven-dialogue-shell.test.tsx`
- `projects/chirality-app-dev/frontend/src/__tests__/components/woven-right-panel.test.tsx`
- `projects/chirality-app-dev/frontend/src/__tests__/electron/directory-selection.test.ts`
- `projects/chirality-app-dev/frontend/src/__tests__/lib/native-progress.test.ts`
- `projects/chirality-app-dev/frontend/src/__tests__/lib/runtime-daemon-harness-port.test.ts`
- `projects/chirality-app-dev/frontend/src/__tests__/lib/woven-workspace-state.test.ts`
- `projects/chirality-app-dev/frontend/src/app/api/harness/session/[id]/turn/steer/route.ts`
- `projects/chirality-app-dev/frontend/src/app/globals.css`
- `projects/chirality-app-dev/frontend/src/components/shell/chat-panel.tsx`
- `projects/chirality-app-dev/frontend/src/components/shell/conversation-message.tsx`
- `projects/chirality-app-dev/frontend/src/components/shell/native-plan-panel.tsx`
- `projects/chirality-app-dev/frontend/src/components/shell/permission-requests.tsx`
- `projects/chirality-app-dev/frontend/src/components/shell/request-card.tsx`
- `projects/chirality-app-dev/frontend/src/components/shell/subagent-stream-view.tsx`
- `projects/chirality-app-dev/frontend/src/components/shell/turn-activity.tsx`
- `projects/chirality-app-dev/frontend/src/components/woven-dialogue/chat-attention.tsx`
- `projects/chirality-app-dev/frontend/src/components/woven-dialogue/coordination-panel.tsx`
- `projects/chirality-app-dev/frontend/src/components/woven-dialogue/method-library-view.tsx`
- `projects/chirality-app-dev/frontend/src/components/woven-dialogue/navigator.tsx`
- `projects/chirality-app-dev/frontend/src/components/woven-dialogue/right-panel.tsx`
- `projects/chirality-app-dev/frontend/src/components/woven-dialogue/woven-dialogue-shell.tsx`
- `projects/chirality-app-dev/frontend/src/lib/harness/client.ts`
- `projects/chirality-app-dev/frontend/src/lib/runtime-client/daemon-harness-port.ts`
- `projects/chirality-app-dev/frontend/src/lib/runtime-client/runtime-daemon-harness-port.ts`
- `projects/chirality-app-dev/frontend/src/lib/shell/harness-event-views.ts`
- `projects/chirality-app-dev/frontend/src/lib/shell/native-progress.ts`
- `projects/chirality-app-dev/frontend/src/lib/shell/turn-activity.ts`
- `projects/chirality-app-dev/frontend/src/lib/workspace/use-conversation-file-catalog.ts`
- `projects/chirality-app-dev/frontend/src/lib/woven-dialogue/contracts.ts`
- `projects/chirality-app-dev/frontend/src/lib/woven-dialogue/selected-session-replay.ts`
- `projects/chirality-app-dev/frontend/src/lib/woven-dialogue/woven-workspace-state.ts`
- `projects/chirality-app-dev/instructions/AGENTS.md`
- `projects/chirality-runtime/execution/_Coordination/NOTICE_2026-09-13_CORE_WORKFLOW_AUTHORING.md`
- `projects/chirality-runtime/packages/client/src/client.ts`
- `projects/chirality-runtime/packages/contracts/src/delegated.ts`
- `projects/chirality-runtime/packages/contracts/src/harness/event-schema.ts`
- `projects/chirality-runtime/packages/contracts/src/harness/transcript-replay.ts`
- `projects/chirality-runtime/packages/contracts/src/protocol.ts`
- `projects/chirality-runtime/packages/core/src/delegated-engine-adapter.ts`
- `projects/chirality-runtime/packages/core/src/delegated-runtime.ts`
- `projects/chirality-runtime/packages/daemon/src/codex-supervisor.ts`
- `projects/chirality-runtime/packages/daemon/src/native-steering.ts`
- `projects/chirality-runtime/packages/daemon/src/runtime-daemon.ts`
- `projects/chirality-runtime/packages/daemon/src/turn-registry.ts`
- `projects/chirality-runtime/tests/codex-supervisor.test.ts`
- `projects/chirality-runtime/tests/daemon.test.ts`
- `projects/chirality-runtime/tests/native-event-adapter.test.ts`
- `projects/chirality-runtime/tests/native-message-replay.test.ts`
- `projects/chirality-runtime/tests/native-steering.test.ts`
- `tools/validation/build_workflow_index.py`
- `tools/validation/test_workflow_catalog.py`
- `workflows/README.md`
- `workflows/catalog.schema.json`
- `workflows/catalog.yaml`
- `workflows/create-workflow/WORKFLOW.md`
- `workflows/index.json`
