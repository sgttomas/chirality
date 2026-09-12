# TASK: repair observed live recovery gaps

Parent HELP_HUMAN is the direct tester. Type 2 gpt-6-astra medium, no delegation.
This extends the diagnosis assignment under the owner's explicit instruction to
fix defects exposed by the three live checks. Author and final reviewer remain
separate instances.

Write only the source and regression tests necessary in Runtime client/HTTP
stream handling and the App harness client/proxy/port and chat-panel/turn-phase
projection. No Root instructions, policy modes, account/security boundary,
packaging, unrelated UI, workflows, user state, or native process operations.
Use the fresh checkout containing eb60db019, source basis 85f19f019. The parent
owns run logs, handoff, commits, full-suite integration, native trials and build.

Implement the smallest sound fix from the returned diagnosis:
1. Detect stalled Runtime observation by received transport bytes, including its
   periodic heartbeat comments. Use a separate bounded transport inactivity and
   connection-opening deadline (25 seconds is the proposed bound). Preserve long
   silent but healthy tool turns. Timeout/cancel only closes observation; it
   never interrupts the owned turn, cancels it via a proxy, or repeats turn POST.
2. Report actual attachment/healthy transport to the UI so recovery returns
   Reconnecting to Working/Waiting even with heartbeat-only traffic. Do not claim
   recovery just before an attachment attempt, or end re-observation prematurely
   when the first attach fails. Preserve event sequence de-duplication.
3. Preserve shutdown/restart interruption reasons through live and replay
   projections. Explicit user Stop remains Stopped. Service shutdown displays
   Failed with an accurate service-ended explanation; an unobserved ending
   reconciled on restart is Outcome unknown. Generic interrupted exit frames
   must not erase an already known specific cause. Keep the sent message in the
   conversation, never auto-resend or restore it as an implicit retry.

Direct observations on unchanged source: 25-second SIGSTOP at 20:41:14Z,
SIGCONT at 20:41:39Z, UI stayed Working at samples then Completed once (77.1 s).
SIGTERM at 20:44:17Z during the next tool turn yielded Stopped, one action,
71.3 s, no duplicate send. The reviewer has confirmed service-shutdown is already
in the Runtime facts. Parent will send reload observations shortly.

Add meaningful focused regressions for heartbeat-only healthy streams versus
stalls, subscription-only cancellation, recovered healthy state before terminal
output, shutdown/restart/user-Stop classification live and replay, and reload
attach with one original POST. Install dependencies in the fresh checkout if
needed and rebuild Runtime dist for frontend tests. Run focused affected tests;
parent will run full Runtime/frontend and typecheck once after fan-in. Avoid
live/supplier/credential-dependent tests. Never read protected live files/logs,
use security, launch an App or signal processes. Do not commit. Return changed
files, source reasoning, focused results and limits. If more write scope or a
materially different design is needed, return the issue before changing it.

## Independent-review repair, 2026-09-12T21:21:14Z

Review of 9eb92d33b found one P1: an ambiguous fresh POST could attach to an old retained turn or select an old replay terminal before learning the new turn identity. Parent authorizes a generated submission turnId through the App to the existing Runtime SessionTurnRequest.turnId, plus an optional expected identity on the App/client/Runtime attach path checked atomically in TurnRegistry.subscribe. Legacy omitted-identity calls retain their existing behavior. Supplier protocol is unchanged. Extend only the related request/port/client/route/registry types and maintained tests. Replay must use the same expected identity. Test old retained completion, old replay, matching recovery, preserved known-rejection restoration and no automatic second POST. See returns/REVIEW_LIVE_RECOVERY_1.md.

## Plan-attempt identity continuation at 2026-09-12T21:39:56Z

The fresh independent reviewer confirmed a remaining P1 in cf3b1338b: the
submitted UUID reaches the persisted plan attempt only after observation ends,
and an idless running attempt can inherit another live turn on reload. Repair
only this continuation boundary: persist the preallocated identity on the
execution attempt before the POST can be dispatched; require exact identity
for recovered plan settlement; legacy idless or mismatched attempts must not
inherit another turn's terminal. Add meaningful reload/ambiguous-POST and
matching-plan regressions, preserving ordinary plan execution, explicit Stop,
unknown outcomes and send-once behavior. Scope is ChatPanel and its existing
plan execution store/tests if needed. No new feature, supplier or packaging
change. Return the frozen diff and check results without committing. Parent
records and validates; the separate reviewer reassesses the final candidate.
