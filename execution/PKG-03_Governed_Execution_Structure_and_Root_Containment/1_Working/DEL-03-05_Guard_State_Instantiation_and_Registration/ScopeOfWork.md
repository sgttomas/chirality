---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-03-05
package_id: PKG-03
decomposition_basis: execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md@653fabc9b3e8abf369f5e776a7d3ee24bf235e7a
project_scope_refs: [SOW-001, SOW-034]
package_objective_refs: [OBJ-004]
---

# Scope of Work — DEL-03-05

## Purpose and Objective Traceability

This deliverable instantiates and maintains the root guard state surfaces that
the G0–G4 guards read — guard registration, the harness adapter, the
surface-ownership register, and the accepted work graph — so that every
materialization runs with guards registered and passing.

It covers two project scope items and supports one package objective:

- `SOW-001` (SourceRef: PRD §3 v1 boundary (a) [PROPOSED]) — v1 is reached only
  when the D-GOV-21 §6 sequence has closed through step 9: root packages
  materialized from an accepted root decomposition with G0–G4 registered and
  passing. The scope ledger records that materialization itself remains behind
  the D-GOV-21 §5.3 gate.
- `SOW-034` (SourceRef: PRD §5.2 O-9 [TRANSCRIBED]) — the replacement
  containment contract of mechanisms M1–M7 and guards G0–G4, with its gate
  ordering, is required and incorporated by reference.
- `OBJ-004` — safe self-application without self-authorization, whose success
  condition includes G0–G4 registered and passing at every materialization.

The deliverable is a `DATA_MODEL_CHANGE` under context envelope M. Its
`AnticipatedWriteLocus` in the accepted decomposition is
`execution/_harness (root Project Setup; authorized separately)`.

**Write-authority boundary.** The anticipated outputs below live under
`execution/_harness/**`. Producing or amending any of them is root Project
Setup work, authorized separately from this package. This Scope of Work
describes those surfaces as the deliverable's anticipated outputs and grants no
authorization whatsoever to create, amend, or delete them. Nothing here is a
write permission, and no act of authoring this contract touched that surface.

## Deliverable Definition — Ontology

The anticipated artifacts transcribed from the deliverable register are four
schema-bound state files, one per guard that reads state.

- **OUT-001** — `execution/_harness/root_guards.yaml`. The guard registration
  surface: the record that each guard is wired and observed passing, which the
  materialization fence reads.
- **OUT-002** — `execution/_harness/adapter.yaml`. The root harness adapter
  state surface.
- **OUT-003** — `execution/_harness/surface_ownership.yaml`. The
  surface-ownership register, recording declared write ownership over
  materialized root structure.
- **OUT-004** — `execution/_harness/work_graph.yaml`. The accepted work graph,
  carrying declared write targets and dependency structure for dispatch.

- **CLM-001** — Under `SOW-001`, guard registration is a precondition of the v1
  boundary rather than an optional hygiene surface: v1 is reached only with
  G0–G4 registered and passing. `OUT-001` is the surface on which that
  condition is observable.
- **CLM-002** — Under `SOW-034`, the guard set G0–G4 and the gate ordering are
  incorporated by reference to D-GOV-21 §5. This deliverable supplies the state
  those guards consume; it does not define the guards, the contract, or the
  ordering.
- **CLM-003** — Registration is state, not authority. Recording that a guard is
  wired and observed passing holds no authority and confers none: deterministic
  guards supply containment and never supply authorization (PRD §6.2; K-AUTH-1).
- **CLM-004** — Per the deliverable's `AnticipatedWriteLocus`, the four surfaces
  are root Project Setup's write locus, authorized separately. This deliverable
  is the scope statement for that state; it is not the authorization for it.

## Completion and Reliance Basis — Epistemology

- **REQ-001** — All four state surfaces shall exist and shall validate against
  the schema each reading guard enforces, so that G0–G4 can be registered and
  observed passing at materialization.
- **REQ-002** — The surfaces shall be maintained current against the state they
  describe. When materialized root structure, declared write ownership, or the
  accepted work graph changes, the corresponding surface is updated in the same
  authorized act, so that its guard continues to pass rather than passing on
  stale state.
- **REQ-003** — No validator change is implied or authorized. The context
  envelope records four schema-bound state files with existing validators and
  tests; this deliverable produces and maintains the state those existing
  validators consume. A guard failure is evidence about the state, not a reason
  to amend the guard.
- **REQ-004** — Production or amendment of any file under `execution/_harness/**`
  requires a separate root Project Setup authorization. This Scope of Work
  grants none. Any run that treats this contract as permission to write that
  surface is out of scope by construction.
