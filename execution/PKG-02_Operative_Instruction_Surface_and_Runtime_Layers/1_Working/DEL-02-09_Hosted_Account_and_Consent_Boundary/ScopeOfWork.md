---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-02-09
package_id: PKG-02
decomposition_basis: execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md@75c4e2ba401a6f5ad0c2f38846c39db6ab157405
project_scope_refs: [SOW-104]
package_objective_refs: [OBJ-001, OBJ-002, OBJ-004, OBJ-007]
status: DRAFT_AWAITING_OWNER_ACCEPTANCE
---

# Scope of Work — DEL-02-09

## Purpose and Objective Traceability

This draft Scope of Work defines the production boundary for `DEL-02-09`,
Hosted Account and Consent Boundary, a `SECURITY_CONTROL` deliverable of
`PKG-02_Operative_Instruction_Surface_and_Runtime_Layers`. It serves project
scope item `SOW-104` and package objectives `OBJ-001`, `OBJ-002`, `OBJ-004`,
and `OBJ-007`, exactly as recorded in the applied deliverable register.

The accepted register row assigns this deliverable the per-root hosted-account
and consent boundary: `HostedEngineConsentPort`; root-private app-owned
`CODEX_HOME`; account/epoch and policy continuity; the `K-ROLE-2`
role-posture digest; Agent 0/1/2 role-entry parity with a labelled Agent 2/TASK
fallback; and the per-root three-posture command-network consent model. The
accepted Context Envelope is `M`.

The binding boundary is: **root-private account/consent boundary, ambient `~/.codex` excluded, labelled fallback**.
Consent never crosses root, account, or policy-digest drift, and hard
filesystem/network/process containment is unchanged.

The applied register records the anticipated write locus as `runtime/**; execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-09_Hosted_Account_and_Consent_Boundary/**`.
That locus is planning only and is not authorization to implement or write
there.

## Deliverable Definition — Ontology

The six outputs below are the anticipated artifacts transcribed from the
applied register row and carrier `_CONTEXT.md`. Their detailed schemas and
implementation forms are not specified by the accepted sources and are not
invented by this draft.

- **OUT-001** — `HostedEngineConsentPort` contract.
- **OUT-002** — Root-private `CODEX_HOME` and account-continuity controls.
- **OUT-003** — `K-ROLE-2` digest schema.
- **OUT-004** — Agent 0/1/2 parity and labelled Agent 2/TASK fallback
  controls.
- **OUT-005** — Per-root three-posture consent-state model.
- **OUT-006** — Isolation, consent, and continuity tests.

## Completion and Reliance Basis — Epistemology

- **CLM-001** — The applied register row and carrier `_CONTEXT.md` allocate
  `SOW-104` and `OBJ-001`, `OBJ-002`, `OBJ-004`, and `OBJ-007` to this
  deliverable and identify its type as `SECURITY_CONTROL` and Context Envelope
  as `M`.
- **CLM-002** — G0 A3 requires Agent 0/1/2 role entry always to be offered for
  Codex sessions. When `G-ROLE` cannot mechanically prove Agent-2
  non-delegation, explicit Agent 2/TASK remains offered and is labelled `role
  not mechanically enforced`; governed-workflow evidence from that posture is
  marked `instruction-asserted`. For the delegated-harness-native class,
  `K-SUBAGENT` non-delegation is instruction+config asserted, not
  mechanism-proven. Hard filesystem/network/process containment is unchanged.
- **CLM-003** — G0 A7 requires each canonical root to choose under consent
  among three command-network postures: no command network by default; ask per
  destination through `networkApprovalContext`; or labelled command network on
  with `network_access = true`.
- **REQ-001** — The hosted-account boundary shall use root-private app-owned
  `CODEX_HOME`; ambient `~/.codex` is excluded.
- **REQ-002** — The boundary shall preserve account/epoch and policy continuity,
  and consent shall not cross root, account, or policy-digest drift.
- **REQ-003** — The `K-ROLE-2` digest and role controls shall preserve the A3
  parity, label, and evidence-posture distinctions stated in `CLM-002` without
  changing hard filesystem/network/process containment.
- **REQ-004** — The per-root consent-state model shall preserve all three A7
  postures stated in `CLM-003`, with no command network as the default.
- **REQ-005** — In ask-per-destination posture,
  `networkApprovalContext` shall show host/protocol and shall preserve the
  caveat that a grant may unblock queued requests to the same destination;
  `acceptForSession` is allowed only by explicit user act.
- **REQ-006** — The labelled command-network-on posture shall use
  `network_access = true`.

