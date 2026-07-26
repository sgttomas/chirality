# Context: DEL-04-02

**Name:** Identity Attribution and Refusal Controls
**Package:** PKG-04 Developmental Machinery and Change Control
**Discipline:** TBD
**Type:** SECURITY_CONTROL
**Responsible:** Ryan Tufts

## Description

Keep attribution of rulings and adoptions matched against the owner-curated identity allowlist, with identity-dependent checks refusing rather than guessing and the list never extended programmatically.

## Acceptance Criteria

TBD — the accepted decomposition states no per-deliverable acceptance criteria.
Nothing is inferred here (K-INVENT-1).

## Anticipated Artifacts

- Identity-match check evidence
- refusal-path tests
- curation-path note

## Scope Traceability

- Scope items: SOW-038, SOW-093
- Objectives: OBJ-002
- ContextEnvelope: S
- ContextEnvelopeNotes: One check with a small allowlist surface.
- AnticipatedWriteLocus: execution-tree; tools/ (M2) if a check must change

`AnticipatedWriteLocus` is a planning note from the accepted decomposition, not
authorization. Any locus naming the instruction surface (`AGENTS.md`, `agents/`,
`skills/`, `tools/`, root `docs/`, `init/`, `.github/workflows/`) requires an
independently authorized M2 tranche.

## Decomposition Reference

- **Decomposition file:** `execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md`
- **Companion register:** `execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv`
- **Deliverable ID:** DEL-04-02_Identity_Attribution_and_Refusal_Controls
- **Package ID:** PKG-04_Developmental_Machinery_and_Change_Control

## Source Authority

Scaffolded by PROJECT_SETUP at D-GOV-21 §6 step-9 materialization from the
accepted root decomposition (D-GOV-25), accepted basis
`653fabc9b3e8abf369f5e776a7d3ee24bf235e7a`. Header fields are transcribed from the accepted decomposition and
its companion deliverable register; nothing is inferred. Downstream work must
preserve `ResponsibleParty: TBD` until a human assigns ownership.
