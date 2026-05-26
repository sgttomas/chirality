# Specification — DEL-077-05 Vendor Document Turnover Package (PKG-077)

## Scope

### In scope
- The complete vendor document set required for the PKG-077 Methanol Injection package, organized in a Vendor Document Index (`PRQ-009`) and controlled per the Vendor Document Control Procedure (`DOC-008`).
- All "Core vendor documents" enumerated in `_Sources/26020-Package_Requirements.docx` ("Vendor Engineering Deliverables" section).
- The discipline-applicable engineering and design documents required for a Mechanical-led packaged equipment package consisting of a methanol storage tank (`TK-6395-1`), a triplex reciprocating injection pump (`P-6396-1`), associated injection-distribution piping/instrumentation/controls, and required electrical, structural, drainage, and fire-and-gas interfaces (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 1328–1329; `PACKAGE_REGISTER.csv` row 72).
- Vendor quality records: Supplier Quality Plan, ITP, MTRs/Certificates, Inspection Release Certificate, Manufacturing Record Book / VDB (`QLT-006`, `QLT-003`, `QLT-013`, `QLT-020`, `QLT-021`).
- Logistics records: Shipping Plan (`PRQ-013`), SPIR (`PRQ-015`).
- Final/turnover books: `PRQ-016` and discipline final books (e.g., `MEC-023`, `ELE-030` energization package).

### Out of scope
- Production of the engineered equipment package itself (covered by `DEL-077-04`).
- EPC Integrator review and acceptance of the submitted documents (covered by `DEL-077-06`).
- Construction tie-in and turnover into the larger facility (covered by `DEL-077-03`).
- The Cryogenic Unit vendor turnover (`PKG-076`), even though Gate 6 disposition records that the Methanol Injection scope is included with the Cryogenic Unit package scope; co-issue is permitted as an EPC Integrator decision but is not in this deliverable's binding scope. (Source: `PACKAGE_REGISTER.csv` row 72.)

## Requirements

### R-1 Vendor Document Index
The Package Vendor shall provide a Vendor Document Index (`PRQ-009`) listing every document in the turnover set with document number, revision, status, applicability (APPLICABLE / N/A with rationale), and submittal/return-cycle status.
- Source: `_Sources/26020-Package_Requirements.docx` — "Vendor Engineering Deliverables / Core vendor documents".

### R-2 Vendor Document Control Procedure
The Package Vendor shall provide a Document Control Procedure (`DOC-008`) describing numbering, revisioning, transmittal mechanics, and review-cycle handling.
- Source: same as R-1.

### R-3 Core vendor documents
The set shall include all "Core vendor documents" listed in `_Sources/26020-Package_Requirements.docx`:
`PRQ-009`, `DOC-008`, `QLT-006`, `QLT-003`, `QLT-013`, `QLT-020`, `QLT-021`, `PRQ-013`, `PRQ-015`, `PRQ-016`.

### R-4 Discipline applicability (Mechanical — primary)
The set shall include the Mechanical packaged-equipment document classes applicable to a methanol storage tank + reciprocating injection pump package per the source's discipline tables:
- Core mechanical engineering: `MEC-001`, `MEC-002`, `MEC-003`, `MEC-006`, `MEC-014`, `MEC-016`, `MEC-017`, `MEC-018`, `MEC-021`, `MEC-022`, `MEC-023`, `MEC-024`, `MEC-025`.
- Source: `_Sources/26020-Package_Requirements.docx` — "Core package engineering" and "Mechanical Equipment IOM Manual" rows.
- Source for package scope: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 1328–1329, 2545, 2605–2606.

