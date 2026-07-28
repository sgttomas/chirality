# Context: DEL-02-01

**Name:** Instruction Surface Membership and Release Management
**Package:** PKG-02 Operative Instruction Surface and Runtime Layers
**Discipline:** TBD
**Type:** DOC_UPDATE
**Responsible:** Ryan Tufts

## Description

Keep the shared instruction surface membership explicit, release-managed, and read-mostly, so that changing it is a repo-wide governance action rather than ordinary working-root execution.

## Acceptance Criteria

TBD — the accepted decomposition states no per-deliverable acceptance criteria.
Nothing is inferred here (K-INVENT-1).

## Anticipated Artifacts

- Instruction-surface membership register
- M2 tranche checklist
- read-mostly conformance notes

## Scope Traceability

- Scope items: SOW-026
- Objectives: OBJ-001
- ContextEnvelope: M
- ContextEnvelopeNotes: One membership definition plus the change-path checklist.
- AnticipatedWriteLocus: instruction-surface (M2)

`AnticipatedWriteLocus` is a planning note from the accepted decomposition, not
authorization. Any locus naming the instruction surface (`AGENTS.md`, `agents/`,
`skills/`, `tools/`, root `docs/`, `init/`, `.github/workflows/`) requires an
independently authorized M2 tranche.

## Decomposition Reference

- **Decomposition file:** `execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md`
- **Companion register:** `execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv`
- **Deliverable ID:** DEL-02-01_Instruction_Surface_Membership_and_Release_Management
- **Package ID:** PKG-02_Operative_Instruction_Surface_and_Runtime_Layers

## Source Authority

Scaffolded by PROJECT_SETUP at D-GOV-21 §6 step-9 materialization from the
accepted root decomposition (D-GOV-25), accepted basis
`653fabc9b3e8abf369f5e776a7d3ee24bf235e7a`. Header fields are transcribed from the accepted decomposition and
its companion deliverable register; nothing is inferred. Downstream work must
preserve `ResponsibleParty: Ryan Tufts` as assigned by D-GOV-27 unless a later human ruling changes the accepted assignment.
