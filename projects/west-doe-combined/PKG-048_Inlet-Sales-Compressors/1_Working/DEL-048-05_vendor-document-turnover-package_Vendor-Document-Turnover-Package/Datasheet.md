# Datasheet — DEL-048-05 Vendor Document Turnover Package

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-048-05_vendor-document-turnover-package` | `_CONTEXT.md` Identity |
| Name | Vendor Document Turnover Package | `_CONTEXT.md` Identity |
| ParentPackageID | `PKG-048` | `_CONTEXT.md` Identity |
| PackageName | Inlet / Sales Compressors | `_CONTEXT.md` Identity |
| Discipline | Mechanical | `_CONTEXT.md` Identity |
| Type | Vendor Document Turnover | `_CONTEXT.md` Identity |
| ResponsibleParty | Package Vendor (vendor documentation) with EPC Integrator interface/integration review | `_CONTEXT.md` Identity |
| Source package heading | `26020-Package_Requirements.docx` heading 3 — Inlet / Sales Compressors (ASSUMPTION: heading number per `_CONTEXT.md` Source Reference; exact heading text TBD pending direct extraction) | `_CONTEXT.md` Source Reference; `_REFERENCES.md` |
| Covers Scope Items | SOW-0115; SOW-0116; SOW-0117; SOW-0118 | `_CONTEXT.md` Covers Scope Items |
| Supports Objectives | OBJ-001; OBJ-003; OBJ-004; OBJ-005; OBJ-006; OBJ-007; OBJ-008; OBJ-009; OBJ-010 (ASSUMPTION — PACKAGE_HEURISTIC association per skill default) | `_CONTEXT.md` Supports Objectives |

## Attributes — Package Configuration Context (from source)

The PKG-048 package is `Inlet / Sales Compressors`. The combined naming distinguishes this package from the inlet-only PKG-080 sibling: PKG-048 nominally covers both inlet-compression and sales-compression service within the Doe field combined compressor scope. Specific equipment counts, capacities, and pressure ranges for heading 3 are not directly extractable from the locally available binary source slice.

| Attribute | Value | Source |
|---|---|---|
| Service | Inlet compression and sales compression (combined package scope) | `_CONTEXT.md` PackageName; `_Decomposition/.../PACKAGE_REGISTER.csv` |
| Configuration | TBD (likely 2 x 50% or 2 x 100% with stage-distinct duties per typical compressor-station basis) | `26020-Package_Requirements.docx` heading 3 — `location TBD` (binary slice not extracted) |
| Capacity (per unit / combined) | TBD | `26020-Package_Requirements.docx` heading 3 — `location TBD` |
| Suction / discharge pressures | TBD | `26020-Package_Requirements.docx` heading 3 — `location TBD` |
| Materials / seals | NACE-compliant materials and seals required (ASSUMPTION based on sour-service combined inlet/sales scope; consistent with parallel sour-service package PKG-080) | ASSUMPTION; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-04 confirms sour-service plant basis |
| Major included equipment | TBD (compressor packages, drivers, intercoolers/aftercoolers, package auxiliaries; specific make/model TBD) | `26020-Package_Requirements.docx` heading 3 — `location TBD` |
| Location / Status | 3-25 / 03-25 West Doe Compressor Station (ASSUMPTION based on `_Sources/DBM-Comp_and_Liquids` plant identification) | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` |
| Source basis | `26020-Package_Requirements.docx` heading 3; supporting interface workbook `26020-Packages_Interfaces_4_export.xlsx` (PKG-048 / row 65 of Workbook Packages — exact slice `location TBD`) | `_CONTEXT.md` Source Reference |

These attributes are package-level context; the deliverable defined here is the *vendor document turnover package* covering the documentation for the equipment above.

## Documents in Turnover Scope — Source Vendor Document Table (heading 3 vendor engineering deliverables)

The 26020 package-requirements document defines the vendor document set for each package under a per-heading vendor-engineering-deliverables table (sibling PKG-080 at heading 33 carries a ~114-row table — Table 133). The PKG-048 heading 3 vendor deliverables table is the authoritative document-scope set for this deliverable and is assumed to use the same source-document-ID nomenclature (PRQ-/DOC-/QLT-/MEC-/PRO-/PIP-/ELE-/INS-/CTL-/TSF-/STR-/CIV-/REG-) as the sibling package.

**ASSUMPTION:** The set below lists the source-document-ID categories that are *expected* to apply to a combined inlet/sales sour-gas compression package and that appear in the sibling heading 33 table. Individual rows must be reconciled against the PKG-048 heading 3 table once the source slice is directly extracted. Rows that prove not to be enumerated in heading 3 must be deleted from PRQ-009 with a scope-change record; rows that prove to be present but missing here must be added.

