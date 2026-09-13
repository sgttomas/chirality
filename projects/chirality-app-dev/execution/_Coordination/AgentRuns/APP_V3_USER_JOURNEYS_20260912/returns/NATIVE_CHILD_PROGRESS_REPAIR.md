# Native child and compact progress repair

Bounded Type 2 return; source work after parent stopped frozen candidate journeys. No delegation, live UI/API/account operations, build, full suite, Stop edit, attachment edit, or Git mutation.

## Changes

- `frontend/src/lib/shell/harness-event-views.ts`: raw stock v2 subAgentActivity and retained subagent.progress (top-level fields or nested Codex params.item) now merge by Runtime session plus actual agentThreadId. Native retained records bypass legacy taskId reduction. Activity item IDs deduplicate started/completed lifecycle pairs and raw/retained duplicates; outer phase never determines child completion. Kind started/completed/interrupted supplies status; interacted retains existing status or remains unknown. Native thread metadata and child messages merge into that identity. Actual native thread ID, parent thread ID, path and role are retained separately; missing output/role is not invented. Existing explicit observation-ended evidence remains nonterminal.
- `frontend/src/components/woven-dialogue/coordination-panel.tsx`: existing native evidence section beside recorded Runtime hierarchy now benefits from stock projection, uses recorded path when name is absent, and exposes only supplied role/path/parent/thread metadata. Native rows are disclosure elements, not fabricated selectable Runtime sessions.
- `frontend/src/components/shell/subagent-stream-view.tsx`: recorded path is the fallback label for unnamed stock children.
- `frontend/src/lib/shell/turn-activity.ts`: compact summary uses the fixed observed activity title plus action/failure counts; it no longer appends raw detail. Expanded Activity data retains command details. No purpose inferred from shell contents.

Runtime author confirmed the coordinated contract: new stock activity flows as raw codex.notification only; already-persisted projected activity remains supported by this App repair. No App contract export changes required.

## Evidence

`npx vitest run src/__tests__/lib/native-progress.test.ts src/__tests__/lib/turn-activity.test.ts src/__tests__/components/native-coordination.test.tsx src/__tests__/lib/harness-event-views.test.ts src/__tests__/lib/harness-event-views-codex.test.ts`: **5 files / 35 tests PASS**.

Focused regressions cover exact stock start pair + empty-target wait + completed pair for one child, raw/retained deduplication, retained-only top-level/nested compatibility, distinct child identities, interacted unknown, interrupted, explicit observation end without terminal evidence, actual name/role/parent/message merging, Agents path display without invented role/session, and compact shell omission with retained activity detail.

`npm run typecheck`: **PASS** (frontend and Electron no-emit checks). Final metadata display was followed by `npx vitest run src/__tests__/components/native-coordination.test.tsx`: **2 tests PASS**.

Handoff: source slice complete and released for independent review and parent qualification. This return is derivative implementation evidence, not governed deliverable acceptance. Live qualification and final tranche fan-in remain parent-owned.