### R-5 Static pressure / tank equipment applicability
- `MEC-005` Static Equipment Specifications APPLIES to the methanol storage tank (`TK-6395-1`).
- `MEC-009` Pressure Vessel Data Sheets APPLIES only if pulsation dampeners/accumulators or other code pressure vessels are part of the package scope; ASSUMPTION: not required for the bare atmospheric tank.
- `REG-022` Pressure Equipment Registration Package applicability is TBD; depends on jurisdictional treatment of the double-walled atmospheric tank and any pulsation/accumulator equipment.
- Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 1329 ("atmospheric double-walled methanol tank"; "triplex reciprocating injection pump"); `_Sources/26020-Package_Requirements.docx` "Static pressure equipment".

### R-6 Process package design applicability
The set shall include process-package design documents necessary to describe the methanol injection function, distribution, control, and safety basis:
- `PRO-007`, `PRO-008`, `PRO-010`, `PRO-011`, `PRO-012`, `PRO-020`, `PRO-025`, `PRO-026`, `PRO-027`, `PRO-028` APPLY.
- `PRO-004` (PFD) APPLIES only if the package-level PFD is required by the EPC Integrator; otherwise integrated into the facility PFD.
- `PRO-005` (Heat and Material Balance) is presumed NOT APPLICABLE for a methanol injection package; APPLIES only if vaporization or heat-of-mixing effects require explicit basis.
- Source: `_Sources/26020-Package_Requirements.docx` "Process package design"; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 1328 (single-point selection logic).

### R-7 Relief / overpressure protection
The Package Vendor shall provide pump-discharge thermal/PSV relief documentation:
- `PRO-014` Relief and Flare Design Basis APPLIES for the pump-discharge protection.
- `PRO-015` PSV / Pressure Relief Sizing Calculations APPLIES for any package PSV.
- `PRO-016` Relief Valve Data Sheets APPLIES for any PSV in the package.
- `PRO-017` Flare Load Summary / Flare System Study applicability is TBD (methanol injection is not typically a flare-load contributor).
- `PRO-018` Blowdown / Depressurization Study applicability is TBD.
- ASSUMPTION: A positive-displacement (triplex reciprocating) pump requires deadhead/overpressure protection; the source DBM does not enumerate the PSV explicitly. Mark `location TBD` for the specific PSV location and set in detailed design.
- Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 1329 (triplex reciprocating pump); `_Sources/26020-Package_Requirements.docx` "Relief / flare / vent design".

### R-8 Process piping and tie-in interfaces
The set shall include process-piping and tie-in documentation for all injection points enumerated in source:
- Tie-in points: BAHX pass inlets upstream of strainers; J-T valve inlet; inlet separators upstream of PCV; inlet separators upstream of HCL and water dump valves; acid-gas compressor package.
- Documents: `PIP-003`, `PIP-004`, `PIP-006`, `PIP-007`, `PIP-008`, `PIP-009`, `PIP-017`, `PIP-018`, `PIP-024`, `PIP-025`, `PIP-028`.
- Cold-climate add-ons: `PIP-020` (insulation/heat-tracing schedule) and `PIP-021` (heat-tracing interface package) APPLY.
- Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 1328 (injection-point enumeration); `_Sources/26020-Package_Requirements.docx` "Process piping interfaces".

### R-9 Drainage / containment
- `CIV-014` Bund / Dike / Secondary Containment Drawings APPLIES (consistent with the "double-walled" atmospheric tank basis at DBM line 1329).
- `PRO-023` Process Sewer / Closed Drain Design Basis applicability is TBD pending facility drainage classification of methanol service.
- Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 1329; `_Sources/26020-Package_Requirements.docx` "Drainage / containment interfaces".

### R-10 Electrical and EHT
The set shall include the electrical documentation for the pump motor, package instrumentation, and electrical heat tracing (cold-climate freeze protection):
- `ELE-002`, `ELE-003`, `ELE-014`, `ELE-015`, `ELE-016`, `ELE-020`, `ELE-027`, `ELE-028`, `ELE-029`, `ELE-030` APPLY.
- `ELE-018` Electrical Heat Tracing Design Package APPLIES for cold-climate freeze protection of methanol piping.
- `ELE-012` Grounding / Earthing Study and `ELE-019` Earthing / Bonding Layout Drawings APPLY (atmospheric tank earthing; pump motor).
- `ELE-017` Lighting Layout Drawings applicability is TBD (package-area lighting typically EPC scope).
- Source: `_Sources/26020-Package_Requirements.docx` "Electrical, lighting, EHT, grounding"; cold-climate site basis per `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`.

