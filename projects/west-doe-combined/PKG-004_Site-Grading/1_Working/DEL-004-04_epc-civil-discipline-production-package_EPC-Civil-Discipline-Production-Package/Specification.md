# Specification: EPC / Civil Discipline Production Package

## Scope

This specification governs the source-limited initialization of the EPC / Civil Discipline Production Package for `PKG-004 - Site Grading`, WBS 02. The package is a non-vendor Civil production unit for the workbook-defined Site Grading scope and must preserve the accepted Gate 7 package identity, scope item `SOW-0004`, and declared interface facts.

The scope includes production-package basis content for civil site grading, drainage, surface-water management, and drain/containment coordination where supported by the accepted sources. It excludes final discipline drawing lists, sealed design calculations, construction IFC issue content, and detailed authority/permit submissions where the current source set does not define them.

## Requirements

| ID | Requirement | Source |
|---|---|---|
| REQ-001 | The production package shall identify the package as `PKG-004 - Site Grading`, WBS 02, Civil discipline, CoA tracking number `26020-01-42-003`. | PACKAGE_REGISTER.csv row `PKG-004`; workbook row 5 |
| REQ-002 | The package shall carry the workbook-defined Civil Site Grading package as a distinct flat project package and shall not merge duplicate tracking-number packages across WBS rows. | SCOPE_LEDGER.csv row `SOW-0004` |
| REQ-003 | The production package shall preserve the applicable interface types `Drain / Containment` and `Grading / Site Drainage / Spill Containment`. | INTERFACE_REGISTER.csv rows `IFC-FA26BF6895`, `IFC-D2D12F4CA2`; workbook row 5 |
| REQ-004 | Civil design content shall cover grading, drainage, roads, surface-water management, retention pond, and related civil/site conditions where applicable to Site Grading. | DBM 3-25 SEC-11, Site and Civil Conditions |
| REQ-005 | Surface-water management shall prevent uncontrolled offsite discharge, protect process areas, and support construction and operations access. | DBM 3-25 SEC-11, Surface Water and Drainage |
| REQ-006 | Retention pond sizing and drainage design shall use the current precipitation and storm basis until hydrology is updated. | DBM 3-25 SEC-11, Surface Water and Drainage; DBM rainfall-basis paragraph |
| REQ-007 | Process-contaminated drainage shall be routed to the appropriate drain or containment system rather than surface-water discharge. | DBM 3-25 SEC-11, Surface Water and Drainage |
| REQ-008 | The production package shall record that the final geotechnical report is required before foundation design closure where civil production outputs depend on foundation or support design. | DBM 3-25 SEC-11, Site and Civil Conditions |
| REQ-009 | The production package shall include a source-limited requirements closure record and mark unresolved values or missing design inputs as `TBD`. | DELIVERABLE_REGISTER.csv row `DEL-004-04`; four-documents source-grounding rule |
| REQ-010 | ASSUMPTION: The discipline production package should include a deliverable register or index for civil drawings, calculations, and closure records once the discipline subcontractor or EPC Integrator assigns the detailed production scope. | Derived from DELIVERABLE_REGISTER.csv anticipated artifact `TBD discipline deliverable register`; human ruling required before treating as complete deliverable content |

## Standards

| Standard / governing content | Status |
|---|---|
| NBCC | Identified as governing civil/structural content in DBM 3-25 SEC-15; clause-level application TBD |
| Geotechnical report | Required for foundation design closure; final report not available in current source set |
| Site data | Current SEC-02 values available for elevation, ambient temperature, precipitation, snow, wind, seismic, and preliminary geotechnical assumptions |
| Civil drawings | Required verification reference before final issue; drawing list not available in current source set |
| Surface-water management | Governing content identified in DBM 3-25 SEC-11 and SEC-15 |
| BC water legislation and regulator requirements | Applicable to water use, watercourse interaction, diversion, discharge, produced-water handling, stormwater management, and related activities; detailed trigger register TBD |

## Verification

| Requirement | Verification approach |
|---|---|
| REQ-001, REQ-002 | Check production package cover sheet and basis section against Gate 7 `PACKAGE_REGISTER.csv`, `SCOPE_LEDGER.csv`, and workbook row 5 |
| REQ-003 | Check interface matrix or package basis against Gate 7 `INTERFACE_REGISTER.csv` and workbook row 5 X-columns |
| REQ-004 through REQ-007 | Check civil design basis, drawings, and calculations against DBM 3-25 SEC-11 and current storm/hydrology basis |
| REQ-008 | Confirm final geotechnical report status is recorded before civil/foundation-dependent closure |
| REQ-009 | Confirm every requirement in the closure record has a cited source or is marked `TBD`, `ASSUMPTION`, or `CONFLICT` |
| REQ-010 | Human review of the discipline deliverable register structure and ownership before final package use |

## Documentation

The production package should contain or reference the following records:

- Discipline production package basis.
- Discipline deliverable register: TBD.
- Source-limited requirements closure record.
- Interface evidence for `Drain / Containment` and `Grading / Site Drainage / Spill Containment`.
- Current hydrology/storm-basis status and any update requirements.
- Current geotechnical-report status where the production package touches foundation or support design closure.
