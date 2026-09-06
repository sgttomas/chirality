---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-02-11
package_id: PKG-02
decomposition_basis: projects/chirality-runtime/execution/_Decomposition/Chirality_Runtime_SOFTWARE_DECOMP_v1_0.md@8209bc54e0d133b19437c93b184cd50ba3d43489
project_scope_refs: [SOW-104]
package_objective_refs: [OBJ-001, OBJ-002, OBJ-004, OBJ-007]
---

# Scope of Work — DEL-02-11

## Purpose and Objective Traceability

This Scope of Work defines the production contract for `DEL-02-11`, Worker
Retirement, Restart, and Terminal Reconciliation, a `BACKEND_FEATURE_SLICE`
deliverable of `PKG-02_Runtime_Product`. The
applied deliverable register assigns it Context Envelope `M`, project scope
item `SOW-104`, and package objectives `OBJ-001`, `OBJ-002`, `OBJ-004`, and
`OBJ-007`.

The accepted register purpose is to provide `WorkerRetirementCoordinatorPort`,
prepared/committed/reconciliation-required journal state, exactly-once
active-turn terminalization, and restart behavior that uses `thread/resume`
only when canonical-root, account-identity, and policy-digest continuity holds
with cwd fixed to the canonical root; otherwise restart uses a fresh thread.
This is one bounded worker-retirement/recovery slice carrying accepted G0 A4.

**Required carriage (verbatim):** exactly-once terminalization, `thread/resume` only under recorded continuity, no in-flight re-attach claim.

The historical accepted grounding surfaces are:

- `execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv`, row
  `DEL-02-11_Worker_Retirement_Restart_and_Terminal_Reconciliation`;
- this deliverable's `_CONTEXT.md`;
- `execution/_ScopeChange/SCA-004_2026-08-22_1749/Propagation_Plan.md` §2,
  `INIT-05`; and
- `plans/steers/chirality_app_v3_g0_record_2026-08-22.md`, ruling A4.

Current allocation is the runtime-project register and approved ownership
overlay in `projects/chirality-runtime/execution/_Decomposition/`; actual
application status is `projects/chirality-runtime/execution/_Coordination/MIGRATION_APPLICATION.md`.
Root retains instruction governance and D-GOV-20 boundary authority; Ryan Tufts
remains the accountable human. The accepted compatibility identity remains
`root-runtime-1`, epoch 1; nine holds remain, with the historical Tier-0 marker
disposed separately by R16-B. DEL-02-06/REQ-027 remains specification, inventory
and evidence planning only. TM-ROOT-106 remains open; R18 closed TM-ROOT-122.
No implementation identity, hold release or effective transfer act is supplied.

## Deliverable Definition — Ontology

The anticipated artifacts recorded by the accepted register and carrier are
expressed as the following outputs:

- **OUT-001** — `WorkerRetirementCoordinatorPort` contract.
- **OUT-002** — Retirement journal and
  prepared/committed/reconciliation-required state.
- **OUT-003** — Exactly-once active-turn terminalization implementation.
- **OUT-004** — Conditional `thread/resume` continuity checks and fresh-thread
  fallback.
- **OUT-005** — Crash-retirement and replay tests.

Together these outputs cover only the accepted retirement/recovery slice.
They create no automatic replay behavior and make no in-flight re-attach
claim.

## Completion and Reliance Basis — Epistemology

- **CLM-001** — The applied DEL-02-11 register row allocates this bounded slice
  to DEL-02-11 and records the five anticipated artifacts represented by
  OUT-001 through OUT-005.
- **CLM-002** — Accepted G0 A4 requires active turns to terminalize on
  retirement or crash before the next action; the next action may use
  `thread/resume` only when canonical-root, account-identity, policy-digest,
  and canonical-cwd continuity hold, and otherwise uses a fresh thread.
- **CLM-003** — The accepted carrier context and INIT-05 boundary exclude any
  in-flight re-attach or automatic replay claim.

A completion claim requires this deliverable's own accepted evidence. This
Scope of Work is not that evidence and does not establish completion,
reliance, release, or acceptance. Nothing in this Scope of Work lifts any hold,
authorizes implementation, or creates dispatch authority. Owner acceptance of
this Scope of Work is a separate act against its exact bytes.

No dependency is declared or inferred here. Dependencies, interfaces beyond
the accepted `WorkerRetirementCoordinatorPort` name, tools, estimates,
schedules, lifecycle transitions, implementation details, activation, and
hold disposition remain outside this Scope of Work.

