# Guidance: DEL-004-02_package-datasheet — Package Datasheet

## Purpose

The Package Datasheet exists to give downstream Site Grading discipline engineering or third-party package engineering a controlled technical handoff basis for PKG-004. It should carry the package identity, civil/site grading design context, applicable interface facts, source-supported conditions, and known open inputs without treating unresolved design information as closed.

Sources: `_CONTEXT.md`; Gate 7 `DELIVERABLE_REGISTER.csv`; Gate 7 `ARTIFACT_REGISTER.csv`; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-02 and SEC-11.

## Principles

- Use accepted Gate 7 registers for deliverable identity, package identity, objective association, artifact intent, and interface evidence.
- Use workbook row 5 as the direct package source for the Site Grading row and its interface X-columns.
- Use the 03-25 DBM civil/site sections for design conditions and civil/drainage requirements.
- Preserve uncertainty explicitly. Final geotechnical data, final hydrology, civil drawings, and package-specific exclusions are not closed in the accessible source set.
- Do not convert objective mappings into standalone design requirements unless the source slice supports the requirement.
- Treat workbook interface facts as datasheet evidence, not separate deliverables.

## Considerations

| Topic | Guidance | Source |
|---|---|---|
| Drain / Containment interface | Include the interface as applicable and connect it to process-contaminated drainage routing and containment coordination. | Workbook row 5; Gate 7 `INTERFACE_REGISTER.csv`; 03-25 DBM SEC-11 Surface Water and Drainage |
| Grading / Site Drainage / Spill Containment interface | Include the interface as applicable and connect it to surface-water collection, segregation, retention, and offsite-discharge prevention. | Workbook row 5; Gate 7 `INTERFACE_REGISTER.csv`; 03-25 DBM SEC-11 Layout Basis and Surface Water and Drainage |
| Hydrology | Keep rainfall and storm design language qualified because the DBM uses NBCC 2020 Dawson Creek IDF data as proxy pending site-specific update. | 03-25 DBM SEC-02 Site-Specific Design Data |
| Geotechnical design | Keep foundation and geotechnical closure qualified pending final geotechnical report acceptance. | 03-25 DBM SEC-02 Geotechnical and Seismic Basis; SEC-11 Site and Civil Conditions |
| Civil drawings | Treat plot plan, spacing, and equipment layout verification as required before final issue. | 03-25 DBM SEC-11 Layout Basis |
| Standards | List NBCC and other governing content as referenced by the DBM, but avoid clause-level requirements where source text is unavailable. | 03-25 DBM SEC-15 table |

## Trade-offs

| Trade-off | Direction |
|---|---|
| Early handoff versus final design certainty | The datasheet can provide a controlled early handoff, but must flag hydrology, geotechnical, civil drawing, and exclusion gaps as `TBD` rather than closing them. |
| Interface completeness versus scope creep | Include only the workbook row 5 interface facts and DBM-supported civil/drainage implications. Do not add undeclared interfaces from similar packages. |
| Civil design detail versus source fidelity | Include explicit source-supported values and requirements. Leave unstated elevations, slopes, pond volumes, material sections, and drawing references as `TBD`. |

## Examples

TBD. The accessible source set does not provide a completed Site Grading datasheet example.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-004-02-001 | The final geotechnical report is required before foundation design closure, but the report is not available in the deliverable source set. | 03-25 DBM SEC-02 Geotechnical and Seismic Basis; SEC-11 Site and Civil Conditions | Missing local final geotechnical report | Datasheet Conditions; Specification Standards; Procedure Verification | Keep geotechnical-dependent values and closure criteria as `TBD` until final report is accepted. | TBD |
| HRR-004-02-002 | Hydrology/site-specific rainfall inputs are pending while current drainage and retention design uses NBCC 2020 Dawson Creek IDF proxy data. | 03-25 DBM SEC-02 Site-Specific Design Data; SEC-11 Surface Water and Drainage | Missing site-specific hydrology update | Datasheet Conditions; Specification Requirements; Procedure Verification | Use current DBM proxy basis for preliminary datasheet content and mark final hydrology as `TBD`. | TBD |
| HRR-004-02-003 | Plot plan, spacing, and equipment layout must be verified before final issue, but civil drawings/layout files are not available in the deliverable source set. | 03-25 DBM SEC-11 Layout Basis | Missing local civil drawings/current equipment layout | Datasheet Construction; Procedure Steps | Treat layout-dependent Site Grading data as `TBD` pending current civil drawing/layout verification. | TBD |
