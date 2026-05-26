# Guidance: DEL-101-04 — EPC / Structural Discipline Production Package

## Purpose

DEL-101-04 exists to carry the **non-vendor, discipline-led** production work for PKG-101 (Precast concrete foundations) conservatively from the workbook and DBM context, so that integrator anchor deliverables (DEL-101-01 Scope of Work, DEL-101-02 Package Datasheet, DEL-101-03 Construction Work Package) remain integrator-authored while a parallel discipline production unit captures, records, and closes source-limited gaps for Gate 5 disposition. (Source: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row DEL-101-04; `ARTIFACT_REGISTER.csv` ART-D61EA18810 and ART-5FB1815B54.)

The deliverable supports OBJ-001 (Deepcut facility scope) and OBJ-008 (civil/structural/site/construction support) through the package-grouping heuristic; this association is recorded as **ASSUMPTION (best-effort mapping)**. (Source: `_CONTEXT.md`; `PACKAGE_REGISTER.csv` SupportsObjectives; `OBJECTIVE_REGISTER.csv` rows OBJ-001, OBJ-008.)

## Principles

- **Source fidelity over convention.** Structural production content MUST be grounded in workbook row 102 and any locally accessible source slices. Where source content is absent, mark TBD; do not import generic structural-engineering convention as if it were source. (Principle derived from authority hierarchy.)
- **Conservative carry.** The package scope is carried conservatively from workbook and DBM support; no vendor-package ownership model is inferred. (Source: `PACKAGE_REGISTER.csv` ResponsibilityModel.)
- **Interface preservation.** Declared physical interfaces (Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports) MUST be preserved as facts in production content. (Source: `INTERFACE_REGISTER.csv` PKG-101.)
- **Gap visibility.** Source-limited requirements MUST be surfaced in the closure record rather than silently resolved; Gate 5 disposition is the intended ruling point. (Source: `DELIVERABLE_REGISTER.csv` Notes.)
- **No agent certification.** Responsibility assignment and acceptance of source-limited closure positions are human decisions. (Governance principle K-AUTH-1.)

## Considerations

- **Responsibility ambiguity.** ResponsibleParty is "TBD; EPC Integrator or discipline subcontractor as assigned" — production cannot complete until the human responsibility assignment is recorded. (Source: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv`.)
- **Source set is thin.** Of the references listed in `_REFERENCES.md`, only the decomposition registers are slice-extracted for this deliverable; the workbook (`26020-Packages_Interfaces_4_export.xlsx`), package requirements document (`26020-Package_Requirements.docx`), and DBM markdown files have not been opened as deliverable-local source slices during this run. (Source: `_REFERENCES.md` Missing/Deferred References.)
- **Sibling boundary.** Care is required not to duplicate scope of work, datasheet content, or construction work package content that legitimately belongs to DEL-101-01..03. (Source: `DELIVERABLE_REGISTER.csv` rows for the sibling deliverables.)
- **Interface ownership.** Both PKG-101 interfaces are flagged YES in `INTERFACE_REGISTER.csv`; the production package must coordinate with the adjacent grading/site-drainage and structural support work, even though those interfaces are recorded primarily as datasheet evidence under DEL-101-02. (Source: `INTERFACE_REGISTER.csv`; `ARTIFACT_REGISTER.csv` ART-B722B4EE97, ART-1D7D43BEDB.)

## Trade-offs

- **Carrying source-limited scope conservatively vs. waiting for full sources.** The chosen direction is to produce a conservative production-package basis and an explicit closure record now, accepting that detailed design values remain TBD until Gate 5. The alternative (defer all production-unit work until full source extraction) was not adopted by the decomposition. (Source: `_CONTEXT.md` Notes; `DELIVERABLE_REGISTER.csv` Notes.)
- **Single discipline production unit per package vs. multiple discipline subdeliverables.** The decomposition uses a single discipline production unit per package; finer subdivision is TBD and would be introduced through the discipline deliverable register if warranted. (Source: `_CONTEXT.md` Anticipated Artifacts: "TBD discipline deliverable register".)

## Examples

TBD — no concrete worked examples are present in the locally accessible source slices for this deliverable.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONF-101-04-01 | Responsibility model: `_CONTEXT.md` and `DELIVERABLE_REGISTER.csv` say "TBD; EPC Integrator or discipline subcontractor as assigned"; `PACKAGE_REGISTER.csv` ResponsibilityModel states "EPC Integrator or discipline subcontractor responsibility is source-dependent; no separate vendor-package ownership model is inferred." | `_CONTEXT.md` Identity (ResponsibleParty) | `PACKAGE_REGISTER.csv` PKG-101 ResponsibilityModel | Datasheet Identification; Specification R-101-04-06, R-101-04-08; Procedure Prerequisites | PROPOSAL: treat the package-register text as authoritative framing (source-dependent, no vendor-ownership inference) and resolve the deliverable-level ResponsibleParty as a human assignment recorded before production starts. | TBD |
| CONF-101-04-02 | Standards basis: Specification lists `26020-Package_Requirements.docx` and DBM SEC-11 as ASSUMPTION-likely applicable, but no slice has been extracted; the closure record is meant to enumerate source-limited gaps, which would be premature without confirming whether these documents contain PKG-101 structural requirements. | `_REFERENCES.md` Shared Source Root (file presence) | `_REFERENCES.md` Missing/Deferred References (no slices extracted) | Specification Standards; closure record content | PROPOSAL: open `26020-Package_Requirements.docx` and DBM SEC-11 as deliverable-local source slices during the next pass, before authoring the closure record. | TBD |
| CONF-101-04-03 | Objective association is ASSUMPTION via package-grouping heuristic; OBJECTIVE_DELIVERABLE_MAP rows for PKG-101 were not located in the slice extracted (only earlier packages appear in the head). | `_CONTEXT.md` Supports Objectives (OBJ-001, OBJ-008) | `OBJECTIVE_DELIVERABLE_MAP.csv` (PKG-101 rows not confirmed in extracted slice) | Datasheet Identification (Supports Objectives) | PROPOSAL: confirm OBJ→DEL-101-04 rows in `OBJECTIVE_DELIVERABLE_MAP.csv` and demote ASSUMPTION to FACT if present; otherwise retain ASSUMPTION label. | TBD |
