# Context: DEL-04-03

**Name:** Validation Severity and Override Controls
**Package:** PKG-04 Developmental Machinery and Change Control
**Discipline:** TBD
**Type:** CI_CD_CHANGE
**Responsible:** Ryan Tufts

## Description

Keep validation deterministic and severity-typed with exit-code semantics and human-only recorded BLOCK override, keep BLOCK bounded to its declared observation boundary, and keep validator findings from mechanically rejecting owner-ruled content.

## Acceptance Criteria

TBD — the accepted decomposition states no per-deliverable acceptance criteria.
Nothing is inferred here (K-INVENT-1).

## Anticipated Artifacts

- Severity conformance report
- override-record format
- defective-validator escalation path

## Scope Traceability

- Scope items: SOW-039
- Objectives: OBJ-003
- ContextEnvelope: M
- ContextEnvelopeNotes: One severity model across the validator set.
- AnticipatedWriteLocus: tools/ (M2); execution-tree for evidence

`AnticipatedWriteLocus` is a planning note from the accepted decomposition, not
authorization. Any locus naming the instruction surface (`AGENTS.md`, `agents/`,
`skills/`, `tools/`, root `docs/`, `init/`, `.github/workflows/`) requires an
independently authorized M2 tranche.

## Decomposition Reference

- **Decomposition file:** `execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md`
- **Companion register:** `execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv`
- **Deliverable ID:** DEL-04-03_Validation_Severity_and_Override_Controls
- **Package ID:** PKG-04_Developmental_Machinery_and_Change_Control

## Source Authority

Scaffolded by PROJECT_SETUP at D-GOV-21 §6 step-9 materialization from the
accepted root decomposition (D-GOV-25), accepted basis
`653fabc9b3e8abf369f5e776a7d3ee24bf235e7a`. Header fields are transcribed from the accepted decomposition and
its companion deliverable register; nothing is inferred. Downstream work must
preserve `ResponsibleParty: Ryan Tufts` as assigned by D-GOV-27 unless a later human ruling changes the accepted assignment.