### R-11 Instrumentation and controls
The set shall include the I&C documentation required for tank level/pressure, pump status/flow, and injection-point control valves (single-point selection logic):
- `INS-002`, `INS-003`, `INS-005`, `INS-006`, `INS-008`, `INS-009`, `INS-010`, `INS-011`, `INS-016`, `INS-018`, `INS-025`, `INS-029`, `CTL-003`, `CTL-005`, `CTL-006`, `CTL-026` APPLY.
- `INS-017` On-Off / Shutdown Valve Data Sheets applicability is TBD.
- Source: `_Sources/26020-Package_Requirements.docx` "Instrumentation and controls interfaces"; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 1328 ("System designed to inject into one point at a time").

### R-12 Fire and gas / technical safety
Methanol is a flammable liquid (atmospheric tank in close proximity to expander building per DBM line 1329); the set shall include:
- `TSF-002`, `TSF-003`, `TSF-004`, `TSF-028` APPLY.
- `TSF-009`, `TSF-011`, `TSF-013` applicability is TBD pending SIL determination scope.
- Source: `_Sources/26020-Package_Requirements.docx` "Fire and gas / technical safety interfaces"; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 1329 (tank location).

### R-13 Structural, foundations, supports, access
The set shall include structural documentation for the tank foundation, pump skid, tank access for sampling/maintenance, and anchorage:
- `STR-001`, `STR-002`, `STR-004`, `STR-005`, `STR-006`, `STR-011`, `STR-013`, `STR-014`, `STR-020` APPLY.
- `STR-012` Module Structural Drawings APPLIES only if delivered as a module.
- Source: `_Sources/26020-Package_Requirements.docx` "Structural, foundations, supports, access".

### R-14 Quality records and traceability
The Package Vendor shall provide:
- Supplier Quality Plan (`QLT-006`),
- Inspection and Test Plan (`QLT-003`) with hold/witness points,
- Material Test Reports / Certificates (`QLT-013`),
- Inspection Release Certificate (`QLT-020`),
- Manufacturing Record Book / Vendor Data Book (`QLT-021`).
- Source: `_Sources/26020-Package_Requirements.docx` — "Core vendor documents".

### R-15 Logistics and spares
The Package Vendor shall provide a Logistics / Shipping Plan (`PRQ-013`) and a Spare Parts Interchangeability Record (`PRQ-015`).
- Source: same as R-14.

### R-16 FAT and pre-startup records
The Package Vendor shall provide FAT and energization records: `MEC-021`/`MEC-022` (mechanical FAT procedure/report for the pump and tank) and `ELE-029`/`ELE-030` (electrical FAT/SAT procedure and energization package for the pump motor and EHT).
- Source: `_Sources/26020-Package_Requirements.docx`.

### R-17 As-built and turnover books
The Package Vendor shall deliver `PRQ-016` Vendor Data Book / Final Supplier Documentation and discipline final books (e.g., `MEC-023`, `PIP-028`); the EPC Integrator integrates these into the package turnover record via `DEL-077-06`. As-built electrical, instrumentation, and piping drawings shall be issued.
- Source: same as R-16.

