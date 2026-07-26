---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-06-05
package_id: PKG-06
decomposition_basis: execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md@653fabc9b3e8abf369f5e776a7d3ee24bf235e7a
project_scope_refs: [SOW-015]
package_objective_refs: [OBJ-005]
---

# Scope of Work — DEL-06-05

## Purpose and Objective Traceability

This Scope of Work is the production contract for `DEL-06-05` — Domain Engine
Truth Boundary — in `PKG-06_Self_Application_Variants_and_Release`. It covers
project scope item SOW-015 and supports package objective OBJ-005 (situated
specialization with governed convergence), exactly as recorded in the
deliverable register and in `_CONTEXT.md` §Scope Traceability.

The deliverable's register description is: keep engine-owned domain truth
sanctioned and exempt from the rebuildable-projection rule while the product
governs only the work around the engine and never becomes the solver or the
source of accepted engineering truth.

This contract is authored in `MODE=INIT` from the accepted decomposition basis
bound in the frontmatter. Its acceptance criteria and verification methods are
**candidates for owner review**; they assert no acceptance, no reliance, and no
lifecycle transition. Lifecycle state is held solely by `_STATUS.md`, and
`ResponsibleParty` remains `TBD` until a human assigns ownership. Nothing here
is inferred beyond the register row, `_CONTEXT.md`, the SOW-015 scope-ledger
statement, and the adopted root PRD (`docs/PRD_ROOT.md`).

The register records `AnticipatedWriteLocus: execution-tree` for this
deliverable. That is a planning note, not authorization. Should production of
any output below require touching the shared instruction surface (`AGENTS.md`,
`agents/`, `skills/`, `tools/`, root `docs/`, `init/`, `.github/workflows/`),
that act requires an independently authorized M2 instruction-surface tranche;
this Scope of Work grants none.

## Deliverable Definition — Ontology

The three outputs below are transcribed from the register field
`AnticipatedArtifacts` and from `_CONTEXT.md` §Anticipated Artifacts.

- **OUT-001** — Domain-truth boundary statement: a record in the deliverable
  folder stating where authoritative domain truth sits (with the domain
  engine), what the exemption from the rebuildable-projection rule covers, and
  where the product's own governance stops.
- **OUT-002** — Engine-owned store inventory: an enumerated list of the
  engine-owned stores held to be sanctioned authoritative domain truth —
  canonical model files, model states, analysis runs, comparisons, solver
  outputs, and handoff internals — each row naming the live engine surface it
  refers to.
- **OUT-003** — Governance-around-the-engine notes: a record of what the
  product does govern at the engine boundary — profiles, manifests, proposals,
  review notes, and gates — stated so that no note can be read as the product
  performing solving or issuing engineering truth.

- **CLM-001** — SOW-015 carries `InOutStatus: IN`, SourceRef `PRD §5.1 N-1
  stated exception [TRANSCRIBED]`, and `DecisionRef: DEC-004`. Its content is
  therefore already-in-force doctrine restated for this scope unit, not a new
  commitment: the adopted PRD labels the N-1 exception `TRANSCRIBED` from
  `docs/DIRECTIVE.md` §2.1/§2.2/§5, D-GOV-01 (Option A) and its scope note, and
  K-DOMAIN-1 (`docs/CONTRACT.md` §1.12). This deliverable records and
  inventories that boundary; it does not create, widen, or narrow it.
- **CLM-002** — The scope-ledger `Notes` field records that SOW-015 was split
  from N-1 because its maintenance locus is the variant/domain boundary. The
  outputs above are therefore boundary-maintenance records, and their natural
  reader is a variant or domain working root deciding what it may treat as
  authoritative.
- **CLM-003** — `_CONTEXT.md` records `ContextEnvelope: S` with the note "One
  stated exception with a small inventory." The output set is bounded
  accordingly: one exception, one inventory, one set of notes.

## Completion and Reliance Basis — Epistemology

The requirements below restate the obligations carried by the covered scope
item. SOW-015 (SourceRef: PRD §5.1 N-1 stated exception, `[TRANSCRIBED]`)
states that domain engines own authoritative domain truth and are exempt from
the rebuildable-projection rule; that the product governs the work around the
engine; and that the product is never the solver or the source of accepted
engineering truth.

- **REQ-001** — The boundary statement shall record that domain engines own
  authoritative domain truth and that engine-owned stores are exempt from the
  rebuildable-projection rule of the normative basis (SOW-015; PRD §5.1 N-1).
- **REQ-002** — The boundary statement shall record that the product governs
  the work *around* the engine and is never the solver and never the source of
  accepted engineering truth (SOW-015; PRD §5.1 N-1).
