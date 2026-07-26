# Context: DEL-03-03

**Name:** Dependency Register and Derived-Graph Boundary
**Package:** PKG-03 Governed Execution Structure and Root Containment
**Discipline:** TBD
**Type:** REQ_SLICE
**Responsible:** TBD

## Description

Keep deliverable-local dependency registers authoritative while allowing derived and aggregated graphs as lawful coordination state, including on-demand read-only aggregation and blocker computation.

## Acceptance Criteria

TBD — the accepted decomposition states no per-deliverable acceptance criteria.
Nothing is inferred here (K-INVENT-1).

## Anticipated Artifacts

- Dependency register conformance note
- derived-graph boundary statement

## Scope Traceability

- Scope items: SOW-033
- Objectives: OBJ-006
- ContextEnvelope: S
- ContextEnvelopeNotes: One boundary rule over an existing register format.
- AnticipatedWriteLocus: execution-tree

`AnticipatedWriteLocus` is a planning note from the accepted decomposition, not
authorization. Any locus naming the instruction surface (`AGENTS.md`, `agents/`,
`skills/`, `tools/`, root `docs/`, `init/`, `.github/workflows/`) requires an
independently authorized M2 tranche.

## Decomposition Reference

- **Decomposition file:** `execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md`
- **Companion register:** `execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv`
- **Deliverable ID:** DEL-03-03_Dependency_Register_and_Derived_Graph_Boundary
- **Package ID:** PKG-03_Governed_Execution_Structure_and_Root_Containment

## Source Authority

Scaffolded by PROJECT_SETUP at D-GOV-21 §6 step-9 materialization from the
accepted root decomposition (D-GOV-25), accepted basis
`653fabc9b3e8abf369f5e776a7d3ee24bf235e7a`. Header fields are transcribed from the accepted decomposition and
its companion deliverable register; nothing is inferred. Downstream work must
preserve `ResponsibleParty: TBD` until a human assigns ownership.
