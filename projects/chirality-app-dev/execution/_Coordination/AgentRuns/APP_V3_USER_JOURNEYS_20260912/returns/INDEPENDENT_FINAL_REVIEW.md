# Independent final candidate review

Verdict: **PASS — no unresolved actionable engineering finding in the final candidate.**

Candidate: `46232f5f5c4b0e7aee8eb022fa11ebf54b1fb516`. Base: `6ac4055690e20ddffd6aa5fff58a8e7ddd3c072f`, verified as `origin/main` during review. This is independent source review, not owner acceptance, native qualification, approval to publish, or proof of all user journeys on this final revision.

Reviewer: TASK / Type 2, gpt-6-astra high, `/root/candidate_independent_review`, under the parent's standing bounded expert-review exception. No delegation. Source and Git were read-only; no repairs, builds, test suites, live UI/API/model/account operations, protected-state reads, or Git mutations. Only this separate final return was written. Both previous historical reviews remain unchanged.

## Complete coverage

The review covers all **135 unique changed paths** in the full base-to-candidate range, through these contiguous complete reviews:

| Frozen slice | Changed files | Review disposition |
| --- | ---: | --- |
| `6ac405569` → `4031c6c54` | 98 | Complete original review; F1–F3 reported |
| `4031c6c54` → `266c121bb` | 34 | Complete repair review; F1–F3 closed |
| `266c121bb` → `0b05fdfbb` | 29 | Complete native-child/progress and evidence review; raw-external attachment design held for replacement |
| `0b05fdfbb` → `0c07007b2` | 16 | Complete contained-copy repair review |
| `0c07007b2` → `46232f5f5` | 1 | Contained-copy component fixture correction reviewed |

Counts overlap; they are not added to invent a unique-file total. Actual diffs, all changed/new files, and connecting source were read. The binary-marked native-picker test was reviewed with text diff. This final review retains the prior complete coverage instead of rereading unchanged source. Its exact full-range manifest follows below; SHA-256 of the newline-delimited `git diff --name-only` output is `ac61c3ff0c737883cb3a074e21770b4426f2aaa4b20ade52d8122f8e3e363f0e`.

The original brief and Root/App/Runtime/TASK/software-code-review instruction basis remain as recorded in INDEPENDENT_CANDIDATE_REVIEW.md. Parent's subsequent dispatches expressly extended this same bounded review through the final repairs and authorized this return. No changed instruction basis was silently substituted.

## Finding dispositions and connected behavior

**F1 remains closed:** the shared live-request classifier recognizes every supported native approval method, including legacy execCommandApproval and applyPatchApproval. Inline cards and cross-chat attention use the classifier; the fallback avoids duplicate cards. Existing owner-session response routing remains intact.

**F2 remains closed:** unresolved steering retains operation ID, expected turn and original text before submission and across draft/replay recovery. Check delivery uses the separate receipt-only endpoint. The full App route/client/router/daemon/native-steering chain cannot dispatch or create an intent; a missing original intent stays unknown. Existing native echo matching, accepted/rejected outcomes, in-flight ordering, idle/recreated-manager reconciliation, stale-session protection and accepted-status non-downgrade remain intact. None of the later attachment or native-child edits alters this chain.

**F3 remains closed:** uncached owner discovery continues past only unrelated root-conflict/inaccessible probes while still validating the successful owner. Actual-owner drift and authorization/transport failures remain enforcing errors. Attachment containment uses the root of the session resolved through that owner path, not a root supplied in the turn body.

**Native-child projection repair is sound:** the Runtime adapter preserves both stock v2 subAgentActivity notification phases and their original id/kind/agentThreadId/agentPath. App normalizes new raw notifications and retained legacy-shaped native records into one row per Runtime session plus actual native child thread. Item IDs deduplicate lifecycle pairs rather than identify separate children. Kind started/completed/interrupted determines the corresponding observed status; interacted supplies no invented running/completed state. Empty-target waits and primary completion do not fabricate children or child completion. Supplied thread metadata and child messages merge into the same identity. Missing role, parent or result remains absent. Native rows appear as disclosures beside recorded Runtime hierarchy and never masquerade as selectable Runtime session IDs. Expanded activity retains command detail while compact progress uses the existing short activity title.

