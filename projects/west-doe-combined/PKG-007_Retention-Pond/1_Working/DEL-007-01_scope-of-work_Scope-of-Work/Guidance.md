# Guidance: DEL-007-01_scope-of-work — Scope of Work

## Purpose

Use this document to shape the PKG-007 Retention Pond Scope of Work so it remains faithful to the accepted Gate 7 decomposition and the accessible source basis. The deliverable is an EPC Integrator package-scope anchor for a Civil retention pond package supporting the 03-25 compressor station and liquids hub. Source: `_CONTEXT.md`; Gate 7 `DELIVERABLE_REGISTER.csv` row 26; Gate 7 `PACKAGE_REGISTER.csv` row 8.

## Principles

- Preserve the package identity exactly as accepted: PKG-007, Retention Pond, WBS 02, CoA tracking number 26020-02-42-007, Civil discipline. Source: workbook export worksheet row 8; Gate 7 `PACKAGE_REGISTER.csv` row 8.
- Treat Drain / Containment and Grading / Site Drainage / Spill Containment as the declared package interfaces. Do not add undeclared electrical, structural, controls, or piping interfaces unless a later accepted source or human ruling supports them. Source: Gate 7 `INTERFACE_REGISTER.csv` rows 14-15; workbook export worksheet row 8.
- Keep hydrology and geotechnical items visible as open basis items. The DBM uses Dawson Creek IDF data as a proxy and states final geotechnical parameters remain to be confirmed. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` rainfall basis note and "Geotechnical and Seismic Basis".
- Do not convert package context into detailed pond geometry, capacity, liner, discharge, or grading quantities unless the values are present in accepted sources. Use `TBD` instead.

## Considerations

The Scope of Work should distinguish between scope identity and design closure. The workbook and Gate 7 registers establish that the Retention Pond is a Civil package with drain/containment and grading/site drainage/spill containment interfaces. The DBM establishes civil design intent and open design-basis constraints, but it does not provide package-specific pond dimensions, storage volume, discharge point, liner system, or final hydrology/geotechnical values in the reviewed source slices.

The retention pond scope is linked to facility-level environmental and operational protection because surface-water management must prevent uncontrolled offsite discharge, protect process areas, and support construction and operations access. Process-contaminated drainage must be routed to the appropriate drain or containment system rather than surface-water discharge. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` "Surface Water and Drainage".

## Trade-offs

| Topic | Guidance |
|---|---|
| Specificity vs. source fidelity | Prefer a short, source-supported SOW with `TBD` design values over an apparently complete SOW that invents pond geometry or capacity. |
| Current rainfall basis vs. final hydrology | Use current precipitation/storm basis only as interim basis; carry hydrology update as an open item. |
| EPC Integrator vs. discipline subcontractor | Treat EPC Integrator as responsible for this deliverable. If the work is later delegated, record the source or human ruling because Gate 7 states package responsibility is source-dependent. |
| Surface water vs. contaminated drainage | Keep the boundary explicit: process-contaminated drainage is not surface-water discharge and belongs in the appropriate drain/containment system. |

## Examples

| Example SOW statement | Status |
|---|---|
| "PKG-007 Retention Pond is the Civil package under WBS 02, CoA tracking number 26020-02-42-007." | Supported by workbook export worksheet row 8 and Gate 7 `PACKAGE_REGISTER.csv` row 8. |
| "The package interfaces are Drain / Containment and Grading / Site Drainage / Spill Containment." | Supported by Gate 7 `INTERFACE_REGISTER.csv` rows 14-15 and workbook export worksheet row 8. |
| "Retention pond storage volume is [value]." | `TBD`; no package-specific capacity found in accessible source slices. |

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-007-01 | Final hydrology basis for retention pond sizing is not closed. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` rainfall basis note | Site-specific final hydrology input not present in accessible sources | Datasheet Conditions; Specification SOW-REQ-006/SOW-REQ-008; Procedure verification | Use DBM current precipitation/storm basis as interim and keep final hydrology as TBD. | TBD |
| HRR-007-02 | Final geotechnical parameters for civil/foundation closure are not closed. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` "Geotechnical and Seismic Basis" | Final geotechnical report not present in accessible sources | Datasheet Conditions; Specification SOW-REQ-008; Procedure verification | Treat current geotechnical basis as preliminary and require final report before closure. | TBD |
| HRR-007-03 | Discipline subcontractor responsibility, if any, is source-dependent. | Gate 7 `PACKAGE_REGISTER.csv` row 8 | No subcontractor assignment source found | Datasheet Identification; Specification SOW-REQ-009; Procedure records | Keep EPC Integrator as deliverable owner until a source or human ruling assigns otherwise. | TBD |
