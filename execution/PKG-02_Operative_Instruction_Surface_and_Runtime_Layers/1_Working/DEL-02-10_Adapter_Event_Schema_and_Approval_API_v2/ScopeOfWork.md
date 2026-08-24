---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-02-10
package_id: PKG-02
decomposition_basis: execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md@75c4e2ba401a6f5ad0c2f38846c39db6ab157405
project_scope_refs: [SOW-104]
package_objective_refs: [OBJ-001, OBJ-002, OBJ-004, OBJ-007]
status: ACCEPTED_BY_OWNER_R7 (record SHA-256 dc62fb222bf2badd521e0b388f9cfa711b980a90f73db9c77de8726d7ec7cd53)
---

# Scope of Work — DEL-02-10

## Purpose and Objective Traceability

This draft Scope of Work defines the candidate production contract for
`DEL-02-10` — Adapter Event Schema and Approval API v2 — an `API_CONTRACT`
deliverable in
`PKG-02_Operative_Instruction_Surface_and_Runtime_Layers`. It covers project
scope item `SOW-104` and supports package objectives `OBJ-001`, `OBJ-002`,
`OBJ-004`, and `OBJ-007`, exactly as recorded in the applied deliverable
register.

The accepted boundary is: **Root API v2, closed event union with only the four terminal identifiers, attributed approvals**.
Within its recorded Context Envelope `M`, this is one versioned adapter/API
slice with deterministic wire fixtures. It carries the allocated G0 A3
role-posture rules and G0 A7 command-network consent rules.

This document is a draft awaiting owner acceptance. It does not claim that the
SOW or any output is accepted, complete, implemented, dispatched, activated,
or relied upon. The deliverable's lifecycle state remains `OPEN` as recorded
in `_STATUS.md`; this SOW does not change it.

## Deliverable Definition — Ontology

The outputs below restate only the anticipated artifacts in the applied
register row and carrier `_CONTEXT.md`.

- **OUT-001 — Root runtime API v2 contract.** One versioned Root runtime API
  v2 contract covering this adapter/event/approval slice.
- **OUT-002 — Attributed approval schemas.** Approval request and approval
  decision schemas whose records are attributed; unattributed decisions are
  excluded.
- **OUT-003 — Closed HarnessEvent v2 union.** A closed event union whose only
  terminal identifiers are `turn.completed`, `turn.failed`,
  `turn.interrupted`, and `turn.cancelled`.
- **OUT-004 — Role-posture evidence projection.** A projection representing
  Agent 0/1/2 role-entry parity and the explicit Agent 2/TASK fallback labelled
  `role not mechanically enforced`, with governed-workflow evidence marked
  `instruction-asserted` when G-ROLE cannot mechanically prove
  non-delegation.
- **OUT-005 — Managed-network approval routing.** `networkApprovalContext`
  routing through Root API v2 that shows host and protocol, preserves the
  caveat that a grant may unblock queued requests to the same destination, and
  permits `acceptForSession` only as an explicit user act.
- **OUT-006 — Adapter projection and redaction fixtures.** Deterministic wire
  fixtures showing that unknown provider payloads are rejected, redacted, or
  projected rather than persisted in provider-shaped form.

These outputs are bounded to one versioned adapter/API slice. They do not add
another interface, provider-persistence model, dependency, tool, schedule, or
implementation surface.

## Completion and Reliance Basis — Epistemology

- **CLM-001 — Attributed approvals.** The applied register and carrier context
  require attributed approval request and decision records and exclude
  unattributed decisions.
- **CLM-002 — Closed terminal set.** The HarnessEvent v2 union is closed, and
  its only terminal identifiers are `turn.completed`, `turn.failed`,
  `turn.interrupted`, and `turn.cancelled`. No fifth terminal identifier is
  admitted by this contract.
- **CLM-003 — Unknown payload boundary.** Adapter behavior rejects, redacts,
  or projects unknown provider payloads; provider-shaped persistence is
  excluded.
- **CLM-004 — G0 A3 carriage.** Agent 0/1/2 role entry remains offered for
  Codex sessions. When G-ROLE cannot mechanically prove Agent 2
  non-delegation, explicit Agent 2/TASK mode remains offered as `role not
  mechanically enforced`; its governed-workflow evidence is
  `instruction-asserted`, and delegated-harness-native K-SUBAGENT
  non-delegation is instruction+config asserted rather than mechanism-proven.
  Hard filesystem, network, and process containment is unchanged.
- **CLM-005 — G0 A7 carriage.** Each canonical root chooses under consent
  among three command-network postures: no command network by default; ask per
  destination using managed-network prompts routed as stated in `OUT-005`; or
  command network on, labelled `network_access = true`. OpenAI account, model,
  and turn service endpoints remain separately enumerated from command
  network.

A completion claim requires this deliverable's own accepted evidence covering
its outputs and the constraints above. The existence of this SOW, another
deliverable's evidence, a prompt, a fixture, or an implementation byte does
not by itself establish completion or warrant reliance. Evidence remains
subject to its own recorded basis and accountable-human disposition.

Nothing in this SOW lifts a hold, authorizes implementation, or creates
dispatch authority. Acceptance of this SOW is a separate owner act against
its exact bytes. No acceptance criterion, dependency edge, interface detail,
tool command, estimate, or schedule is inferred where the accepted sources do
not supply one.

## Production and Verification Method — Praxeology

Production, if separately authorized, is bounded to the six outputs above and
the accepted constraints they carry. The recorded anticipated write locus is:

`runtime/**; execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-10_Adapter_Event_Schema_and_Approval_API_v2/**`