- **REQ-005** — No surface produced under this deliverable shall be relied on as
  authorization for a materialization, a merge, or an acceptance. Each is
  precondition state for a deterministic gate.

- **AC-001** — Each of the harness adapter, surface-ownership register, and
  accepted work graph is present and its reading guard exits 0 against it, with
  the exit status captured as evidence.
- **AC-002** — The guard registration surface carries an entry for each
  registered guard recording its registration status, observed status, reading
  validator, and state surface; the materialization fence exits 0 against the
  resulting state.

- **CON-001** — This contract's anticipated outputs lie outside the write scope
  of the package that owns the contract. Acceptance of `OUT-001`–`OUT-004` is
  therefore conditioned on a separate root Project Setup authorization that this
  Scope of Work neither contains nor implies. Surfaced for owner disposition;
  not resolved here.
- **CON-002** — The accepted decomposition states no per-deliverable acceptance
  criteria for DEL-03-05, and `_CONTEXT.md` records them as TBD. `AC-001` and
  `AC-002` are candidate criteria authored under this initialization run,
  grounded only in the register row, `_CONTEXT.md`, the scope-ledger statements
  of `SOW-001` and `SOW-034`, and the adopted PRD (K-INVENT-1). They claim no
  acceptance. `ResponsibleParty` is `Ryan Tufts` under D-GOV-27 and the current deliverable register.

## Production and Verification Method — Praxeology

Production is the separately authorized root Project Setup act that writes each
state surface and then runs the reading guard against the state written in that
same act. Verification below is read-only and may be run by any party with a
checkout; it asserts nothing about who was authorized to write.

- **VER-001** — State-surface guard execution. Run the validators registered in
  `tools/REGISTRY.md` for the guards that read these surfaces and require each
  to exit 0: `python3 tools/validation/validate_root_harness_adapter.py` (G1,
  reads `OUT-002`), `python3 tools/validation/validate_root_surface_ownership.py`
  (G2, reads `OUT-003`), and
  `python3 tools/validation/validate_root_work_graph_dispatch.py` (G3, reads
  `OUT-004`). A non-zero exit falsifies the corresponding surface.
- **VER-002** — Registration read-back and fence execution. Read
  `execution/_harness/root_guards.yaml` and confirm that every registered guard
  entry names its validator and state surface and records its observed status;
  then run `python3 tools/validation/validate_root_materialization_fence.py`
  (G0) and require exit 0. G0 reads the registration surface once root
  `PKG-*`/`DEL-*` structure exists, so this check binds registration to the
  materialization fence rather than to a self-report.

Both methods execute registered validators and read declared state. Neither
writes, and neither is authorized to repair a failing surface: a failure is
reported and routed, and repair happens only in a separately authorized root
Project Setup act (`REQ-004`).

## Governing Values and Decisions — Axiology

- **AX-001** — Guards contain; they do not authorize (`CLM-003`; K-AUTH-1).
  This deliverable exists to make containment observable, which is precisely why
  its outputs must never be read as permission.
- **AX-002** — Scope may name a surface it may not write. Recording
  `execution/_harness/**` as the anticipated write locus while withholding the
  authorization to write it is the intended shape, not an oversight: it keeps
  the decomposition honest about where the work lands without letting a scope
  document mint authority for it (`REQ-004`; `CON-001`).
- **AX-003** — State serves existing validators; validators are not bent to fit
  state (`REQ-003`). Amending a guard to accommodate a surface it rejects would
  invert the containment relation that `SOW-034` incorporates by reference.
- **AX-004** — Freshness is part of correctness. A guard passing against stale
  state is a false negative, which is why `REQ-002` binds surface maintenance to
  the act that changes the underlying structure rather than to a later sweep.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-001 SOW-034 OBJ-004 | CLM-001 CLM-003 REQ-001 REQ-005 | AC-002 | VER-002 | The registration surface with one entry per registered guard, plus the captured G0 exit status against the resulting state |
| OUT-002 | SOW-034 OBJ-004 | CLM-002 CLM-004 REQ-001 REQ-003 | AC-001 | VER-001 | The adapter state surface and the captured G1 exit status |
| OUT-003 | SOW-034 OBJ-004 | CLM-002 CLM-004 REQ-002 REQ-003 | AC-001 | VER-001 | The surface-ownership register and the captured G2 exit status |
| OUT-004 | SOW-001 SOW-034 OBJ-004 | CLM-002 REQ-002 REQ-003 REQ-004 | AC-001 | VER-001 | The accepted work graph and the captured G3 exit status |

The matrix is the stable target. It records no lifecycle state and no
acceptance; the deliverable remains `OPEN`, and `_STATUS.md` is the sole
lifecycle authority. Neither this matrix nor any row in it authorizes a write
under `execution/_harness/**`.
