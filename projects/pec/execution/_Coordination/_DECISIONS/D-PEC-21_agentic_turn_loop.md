# D-PEC-21 - PROPOSAL: agentic turn loop + conversation memory for the SDK engine

**Status:** RULED 2026-07-07.
**Date prepared:** 2026-07-07
**Decision ID:** D-PEC-21
**Prepared by:** PEC work loop agent. The ruling act is the owner's (K-AUTH-1;
D-GOV-04). Packet form per the D-PEC-17/D-PEC-20 precedent (tranche detail
folded into the packet). Companion rows: `D-PEC-17` (the sidecar this widens),
`D-PEC-20`/`D-T0-21` (the access basis this rides — unchanged here).

## Why this row exists

The owner's first `broad`/live-LLM launch (2026-07-07, his screen) demonstrated
the ruled D-PEC-17 v1 turn shape's ceiling under a live model: read acts fire
through every guard, but the model cannot answer from what it read. Owner
observation of record (2026-07-07, in-session, verbatim): "I can't call this a
pass, but it did demonstrate more read behaviour, I think.   Still not able to
do the task though."

Diagnosis (verified in the live tree):

1. **Single-directive turns by construction.** `engine/sdk.ts` gives the model
   one query (`maxTurns: 1`) and accepts exactly one JSON directive — a reply
   OR an act. An act's result returns to the panel only; the model never sees
   it, so read-then-answer is structurally impossible.
2. **Stateless turns by construction.** `AgentTurnInput` (`engine/port.ts`)
   carries no conversation history; follow-up questions arrive with no trace
   of prior turns.
3. **No self-correction.** A wrong first read (e.g. an empty register) ends
   the turn.

## Verified current state

| Fact | Source |
|---|---|
| One SDK query per turn; one directive parsed; act results are returned as events, never fed back. | `projects/pec/agent-sidecar/src/engine/sdk.ts:98-166` |
| `AgentTurnInput` = `{pid, message, context?, attachment?}` — no history field. | `projects/pec/agent-sidecar/src/engine/port.ts:29-42` |
| The server proxy route relays the client body verbatim (`{...b, pid}`), so a new optional body field needs **no server route change**. | `projects/pec/server/src/api.ts:381-387` |
| Proxy message timeout is a hard-coded 60 s constant. | `projects/pec/server/src/agent-proxy.ts:21` |
| The human-act boundary is structural: no accept/apply/reject-of-others/`force` act exists on `BoundActs`; every act dispatches through the same guards/clamp. | `projects/pec/agent-sidecar/src/engine/port.ts:60-78`; D-PEC-17/20 evidence |
| The panel holds the thread client-side (`Turn[]` state) but sends only the new message. | `projects/pec/web/src/agent/AgentPanel.tsx:68,109-134` |

## Decision to rule

Whether to authorize one source tranche making the SDK engine's turns agentic
and conversational, inside the existing bounded acts surface:

1. **Directive loop (sdk engine only):** after the model names an act, execute
   it through `BoundActs` exactly as today, append the result to a turn log,
   and re-query the model with that log until it emits `{"reply"}` — bounded
   at **8 acts per turn**. On budget exhaustion the model gets one final
   reply-only query; a further act directive becomes a `turn:error`
   (`TURN_ACT_CAP`). Act payloads fed back to the model are size-capped
   (truncated with a disclosure marker) so turns stay bounded. Every act in
   the chain still emits its `act:result`/`act:refused` event to the panel —
   the owner sees the whole chain.
2. **Conversation memory (transport, not storage):** optional
   `history: [{who: 'you'|'agent', text}]` on `AgentTurnInput`, validated in
   `http.ts` (≤ 40 entries, each ≤ 8 KiB text, on top of the existing 6 MiB
   body cap); the web panel flattens its existing thread state (replies,
   act summaries, refusals verbatim) and sends the last 20 turns with each
   message. The sidecar stores nothing between requests — statelessness of
   the *process* is unchanged; the transcript rides the request.
