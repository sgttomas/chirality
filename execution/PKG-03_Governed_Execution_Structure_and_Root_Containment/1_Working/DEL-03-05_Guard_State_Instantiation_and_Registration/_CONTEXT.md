# Context: DEL-03-05

**Name:** Guard State Instantiation and Registration
**Package:** PKG-03 Governed Execution Structure and Root Containment
**Discipline:** TBD
**Type:** DATA_MODEL_CHANGE
**Responsible:** Ryan Tufts

## Description

Instantiate and maintain the root guard state surfaces the G0-G4 guards read - guard registration, harness adapter, surface-ownership register, and the accepted work graph - so that every materialization runs with guards registered and passing.

## Acceptance Criteria

TBD — the accepted decomposition states no per-deliverable acceptance criteria.
Nothing is inferred here (K-INVENT-1).

## Anticipated Artifacts

- execution/_harness/root_guards.yaml
- execution/_harness/adapter.yaml
- execution/_harness/surface_ownership.yaml
- execution/_harness/work_graph.yaml

## Scope Traceability

- Scope items: SOW-001, SOW-034
- Objectives: OBJ-004
- ContextEnvelope: M
- ContextEnvelopeNotes: Four schema-bound state files with existing validators and tests; no validator change implied.
- AnticipatedWriteLocus: execution/_harness (root Project Setup; authorized separately)

`AnticipatedWriteLocus` is a planning note from the accepted decomposition, not
authorization. Any locus naming the instruction surface (`AGENTS.md`, `agents/`,
`skills/`, `tools/`, root `docs/`, `init/`, `.github/workflows/`) requires an
independently authorized M2 tranche.

## Decomposition Reference

- **Decomposition file:** `execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md`
- **Companion register:** `execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv`
- **Deliverable ID:** DEL-03-05_Guard_State_Instantiation_and_Registration
- **Package ID:** PKG-03_Governed_Execution_Structure_and_Root_Containment

## Source Authority

Scaffolded by PROJECT_SETUP at D-GOV-21 §6 step-9 materialization from the
accepted root decomposition (D-GOV-25), accepted basis
`653fabc9b3e8abf369f5e776a7d3ee24bf235e7a`. Header fields are transcribed from the accepted decomposition and
its companion deliverable register; nothing is inferred. Downstream work must
preserve `ResponsibleParty: Ryan Tufts` as assigned by D-GOV-27 unless a later human ruling changes the accepted assignment.
