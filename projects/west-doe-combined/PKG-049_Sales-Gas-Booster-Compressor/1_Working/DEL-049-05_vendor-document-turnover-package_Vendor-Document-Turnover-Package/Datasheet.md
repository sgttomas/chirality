# Datasheet — DEL-049-05 Vendor Document Turnover Package

## Identification

| Field | Value |
|---|---|
| DeliverableID | DEL-049-05_vendor-document-turnover-package |
| Name | Vendor Document Turnover Package |
| ParentPackageID | PKG-049 |
| ParentWorkbookID | 49 |
| PackageName | Sales Gas Booster Compressor |
| Package Tag (source) | 26020-01-PT-12-004 — Sales Gas Booster Compressor |
| Discipline | Mechanical |
| DeliverableType | Vendor Document Turnover |
| ResponsibleParty | Package Vendor (vendor documentation) with EPC Integrator interface/integration review |
| Source | 26020-Package_Requirements.docx, heading "26020-01-PT-12-004 - Sales Gas Booster Compressor"; Workbook Packages row 80 |

## Attributes

The deliverable itself is the **assembled vendor document turnover package** for the Sales Gas Booster Compressor. The attributes below describe the package contents and its index, not the compressor equipment.

| Attribute | Value | Source |
|---|---|---|
| Package scope basis | Vendor-supplied documentation set for one (1) Sales Gas Booster Compressor package, 1 x 100%, Ariel KBX/X reciprocating compressor with motor driver and filter coalescer | 26020-Package_Requirements.docx §26020-01-PT-12-004 "Basic Scope" / "Major Included Equipment" |
| Document index basis | Core vendor documents + discipline document sets enumerated in source Vendor Engineering Deliverables table | 26020-Package_Requirements.docx §26020-01-PT-12-004 "Vendor Engineering Deliverables" |
| Submittal classes | Engineering submittals, quality records, manufacturing records, IOM, spares, logistics, final vendor data book | 26020-Package_Requirements.docx §26020-01-PT-12-004 "Vendor Engineering Deliverables" |
| Turnover record class | Final supplier documentation / Vendor Data Book (PRQ-016) and Mechanical Final Documentation Vendor Data Book (MEC-023); Manufacturing Record Book (QLT-021); Inspection Release Certificate (QLT-020) | 26020-Package_Requirements.docx §26020-01-PT-12-004 |
| Acceptance counterpart | EPC Integrator review and integration acceptance (DEL-049-06) | DELIVERABLE_REGISTER.csv (Gate-07) row DEL-049-06 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Project phase consumed | Engineering through FAT, shipping, site installation, commissioning, turnover | ASSUMPTION (standard package lifecycle); supports SOW-0169..0172 scope items |
| Effective documentation date | Concurrent with vendor RFQ basis "26020-01-PT-RFQ-12-004-Sales Booster Comp.docx" | 26020-Package_Requirements.docx §26020-01-PT-12-004 "Source Basis" |
| Source language | TBD (assumed English) | TBD |
| Submittal medium | TBD — typical: electronic PDF + native files via vendor's document control system | TBD |

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

### Rotating equipment / compressors
| ID | Document Name |
|---|---|
| MEC-004 | Rotating Equipment Specifications |
| MEC-008 | Compressor Data Sheets |
| MEC-019 | Mechanical Seal / Lube Oil Specification |
| ELE-011 | Motor Starting Study |
| REG-022 | Pressure Equipment Registration Package |

### Static, heat transfer, relief, piping, utilities, drainage, electrical, lighting, EHT, grounding (additional discipline document sets enumerated in source)

Additional discipline document sets are required per the source Vendor Engineering Deliverables table for the applicable physical interfaces (process piping, utility piping, relief/flare/vent, drain/containment, electrical, lighting, EHT, grounding, I&C, fire & gas, structural, etc.). The complete enumerated list is recorded in `Specification.md` §Requirements.

Source: 26020-Package_Requirements.docx §26020-01-PT-12-004 "Vendor Engineering Deliverables".

## References

- 26020-Package_Requirements.docx, package section "26020-01-PT-12-004 - Sales Gas Booster Compressor" (Basic Scope; Major Included Equipment; Scope Notes / Open Items; Physical Interface Summary; Vendor Engineering Deliverables).
- RFQ source pointer: `RFQ/Bid Docs/26020-01-PT-RFQ-12-004-Sales Booster Comp.docx` (location TBD — not directly accessed this run).
- 4-25_Deepcut_DBM.md, "Sales Gas Booster Compressor Basis" (lines ~932-955) for equipment context.
- DEL-049-05 `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`.
- Gate-07 PROJECT_DECOMP snapshot, DELIVERABLE_REGISTER.csv row DEL-049-05 and sibling rows DEL-049-01..06.
