# Context: DEL-05-06

**Name:** Validation Evidence Mutation Control
**Package:** PKG-05 Evidence, Provenance, and Audit
**Discipline:** TBD
**Type:** SECURITY_CONTROL
**Responsible:** Ryan Tufts

## Description

Keep validation evidence written only under declared generated paths under the mutation-control contract, keep the harness from writing governed authority files, and keep governed-file mutation by a validation command an unconditional BLOCK.

## Acceptance Criteria

TBD — the accepted decomposition states no per-deliverable acceptance criteria.
Nothing is inferred here (K-INVENT-1).

## Anticipated Artifacts

- Mutation-control conformance evidence
- generated-path containment tests

## Scope Traceability

- Scope items: SOW-057
- Objectives: OBJ-004
- ContextEnvelope: M
- ContextEnvelopeNotes: One control with existing fail-closed machinery.
- AnticipatedWriteLocus: tools/ (M2); execution-tree for evidence

`AnticipatedWriteLocus` is a planning note from the accepted decomposition, not
authorization. Any locus naming the instruction surface (`AGENTS.md`, `agents/`,
`skills/`, `tools/`, root `docs/`, `init/`, `.github/workflows/`) requires an
independently authorized M2 tranche.

## Decomposition Reference

- **Decomposition file:** `execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md`
- **Companion register:** `execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv`
- **Deliverable ID:** DEL-05-06_Validation_Evidence_Mutation_Control
- **Package ID:** PKG-05_Evidence_Provenance_and_Audit

## Source Authority

Scaffolded by PROJECT_SETUP at D-GOV-21 §6 step-9 materialization from the
accepted root decomposition (D-GOV-25), accepted basis
`653fabc9b3e8abf369f5e776a7d3ee24bf235e7a`. Header fields are transcribed from the accepted decomposition and
its companion deliverable register; nothing is inferred. Downstream work must
preserve `ResponsibleParty: TBD` until a human assigns ownership.
