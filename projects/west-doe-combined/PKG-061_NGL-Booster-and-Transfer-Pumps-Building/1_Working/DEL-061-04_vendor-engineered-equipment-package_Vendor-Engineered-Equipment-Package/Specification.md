# Specification: DEL-061-04 Vendor Engineered Equipment Package — NGL Booster and Transfer Pumps Building

## Scope

This Specification governs the vendor-engineered equipment package for the NGL Booster and Transfer Pumps Building (`PKG-061`). It covers the Package Vendor's engineering, design, fabrication / supply, and delivery of the physical equipment package as developed from the EPC Scope of Work (`DEL-061-01`) and the EPC Package Datasheet (`DEL-061-02`).

**In scope**

- Engineered design of the NGL booster / transfer pump package, including the two tagged pumps `P-9570-1` and `P-9580-1` (DBM-Deepcut `4-25_Deepcut_DBM.md` Trace Appendix row 58).
- Pump skids, baseplates, couplings, drivers, lube systems, seal systems, local instrumentation, local piping within battery limits, and skid wiring (vendor-supplied content of the engineered package).
- Vendor design basis and vendor datasheet set supporting the engineered package (`_CONTEXT.md` Anticipated Artifacts).
- Integration review interface points with EPC Integrator.

**Out of scope (carried by other DEL-061 deliverables or other packages)**

- EPC Scope of Work narrative and responsibility assignment (`DEL-061-01`).
- EPC Package Datasheet (`DEL-061-02`) — provides the design inputs to this deliverable.
- Construction Work Package, installation, tie-ins (`DEL-061-03`).
- Vendor document turnover register and submittals (`DEL-061-05`).
- EPC vendor package review and acceptance (`DEL-061-06`).

## Requirements

| ID | Requirement | Authority / Source |
|---|---|---|
| R-061-04-01 | The Vendor shall supply two (2) NGL booster / transfer pumps tagged `P-9570-1` and `P-9580-1`. | DBM-Deepcut Trace Appendix row 58 (count = 2; tags listed) |
| R-061-04-02 | The pumps shall be of API 610, multi-stage can configuration. | DBM-Deepcut Trace Appendix row 58 ("Pumps (API 610, multi-stage can)") |
| R-061-04-03 | The pumps shall be designed in accordance with the latest project-adopted edition of API 610 (edition `TBD`, to be confirmed against `26020-Package_Requirements.docx` package heading 17 — location TBD). | DBM-Deepcut Trace Appendix row 58; project standard adoption `TBD` |
| R-061-04-04 | The Vendor shall design the engineered equipment package to the duty (flow, head, NPSHr, suction/discharge pressures, temperatures, NGL composition) defined in the EPC Package Datasheet `DEL-061-02`. | `_CONTEXT.md` Scope ("developed from the EPC package Scope of Work and Package Datasheet"); `DELIVERABLE_REGISTER.csv` row 417 |
| R-061-04-05 | Pump mechanical seals shall comply with API 682 (ASSUMPTION — typical companion standard to API 610; confirmation `TBD`). | ASSUMPTION; confirm against `26020-Package_Requirements.docx` |
| R-061-04-06 | Drivers shall be electric induction motors sized to the EPC Package Datasheet (motor voltage, frame, enclosure, insulation class — values `TBD` in `DEL-061-02`). | ASSUMPTION based on facility electrification convention (DBM-Deepcut `4-25_Deepcut_DBM.md` line 936 confirms electric-motor convention for similar rotating equipment); driver specifics for `P-9570-1/P-9580-1` `TBD` |
| R-061-04-07 | The engineered package shall be designed for the project site conditions, including cold-climate startup down to -40 deg C ambient where applicable. | ASSUMPTION from DBM-Deepcut `4-25_Deepcut_DBM.md` line 1679 (-40 deg C startup language for sister liquid-pump service); confirm in `DEL-061-02` |
| R-061-04-08 | The Vendor shall produce a vendor package design basis and vendor datasheet set covering pumps, drivers, seals, instrumentation, and accessories. | `_CONTEXT.md` Anticipated Artifacts: "vendor package design basis and datasheet set" |
| R-061-04-09 | The Vendor shall identify and document all package interfaces (mechanical, process, electrical, I&C, civil/structural, HSE) for EPC integration review. | `_CONTEXT.md` ResponsibleParty wording: "with EPC Integrator integration review"; DELIVERABLE_REGISTER.csv row 417 |
| R-061-04-10 | The engineered package shall satisfy the scope items `SOW-0149`, `SOW-0150`, `SOW-0151`, `SOW-0152` allocated to `PKG-061`. | `DELIVERABLE_REGISTER.csv` row 417; `OBJECTIVE_SCOPE_MAP.csv` PKG-061 entries |
| R-061-04-11 | Materials of construction for wetted parts shall be suitable for NGL service per the EPC Package Datasheet (`DEL-061-02`); specific material class `TBD`. | ASSUMPTION; location TBD: `26020-Package_Requirements.docx` package heading 17 |
| R-061-04-12 | Sparing philosophy — the Vendor shall implement the sparing configuration directed by the EPC Package Datasheet. ASSUMPTION: 2 x 100% based on equipment count of 2 (DBM-Deepcut row 58). The DBM-Deepcut sparing table does not list "NGL Booster" — confirm against `26020-Package_Requirements.docx`. | DBM-Deepcut Trace Appendix row 58; sparing percentages `TBD` |

