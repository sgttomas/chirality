# Specification — DEL-075-05 Vendor Document Turnover Package (PKG-075)

## Scope

### In scope
- The complete vendor document set required for the PKG-075 Cryogenic Unit ("Deepcut") package, organized in a Vendor Document Index (`PRQ-009`) and controlled per the Vendor Document Control Procedure (`DOC-008`).
- All "Core vendor documents" enumerated in `_Sources/26020-Package_Requirements.docx` ("Vendor Engineering Deliverables" section, package heading 29 — Cryogenic Unit).
- The discipline-applicable engineering and design documents required for a sour-service cryogenic deep-cut propane-plus recovery package (Mechanical lead with Process, Piping/Pressure, Relief/Flare/Vent, Drain/Containment, Electrical, I&C, F&G, Civil/Structural, and HVAC where applicable).
- Vendor quality records: Supplier Quality Plan, ITP, MTRs/Certificates, Inspection Release Certificate, Manufacturing Record Book / VDB (`QLT-006`, `QLT-003`, `QLT-013`, `QLT-020`, `QLT-021`).
- Logistics records: Shipping Plan (`PRQ-013`), SPIR (`PRQ-015`).
- Final/turnover books: `PRQ-016` Vendor Data Book / Final Supplier Documentation and discipline final books (e.g., `MEC-023`, `ELE-030` energization package).
- Source vendor document table rows themselves (as artifacts/evidence) referenced from the index, where available.

### Out of scope
- Production of the engineered equipment package itself (covered by `DEL-075-04`).
- EPC Integrator review and acceptance of the submitted documents (covered by `DEL-075-06` — ASSUMPTION based on package-internal numbering convention used across the other DEL-XX-05 vendor-document-turnover deliverables).
- Construction tie-in and turnover into the larger facility (covered by `DEL-075-03`).
- Authoring the EPC Scope of Work (`DEL-075-01`) and the EPC Package Datasheet (`DEL-075-02`).

## Requirements

### R-1 Vendor Document Index
The Package Vendor shall provide a Vendor Document Index (`PRQ-009`) listing every document in the turnover set with document number, revision, status, and submittal/return cycle status.
- Source: `_Sources/26020-Package_Requirements.docx` — "Vendor Engineering Deliverables / Core vendor documents" (location TBD at clause level).

### R-2 Vendor Document Control Procedure
The Package Vendor shall provide a Document Control Procedure (`DOC-008`) describing numbering, revisioning, transmittal mechanics, and review-cycle handling.
- Source: same as R-1.

### R-3 Core vendor documents
The set shall include all "Core vendor documents" listed in `_Sources/26020-Package_Requirements.docx`:
`PRQ-009`, `DOC-008`, `QLT-006`, `QLT-003`, `QLT-013`, `QLT-020`, `QLT-021`, `PRQ-013`, `PRQ-015`, `PRQ-016`.

### R-4 Discipline applicability (Process / Mechanical / Pressure / Piping)
The set shall include process, mechanical equipment, pressure-equipment, and piping document classes per the source template:
- Mechanical Equipment: `MEC-001`, `MEC-002`, `MEC-003`, `MEC-006`, `MEC-016`, `MEC-017`, `MEC-018`, `MEC-021`, `MEC-022`, `MEC-023`, `MEC-024`, `MEC-025`.
- Pressure Equipment (PV/columns/exchangers): per source IDs (e.g., `PV-xxx`/`PIP-xxx` ranges defined in the template — specific IDs and clause locations TBD).
- Piping (process and utility): per source IDs (TBD per source clause).
- Source: `_Sources/26020-Package_Requirements.docx` — discipline tables for piping, pressure equipment, and mechanical equipment.
- ASSUMPTION: All MEC/PIP/PV lines listed in the source template are applicable to a sour-service cryogenic deep-cut package; the EPC Integrator confirms per-line applicability during `DEL-075-06` review.

### R-5 Discipline applicability (Relief / Flare / Vent / Drain / Containment)
The set shall include relief-device data, flare load tabulations, and drain/containment documents for the cryogenic relief network. Cryogenic flare rates and incinerator rates are preliminary at the DBM and are to be confirmed during detailed engineering by the flare stack vendor.
- Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2186, 2294; `_Sources/26020-Package_Requirements.docx` (Relief/Flare/Vent rows).

### R-6 Discipline applicability (Electrical and I&C)
The set shall include the Electrical and I&C document classes applicable to an electrified, instrumented cryogenic process package:
- Electrical: `ELE-002`, `ELE-003`, `ELE-014`, `ELE-015`, `ELE-016`, `ELE-020`, `ELE-027`, `ELE-028`, `ELE-029`, `ELE-030`.
- I&C: `INS-002`, `INS-003`, `INS-005`, `INS-006`, `INS-008`, `INS-009`, and remaining INS line items per source.
- Source: `_Sources/26020-Package_Requirements.docx` — "Electrical, lighting, EHT, grounding" and "Instrumentation and controls interfaces" rows.
- ASSUMPTION: All INS/ELE lines listed in the source template apply at the package level; EPC Integrator confirms in `DEL-075-06`.

