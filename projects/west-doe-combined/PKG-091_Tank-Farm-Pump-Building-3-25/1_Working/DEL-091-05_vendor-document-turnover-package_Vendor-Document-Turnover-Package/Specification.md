# Specification — DEL-091-05 Vendor Document Turnover Package

## Scope

### In scope
- Compilation, control, submission, review, and final turnover of all vendor documents required for the PKG-091 Tank Farm Pump Building 3-25 package.
- The vendor document register; vendor document submittals; per-source-table vendor documentation rows carried as artifacts/evidence; turnover records.
- EPC Integrator interface and integration review of the vendor's submitted documents.

Source: GATE-07 DELIVERABLE_REGISTER.csv (DEL-091-05 row); SOW-0185; PROJECT_DECOMP Gate 5 deliverable basis.

### Out of scope
- Physical fabrication, supply, installation, or commissioning of the equipment package (covered under DEL-091-04 vendor-engineered-equipment-package and DEL-091-03 construction-work-package).
- Standalone deliverable status for individual source-table vendor document rows; per PROJECT_DECOMP DEC-004, those rows are artifacts/evidence under this turnover deliverable, not separate deliverables.
- DCS integration, foundations, and electrical supply to the MCC (by others per SOW-0188).

## Requirements

> Numbering: `R-091-05-NN`. Each row cites the authoritative source slice. Where the underlying DOCX source table for individual document rows is not locally readable as text in this run, the **list** of required documents is taken from the GATE-07 ARTIFACT_REGISTER (derived from the same source) and the per-row source slice is marked `location TBD`.

| ID | Requirement | Source |
|---|---|---|
| R-091-05-01 | The Package Vendor shall produce and maintain a Vendor Document Register (Vendor Document Index) covering all documents required by the package source vendor-documentation table. | ART-8AEAB021A9 (Vendor Documentation Register); ART-0C24267CA9 (Vendor Document Index, PRQ-009); 26020-Package_Requirements.docx package heading 44 — Vendor Engineering Deliverables table (location TBD) |
| R-091-05-02 | The Package Vendor shall implement and apply a Vendor Document Control Procedure (DOC-008) for revision control, transmittals, and status of all package documents. | ART-A0D4D9C668 (Vendor Document Control Procedure) |
| R-091-05-03 | Core vendor documents shall include, at minimum: Vendor Document Index, Vendor Document Control Procedure, Supplier Quality Plan (QLT-006), Inspection and Test Plan (QLT-003), Material Test Reports / Certificates (QLT-013), Inspection Release Certificate (QLT-020), Manufacturing Record Book / Vendor Data Book (QLT-021), Logistics / Shipping Plan (PRQ-013), Spare Parts Interchangeability Record (PRQ-015), and the Final Vendor Data Book / Final Supplier Documentation (PRQ-016). | GATE-07 ARTIFACT_REGISTER.csv, DEL-091-05 rows under `Vendor Documentation Evidence - Core vendor documents` |
| R-091-05-04 | Core package engineering documents shall include, at minimum: Mechanical Design Basis (MEC-001), Mechanical Equipment List (MEC-002), Mechanical Equipment Data Sheets (MEC-003), Package Equipment Specifications (MEC-006), Mechanical Calculation Package (MEC-014), Equipment General Arrangement Drawing (MEC-016), Equipment Installation / Setting Drawings (MEC-017), Lifting / Handling Study for Major Equipment (MEC-018), Equipment FAT / Performance Test Procedure (MEC-021), Equipment FAT / Performance Test Report (MEC-022), Mechanical Vendor Data Book / Final Documentation (MEC-023), Mechanical Spares / Special Tools Requirements (MEC-024), and the Mechanical Equipment IOM Manual (MEC-025). | GATE-07 ARTIFACT_REGISTER.csv, DEL-091-05 rows under `Vendor Documentation Evidence - Core package engineering` |
| R-091-05-05 | Rotating equipment / pumps documents shall include, at minimum: Rotating Equipment Specifications (MEC-004), Pump Data Sheets (MEC-007), and Mechanical Seal / Lube Oil Specification (MEC-019); additional rotating-equipment rows in the snapshot register apply where present. | GATE-07 ARTIFACT_REGISTER.csv, DEL-091-05 rows under `Vendor Documentation Evidence - Rotating equipment / pumps`; SOW-0187 (pump populations and seal plans) |
| R-091-05-06 | Pump data sheets and rotating equipment specifications shall reflect the equipment, seal plan, and power data declared in SOW-0187 (e.g., API-682 Plan 14/52 seal plans on the vertical inline centrifugal services; pneumatic diaphragm services per Hydracell / Graco selections; 575 V/3 Ph/60 Hz drives). | SOW-0187 |
| R-091-05-07 | Additional vendor document categories beyond Core/Engineering/Rotating (e.g., electrical, instrumentation, piping, structural, HSE, commissioning/turnover) shall be supplied where the source `Vendor Engineering Deliverables` table requires them; the full per-category list is carried as artifact rows under DEL-091-05. | GATE-07 ARTIFACT_REGISTER.csv (DEL-091-05 `Vendor Documentation Category Evidence` rows); 26020-Package_Requirements.docx package heading 44 (location TBD) |
| R-091-05-08 | The Package Vendor shall produce a Manufacturing Record Book / Vendor Data Book (QLT-021) and a Final Vendor Data Book / Final Supplier Documentation (PRQ-016) that consolidate all in-shop quality records prior to release/shipment. | ART-05D6947438; ART-DFD3CCA60D |
| R-091-05-09 | An Inspection Release Certificate (QLT-020) shall be issued by the Package Vendor prior to shipment, evidencing completion of ITP hold/witness points. | ART-E912751A7A |
| R-091-05-10 | Final turnover documentation to the EPC Integrator shall include the Mechanical Vendor Data Book / Final Documentation (MEC-023) and the Mechanical Equipment IOM Manual (MEC-025) for operations/maintenance use. | ART-1F262997B5; ART-619427A756 |
| R-091-05-11 | The EPC Integrator shall perform an interface/integration review of vendor-submitted documents and shall be the recipient of the turnover documentation set. | GATE-07 DELIVERABLE_REGISTER.csv (ResponsibleParty for DEL-091-05); PROJECT_DECOMP DEC-006 |
| R-091-05-12 | The deliverable shall not split individual source-table vendor document rows into separate deliverables; all such rows are carried as artifacts under this turnover deliverable. | PROJECT_DECOMP DEC-004; DEC-012 |
| R-091-05-13 | Required vs optional designation, document numbering, and submittal sequencing per source vendor-documentation table. | **TBD** — source slice in `_Sources/26020-Package_Requirements.docx` package heading 44 not locally readable as text in this run (location TBD). |