### R-18 Standards compliance traceability
Each vendor-supplied document subject to industry codes/standards shall reference the governing standard. The accessible source set does not enumerate specific governing standards for the methanol injection package beyond the generic facility design basis; specific standards (e.g., API 675 controlled-volume reciprocating pumps; API 650 atmospheric storage tanks; NACE methanol-service materials; relevant fire-and-gas standards) are ASSUMPTIONS until detailed-design specifications are issued.
- Source: `_Sources/26020-Package_Requirements.docx` (no methanol-package-specific clause cited); `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (no specific standards cited for methanol injection equipment in the slices reviewed).

### R-19 Submittal cadence and native files
- Submittal cadence (preliminary / certified / as-built): TBD — not stated in accessible source slices.
- Native file format requirements (e.g., CAD format, electronic transmittal): TBD — not stated in accessible source slices.

### R-20 Capacities and TBD parameters carried forward
The Vendor Document Index shall record the following items as TBD/TBC and confirm closure during detailed design and FAT:
- Methanol injection-point design capacities (DBM line 1328 "all design capacities TBC").
- Methanol injection rates (DBM line 1351).
- Methanol tank design specific gravity (DBM line 1329 / line 1392).
- Acid-gas-compressor methanol-injection details (DBM line 1371).
- Required injection points (DBM line 1351).

## Standards

| Standard | Applicability | Location |
|---|---|---|
| Facility design basis (Deepcut DBM 4-25) | Site ambient, area classification, drainage, fire-and-gas basis | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |
| API 650 (atmospheric storage tanks) | ASSUMPTION; applicability to a double-walled atmospheric methanol tank TBD against vendor standard practice | location TBD |
| API 675 / API 674 (controlled-volume / positive-displacement reciprocating pumps) | ASSUMPTION; applicable to the triplex reciprocating injection pump | location TBD |
| NACE / methanol-service materials standards | ASSUMPTION; methanol-service material compatibility | location TBD |
| Fire and gas detection standards (e.g., ISA/IEC 60079 series) | ASSUMPTION; electrical area classification per facility design basis | location TBD |
| Pressure-equipment jurisdictional registration (CRN / BC) | ASSUMPTION; depends on package equipment list | location TBD |

## Verification

| Requirement | Verification Method |
|---|---|
| R-1 (Index) | Document review against source's Core vendor documents list and applicable discipline lines; completeness check by EPC Integrator (`DEL-077-06`). |
| R-2 (Control Procedure) | Review of `DOC-008` against EPC document-control expectations. |
| R-3, R-14, R-15 (Core/quality/logistics) | Checklist verification at submittal milestones and at final turnover. |
| R-4–R-13 (Discipline applicability) | Per-line applicability disposition recorded on Vendor Document Index; reviewed in `DEL-077-06`. |
| R-7 (Pump-discharge relief) | PSV sizing review; data sheet review; PSV install verified on as-built P&ID. |
| R-8 (Tie-ins) | Tie-in list cross-checked against DBM injection-point enumeration (line 1328) and against the EPC integration P&IDs. |
| R-9 (Containment) | Containment drawings verify the double-walled tank basis and any required bund/dike. |
| R-10 (Electrical / EHT) | EHT design package and FAT/SAT records reviewed; freeze-protection coverage check. |
| R-11 (I&C) | Single-point injection-selection control narrative and C&E matrix reviewed against DBM line 1328. |
| R-12 (F&G) | F&G mapping coverage verified for tank, pump skid, and high-leak-potential connections. |
| R-13 (Structural) | Foundation calc/anchor-bolt review; access platform verified for sampling/maintenance. |
| R-16 (FAT/SAT) | Receipt of signed FAT report (`MEC-022`) and `ELE-030` energization package prior to acceptance. |
| R-17 (As-built and turnover books) | Receipt of `PRQ-016` and discipline final books; cross-check against ITP closure. |
| R-18 (Standards) | Each engineered document cites governing standards (or marks `location TBD` per HRR-077-05-002). |
| R-19 (Cadence / native files) | TBD — specify in package PO/contract prior to vendor mobilization. |
| R-20 (TBD capacities) | Index records open items; closed during detailed design / FAT; verified at `DEL-077-06`. |

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
