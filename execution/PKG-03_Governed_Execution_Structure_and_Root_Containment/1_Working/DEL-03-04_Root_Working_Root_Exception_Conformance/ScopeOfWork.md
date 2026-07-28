---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-03-04
package_id: PKG-03
decomposition_basis: execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md@653fabc9b3e8abf369f5e776a7d3ee24bf235e7a
project_scope_refs: [SOW-034, SOW-063]
package_objective_refs: [OBJ-004]
---

# Scope of Work — DEL-03-04

## Purpose and Objective Traceability

This deliverable keeps the single governed working-root exception exact. The
root product's working root is the repository root and root `execution/` is its
execution root, eligible for packages and deliverables only from an accepted
root decomposition derived from an adopted PRD and only while the guards pass,
with the containment mechanisms incorporated by reference and containment never
mistaken for authorization.

It covers two project scope items and supports one package objective:

- `SOW-034` (SourceRef: PRD §5.2 O-9 [TRANSCRIBED]) — the instruction root is
  separated from the working root with exactly one governed exception, and the
  replacement containment contract of mechanisms M1–M7 and guards G0–G4 with
  its gate ordering is required and incorporated by reference.
- `SOW-063` (SourceRef: PRD §6.2 [TRANSCRIBED]) — deterministic guards and
  human gates supply containment but neither supplies authorization; the
  instruction-surface gate does not itself grant authorization.
- `OBJ-004` — safe self-application without self-authorization: falsifiers
  F1–F3 unobserved; every root capability consumed by root development was
  accepted through the basis or an explicitly accepted predecessor; G0–G4
  registered and passing at every materialization.

The deliverable is a `REQ_SLICE` under context envelope M. Its
`AnticipatedWriteLocus` in the accepted decomposition is `execution-tree`; that
is a planning note, not authorization. Any act touching the instruction surface
(`AGENTS.md`, `agents/`, `skills/`, `tools/`, root `docs/`, `init/`,
`.github/workflows/`) requires an independently authorized M2 tranche, and this
Scope of Work grants none.

## Deliverable Definition — Ontology

The anticipated artifacts transcribed from the deliverable register are three
conformance products held in the execution tree.

- **OUT-001** — Exception conformance statement. A statement that records the
  single governed exception exactly as `SOW-034` states it: both roots named,
  the eligibility conditions stated in full (an accepted root decomposition,
  itself derived from an adopted PRD, and guards passing), and no second
  exception created or implied.
- **OUT-002** — Mechanism and guard reference map. A resolution map from each
  containment mechanism M1–M7 and each deterministic guard G0–G4 to its live
  source anchor and, for the guards, to the registered validator that executes
  it. The map incorporates the containment contract by reference; it does not
  restate, amend, or re-derive it.
- **OUT-003** — Containment-is-not-authorization note. A note recording that
  deterministic guards and human gates supply containment and that neither
  supplies authorization, including the specific case that the
  instruction-surface (M2) gate does not itself grant authorization.

- **CLM-001** — `SOW-034` is a TRANSCRIBED scope item: its authority is PRD
  §5.2 O-9, which itself incorporates D-GOV-21 §5 by reference. The mechanism
  set and guard set are therefore enumerated at their source and consumed here,
  not defined here.
- **CLM-002** — `SOW-063` is a TRANSCRIBED scope item sourced at PRD §6.2. It
  states a limit on what containment machinery can do, not a capability the
  machinery has.
- **CLM-003** — The exception is narrow by construction. D-GOV-21 §Effects 1
  records that no other working root gains this property, and §Effects 2
  records that root `execution/` becomes eligible for `PKG-*`/`DEL-*` only
  after the packet's §6 gates close.

## Completion and Reliance Basis — Epistemology

- **REQ-001** — The exception conformance statement shall state the exception
  in the exact terms of `SOW-034`, naming the repository root as the root
  product's working root, root `execution/` as its execution root, and both
  eligibility conditions. It shall create no second exception and shall
  generalize the exception to no other working root.
- **REQ-002** — The mechanism and guard reference map shall cover mechanisms
  M1–M7 and guards G0–G4 with no gap, and every entry shall resolve to a live
  anchor. Guard entries shall name the registered validator and its state
  surface. The map shall incorporate the §5.3 gate ordering by reference rather
  than restating it.
- **REQ-003** — The containment-is-not-authorization note shall state the
  `SOW-063` limit without exception or hedge, and shall name the
  instruction-surface gate as a case that does not itself grant authorization.
- **REQ-004** — No output of this deliverable shall create, extend, or imply
  authority. Each output is conformance description against an accepted source;
  authorization remains an attributable human act under the governed record.

- **AC-001** — The conformance statement names both roots, states both
  eligibility conditions, and contains no exception beyond the single governed
  one; a reviewer can check each element against PRD §5.2 O-9 without consulting
  a person.