## Standards

| Standard | Application | Status |
|---|---|---|
| API 610 | Pump design (multi-stage can configuration) | Authoritative per DBM-Deepcut Trace Appendix row 58; edition `TBD` (location TBD: `26020-Package_Requirements.docx`) |
| API 682 | Pump mechanical seal systems | ASSUMPTION (typical companion to API 610); confirmation `TBD` |
| NEMA MG 1 / IEC equivalents | Electric motor design | ASSUMPTION (project rotating-equipment convention, DBM-Deepcut line 936 reference); applicability to `P-9570-1/P-9580-1` `TBD` |
| Project Basis of Design (cold climate, -40 deg C) | Site/operability | DBM-Deepcut line 1679 (sister service); confirm in `DEL-061-02` |
| `26020-Package_Requirements.docx` package heading 17 | Authoritative project package requirements | location TBD — binary source not locally text-accessible |

## Verification

| Requirement | Verification Method | Evidence |
|---|---|---|
| R-061-04-01 | Document review of vendor datasheet set | Pump count and tag list reconcile with `DEL-061-02` |
| R-061-04-02 | Design review against API 610 | Type code (VS configuration consistent with "multi-stage can") confirmed on vendor datasheet |
| R-061-04-03 | Vendor compliance certificate | Statement of compliance with adopted API 610 edition |
| R-061-04-04 | Cross-check vendor datasheet vs. `DEL-061-02` duty data | Datasheet alignment record |
| R-061-04-05 | Seal datasheet review | API 682 compliance statement (`TBD` until confirmed) |
| R-061-04-06 | Motor datasheet and electrical interface review | Voltage, frame, enclosure confirmed against `DEL-061-02` |
| R-061-04-07 | Cold-climate design review | Materials and lube-oil heating verified vs. -40 deg C basis |
| R-061-04-08 | Document register check | Vendor design basis and datasheet set present in `DEL-061-05` turnover |
| R-061-04-09 | Interface matrix review with EPC Integrator | Captured in EPC review `DEL-061-06` |
| R-061-04-10 | Scope traceability matrix | Cross-references `SOW-0149..0152` |
| R-061-04-11 | Material certificates / MTRs | Reviewed at FAT and turnover |
| R-061-04-12 | Sparing-config review | Confirmed during `DEL-061-06` |

Factory Acceptance Test (FAT) and Inspection & Test Plan (ITP) details are governed by the vendor datasheet set; specific FAT scope `TBD`.

## Documentation

The Vendor shall produce the following artifacts (anticipated per `_CONTEXT.md`):

- Vendor engineered physical equipment package (delivered).
- Vendor package design basis.
- Vendor datasheet set (pumps, drivers, seals, accessories, instruments).
- Package interface matrix (for EPC Integrator review).
- Compliance statement against API 610 (and other adopted standards).
- Inputs to `DEL-061-05` Vendor Document Turnover Package.
