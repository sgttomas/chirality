# Woven Dialogue Shared Contract Freeze

**RunID:** `APPDEV_WOVEN_DIALOGUE_IMPLEMENTATION_2026-07-23`
**Contract freeze:** `C0`
**Status:** `FROZEN_FOR_IMPLEMENTATION`
**Authority:** owner activation plus accepted SCA-APP-004 handoff

## Common contract

The integration owner owns
`frontend/src/lib/woven-dialogue/contracts.ts`. Package workers may import but
must not edit it. It fixes:

- admitted Work item authority and currency classes;
- provider-neutral recorded-session attribution;
- exact recorded/not-recorded parentage;
- hierarchy, diagnostic, and unresolved-parent structures;
- replay disclosure and isolated replay state; and
- the Work/Agents panel selector.

No projection may infer a plan, assignment, parent, role, model, approval,
acceptance, lifecycle transition, or currency from prose, visual placement,
timestamp order, persona, or model identity.

## Package fences

### PKG-02

Owns only:

- `frontend/src/lib/woven-dialogue/woven-workspace-state.ts`
- `frontend/src/components/woven-dialogue/work-projection.tsx`
- `frontend/src/__tests__/lib/woven-workspace-state.test.ts`
- `frontend/src/__tests__/components/woven-dialogue-work-projection.test.tsx`

The state schema is `chirality.woven-workspace/v1` at
`chirality.wovenWorkspace.v1`. Migration may copy only legacy file-tree
geometry into Navigator geometry, records the mapped fields, and never
overwrites or deletes any legacy key. Work renders only supplied admitted
items and an honest empty state.

### PKG-05

Owns only:

- `frontend/src/lib/woven-dialogue/operator-projection.ts`
- `frontend/src/lib/woven-dialogue/selected-session-replay.ts`
- `frontend/src/components/woven-dialogue/selected-session-replay-lens.tsx`
- `frontend/src/__tests__/lib/operator-projection.test.ts`
- `frontend/src/__tests__/lib/selected-session-replay.test.ts`
- `frontend/src/__tests__/components/selected-session-replay-lens.test.tsx`

Replay is GET-only, isolated from `HarnessEventsProvider`, bounded with visible
counts, and has no send, continue, interrupt, permission, resume, boot, delete,
or lifecycle callbacks.

### PKG-08

Owns only:

- `frontend/src/lib/woven-dialogue/recorded-agent-hierarchy.ts`
- `frontend/src/lib/woven-dialogue/guarded-session-selection.ts`
- `frontend/src/lib/pipeline/pipeline-dispatch-contract.ts`
- `frontend/src/__tests__/lib/recorded-agent-hierarchy.test.ts`
- `frontend/src/__tests__/lib/guarded-session-selection.test.ts`
- `frontend/src/__tests__/lib/pipeline-dispatch-contract.test.ts`
- `frontend/src/__tests__/lib/pkg08-compatibility-boundaries.test.ts`

Hierarchy uses exact `parentSessionId` only. Selection is presentation state
only. Dispatch is inert data with no execution/delegation method. The
`ORCHESTRATE` compatibility alias remains `PROJECT_SETUP`; the conflicting
folder-local `ORCHESTRATOR` wording is recorded as a pre-existing governance
observation and is not implemented.

## Integration-owner fence

Only the root integration owner edits existing route/shell files,
`globals.css`, common contracts, new shell composition, package metadata,
lockfiles, and AgentRuns records. The primary `ChatPanel` is mounted once
inside the new shell and remains mounted while Work/Agents, replay, artifacts,
and Activity Shelf presentation changes.

Compatibility routes and query parameters remain resolving. Existing APIs,
SSE names/order, provider/runtime ownership, permission handling, dispatch
semantics, and old UI code remain unchanged.
