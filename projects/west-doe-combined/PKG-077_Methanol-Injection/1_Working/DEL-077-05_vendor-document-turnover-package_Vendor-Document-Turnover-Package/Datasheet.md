# Datasheet — DEL-077-05 Vendor Document Turnover Package (PKG-077)

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-077-05_vendor-document-turnover-package` |
| Name | Vendor Document Turnover Package |
| ParentPackageID | `PKG-077` |
| Package Name | Methanol Injection |
| Workbook Tag | `26020-01-29-002` (PACKAGE_REGISTER row 72) |
| Discipline | Mechanical |
| WBS | 01 |
| Type | Vendor Document Turnover |
| ResponsibleParty | Package Vendor (vendor documentation) with EPC Integrator interface/integration review |
| Covers Scope Items | `SOW-0143` |
| Supports Objectives | `OBJ-001`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` (ASSUMPTION: PACKAGE_HEURISTIC mapping by package; not individually confirmed at deliverable-ID level) |
| Decomposition status note | Gate 6 disposition: "Methanol Injection scope is included with the Cryogenic Unit package scope." This vendor-document deliverable nonetheless exists as a distinct production unit under PKG-077; turnover may be physically co-issued with the Cryogenic Unit (`PKG-076`) vendor turnover at EPC Integrator discretion. (Source: `PACKAGE_REGISTER.csv` row 72.) |

## Attributes

The deliverable is a document set rather than a physical artifact. Attribute values describe the document register that the Package Vendor must deliver and the EPC Integrator must accept for the Methanol Injection package.

| Attribute | Value | Source |
|---|---|---|
| Document register basis | Per-package `Vendor Engineering Deliverables` list defined in source `26020-Package_Requirements.docx` | `_Sources/26020-Package_Requirements.docx` ("Vendor Engineering Deliverables" / "Core vendor documents") |
| Document control procedure | Vendor Document Control Procedure (`DOC-008`) required as core vendor document | same as above |
| Index | Vendor Document Index (`PRQ-009`) required as core vendor document | same as above |
| Final book | Vendor Data Book / Final Supplier Documentation (`PRQ-016`); mechanical final book `MEC-023` | same as above |
| Quality records | Supplier Quality Plan `QLT-006`; ITP `QLT-003`; MTRs/Certificates `QLT-013`; Inspection Release Certificate `QLT-020`; Manufacturing Record Book / VDB `QLT-021` | same as above |
| Logistics records | Logistics / Shipping Plan `PRQ-013`; SPIR `PRQ-015` | same as above |
| Discipline applicability | Mechanical-led packaged equipment with significant process, piping, electrical, I&C, structural, and fire & gas interfaces per the package interface list | `PACKAGE_REGISTER.csv` row 72 (interface types); `_Sources/26020-Package_Requirements.docx` |
| Major included equipment | Methanol storage tank (`TK-6395-1`); methanol pump (`P-6396-1`) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2545, 2605–2606 |
| Coverage | Single SOW item `SOW-0143` | `DELIVERABLE_REGISTER.csv` (`DEL-077-05` row); `SCOPE_LEDGER.csv` (SOW-0143) |
| Source basis pointer | Detailed per-package vendor-document section text for "Methanol Injection" is not present as a separate slice in `_Sources/`. The package-vendor-deliverables enumeration is drawn from the generic `26020-Package_Requirements.docx` template; methanol-specific scope context is drawn from `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`. | `_Sources/26020-Package_Requirements.docx`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |
| Vendor documentation gap evidence | ARTIFACT_REGISTER entry `ART-CF38039426` records "TBD vendor document register — Detailed vendor-document requirements are not present in current source material for this package." | `_Decomposition/.../ARTIFACT_REGISTER.csv` |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Lifecycle stage at acceptance | Post-FAT through turnover, including as-built records | `_Sources/26020-Package_Requirements.docx` (PIP-028 As-Built; MEC-022 FAT Report; ELE-030 Energization Package) |
| Site basis affecting documentation | Cold-climate West Doe Deepcut site; vendor data must reflect site ambient and electrical-area classification per facility design basis | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (site basis); `_Sources/26020-Package_Requirements.docx` |
| Process function | Provide methanol injection capability for transient/temporary hydrate management at multiple plant injection points (BAHX pass inlets, J-T valve inlet, inlet separators upstream of PCV, inlet separators upstream of HCL/water dump valves, and acid-gas-compressor package) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 428, 630, 1328 |
| Storage and pumping basis | Atmospheric double-walled methanol tank adjacent to expander building; pure methanol tank design specific gravity 1.00 TBC; triplex reciprocating injection pump | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 1329 |
| Injection-point capacities | Design capacities TBC (per DBM line 1328); methanol injection rates listed among items TBD/TBC at line 1351; acid-gas-compressor methanol-injection details TBD at line 1371 | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 1328, 1351, 1371, 1392 |
| Acceptance gate | EPC Integrator interface/integration review and acceptance via `DEL-077-06` | `DELIVERABLE_REGISTER.csv` (`DEL-077-06` row) |
| Submittal cadence | TBD — not stated in accessible source slices |
| Native file format requirements | TBD — not stated in accessible source slices |
| Co-issue option | Gate 6 disposition allows the vendor turnover to be physically co-issued with `PKG-076` Cryogenic Unit turnover; this is an EPC Integrator decision | `PACKAGE_REGISTER.csv` row 72 |

