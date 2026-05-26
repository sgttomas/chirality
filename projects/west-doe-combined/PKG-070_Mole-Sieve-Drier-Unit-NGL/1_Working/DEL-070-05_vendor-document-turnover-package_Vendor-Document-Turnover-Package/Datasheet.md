# Datasheet — DEL-070-05 Vendor Document Turnover Package

## Identification

| Field | Value |
|---|---|
| DeliverableID | DEL-070-05_vendor-document-turnover-package |
| Name | Vendor Document Turnover Package |
| ParentPackageID | PKG-070 |
| PackageName | Mole Sieve Drier Unit (NGL) |
| Tagged Equipment | 26020-01-PT-22-003 — Mole Sieve Drier Unit (NGL) |
| Discipline | Mechanical |
| Type | Vendor Document Turnover |
| ResponsibleParty | Package Vendor (vendor documentation); EPC Integrator interface/integration review |
| Decomposition Row | DELIVERABLE_REGISTER.csv row 412 |
| Source | Workbook Packages row 74; 26020-Package_Requirements.docx package heading 24 |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Turnover artifact set scope | Vendor document register, vendor document submittals, source-required vendor documentation, turnover records | _CONTEXT.md Scope; DELIVERABLE_REGISTER.csv row 412 |
| Vendor document count (core vendor documents) | 11 entries (`PRQ-009`, `DOC-008`, `QLT-006`, `QLT-003`, `QLT-013`, `QLT-020`, `QLT-021`, `PRQ-013`, `PRQ-015`, `PRQ-016`, plus the vendor data book closures) | 26020-Package_Requirements.docx §"26020-01-PT-22-003 — Mole Sieve Drier Unit (NGL)" / Vendor Engineering Deliverables, "Core vendor documents" group |
| Source-required vendor documentation scope (engineering/design feeders) | Core package engineering (MEC-001/002/003/006/014/016/017/018/021/022/023/024/025), Static pressure equipment (MEC-005/009; REG-022), Heat transfer equipment (MEC-010), Process package design (PRO-004/005/007/008/010/011/012/020/025/026/027/028), Relief/flare/vent (PRO-014/015/016/017/018), Process piping interfaces (PIP-003/004/006/007/008/009/017/018/024/025/028), Drainage/containment (PRO-023; CIV-014), Electrical/lighting/EHT/grounding (ELE-002/003/014/015/016/020/027/028/029/030/017/018/012/019; PIP-020/021), I&C interfaces (INS-002/003/005/006/008/009/010/011/016/017/018/025/029; CTL-003/005/006/026), F&G / Technical safety (TSF-002/003/004/009/011/013/028), Structural/foundations/supports/access (STR-001/002/004/005/006/011/012/013/014/020) | 26020-Package_Requirements.docx §Mole Sieve Drier Unit (NGL) / Vendor Engineering Deliverables table |
| Covers SOW items | SOW-0145, SOW-0146, SOW-0147, SOW-0148 | _CONTEXT.md |
| Supports objectives | OBJ-001, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 | _CONTEXT.md (PACKAGE_HEURISTIC) — ASSUMPTION: package-grouped mapping |
| Turnover acceptance threshold | TBD — not stated in accessible sources |
| Final vendor data book closure document | PRQ-016 "Vendor Data Book / Final Supplier Documentation" (commercial); MEC-023 "Vendor Data Book / Mechanical Final Documentation" (mechanical close-out) | 26020-Package_Requirements.docx Mole Sieve table |
| Document control procedure | DOC-008 "Vendor Document Control Procedure" | 26020-Package_Requirements.docx Mole Sieve table |
| Vendor document index | PRQ-009 "Vendor Document Index" | 26020-Package_Requirements.docx Mole Sieve table |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Package operating mode (context) | Three-tower NGL molecular sieve dehydration: one adsorbing, one regenerating, one standby; 2,385 m³/d (15,000 bbl/d); target outlet water < 7 ppmw | 26020-Package_Requirements.docx §Mole Sieve Drier Unit / Basic Scope |
| Interface coordination notes | TBD — source explicitly states "TBD." | 26020-Package_Requirements.docx §Mole Sieve / Interface Coordination Notes |
| Heated/enclosed building scope | Required around inlet gas coalescer, inline mixers, settling vessel, and regeneration gas scrubber per final heater/scrubber location and area classification (drives applicable vendor doc subset for the enclosure) | 26020-Package_Requirements.docx §Mole Sieve / Major Included Equipment |

## Construction

| Element | Value | Source |
|---|---|---|
| Register physical form | Vendor document register table (rows = vendor document IDs from the Mole Sieve "Vendor Engineering Deliverables" table) | DELIVERABLE_REGISTER.csv row 412; 26020-Package_Requirements.docx |
| Submittal physical form | Native vendor files (PDFs, CAD, calculations, ITP records) plus EPC review/transmittal records | DELIVERABLE_REGISTER.csv row 412 ("vendor document submittals") |
| Turnover record physical form | Manufacturing Record Book / Vendor Data Book per QLT-021 and PRQ-016; EPC handoff log | 26020-Package_Requirements.docx Mole Sieve table |
| Storage location | TBD — not specified by accessible sources |
| Numbering / tag convention | TBD — not specified by accessible sources |

## References

- `_CONTEXT.md`
- `_REFERENCES.md`
- DELIVERABLE_REGISTER.csv row 412 (`DEL-070-05_vendor-document-turnover-package`)
- 26020-Package_Requirements.docx, §"26020-01-PT-22-003 — Mole Sieve Drier Unit (NGL)" (heading 24), subsection "Vendor Engineering Deliverables"
- 26020-Packages_Interfaces_4_export.xlsx (interface source pointer; location TBD at slice level)