That locus is planning information only. It grants no write, implementation,
dispatch, activation, or release authority.

Verification is evidence planning, not a claim that a method, tool, or result
already exists:

- **VER-001 — Contract and fixture inspection.** Evidence for `OUT-001`,
  `OUT-002`, and `OUT-003` identifies the exact versioned contract bytes,
  demonstrates attribution of approval requests and decisions, and
  demonstrates that the terminal set contains exactly the four identifiers in
  `CLM-002`.
- **VER-002 — Unknown-payload fixture inspection.** Evidence for `OUT-006`
  demonstrates each applicable reject, redact, or project outcome and shows no
  provider-shaped persistence.
- **VER-003 — Role-posture projection inspection.** Evidence for `OUT-004`
  preserves the exact fallback and evidence labels in `CLM-004` without
  presenting instruction+config assertion as mechanism proof.
- **VER-004 — Managed-network prompt evidence.** Evidence for `OUT-005`
  demonstrates routed prompt delivery with visible host/protocol, records the
  same-destination queued-request grouping caveat, and shows
  `acceptForSession` only after an explicit user act. In accordance with G0
  A7, G-APPR must prove prompt delivery and observe grouping empirically at the
  exact pin; this SOW neither selects that pin nor claims that proof exists.
- **VER-005 — Posture inspection.** Evidence distinguishes the three
  per-root consent postures and preserves no command network as the default and
  `network_access = true` as the labelled command-network-on posture, while
  keeping OpenAI account, model, and turn service endpoints separately
  enumerated from command network.

No verification tool or command is named because the accepted grounding
sources name none for this deliverable. The eventual evidence must record its
own exact basis; semantic completion and reliance remain accountable-human
judgments.

## Governing Values and Decisions — Axiology

- **AX-001 — Accepted grounding only.** This draft is grounded in the applied
  `DEL-02-10_Adapter_Event_Schema_and_Approval_API_v2` register row, the
  carrier `_CONTEXT.md`, `Propagation_Plan.md` section 2 `INIT-04`, and the
  accepted G0 A3/A7 record and amendment carriage. No unaccepted plan content
  is treated as product truth.
- **AX-002 — Human authority.** The owner separately accepts, corrects, or
  declines this exact SOW. Evidence supports a later decision; it does not
  make that decision.
- **AX-003 — Consent and attribution.** No command network is the default;
  broader posture requires the recorded consent path. Approval decisions are
  attributed, and `acceptForSession` is available only through explicit user
  action.
- **AX-004 — Closed and truthful projection.** The four-terminal union remains
  closed. Unknown provider payloads are rejected, redacted, or projected, and
  provider-shaped persistence is excluded.
- **AX-005 — Calibrated role evidence.** Role parity and the labelled
  Agent 2/TASK fallback are preserved while instruction-asserted evidence is
  not upgraded to mechanism-proven evidence. Hard filesystem/network/process
  containment remains unchanged.
- **AX-006 — Planning is not authority.** The anticipated write locus and the
  outputs in this contract are planning statements. They authorize no
  implementation, dispatch, activation, lifecycle transition, hold lift, or
  release act.

Grounding citations:

- `execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv`, row
  `DEL-02-10_Adapter_Event_Schema_and_Approval_API_v2`.
- `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-10_Adapter_Event_Schema_and_Approval_API_v2/_CONTEXT.md`.
- `execution/_ScopeChange/SCA-004_2026-08-22_1749/Propagation_Plan.md`, section
  2, `INIT-04`.
- `plans/steers/chirality_app_v3_g0_record_2026-08-22.md`, owner rulings A3
  and A7, as allocated by the accepted SCA-004 amendment.

## Output and Evaluation Matrix

| Output | Scope/objective refs | Grounded completion subject | Evidence expectation | Reliance boundary |
|---|---|---|---|---|
| OUT-001 | SOW-104; OBJ-001, OBJ-002, OBJ-004, OBJ-007 | One versioned Root runtime API v2 contract for this slice | Exact contract identity and bytes, bound to the evidence basis | Draft output definition only; completion requires this deliverable's own accepted evidence |
| OUT-002 | SOW-104; OBJ-001, OBJ-002, OBJ-004, OBJ-007 | Attributed approval request and decision schemas; no unattributed decisions | Contract/fixture evidence showing attribution in request and decision records | No approval or reliance claim is made by this SOW |
| OUT-003 | SOW-104; OBJ-001, OBJ-002, OBJ-004, OBJ-007 | Closed HarnessEvent v2 union with exactly the four stated terminal identifiers | Contract/fixture evidence enumerating the closed terminal set and no fifth identifier | No completion claim without accepted DEL-02-10 evidence |
| OUT-004 | SOW-104; OBJ-001, OBJ-002, OBJ-004, OBJ-007 | Role parity, labelled fallback, and instruction-asserted projection | Projection evidence preserving the accepted labels and proof calibration | Does not weaken containment or convert assertion into mechanism proof |
| OUT-005 | SOW-104; OBJ-001, OBJ-002, OBJ-004, OBJ-007 | Routed `networkApprovalContext`, host/protocol visibility, grouping caveat, explicit-user-act `acceptForSession`, three consent postures, and separately enumerated OpenAI service endpoints | Exact-basis prompt-delivery and empirical grouping evidence plus posture and endpoint-separation evidence | No consent, network grant, or hold lift is created here |
| OUT-006 | SOW-104; OBJ-001, OBJ-002, OBJ-004, OBJ-007 | Reject, redact, or project unknown provider payloads; no provider-shaped persistence | Deterministic wire fixtures bound to the exact contract basis | Fixture presence alone does not establish accepted completion |
