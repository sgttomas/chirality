# Specification — DEL-058-05 Vendor Document Turnover Package (PKG-058)

## Scope

### In scope
- The complete vendor document set required for the PKG-058 Medium Pressure Flash Feed Separator (MPFF) package, organized in a Vendor Document Index (`PRQ-009`) and controlled per the Vendor Document Control Procedure (`DOC-008`).
- All "Core vendor documents" enumerated in `_Sources/26020-Package_Requirements.docx` ("Vendor Engineering Deliverables").
- Discipline-applicable engineering and design documents for a mechanical packaged separator: pressure-vessel/code-vessel data, mechanical equipment IOM and FAT records, skid piping and supports, instrumentation and controls, electrical/lighting for the enclosure, civil/structural interface data.
- Vendor quality records: `QLT-006`, `QLT-003`, `QLT-013`, `QLT-020`, `QLT-021`.
- Logistics records: `PRQ-013`, `PRQ-015`.
- Final/turnover books: `PRQ-016` and discipline final books (e.g., `MEC-023`).
- Source vendor document table rows themselves (as artifacts/evidence) referenced from the index per `_CONTEXT.md`.

### Out of scope
- Production of the engineered equipment package itself (covered by `DEL-058-04`).
- EPC Integrator review and acceptance of the submitted documents (covered by `DEL-058-06`).
- Construction tie-in and turnover into the larger facility (covered by `DEL-058-03`).
- Package datasheet authorship (covered by `DEL-058-02`); the vendor documentation set carries vendor-issued data and may reference the EPC datasheet but does not replace it.

## Requirements

### R-1 Vendor Document Index
The Package Vendor shall provide a Vendor Document Index (`PRQ-009`) listing every document in the turnover set with document number, revision, status, applicability disposition, and submittal/return cycle status.
- Source: `_Sources/26020-Package_Requirements.docx` — "Vendor Engineering Deliverables / Core vendor documents".

### R-2 Vendor Document Control Procedure
The Package Vendor shall provide a Document Control Procedure (`DOC-008`) describing numbering, revisioning, transmittal mechanics, named submittal milestones, and review-cycle handling.
- Source: same as R-1.

### R-3 Core vendor documents
The set shall include all "Core vendor documents" listed in `_Sources/26020-Package_Requirements.docx`:
`PRQ-009`, `DOC-008`, `QLT-006`, `QLT-003`, `QLT-013`, `QLT-020`, `QLT-021`, `PRQ-013`, `PRQ-015`, `PRQ-016`.

### R-4 Discipline applicability (Mechanical / pressure equipment)
The set shall include mechanical equipment data documents for the MPFF as a packaged pressure-vessel item: `MEC-001`, `MEC-002`, `MEC-003`, `MEC-006`, `MEC-016`, `MEC-017`, `MEC-018`, `MEC-021`, `MEC-022`, `MEC-023`, `MEC-024`, `MEC-025`.
- The package vendor shall additionally supply pressure-vessel code-compliance documentation (vessel datasheet, design calculations, NDE reports, hydrotest records, manufacturer data report or jurisdictional equivalent) appropriate to the governing pressure-vessel code.
- ASSUMPTION: governing pressure-vessel code is ASME BPVC Section VIII Div. 1 unless detailed engineering selects another jurisdictional code; clause-level claim TBD until source slice is accepted.
- Source: `_Sources/26020-Package_Requirements.docx` — "Core package engineering" and "Mechanical Equipment IOM Manual" rows.

### R-5 Discipline applicability (Instrumentation and Controls)
The set shall include I&C documentation for level control, inlet pressure control, overhead vapour PCV to SOC third-stage suction, automated blowdown valve, and methanol-injection instrumentation: `INS-002`, `INS-003`, `INS-005`, `INS-006`, `INS-008`, `INS-009`, and the remaining INS line items enumerated in the source list.
- Source: `_Sources/26020-Package_Requirements.docx` — "Instrumentation and controls interfaces"; process-basis triggers for the controls listed in `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 672, 674.
- ASSUMPTION: full INS line set is applicable; EPC Integrator confirms per-line during `DEL-058-06`.

### R-6 Discipline applicability (Electrical / lighting / grounding)
The set shall include electrical/lighting/grounding documentation supporting the self-framing building enclosure and instrumentation power: `ELE-002`, `ELE-003`, `ELE-014`, `ELE-015`, `ELE-016`, `ELE-017` (lighting if integral), `ELE-019`, `ELE-020`, `ELE-027`, `ELE-028`, `ELE-029`, `ELE-030`.
- Source: `_Sources/26020-Package_Requirements.docx` — "Electrical, lighting, EHT, grounding"; enclosure basis in `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 672.
- ASSUMPTION: scope limited to the building enclosure and instrumentation; no medium-voltage motor scope.

### R-7 Discipline applicability (Piping / structural / civil interface)
The set shall include skid-edge piping documentation (isometrics, line lists for vendor-scope piping, supports), structural/skid steel documentation (drawings, calculations, anchor-bolt details), and the vendor-supplied loads/loadings package required for the civil/foundation interface.
- Per-line source IDs TBD until the Vendor Engineering Deliverables list is re-read against the package heading at production time.
- Source: `_Sources/26020-Package_Requirements.docx` — piping, structural, and civil interface sections.