### R-7 Discipline applicability (Civil / Structural / HVAC)
The set shall include structural-foundation, support-steel, and where vendor-supplied enclosures are included, HVAC/building-services documents. Per `PACKAGE_REGISTER.csv` row 52 the applicable interfaces include Structural / Foundations / Supports, Maintenance Access, and Building HVAC / Services.
- Source: `_Sources/26020-Package_Requirements.docx`; `PACKAGE_REGISTER.csv` row 52.

### R-8 Discipline applicability (Fire & Gas / Safety Systems)
The set shall include vendor F&G device data, ESD interface documentation, and area-classification confirmations for sour cryogenic service.
- Source: `PACKAGE_REGISTER.csv` row 52 (Fire & Gas / Safety Systems interface). Detailed clause-level F&G requirements: location TBD in `_Sources/26020-Package_Requirements.docx`.

### R-9 Quality records and traceability
The Package Vendor shall provide:
- Supplier Quality Plan (`QLT-006`),
- Inspection and Test Plan (`QLT-003`) with hold/witness points,
- Material Test Reports / Certificates (`QLT-013`) — pressure boundary materials in sour cryogenic service require traceability,
- Inspection Release Certificate (`QLT-020`),
- Manufacturing Record Book / Vendor Data Book (`QLT-021`).
- Source: `_Sources/26020-Package_Requirements.docx` — "Core vendor documents".

### R-10 Logistics and spares
The Package Vendor shall provide a Logistics / Shipping Plan (`PRQ-013`) and a Spare Parts Interchangeability Record (`PRQ-015`).
- Source: same as R-9.

### R-11 FAT/SAT and energization records
The Package Vendor shall provide FAT and energization records: `MEC-021` / `MEC-022` (mechanical FAT procedure/report) and `ELE-029` / `ELE-030` (electrical FAT/SAT procedure and energization package).
- Source: `_Sources/26020-Package_Requirements.docx`.

### R-12 As-built and turnover books
The Package Vendor shall deliver `PRQ-016` Vendor Data Book / Final Supplier Documentation and discipline final books (e.g., `MEC-023`); the EPC Integrator integrates these into the package turnover record. As-built process, mechanical, piping, electrical, and instrumentation drawings shall be issued.
- Source: same as R-11.

### R-13 Standards compliance traceability
Each vendor-supplied document subject to industry codes/standards shall reference the governing standard. Specific governing standards for cryogenic deep-cut process equipment (e.g., ASME B31.3, ASME BPVC Section VIII, API 660/661, API 521, CSA Z662, BC OGC requirements) are not explicitly cited clause-by-clause in the accessible source slices.
- Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` SEC for regulatory basis (BC Energy Regulator); `_Sources/26020-Package_Requirements.docx` (codes-and-standards register location TBD).
- ASSUMPTION: Standard sour-service, cryogenic-service, pressure-vessel, piping, and Canadian regulatory codes apply; specific clauses are TBD until detailed-design specifications are issued.

### R-14 Submittal cadence and native files
- Submittal cadence (preliminary / certified / as-built): TBD — not stated in accessible source slices.
- Native file format requirements (e.g., CAD format, electronic transmittal): TBD — not stated in accessible source slices.

## Standards

| Standard | Applicability | Location |
|---|---|---|
| BC Energy Regulator requirements | Facility-level regulatory basis (cited in DBM SEC on regulatory/permitting) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-near line 3320 |
| ASME B31.3, ASME BPVC Section VIII | Process piping and pressure vessels (ASSUMPTION — not explicitly cited in accessible source set) | location TBD |
| API 521, API 660/661 | Relief, heat exchangers (ASSUMPTION) | location TBD |
| CSA Z662 | Pipeline tie-ins (ASSUMPTION) | location TBD |
| Cryogenic / sour-service material standards | Applicable to PV/PIP/MEC documents (ASSUMPTION) | location TBD |

## Verification

| Requirement | Verification Method |
|---|---|
| R-1 (Index) | Document review against source's Core vendor documents list; index completeness check by EPC Integrator (`DEL-075-06`). |
| R-2 (Control Procedure) | Review of `DOC-008` against EPC document-control expectations. |
| R-3, R-9, R-10 (Core/quality/logistics) | Checklist verification at submittal milestones and at final turnover. |
| R-4 through R-8 (Discipline applicability) | Per-line applicability disposition recorded on Vendor Document Index; reviewed in `DEL-075-06`. |
| R-11 (FAT/SAT) | Receipt of signed FAT report (`MEC-022`) and electrical energization package (`ELE-030`) prior to acceptance. |
| R-12 (As-built and turnover books) | Receipt of `PRQ-016` and discipline final books; cross-check against ITP closure. |
| R-13 (Standards) | Each engineered document cites governing standards; standards list reviewed during `DEL-075-06`. |
| R-14 (Cadence / native files) | TBD — specify in package PO/contract prior to vendor mobilization. |

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
