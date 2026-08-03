# N1 current-state inventory — accepted-turn recovery

- RunID: `DEL-02-06-RUNTIME-SPEC-001`
- Node: `N1`
- Runtime identity: `/root/w1_del0206/n1_w6`
- Date: `2026-08-03`
- Status: current-state inventory only; no semantic choice or implementation authority
- Accepted dependency: `basis/N0_R2_RETURN.md` SHA-256 `ca8c1b18f6bd3d32ab7f1bad5d0cdc15d3bd31c811d3a2484ed38f61c64ac522`
- Governing brief: `briefs/N1.md` SHA-256 `719b0094793bf657ac4755b9d94db3df56f042723210520fd30c9a55ad698116`
- Read-scope amendment: `READ_SCOPE_AMENDMENT_1.md` SHA-256 `01320cbe83e72fbcf7861bb30651654904764d27f3200b56ff4e118764331206`

## Interpretation boundary

Sections headed **Current fact** report only behavior visible in the declared
sources. Sections headed **Gap** identify missing or conflicting current
behavior. The final **Candidate affected paths** section is proposal-only: it
does not select a design, classify a client as affected, or authorize a write.

## Source coverage

All four paths in accepted Scope-of-Work read item 4 and all eleven paths in
`READ_SCOPE_AMENDMENT_1.md` were read in full using non-shell Node file reads.

| Source | SHA-256 | Coverage |
|---|---|---|
| `runtime/packages/contracts/src/protocol.ts` | `1d8d329fb2f296de30aa13c04f5d528efa717a762b49936000a9b162f50bfa9e` | Full |
| `runtime/packages/contracts/src/errors.ts` | `75d30b4139c8ba11264cb1165c4e51401cbc9c930770e8cb966513509b6b1501` | Full |
| `runtime/packages/client/src/client.ts` | `38a55c95ba2ffa488e46a1debb48939a4aa8af2da89b80777e9d28f6f0c4adf4` | Full |
| `runtime/packages/cli/src/cli.ts` | `77e2601afd3ee286444925fa08b1f890760f69e71b56c3feee690d034a4a53f5` | Full |
| `runtime/packages/contracts/src/events.ts` | `d20fd7dcc8f1d41ad713e9b840410acd6200666765f0217a275dc0ce945596cd` | Full |
| `runtime/packages/contracts/src/harness/event-schema.ts` | `8c6d17f0547f9433d9a2b0892ba50c266b08918142e39984ecc0a7d479661a2f` | Full |
| `runtime/packages/core/src/turn-coordinator.ts` | `992d501b49629b88cb72e42ad2c54d7934859da7e3a822259c68151e3ab3715b` | Full |
| `runtime/packages/core/src/agent1-run-coordinator.ts` | `d0e8483df38d837a52c371b1a150a766046de44d17f0da66e5fd34c1415d27e7` | Full |
| `runtime/packages/core/src/session-store.ts` | `fe81bc9a51ad7ebbeb2c1486fc802dffafde434d4d56d677c17347893150ffad` | Full |
| `runtime/packages/core/src/runtime-service.ts` | `43b2dd4dbf8b1a91a057350558229616e34bfec258b2b9ad8f5e36c058c7c74d` | Full |
| `runtime/packages/core/src/residency-coordinator.ts` | `9b37829aaa97cdf0f4e3ed6fde9135a57bf0b33a345b3b5cc8f7e6d4175dc327` | Full |
| `runtime/packages/daemon/src/runtime-daemon.ts` | `a6bb6b2388bbca084640611d15f4186b3c98379776001e2335b96831cebe2d46` | Full |
| `runtime/tests/daemon.test.ts` | `bbcfcabb48dd7c4b5c5e0645b14601efd89404e34a5cdde322a0bef5b22a693e` | Full |
| `runtime/tests/turn-hardening.test.ts` | `e5880870ef7ee94b90ebef4baf72335bf24073ca35b1d829ead05c3be9ee7b2b` | Full |
| `runtime/tests/session-and-residency.test.ts` | `5d9c1cda16267557ea8ca599109568718fcb7a22b3dcb8f58a67f760fa596b02` | Full |

## Current fact — event producer, store, and reader matrix

