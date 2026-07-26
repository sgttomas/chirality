# Context: DEL-04-08

**Name:** PRD Amendment and Attributable Change Control
**Package:** PKG-04 Developmental Machinery and Change Control
**Discipline:** TBD
**Type:** REQ_SLICE
**Responsible:** Ryan Tufts

## Description

Keep the adopted PRD amendable only by a superseding instrument bound to a git SHA, keep every change to approved content a new attributable act with prior bytes recoverable, keep declared-immutable classes never overwritten while living surfaces amend in place, and keep provenance labels from decaying.

## Acceptance Criteria

TBD — the accepted decomposition states no per-deliverable acceptance criteria.
Nothing is inferred here (K-INVENT-1).

## Anticipated Artifacts

- Amendment procedure note
- immutable-class register
- label-integrity check
- placement pointer maintenance

## Scope Traceability

- Scope items: SOW-047, SOW-051, SOW-085, SOW-096, SOW-102
- Objectives: OBJ-003
- ContextEnvelope: M
- ContextEnvelopeNotes: One change-control regime with an enumerated immutable-class list.
- AnticipatedWriteLocus: execution-tree; instruction-surface (M2) for any PRD amendment

`AnticipatedWriteLocus` is a planning note from the accepted decomposition, not
authorization. Any locus naming the instruction surface (`AGENTS.md`, `agents/`,
`skills/`, `tools/`, root `docs/`, `init/`, `.github/workflows/`) requires an
independently authorized M2 tranche.

## Decomposition Reference

- **Decomposition file:** `execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md`
- **Companion register:** `execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv`
- **Deliverable ID:** DEL-04-08_PRD_Amendment_and_Attributable_Change_Control
- **Package ID:** PKG-04_Developmental_Machinery_and_Change_Control

## Source Authority

Scaffolded by PROJECT_SETUP at D-GOV-21 §6 step-9 materialization from the
accepted root decomposition (D-GOV-25), accepted basis
`653fabc9b3e8abf369f5e776a7d3ee24bf235e7a`. Header fields are transcribed from the accepted decomposition and
its companion deliverable register; nothing is inferred. Downstream work must
preserve `ResponsibleParty: TBD` until a human assigns ownership.
