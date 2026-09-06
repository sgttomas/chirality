---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-02-07
package_id: PKG-02
decomposition_basis: projects/chirality-runtime/execution/_Decomposition/Chirality_Runtime_SOFTWARE_DECOMP_v1_0.md@8209bc54e0d133b19437c93b184cd50ba3d43489
project_scope_refs: [SOW-104]
package_objective_refs: [OBJ-001, OBJ-002, OBJ-004, OBJ-007]
---

# Scope of Work — DEL-02-07

## Purpose and Objective Traceability

This Scope of Work defines the production contract for
`DEL-02-07`, Process Supervisor and Purpose-Limited Control, a
`BACKEND_FEATURE_SLICE` deliverable of
`PKG-02_Runtime_Product`. It serves project
scope item `SOW-104` and package objectives `OBJ-001`, `OBJ-002`, `OBJ-004`,
and `OBJ-007`. Its accepted Context Envelope is `M`.

The applied deliverable-register row and carrier `_CONTEXT.md` define one
cohesive supervisor/control slice: provide
`DelegatedHarnessProcessSupervisorPort`; a purpose-limited second private Unix
socket; worker acquisition, inventory, and reconnect; generation fencing and
stale recovery; and daemon-plus-supervisor two-job launch integration. The
same accepted sources require authentication-token validation for every
socket request, with each token bound to the socket owner and worker
generation and invalidated during stale-socket recovery.

The controlling runtime boundary is: **daemon remains sole runtime broker, authenticated private Unix socket, no TCP listener**. The purpose-limited
socket is never renderer- or CLI-callable. Delegated-harness-native descent
does not assign a role. Agent 0/1/2 role-entry parity for primary Codex
sessions is preserved inside unchanged hard filesystem/network/process
containment.

This contract is grounded in the accepted runtime decomposition, its
`RUNTIME_DELIVERABLE_REGISTER.csv`, and this carrier's `_CONTEXT.md`.
The inherited source is retained at
`projects/chirality-runtime/execution/_Decomposition/SOURCE_SCOPE_REQUIREMENTS/DEL-02-07_Process_Supervisor_and_Purpose_Limited_Control.md`.
Its historical bases remain the Root deliverable register,
`execution/_ScopeChange/SCA-004_2026-08-22_1749/Propagation_Plan.md` section 2,
`INIT-01`, and `plans/steers/chirality_app_v3_g0_record_2026-08-22.md`, ruling A3.
The accepted `OWNERSHIP_OVERLAY.md` governs the exact ownership and code-locus
changes; `_AUTHORITY.md` and the project's `MIGRATION_APPLICATION.md` record
actual acceptance and application. Relative companion names resolve beside the
runtime decomposition; historical paths remain repository-relative.

The runtime contract identity remains `root-runtime-1`, epoch 1. Its immutable
compatibility evidence retains ten historical markers: nine holds remain;
R16-B disposes Tier-0 separately as continue-separate. The upstream
DEL-02-06/REQ-027 specification/inventory/evidence-planning limit remains in
force. No implementation identity, activation, cutover, release or effective
ownership transfer is inferred from this initialization.

## Deliverable Definition — Ontology

- **OUT-001 — `DelegatedHarnessProcessSupervisorPort` contract.** The contract
  artifact for the process-supervisor boundary named by the applied register.
- **OUT-002 — Purpose-limited private Unix-socket protocol.** The protocol
  artifact carries `0700`/`0600` ownership controls and the required
  authentication-token, owner, worker-generation, and stale-recovery rules.
- **OUT-003 — Worker-control implementation.** The implementation artifact
  covers worker acquisition, inventory, reconnect, generation fencing, and
  stale recovery.
- **OUT-004 — Two-job launch integration.** The integration artifact covers
  the daemon-plus-supervisor launch topology while retaining one daemon as the
  sole runtime broker.
- **OUT-005 — Role-parity and hard-containment evidence.** The test artifact
  covers Agent 0/1/2 role-entry parity and unchanged hard
  filesystem/network/process containment.

