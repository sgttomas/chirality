# Chat attention implementation return

Status: bounded authoring and focused checks complete; parent integration/review and live qualification pending.
Executor: TASK / Type 2, gpt-6-astra medium, delegated-harness-native child of campaign parent. No delegation, Git mutations, builds, supplier/account/UI operations or protected live-state reads. Active checkout resolved by git rev-parse to the packaged-refinement checkout, HEAD 6ac4055690e20ddffd6aa5fff58a8e7ddd3c072f.

## Changed files

- frontend/src/components/woven-dialogue/navigator.tsx: independent Needs answer controls remain enabled while chat navigation stays disabled during primary work.
- frontend/src/components/woven-dialogue/woven-dialogue-shell.tsx: shared primary live-request subscription, background running-session discovery, badge/dialog integration and collapsed-navigation attention indicator. No transcript switching or Stop operation.
- frontend/src/components/woven-dialogue/chat-attention.tsx: one shared live-request observer per background running session, dialog reusing RequestCards with known live rows; Escape, focus return and Tab containment.
- frontend/src/__tests__/components/woven-dialogue-shell.test.tsx: timer-capable existing fixtures plus integrated second-folder answer, stale submission, failed root/request lookup isolation and cleanup coverage.

Uses native App author's shared ref-counted useLiveSessionRequests and RequestCards; those files were not edited by this child. Dialog uses only known live rows, so no historical pending record becomes actionable and no additional request polling starts when opening it. Existing request submission revalidates its own session/request ID before answering.

## Checks

APP-HOLD-1 reliance, entry APP_V3_USER_JOURNEYS_20260912:CHAT_ATTENTION_IMPLEMENTATION, target DEL-02-01: ALLOW / CLEAR; no active holds. Register SHA d289b248a900122b012ae540b9b197feae3adbe264bf181f3d46556c500f320c; scan fingerprint 350872de553b81ba726bca5d8bcff1e105e8b5bd7407bdec15bb8e9f08cdeffe.

From frontend:
- npx vitest run src/__tests__/components/woven-dialogue-shell.test.tsx src/__tests__/components/request-card.test.tsx — PASS, 2 files / 35 tests (latest run 18:57 local).
- npx tsc --noEmit --incremental false — PASS.
- git diff --check — PASS at source inspection before final evidence write.

The integrated test keeps the primary controller mounted/running and navigation disabled while answering the second-folder request through session `second`. A vanished pending request is rejected before posting; the answer draft survives. Missing-folder and primary request-lookup failures do not erase the second chat. Resolved cards and badge clear, unmount stops polling. These are synthetic component proofs, not live App qualification or visual QA.

## Integration limits and handoff

Current-root session metadata refreshes quietly every 5 seconds. Other remembered roots rotate one root per 5 seconds, newest remembered roots first; only sessions reported running receive request subscriptions. Newly discovered running chats appear even if absent from the local historical index. At the 50-known-root bound, an older root can take roughly 245 seconds plus request latency to be revisited; request refresh adds up to 2 seconds under responsive APIs. Failed or slow APIs can extend this; this is polling, not push attention. It does not poll every historical chat.

Parent reported a real cross-folder Unknown session failure during parallel baseline. This child has not established that listHarnessSessions(root) is backend side-effect-free. Cross-folder attention relies on that route, so live reliance remains BLOCKED pending parent's separate shared-port diagnosis/repair and qualification. No new all-live API was introduced. Parent authorized bounded rotating discovery after that concrete option was reported; parent subsequently reserved production reliance pending diagnosis.

No authoritative snapshot acceptance, decomposition changes, lifecycle closure or release claim. This return is a derivative implementation/evidence package against the campaign source basis. Parent owns fresh full-diff review, real render/focus QA, backend routing reconciliation and applicable consolidated gates. Rerun affected attention tests after integration changes and qualify simultaneous distinct-folder sessions after route repair.

## Supplied basis hashes

- `AGENTS.md`: `59d8454064101253c829799ad8a6fc068cec97c6cce017fa133cb5bedc7203ed`
- `agents/AGENT_TASK.md`: `1a13a5b00b3ce01ff8519efe6b46bcbe0cd6a5b7985e24282fa7efa2c57c8fb7`
- `projects/chirality-app-dev/AGENTS.md`: `00663c45ca2deb9a21df273d3e8412f609c435f0a8f7746822a51c7f45006f9a`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/PLAN.md`: `62bd95560c979477244a5132e37343d2f31718419853aeeb7bce6c61062ac619`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/NATIVE_INTERACTIONS_PROPOSAL.md`: `818b8c380d7c25c706e8e259161e8ef760bf5b4d1965473aa889fd8f31553914`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/briefs/CHAT_ATTENTION_IMPLEMENTATION.md`: `889ce188972c6011f938b6dc4be863a18676cd6f0d161c58092859459bc68c0b`

## Reconnect fixture repair, candidate 4031c6c54f76760baaaf3d92e2db83819ce3a8ac

Parent dispatched focused remediation after the full frontend run exposed three reconnect test failures. Inspected the requested first 88 log lines through an at-sign-line filter. Root cause: reconnect tests installed an incomplete fake window without setInterval/clearInterval. Their afterEach removed window before React's error-triggered detached cleanup, producing secondary window-undefined errors. This evidence did not establish a production browser lifecycle failure.

Changed only frontend/src/__tests__/components/woven-dialogue-runtime-reconnect.test.tsx for this follow-up: supply controlled browser timers, track created renderers and flush unmount cleanup before removing globals even on a failed assertion. Preserve original reconnect/replay expectations; add verification that reconnect retains exactly one discovery poll and unmount prevents subsequent calls. No production behavior was removed or disabled.

APP-HOLD-1 reliance entry APP_V3_USER_JOURNEYS_20260912:CHAT_ATTENTION_RECONNECT, DEL-02-01: ALLOW / CLEAR, register SHA unchanged; scan fingerprint 0954ed105705301ccab40f3b6bcaed1fce542bc4f961055d40cc121b91b5dc29.

Focused command: npx vitest run src/__tests__/components/woven-dialogue-runtime-reconnect.test.tsx src/__tests__/components/woven-dialogue-shell.test.tsx — PASS, 2 files / 34 tests, 19:22 local. No builds, live UI, Git mutations or broader suite reruns. Parent owns the separately assigned approval-filter repairs and remaining full-suite integration.