- **REQ-003** — Each inventory row shall name a live engine-owned surface that
  exists at the recorded basis, so that the inventory is checkable against the
  repository rather than asserted (K-INVENT-1 discipline as carried by PRD
  §5.1 N-4; unknown rows remain `TBD`).
- **REQ-004** — The three outputs shall be mutually consistent in the stores
  they treat as engine-owned; any disagreement between them, or between them
  and a live domain-engine profile, shall be surfaced rather than silently
  resolved (PRD §5.1 N-4).
- **REQ-005** — No output shall assert acceptance, issuance, professional
  approval, or engineering conclusions on behalf of an engine, and no output
  shall extend the exemption beyond engine-owned domain truth (SOW-015).

- **AC-001** — The boundary statement (OUT-001) and the notes (OUT-003)
  together state the engine-ownership rule, the projection-rule exemption, the
  "governs the work around the engine" limit, and the "never the solver, never
  the source of accepted engineering truth" limit, each cited to SOW-015 and
  its source clause.
- **AC-002** — Every row of the inventory (OUT-002) resolves to a live
  engine-owned surface at the recorded basis, or is marked `TBD` with the
  reason recorded.
- **AC-003** — No output claims lifecycle state, acceptance, or engineering
  truth, and none extends the SOW-015 exemption to any store outside
  engine-owned domain truth.

## Production and Verification Method — Praxeology

Production reads the SOW-015 ledger row, the adopted PRD §5.1 N-1 exception
text, `docs/CONTRACT.md` §1.12 (K-DOMAIN-1), and the live domain-engine
profiles under `_DomainEngines/profiles/` (at this basis:
`open_pipe_stress.yaml`, `pec.yaml`). Each inventory row is drawn from a
profile's declared path taxonomy rather than from prose.

- **VER-001** — Run
  `python3 tools/validation/validate_domain_engine_profile.py
  _DomainEngines/profiles/<profile>.yaml --output-report
  _DomainEngines/profiles/_validation/<profile>.validation.json` for each
  profile named by an inventory row, and confirm each row maps to a declared
  path-taxonomy entry in a profile that validates. Deterministic; evidence is
  the emitted JSON report.

No deterministic verification is defined for OUT-001 or OUT-003. Both are prose
records whose defect mode is *misstatement of a boundary*, and no tool in this
repository reads a boundary statement and rules on its faithfulness. Validating
this contract would not do so either: `tools/scope_of_work/validate_scope_of_work.py`
resolves this deliverable's production format and reports `SOW_V1`, a result
invariant to whether either record has been written or states the boundary
correctly. Those two rows therefore carry named human review.

Where a criterion turns on whether prose states a boundary faithfully, no
deterministic check exists; those rows are verified by named human review in
the matrix below and remain the owner's judgment (K-AUTH-1).

## Governing Values and Decisions — Axiology

- **AX-001** — The exemption is stated, bounded, and sanctioned. SOW-015 is an
  exception carved into the file-native normative basis, so the deliverable's
  value is precision about its edges: what is exempt, and everything that is
  not.
- **AX-002** — The product is not the solver. Recording the boundary must never
  read as the product acquiring domain authority; the engine's truth stays the
  engine's, and accepted engineering truth is never sourced from this product
  (SOW-015; PRD §5.1 N-1).
- **AX-003** — Restatement is not amendment. Because SOW-015 is `TRANSCRIBED`
  doctrine, a production act that appears to change the boundary is a defect in
  this deliverable, not a change to the boundary; changing it would require its
  own governed instrument.
- **AX-004** — Unknowns stay `TBD` and conflicts are surfaced. An inventory row
  that cannot be tied to a live engine-owned surface is recorded as unknown,
  never invented (PRD §5.1 N-4; K-INVENT-1, K-CONFLICT-1).

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-015 OBJ-005 | REQ-001 REQ-002 REQ-005 CLM-001 | AC-001 AC-003 | HUMAN_REVIEW: owner or delegate reads the boundary statement against the SOW-015 ledger row and PRD §5.1 N-1 and records the reading | Boundary statement in the deliverable folder plus the recorded review note |
| OUT-002 | SOW-015 OBJ-005 | REQ-003 REQ-004 CLM-002 CLM-003 | AC-002 | VER-001 | Inventory record plus the domain-engine profile validation report for each cited profile |
| OUT-003 | SOW-015 OBJ-005 | REQ-002 REQ-004 REQ-005 CLM-001 | AC-001 AC-003 | HUMAN_REVIEW: owner or delegate reads the governance-around-the-engine notes against the SOW-015 ledger row and PRD §5.1 N-1, confirms every item the notes claim the product governs sits around the engine rather than inside engine-owned domain truth, and records that no note states or implies the product solving or issuing accepted engineering truth | Governance-around-the-engine notes plus the recorded review note naming the reviewer, the basis read, and the disposition |
