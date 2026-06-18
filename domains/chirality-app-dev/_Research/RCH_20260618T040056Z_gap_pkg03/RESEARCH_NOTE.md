# Research Note - gap pkg03

Status: DERIVATIVE_RESEARCH_PACKET

## Question

Assess package PKG-03 (Runtime Engine Contract and Turn Lifecycle, roadmap role R1):
for each of DEL-03-01..DEL-03-04, extract acceptance criteria, judge
implementationReality against the LIVE tree, and state the gap from IN_PROGRESS to
ISSUED.

## Accepted Basis

- Live execution tree + git HEAD of projects/chirality-app-dev (ACCEPTED_BASIS).
- Deliverable docs under execution/PKG-03_.../1_Working/DEL-03-0x/.
- Retrieval snapshot SRCIDX_20260616T043733Z (STALE; discovery only).

## Short Answer

PKG-03 is substantially implemented and proven live. The product-owned engine
boundary (agent-engine-port.ts), the conformance suite (engine-conformance.ts +
8 fixtures), the thin TurnEngine with one-turn-per-session locking + cleanup
(turn-engine.ts), the thin /api/harness/turn and /api/harness/interrupt routes,
the versioned HarnessEvent schema + append-only redacted JSONL, and interrupt /
terminal-outcome handling all exist and are covered by green tests (6 PKG-03
suites, 54 tests passed). No deliverable has advanced past IN_PROGRESS: zero are
in CHECKING/ISSUED. The gap to ISSUED is consolidation + human gating, not
missing code: refresh per-deliverable Evidence files mapping live code/tests to
each REQ, resolve the REF-006 HASH_MISMATCH ruling and the DEL-03-04 interruption
taxonomy conflict, confirm the DEL-04-01 SDK-backed fixture and Section 9
(DEL-09-02) validation linkage, then run the human-gated CHECKING then ISSUED
transitions.

## Evidence

See Evidence_Map.csv (EV-01..EV-16). Load-bearing :RUN anchors: EV-03 (conformance
fixtures green, replay asserts turn.accepted first + redaction), EV-04 (6 suites /
54 tests pass), EV-06 (overlap=>409 + lock release + recovery), EV-08 (ordered SSE
event names + media type), EV-12 (append-only JSONL replay + no raw secrets).
Load-bearing :READ anchors confirm structure: EV-01 port, EV-05 TurnEngine,
EV-07 thin turn route, EV-09 interrupt route, EV-10 terminal handling, EV-11
HarnessEvent schema, EV-13 contract doc.

## Interpretation

- DEL-03-01 (port + conformance): SUBSTANTIAL. Port + suite + doc all live; suite
  proves accepted-turn-before-execution, terminal persistence, SDK mapping, tool
  exposure, interrupt, leakage rejection, redaction. Gaps: live SDK-query and
  Electron-packaged-subprocess conformance cases are BLOCKED_TBD; the suite does
  not itself enumerate the REQ-010 permission-denial and session-resume cases
  (covered by adjacent suites/modules). Spec literal names runTurn/TurnInput
  diverge from implemented startTurn/AgentEngineRunInput (AC-01).
- DEL-03-02 (TurnEngine + locking): SUBSTANTIAL->COMPLETE for the lifecycle/lock
  scope. One-turn lock, TURN_IN_PROGRESS 409, release on completion/failure/cancel,
  TurnInput binding, session metadata persistence all proven. Caveat: turn.accepted
  is persisted at the SDK adapter boundary, not in TurnEngine, and the stub path
  does not write it (AC-02 / REQ-008).
- DEL-03-03 (API + SSE compat): SUBSTANTIAL. Thin route delegation, stable SSE
  names, media type, UI/HarnessEvent separation proven. Formal route-to-fixture
  index / SSE compatibility fixture README artifacts (REQ-008/REQ-010) are doc
  deliverables not yet confirmed present.
- DEL-03-04 (interrupt/cancel/terminal): SUBSTANTIAL. Interrupt route, exitCode-130
  interrupted process:exit, durable terminal outcomes, versioned HarnessEvent,
  redaction, malformed-line-tolerant replay all live + tested. Open conflict
  CONFLICT-001 (interruption taxonomy) is de-facto resolved in code but unruled in
  the ledger (CF-01 / AC-03).

## Caveats

- Retrieval index is STALE (CONTENT_DRIFT, 49 changed); used for discovery only.
  All load-bearing claims re-verified against the live tree.
- Ran the 6 PKG-03-relevant vitest suites, not the full repo suite.
- REF-006 docs/PRD.md HASH_MISMATCH carried across all four deliverables as a
  closure blocker pending human confirmation.
- No code change recommended that crosses a HARD FENCE; non-Anthropic provider
  routing and remote MCP remain blocked and are out of scope here.

## Open Questions

See Open_Questions.csv. Chiefly: does adapter-level turn.accepted satisfy
DEL-03-02-REQ-008; is the implemented interrupt=>cancellation taxonomy the accepted
ruling; are the DEL-03-03 fixture-index/README doc artifacts present.

## Handoff / Next Action

Return structured object to the dispatching orchestrator. Route Amendment_Candidates
(AC-01..AC-04) to SCOPE_CHANGE / DOMAIN_DECOMP / CHANGE as marked; route CF-01 to
the DEL-03-04 owner for a human ruling. No accepted truth modified by this packet.