## Construction

The "construction" of this deliverable is the assembly and turnover of a vendor document set. The composing document classes are taken directly from `_Sources/26020-Package_Requirements.docx` "Vendor Engineering Deliverables" template, filtered for the Methanol Injection (mechanical pump/tank) package scope. Per-line applicability is set in `Specification.md`; the lists below are the candidate enumeration the vendor and EPC reviewer dispose against.

**Core vendor documents (always required):**

- `PRQ-009` Vendor Document Index
- `DOC-008` Vendor Document Control Procedure
- `QLT-006` Supplier Quality Plan
- `QLT-003` Inspection and Test Plan (ITP)
- `QLT-013` Material Test Reports / Certificates
- `QLT-020` Inspection Release Certificate
- `QLT-021` Manufacturing Record Book / Vendor Data Book
- `PRQ-013` Logistics / Shipping Plan
- `PRQ-015` Spare Parts Interchangeability Record (SPIR)
- `PRQ-016` Vendor Data Book / Final Supplier Documentation

**Core package engineering (mechanical) — APPLICABLE:**

- `MEC-001` Mechanical Design Basis
- `MEC-002` Mechanical Equipment List
- `MEC-003` Mechanical Equipment Data Sheets (for `TK-6395-1`, `P-6396-1`)
- `MEC-006` Package Equipment Specifications
- `MEC-014` Mechanical Calculation Package (pump/tank)
- `MEC-016` Equipment General Arrangement Drawing
- `MEC-017` Equipment Installation / Setting Drawings
- `MEC-018` Lifting / Handling Study for Major Equipment
- `MEC-021` Equipment FAT / Performance Test Procedure
- `MEC-022` Equipment FAT / Performance Test Report
- `MEC-023` Vendor Data Book / Mechanical Final Documentation
- `MEC-024` Mechanical Spares / Special Tools Requirements
- `MEC-025` Mechanical Equipment IOM Manual

**Static pressure equipment — APPLICABILITY PROPOSAL:**

- `MEC-005` Static Equipment Specifications — ASSUMPTION: applies to the methanol storage tank (`TK-6395-1`) per DBM line 1329 ("atmospheric double-walled methanol tank"); pressure-vessel rules vs. atmospheric-tank rules disposed during detailed design.
- `MEC-009` Pressure Vessel Data Sheets — likely N/A for an atmospheric tank; APPLICABLE only if pulsation dampener or accumulator is included with the triplex pump (TBD).
- `REG-022` Pressure Equipment Registration Package — APPLICABILITY TBD; depends on jurisdictional treatment of the double-walled atmospheric tank and any pulsation/accumulator equipment.

**Process package design:**