- **AC-001** — Separately accepted evidence for the `WorkerRetirementCoordinatorPort` contract. Evaluation is HUMAN_REVIEW against CLM-001.
- **AC-002** — Separately accepted evidence for prepared, committed, and reconciliation-required journal state. Evaluation is HUMAN_REVIEW against CLM-001.
- **AC-003** — Separately accepted evidence that active turns terminalize exactly once on retirement or crash. Evaluation is HUMAN_REVIEW against CLM-001 CLM-002.
- **AC-004** — Separately accepted evidence that `thread/resume` occurs only under recorded continuity and a fresh thread is used otherwise. Evaluation is HUMAN_REVIEW against CLM-001 CLM-002.
- **AC-005** — Separately accepted crash-retirement and replay-test evidence carrying no automatic replay or in-flight re-attach claim. Evaluation is HUMAN_REVIEW against CLM-001 CLM-003.

These acceptance records express only the inherited matrix evidence expectations.
They add no threshold, implementation method or claim of acceptance.

## Production and Verification Method — Praxeology

A later, separately authorized production act may realize OUT-001 through
OUT-005 only within the accepted anticipated write-locus planning boundary:
`projects/chirality-runtime/**` and this runtime-project deliverable folder. That locus is a planning note and is
never write authorization.

Verification is limited to the evidence surfaces already anticipated by the
accepted register: the coordinator contract, journal and reconciliation
state, terminalization implementation, continuity checks with fresh-thread
fallback, and crash-retirement and replay tests. The evidence must demonstrate
that active-turn retirement/crash terminalization occurs exactly once; that
`thread/resume` is used only under the recorded canonical-root,
account-identity, policy-digest, and canonical-cwd continuity; that a fresh
thread is used otherwise; and that neither automatic replay nor in-flight
re-attachment is claimed.

The applicable implementation method, test tool, dispatch structure, and
acceptance procedure are not established by the accepted sources and are
therefore not invented here.

## Governing Values and Decisions — Axiology

- **AX-001** — Exactly-once terminalization precedes restart choice; persisted
  thread availability alone is not recorded continuity.
- **AX-002** — Conditional `thread/resume` is recovery of a stored thread, not
  a claim that an in-flight turn can be re-attached.
- **AX-003** — Fresh-thread fallback is required when the recorded continuity
  conditions do not hold and does not imply automatic replay.
- **AX-004** — The anticipated write locus is planning only. Implementation,
  activation, lifecycle change, hold lift, release, and reliance each remain
  behind their separate authority gates.
- **AX-005** — Consequential acceptance, reliance, and release disposition
  remain accountable-human judgments; this Scope of Work neither performs nor
  transfers them.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-104; OBJ-001, OBJ-002, OBJ-004, OBJ-007 | CLM-001 | AC-001 | HUMAN_REVIEW: accountable human reviews the stated evidence against the cited existing claims | Separately accepted evidence for the `WorkerRetirementCoordinatorPort` contract |
| OUT-002 | SOW-104; OBJ-001, OBJ-002, OBJ-004, OBJ-007 | CLM-001 | AC-002 | HUMAN_REVIEW: accountable human reviews the stated evidence against the cited existing claims | Separately accepted evidence for prepared, committed, and reconciliation-required journal state |
| OUT-003 | SOW-104; OBJ-001, OBJ-002, OBJ-004, OBJ-007 | CLM-001 CLM-002 | AC-003 | HUMAN_REVIEW: accountable human reviews the stated evidence against the cited existing claims | Separately accepted evidence that active turns terminalize exactly once on retirement or crash |
| OUT-004 | SOW-104; OBJ-001, OBJ-002, OBJ-004, OBJ-007 | CLM-001 CLM-002 | AC-004 | HUMAN_REVIEW: accountable human reviews the stated evidence against the cited existing claims | Separately accepted evidence that `thread/resume` occurs only under recorded continuity and a fresh thread is used otherwise |
| OUT-005 | SOW-104; OBJ-001, OBJ-002, OBJ-004, OBJ-007 | CLM-001 CLM-003 | AC-005 | HUMAN_REVIEW: accountable human reviews the stated evidence against the cited existing claims | Separately accepted crash-retirement and replay-test evidence carrying no automatic replay or in-flight re-attach claim |
