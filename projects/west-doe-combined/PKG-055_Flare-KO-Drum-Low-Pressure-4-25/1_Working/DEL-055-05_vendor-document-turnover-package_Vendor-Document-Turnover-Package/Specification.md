# Specification — DEL-055-05 Vendor Document Turnover Package (PKG-055)

## Scope

### In scope
- The complete vendor document set required for the PKG-055 LP Flare KO Drum package (one LP flare KO drum V-3900-1 and one LP KO drum transfer pump P-3900-1, shop-built as Module 390-1 per the 4-25 module list), organized in a Vendor Document Index (`PRQ-009`) and controlled per the Vendor Document Control Procedure (`DOC-008`).
- All "Core vendor documents" enumerated in `_Sources/26020-Package_Requirements.docx` ("Vendor Engineering Deliverables" section; location TBD pending text access).
- The discipline-applicable engineering and design documents required for a Mechanical pressure-vessel + transfer-pump package, with associated electrical motor data, instrumentation, and structural documents for the supplied skid/saddle.
- Vendor quality records: Supplier Quality Plan, ITP, MTRs/Certificates, Inspection Release Certificate, Manufacturing Record Book / VDB (`QLT-006`, `QLT-003`, `QLT-013`, `QLT-020`, `QLT-021`).
- Logistics records: Shipping Plan (`PRQ-013`), SPIR (`PRQ-015`).
- Final/turnover books: `PRQ-016` and discipline final book(s) (e.g., `MEC-023`).
- Source vendor document table rows (as artifacts/evidence) referenced from the index.

### Out of scope
- Production of the engineered equipment package itself (covered by `DEL-055-04`).
- EPC Integrator review and acceptance of the submitted documents (covered by `DEL-055-06`).
- EPC Scope of Work and Package Datasheet (covered by `DEL-055-01` and `DEL-055-02`).
- Construction work-package execution and physical tie-in into the facility (covered by `DEL-055-03`).

## Requirements

### R-1 Vendor Document Index
The Package Vendor shall provide a Vendor Document Index (`PRQ-009`) listing every document in the turnover set with document number, revision, status, and submittal/return cycle status.
- Source: `_Sources/26020-Package_Requirements.docx` — "Vendor Engineering Deliverables / Core vendor documents" (location TBD).

### R-2 Vendor Document Control Procedure
The Package Vendor shall provide a Document Control Procedure (`DOC-008`) describing numbering, revisioning, transmittal mechanics, and review-cycle handling.
- Source: same as R-1.

### R-3 Core vendor documents
The set shall include all "Core vendor documents":
`PRQ-009`, `DOC-008`, `QLT-006`, `QLT-003`, `QLT-013`, `QLT-020`, `QLT-021`, `PRQ-013`, `PRQ-015`, `PRQ-016`.
- Source: `_Sources/26020-Package_Requirements.docx` (location TBD).

### R-4 Discipline applicability (Mechanical — pressure vessel)
The set shall include mechanical / pressure-vessel document classes for the LP KO drum (V-3900-1):
- Code calculations and design (vessel design report, nozzle schedule, weight/CG, lifting/transport drawings).
- IOM manual (`MEC-023` equivalent).
- General arrangement, foundation loads, anchor-bolt details for vessel saddles.
- Source: `_Sources/26020-Package_Requirements.docx` — "Mechanical Equipment IOM Manual" / pressure-vessel template rows (location TBD).
- ASSUMPTION: LP KO drum is an ASME Section VIII Division 1 pressure vessel (LP service); specific code stamp and Division to be confirmed against package datasheet `DEL-055-02` and vendor proposal.

### R-5 Discipline applicability (Mechanical — rotating equipment: transfer pump)
The set shall include rotating-equipment data documents for the LP KO drum transfer pump (P-3900-1): `MEC-001`, `MEC-002`, `MEC-003`, `MEC-006`, `MEC-016`, `MEC-017`, `MEC-018`, `MEC-021`, `MEC-022`, `MEC-024`, `MEC-025` (ASSUMPTION: same MEC IDs used by sibling DEL-081-05 derived from the common template).
- ASSUMPTION: Transfer pump is a centrifugal or positive-displacement pump with associated motor; specific API code (e.g., API 610 / API 676) applicability TBD until detailed design.

### R-6 Electrical and I&C applicability (motor, instruments, controls)
The set shall include the Electrical and I&C document classes applicable to the transfer-pump motor and the KO drum instrumentation (level, pressure, temperature, level-trip):
- Electrical (motor data, area-classification certificates, grounding/bonding): `ELE-*` IDs as applicable (ASSUMPTION; per-line call in `DEL-055-06`).
- I&C (instruments, control schematics, alarm/trip schedules, junction box drawings): `INS-*` IDs as applicable (ASSUMPTION).
- Source: `_Sources/26020-Package_Requirements.docx` — "Electrical, lighting, EHT, grounding" and "Instrumentation and controls interfaces" (location TBD).

### R-7 Process piping / relief / drain interface documentation
The set shall include vendor scope-of-supply termination drawings and data for the package interfaces typical of a flare KO drum module: Process Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Maintenance Access; Structural / Foundations / Supports.
- ASSUMPTION: Vendor scope ends at the package skirt/skid edge; piping beyond that point is EPC Integrator scope. Confirm boundary in `DEL-055-01` / `DEL-055-02`.
- Specific interface line items for PKG-055 are TBD pending text extraction of `_Sources/26020-Packages_Interfaces_4_export.xlsx` row 57.