- **AC-002** — Every mechanism M1–M7 and guard G0–G4 has exactly one map entry;
  every entry's cited anchor resolves in the checkout; and every guard entry's
  named validator exists and exits 0 when run.
- **AC-003** — The note states that neither deterministic guards nor human
  gates supply authorization, and names the instruction-surface gate case
  explicitly.

- **CON-001** — The accepted decomposition states no per-deliverable acceptance
  criteria for DEL-03-04, and `_CONTEXT.md` records them as TBD. `AC-001`,
  `AC-002`, and `AC-003` are therefore candidate criteria authored under this
  initialization run; they claim no acceptance and become binding only through
  an owner act at the human-gated review. `ResponsibleParty` is `Ryan Tufts` under D-GOV-27 and the current deliverable register.

## Production and Verification Method — Praxeology

Production reads the accepted decomposition row, this deliverable's
`_CONTEXT.md`, the scope-ledger statements of `SOW-034` and `SOW-063`, and the
adopted PRD. It reads the containment contract at its source and cites it; it
never re-derives the mechanism or guard sets from discussion.

- **VER-001** — Registered guard execution. Run the validators registered for
  G0–G4 in `tools/REGISTRY.md` and require each to exit 0:
  `python3 tools/validation/validate_root_materialization_fence.py` (G0),
  `python3 tools/validation/validate_root_harness_adapter.py` (G1),
  `python3 tools/validation/validate_root_surface_ownership.py` (G2),
  `python3 tools/validation/validate_root_work_graph_dispatch.py` (G3), and
  `python3 tools/validation/validate_instruction_tranche_manifest.py` (G4).
  A non-zero exit falsifies the map's guard half.
- **VER-002** — Reference resolution. Confirm that every identifier in the map
  resolves against its live anchor: mechanisms M1–M7 against
  `docs/governance_harness/_DECISIONS/D-GOV-21_root_working_root_exception.md`
  §Effects 4 and the D-GOV-21 packet §5; guards G0–G4 against the
  `tools/REGISTRY.md` rows and the guard entries in
  `execution/_harness/root_guards.yaml`. An unresolvable identifier or a missing
  M1–M7 / G0–G4 entry is a failure.

Where a criterion turns on whether prose says the right thing rather than on a
computable fact, verification is an explicit human review at the gate. That
applies to `OUT-001` and `OUT-003`: a deterministic check can confirm that a
statement exists, not that it states the exception exactly or that it concedes
no authorization. No command is invented for those.

Guard execution and reference resolution are read-only. Neither this Scope of
Work nor any verification it names authorizes a write to
`execution/_harness/**`, which is root Project Setup's surface and is
authorized separately.

## Governing Values and Decisions — Axiology

- **AX-001** — Containment is not authorization (K-AUTH-1). This is the
  governing value of the whole deliverable: every mechanism and guard named here
  constrains what may happen without ever making the judgment that it should.
- **AX-002** — Exactly one exception, held exact. The value at stake in
  `SOW-034` is narrowness. A conformance product that made the exception easier
  to extend would defeat its own purpose, so `REQ-001` forbids generalization
  rather than merely discouraging it.
- **AX-003** — Incorporation by reference, not restatement. The containment
  contract's authority is D-GOV-21 §5. A restatement here would create a second
  live variant of ruled text and put the deliverable in conflict with its own
  source. Detected drift between the map and its anchors is a REVIEW finding
  routed to the owner, never an automatic amendment (D-GOV-02; K-AUTH-1).
- **AX-004** — Falsifiability over assurance. `OBJ-004` is stated as falsifiers
  unobserved and guards passing, so the verification methods here are checks
  that can fail and be seen to fail, not attestations.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-034 OBJ-004 | CLM-001 CLM-003 REQ-001 REQ-004 | AC-001 | HUMAN_REVIEW: owner review of the conformance statement against PRD §5.2 O-9 and D-GOV-21 §Effects 1–2 at the human-gated PR review | The statement in the execution tree, with its element-by-element citation to PRD §5.2 O-9, and the reviewer's recorded disposition |
| OUT-002 | SOW-034 OBJ-004 | CLM-001 CLM-003 REQ-002 REQ-004 | AC-002 | VER-001 VER-002 | The reference map with one entry per M1–M7 and G0–G4; captured exit statuses of the five registered guard validators; recorded resolution of every cited anchor |
| OUT-003 | SOW-063 OBJ-004 | CLM-002 REQ-003 REQ-004 | AC-003 | HUMAN_REVIEW: owner review of the note against PRD §6.2 and K-AUTH-1 at the human-gated PR review | The note in the execution tree, citing PRD §6.2 and the D-GOV-21 M2 gate clause, and the reviewer's recorded disposition |

The matrix is the stable target. It records no lifecycle state and no
acceptance; the deliverable remains `OPEN`, and `_STATUS.md` is the sole
lifecycle authority.