| Surface | Producer | Persistent store | Current reader / consumer | Current guarantee | Exact gap |
|---|---|---|---|---|---|
| Ordinary `turn.accepted` | `TurnCoordinator.run()` appends after project/session lookup, the in-memory session lock, engine resolution, and local residency admission, but before engine preflight and session `running` update (`turn-coordinator.ts:81-159`) | `SessionStore.appendEvent()` appends one JSON line to the session `events.jsonl` (`session-store.ts:127-140, 392-407`) | SSE caller receives the appended event; replay reads it on an explicit replay request (`runtime-daemon.ts:296-304`; `session-store.ts:152-209`) | Acceptance is durable before preflight or consequential engine streaming begins. | No declared startup or later-turn admission reader interprets an accepted event lacking a terminal event. A crash after append can therefore leave durable acceptance without a durable terminal classification. |
| Governed Agent 1 `turn.accepted` | `GovernedAgent1RunCoordinator.run()` persists its run record, then appends acceptance before manager execution (`agent1-run-coordinator.ts:123-207`) | Same session `events.jsonl`, plus a separate agent-run record whose status begins `running` (`agent1-run-coordinator.ts:187-205`) | Live SSE and explicit session replay | The manager run has a durable acceptance marker and run record before manager execution. | The coordinator's `active` map is memory-only and there is no declared startup scan joining accepted manager turns, run records, and terminal evidence. |
| Adapter terminal event | `TurnCoordinator` recognizes exactly `turn.completed`, `turn.failed`, `turn.cancelled`, and `turn.interrupted`, holds at most one, then persists it (`turn-coordinator.ts:26-31, 181-216, 304-318`) | Session `events.jsonl`; `session.json` is separately updated to `completed`, `failed`, or `interrupted` (`turn-coordinator.ts:327-334`) | Live SSE, explicit replay, transcript derivation | Multiple adapter terminal events are rejected; completion requires required-tool receipts; terminal persistence precedes final session-status update. | `turn.cancelled` is retained in the event log but is collapsed to session status `failed`; the session record cannot preserve all four terminal distinctions. |
| Synthetic ordinary terminal event | `TurnCoordinator` appends `turn.completed` or `turn.interrupted` after a conformant stream with no adapter terminal, and appends `turn.failed` or `turn.interrupted` in its catch path (`turn-coordinator.ts:304-345`) | Session `events.jsonl`, then `session.json` status | Live SSE and explicit replay | In-process error and interruption paths attempt one truthful terminal event; the active lock and residency receipt are released in `finally` (`turn-coordinator.ts:335-384`). | The guarantee depends on the coordinator process reaching its catch/finally path; it does not cover process termination after acceptance. |
| Governed Agent 1 terminal event | `GovernedAgent1RunCoordinator` appends completed, interrupted, or failed after persisting the final run record (`agent1-run-coordinator.ts:580-625`) | Session `events.jsonl`, `session.json`, and agent-run record | Live SSE and explicit replay | Coordinator, rather than manager engine, owns the manager terminal event. | The Agent 1 path does not emit `turn.cancelled`, and no restart reconciliation is visible for a run record left `running`. |
| Engine nonterminal harness event | Engine adapter produces it; `TurnCoordinator` validates session/turn identity before `persistEvent()` (`turn-coordinator.ts:181-216`) | Session `events.jsonl`; `persistEvent()` suppresses duplicate `eventId` values already present (`session-store.ts:142-150`) | Live SSE and replay | Cross-session/turn events and duplicate event IDs are rejected or suppressed. | `appendEvent()` has no turn-ID or semantic idempotency check; retrying a request with the same or a new `turnId` is not reconciled against prior accepted/terminal pairs. |
| Replay | No new event producer; daemon reads `SessionStore.replayDetailed()` and derives a transcript (`runtime-daemon.ts:296-304`) | Read-only access to `events.jsonl` and `session.json` | Runtime client exposes `replaySession`; CLI exposes explicit `session replay` (`client.ts:359-367`; `cli.ts:397-408`) | Valid events are returned with malformed-line count and event-type summary (`session-store.ts:156-209`). | Replay reports history but does not classify or repair accepted-without-terminal turns, update session state, or guard a new turn. |

## Current fact — startup, admission, model, drain, and client gates

