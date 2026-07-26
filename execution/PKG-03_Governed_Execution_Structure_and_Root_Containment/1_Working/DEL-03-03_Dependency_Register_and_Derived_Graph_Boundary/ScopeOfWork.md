---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-03-03
package_id: PKG-03
decomposition_basis: execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md@653fabc9b3e8abf369f5e776a7d3ee24bf235e7a
project_scope_refs: [SOW-033]
package_objective_refs: [OBJ-006]
---

# Scope of Work — DEL-03-03

## Purpose and Objective Traceability

This deliverable holds one boundary rule over an existing register format:
deliverable-local dependency registers stay authoritative, no central dependency
graph becomes authoritative, and derived or aggregated graphs remain lawful
coordination state rather than a competing source of truth.

It covers one project scope item and supports one package objective, exactly as
declared in `_CONTEXT.md` "Scope Traceability" and the companion deliverable
register:

- SOW-033 — "Deliverable-local dependency registers are authoritative and no
  central dependency graph is authoritative, while derived and aggregated graphs
  remain lawful coordination state including on-demand read-only aggregation and
  full-graph blocker computation." SourceRef: PRD §5.2 O-8 (transcribed).
- OBJ-006 — coordination remains intelligible as concurrent activity grows, so
  that declared write ownership, dependencies, and pending gates are
  reconstructible from recorded state. The boundary rule is what keeps that
  reconstruction sound: if a derived graph could be cited as authority, the
  reconstructed picture would depend on which projection someone happened to
  read.

The rule is two-sided and both sides matter equally. Treating aggregation as
forbidden would be as much a conformance failure as treating it as
authoritative: the accepted basis explicitly provides for on-demand read-only
aggregation and for blocker computation across the declared graph.

This document is a production contract, not an acceptance record. Every
definition below is a candidate grounded in the accepted decomposition, this
deliverable's `_CONTEXT.md`, the scope-ledger statement of SOW-033, and the
adopted PRD. Nothing here asserts a lifecycle state or an acceptance judgment.

## Deliverable Definition — Ontology

Two anticipated artifacts, transcribed from the register and `_CONTEXT.md`.

- **OUT-001** — Dependency register conformance note. A record of whether each
  deliverable-local dependency register conforms to the canonical register
  schema and is treated as the authoritative statement of that deliverable's
  dependencies, including the disposition of any deliverable that holds no
  register yet.
- **OUT-002** — Derived-graph boundary statement. A statement of where the
  authority line falls: which artifacts are authoritative local registers, which
  are derived or aggregated coordination state, and what a consumer may and may
  not do with each — specifically that a derived graph may inform coordination
  and compute blockers but may never be cited as the authority for a dependency.

- **CLM-001** — Authority is local and distributed. Each deliverable's own
  register is the authoritative statement of its dependencies; no assembled
  central graph holds that authority. This restates SOW-033 (PRD §5.2 O-8).
- **CLM-002** — Derived and aggregated graphs are lawful, not merely tolerated.
  On-demand read-only aggregation and full-graph blocker computation are
  provided for by the accepted basis. This restates SOW-033 (PRD §5.2 O-8).
- **CLM-003** — The distinction is one of authority, not of usefulness. A
  derived graph may be more convenient, more complete, and more current in
  presentation, and still carry no authority; convenience does not promote a
  projection into a source of truth.

## Completion and Reliance Basis — Epistemology

- **REQ-001** — Each deliverable's local dependency register shall be the
  authoritative statement of that deliverable's dependencies, and shall conform
  to the canonical register schema. Obligation restated from SOW-033, SourceRef
  PRD §5.2 O-8.
- **REQ-002** — No central or aggregated dependency graph shall be treated as
  authoritative, and no artifact shall be cited as dependency authority other
  than the local register. Obligation restated from SOW-033, SourceRef PRD §5.2
  O-8.
- **REQ-003** — Derived and aggregated graphs shall remain available as lawful
  coordination state, including on-demand read-only aggregation and blocker
  computation across the declared graph. Obligation restated from SOW-033,
  SourceRef PRD §5.2 O-8.

