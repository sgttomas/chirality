# D-APP-123 — Activity strip primary-session caller locus

**Status: PROPOSAL / AWAITING_RULING.** OwnerCaseSelection: NONE. EffectStatus: HELD.

DEL-02-04-V3-01 already owns the activity strip, but its explicit write locus omits the woven-shell caller. The caller holds the primary session identity and does not pass it to ActivityStrip. D120's separate T2 presentation grant does not authorize a T5 caller change.

## Options

**A — Recommended:** adopt the exact single-line V3-01 write-locus addition in the reviewed candidate. Add only `frontend/src/components/woven-dialogue/woven-dialogue-shell.tsx` and `frontend/src/__tests__/components/woven-dialogue-shell.test.tsx`, solely to pass the existing `primarySessionId` as an explicit optional presentation prop into the existing ActivityStrip. The strip-side prop acceptance/consumption remains within its already seated component/test locus and must be separately selected, implemented and reviewed together with the caller.

**B — Retain current locus:** make no amendment. Caller-dependent primary-session strip work stays held; independently lawful component-local work can continue with truthful unavailable/observed-only output. Never infer the primary session from the last event.

The same ChatPanel instance, event provider, root/session binding and streaming/selection/reconnect/Details handlers remain unchanged. No new state schema, provider write, runtime/session field, event semantics, steering, permission, IPC capability, CSS or Activity-row navigation callback is granted. This identity input does not prove a correct turn summary or full T5 completion.

## Exact reviewed bytes and affected surface

Candidate root: `execution/_Coordination/AgentRuns/APP_SHELL_RESUME_2026-09-06/account-scope/t5-strip-scope/`.

| Artifact | SHA-256 |
|---|---|
| `FROZEN_CANDIDATE.json` | `89cd6d3b8490ea52f105412003e2d2c567fa6812346eb60c0468d29d660e23e6` |
| `PREIMAGE__STATUS.md` | `16053333f23dd8905c5567eeae4151de03e56f77f58fa64d7c52d0dc30d249f0` |
| `CANDIDATE__STATUS.md` | `165f443bba9907bfbbcc6f1c4a4e2bb6ded61241edf5204510c41062ab4f0265` |
| `STATUS_DIFF.patch` | `2ae12b41935929c89435a161325a84dcdfadbb94d7da324ec4a484c264dce89c` |
| `PROPOSAL.md` | `2497f966fdaf573c0e49767662faea421f1766e30f1687119262cc0e1134a8e0` |

The exact target is `execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-04_Toolkit_Options_and_Local_UI_State/_STATUS.md` line 31. Original locus text is retained and the bounded addition appended. Every other byte, including gates, Depends, checks, return/removal criteria, lifecycle, Checking Approval SHA and history, is unchanged. No live status or dependency change is made at registration.

`REFUTATION_RETURN.md` records the fresh read-only Agent 2's **COMMIT-SAFE for proposal presentation/registration only**, with independently recomputed identities. Parent verified and accepted that bounded return for registration. Final review of this actual packet/register delta remains part of the run's pending union review; neither this packet nor the candidate establishes final source/whole-tranche acceptance. Concurrent ActivityView repairs have changed activity-shelf.tsx after the proposal refutation. Those source changes are outside this review, not accepted by it, and must be refreshed/frozen under their own source review and later implementation checks.

## Authority route and risks

SCA-APP-010's DEL-02-04 row and controlling ScopeOfWork already assign the one-line activity strip; no decomposition truth, ID, acceptance criterion, scope/dependency snapshot or pointer amendment is requested. This is a bounded D108-seated item-locus amendment following the D120 precedent. Expanding the explicit caller locus nevertheless requires an owner act under D60/D64. The recommendation and independent review do not supply that act.

Missing, invalid or truncated session/turn/timestamp observations remain unknown or explicitly observed-only; bounded event buffers are not complete audits. Timer/count semantics and row navigation remain subject to their independently accepted scope. Existing ShellFrame reconnect ownership, fixed 32px strip and stable centre dialogue must be preserved. The Walkthrough and surrounding redesign plan are design context reconciled with those live obligations; no new interactive mock viewing is claimed. D122 account scope and every unrelated gate remain unchanged.

## On-ruling mechanism

If A is selected, preserve the owner's words in a ruling record, verify the exact live status preimage and apply the approved postimage through PKG02 under a separately frozen reviewed application set. Actual history/memory/run-record updates follow only after the event. Any intervening status/history drift requires refreshed exact candidate bytes and review; do not blind-apply this historical preimage.

The owner amendment becomes effective only after observation on fetched `origin/main`. Re-derive APP-HOLD, live Remaining and dependency gates before selecting implementation. Freeze the existing caller plus strip-side implementation/tests together against the accepted ActivityView source, serializing shared-file edits. Require fresh full-diff source review PASS, registered frontend/typecheck/Vitest/build/premerge/render and repo harness/receipt checks, the A1 re-stage declaration and applicable browser/live-region/reduced-motion proof. Full T5 closure requires all its residual obligations; this amendment waives none. Publication and merge authority remain separate.

If B is selected, record the no-change disposition and retain current locus. Registration itself moves no authoritative pointer and triggers no SCA/DepClosure rerun. Accepted upstream remains SCA-APP-010_2026-09-04_2045_Shell_Redesign_Dialogue_Centred_IA, accepted DepClosure CLOSURE_SCC-DECOMPOSE-SCA-APP-010_2026-09-05_1034, D108 and D120. Packet/candidate are derivative proposal evidence, not accepted truth or an independent queue.

Prepared 2026-09-06 by SCOPE_CHANGE under HELP_HUMAN's registration-only release; delegated-harness-native, instruction-asserted, Codex/OpenAI GPT-6 family (exact runtime model identifier unavailable). No owner selection, source change, runtime execution, Root act, live status/dependency application or publication is claimed.