**Attachment selection trust finding is closed:** the old raw-external-path approach is superseded. The main-process handler obtains source paths only from the native dialog, captures project directory identity, and revalidates sender/root after the dialog. Shared validation checks normalized canonical nonsymlink regular files, supported extensions, per-file and batch budgets, descriptor identity and read stability. Copy publication uses private directories, captured directory guards, exclusive temporary files and no-overwrite linking. Each selected file has a host-random directory and its original basename, so equal names do not collide. The renderer receives only contained paths.

Runtime's entire source-path batch is lexically confined to the owning session's project before source resolution/open. Canonical and symlink checks then enforce that boundary before bytes are read. A forged external raw path, another project's selected copy, or an in-root symlink alias cannot reach the ordinary external import path. The existing resolver performs final session-scoped hashed custody and keeps names/hash/size history. The delegated adapter still validates contained file inputs and recorded hashes/sizes before stock projection; source folder access and Codex policy are unchanged.

Traced native picker → preload → attachment chip/draft → turn request → session owner routing → Runtime resolver → delegated adapter. Original basenames work with existing buildUiAttachment and replay, avoiding hash-only names or a turn-schema change. The current project/draft/generation guard rejects late picker outcomes. Selection copies precede first session creation and persist independently of handler lifetime. Original source edits after selection cannot change the selected snapshot, and failed-send restoration retains the contained path for retry. Browser fallback remains project-contained selection. Electron's existing Runtime source-resolution plugin includes the newly exported shared helper; no new package-resolution mechanism is assumed.

The final fixture file was initially left uncommitted while its return/hash manifest described the edited bytes. This was reported to the parent and closed by `46232f5f5`. Its committed six-line fixture replacement is reviewed; all ten hashes in ATTACHMENT_CONTAINED_COPY_SOURCE_HASHES.json now match final source. This is a resolved snapshot discrepancy, not an outstanding product defect.

## Verification and evidence calibration

No redundant suites were run by this reviewer. Controlled tests were inspected for meaningful assertions, including real temporary files through the actual picker handler and App-owned service with fake stock transport, original-source edits, same names, retry, forged external/cross-project paths, symlinks, budgets, destination collision, and special-file no-open checks. Native-child tests exercise raw/retained pairs, empty-target waits, distinct identities and absent terminal evidence. Prior approval/receipt/routing coverage remains applicable to unchanged source.

Parent reports full Runtime **39 files / 364 tests PASS** on the final contained-copy source. Author reports final focused Runtime **24 tests PASS**, App **22 tests PASS**, Runtime TypeScript build and App/Electron typecheck PASS; the App typecheck preceded the last internal regular-file prechecks, which did not change exported types. The previous full frontend **2228 pass / four skip** and Runtime **360 pass** totals belong to `0b05fdfbb`. Parent subsequently reports the final frontend suite **218 files passed / one skipped; 2223 tests passed / four skipped**. The lower final count reflects rewritten/replaced raw-import tests, not an inferred production regression. These are attributed execution results, not tests independently rerun by this reviewer.

Journey and artifact returns distinguish fictional substantive-output quality, observed UI behavior, source defects, automation limitations and remaining qualification. They preserve earlier failed runs and do not promote artifact correctness into proof that every final native surface works. Those reports were read as evidence; their external live/profile/session stores were not accessed. Native stock-kind semantics were checked against the retained pinned-source diagnosis and matching producer-shaped fixtures; no new supplier study or live protocol probe was performed.

APP-HOLD final-review reliance check passed ALLOW, all CLEAR/NOT_HELD at the final candidate for DEL-02-01, DEL-02-02, DEL-02-04, DEL-03-01, DEL-03-03 and DEL-09-06. Entry: `APP_V3_USER_JOURNEYS_20260912:INDEPENDENT_FINAL_REVIEW`. Register SHA-256: `d289b248a900122b012ae540b9b197feae3adbe264bf181f3d46556c500f320c`. Scan SHA-256: `543a2272b489b62bda5db44c2fdd06c9f6da5fe8f7a47aedaf80b4b0525b6811`. No governance acceptance or pointer update follows from that check.