### Core vendor documents (expected)
| ID | Name |
|---|---|
| PRQ-009 | Vendor Document Index |
| DOC-008 | Vendor Document Control Procedure |
| QLT-006 | Supplier Quality Plan |
| QLT-003 | Inspection and Test Plan (ITP) |
| QLT-013 | Material Test Reports / Certificates |
| QLT-020 | Inspection Release Certificate |
| QLT-021 | Manufacturing Record Book / Vendor Data Book |
| PRQ-013 | Logistics / Shipping Plan |
| PRQ-015 | Spare Parts Interchangeability Record (SPIR) |
| PRQ-016 | Vendor Data Book / Final Supplier Documentation |

### Core package engineering (expected)
| ID | Name |
|---|---|
| MEC-001 | Mechanical Design Basis |
| MEC-002 | Mechanical Equipment List |
| MEC-003 | Mechanical Equipment Data Sheets |
| MEC-006 | Package Equipment Specifications |
| MEC-014 | Mechanical Calculation Package |
| MEC-016 | Equipment General Arrangement Drawing |
| MEC-017 | Equipment Installation / Setting Drawings |
| MEC-018 | Lifting / Handling Study for Major Equipment |
| MEC-021 | Equipment FAT / Performance Test Procedure |
| MEC-022 | Equipment FAT / Performance Test Report |
| MEC-023 | Vendor Data Book / Mechanical Final Documentation |
| MEC-024 | Mechanical Spares / Special Tools Requirements |
| MEC-025 | Mechanical Equipment IOM Manual |

### Rotating equipment / compressors (expected, both inlet and sales duties)
| ID | Name |
|---|---|
| MEC-004 | Rotating Equipment Specifications |
| MEC-008 | Compressor Data Sheets |
| MEC-019 | Mechanical Seal / Lube Oil Specification |
| ELE-011 | Motor Starting Study |
| REG-022 | Pressure Equipment Registration Package |

### Relief / flare / vent design (expected)
| ID | Name |
|---|---|
| PRO-014 | Relief and Flare Design Basis |
| PRO-015 | PSV / Pressure Relief Sizing Calculations |
| PRO-016 | Relief Valve Data Sheets |
| PRO-017 | Flare Load Summary / Flare System Study |
| PRO-018 | Blowdown / Depressurization Study |

### Process piping interfaces (expected)
| ID | Name |
|---|---|
| PRO-008 | Piping and Instrumentation Diagrams (P&IDs) |
| PIP-003 | Piping Line List |
| PIP-004 | Tie-In List / Tie-In Scope Sheets |
| PIP-006 | Equipment Arrangement / Piping General Arrangement |
| PIP-007 | Piping Plans and Sections |
| PIP-008 | Piping Isometric Drawings |
| PIP-009 | Fabrication Isometrics with BOM |
| PIP-017 | Piping MTO / Material Take-Off |
| PIP-018 | Valve Data Sheets |
| PIP-024 | Hydrotest / Pressure Test Packages |
| PIP-025 | Flushing / Cleaning / Drying Procedure |
| PIP-028 | Piping As-Built Drawings |

### Utility piping interfaces (expected)
| ID | Name |
|---|---|
| PRO-011 | Utility Summary / Utility Consumption Report |

### Drainage / containment interfaces (expected)
| ID | Name |
|---|---|
| PRO-023 | Process Sewer / Closed Drain Design Basis |
| CIV-014 | Bund / Dike / Secondary Containment Drawings |

### Electrical, lighting, EHT, grounding (expected)
| ID | Name |
|---|---|
| ELE-002 | Electrical Load List / Consumer List |
| ELE-003 | Single-Line Diagrams (SLDs) |
| ELE-014 | Cable Schedule |
| ELE-015 | Cable Tray / Routing Drawings |
| ELE-016 | Electrical Layout Drawings |
| ELE-020 | Electrical Equipment Data Sheets |
| ELE-027 | Electrical Installation Details |
| ELE-028 | Electrical Interconnection / Connection Diagrams |
| ELE-029 | Electrical FAT / SAT Procedure |
| ELE-030 | Electrical Test Records / Energization Package |
| ELE-017 | Lighting Layout Drawings |
| ELE-018 | Electrical Heat Tracing Design Package |
| PIP-020 | Piping Insulation / Heat Tracing Schedule |
| PIP-021 | Piping Heat Tracing Interface Package |
| ELE-012 | Grounding / Earthing Study |
| ELE-019 | Earthing / Bonding Layout Drawings |

### Instrumentation and controls interfaces (expected)
| ID | Name |
|---|---|
| INS-002 | Instrument Index |
| INS-003 | Instrument Data Sheets |
| INS-005 | Instrument Location Plans |
| INS-006 | Instrument Hook-Up Drawings |
| INS-008 | Instrument Loop Diagrams |
| INS-009 | Instrument Wiring / Termination Diagrams |
| INS-010 | Junction Box / Marshalling Drawings |
| INS-011 | Instrument Cable Schedule |
| INS-016 | Control Valve Data Sheets |
| INS-017 | On-Off / Shutdown Valve Data Sheets |
| INS-018 | Instrument I/O List |
| INS-025 | Instrument MTO / Quantity Take-Off |
| INS-029 | Instrument As-Built Drawings |
| CTL-003 | Control Narrative / Functional Specification |
| CTL-005 | Cause and Effect Matrix |
| CTL-006 | DCS I/O List |
| CTL-026 | Package Vendor Interface Specification |

