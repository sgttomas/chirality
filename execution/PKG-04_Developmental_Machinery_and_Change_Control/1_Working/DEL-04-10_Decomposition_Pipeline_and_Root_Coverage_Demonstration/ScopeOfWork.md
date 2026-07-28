---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-04-10
package_id: PKG-04
decomposition_basis: execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md@653fabc9b3e8abf369f5e776a7d3ee24bf235e7a
project_scope_refs: [SOW-004, SOW-005, SOW-008, SOW-012, SOW-043, SOW-046, SOW-050, SOW-076, SOW-083]
package_objective_refs: [OBJ-003]
---

# Scope of Work — DEL-04-10

## Purpose and Objective Traceability

This Scope of Work defines the production contract for `DEL-04-10`,
Decomposition Pipeline and Root Coverage Demonstration, a `REGISTER`
deliverable of `PKG-04_Developmental_Machinery_and_Change_Control`. It serves
project scope items SOW-004, SOW-005, SOW-008, SOW-012, SOW-043, SOW-046,
SOW-050, SOW-076 and SOW-083, and package objective OBJ-003.

The register describes the deliverable as keeping the decomposition pipeline
non-waivable, keeping developmental machinery inside product scope rather than
exempt overhead, demonstrating coverage across all four functional categories,
and maintaining the bidirectional PRD-traceability register that F4 is checked
against.

OBJ-003 requires that the human evaluation and iteration loops close, with
structural completeness holding universally rather than by sample. The
bidirectional registers are what make that completeness inspectable from files
alone, which is why nine scope items converge here.

The register records ContextEnvelope `M` with the note that this is
register-shaped machine truth over this decomposition package. The nine items
are therefore contracted as three grouped obligations rather than nine
separate ones.

## Deliverable Definition — Ontology

The anticipated artifacts recorded in the register and `_CONTEXT.md` are a
category coverage table, forward and reverse traceability registers, and
unmapped-objective open issues. They are expressed here as three outputs.

- **OUT-001** — A category coverage table showing, for each of the four
  functional categories, its decomposition coverage or its recorded reasoned
  deferral.
- **OUT-002** — Forward and reverse bidirectional traceability registers
  linking PRD items to scope items, packages, and deliverables, and linking
  each accepted scope unit back to the PRD items it serves.
- **OUT-003** — An unmapped-objective open-issues record listing every
  objective or PRD requirement without coverage, surfaced as an open issue with
  its status.

- **CLM-001** — Three items fix the pipeline's authority. SOW-043 states that
  the decomposition pipeline is not waivable, that packages and deliverables
  come only from an accepted decomposition, and that nothing authorizes
  inventing packages from discussion (PRD §5.3 D-9). SOW-046 states that
  developmental machinery is product scope rather than surrounding process — a
  legitimate target of decomposition, deliverables, and acceptance rather than
  exempt overhead (PRD §5.3 D-12). SOW-076 is an `OUT`-status transcribed
  non-goal, no waiver of the decomposition pipeline (PRD §8.1, DecisionRef
  DEC-007), and constrains this deliverable rather than describing work.
- **CLM-002** — Three items fix what the categories do and do not settle.
  SOW-008 states that the root product is constituted by four functional
  categories — normative basis, operative product, developmental machinery, and
  evidence (PRD §4.1). SOW-012 states that the categories classify functions and
  authority relationships, are non-exclusive, and do not prescribe four
  packages, and that the decomposition partition is not determined by them (PRD
  §4.3). SOW-050 states that the first root decomposition demonstrates coverage
  across all four categories, each having decomposition coverage or a recorded
  reasoned deferral, and that this constrains coverage demonstration only (PRD
  §5.3 D-15).
- **CLM-003** — Three items fix the traceability obligation. SOW-083 states
  falsifier F4: at the close of the first root decomposition, an accepted scope
  unit cannot be traced to a PRD requirement or objective, or a PRD requirement
  or objective has neither coverage nor a recorded deferral (PRD §8.2). The
  ledger records that this candidate's bidirectional traceability registers are
  the artifact F4 is checked against. SOW-005 states that objectives are
  objectives of the product rather than of any single tranche, and that
  objectives unmapped at decomposition time are surfaced as open issues rather
  than silently dropped (PRD §3). SOW-004 states that completeness is claimed
  only for the stated v1 boundary, and that if the owner defines v1 differently
  the success conditions re-scope accordingly (PRD §3, DecisionRef DEC-006).
- **CLM-004** — Because SOW-012 denies that the categories prescribe the
  partition, the coverage table is a coverage demonstration and never a
  partition justification. A category with coverage spread across several
  packages satisfies SOW-050 exactly as well as one concentrated in a single
  package.

## Completion and Reliance Basis — Epistemology

- **REQ-001** — The registers shall close in both directions: every PRD item
  carries a coverage status, and every accepted scope unit traces to at least
  one PRD item. An untraced unit or an uncovered item is recorded, not omitted
  (SOW-083).
- **REQ-002** — The coverage table shall show all four categories of SOW-008,
  each with either decomposition coverage or a recorded reasoned deferral
  carrying its reason, and shall assert no partition claim (SOW-050, SOW-012).
