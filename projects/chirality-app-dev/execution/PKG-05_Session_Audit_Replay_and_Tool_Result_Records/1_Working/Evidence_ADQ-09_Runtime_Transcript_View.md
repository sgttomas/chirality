# Evidence ADQ-09 - Runtime Transcript View

## Scope

ADQ-09 implements the G4 transcript view using existing replay/event data for DEL-05-04 Runtime Replay and Transcript View.

## Ruling / Authority Context

- D-APP-39 authorizes the autonomous development queue.
- D-APP-41 Option D is already applied: legacy flat session records convert eagerly to canonical folders, so replay resolves session metadata through the canonical session manager.
- D-APP-40 Option B is active: explicit user interruption is represented as terminal `turn.interrupted`; transcript projection preserves that terminal outcome.
- D-APP-38 authority corpus v2 is current for this deliverable; `_REFERENCES.md` reports `MATCH` for all listed authority references.

## Implementation

- Replay parser: `frontend/src/lib/harness/session-events.ts`
  - Reads canonical `.chirality/sessions/<sessionId>/events.jsonl`.
  - Preserves write order.
  - Counts malformed JSONL lines.
  - Applies read-time redaction to parsed replay records so imported/manual event logs cannot leak configured API keys.
- Transcript model: `frontend/packages/harness-contract/src/transcript-replay.ts`
  - Exports `TranscriptView`, `TranscriptItem`, `TranscriptSdkLinkage`, and `deriveTranscriptView(events, session?)`.
  - Projects user/assistant message events, accumulated assistant deltas, tool completions/failures, compact tool summaries, artifact links, terminal outcomes, diagnostics, and SDK linkage metadata.
  - Keeps SDK transcript/store fields as adapter metadata under `sdkLinkage`.
- Replay API: `frontend/src/app/api/harness/session/[id]/events/route.ts`
  - Validates the session id.
  - Resolves the canonical session record through `runtime.sessionManager.getById`.
  - Returns replay events, malformed-line count, summary, session metadata, and transcript projection.
- Sidebar UI: `frontend/src/components/shell/transcript-stream-view.tsx`; `frontend/src/components/shell/workspace-sidebar.tsx`; `frontend/src/components/shell/session-list-view.tsx`; `frontend/src/app/globals.css`
  - Adds the right-sidebar Transcript tab.
  - Renders transcript messages, terminal status, compact tool summaries, and artifact path/size/truncation metadata.
  - Updates session-open copy to point operators to Transcript / Tools / Subagents.
- Section 9 validation map: `frontend/scripts/validate-harness-section9.mjs`
  - Extends `section9.session_event_replay` with transcript projection coverage.
  - Adds `section9.sdk_session_link_resume` over SDK resume, canonical session migration, and transcript SDK linkage tests.

## Fixtures / Tests

- `frontend/src/__tests__/lib/transcript-replay.test.ts`
  - Proves message/tool/terminal transcript projection.
  - Proves accumulated assistant deltas when no completed assistant message exists.
  - Proves SDK linkage projection from `SessionRecord`.
- `frontend/src/__tests__/lib/session-events.test.ts`
  - Proves append/replay, malformed-line diagnostics, artifact references, and read-time redaction for imported/manual raw JSONL records.
- `frontend/src/__tests__/api/harness/routes.test.ts`
  - Proves the replay API returns ordered events, honest malformed-line count, canonical session metadata, and transcript items.
- `frontend/src/__tests__/components/harness-stream-views.test.ts`
  - Proves Transcript sidebar rendering, empty state, assistant text, tool artifact metadata, and terminal status.
- `frontend/src/__tests__/lib/session-manager.test.ts`
  - Proves D-APP-41 eager conversion remains available for replay-related session discovery.
- `frontend/src/__tests__/lib/sdk-options-builder.test.ts`
  - Proves SDK session resume option construction.

## Validation

Validation passed on 2026-06-21:

- `npm run test -- src/__tests__/lib/transcript-replay.test.ts src/__tests__/lib/session-events.test.ts src/__tests__/api/harness/routes.test.ts src/__tests__/components/harness-stream-views.test.ts src/__tests__/lib/harness-client.test.ts --testTimeout=30000`
  - Result: 5 files passed; 62 tests passed.
- `npm run typecheck`
  - Result: pass.
- `npm run harness:validate:section9`
  - Result: `HARNESS_SECTION9_STATUS=pass`; `HARNESS_SECTION9_TEST_COUNT=14`.
- `npm run harness:validate:section8`
  - Result: `HARNESS_VALIDATION_STATUS=pass`.
- `npm run test -- --testTimeout=30000`
  - Result: 78 files passed; 533 tests passed.
- `python3 execution/_Reconciliation/References/reconcile_authority_corpus.py status`
  - Result: corpus `v2`; all references `MATCH`; no drift.
- `git diff --check`
  - Result: pass.

## Residual Scope

No ADQ-09-specific transcript replay finding remains open. ADQ-10 remains responsible for DEL-05-05 checksum/retention and complete artifact metadata policy under D-APP-42 Option A.