- `PRO-007` Process Description / Operating Philosophy (transient hydrate-management injection)
- `PRO-008` Piping and Instrumentation Diagrams (P&IDs) for the methanol storage, pump, distribution headers, and tie-ins
- `PRO-010` Major Equipment Process Data Sheets (`TK-6395-1`, `P-6396-1`)
- `PRO-011` Utility Summary / Utility Consumption Report (methanol consumption per injection point)
- `PRO-012` Line Sizing / Hydraulic Calculation Package (injection lines, pump discharge)
- `PRO-020` Process Control Philosophy (single-point injection control; see DBM line 1328 "designed to inject into one point at a time")
- `PRO-025` Operating Guidelines / Startup-Shutdown Narrative
- `PRO-026` HAZOP / PHA Technical Input Package
- `PRO-027` Process Safety Information (PSI) Package
- `PRO-028` Process As-Built P&ID Package
- `PRO-004` Process Flow Diagram (PFD) — APPLICABILITY PROPOSAL: applicable if a package-level PFD is required; otherwise integrated into the facility PFD by EPC Integrator.
- `PRO-005` Heat and Material Balance — APPLICABILITY PROPOSAL: typically N/A for a methanol injection package; included only if vaporization / heat-of-mixing effects require explicit basis.

**Relief / flare / vent design — APPLICABILITY PROPOSAL:**

- `PRO-014` Relief and Flare Design Basis — APPLICABLE for the pump discharge (positive-displacement triplex pump requires overpressure protection); applicability to the atmospheric tank is via vent/pressure-vacuum protection, not flare.
- `PRO-015` PSV / Pressure Relief Sizing Calculations — APPLICABLE for pump discharge PSV / thermal relief.
- `PRO-016` Relief Valve Data Sheets — APPLICABLE for any PSV in the package.
- `PRO-017` Flare Load Summary / Flare System Study — APPLICABILITY TBD; methanol injection is not typically a flare load contributor.
- `PRO-018` Blowdown / Depressurization Study — APPLICABILITY TBD.

**Process piping interfaces — APPLICABLE:**

- `PIP-003` Piping Line List (injection headers and branch lines to each injection point)
- `PIP-004` Tie-In List / Tie-In Scope Sheets (BAHX pass inlets, J-T valve inlet, inlet separators ×2, acid-gas compressor package)
- `PIP-006` Equipment Arrangement / Piping General Arrangement
- `PIP-007` Piping Plans and Sections
- `PIP-008` Piping Isometric Drawings
- `PIP-009` Fabrication Isometrics with BOM
- `PIP-017` Piping MTO / Material Take-Off
- `PIP-018` Valve Data Sheets (injection isolation/check valves)
- `PIP-024` Hydrotest / Pressure Test Packages
- `PIP-025` Flushing / Cleaning / Drying Procedure (methanol service: cleanliness and water-content control)
- `PIP-028` Piping As-Built Drawings
- `PIP-020` Piping Insulation / Heat Tracing Schedule — APPLICABLE (cold-climate service; freeze protection)
- `PIP-021` Piping Heat Tracing Interface Package — APPLICABLE per cold-climate basis

**Drainage / containment interfaces:**

- `PRO-023` Process Sewer / Closed Drain Design Basis — APPLICABILITY TBD; methanol is hydrocarbon-class drainage candidate.
- `CIV-014` Bund / Dike / Secondary Containment Drawings — APPLICABLE for the atmospheric methanol tank (secondary containment is consistent with "double-walled" basis at DBM line 1329).

**Electrical, lighting, EHT, grounding — APPLICABLE (limited):**

- `ELE-002` Electrical Load List / Consumer List (pump motor; instrumentation; EHT circuits)
- `ELE-003` Single-Line Diagrams (SLDs) (package SLD if integral, otherwise interface-only)
- `ELE-014` Cable Schedule
- `ELE-015` Cable Tray / Routing Drawings (package-internal where applicable)
- `ELE-016` Electrical Layout Drawings
- `ELE-020` Electrical Equipment Data Sheets (pump motor)
- `ELE-027` Electrical Installation Details
- `ELE-028` Electrical Interconnection / Connection Diagrams
- `ELE-029` Electrical FAT / SAT Procedure
- `ELE-030` Electrical Test Records / Energization Package
- `ELE-017` Lighting Layout Drawings — APPLICABILITY TBD (package-area lighting typically EPC scope)
- `ELE-018` Electrical Heat Tracing Design Package — APPLICABLE for cold-climate freeze protection of methanol piping
- `ELE-012` Grounding / Earthing Study — APPLICABLE (atmospheric tank earthing; pump motor)
- `ELE-019` Earthing / Bonding Layout Drawings — APPLICABLE