| Gate | Current behavior | Evidence | Exact gap |
|---|---|---|---|
| Daemon startup | Creates private runtime/socket directories, recovers the socket, writes owner identity, ensures operator credentials, starts the Unix-socket server, and chmods the socket. | `runtime-daemon.ts:49-87` | No session enumeration, event replay, accepted-turn scan, terminal-set comparison, session-state reconciliation, or drain-account reconstruction occurs before listening. |
| HTTP turn admission | Requires `sessions:write` authorization, parses the request, then enters the runtime turn stream. | `runtime-daemon.ts:306-313` | The route does not perform a persisted-history admission guard or expose an indeterminate-prior-turn result. |
| Ordinary session admission | Requires authorized project and existing session; rejects a concurrent turn using an in-memory map; resolves the stored engine; for local execution, admits exact model residency; then appends acceptance. | `turn-coordinator.ts:81-157` | The lock is not durable. After restart it is empty even if the log contains acceptance without terminal evidence. |
| Governed Agent 1 admission | Requires authorized project, nonempty brief/approval reference, an Agent 1 persona, enabled adapter, creates a manager session, and records it in an in-memory `active` map before appending acceptance. | `agent1-run-coordinator.ts:123-205` | The memory-only reservation and any child-session pointer are lost on restart; no declared recovery reader restores or closes them. |
| Model initialization and drift | Lazily reads `model-residency.json`, checks the recorded managed model is loaded, otherwise clears ownership; `status()` and `admitTurn()` reconcile current oMLX status. | `residency-coordinator.ts:50-95, 246-300` | This reconciliation concerns model residency only. It does not inspect session event logs or reconstruct accepted-turn state. |
| Model transition drain | Local admission increments memory-only `activeTurns`; an idempotent release closure decrements it; activation blocks new local turns and waits for that count to reach zero. | `residency-coordinator.ts:66-95, 98-210, 302-319` | `activeTurns` is initialized to zero and is not persisted or reconstructed. A restarted daemon can therefore report/drain zero despite unresolved accepted local turns in durable session history. |
| Client transport | Client sends the request once, parses SSE, and exposes separate replay and interrupt calls. Cancelling destroys the response. | `client.ts:138-208, 359-390` | A transport loss after server-side acceptance but before client observation is not distinguished from pre-acceptance transport loss. No automatic replay exists (fail-closed), but no exact indeterminate accepted-turn classification is returned either. |
| CLI presentation | `session turn` streams once and requires terminal `process:exit`; `session replay` is a separate explicit command. Runtime transport failures print `RUNTIME_UNAVAILABLE`. | `cli.ts:134-174, 369-445` | The CLI cannot tell an operator whether a failed transport attempt was durably accepted; it offers no accepted-turn recovery/reconciliation command or typed residue result. This is a Root CLI surface observation, not a client ownership ruling. |

## Current fact — preserved guarantees and test evidence

1. The ordinary coordinator reserves its in-memory session lock before the
   asynchronous local-residency admission; a second same-process turn is
   rejected with `SESSION_TURN_IN_PROGRESS`
   (`runtime/tests/turn-hardening.test.ts:88-123`).
2. A nonzero engine exit without terminal evidence is not promoted to success;
   `turn.failed` and session status `failed` are recorded
   (`runtime/tests/turn-hardening.test.ts:179-219`).
3. Events emitted after `process:exit` are rejected and not persisted, and a
   missing `process:exit` fails closed
   (`runtime/tests/turn-hardening.test.ts:221-311`).
4. An orderly SSE disconnect while the daemon remains alive invokes
   interruption and produces exactly one `turn.interrupted`, with no competing
   terminal event (`runtime/tests/daemon.test.ts:266-355`).
5. Model drift is reconciled before status/admission; local activation waits
   for the same-process active-turn count and fails closed on drain timeout or
   ambiguous unload/load outcome
   (`runtime/tests/session-and-residency.test.ts:72-138`).
6. No declared test simulates daemon/process restart after `turn.accepted` and
   before terminal persistence, proves startup reconciliation, proves durable
   drain-account reconstruction, or proves idempotent repeated reconciliation.

## Contradiction and ambiguity list

| ID | Current fact | Consequence for later planning |
|---|---|---|
| `N1-C01` | `RuntimeEventType` omits `turn.cancelled` (`events.ts:1-14`), while `HarnessEventType` and terminal handling include it (`event-schema.ts:1-18`; `turn-coordinator.ts:26-31`). The two event vocabularies are not isomorphic. | N4 must preserve all four terminal types and determine whether the older/general event type is in scope; N1 selects no resolution. |
| `N1-C02` | `TurnCoordinator` preserves `turn.cancelled` in the event log but maps every non-completed, non-interrupted terminal to session status `failed` (`turn-coordinator.ts:327-334`); `SessionStore` normalizes only idle/running/completed/failed/interrupted statuses (`session-store.ts:323-330`). | Event truth and session-summary truth have different cardinality. Any reconciliation design must name which is authoritative without silently erasing cancellation. |
| `N1-C03` | Accepted event persistence occurs before preflight and before the session becomes `running` (`turn-coordinator.ts:150-159`). | A durable `turn.accepted` can coexist with an old/idle session status; status alone cannot prove whether accepted work is unresolved. |
| `N1-C04` | Daemon startup reconciles stale socket ownership but not persisted session work (`runtime-daemon.ts:49-87`), while residency initialization separately reconciles model load state (`residency-coordinator.ts:246-300`). | “Reconciliation” currently exists for socket/model state, not accepted turns; no existing accepted-turn reconciliation may be inferred from those names. |
| `N1-C05` | Orderly disconnect coverage proves same-process interruption, whereas crash/restart skips the in-memory catch/finally and active-turn release mechanisms. | Existing disconnect evidence cannot serve as restart/replay evidence for idempotent accepted-turn reconciliation. |
| `N1-C06` | `persistEvent()` deduplicates exact event IDs, but newly appended events receive random IDs and no producer checks an existing accepted/terminal set by `turnId` (`session-store.ts:127-150`). | Event-ID deduplication is not turn-level reconciliation or retry idempotency. |

