# Context: DEL-02-04

**Name:** Declared Write Scope and Capability-Boundary Controls
**Package:** PKG-02 Operative Instruction Surface and Runtime Layers
**Discipline:** TBD
**Type:** SECURITY_CONTROL
**Responsible:** Ryan Tufts

## Description

Keep every agent's declared write scope explicit and keep capability from conferring authority: sealed context, gate approval, path containment, enforced read/write scope, and durable evidence on every child.

## Acceptance Criteria

TBD — the accepted decomposition states no per-deliverable acceptance criteria.
Nothing is inferred here (K-INVENT-1).

## Anticipated Artifacts

- Write-scope declaration audit
- sealed-brief conformance checks
- capability-boundary control notes

## Scope Traceability

- Scope items: SOW-019, SOW-029
- Objectives: OBJ-004
- ContextEnvelope: M
- ContextEnvelopeNotes: Control-shaped work over the agent surface; enforcement points already exist.
- AnticipatedWriteLocus: instruction-surface (M2); execution-tree for audit evidence

`AnticipatedWriteLocus` is a planning note from the accepted decomposition, not
authorization. Any locus naming the instruction surface (`AGENTS.md`, `agents/`,
`skills/`, `tools/`, root `docs/`, `init/`, `.github/workflows/`) requires an
independently authorized M2 tranche.

## Decomposition Reference

- **Decomposition file:** `execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md`
- **Companion register:** `execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv`
- **Deliverable ID:** DEL-02-04_Declared_Write_Scope_and_Capability_Boundary_Controls
- **Package ID:** PKG-02_Operative_Instruction_Surface_and_Runtime_Layers

## Source Authority

Scaffolded by PROJECT_SETUP at D-GOV-21 §6 step-9 materialization from the
accepted root decomposition (D-GOV-25), accepted basis
`653fabc9b3e8abf369f5e776a7d3ee24bf235e7a`. Header fields are transcribed from the accepted decomposition and
its companion deliverable register; nothing is inferred. Downstream work must
preserve `ResponsibleParty: Ryan Tufts` as assigned by D-GOV-27 unless a later human ruling changes the accepted assignment.
