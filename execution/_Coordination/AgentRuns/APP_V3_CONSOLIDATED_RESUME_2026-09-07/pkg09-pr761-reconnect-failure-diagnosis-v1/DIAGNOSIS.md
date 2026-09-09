# PR761 full-suite reconnect failure diagnosis

Status: **TEST_FIXTURE_DEFECT — ONE TEST PATH REPAIR RECOMMENDED**

## Observed failure

At source commit `f8c9b22cfbc9192c14ee2b6b142371d5bb69f7a5`, GitHub Actions run `34322182961` reported one failure after 181 files / 1,959 tests passed (one failed, four skipped):

- `projects/chirality-app-dev/frontend/src/__tests__/components/woven-dialogue-runtime-reconnect.test.tsx:254`
- case: `reloads a replay lens that was left unavailable`
- expected `state.replayLoad` once immediately after the session click; observed twice.

Section 9 passed separately. No product, setup, package, native, or fixture process was run for this diagnosis.

## Cause

This is a deterministic fixture collision in the current test composition:

1. The test globally mocks `createSelectedSessionReplayLoader` so every loader instance uses the single `state.replayLoad` spy (`woven-dialogue-runtime-reconnect.test.tsx:45-57`).
2. The current shell creates a distinct chat-title reader and, after the recorded session list resolves, asks it to load first operator messages (`woven-dialogue-shell.tsx:129-132, 243-265`).
3. The real chat-title reader creates its own selected-session replay loader and calls `loader.load(...)` for each visible session (`chat-organization.ts:231-264, 276-283`). Because of the global module mock, this background title loader records against the same `state.replayLoad` spy used by the shell's operator-selected replay loader.
4. The session button then correctly invokes the shell's `loadReplay` once (`woven-dialogue-shell.tsx:347-381`). The spy count is therefore two although only one call belongs to the replay lens under test.

The title reader and selected replay loader are separate objects in production. The source has no second operator-click dispatch or render-time `loadReplay` call. The CI result is expected for this exact fixture because `renderShell()` drains mount/session effects before the click. Historical focused evidence showing 59/59 predates the chat-title reader integration and does not disprove the current collision.

## Minimum lawful correction

Change only:

- `projects/chirality-app-dev/frontend/src/__tests__/components/woven-dialogue-runtime-reconnect.test.tsx`

Partially mock `../../lib/woven-dialogue/chat-organization` so `deriveChatTitle` and `visibleActiveChatSessions` remain real, while `createChatReplayReader` returns an independent no-op test reader (`loadFirstOperatorMessages` resolves `{}`, `search` resolves `[]`, and `cancel`/`dispose` are independent spies or no-ops). Keep the existing selected-session replay loader mock and all existing reconnect assertions unchanged.

This isolates the replay-lens contract that the test claims to measure. Do not change the shell, suppress the chat-title effect, relax the call-count assertions, or merge background-title and selected-replay semantics.

Required validation after an authorized edit:

1. focused `woven-dialogue-runtime-reconnect.test.tsx`, including a repeated run to confirm stable isolation;
2. related `woven-dialogue-shell.test.tsx` and `chat-organization.test.ts`;
3. registered frontend typecheck;
4. full App suite / PR CI and Harness wrapper.

## Current identities

- test: `b21c16a91694a4524d97ffc5a75737a415385372cc8a10de8b1ff955c8d4e879` (11,860 bytes)
- shell: `425b3b29417a56fc8fa2c8042913c8a239d1b45fc9cdfe332babf996dd345fa7` (33,468 bytes)
- chat organization: `cf9fb81b2b321be74d5543bf90b81d62940ea87a6ff67f8b8e8268c9d76ec661` (13,348 bytes)
- CI run: `https://github.com/sgttomas/chirality/actions/runs/34322182961`

No correction has been applied and no CI rerun has been requested.