**Instrumentation and controls interfaces — APPLICABLE:**

- `INS-002` Instrument Index
- `INS-003` Instrument Data Sheets (level / pressure / flow on tank and pump; injection-flow indicators where required)
- `INS-005` Instrument Location Plans
- `INS-006` Instrument Hook-Up Drawings
- `INS-008` Instrument Loop Diagrams
- `INS-009` Instrument Wiring / Termination Diagrams
- `INS-010` Junction Box / Marshalling Drawings
- `INS-011` Instrument Cable Schedule
- `INS-016` Control Valve Data Sheets (single-point selection valves at injection points per DBM line 1328)
- `INS-017` On-Off / Shutdown Valve Data Sheets — APPLICABILITY TBD
- `INS-018` Instrument I/O List
- `INS-025` Instrument MTO / Quantity Take-Off
- `INS-029` Instrument As-Built Drawings
- `CTL-003` Control Narrative / Functional Specification (single-point injection selection logic)
- `CTL-005` Cause and Effect Matrix
- `CTL-006` DCS I/O List
- `CTL-026` Package Vendor Interface Specification

**Fire and gas / technical safety interfaces — APPLICABLE (methanol = flammable liquid):**

- `TSF-002` Fire and Gas Philosophy
- `TSF-003` Fire and Gas Mapping Study
- `TSF-004` Fire and Gas Detector Layout Drawings
- `TSF-009` SIL Determination Report — APPLICABILITY TBD
- `TSF-011` Safety Requirements Specification (SRS) — APPLICABILITY TBD
- `TSF-013` Supplier SIL Documentation / Safety Manual — APPLICABILITY TBD
- `TSF-028` Emergency Response Plan Inputs

**Structural, foundations, supports, access — APPLICABLE:**

- `STR-001` Structural Design Basis
- `STR-002` Structural General Arrangement Drawings
- `STR-004` Structural Calculation Package
- `STR-005` Foundation Design Calculations (tank foundation; pump skid)
- `STR-006` Foundation Drawings
- `STR-011` Platform / Access Structure Drawings (tank access for sampling/maintenance)
- `STR-013` Anchor Bolt / Embedment Drawings
- `STR-014` Lifting Lug / Transport Analysis
- `STR-020` Structural MTO / Quantity Take-Off
- `STR-012` Module Structural Drawings — APPLICABILITY TBD (only if delivered as a module)

Refer to `Specification.md` for the binding discipline applicability rules and verification mapping.

## References

- Gate 7 PROJECT_DECOMP snapshot deliverable row: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` (`DEL-077-05_vendor-document-turnover-package`)
- Gate 7 PROJECT_DECOMP snapshot package row: `.../PACKAGE_REGISTER.csv`, row 72 (`PKG-077`, tag `26020-01-29-002`, "Methanol Injection")
- Gate 7 PROJECT_DECOMP snapshot scope ledger row: `.../SCOPE_LEDGER.csv` (`SOW-0143`)
- Gate 7 PROJECT_DECOMP snapshot artifact row: `.../ARTIFACT_REGISTER.csv` (`ART-CF38039426` vendor-document gap evidence)
- `_Sources/26020-Package_Requirements.docx` — "Vendor Engineering Deliverables" (core vendor documents and per-discipline deliverable IDs); methanol-injection-specific section not present (vendor-document gap per `ART-CF38039426`)
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — facility design basis: methanol injection scope, equipment, and injection points (lines 428, 630, 1107, 1135, 1328–1329, 1334, 1351, 1363, 1371, 1392); equipment list (lines 2379, 2545, 2605–2606)
- Deliverable-local: `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`