## Residual limits and handoff

- Selected copies intentionally remain on disk after chip removal, failed send and restart. Automatic reclamation is outside this MVP; repeated selections consume project disk space. They are ordinary project-contained data, not an assertion of per-chat filesystem secrecy.
- A native selection snapshots bytes at Attach. Runtime revalidates the contained copy at Send; edits to the original source require another attachment selection. Final custody retains its existing integrity checks.
- Native descendant evidence remains bounded by the primary observer's lifetime. Unknown result/status is not proof of success, and observed thread identity is not a fabricated managed session. This review does not extend observation.
- Receipt recovery is best-effort when browser storage is unavailable; missing canonical intent remains unknown. Cross-project attention retains the previously recorded polling latency.
- Final native inside/outside selection, filename/retry/history behavior, viewer refresh and repaired child UI still need the parent's direct rechecks on the final candidate. Packaging, signing, installer acceptance, notarization and publication remain separately qualified.

Independent engineering review is complete with no unresolved actionable finding for the cited candidate. This return is derivative evidence over immutable Git snapshots and the earlier review records, not authoritative decomposition truth. Parent owns native rechecks and qualified release handoff. Material subsequent source or integration changes require affected-scope review.

## Exact full-range path manifest

- `AGENTS.md`
- `docs/governance_harness/tranche_manifests/APP-JOURNEYS-CORE-WORKFLOW-20260913.yaml`
- `projects/chirality-app-dev/AGENTS.md`
- `projects/chirality-app-dev/docs/PRD.md`
- `projects/chirality-app-dev/docs/SPEC.md`
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
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/briefs/INDEPENDENT_CANDIDATE_REVIEW.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/briefs/LIBRARY_UI_REPAIR.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/briefs/NATIVE_APP_IMPLEMENTATION.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/briefs/NATIVE_INTERACTIONS_PROPOSAL.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/briefs/NATIVE_PROTOCOL_MAPPING.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/briefs/NATIVE_RUNTIME_IMPLEMENTATION.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/briefs/UI_SOURCE_TRIAGE.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/returns/ATTACHMENT_CONTAINED_COPY_RETURN.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/returns/ATTACHMENT_CONTAINED_COPY_SOURCE_HASHES.json`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/returns/ATTACHMENT_REPAIR_RETURN.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/returns/ATTACHMENT_SCOPE_ASSESSMENT.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/returns/ATTACHMENT_SELECTION_TRUST_ASSESSMENT.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/returns/CHAT_ATTENTION_IMPLEMENTATION.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/returns/CROSS_FOLDER_SESSION_DIAGNOSIS.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/returns/CROSS_FOLDER_SESSION_REPAIR.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/returns/DESIGN_FAN_IN.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/returns/EARLY_ARTIFACT_REVIEW.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/returns/INDEPENDENT_CANDIDATE_REVIEW.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/returns/INDEPENDENT_REPAIR_REVIEW.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/returns/J02_J05_ARTIFACT_REVIEW.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/returns/J04_ARTIFACT_REVIEW.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/returns/J06_J08_ARTIFACT_REVIEW.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/returns/J07_THREE_CYCLE_REVIEW.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/returns/NATIVE_APP_F1_F2_REPAIR.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/returns/NATIVE_APP_F1_F2_TESTS.txt`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/returns/NATIVE_APP_FOCUSED_TESTS.txt`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/returns/NATIVE_APP_IMPLEMENTATION.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/returns/NATIVE_APP_REJECTED_SEND_TESTS.txt`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/returns/NATIVE_CHILD_LIVE_DIAGNOSIS.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/returns/NATIVE_CHILD_PROGRESS_REPAIR.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/returns/NATIVE_PROTOCOL_MAPPING.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/returns/NATIVE_RUNTIME_IMPLEMENTATION.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/returns/STOP_READONLY_DIAGNOSIS.md`
- `projects/chirality-app-dev/execution/_Coordination/NOTICE_2026-09-13_CORE_WORKFLOW_AUTHORING.md`
- `projects/chirality-app-dev/frontend/electron/attachment-picker.ts`
- `projects/chirality-app-dev/frontend/electron/main.ts`
- `projects/chirality-app-dev/frontend/electron/preload.ts`
- `projects/chirality-app-dev/frontend/src/__tests__/api/harness/daemon-proxy-boundary.test.ts`
- `projects/chirality-app-dev/frontend/src/__tests__/api/harness/fake-daemon-harness-port.ts`
- `projects/chirality-app-dev/frontend/src/__tests__/api/harness/turn-route-attachments.test.ts`
- `projects/chirality-app-dev/frontend/src/__tests__/components/chat-panel-folder-binding.test.tsx`
- `projects/chirality-app-dev/frontend/src/__tests__/components/chat-panel-native-attachments.test.tsx`
- `projects/chirality-app-dev/frontend/src/__tests__/components/chat-panel-turn-attach.test.tsx`
- `projects/chirality-app-dev/frontend/src/__tests__/components/live-session-requests.test.tsx`
- `projects/chirality-app-dev/frontend/src/__tests__/components/method-library-view.test.tsx`
- `projects/chirality-app-dev/frontend/src/__tests__/components/native-coordination.test.tsx`
- `projects/chirality-app-dev/frontend/src/__tests__/components/right-panel-method-refresh.test.tsx`
- `projects/chirality-app-dev/frontend/src/__tests__/components/woven-dialogue-runtime-reconnect.test.tsx`
- `projects/chirality-app-dev/frontend/src/__tests__/components/woven-dialogue-shell.test.tsx`
- `projects/chirality-app-dev/frontend/src/__tests__/components/woven-right-panel.test.tsx`
- `projects/chirality-app-dev/frontend/src/__tests__/electron/attachment-picker.test.ts`
- `projects/chirality-app-dev/frontend/src/__tests__/electron/directory-selection.test.ts`
- `projects/chirality-app-dev/frontend/src/__tests__/integration/pi-omlx-wire.integration.test.ts`
- `projects/chirality-app-dev/frontend/src/__tests__/lib/native-progress.test.ts`
- `projects/chirality-app-dev/frontend/src/__tests__/lib/runtime-daemon-harness-port.test.ts`
- `projects/chirality-app-dev/frontend/src/__tests__/lib/turn-activity.test.ts`
- `projects/chirality-app-dev/frontend/src/__tests__/lib/woven-workspace-state.test.ts`
- `projects/chirality-app-dev/frontend/src/__tests__/scripts/prepare-packaged-instruction-root.test.ts`
- `projects/chirality-app-dev/frontend/src/__tests__/scripts/verify-instruction-root-integrity.test.ts`
- `projects/chirality-app-dev/frontend/src/app/api/harness/session/[id]/turn/steer/receipt/route.ts`
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
- `projects/chirality-app-dev/frontend/src/lib/shell/steering-receipts.ts`
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
- `projects/chirality-runtime/packages/core/src/attachment-copy.ts`
- `projects/chirality-runtime/packages/core/src/delegated-engine-adapter.ts`
- `projects/chirality-runtime/packages/core/src/delegated-runtime.ts`
- `projects/chirality-runtime/packages/core/src/index.ts`
- `projects/chirality-runtime/packages/core/src/runtime-attachment-resolver.ts`
- `projects/chirality-runtime/packages/daemon/src/app-owned-composition.ts`
- `projects/chirality-runtime/packages/daemon/src/codex-supervisor.ts`
- `projects/chirality-runtime/packages/daemon/src/native-steering.ts`
- `projects/chirality-runtime/packages/daemon/src/runtime-daemon.ts`
- `projects/chirality-runtime/packages/daemon/src/turn-registry.ts`
- `projects/chirality-runtime/tests/app-owned-composition.test.ts`
- `projects/chirality-runtime/tests/attachment-copy.test.ts`
- `projects/chirality-runtime/tests/codex-attachment-adapter.test.ts`
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