### R-8 Quality records and traceability
The Package Vendor shall provide:
- Supplier Quality Plan (`QLT-006`),
- Inspection and Test Plan (`QLT-003`) with hold/witness points (including hydrotest, NDE, mechanical FAT),
- Material Test Reports / Certificates (`QLT-013`) for pressure parts and internals,
- Inspection Release Certificate (`QLT-020`),
- Manufacturing Record Book / Vendor Data Book (`QLT-021`).
- Source: `_Sources/26020-Package_Requirements.docx` — "Core vendor documents".

### R-9 Logistics and spares
The Package Vendor shall provide a Logistics / Shipping Plan (`PRQ-013`) and a Spare Parts Interchangeability Record (`PRQ-015`).
- Source: same as R-8.

### R-10 FAT records
The Package Vendor shall provide mechanical FAT and performance test records (`MEC-021` procedure, `MEC-022` report) for the MPFF vessel and skid. Electrical FAT records (`ELE-029`/`ELE-030`) shall apply to the enclosure electrical scope where applicable.
- Source: `_Sources/26020-Package_Requirements.docx`.

### R-11 As-built and turnover books
The Package Vendor shall deliver `PRQ-016` Vendor Data Book / Final Supplier Documentation and `MEC-023` Mechanical Final Documentation; the EPC Integrator integrates these into the package turnover record via `DEL-058-06`. As-built mechanical, piping, instrumentation, and electrical drawings shall be issued at turnover.
- Source: same as R-10.

### R-12 Process-basis traceability
Vendor documentation describing process functions of the MPFF (overheads to SOC, automated blowdown, internals, methanol injection, enclosure) shall remain consistent with the facility design basis. The vendor documentation set shall not contradict the DBM-cited functional configuration without an explicit deviation record routed through `DEL-058-06`.
- Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 668, 672, 674.

### R-13 Standards compliance traceability
Each vendor-supplied document subject to industry codes/standards shall reference the governing standard. Specific standards governing the MPFF (e.g., ASME BPVC Sec. VIII Div. 1, ASME B31.3 for piping, applicable Canadian jurisdictional codes for cold-climate site) are not explicitly cited in the locally accessible source slices and shall be confirmed during detailed engineering.
- ASSUMPTION: ASME BPVC Sec. VIII Div. 1 and ASME B31.3 likely applicable; clause-level claims TBD.
- Specific source clause: `location TBD`.

### R-14 Submittal cadence and native files
- Submittal cadence (preliminary / certified-for-construction / as-built): TBD — not stated in accessible source slices.
- Native file format requirements (e.g., CAD format, electronic transmittal): TBD — not stated in accessible source slices.

## Standards

| Standard | Applicability | Location |
|---|---|---|
| ASME BPVC Sec. VIII Div. 1 | Pressure-vessel design and certification for MPFF vessel | ASSUMPTION; location TBD |
| ASME B31.3 | Process piping at skid edge and within vendor scope | ASSUMPTION; location TBD |
| Canadian jurisdictional pressure-equipment registration (e.g., ABSA in Alberta) | Pressure-vessel registration for cold-climate site | ASSUMPTION; location TBD |
| CSA / electrical area classification standards | Enclosure electrical, lighting, grounding | ASSUMPTION; location TBD |
| Industry mist-eliminator/coalescer guidance | MPFF internals (Mistex per DBM) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 672 (vendor-named internals; standards location TBD) |

## Verification

| Requirement | Verification Method |
|---|---|
| R-1 (Index) | Document review against source's Core vendor documents list and applicability disposition for MPFF; index completeness check by EPC Integrator (`DEL-058-06`). |
| R-2 (Control Procedure) | Review of `DOC-008` against EPC document-control expectations. |
| R-3, R-8, R-9 (Core/quality/logistics) | Checklist verification at submittal milestones and at final turnover. |
| R-4 (Mechanical / pressure equipment) | Review of vessel datasheet, design calculations, NDE reports, hydrotest record, MDR; cross-check that pressure-vessel certification matches PO. |
| R-5 (I&C) | Per-line applicability disposition on Vendor Document Index; confirm controls aligned to MPFF process functions per R-12. |
| R-6 (Electrical) | Per-line applicability disposition on Index; review for enclosure scope only. |
| R-7 (Piping / structural / civil interface) | Receipt of skid-edge isometrics, structural drawings/calcs, civil loadings package; reviewed by EPC piping/structural/civil in `DEL-058-06`. |
| R-10 (FAT) | Receipt of signed mechanical FAT report (`MEC-022`) and applicable electrical FAT/energization records. |
| R-11 (As-built and turnover books) | Receipt of `PRQ-016` and `MEC-023`; cross-check against ITP closure. |
| R-12 (Process-basis traceability) | Cross-read of vendor documents against DBM lines 668, 672, 674; deviations recorded. |
| R-13 (Standards) | Each engineered document cites governing standards; standards list reviewed during `DEL-058-06`. |
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
