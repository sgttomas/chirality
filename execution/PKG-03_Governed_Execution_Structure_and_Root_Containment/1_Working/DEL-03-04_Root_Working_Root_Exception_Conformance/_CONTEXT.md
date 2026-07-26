# Context: DEL-03-04

**Name:** Root Working-Root Exception Conformance
**Package:** PKG-03 Governed Execution Structure and Root Containment
**Discipline:** TBD
**Type:** REQ_SLICE
**Responsible:** Ryan Tufts

## Description

Keep the single governed exception exact: the root product's working root is the repository root and root execution/ is its execution root, eligible for packages and deliverables only from an accepted root decomposition derived from an adopted PRD and only while the guards pass, with the containment mechanisms incorporated by reference and containment never mistaken for authorization.

## Acceptance Criteria

TBD — the accepted decomposition states no per-deliverable acceptance criteria.
Nothing is inferred here (K-INVENT-1).

## Anticipated Artifacts

- Exception conformance statement
- mechanism/guard reference map
- containment-is-not-authorization note

## Scope Traceability

- Scope items: SOW-034, SOW-063
- Objectives: OBJ-004
- ContextEnvelope: M
- ContextEnvelopeNotes: One exception with an enumerated mechanism set.
- AnticipatedWriteLocus: execution-tree

`AnticipatedWriteLocus` is a planning note from the accepted decomposition, not
authorization. Any locus naming the instruction surface (`AGENTS.md`, `agents/`,
`skills/`, `tools/`, root `docs/`, `init/`, `.github/workflows/`) requires an
independently authorized M2 tranche.

## Decomposition Reference

- **Decomposition file:** `execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md`
- **Companion register:** `execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv`
- **Deliverable ID:** DEL-03-04_Root_Working_Root_Exception_Conformance
- **Package ID:** PKG-03_Governed_Execution_Structure_and_Root_Containment

## Source Authority

Scaffolded by PROJECT_SETUP at D-GOV-21 §6 step-9 materialization from the
accepted root decomposition (D-GOV-25), accepted basis
`653fabc9b3e8abf369f5e776a7d3ee24bf235e7a`. Header fields are transcribed from the accepted decomposition and
its companion deliverable register; nothing is inferred. Downstream work must
preserve `ResponsibleParty: TBD` until a human assigns ownership.
