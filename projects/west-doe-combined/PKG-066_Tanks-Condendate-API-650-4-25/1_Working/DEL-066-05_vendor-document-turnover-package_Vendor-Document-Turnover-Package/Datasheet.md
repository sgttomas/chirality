# Datasheet — DEL-066-05 Vendor Document Turnover Package

## Identification

| Field | Value |
|---|---|
| DeliverableID | DEL-066-05_vendor-document-turnover-package |
| Name | Vendor Document Turnover Package |
| ParentPackageID | PKG-066 |
| ParentWorkbookID | 66 |
| PackageName | Tanks, Condensate (API 650) — 4-25 (Deepcut) |
| Package Tag (source) | 26020-01-PT-19-004 — Tanks, Condensate |
| Equipment Tags | TK-9110-1, TK-9120-1, TK-9130-1, TK-9140-1, TK-9150-1 (5 condensate storage tanks) |
| Discipline | Mechanical |
| DeliverableType | Vendor Document Turnover |
| ResponsibleParty | Package Vendor (vendor documentation) with EPC Integrator interface/integration review |
| Source | 26020-Package_Requirements.docx, heading "26020-01-PT-19-004 - Tanks, Condensate" (heading 21); Workbook Packages row 89 |

## Attributes

The deliverable itself is the **assembled vendor document turnover package** for the 4-25 (Deepcut) condensate storage tanks. The attributes below describe the package contents and its index, not the tanks themselves.

| Attribute | Value | Source |
|---|---|---|
| Package scope basis | Vendor-supplied documentation set for the 4-25 condensate product storage tanks (analog basis from 26020-03-PT-19-006 / 3-25 condensate tanks; 4-25 specifics pending package RFQ or brief) | 26020-Package_Requirements.docx §26020-01-PT-19-004 "Basic Scope" / "Source Basis" / "Scope Notes" |
| Document index basis | Core vendor documents + discipline document sets enumerated in source Vendor Engineering Deliverables table | 26020-Package_Requirements.docx §26020-01-PT-19-004 "Vendor Engineering Deliverables" |
| Submittal classes | Engineering submittals, quality records, manufacturing records, IOM, spares, logistics, final vendor data book | 26020-Package_Requirements.docx §26020-01-PT-19-004 "Vendor Engineering Deliverables" |
| Turnover record class | Final supplier documentation / Vendor Data Book (PRQ-016) and Mechanical Final Documentation Vendor Data Book (MEC-023); Manufacturing Record Book (QLT-021); Inspection Release Certificate (QLT-020) | 26020-Package_Requirements.docx §26020-01-PT-19-004 |
| Acceptance counterpart | EPC Integrator review and integration acceptance (DEL-066-06) | DELIVERABLE_REGISTER.csv (Gate-07) — sibling row DEL-066-06 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Project phase consumed | Engineering through fabrication, site erection, hydrotest, commissioning, turnover | ASSUMPTION (standard tank-package lifecycle; supports SOW-0205..0208) |
| Effective documentation date | Concurrent with vendor RFQ (4-25 package RFQ not yet issued per source basis note) | 26020-Package_Requirements.docx §26020-01-PT-19-004 "Source Basis" |
| Source language | TBD (assumed English) | TBD |
| Submittal medium | TBD — typical: electronic PDF + native files via vendor's document control system | TBD |
| Design code | Modified API 650 (atmospheric condensate storage) | 4-25_Deepcut_DBM.md line 1646 "Condensate tank specification — Modified API 650"; 26020-Package_Requirements.docx §26020-01-PT-19-004 "Major Included Equipment" |

## Construction

The turnover package is a **derivative aggregation** of vendor-produced documents grouped by class. The source Vendor Engineering Deliverables list defines the **document classes that must populate the index**:

### Core vendor documents
| ID | Document Name |
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

### Core package engineering
| ID | Document Name |
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

### Storage tanks
| ID | Document Name |
|---|---|
| MEC-005 | Static Equipment Specifications |
| MEC-011 | Storage Tank Data Sheets |

### Relief / flare / vent design
| ID | Document Name |
|---|---|
| PRO-014 | Relief and Flare Design Basis |
| PRO-015 | PSV / Pressure Relief Sizing Calculations |
| PRO-016 | Relief Valve Data Sheets |
| PRO-017 | Flare Load Summary / Flare System Study |
| PRO-018 | Blowdown / Depressurization Study |

### Process piping interfaces
| ID | Document Name |
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

### Drainage / containment interfaces
| ID | Document Name |
|---|---|
| PRO-023 | Process Sewer / Closed Drain Design Basis |
| CIV-014 | Bund / Dike / Secondary Containment Drawings |

### Electrical, lighting, EHT, grounding
| ID | Document Name |
|---|---|
| ELE-017 | Lighting Layout Drawings |
| ELE-012 | Grounding / Earthing Study |
| ELE-019 | Earthing / Bonding Layout Drawings |

### Cathodic protection interfaces
| ID | Document Name |
|---|---|
| PLN-015 | Corrosion Protection Design Basis |
| PLN-016 | Cathodic Protection Design Package |

### Instrumentation and controls interfaces
| ID | Document Name |
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

### Structural, foundations, supports, access
| ID | Document Name |
|---|---|
| STR-001 | Structural Design Basis |
| STR-002 | Structural General Arrangement Drawings |
| STR-004 | Structural Calculation Package |
| STR-005 | Foundation Design Calculations |
| STR-006 | Foundation Drawings |
| STR-011 | Platform / Access Structure Drawings |
| STR-012 | Module Structural Drawings |
| STR-013 | Anchor Bolt / Embedment Drawings |
| STR-014 | Lifting Lug / Transport Analysis |
| STR-020 | Structural MTO / Quantity Take-Off |

### Civil grading / spill containment interfaces
| ID | Document Name |
|---|---|
| CIV-003 | Grading Plan |
| CIV-004 | Drainage / Stormwater Management Report |
| CIV-015 | Retention Pond / Containment Basin Design |
| CIV-019 | Civil MTO / Quantity Take-Off |

Source: 26020-Package_Requirements.docx §26020-01-PT-19-004 "Vendor Engineering Deliverables".

## References

- 26020-Package_Requirements.docx, package section "26020-01-PT-19-004 - Tanks, Condensate" (Basic Scope; Major Included Equipment; Scope Notes / Open Items; Physical Interface Summary; Vendor Engineering Deliverables; Interface Coordination Notes — last marked "TBD").
- Analog RFQ source pointer: `26020-03-PT-19-006_Tanks_Cond/Bid Docs/Budgetary/26020-03-PT-RFQ-19-006 - Conde Tanks.docx` (location TBD — not directly accessed this run; identified by source as the basis analog for 4-25).
- 4-25_Deepcut_DBM.md — condensate tank capacity, count, and design basis (lines ~1633–1665, 1639–1646, 2557, 2625).
- DEL-066-05 `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`.
- Gate-07 PROJECT_DECOMP snapshot, DELIVERABLE_REGISTER.csv row DEL-066-05 and sibling rows DEL-066-01..06.
