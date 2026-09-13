# TASK: native Runtime interaction implementation

Type 2 gpt-6-astra medium, no delegation. Owner approved native questions and
attention, readable children, checklist and steering, alongside message-boundary
and progress repairs. Use returns/NATIVE_PROTOCOL_MAPPING.md and actual source.
Implement the smallest compatible production path; preserve stock 0.154, current
account/auth/lifecycle boundaries, additive role context and history/replay.

Own changes within projects/chirality-runtime/packages: contracts, core, daemon,
client and directly affected tests. No App frontend files, instruction libraries,
governance, Git mutations, packaged builds, live supplier/account/UI operations
or protected filesystem reads. Parent drives real native qualification. Other
authors own frontend and library. Read Root/Runtime AGENTS, TASK. Read-only Git
inspection is allowed. Do not use historical admission machinery.

Preserve assistant native item identity/phase and supplied reasoning summaries
through live events and history, avoiding double legacy text. Preserve checklist
updates distinctly from saved native plans. Represent children using actual
thread/turn identity and reported child states/results, never completed collab
CALL as assignment completion. Inspect late-child and descendant request
resolution routing; either capture correctly within existing session ownership
or report limits truthfully, never fabricate completed results.

Add native steering end to end Runtime contracts -> authorized route -> registry
ownership -> delegated runtime/supervisor -> stock turn/steer. Proposed shared
interface for frontend author: SessionSteerRequest { operationId, expectedTurnId,
text }, where expectedTurnId is Runtime's current turn, not a renderer-supplied
native ID. SessionSteerResponse { operationId, turnId, status: accepted|rejected|
unknown, message?, providerTurnId? }. Use existing route naming conventions with
sessionTurnSteer and /sessions/:id/turn/steer. Announce finalized exported names
and signatures to parent early so frontend can bind; no sibling messaging.

Record submitted/accepted/rejected/uncertain input in the owning event stream.
Repeated operation IDs must not dispatch twice; conflicting payload fails. A
supplier acknowledgment proves receipt only; uncertain delivery is never auto
retried or silently turned into a new turn. Correlate native clientUserMessageId
if available. Retain uncertainty across restart using existing session evidence,
without creating a new governance/approval layer. Stop and permission modes stay
separate. Validate expected Runtime AND provider turn identity before admission.

Use additive compatibility and a shared native projection basis where useful.
Controlled adapter tests must cover boundaries, phase/null/partial/repeated
items, checklist replacement, child lifecycle and routing, pending requests,
steer stale target, reject/unknown/reconciliation/dedup/restart. Run meaningful
focused Runtime checks and tsc; parent runs whole integration after fan-in.
Return actual files/checks, exported interface and remaining native qualification.
