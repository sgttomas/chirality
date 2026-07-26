# Context: DEL-05-01

**Name:** Run Record Tree Conformance
**Package:** PKG-05 Evidence, Provenance, and Audit
**Discipline:** TBD
**Type:** REQ_SLICE
**Responsible:** TBD

## Description

Keep every orchestration run persisting a durable, versioned record tree capturing plan, work graph, briefs, returns, notices, dispositions, amendments, and final handoff state, with run IDs created only when a real run begins and no placeholder runs presented as executed children.

## Acceptance Criteria

TBD — the accepted decomposition states no per-deliverable acceptance criteria.
Nothing is inferred here (K-INVENT-1).

## Anticipated Artifacts

- Run-record structure checklist
- placeholder-run prohibition check
- handoff-state conformance notes

## Scope Traceability

- Scope items: SOW-052
- Objectives: OBJ-006
- ContextEnvelope: M
- ContextEnvelopeNotes: One record shape over an existing directory convention.
- AnticipatedWriteLocus: execution-tree

`AnticipatedWriteLocus` is a planning note from the accepted decomposition, not
authorization. Any locus naming the instruction surface (`AGENTS.md`, `agents/`,
`skills/`, `tools/`, root `docs/`, `init/`, `.github/workflows/`) requires an
independently authorized M2 tranche.

## Decomposition Reference

- **Decomposition file:** `execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md`
- **Companion register:** `execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv`
- **Deliverable ID:** DEL-05-01_Run_Record_Tree_Conformance
- **Package ID:** PKG-05_Evidence_Provenance_and_Audit

## Source Authority

Scaffolded by PROJECT_SETUP at D-GOV-21 §6 step-9 materialization from the
accepted root decomposition (D-GOV-25), accepted basis
`653fabc9b3e8abf369f5e776a7d3ee24bf235e7a`. Header fields are transcribed from the accepted decomposition and
its companion deliverable register; nothing is inferred. Downstream work must
preserve `ResponsibleParty: TBD` until a human assigns ownership.