3. **System-prompt update** describing the loop protocol; the basis-refusal
   rule ("a refusal naming the access basis is final for this turn") stays.
4. **Proxy timeout:** `MESSAGE_TIMEOUT_MS` becomes env-configurable
   (`PEC_AGENT_MESSAGE_TIMEOUT_MS`, default 300 000 ms), read per-request like
   `agentTargetFromEnv`; invalid values → 500 `AGENT_MISCONFIGURED`.
5. **Stub engine unchanged** (deterministic single-directive routing is its
   design; it ignores `history` — disclosed, not a silent trim).
6. **Panel type cleanup (disclosed):** `AgentStatus` in `web/src/agent/api.ts`
   gains the `access?: string` field the Receipt-46 delta noted as
   hand-synced structurally; `AgentPanel.tsx` drops the structural cast.
7. **Tests:** loop-until-reply with injected fake query function (act result
   fed back verbatim, cap enforced, cap-then-reply, cap-then-act →
   `TURN_ACT_CAP`, malformed directive → raw-text reply unchanged); history
   validation pins (shape, entry cap, text cap); refused-act results feed
   back and can still end in a reply; boundary re-pin (an accept-shaped act
   name from the model → `UNKNOWN_ACT`, unchanged); proxy timeout env pin
   (default, override, invalid).

**Not in scope (unchanged, structural):** the act vocabulary (no new act, no
accept/apply/reject-of-others/`force`/conversion-disposition), the access
basis and clamp (D-T0-21/D-PEC-20 as ruled), the server route surface, new
runtime dependencies, sidecar persistence of any conversation state, the stub
engine's behavior, real/non-scratch mutation basis.

## Fence (exact; STOP outside it)

- `projects/pec/agent-sidecar/src/engine/{port.ts,sdk.ts}`
- `projects/pec/agent-sidecar/src/http.ts`
- `projects/pec/agent-sidecar/test/engine-sdk-loop.test.ts` (new) +
  `projects/pec/agent-sidecar/test/sidecar-e2e.test.ts` (history-validation
  pins only)
- `projects/pec/agent-sidecar/README.md` (if a doc line is needed)
- `projects/pec/web/src/agent/{api.ts,AgentPanel.tsx}`
- `projects/pec/server/src/agent-proxy.ts` (timeout mechanism only)
- `projects/pec/server/test/agent-proxy.test.ts` (timeout pins)
- No `core/**`, no other `server/**`, no root manifests, no profile, no DB,
  no `config.ts`, no `acts.ts`, no `pec-client.ts`, no `stub.ts`.

## Options

- **O-A (recommended):** the tranche as specified (items 1–7): loop +
  conversation memory + configurable timeout.
- **O-B:** items 1, 3, 4, 7 only — the loop without conversation memory
  (turns compose internally but each starts fresh).
- **O-C:** defer; keep v1 as a read-demonstrator.

## Verification plan (workplan step-4 bar)

pec `npm run typecheck && npm test && npm run build && npm run drill`; scope
containment `git diff --name-only ⊆ fence`; adversarial review of the loop
bound + boundary re-pins + history caps; self-check no baseline shift;
coord-check on the range; evidence: a live-LLM capture at the owner's screen
re-asking the three demonstrated-failing questions (deliverables-on-plan %,
follow-up-from-memory, worst-forecast-slip with self-correction), plus the
boundary refusal under the loop.

## Rollback

Single revert of the tranche commit(s). Without `history` the panel simply
sends none (field optional end-to-end); the proxy default timeout reverts
with the same commit.

## Human ruling

**RULED — 2026-07-07** (owner in-session, Ryan Tufts, verbatim):

> My ruling is `O-A` proceed accordingly.

Recorded interpretation (agent, per the presented slate): O-A affirmed — the
full tranche (items 1–7: bounded directive loop, conversation memory over the
request, env-configurable proxy timeout), implementation authorized in the
same ruling inside the fence above, branch-first, no self-merge; the live-LLM
evidence capture at the owner's screen closes the row's verification plan.
