# Specification — DEL-041-05 Vendor Document Turnover Package (PKG-041)

## Scope

### In scope
- The complete vendor document set required for the PKG-041 13.8kV, 3.0MW Standby Generator Building (490-1) package, organized in a Vendor Document Index (`PRQ-009`) and controlled per the Vendor Document Control Procedure (`DOC-008`).
- All "Core vendor documents" enumerated in `_Sources/26020-Package_Requirements.docx` ("Vendor Engineering Deliverables" section).
- The discipline-applicable engineering and design documents required for an Electrical-led packaged standby generator building delivered as a vendor-engineered module (Electrical lead; substantial Mechanical, I&C, Structural, and limited Civil/HVAC content per the building/enclosure form factor).
- Vendor quality records: Supplier Quality Plan, ITP, MTRs/Certificates, Inspection Release Certificate, Manufacturing Record Book / VDB (`QLT-006`, `QLT-003`, `QLT-013`, `QLT-020`, `QLT-021`).
- Logistics records: Shipping Plan (`PRQ-013`), SPIR (`PRQ-015`).
- Final/turnover books: `PRQ-016` and discipline final books (e.g., `MEC-023`, `ELE-030` energization package).
- Source vendor document table rows themselves (as artifacts/evidence) referenced from the index.

### Out of scope
- Production of the engineered equipment package itself (covered by `DEL-041-04`).
- EPC Integrator review and acceptance of the submitted documents (covered by `DEL-041-06`).
- Construction tie-in and turnover into the larger facility (covered by `DEL-041-03`).
- Facility-level standby-power architecture decisions and load-shedding/sequencing studies (TBD per `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2943, 3086; not a Package Vendor scope item).

## Requirements

### R-1 Vendor Document Index
The Package Vendor shall provide a Vendor Document Index (`PRQ-009`) listing every document in the turnover set with document number, revision, status, and submittal/return cycle status.
- Source: `_Sources/26020-Package_Requirements.docx` — "Vendor Engineering Deliverables / Core vendor documents".

### R-2 Vendor Document Control Procedure
The Package Vendor shall provide a Document Control Procedure (`DOC-008`) describing numbering, revisioning, transmittal mechanics, and review-cycle handling.
- Source: same as R-1.

### R-3 Core vendor documents
The set shall include all "Core vendor documents" listed in `_Sources/26020-Package_Requirements.docx`:
`PRQ-009`, `DOC-008`, `QLT-006`, `QLT-003`, `QLT-013`, `QLT-020`, `QLT-021`, `PRQ-013`, `PRQ-015`, `PRQ-016`.

### R-4 Discipline applicability (Electrical, I&C)
The set shall include the Electrical and I&C document classes applicable to a packaged standby generator building per the source's discipline tables:
- Electrical: `ELE-002`, `ELE-003`, `ELE-011` (Motor/Generator Starting Study if package-internal motors warrant; otherwise N/A), `ELE-012`, `ELE-014`, `ELE-015`, `ELE-016`, `ELE-017` (integral lighting), `ELE-019`, `ELE-020`, `ELE-027`, `ELE-028`, `ELE-029` (FAT), `ELE-030` (Energization Package).
- I&C: `INS-002`, `INS-003`, `INS-005`, `INS-006`, `INS-008`, `INS-009`, and the remaining INS entries enumerated in the source list applicable to the genset control/monitoring/trip interfaces.
- Source: `_Sources/26020-Package_Requirements.docx` — "Electrical, lighting, EHT, grounding" and "Instrumentation and controls interfaces".
- ASSUMPTION: All INS entries listed in the source are applicable; the EPC Integrator confirms the per-line applicability call during `DEL-041-06` review.

### R-5 Discipline applicability (Mechanical / Enclosure / Engine)
The set shall include mechanical equipment data documents for the packaged genset and enclosure: `MEC-001`, `MEC-002`, `MEC-003`, `MEC-006`, `MEC-016`, `MEC-017`, `MEC-018`, `MEC-021`, `MEC-022` (FAT report), `MEC-023` (Mechanical Final Documentation), `MEC-024`, `MEC-025`.
- Source: `_Sources/26020-Package_Requirements.docx` — "Core package engineering" and "Mechanical Equipment IOM Manual" rows; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2076–2083 (enclosure, walkway, lift provisions, fuel, driver basis).

### R-6 Discipline applicability (Structural, Civil/Foundations, HVAC, Fire & Gas, Drainage)
- Structural: applicable subset of the source's structural document classes for the building/enclosure (skid, lifting, anchoring) — ASSUMPTION confirmed via `DEL-041-06`.
- Civil / Foundations / Drainage: per `PACKAGE_REGISTER.csv` row 43 these interface types are identified for the package, but the foundation and site drainage tie-ins are owned by the EPC Integrator at the facility level; Package Vendor documents shall provide the loads, anchor patterns, and drainage/containment requirements needed for those tie-ins. Mark interior civil items N/A with rationale.
- HVAC / Building services: enclosure ventilation, heating, integral lighting, fire/gas as integral to the module — applicable.
- Fire & Gas / Safety Systems: vendor documents shall include the F&G interface basis as a tie-in package; site F&G is EPC Integrator scope.
- Source: `PACKAGE_REGISTER.csv` row 43 (Applicable interface types); `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2076 (vendor-supplied weather-protective enclosure suitable for outdoor installation).

### R-7 Quality records and traceability
The Package Vendor shall provide:
- Supplier Quality Plan (`QLT-006`),
- Inspection and Test Plan (`QLT-003`) with hold/witness points,
- Material Test Reports / Certificates (`QLT-013`),
- Inspection Release Certificate (`QLT-020`),
- Manufacturing Record Book / Vendor Data Book (`QLT-021`).
- Source: `_Sources/26020-Package_Requirements.docx` — "Core vendor documents".

### R-8 Logistics and spares
The Package Vendor shall provide a Logistics / Shipping Plan (`PRQ-013`) and a Spare Parts Interchangeability Record (`PRQ-015`). Shipping plan shall account for the enclosure form factor (single shop-fabricated module per `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2787).
- Source: same as R-7.

### R-9 FAT/SAT records
The Package Vendor shall provide FAT and energization records:
- `MEC-021` / `MEC-022` (mechanical FAT procedure/report for the engine/genset),
- `ELE-029` / `ELE-030` (electrical FAT/SAT procedure and energization package).
- Source: `_Sources/26020-Package_Requirements.docx`.

### R-10 As-built and turnover books
The Package Vendor shall deliver `PRQ-016` Vendor Data Book / Final Supplier Documentation and discipline final books (e.g., `MEC-023`); the EPC Integrator integrates these into the package turnover record. As-built electrical, I&C, and mechanical drawings shall be issued.
- Source: same as R-9.

### R-11 Standards compliance traceability
Each vendor-supplied document subject to industry codes/standards shall reference the governing standard. Specific code citations applicable to a standby generator package (e.g., NFPA 110 emergency/standby power systems, NEMA MG1 motors/generators, NFPA 37 stationary combustion engines, IBC/ASCE 7 structural, applicable Canadian electrical area/CSA standards for a cold-climate site) are **not explicitly cited** in the accessible source set for this deliverable.
- Source: `_Sources/26020-Package_Requirements.docx`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (no standby-generator-specific standards clause located in the accessed slices).
- ASSUMPTION: Industry-standard standby generator codes apply; specific clauses are TBD until detailed-design specifications are issued. See Conflict Table HRR-041-05-002.

### R-12 Submittal cadence and native files
- Submittal cadence (preliminary / certified / as-built): TBD — not stated in accessible source slices.
- Native file format requirements (e.g., CAD format, electronic transmittal): TBD — not stated in accessible source slices.

### R-13 Voltage/rating reconciliation (package identity)
The Package Vendor's documentation set must clearly state the as-engineered generator rating(s), terminal voltage(s), and connection scheme. The package title carried in `PACKAGE_REGISTER.csv` row 43 ("13.8kV, 3.0MW") and the current standby-power basis in `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2943 ("TOU standby generators connected at the low-voltage MCC level with transfer switches, replacing the prior centralized 13.8 kV emergency-generator concept for this facility scope") are not aligned. See Conflict Table HRR-041-05-001.
- Disposition: Package Vendor documentation shall report actual engineered ratings as ordered; turnover Index shall note the rating-basis source. EPC Integrator confirms identity reconciliation in `DEL-041-06`.

## Standards

| Standard | Applicability | Location |
|---|---|---|
| NFPA 110 Emergency and Standby Power Systems | Standby generator system — ASSUMPTION; not explicitly cited in accessible source set | location TBD |
| NEMA MG1 | Generator/large rotating machines — ASSUMPTION; cited in DBM for motors but not specifically for standby generator | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (motor context only) |
| NFPA 37 Stationary Combustion Engines | Engine fuel and installation — ASSUMPTION; not explicitly cited | location TBD |
| IBC / ASCE 7 / NBCC (structural and seismic) | Building/enclosure structural design — ASSUMPTION | location TBD |
| CSA / Canadian electrical area classification standards | Cold-climate Canadian site; electrical area classification — ASSUMPTION | location TBD |
| Workbook package applicable interface types | Utility Piping; Drain/Containment; Electrical Power; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Communications/Network; Building HVAC/Services; Fire & Gas/Safety Systems; Maintenance Access; Grading/Site Drainage/Spill Containment; Structural/Foundations/Supports | `PACKAGE_REGISTER.csv` row 43 |

## Verification

| Requirement | Verification Method |
|---|---|
| R-1 (Index) | Document review against source's Core vendor documents list; index completeness check by EPC Integrator (`DEL-041-06`). |
| R-2 (Control Procedure) | Review of `DOC-008` against EPC document-control expectations. |
| R-3, R-7, R-8 (Core/quality/logistics) | Checklist verification at submittal milestones and at final turnover. |
| R-4, R-5, R-6 (Discipline applicability) | Per-line applicability disposition recorded on Vendor Document Index; reviewed in `DEL-041-06`. |
| R-9 (FAT/SAT) | Receipt of signed FAT report (`MEC-022`) and `ELE-030` energization package prior to acceptance. |
| R-10 (As-built and turnover books) | Receipt of `PRQ-016` and discipline final books; cross-check against ITP closure. |
| R-11 (Standards) | Each engineered document cites governing standards; standards list reviewed during `DEL-041-06`. |
| R-12 (Cadence / native files) | TBD — specify in package PO/contract prior to vendor mobilization. |
| R-13 (Voltage/rating reconciliation) | EPC Integrator reconciles package title vs. as-engineered rating in `DEL-041-06`; document register annotated accordingly. |

## Documentation

The artifacts produced under this deliverable are themselves documents. The deliverable folder will record:

- A package-specific Vendor Document Index instance (or pointer) when issued by the vendor.
- Transmittal records and disposition log for each submittal cycle.
- Final turnover book(s).
- Anticipated artifacts per `_CONTEXT.md`:
  - Vendor document register
  - Vendor document submittals
  - Source vendor document table rows as artifacts where available
  - Turnover records
