# Specification — DEL-019-05 Vendor Document Turnover Package (PKG-019)

## Scope

### In scope
- The complete vendor document set required for the PKG-019 MV VFD package, organized in a Vendor Document Index (`PRQ-009`) and controlled per the Vendor Document Control Procedure (`DOC-008`).
- All "Core vendor documents" enumerated in `_Sources/26020-Package_Requirements.docx` ("Vendor Engineering Deliverables" section).
- The discipline-applicable engineering and design documents required for a Medium-Voltage Variable Frequency Drive package (Electrical lead with I&C; mechanical/structural where the VFD is delivered as an enclosed lineup or skid).
- Vendor quality records: Supplier Quality Plan, ITP, MTRs/Certificates, Inspection Release Certificate, Manufacturing Record Book / VDB (`QLT-006`, `QLT-003`, `QLT-013`, `QLT-020`, `QLT-021`).
- Logistics records: Shipping Plan (`PRQ-013`), SPIR (`PRQ-015`).
- Final/turnover books: `PRQ-016` and discipline final books (e.g., `MEC-023`, `ELE-030` energization package).
- Source vendor document table rows themselves (as artifacts/evidence) referenced from the index.

### Out of scope
- Production of the engineered equipment package itself (covered by `DEL-019-04`).
- EPC Integrator review and acceptance of the submitted documents (covered by `DEL-019-06`).
- Construction tie-in and turnover into the larger facility (covered by `DEL-019-03`).

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
The set shall include the Electrical and I&C document classes applicable to a Medium-Voltage VFD package per source's discipline tables:
- Electrical: `ELE-002`, `ELE-003`, `ELE-011` (Motor Starting Study), `ELE-012`, `ELE-014`, `ELE-015`, `ELE-016`, `ELE-017` (if integral lighting), `ELE-019`, `ELE-020`, `ELE-027`, `ELE-028`, `ELE-029`, `ELE-030`.
- I&C: `INS-002`, `INS-003`, `INS-005`, `INS-006`, `INS-008`, `INS-009`, and the remaining INS entries enumerated in the source list.
- Source: `_Sources/26020-Package_Requirements.docx` — "Electrical, lighting, EHT, grounding" and "Instrumentation and controls interfaces".
- ASSUMPTION: All INS entries listed in the source are applicable; the EPC Integrator confirms the per-line applicability call during `DEL-019-06` review.

### R-5 Discipline applicability (Mechanical / structural)
The set shall include mechanical equipment data documents for the VFD as a packaged equipment item: `MEC-001`, `MEC-002`, `MEC-003`, `MEC-006`, `MEC-016`, `MEC-017`, `MEC-018`, `MEC-021`, `MEC-022`, `MEC-023`, `MEC-024`, `MEC-025`.
- ASSUMPTION: The VFD is delivered as an enclosed cabinet lineup or skid with mechanical handling/installation requirements; the source treats packaged equipment uniformly under this template.
- Source: `_Sources/26020-Package_Requirements.docx` — "Core package engineering" and "Mechanical Equipment IOM Manual" rows.

### R-6 Pressure / piping / civil applicability
Pressure-equipment, piping, civil/foundation, and process documents are presumed NOT APPLICABLE for a power-electronics VFD package and may be omitted from the turnover set, unless detailed-design discovery shows otherwise (e.g., cooling-water piping, oil cooling, integral civil pad).
- Disposition status: PROPOSAL — EPC Integrator confirms during `DEL-019-06` review. Mark on the Vendor Document Index as N/A with rationale.

### R-7 Quality records and traceability
The Package Vendor shall provide:
- Supplier Quality Plan (`QLT-006`),
- Inspection and Test Plan (`QLT-003`) with hold/witness points,
- Material Test Reports / Certificates (`QLT-013`),
- Inspection Release Certificate (`QLT-020`),
- Manufacturing Record Book / Vendor Data Book (`QLT-021`).
- Source: `_Sources/26020-Package_Requirements.docx` — "Core vendor documents".

### R-8 Logistics and spares
The Package Vendor shall provide a Logistics / Shipping Plan (`PRQ-013`) and a Spare Parts Interchangeability Record (`PRQ-015`).
- Source: same as R-7.

### R-9 FAT/SAT records
The Package Vendor shall provide FAT and energization records: `MEC-021`/`MEC-022` (mechanical FAT procedure/report where applicable) and `ELE-029`/`ELE-030` (electrical FAT/SAT procedure and energization package).
- Source: `_Sources/26020-Package_Requirements.docx`.

### R-10 As-built and turnover books
The Package Vendor shall deliver `PRQ-016` Vendor Data Book / Final Supplier Documentation and discipline final books (e.g., `MEC-023`); the EPC Integrator integrates these into the package turnover record. As-built electrical and instrumentation drawings shall be issued.
- Source: same as R-9.

### R-11 Standards compliance traceability
Each vendor-supplied document subject to industry codes/standards shall reference the governing standard. For motor/VFD systems, the DBM cites NEMA MG1 compliance for the driven motor; VFD-specific governing standards (e.g., IEEE 519 harmonics, NEMA ICS 7 / IEC 61800 series) are not explicitly cited in the accessible source set.
- Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 324, 326, 533, 756.
- ASSUMPTION: Industry-standard VFD electrical codes apply; specific clauses are TBD until detailed-design specifications are issued.

### R-12 Submittal cadence and native files
- Submittal cadence (preliminary / certified / as-built): TBD — not stated in accessible source slices.
- Native file format requirements (e.g., CAD format, electronic transmittal): TBD — not stated in accessible source slices.

## Standards

| Standard | Applicability | Location |
|---|---|---|
| NEMA MG1 | Driven motor (cited in DBM) | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 324 |
| API 661 (modified) | Air-cooled heat exchanger (cited for compressor package; applicability to PKG-019 VFD-only scope: not applicable unless cooling provided) | `_Sources/26020-Package_Requirements.docx` Acid Gas Compressor section |
| IEEE 519, NEMA ICS 7, IEC 61800 (VFDs) | ASSUMPTION; not explicitly cited in accessible source set | location TBD |
| CSA / electrical area classification standards | ASSUMPTION; site-electrical detailed design dependency | location TBD |

## Verification

| Requirement | Verification Method |
|---|---|
| R-1 (Index) | Document review against source's Core vendor documents list; index completeness check by EPC Integrator (`DEL-019-06`). |
| R-2 (Control Procedure) | Review of `DOC-008` against EPC document-control expectations. |
| R-3, R-7, R-8 (Core/quality/logistics) | Checklist verification at submittal milestones and at final turnover. |
| R-4, R-5 (Discipline applicability) | Per-line applicability disposition recorded on Vendor Document Index; reviewed in `DEL-019-06`. |
| R-6 (Civil/piping not applicable) | Recorded as N/A with rationale on the Index; reviewed in `DEL-019-06`. |
| R-9 (FAT/SAT) | Receipt of signed FAT report (`MEC-022` if applicable, `ELE-030` energization package) prior to acceptance. |
| R-10 (As-built and turnover books) | Receipt of `PRQ-016` and discipline final books; cross-check against ITP closure. |
| R-11 (Standards) | Each engineered document cites governing standards; standards list reviewed during `DEL-019-06`. |
| R-12 (Cadence / native files) | TBD — specify in package PO/contract prior to vendor mobilization. |

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
