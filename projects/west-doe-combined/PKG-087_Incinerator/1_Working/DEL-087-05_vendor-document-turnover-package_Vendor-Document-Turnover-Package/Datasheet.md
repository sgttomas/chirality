# Datasheet — DEL-087-05 Vendor Document Turnover Package

## Identification

| Field | Value |
|---|---|
| DeliverableID | DEL-087-05_vendor-document-turnover-package |
| Name | Vendor Document Turnover Package |
| ParentPackageID | PKG-087 |
| ParentWorkbookID | 87 |
| PackageName | Incinerator |
| Package Tag (source) | 26020-Package_Requirements.docx, package heading 40 — Incinerator (Workbook Packages row 64) |
| Discipline | Mechanical |
| DeliverableType | Vendor Document Turnover |
| ResponsibleParty | Package Vendor (vendor documentation) with EPC Integrator interface/integration review |
| Source | 26020-Package_Requirements.docx, package heading 40 (Incinerator); Workbook Packages row 64; 3-25_Comp_and_Liquids_DBM.md (incinerator service description); 4-25_Deepcut_DBM.md §2.4 Flare and Incinerator Spacing |

## Attributes

The deliverable itself is the **assembled vendor document turnover package** for the Incinerator package. The attributes below describe the package contents and its index, not the incinerator equipment itself.

| Attribute | Value | Source |
|---|---|---|
| Package scope basis | Vendor-supplied documentation set for the Incinerator system that services spent-caustic and DSO off-gas vapours from the 4-25 NGL mercaptan treating system and other shared 3-25/4-25 interfaces, including upstream knock-out drum and stack | 26020-Package_Requirements.docx package heading 40 (location TBD — exact source slice not parsed); 3-25_Comp_and_Liquids_DBM.md §"Incinerator Interface" (lines ~1568-1572) |
| Document index basis | Core vendor documents + discipline document sets enumerated in the source Vendor Engineering Deliverables table for this package | 26020-Package_Requirements.docx package heading 40 "Vendor Engineering Deliverables" (location TBD) |
| Submittal classes | Engineering submittals, quality records, manufacturing records, IOM, spares, logistics, final vendor data book | 26020-Package_Requirements.docx (general project package convention; section heading 40 specifics location TBD) |
| Turnover record class | Final Supplier Documentation / Vendor Data Book (PRQ-016); Mechanical Final Documentation Vendor Data Book (MEC-023); Manufacturing Record Book (QLT-021); Inspection Release Certificate (QLT-020) | 26020-Package_Requirements.docx (project-wide vendor documentation convention) |
| Acceptance counterpart | EPC Integrator review and integration acceptance (DEL-087-06 EPC Vendor Package Review and Acceptance) | DELIVERABLE_REGISTER.csv (Gate-07) row DEL-087-06 |
| Covers scope items | SOW-0111, SOW-0112, SOW-0113, SOW-0114 | `_CONTEXT.md`; DELIVERABLE_REGISTER.csv row DEL-087-05 |
| Supports objectives | OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 | `_CONTEXT.md`; OBJECTIVE_DELIVERABLE_MAP.csv (PACKAGE_HEURISTIC association — ASSUMPTION at deliverable-ID level) |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Project phase consumed | Engineering through FAT, shipping, site installation, commissioning, turnover | ASSUMPTION (standard package lifecycle); supports SOW-0111..0114 |
| Effective documentation date | Concurrent with vendor RFQ basis for the Incinerator package | TBD — RFQ document for Incinerator package not identified in accessible sources |
| Source language | TBD (assumed English) | TBD |
| Submittal medium | TBD — typical: electronic PDF + native files via vendor's document control system | TBD |
| Shared-facility service split | Incinerator is shared 3-25/4-25 system; exact service allocation requires current source ruling | 3-25_Comp_and_Liquids_DBM.md §"SEC-08 Emissions" (lines 547, 555); §"Incinerator Interface" (lines 1568-1572) |

## Construction

The turnover package is a **derivative aggregation** of vendor-produced documents grouped by class. The source Vendor Engineering Deliverables list (26020-Package_Requirements.docx package heading 40) defines the **document classes that must populate the index**. Because the exact source slice for heading 40 has not been parsed in this run, the discipline-document enumeration below is given at the **package-vendor convention level** used consistently across this project's vendor packages; deliverable-specific deltas (e.g., emissions-specific certificates) are listed with **location TBD** until heading 40 is read.

### Core vendor documents (convention)
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

### Core package engineering (convention)
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

### Fired/combustion equipment (incinerator-specific, convention + DBM evidence)
| ID | Document Name |
|---|---|
| MEC-011 | Fired Equipment / Combustion Equipment Specifications (location TBD) |
| MEC-012 | Burner / Pilot / Ignition System Data Sheets (location TBD) |
| MEC-013 | Fired Equipment Performance / Emissions Test Procedure (location TBD) |
| PRO-024 | Emissions Compliance Calculation / Permit Package (location TBD) |
| REG-022 | Pressure Equipment Registration Package (knock-out drum and any pressure-retaining components — applicable per 3-25_Comp_and_Liquids_DBM.md §"Incinerator Interface" KO drum mention) |

### Static, relief, piping, utilities, drainage, electrical, controls, EHT, grounding (interface-driven)

Additional discipline document sets are required per the source Vendor Engineering Deliverables table for the applicable physical interfaces (process piping, utility piping including supplemental fuel-gas supply, relief/vent, drain/containment, electrical power, area lighting, EHT, grounding, I&C, fire & gas, structural). The complete enumerated list is recorded in `Specification.md` §Requirements. The Physical Interface Summary specific to heading 40 is **TBD** until the source heading is parsed; sibling packages confirm the pattern.

## References

- 26020-Package_Requirements.docx, package section "heading 40 — Incinerator" (Basic Scope; Major Included Equipment; Scope Notes / Open Items; Physical Interface Summary; Vendor Engineering Deliverables) — **location TBD** (file present at `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/26020-Package_Requirements.docx`; specific heading slice not parsed this run).
- RFQ source pointer: vendor RFQ for the Incinerator package — TBD (not identified in accessible sources).
- 3-25_Comp_and_Liquids_DBM.md "Incinerator Interface" (lines 1568-1572); "SEC-08 Emissions" rows referencing incinerator (lines 547-555).
- 4-25_Deepcut_DBM.md §2.4 "Flare and Incinerator Spacing" (lines 276-300) — spacing/thermal-radiation requirements applicable to layout but not directly to vendor documentation scope.
- DEL-087-05 `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`.
- Gate-07 PROJECT_DECOMP snapshot, DELIVERABLE_REGISTER.csv row DEL-087-05 and sibling rows DEL-087-01..06.