- **REQ-003** — Every package and deliverable appearing in the registers shall
  originate in the accepted decomposition. No unit invented outside that
  pipeline may appear, and developmental machinery shall be carried as in-scope
  product rather than excluded as overhead (SOW-043, SOW-046, SOW-076).
- **REQ-004** — Unmapped objectives shall be surfaced as open issues with their
  status, and the registers shall state that completeness is claimed only for
  the stated v1 boundary (SOW-005, SOW-004).

- **AC-001** — All four categories appear in the coverage table, each with a
  coverage entry or a deferral entry whose reason is non-empty, and the table
  contains no claim that the categories determine the partition.
- **AC-002** — Forward closure holds: every row of the forward register carries
  a coverage status, and every row recording a deferral carries a deferral
  reason.
- **AC-003** — Reverse closure holds: every package and deliverable in the
  accepted decomposition register appears in the reverse register with a
  non-empty PRD-item list and trace status, and no unit appears in the reverse
  register that is absent from the accepted decomposition.
- **AC-004** — Every objective without coverage appears in the open-issues
  record; none is absent from both the coverage register and the open-issues
  record.

## Production and Verification Method — Praxeology

Production reads the accepted decomposition and its companion registers,
compiles the coverage table, and reconciles the two traceability directions.
It adds no scope unit and creates no package.

- **VER-001** — Confirm each of the four categories of SOW-008 appears in the
  `Categories` column of
  `execution/_Decomposition/chirality_root_scope_ledger_v1_0.csv` with at least
  one `IN`-status item mapped to a deliverable, or has a recorded reasoned
  deferral in the coverage table.
- **VER-002** — Confirm forward closure over
  `execution/_Decomposition/chirality_root_prd_coverage_forward_v1_0.csv`: no
  row has an empty `CoverageStatus`, and every row whose status records a
  deferral has a non-empty `DeferralReason`.
- **VER-003** — Confirm reverse closure by comparing the `UnitID` set of
  `execution/_Decomposition/chirality_root_trace_reverse_v1_0.csv` against the
  package and deliverable identifiers in
  `execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv`,
  expecting set equality with no empty `PRDItems` or `TraceStatus`.
- **VER-004** — Confirm that the objective identifiers in
  `execution/_Decomposition/chirality_root_objective_register_v1_0.csv` are
  partitioned between covered entries in the forward register and entries in
  the open-issues record, with none in neither.

Whether a recorded deferral is genuinely reasoned, rather than a gap given a
label, is a judgment about adequacy and not a set comparison. So is whether the
coverage table has crept from demonstrating coverage into justifying the
partition, which SOW-012 denies it may do. Both are routed to human review in
the matrix below rather than assigned a deterministic method.

## Governing Values and Decisions — Axiology

- **AX-001** — The decomposition pipeline is not waivable. Nothing in this
  deliverable authorizes inventing a package or deliverable from discussion;
  units enter only through an accepted decomposition (SOW-043, SOW-076).
- **AX-002** — Unmapped objectives are surfaced, never silently dropped (PRD
  §3; SOW-005), consistent with the conflict-surfacing discipline PRD §5.1 N-4
  transcribes. A register that hides a gap is worse than one that records it.
- **AX-003** — Completeness is claimed only for the stated v1 boundary. If the
  owner defines v1 differently, the success conditions re-scope accordingly and
  these registers are re-derived rather than reinterpreted (SOW-004; DEC-006).
- **AX-004** — The register records `AnticipatedWriteLocus: execution-tree`.
  That is a planning note, not authorization. This Scope of Work grants no act
  on the instruction surface — `AGENTS.md`, `agents/`, `skills/`, `tools/`,
  root `docs/`, `init/`, `.github/workflows/` — and any such act requires an
  independently authorized M2 tranche.
- **AX-005** — Every `AC-*` and `VER-*` defined here is a candidate. This
  document claims no acceptance, no approval, and no lifecycle state. The accepted decomposition states no per-deliverable acceptance criteria; nothing is inferred to fill that gap. `ResponsibleParty` is `Ryan Tufts` under D-GOV-27 and the current deliverable register
  (K-INVENT-1).

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-008 SOW-012 SOW-050 OBJ-003 | REQ-002 CLM-002 CLM-004 | AC-001 | HUMAN_REVIEW: owner judgment that each category entry is coverage or a genuinely reasoned deferral rather than a gap given a label, and that the table asserts no partition claim | Four-category coverage table with a recorded owner disposition per deferral entry |
| OUT-002 | SOW-043 SOW-046 SOW-076 SOW-083 OBJ-003 | REQ-001 REQ-003 CLM-001 CLM-003 | AC-002 AC-003 | VER-001 VER-002 VER-003 | Forward and reverse registers closing in both directions, with unit sets reconciled against the accepted decomposition and every category represented |
| OUT-003 | SOW-004 SOW-005 OBJ-003 | REQ-004 CLM-003 | AC-004 | VER-004 | Open-issues record covering every uncovered objective, with the v1-boundary qualification stated |