## Standards

The following standards are referenced explicitly in accessible source slices:

| Standard | Use | Source |
|---|---|---|
| API 682 (Plan 14/52) | Mechanical seal plan for vertical inline centrifugal pumps (sour condensate booster, condensate sweetening feed, condensate booster) | SOW-0187 |

ASSUMPTION: likely applicable additional standards (e.g., API 610 for centrifugal pumps; vendor's quality system standard for ITP/MRB; project-specific document numbering standard) are not derivable here because the supporting clause text is not locally accessible. Recorded as ASSUMPTION; do not derive clause-level requirements. (Location TBD — DOCX heading 44 not readable as text.)

## Verification

| Requirement | Verification Approach |
|---|---|
| R-091-05-01, R-091-05-02 | Document review of submitted Vendor Document Index and Vendor Document Control Procedure against source vendor-documentation table; EPC Integrator interface review. |
| R-091-05-03, R-091-05-04, R-091-05-05, R-091-05-07 | Cross-check submitted document register against the GATE-07 DEL-091-05 artifact list; verify each category's minimum set is present and accepted. |
| R-091-05-06 | Data-sheet review against SOW-0187 equipment list, seal plans, and motor data. |
| R-091-05-08, R-091-05-09 | Receipt and acceptance of Manufacturing Record Book, Final Vendor Data Book, and Inspection Release Certificate prior to release/shipment; ITP hold/witness sign-offs confirmed. |
| R-091-05-10 | Receipt of Mechanical Vendor Data Book and IOM Manual on turnover; spot-check completeness against equipment list. |
| R-091-05-11 | EPC Integrator review record recorded under DEL-091-06 (EPC Vendor Package Review and Acceptance) referencing this deliverable's submittals. |
| R-091-05-12 | Snapshot audit: confirm no per-row vendor document is registered as a sibling deliverable; rows appear only as artifacts under DEL-091-05. |

## Documentation (Anticipated Artifacts)

- Vendor document register (Vendor Documentation Register; Vendor Document Index)
- Vendor document submittals (per-document transmittals across categories)
- Source vendor-document table rows carried as artifacts where available (114 rows in current GATE-07 snapshot)
- Turnover records (Inspection Release Certificate; Manufacturing Record Book / Vendor Data Book; Final Vendor Data Book; IOM Manual; Spares / SPIR)

Source: GATE-07 DELIVERABLE_REGISTER.csv `Anticipated Artifacts` for DEL-091-05; ARTIFACT_REGISTER row enumeration.
