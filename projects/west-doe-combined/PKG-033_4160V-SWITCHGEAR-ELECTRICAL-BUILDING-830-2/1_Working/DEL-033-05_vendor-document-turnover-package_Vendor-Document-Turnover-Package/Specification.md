# Specification — DEL-033-05 Vendor Document Turnover Package (PKG-033)

## Scope

### In scope
- The complete vendor document set required for the PKG-033 4160V Switchgear Electrical Building (830-2) package, organized in a Vendor Document Index (`PRQ-009`) and controlled per the Vendor Document Control Procedure (`DOC-008`).
- All "Core vendor documents" enumerated in `_Sources/26020-Package_Requirements.docx` ("Vendor Engineering Deliverables" section).
- The discipline-applicable engineering and design documents required for a medium-voltage (4,160 V) switchgear lineup housed inside a vendor-supplied electrical building (Electrical lead with I&C; mechanical/structural/HVAC for the building enclosure and integral services).
- Vendor quality records: Supplier Quality Plan, ITP, MTRs/Certificates, Inspection Release Certificate, Manufacturing Record Book / VDB (`QLT-006`, `QLT-003`, `QLT-013`, `QLT-020`, `QLT-021`).
- Logistics records: Shipping Plan (`PRQ-013`), SPIR (`PRQ-015`).
- Final/turnover books: `PRQ-016` and discipline final books (e.g., `MEC-023`, `ELE-030` energization package).
- Source vendor document table rows themselves (as artifacts/evidence) referenced from the index.

### Out of scope
- Production of the engineered equipment package itself (covered by `DEL-033-04`).
- EPC Integrator review and acceptance of the submitted documents (covered by `DEL-033-06`).
- Construction tie-in and turnover into the larger facility (covered by `DEL-033-03`).
- Facility-side electrical interfaces, feeder routing, and grounding/bonding design outside the building edge (EPC Integrator scope).

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
The set shall include the Electrical and I&C document classes applicable to a medium-voltage switchgear electrical-building package per source's discipline tables:
- Electrical: `ELE-002`, `ELE-003`, `ELE-011` (protective coordination / short-circuit / arc-flash study), `ELE-012`, `ELE-014`, `ELE-015`, `ELE-016`, `ELE-017` (integral building lighting), `ELE-019`, `ELE-020`, `ELE-027`, `ELE-028`, `ELE-029`, `ELE-030`.
- I&C: `INS-002`, `INS-003`, `INS-005`, `INS-006`, `INS-008`, `INS-009`, and the remaining INS entries enumerated in the source list applicable to switchgear protection, metering, and PCN/EtherNet interfaces (DBM SEC-12 cites EtherNet to plant PLC for the 4160V MCC; carry the same interface convention for the 4160V switchgear).
- Source: `_Sources/26020-Package_Requirements.docx` — "Electrical, lighting, EHT, grounding" and "Instrumentation and controls interfaces"; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 754.
- ASSUMPTION: All INS entries listed in the source are applicable to a 4160V switchgear lineup; the EPC Integrator confirms per-line applicability during `DEL-033-06` review.

### R-5 Discipline applicability (Mechanical / structural / building)
The set shall include mechanical equipment and packaged-equipment data documents for the switchgear and its enclosing electrical building: `MEC-001`, `MEC-002`, `MEC-003`, `MEC-006`, `MEC-016`, `MEC-017`, `MEC-018`, `MEC-021`, `MEC-022`, `MEC-023`, `MEC-024`, `MEC-025`. Building enclosure, HVAC, lighting, fire/gas detection, and building services where supplied integral to the vendor scope shall be documented.
- ASSUMPTION: The 4160V switchgear lineup is delivered inside a vendor-supplied electrical building consistent with DBM SEC-11 "Electrical buildings shall house MCCs, switchgear, distribution equipment, and associated HVAC/ventilation systems" (line 766). The source template treats packaged equipment uniformly under this set.
- Source: `_Sources/26020-Package_Requirements.docx` — "Core package engineering" and "Mechanical Equipment IOM Manual" rows; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 764-770.

### R-6 Pressure / piping / civil applicability
Pressure-equipment and piping document classes are presumed NOT APPLICABLE for a power-distribution switchgear/electrical-building package. Civil (foundation, anchorage) document classes apply where the vendor supplies the building foundation/skid; otherwise they are EPC Integrator scope.
- Disposition status: PROPOSAL — EPC Integrator confirms during `DEL-033-06` review based on the building/foundation split-of-supply. Mark on the Vendor Document Index as N/A with rationale or APPLICABLE accordingly.