A completion claim requires this deliverable's own accepted evidence for the
applicable outputs and requirements. The accepted sources specify no
per-output acceptance criteria, implementation design, dependency set,
schedule, or production tool, so this draft supplies none. Nothing in this
Scope of Work lifts a hold, authorizes implementation, or creates dispatch
authority. All ten DEL-02-06 bindings remain `HELD_UNAVAILABLE`. Acceptance of
this Scope of Work is itself a separate owner act against its exact bytes.

## Production and Verification Method — Praxeology

The accepted sources allocate the artifact classes and boundary constraints,
but do not prescribe a production sequence, interface design, implementation
method, dependency, tool, schedule, or acceptance procedure. Those matters
remain for separately authorized and accepted later work; this draft does not
fill them by inference.

Verification evidence, when separately produced and accepted, must be the
deliverable's own evidence and must address only the accepted claims attached
to each output in the matrix below. `OUT-006` is the accepted artifact class
for isolation, consent, and continuity tests. G0 A7 additionally states that
`G-APPR` must prove prompt delivery and observe destination grouping
empirically at the exact pin; this draft neither performs that proof nor claims
its result.

No test result, contract candidate, schema candidate, or observed behavior can
accept this SOW, lift a hold, authorize implementation, create dispatch
authority, or change a lifecycle state.

## Governing Values and Decisions — Axiology

- **AX-001** — Grounding is limited to
  `plans/steers/chirality_app_v3_phase2_steer_root_2026-08-23.md`; the applied
  `DEL-02-09_Hosted_Account_and_Consent_Boundary` row in
  `execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv`; the
  carrier `_CONTEXT.md`;
  `execution/_ScopeChange/SCA-004_2026-08-22_1749/Propagation_Plan.md` §2
  `INIT-03`; and A3/A7 in
  `plans/steers/chirality_app_v3_g0_record_2026-08-22.md`.
- **AX-002** — `INIT-03` carries the root-private account/consent slice with G0
  A3/A7, excludes ambient `~/.codex`, and does not itself create a Scope of
  Work, dependency, estimate, schedule, or activation state.
- **AX-003** — The anticipated write locus is a planning note, never write or
  implementation authority. Runtime implementation and any other act beyond
  these exact draft bytes require their own authority.
- **AX-004** — The A3 labelled fallback preserves truthful evidence
  calibration: `instruction-asserted` and `instruction+config asserted` are not
  restated as mechanism-proven.
- **AX-005** — The A7 consent model remains per canonical root. The default,
  prompt contents, destination-grouping caveat, explicit-user-act condition,
  and labelled on-state are preserved without adding another posture.
- **AX-006** — Unknown implementation and evaluation details remain
  unspecified rather than being inferred. The responsible party recorded in
  the applied register is Ryan Tufts; only the separate owner act can accept
  this SOW.

## Output and Evaluation Matrix

The accepted basis defines no per-output acceptance criteria or verification
procedure. `NOT_SPECIFIED` below records that grounding limit; it is not a
waiver or a completion result.

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-104 OBJ-001 OBJ-002 OBJ-004 OBJ-007 | CLM-001 REQ-001 REQ-002 | NOT_SPECIFIED | NOT_SPECIFIED | Own accepted evidence for the `HostedEngineConsentPort` contract within the account/consent boundary |
| OUT-002 | SOW-104 OBJ-002 OBJ-004 OBJ-007 | REQ-001 REQ-002 | NOT_SPECIFIED | OUT-006 | Own accepted evidence for root-private `CODEX_HOME`, ambient-home exclusion, continuity, and no cross-root/account/policy-digest consent |
| OUT-003 | SOW-104 OBJ-001 OBJ-002 OBJ-004 | CLM-002 REQ-003 | NOT_SPECIFIED | OUT-006 | Own accepted evidence for the `K-ROLE-2` digest schema and truthful role-posture distinctions |
| OUT-004 | SOW-104 OBJ-001 OBJ-002 OBJ-004 | CLM-002 REQ-003 | NOT_SPECIFIED | OUT-006 | Own accepted evidence for Agent 0/1/2 parity and the labelled Agent 2/TASK fallback without a mechanism-proven overclaim |
| OUT-005 | SOW-104 OBJ-002 OBJ-004 | CLM-003 REQ-004 REQ-005 REQ-006 | NOT_SPECIFIED | OUT-006; G-APPR evidence named by G0 A7 | Own accepted evidence for the three postures, default, prompt content, grouping caveat, explicit-user-act condition, and labelled on-state |
| OUT-006 | SOW-104 OBJ-002 OBJ-004 OBJ-007 | REQ-001 REQ-002 REQ-003 REQ-004 REQ-005 REQ-006 | NOT_SPECIFIED | NOT_SPECIFIED | Own accepted isolation, consent, and continuity evidence; no completion claim until that evidence is accepted |
