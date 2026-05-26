# Guidance: DEL-104-04 — EPC / Structural Discipline Production Package

## Purpose

DEL-104-04 exists to carry the **non-vendor, discipline-led** production work for PKG-104 (Structural steel - outside of modules) conservatively from the workbook and DBM context, so that integrator anchor deliverables (DEL-104-01 Scope of Work, DEL-104-02 Package Datasheet, DEL-104-03 Construction Work Package) remain integrator-authored while a parallel discipline production unit captures, records, and closes source-limited gaps for Gate 5 disposition. (Source: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row DEL-104-04; `ARTIFACT_REGISTER.csv` rows ART-26DA5854ED and ART-E815C1D6F1.)

The deliverable supports OBJ-001 (Deepcut facility scope) and OBJ-008 (civil/structural/site/construction support). These associations are FACT, confirmed by explicit DEL-104-04 rows in `OBJECTIVE_DELIVERABLE_MAP.csv`. (Source: `OBJECTIVE_DELIVERABLE_MAP.csv` rows for DEL-104-04; `_CONTEXT.md`; `PACKAGE_REGISTER.csv` SupportsObjectives.)

## Principles

- **Source fidelity over convention.** Structural production content MUST be grounded in workbook row 105, `DBM-Deepcut/4-25_Deepcut_DBM.md`, and any locally accessible source slices. Where source content is absent, mark TBD; do not import generic structural-steel-engineering convention (AISC, fabrication standards, erection practice) as if it were source. (Principle derived from authority hierarchy.)
- **Conservative carry.** The package scope is carried conservatively from workbook and DBM support; no vendor-package ownership model is inferred. (Source: `PACKAGE_REGISTER.csv` ResponsibilityModel.)
- **Interface preservation.** Declared physical interfaces (Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports) MUST be preserved as facts in production content. (Source: `INTERFACE_REGISTER.csv` PKG-104.)
- **Gap visibility.** Source-limited requirements MUST be surfaced in the closure record rather than silently resolved; Gate 5 disposition is the intended ruling point. (Source: `DELIVERABLE_REGISTER.csv` Notes.)
- **No agent certification.** Responsibility assignment and acceptance of source-limited closure positions are human decisions. (Governance principle K-AUTH-1.)

## Considerations

- **Responsibility ambiguity.** ResponsibleParty is "TBD; EPC Integrator or discipline subcontractor as assigned" — production cannot complete until the human responsibility assignment is recorded. (Source: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv`.)
- **Source set is thin.** Of the references listed in `_REFERENCES.md`, only the decomposition registers are slice-extracted for this deliverable; the workbook (`26020-Packages_Interfaces_4_export.xlsx`), package requirements document (`26020-Package_Requirements.docx`), and DBM markdown files (including `DBM-Deepcut/4-25_Deepcut_DBM.md` directly cited as SourceBasis) have not been opened as deliverable-local source slices during this run. (Source: `_REFERENCES.md` Missing/Deferred References; `PACKAGE_REGISTER.csv` SourceBasis.)
- **Sibling boundary.** Care is required not to duplicate scope of work, datasheet content, or construction work package content that legitimately belongs to DEL-104-01..03. (Source: `DELIVERABLE_REGISTER.csv` rows for the sibling deliverables.)
- **Interface ownership.** Both PKG-104 interfaces are flagged YES in `INTERFACE_REGISTER.csv`; the production package must coordinate with the adjacent grading/site-drainage and structural support work, even though those interfaces are recorded primarily as datasheet evidence under DEL-104-02 (artifacts ART-2280F54DB3, ART-41502579DF). (Source: `INTERFACE_REGISTER.csv`; `ARTIFACT_REGISTER.csv`.)
- **"Outside of modules" framing.** The package name distinguishes structural steel that is fabricated/erected outside the modular scope. Detailed boundary against modular structural steel scope is not slice-extracted from sources during this run and remains TBD.

## Trade-offs

- **Carrying source-limited scope conservatively vs. waiting for full sources.** The chosen direction is to produce a conservative production-package basis and an explicit closure record now, accepting that detailed design values remain TBD until Gate 5. The alternative (defer all production-unit work until full source extraction) was not adopted by the decomposition. (Source: `_CONTEXT.md` Notes; `DELIVERABLE_REGISTER.csv` Notes.)
- **Single discipline production unit per package vs. multiple discipline subdeliverables.** The decomposition uses a single discipline production unit per package; finer subdivision is TBD and would be introduced through the discipline deliverable register if warranted. (Source: `_CONTEXT.md` Anticipated Artifacts: "TBD discipline deliverable register".)

## Examples

TBD — no concrete worked examples are present in the locally accessible source slices for this deliverable.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONF-104-04-01 | Responsibility model: `_CONTEXT.md` and `DELIVERABLE_REGISTER.csv` say "TBD; EPC Integrator or discipline subcontractor as assigned"; `PACKAGE_REGISTER.csv` ResponsibilityModel states "EPC Integrator or discipline subcontractor responsibility is source-dependent; no separate vendor-package ownership model is inferred from the current sources." | `_CONTEXT.md` Identity (ResponsibleParty) | `PACKAGE_REGISTER.csv` PKG-104 ResponsibilityModel | Datasheet Identification; Specification R-104-04-06, R-104-04-08; Procedure Prerequisites | PROPOSAL: treat the package-register text as authoritative framing (source-dependent, no vendor-ownership inference) and resolve the deliverable-level ResponsibleParty as a human assignment recorded before production starts. | TBD |
| CONF-104-04-02 | Standards basis: Specification lists `26020-Package_Requirements.docx` and `DBM-Deepcut/4-25_Deepcut_DBM.md` as relevant, but no slice has been extracted; the closure record is meant to enumerate source-limited gaps, which would be premature without confirming whether these documents contain PKG-104 structural-steel requirements. | `_REFERENCES.md` Shared Source Root (file presence); `PACKAGE_REGISTER.csv` SourceBasis | `_REFERENCES.md` Missing/Deferred References (no slices extracted) | Specification Standards; closure record content | PROPOSAL: open `26020-Package_Requirements.docx` and `DBM-Deepcut/4-25_Deepcut_DBM.md` as deliverable-local source slices during the next pass, before authoring the closure record. | TBD |
| CONF-104-04-03 | "Outside of modules" boundary: the package name distinguishes outside-of-modules structural steel, but the boundary against modular structural steel scope (whether handled in PKG-103 Pipe Rack Modules or elsewhere) is not explicitly defined in the slice-extracted source rows for PKG-104. | `PACKAGE_REGISTER.csv` row PKG-104 (name only) | `PACKAGE_REGISTER.csv` row PKG-103 (Pipe Rack Modules) and other modular packages (not slice-compared) | Specification Scope; Guidance Considerations | PROPOSAL: extract a boundary statement from workbook row 105 and DBM SourceBasis in the next pass to make the outside-of-modules vs. modular split explicit; until then, retain the conservative carry. | TBD |