### R-7 Quality records and traceability
The Package Vendor shall provide:
- Supplier Quality Plan (`QLT-006`),
- Inspection and Test Plan (`QLT-003`) with hold/witness points,
- Material Test Reports / Certificates (`QLT-013`),
- Inspection Release Certificate (`QLT-020`),
- Manufacturing Record Book / Vendor Data Book (`QLT-021`).
- Source: `_Sources/26020-Package_Requirements.docx` — "Core vendor documents".

### R-8 Logistics and spares
The Package Vendor shall provide a Logistics / Shipping Plan (`PRQ-013`) and a Spare Parts Interchangeability Record (`PRQ-015`). Building/lineup transportation, lifting plan, and field assembly instructions shall be included given the modular vendor-building delivery model.
- Source: same as R-7.

### R-9 FAT/SAT records
The Package Vendor shall provide FAT and energization records: `MEC-021`/`MEC-022` (mechanical FAT procedure/report for building/HVAC components where applicable) and `ELE-029`/`ELE-030` (electrical FAT/SAT procedure and energization package for the switchgear lineup and protection relays).
- Source: `_Sources/26020-Package_Requirements.docx`.

### R-10 As-built and turnover books
The Package Vendor shall deliver `PRQ-016` Vendor Data Book / Final Supplier Documentation and discipline final books (e.g., `MEC-023`); the EPC Integrator integrates these into the package turnover record. As-built electrical, I&C, and building drawings shall be issued.
- Source: same as R-9.

### R-11 Standards compliance traceability
Each vendor-supplied document subject to industry codes/standards shall reference the governing standard. The accessible source set cites Class I Zone 2 Gas Groups IIA/IIB area-classification basis (DBM line 722) and API RP 505 for outdoor hazardous-area classification. Switchgear-specific governing standards (e.g., IEEE C37 series, ANSI/IEEE C57 for instrument transformers, CSA Z462 arc-flash, IEEE 1584) are not explicitly cited in the accessible source set.
- Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 720-727; `_Sources/26020-Package_Requirements.docx` standards-citation rows.
- ASSUMPTION: Industry-standard medium-voltage switchgear codes apply; specific clauses are TBD until detailed-design specifications are issued.

### R-12 Submittal cadence and native files
- Submittal cadence (preliminary / certified / as-built): TBD — not stated in accessible source slices.
- Native file format requirements (e.g., CAD format, electronic transmittal): TBD — not stated in accessible source slices.

## Standards

| Standard | Applicability | Location |
|---|---|---|
| API RP 505 | Hazardous area classification basis for process modules/buildings (Class I Zone 2 IIA/IIB) | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 722 |
| IEEE C37 series (MV switchgear) | ASSUMPTION; not explicitly cited in accessible source set | location TBD |
| IEEE C57 / ANSI C57 (instrument transformers) | ASSUMPTION | location TBD |
| CSA Z462 / IEEE 1584 (arc-flash) | ASSUMPTION; site-electrical detailed-design dependency | location TBD |
| CSA / electrical area classification standards | ASSUMPTION; site-electrical detailed-design dependency | location TBD |

## Verification

| Requirement | Verification Method |
|---|---|
| R-1 (Index) | Document review against source's Core vendor documents list; index completeness check by EPC Integrator (`DEL-033-06`). |
| R-2 (Control Procedure) | Review of `DOC-008` against EPC document-control expectations. |
| R-3, R-7, R-8 (Core/quality/logistics) | Checklist verification at submittal milestones and at final turnover. |
| R-4, R-5 (Discipline applicability) | Per-line applicability disposition recorded on Vendor Document Index; reviewed in `DEL-033-06`. |
| R-6 (Civil/piping applicability) | Recorded as APPLICABLE/N/A with rationale on the Index per split-of-supply; reviewed in `DEL-033-06`. |
| R-9 (FAT/SAT) | Receipt of signed FAT report (`MEC-022` if applicable, `ELE-030` energization package) prior to acceptance. |
| R-10 (As-built and turnover books) | Receipt of `PRQ-016` and discipline final books; cross-check against ITP closure. |
| R-11 (Standards) | Each engineered document cites governing standards; standards list reviewed during `DEL-033-06`. |
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
