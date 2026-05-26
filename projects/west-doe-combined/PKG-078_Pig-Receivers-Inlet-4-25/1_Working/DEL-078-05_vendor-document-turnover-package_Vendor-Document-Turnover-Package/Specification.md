# Specification — DEL-078-05 Vendor Document Turnover Package

## Scope

### In scope

This specification governs the **Vendor Document Turnover Package** for `PKG-078` Pig Receivers (Inlet) 4-25, equipment tag `26020-01-PT-35-001`. It defines the required composition, content, and quality of vendor-supplied documentation and turnover records for the three (3) 610 mm OD pig receiver assemblies (`PR-1010/1020/1030-1`) and their associated HIPPS packages. Source: `_Sources/26020-Package_Requirements.docx` (heading `26020-01-PT-35-001`).

Specifically includes:
- Vendor document register (the controlled index).
- Vendor document submittals (engineering, fabrication, QA/QC, operations).
- Turnover records (transmittals, acceptance, as-shipped evidence).
- EPC Integrator interface/integration review hooks. Source: `_CONTEXT.md` ResponsibleParty; DELIVERABLE_REGISTER row 436.

### Out of scope

- Equipment design, fabrication, and supply — covered by `DEL-078-04_vendor-engineered-equipment-package`.
- EPC review and acceptance disposition — covered by `DEL-078-06_epc-vendor-package-review-and-acceptance`.
- Construction work and field installation records — covered by `DEL-078-03_construction-work-package`.
- EPC package scope of work and datasheet — covered by `DEL-078-01` and `DEL-078-02`.

## Requirements

### R-01 Vendor document register exists and is controlled

- The Package Vendor SHALL maintain a vendor document register listing every document transmitted for this package, with document number, title, revision, status, transmittal reference, and date.
- Source: `_CONTEXT.md` Anticipated Artifacts; DELIVERABLE_REGISTER row 436 Primary Artifact column.

### R-02 Document classes match source-required list

- The vendor document set SHALL include every document class enumerated in the source `Vendor Engineering Deliverables` section for `26020-01-PT-35-001`.
- ASSUMPTION: The source `Vendor Engineering Deliverables` body is empty in the currently accessible slice; the canonical list is therefore `TBD`. Until populated, a conflict is recorded in `Guidance.md` Conflict Table.

### R-03 Pressure-containing equipment documentation

- Documentation SHALL cover the pressure-containing scope identified in source: pig receiver barrels (610 mm OD), upstream ESDVs, HIPPS shutdown valves (primary and redundant), HIPPS pressure control valve, outlet pressure transmitter, vent piping to HP flare. Source: `_Sources/26020-Package_Requirements.docx` Major Included Equipment.
- Pressure vessel design code, jurisdiction, and code-stamp requirements: TBD (not stated in available source slice).

### R-04 HIPPS package documentation

- Vendor SHALL provide documentation that supports the HIPPS function described in source: PID control of inlet separator pressure, pneumatic hi-low shutoff (primary), redundant pneumatic hi-low shutoff valve, pressure control valve, outlet pressure transmitter. Source: same.
- Target SIL and proof-test interval: TBD (not stated in source).

### R-05 Sour-service documentation

- Vendor SHALL provide material selection, NACE/MR0175 (ASSUMPTION) compliance evidence, and welding/PWHT records appropriate to sour service at the stated 1.0 mol% design basis. Source: `_Sources/26020-Package_Requirements.docx` Major Included Equipment ("Sour service: Design is 1.0 mol%"). Species (H2S) is ASSUMPTION; standard reference is ASSUMPTION pending project-level standard.

### R-06 Purge and vent system documentation

- Vendor SHALL document the sweet-gas purge arrangement downstream of the manual isolation valve and the HP-flare vent connection. Source: `_Sources/26020-Package_Requirements.docx` Major Included Equipment.

### R-07 Interface evidence

- Vendor documentation SHALL support the physical-interface scope identified in `_Sources/26020-Packages_Interfaces_4_export.xlsx` (specific rows: TBD).

### R-08 Turnover records completeness

- Each transmittal in the register SHALL have an associated acceptance status (e.g., Code 1/2/3 ASSUMPTION) and date. Final turnover SHALL produce a complete-set acceptance record.
- Specific code scheme: TBD (project document control standard not in accessible references).

### R-09 Revision discipline

- Every superseded document revision SHALL remain traceable in the register; the register SHALL identify the current revision in force.

### R-10 EPC review interface

- The turnover package SHALL expose a defined review handoff to EPC Integrator (informs `DEL-078-06`). Mechanism (transmittal portal, format): TBD.

## Standards

| Standard | Status | Source / Notes |
|---|---|---|
| Project EPC vendor documentation standard | Identification TBD | Not stated in available references |
| NACE MR0175 / ISO 15156 (sour service materials) | ASSUMPTION: likely applicable given 1.0 mol% sour design | Source mentions sour service but does not cite a standard |
| ASME BPVC Section VIII (pig receiver barrels as pressure vessels) | ASSUMPTION: likely applicable | Not cited in available source slice |
| IEC 61508 / IEC 61511 (HIPPS SIL) | ASSUMPTION: likely applicable | Not cited in available source slice |
| Document numbering / control standard | TBD | Not stated |

## Verification

| Requirement | Verification approach |
|---|---|
| R-01 | Existence and currency of vendor document register; sample audit of register rows against transmittals. |
| R-02 | Cross-check vendor register classes against source `Vendor Engineering Deliverables` list (when populated). Gap report. |
| R-03 | Inspection of submitted equipment datasheets, code calculations, MTRs, and code stamps against equipment list. |
| R-04 | Review of HIPPS functional design, SIL verification report, and proof-test records. |
| R-05 | Material certifications and NACE compliance statements reviewed; welding/PWHT records sampled. |
| R-06 | Drawings show purge and vent routing as described in source; tie-in points consistent with interface register. |
| R-07 | Vendor documents cross-reference rows in `26020-Packages_Interfaces_4_export.xlsx`. |
| R-08 | Each transmittal has acceptance disposition; final turnover acceptance record exists. |
| R-09 | Register shows historical revisions and current-revision flag. |
| R-10 | Documented review/transmittal route to EPC Integrator exists. |

## Documentation

- `Datasheet.md` — descriptive attributes for the turnover-package composition.
- `Specification.md` — this document.
- `Guidance.md` — rationale and Conflict Table.
- `Procedure.md` — operational steps to produce/use the turnover package.
- Vendor document register (artifact, produced by Package Vendor).
- Vendor document submittals (artifacts, produced by Package Vendor).
- Turnover transmittals and acceptance records (artifacts).
