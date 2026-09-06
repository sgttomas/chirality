---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-02-10
package_id: PKG-02
decomposition_basis: projects/chirality-runtime/execution/_Decomposition/Chirality_Runtime_SOFTWARE_DECOMP_v1_0.md@8209bc54e0d133b19437c93b184cd50ba3d43489
project_scope_refs: [SOW-104]
package_objective_refs: [OBJ-001, OBJ-002, OBJ-004, OBJ-007]
---

# Scope of Work — DEL-02-10

## Purpose and Objective Traceability

This Scope of Work defines the production contract for
`DEL-02-10` — Adapter Event Schema and Approval API v2 — an `API_CONTRACT`
deliverable in
`PKG-02_Runtime_Product`. It covers project
scope item `SOW-104` and supports package objectives `OBJ-001`, `OBJ-002`,
`OBJ-004`, and `OBJ-007`, exactly as recorded in the applied deliverable
register.

The accepted boundary is: **Runtime API v2, closed event union with only the four terminal identifiers, attributed approvals**.
Within its recorded Context Envelope `M`, this is one versioned adapter/API
slice with deterministic wire fixtures. It carries the allocated G0 A3
role-posture rules and G0 A7 command-network consent rules.

This contract does not claim that any output is accepted, complete, implemented, dispatched, activated,
or relied upon. The deliverable's lifecycle state remains `OPEN` as recorded
in `_STATUS.md`; this SOW does not change it.

Current scope grounding is the runtime decomposition and its
`RUNTIME_DELIVERABLE_REGISTER.csv`, with this carrier's `_CONTEXT.md`.
The full inherited contract is retained at
`projects/chirality-runtime/execution/_Decomposition/SOURCE_SCOPE_REQUIREMENTS/DEL-02-10_Adapter_Event_Schema_and_Approval_API_v2.md`.
The exact accepted `OWNERSHIP_OVERLAY.md`, `_AUTHORITY.md` and project
`execution/_Coordination/MIGRATION_APPLICATION.md` distinguish present
application from historical acceptance. Companion filenames resolve beside the
runtime decomposition; historical citations remain repository-relative.

The contract identity remains `root-runtime-1`, epoch 1. Ten historical
compatibility markers remain immutable: nine holds remain outstanding and
R16-B disposes Tier-0 separately as continue-separate. Upstream
DEL-02-06/REQ-027 remains specification/inventory/evidence planning only.
Initialization supplies no implementation identity, effective ownership act,
activation, cutover, release or acceptance of new evidence.

## Deliverable Definition — Ontology

The outputs below restate only the anticipated artifacts in the applied
register row and carrier `_CONTEXT.md`.

- **OUT-001 — Runtime API v2 contract.** One versioned runtime API
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
  routing through runtime API v2 that shows host and protocol, preserves the
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
its exact bytes. The acceptance records below name only inherited matrix evidence expectations and reliance limits; they introduce no additional acceptance condition. No dependency edge, interface detail,
tool command, estimate, or schedule is inferred where the accepted sources do
not supply one.

### Acceptance records from inherited matrix expectations

- **AC-001** — Exact contract identity and bytes, bound to the evidence basis. Draft output definition only; completion requires this deliverable's own accepted evidence. Verification: VER-001.
- **AC-002** — Contract/fixture evidence showing attribution in request and decision records. No approval or reliance claim is made by this SOW. Verification: VER-001.
- **AC-003** — Contract/fixture evidence enumerating the closed terminal set and no fifth identifier. No completion claim without accepted DEL-02-10 evidence. Verification: VER-001.
- **AC-004** — Projection evidence preserving the accepted labels and proof calibration. Does not weaken containment or convert assertion into mechanism proof. Verification: VER-003.
- **AC-005** — Exact-basis prompt-delivery and empirical grouping evidence plus posture and endpoint-separation evidence. No consent, network grant, or hold lift is created here. Verification: VER-004, VER-005.
- **AC-006** — Deterministic wire fixtures bound to the exact contract basis. Fixture presence alone does not establish accepted completion. Verification: VER-002.

## Production and Verification Method — Praxeology

Production, if separately authorized, is bounded to the six outputs above and
the accepted constraints they carry. The recorded anticipated write locus is:

`projects/chirality-runtime/**; projects/chirality-runtime/execution/PKG-02_Runtime_Product/1_Working/DEL-02-10_Adapter_Event_Schema_and_Approval_API_v2/**`

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

- **AX-001 — Accepted grounding only.** The inherited contract is grounded in the applied
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

Historical grounding citations (retained at original locations):

- `execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv`, row
  `DEL-02-10_Adapter_Event_Schema_and_Approval_API_v2`.
- `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-10_Adapter_Event_Schema_and_Approval_API_v2/_CONTEXT.md`.
- `execution/_ScopeChange/SCA-004_2026-08-22_1749/Propagation_Plan.md`, section
  2, `INIT-04`.
- `plans/steers/chirality_app_v3_g0_record_2026-08-22.md`, owner rulings A3
  and A7, as allocated by the accepted SCA-004 amendment.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-104; OBJ-001, OBJ-002, OBJ-004, OBJ-007 | CLM-001, CLM-002 | AC-001 | VER-001 | One versioned Runtime API v2 contract for this slice; Exact contract identity and bytes, bound to the evidence basis; Draft output definition only; completion requires this deliverable's own accepted evidence |
| OUT-002 | SOW-104; OBJ-001, OBJ-002, OBJ-004, OBJ-007 | CLM-001 | AC-002 | VER-001 | Attributed approval request and decision schemas; no unattributed decisions; Contract/fixture evidence showing attribution in request and decision records; No approval or reliance claim is made by this SOW |
| OUT-003 | SOW-104; OBJ-001, OBJ-002, OBJ-004, OBJ-007 | CLM-002 | AC-003 | VER-001 | Closed HarnessEvent v2 union with exactly the four stated terminal identifiers; Contract/fixture evidence enumerating the closed terminal set and no fifth identifier; No completion claim without accepted DEL-02-10 evidence |
| OUT-004 | SOW-104; OBJ-001, OBJ-002, OBJ-004, OBJ-007 | CLM-004 | AC-004 | VER-003 | Role parity, labelled fallback, and instruction-asserted projection; Projection evidence preserving the accepted labels and proof calibration; Does not weaken containment or convert assertion into mechanism proof |
| OUT-005 | SOW-104; OBJ-001, OBJ-002, OBJ-004, OBJ-007 | CLM-005 | AC-005 | VER-004, VER-005 | Routed `networkApprovalContext`, host/protocol visibility, grouping caveat, explicit-user-act `acceptForSession`, three consent postures, and separately enumerated OpenAI service endpoints; Exact-basis prompt-delivery and empirical grouping evidence plus posture and endpoint-separation evidence; No consent, network grant, or hold lift is created here |
| OUT-006 | SOW-104; OBJ-001, OBJ-002, OBJ-004, OBJ-007 | CLM-003 | AC-006 | VER-002 | Reject, redact, or project unknown provider payloads; no provider-shaped persistence; Deterministic wire fixtures bound to the exact contract basis; Fixture presence alone does not establish accepted completion |
