# Context: DEL-04-07

**Name:** Public Export Boundary Conformance
**Package:** PKG-04 Developmental Machinery and Change Control
**Discipline:** TBD
**Type:** SECURITY_CONTROL
**Responsible:** Ryan Tufts

## Description

Keep the public-export boundary an explicit allowlist profile that copies allowlisted content, sanitizes private absolute paths, writes a manifest and report, and fails on forbidden paths or leaks - and keep the boundary itself unchanged absent a governed act.

## Acceptance Criteria

TBD — the accepted decomposition states no per-deliverable acceptance criteria.
Nothing is inferred here (K-INVENT-1).

## Anticipated Artifacts

- Export run manifest/report
- boundary conformance note
- leak-check evidence

## Scope Traceability

- Scope items: SOW-044, SOW-074
- Objectives: OBJ-001
- ContextEnvelope: S
- ContextEnvelopeNotes: One profile with existing failure modes.
- AnticipatedWriteLocus: execution-tree; exports/ (M2) if the profile must change

`AnticipatedWriteLocus` is a planning note from the accepted decomposition, not
authorization. Any locus naming the instruction surface (`AGENTS.md`, `agents/`,
`skills/`, `tools/`, root `docs/`, `init/`, `.github/workflows/`) requires an
independently authorized M2 tranche.

## Decomposition Reference

- **Decomposition file:** `execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md`
- **Companion register:** `execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv`
- **Deliverable ID:** DEL-04-07_Public_Export_Boundary_Conformance
- **Package ID:** PKG-04_Developmental_Machinery_and_Change_Control

## Source Authority

Scaffolded by PROJECT_SETUP at D-GOV-21 §6 step-9 materialization from the
accepted root decomposition (D-GOV-25), accepted basis
`653fabc9b3e8abf369f5e776a7d3ee24bf235e7a`. Header fields are transcribed from the accepted decomposition and
its companion deliverable register; nothing is inferred. Downstream work must
preserve `ResponsibleParty: TBD` until a human assigns ownership.
