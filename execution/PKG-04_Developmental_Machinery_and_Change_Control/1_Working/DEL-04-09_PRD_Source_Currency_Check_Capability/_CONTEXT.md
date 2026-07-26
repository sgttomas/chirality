# Context: DEL-04-09

**Name:** PRD Source-Currency Check Capability
**Package:** PKG-04 Developmental Machinery and Change Control
**Discipline:** TBD
**Type:** TEST_SUITE
**Responsible:** Ryan Tufts

## Description

Build the standing source-currency check over the nine declared classes, with the five mechanical classes automated and the four semantic classes routed as REVIEW findings to the owner, together with the regenerable concordance annex it runs against.

## Acceptance Criteria

TBD — the accepted decomposition states no per-deliverable acceptance criteria.
Nothing is inferred here (K-INVENT-1).

## Anticipated Artifacts

- Currency check tool
- annex generator/schema
- check report format
- REVIEW routing note

## Scope Traceability

- Scope items: SOW-048, SOW-049, SOW-097
- Objectives: OBJ-001
- ContextEnvelope: L
- ContextEnvelopeNotes: Large but single-domain: one checker plus one regenerable derivative package; five mechanical classes are automatable while four require semantic judgment, so the deliverable may be split by class if implementation review finds churn.
- AnticipatedWriteLocus: tools/ (M2); execution-tree for the annex and reports

`AnticipatedWriteLocus` is a planning note from the accepted decomposition, not
authorization. Any locus naming the instruction surface (`AGENTS.md`, `agents/`,
`skills/`, `tools/`, root `docs/`, `init/`, `.github/workflows/`) requires an
independently authorized M2 tranche.

## Decomposition Reference

- **Decomposition file:** `execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md`
- **Companion register:** `execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv`
- **Deliverable ID:** DEL-04-09_PRD_Source_Currency_Check_Capability
- **Package ID:** PKG-04_Developmental_Machinery_and_Change_Control

## Source Authority

Scaffolded by PROJECT_SETUP at D-GOV-21 §6 step-9 materialization from the
accepted root decomposition (D-GOV-25), accepted basis
`653fabc9b3e8abf369f5e776a7d3ee24bf235e7a`. Header fields are transcribed from the accepted decomposition and
its companion deliverable register; nothing is inferred. Downstream work must
preserve `ResponsibleParty: TBD` until a human assigns ownership.