### R-8 Quality records and traceability
The Package Vendor shall provide:
- Supplier Quality Plan (`QLT-006`),
- Inspection and Test Plan (`QLT-003`) with hold/witness points (including ASME inspection points for the pressure vessel and hydrostatic test),
- Material Test Reports / Certificates (`QLT-013`),
- Inspection Release Certificate (`QLT-020`),
- Manufacturing Record Book / Vendor Data Book (`QLT-021`) — including the vessel U-1A / Data Report for the ASME-stamped vessel (ASSUMPTION).
- Source: `_Sources/26020-Package_Requirements.docx` — "Core vendor documents" (location TBD).

### R-9 Logistics and spares
The Package Vendor shall provide a Logistics / Shipping Plan (`PRQ-013`) and a Spare Parts Interchangeability Record (`PRQ-015`). The Shipping Plan shall identify lift points, transport orientation, and field-handling restrictions for the shop-built module (Module 390-1) including the pressure vessel and pump skid.
- Source: same as R-8.

### R-10 FAT / acceptance records
The Package Vendor shall provide FAT records appropriate to the package scope:
- Pressure-vessel hydrostatic test record (per ASME); MTRs and weld NDE records (`QLT-013`).
- Pump performance test report (`MEC-022` equivalent) per applicable API code (ASSUMPTION: API 610 or 676 depending on pump type).
- Module FAT report covering the integrated 390-1 LP Flare KO Drum Module (ASSUMPTION; consistent with shop-built modularization basis).
- Source: `_Sources/26020-Package_Requirements.docx` (location TBD).

### R-11 As-built and turnover books
The Package Vendor shall deliver `PRQ-016` Vendor Data Book / Final Supplier Documentation and the mechanical final book `MEC-023`; the EPC Integrator integrates these into the package turnover record via `DEL-055-06`. As-built drawings (general arrangement, P&ID interface points, foundation loads) shall be issued at the as-built revision.
- Source: same as R-10.

### R-12 Standards compliance traceability
Each vendor-supplied document subject to industry codes/standards shall reference the governing standard. For an LP Flare KO Drum + transfer pump package, the likely applicable standard set includes:

| Standard | Applicability |
|---|---|
| ASME BPVC Section VIII Div. 1 | Pressure vessel design and stamping (ASSUMPTION; not explicitly cited in accessible source slices) |
| API 521 / API STD 521 | Pressure-relieving and depressuring systems (sets flare-system functional context); ASSUMPTION |
| API 537 | Flare details and general refinery and petrochemical service (parent flare-stack context); ASSUMPTION |
| API 610 / API 676 | Centrifugal / rotary positive-displacement pumps (whichever is applicable to the transfer pump); ASSUMPTION |
| ASME B31.3 | Process piping for vendor scope-of-supply piping; ASSUMPTION |
| NEMA MG1 | Driven motor for the transfer pump; ASSUMPTION at the PKG-055 line |
| CSA / electrical area classification | Site cold-climate basis (DBM); ASSUMPTION |

- Specific standard clauses, edition years, and code-stamp details are TBD until detailed-design specifications and vendor proposals are issued.

### R-13 Submittal cadence and native files
- Submittal cadence (preliminary / certified / as-built): TBD — not stated in accessible source slices.
- Native file format requirements (e.g., CAD format, electronic transmittal, 3D model deliverables): TBD — not stated in accessible source slices.

## Standards

| Standard | Applicability | Location |
|---|---|---|
| ASME BPVC Section VIII | LP KO drum pressure-vessel design | location TBD (ASSUMPTION) |
| API 521 | Pressure-relieving and depressuring systems context | location TBD (ASSUMPTION) |
| API 537 | Flare system context | location TBD (ASSUMPTION) |
| API 610 / API 676 | Transfer-pump design and test | location TBD (ASSUMPTION) |
| ASME B31.3 | Vendor scope-of-supply process piping | location TBD (ASSUMPTION) |
| NEMA MG1 | Transfer-pump driver motor | location TBD (ASSUMPTION) |
| CSA / Electrical area classification | Site-electrical detailed design dependency | location TBD (ASSUMPTION) |

## Verification

| Requirement | Verification Method |
|---|---|
| R-1 (Index) | Document review against source's Core vendor documents list; index completeness check by EPC Integrator (`DEL-055-06`). |
| R-2 (Control Procedure) | Review of `DOC-008` against EPC document-control expectations. |
| R-3, R-8, R-9 (Core/quality/logistics) | Checklist verification at submittal milestones and at final turnover. |
| R-4, R-5, R-6, R-7 (Discipline applicability and interfaces) | Per-line APPLICABLE / N/A disposition recorded on Vendor Document Index; reviewed in `DEL-055-06`. |
| R-10 (FAT records) | Receipt of signed hydrostatic test certificate (per ASME); receipt of pump performance test report (per applicable API); receipt of module FAT report. |
| R-11 (As-built and turnover books) | Receipt of `PRQ-016` and `MEC-023`; cross-check against ITP closure. |
| R-12 (Standards) | Each engineered document cites governing standards; standards list reviewed during `DEL-055-06`. |
| R-13 (Cadence / native files) | TBD — specify in package PO/contract prior to vendor mobilization. |

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