## Gap register

| Finding | One-sentence gap | Evidence |
|---|---|---|
| `N1-F01` | No daemon-start scan discovers durable `turn.accepted` events that lack all four terminal types before the daemon begins accepting requests. | `runtime-daemon.ts:49-87`; `session-store.ts:152-209` |
| `N1-F02` | No turn-admission scan blocks or classifies a session whose durable history contains accepted-without-terminal residue. | `runtime-daemon.ts:306-313`; `turn-coordinator.ts:81-113` |
| `N1-F03` | No current producer emits a reconciliation terminal/evidence record for crash residue, and no idempotent turn-level compare-and-append operation is present. | `turn-coordinator.ts:304-345`; `session-store.ts:127-150` |
| `N1-F04` | Local model drain accounting is memory-only and resets to zero after process restart. | `residency-coordinator.ts:24-31, 66-95, 302-319` |
| `N1-F05` | Client and CLI transport failures do not distinguish “request not accepted” from “accepted but terminal unknown.” | `client.ts:138-208`; `cli.ts:134-174, 439-445` |
| `N1-F06` | Replay is descriptive only and does not reconcile event truth with session/run status. | `runtime-daemon.ts:296-304`; `session-store.ts:156-209` |
| `N1-F07` | The runtime event vocabularies disagree on `turn.cancelled`, and session status collapses cancellation into failure. | `events.ts:1-14`; `event-schema.ts:1-18`; `turn-coordinator.ts:327-334` |
| `N1-F08` | Existing tests cover same-process failure, disconnect, lock, and model drain but not crash/restart reconciliation or repeated reconciliation idempotency. | `daemon.test.ts:266-355`; `turn-hardening.test.ts:88-311`; `session-and-residency.test.ts:72-138` |

## Candidate affected paths — proposal only

The following are candidate review loci for N4 planning, not selected changes:

| Candidate path | Why it may be affected | Authority statement |
|---|---|---|
| `runtime/packages/contracts/src/events.ts` | Align or explicitly separate the four-terminal vocabulary. | Proposal only. |
| `runtime/packages/contracts/src/harness/event-schema.ts` | Preserve the accepted/terminal/reconciliation evidence vocabulary. | Proposal only. |
| `runtime/packages/contracts/src/protocol.ts` | A typed residue/status or recovery response may require a contract surface. | Proposal only; no contract adopted. |
| `runtime/packages/contracts/src/errors.ts` | A truthful indeterminate/reconciliation class may be required. | Proposal only; no error code selected. |
| `runtime/packages/core/src/session-store.ts` | Durable accepted/terminal indexing and idempotent compare-and-append would live near current canonical event persistence. | Proposal only; no store design selected. |
| `runtime/packages/core/src/turn-coordinator.ts` | Admission guard and terminal preservation touch ordinary-turn orchestration. | Proposal only. |
| `runtime/packages/core/src/agent1-run-coordinator.ts` | Governed manager turns have the same accepted-without-terminal exposure plus a run record. | Proposal only. |
| `runtime/packages/core/src/runtime-service.ts` | A bounded reconciliation service boundary may be needed between storage and daemon routes/startup. | Proposal only. |
| `runtime/packages/core/src/residency-coordinator.ts` | Drain semantics may need a deliberate relationship to unresolved durable local turns. | Proposal only; model behavior is not selected. |
| `runtime/packages/daemon/src/runtime-daemon.ts` | Startup ordering and/or explicit operator route placement are possible planning loci. | Proposal only; automatic behavior is not selected. |
| `runtime/packages/client/src/client.ts` | Root client may need a typed way to inspect residue without automatic resend. | Proposal only; source proximity creates no client obligation. |
| `runtime/packages/cli/src/cli.ts` | Root CLI may need truthful operator presentation while preserving no automatic replay. | Proposal only; no UX selected. |
| `runtime/tests/daemon.test.ts` | Restart-before-listen and repeated-reconciliation evidence may be required. | Proposal only. |
| `runtime/tests/turn-hardening.test.ts` | Four-terminal and admission-blocking invariants may need coverage. | Proposal only. |
| `runtime/tests/session-and-residency.test.ts` | Durable drain/restart relationships may need coverage. | Proposal only. |

No App, PEC, Piping, Tier-0, or other client is classified as affected by this
inventory. Actual obligation requires a later accepted Root contract and a
separately governed affected-client determination.

## N1 disposition

`ACCEPT_FOR_N4` is recommended. The inventory establishes the current event
producers, canonical event store, explicit replay reader, startup/admission and
model/drain gates, preserved guarantees, contradictions, exact recovery gaps,
and candidate planning loci without selecting a solution or changing runtime
state.