These outputs are the anticipated artifacts from the applied register and
carrier context. Their naming here does not select implementation details,
dependencies, tools, schedules, or an implementation write tranche.

## Completion and Reliance Basis — Epistemology

### Grounded claims and requirements

- **CLM-001** — The applied register assigns this deliverable one cohesive
  PKG-02 supervisor/control slice under `SOW-104` and `OBJ-001`, `OBJ-002`,
  `OBJ-004`, and `OBJ-007`.
- **REQ-001** — The slice shall provide
  `DelegatedHarnessProcessSupervisorPort` and the purpose-limited second
  private Unix socket.
- **REQ-002** — Every request to that socket shall undergo
  authentication-token validation. Each token shall be bound to the socket
  owner and worker generation and invalidated during stale-socket recovery.
- **REQ-003** — The private Unix-socket protocol shall retain `0700`/`0600`
  ownership controls.
- **REQ-004** — The worker-control artifact shall cover worker acquisition,
  inventory, reconnect, generation fencing, and stale recovery.
- **REQ-005** — The launch integration shall carry the daemon-plus-supervisor
  two-job topology while retaining one daemon as the sole runtime broker.
- **REQ-006** — The control surface shall remain purpose-limited and never
  renderer- or CLI-callable, and it shall introduce no TCP listener.
- **REQ-007** — Agent 0/1/2 role entry shall always be offered for Codex
  sessions. When G-ROLE cannot mechanically prove Agent-2 non-delegation,
  explicit Agent 2/TASK shall remain offered as `role not mechanically
  enforced`; governed-workflow evidence shall be `instruction-asserted`; and
  delegated-harness-native K-SUBAGENT non-delegation shall be
  instruction+config asserted rather than mechanism-proven.
- **REQ-008** — Delegated-harness-native descent shall not assign a role, and
  hard filesystem/network/process containment shall remain unchanged.

### Acceptance records from existing evidence expectations

- **AC-001** — Contract evidence for the named `DelegatedHarnessProcessSupervisorPort` boundary. Reliance requires this deliverable's own accepted evidence plus a separate owner act. Verified by VER-001.
- **AC-002** — Protocol evidence for the purpose-limited private Unix socket, ownership controls, and token/owner/generation/stale-recovery rules. Reliance requires this deliverable's own accepted evidence plus a separate owner act. Verified by VER-001.
- **AC-003** — Evidence covering acquisition, inventory, reconnect, generation fencing, and stale recovery. Reliance requires this deliverable's own accepted evidence plus a separate owner act. Verified by VER-002.
- **AC-004** — Evidence for the two-job topology and all sole-broker, caller-exclusion, Unix-only, and no-TCP boundaries. Reliance requires this deliverable's own accepted evidence plus a separate owner act. Verified by VER-003.
- **AC-005** — Evidence for role-entry parity, calibrated non-delegation claims, and unchanged hard containment. Reliance requires this deliverable's own accepted evidence plus a separate owner act. Verified by VER-004.

### Completion and reliance limits

Completion claims require this deliverable's own accepted evidence for the
outputs and requirements above. The anticipated-artifact list, an
implementation, a test result, or this contract alone is not accepted evidence
and cannot establish completion by implication.

The inherited sources provide no separate per-deliverable acceptance criteria,
dependency set, implementation method, tool selection, schedule, or
activation decision. The acceptance records below structurally name only the existing matrix evidence expectations and reliance gates; no additional test, threshold or scope is introduced. Nothing in this Scope of Work
lifts a hold, authorizes implementation, creates dispatch authority, or
changes the carrier's `OPEN` lifecycle state. Acceptance of this Scope of Work
is itself a separate owner act against its exact bytes.

## Production and Verification Method — Praxeology

Production and verification remain future, separately authorized work. Within
that work, evidence must be organized against the five outputs and the eight
grounded requirements without broadening the accepted slice:

