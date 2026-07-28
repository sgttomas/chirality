# Context: DEL-06-01

**Name:** Self-Application Discipline and Falsifier Observation
**Package:** PKG-06 Self-Application, Variants, and Release
**Discipline:** TBD
**Type:** REQ_SLICE
**Responsible:** Ryan Tufts

## Description

Keep root self-application disciplined - no root node consuming a capability produced by root development before that capability was accepted - and keep the containment falsifiers observable so a containment failure, loop bypass, or self-authorization would be detected rather than inferred.

## Acceptance Criteria

TBD — the accepted decomposition states no per-deliverable acceptance criteria.
Nothing is inferred here (K-INVENT-1).

## Anticipated Artifacts

- Self-application discipline checklist
- falsifier observation record
- consumed-capability provenance list

## Scope Traceability

- Scope items: SOW-060, SOW-062, SOW-080, SOW-081, SOW-082
- Objectives: OBJ-004
- ContextEnvelope: M
- ContextEnvelopeNotes: One discipline rule plus three enumerated falsifiers.
- AnticipatedWriteLocus: execution-tree

`AnticipatedWriteLocus` is a planning note from the accepted decomposition, not
authorization. Any locus naming the instruction surface (`AGENTS.md`, `agents/`,
`skills/`, `tools/`, root `docs/`, `init/`, `.github/workflows/`) requires an
independently authorized M2 tranche.

## Decomposition Reference

- **Decomposition file:** `execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md`
- **Companion register:** `execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv`
- **Deliverable ID:** DEL-06-01_Self_Application_Discipline_and_Falsifier_Observation
- **Package ID:** PKG-06_Self_Application_Variants_and_Release

## Source Authority

Scaffolded by PROJECT_SETUP at D-GOV-21 §6 step-9 materialization from the
accepted root decomposition (D-GOV-25), accepted basis
`653fabc9b3e8abf369f5e776a7d3ee24bf235e7a`. Header fields are transcribed from the accepted decomposition and
its companion deliverable register; nothing is inferred. Downstream work must
preserve `ResponsibleParty: Ryan Tufts` as assigned by D-GOV-27 unless a later human ruling changes the accepted assignment.
