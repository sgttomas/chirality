# Context: DEL-03-01

**Name:** Path Model and ScopePath Containment Conformance
**Package:** PKG-03 Governed Execution Structure and Root Containment
**Discipline:** TBD
**Type:** SECURITY_CONTROL
**Responsible:** Ryan Tufts

## Description

Keep the two-root path model, the containment rule, and the closed token registry enforced, with every scope path and write target resolving under the active checkout or the task stopping, and no machine-absolute paths in instruction, coordination, or plan files.

## Acceptance Criteria

TBD — the accepted decomposition states no per-deliverable acceptance criteria.
Nothing is inferred here (K-INVENT-1).

## Anticipated Artifacts

- Path-anchor validation runs
- containment test evidence
- token-registry conformance note

## Scope Traceability

- Scope items: SOW-020, SOW-031
- Objectives: OBJ-004, OBJ-007
- ContextEnvelope: M
- ContextEnvelopeNotes: One rule set with existing deterministic checks to extend and evidence.
- AnticipatedWriteLocus: execution-tree; tools/ (M2) if a check must change

`AnticipatedWriteLocus` is a planning note from the accepted decomposition, not
authorization. Any locus naming the instruction surface (`AGENTS.md`, `agents/`,
`skills/`, `tools/`, root `docs/`, `init/`, `.github/workflows/`) requires an
independently authorized M2 tranche.

## Decomposition Reference

- **Decomposition file:** `execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md`
- **Companion register:** `execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv`
- **Deliverable ID:** DEL-03-01_Path_Model_and_ScopePath_Containment_Conformance
- **Package ID:** PKG-03_Governed_Execution_Structure_and_Root_Containment

## Source Authority

Scaffolded by PROJECT_SETUP at D-GOV-21 §6 step-9 materialization from the
accepted root decomposition (D-GOV-25), accepted basis
`653fabc9b3e8abf369f5e776a7d3ee24bf235e7a`. Header fields are transcribed from the accepted decomposition and
its companion deliverable register; nothing is inferred. Downstream work must
preserve `ResponsibleParty: TBD` until a human assigns ownership.