- **VER-001 — Contract and protocol trace.** Trace OUT-001 and OUT-002 to
  REQ-001, REQ-002, and REQ-003, including request-by-request token
  validation, owner and worker-generation binding, stale-recovery
  invalidation, and the stated ownership controls.
- **VER-002 — Worker-control trace.** Trace OUT-003 to REQ-004 across worker
  acquisition, inventory, reconnect, generation fencing, and stale recovery.
- **VER-003 — Launch-boundary trace.** Trace OUT-004 to REQ-005 and REQ-006,
  including evidence that the daemon remains the sole runtime broker, the
  control surface is not renderer- or CLI-callable, and no TCP listener is
  introduced.
- **VER-004 — Role and containment trace.** Trace OUT-005 to REQ-007 and
  REQ-008, preserving the required role-entry and evidence labels and showing
  unchanged hard filesystem/network/process containment.

These traces state the evaluation boundary derived from accepted sources;
they do not prescribe a tool, implementation design, schedule, dependency, or
dispatch plan. Verification results become reliance-bearing only after their
own evidence is accepted through a separately authorized act.

## Governing Values and Decisions — Axiology

- **AX-001 — Single-broker containment.** The process supervisor and its
  purpose-limited control surface do not become another runtime broker. The
  binding boundary remains: **daemon remains sole runtime broker, authenticated private Unix socket, no TCP listener**.
- **AX-002 — Least-purpose access.** The second private Unix socket remains
  purpose-limited, uses the stated ownership and authentication-token rules,
  and is never renderer- or CLI-callable.
- **AX-003 — Evidence calibration.** G0 A3 role parity is preserved without
  overstating proof: `instruction-asserted` and instruction+config-asserted
  claims are not represented as mechanism-proven.
- **AX-004 — Unchanged outer containment.** The slice does not weaken hard
  filesystem, network, or process containment and does not assign a role to
  delegated-harness-native descent.
- **AX-005 — Planning is not authority.** The applied register's anticipated
  write locus of `projects/chirality-runtime/**` and the successor deliverable folder is a planning note
  only. It grants no implementation or other write authority.
- **AX-006 — Human acceptance remains separate.** Drafting, verification, or
  evidence production does not accept this SOW or the deliverable. Each
  acceptance and reliance judgment remains a separate owner act over exact
  bytes and evidence.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-104; OBJ-001, OBJ-002, OBJ-004, OBJ-007 | CLM-001; REQ-001 | AC-001 | VER-001 | Contract evidence for the named `DelegatedHarnessProcessSupervisorPort` boundary; This deliverable's own accepted evidence plus a separate owner act |
| OUT-002 | SOW-104; OBJ-001, OBJ-002, OBJ-004, OBJ-007 | REQ-001, REQ-002, REQ-003 | AC-002 | VER-001 | Protocol evidence for the purpose-limited private Unix socket, ownership controls, and token/owner/generation/stale-recovery rules; This deliverable's own accepted evidence plus a separate owner act |
| OUT-003 | SOW-104; OBJ-001, OBJ-002, OBJ-004, OBJ-007 | REQ-004 | AC-003 | VER-002 | Evidence covering acquisition, inventory, reconnect, generation fencing, and stale recovery; This deliverable's own accepted evidence plus a separate owner act |
| OUT-004 | SOW-104; OBJ-001, OBJ-002, OBJ-004, OBJ-007 | REQ-005, REQ-006 | AC-004 | VER-003 | Evidence for the two-job topology and all sole-broker, caller-exclusion, Unix-only, and no-TCP boundaries; This deliverable's own accepted evidence plus a separate owner act |
| OUT-005 | SOW-104; OBJ-001, OBJ-002, OBJ-004, OBJ-007 | REQ-007, REQ-008 | AC-005 | VER-004 | Evidence for role-entry parity, calibrated non-delegation claims, and unchanged hard containment; This deliverable's own accepted evidence plus a separate owner act |