- **AC-001** — OUT-001 accounts for every deliverable in the execution instance,
  recording for each either a schema-conforming local register or an explicit
  disposition for its absence, with no deliverable silently omitted.
- **AC-002** — OUT-002 names, for each dependency-bearing artifact class in use,
  whether it is authoritative or derived, and states the permitted use of each
  class in terms a consumer can apply without further interpretation.
- **AC-003** — OUT-002 demonstrates the permitted-but-non-authoritative case
  concretely: an aggregation performed read-only, producing coordination output,
  with the authority of the underlying local registers unchanged.

Reliance basis: OUT-001 rests on deterministic schema validation per register,
plus human review for instance-wide coverage, since the schema checker validates
one file at a time and cannot itself establish that every deliverable was
considered. OUT-002 rests on human review; see CON-001. No artifact here carries
acceptance until a human accepts it.

## Production and Verification Method — Praxeology

Production is: enumerate the deliverables, validate each local register that
exists, disposition each that does not, perform a read-only aggregation to
exercise the lawful-derivation half of the rule, and write the boundary
statement in terms a consumer can act on.

- **VER-001** — For each deliverable-local register, execute
  `python3 tools/validation/validate_dependencies_schema.py <Dependencies.csv>`
  and record the result and exit status. This is the deterministic signal for
  the schema half of REQ-001.
- **VER-002** — Execute
  `python3 tools/coordination/analyze_dep_closure.py <EXECUTION_ROOT>` with no
  output directory argument, and record its summary. Invoked this way the tool
  reads the declared registers and emits an aggregate summary without writing,
  which is the concrete demonstration required by REQ-003 and AC-003: the
  aggregation happens, it is useful, and it changes nothing about where
  authority sits.

Note on current state: at the accepted basis this execution instance holds no
populated deliverable-local registers, so VER-001 has no subject yet and VER-002
summarizes an empty graph. Both remain the correct methods; the conformance
claim they support becomes meaningful as registers are populated, and OUT-001
must disposition the empty case rather than report it as conformance.

- **CON-001** — Verification gap. No deterministic check was found that
  enforces the authority boundary itself — that is, nothing mechanically detects
  a derived or aggregated graph being cited as dependency authority. The schema
  checker validates register shape, and the closure tool aggregates; neither
  tests the boundary rule. OUT-002 therefore verifies by human review, and the
  boundary remains a discipline enforced by review rather than by tooling. This
  is recorded, not resolved here.

## Governing Values and Decisions — Axiology

- **AX-001** — Grounding discipline. Every definition above traces to this
  deliverable's register row, its `_CONTEXT.md`, the scope-ledger statement of
  SOW-033, or the adopted PRD. Nothing is inferred, and unknowns stay marked.
- **AX-002** — Write-locus boundary. The register records this deliverable's
  `AnticipatedWriteLocus` as the execution tree only. Nothing in this document
  authorizes a change to the instruction surface; any such act, including
  building tooling to close CON-001, requires an independently authorized M2
  tranche, which this document does not grant.
- **AX-003** — Lifecycle neutrality. This contract asserts no lifecycle state
  and no acceptance. Lifecycle authority remains each deliverable's `_STATUS.md`,
  and acceptance remains a human judgment.
- **AX-004** — Locality of truth is a durability property. Distributed local
  registers survive the loss of any assembled projection, whereas a central
  graph promoted to authority would make every deliverable's truth depend on one
  artifact staying correct and current.
- **AX-005** — An empty result is a finding, not a pass. Where no register
  exists to validate, the conformance note records the absence and its
  disposition rather than reporting a clean run.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-033 OBJ-006 | REQ-001 CLM-001 | AC-001 | VER-001 | Per-deliverable record of command, result, and exit status for each register present, plus an explicit disposition for each deliverable holding none, and an enumeration showing instance-wide coverage |
| OUT-002 | SOW-033 OBJ-006 | REQ-002 REQ-003 CLM-002 CLM-003 | AC-002 AC-003 | VER-002 | Artifact-class table marking each class authoritative or derived with its permitted use, plus the recorded read-only aggregation run and its summary, showing coordination output produced without any authority shift |