### Building / HVAC / code interfaces (expected)
| ID | Name |
|---|---|
| PRO-024 | Ventilation / Process Safety Equipment Inputs |
| TSF-023 | Building Siting / Occupied Building Risk Assessment |
| REG-021 | Fire Code / Building Code Compliance Package |
| STR-002 | Structural General Arrangement Drawings |
| STR-012 | Module Structural Drawings |

### Fire and gas / technical safety interfaces (expected)
| ID | Name |
|---|---|
| TSF-002 | Fire and Gas Philosophy |
| TSF-003 | Fire and Gas Mapping Study |
| TSF-004 | Fire and Gas Detector Layout Drawings |
| TSF-009 | SIL Determination Report |
| TSF-011 | Safety Requirements Specification (SRS) |
| TSF-013 | Supplier SIL Documentation / Safety Manual |
| TSF-028 | Emergency Response Plan Inputs |

### Structural, foundations, supports, access (expected)
| ID | Name |
|---|---|
| STR-001 | Structural Design Basis |
| STR-004 | Structural Calculation Package |
| STR-005 | Foundation Design Calculations |
| STR-006 | Foundation Drawings |
| STR-011 | Platform / Access Structure Drawings |
| STR-013 | Anchor Bolt / Embedment Drawings |
| STR-014 | Lifting Lug / Transport Analysis |
| STR-020 | Structural MTO / Quantity Take-Off |

## Conditions

| Field | Value | Source |
|---|---|---|
| Submittal stages | Bid, IFR, IFA, IFC, As-Built / Final | ASSUMPTION (industry-typical); not stated in source heading 3 (slice not extracted). TBD against vendor document control procedure (DOC-008) when issued. |
| Review cycle | EPC Integrator review per DOC-008 / Vendor Document Control Procedure | TBD (DOC-008 not yet issued) |
| Transmittal medium | TBD (vendor portal vs. controlled file transfer) | TBD |
| Document numbering | Vendor-native numbering aligned to Vendor Document Index (PRQ-009) | source: PRQ-009 (expected) in heading 3 vendor deliverables table |
| Turnover package medium | Vendor Data Book (PRQ-016 / MEC-023) plus electronic transmittal | source: PRQ-016, MEC-023 (expected) in heading 3 |

## Construction (turnover package composition)

| Element | Content | Source |
|---|---|---|
| Vendor Document Index | Master list of all vendor documents in scope for PKG-048, with revision status, transmittal dates, EPC review state, and separate columns/rows distinguishing inlet-duty vs sales-duty unit documents where applicable | source: PRQ-009 (expected) in heading 3 |
| Vendor Document Control Procedure | Vendor-issued procedure governing identification, numbering, revision, transmittal, and acceptance | source: DOC-008 (expected) in heading 3 |
| Document submittals | Each vendor document at the contractually required revision (Bid/IFR/IFA/IFC/As-Built) | ASSUMPTION on stage labels; document set per heading 3 vendor deliverables table (location TBD) |
| Turnover records | Inspection Release Certificate (QLT-020), Manufacturing Record Book / Vendor Data Book (QLT-021), Final Supplier Documentation (PRQ-016), Mechanical Final Documentation (MEC-023), Logistics / Shipping Plan (PRQ-013), SPIR (PRQ-015) | source: heading 3 vendor deliverables table (expected) |
| Quality and inspection evidence | Supplier Quality Plan (QLT-006), ITP (QLT-003), Material Test Reports / Certificates (QLT-013) | source: heading 3 vendor deliverables table (expected) |

## References

- `_Sources/26020-Package_Requirements.docx`, heading 3 — Inlet / Sales Compressors (binary; specific slice not directly text-extracted in this run — `location TBD`).
- `_Sources/26020-Packages_Interfaces_4_export.xlsx` (Workbook Packages row 65 per `_CONTEXT.md`; binary, not text-extracted).
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (plant-basis context confirming sour-service compressor station; advisory only).
- `_REFERENCES.md` (deliverable-local).
- `_CONTEXT.md` (deliverable-local).
- GATE-07 snapshot: `DELIVERABLE_REGISTER.csv`, `PACKAGE_REGISTER.csv`, `OBJECTIVE_DELIVERABLE_MAP.csv`.
- Sibling pattern for structural framework only (NOT used as authority): `PKG-080_Inlet-Compressors/.../DEL-080-05_vendor-document-turnover-package_Vendor-Document-Turnover-Package/`.
