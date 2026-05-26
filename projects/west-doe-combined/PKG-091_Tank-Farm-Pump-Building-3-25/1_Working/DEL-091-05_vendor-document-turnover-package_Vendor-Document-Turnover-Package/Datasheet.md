# Datasheet — DEL-091-05 Vendor Document Turnover Package

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-091-05_vendor-document-turnover-package` |
| Name | Vendor Document Turnover Package |
| ParentPackageID | `PKG-091` |
| PackageName | Tank Farm Pump Building 3-25 |
| Discipline | Mechanical |
| DeliverableType | Vendor Document Turnover |
| ResponsibleParty | Package Vendor (vendor documentation); EPC Integrator (interface/integration review) |
| DecompositionSnapshot | GATE-07_Final_Published_2026-05-24 (PROJECT_DECOMP) |
| CoversScopeItems | SOW-0185; SOW-0186; SOW-0187; SOW-0188 |
| SupportsObjectives | OBJ-002; OBJ-003; OBJ-004; OBJ-005; OBJ-006; OBJ-007; OBJ-008; OBJ-009; OBJ-010 (ASSUMPTION: PACKAGE_HEURISTIC association via PKG-091) |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package physical scope | Tank Farm Pump Building 3-25 — building housing all tank-farm pumps | SOW-0186 (Workbook Packages row 84; 26020-Package_Requirements.docx package heading 44; Basic scope) |
| Major equipment populations | 1 Building Drain Pump (P-9295-2); 2 Water Transfer Pumps (P-9290/9293-2); 2 Sour Condensate Booster Pumps (P-9215/9216-2); 2 Condensate Sweetening Feed Pumps (P-9210/9220-2); 1 Condensate Skim Pump (P-9200-2); 1 Sour Condensate Recycle Pump (P-9230-2); 2 Condensate Booster Pumps (P-9211/9221-2); 1 Condensate Product Recycle Pump (P-9240-2) | SOW-0187 (26020-Package_Requirements.docx package heading 44; Major included equipment) |
| Documentation register cardinality | 114 artifact rows currently associated to DEL-091-05 in the snapshot ARTIFACT_REGISTER | GATE-07 ARTIFACT_REGISTER.csv (count of DEL-091-05 rows) |
| Vendor document categories represented | Core vendor documents; Core package engineering; Rotating equipment / pumps; plus additional categories carried as `Vendor Documentation Category Evidence` rows | GATE-07 ARTIFACT_REGISTER.csv (DEL-091-05 rows, ArtifactType column) |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Site / service environment | Tank-farm pump aggregation building (cold-climate facility implied by `-40C start-up` reference) | SOW-0188 (Scope notes and open items) |
| Electrical supply for driven equipment | 575 V / 3 Ph / 60 Hz motors fed from 600 V MCC; DOL or VFD starting; local H-O-A or On/Off | SOW-0188 |
| Interface boundary (by others) | DCS integration, foundations, electrical supply to MCC by others | SOW-0188 |
| Vendor/EPC responsibility split | Package Vendor owns engineering, design, vendor documentation, physical equipment; EPC Integrator owns facility integration and interface review | SOW-0185; PROJECT_DECOMP DEC-006 |

## Construction (Documentation Set Composition)

The deliverable is a documentation set, not a physical assembly. Its "construction" is the composition of the vendor document register and turnover binder.

| Component | Representative artifact rows (from GATE-07 ARTIFACT_REGISTER) | Source |
|---|---|---|
| Register-level | Vendor Documentation Register (ART-8AEAB021A9) | 26020-Package_Requirements.docx package heading 44; Vendor Engineering Deliverables table |
| Category — Core vendor documents | Vendor Document Index (PRQ-009); Vendor Document Control Procedure (DOC-008); Supplier Quality Plan (QLT-006); ITP (QLT-003); MTRs/Certificates (QLT-013); Inspection Release Certificate (QLT-020); Manufacturing Record Book / Vendor Data Book (QLT-021); Logistics/Shipping Plan (PRQ-013); SPIR (PRQ-015); Final Vendor Data Book (PRQ-016) | 26020-Package_Requirements.docx package heading 44; Vendor Engineering Deliverables table |
| Category — Core package engineering | Mechanical Design Basis (MEC-001); Mechanical Equipment List (MEC-002); Equipment Data Sheets (MEC-003); Package Equipment Specifications (MEC-006); Mechanical Calculation Package (MEC-014); GA Drawing (MEC-016); Installation/Setting Drawings (MEC-017); Lifting/Handling Study (MEC-018); FAT Procedure (MEC-021); FAT Report (MEC-022); Mechanical Final Data Book (MEC-023); Spares/Special Tools (MEC-024); IOM Manual (MEC-025) | 26020-Package_Requirements.docx package heading 44; Vendor Engineering Deliverables table |
| Category — Rotating equipment / pumps | Rotating Equipment Specifications (MEC-004); Pump Data Sheets (MEC-007); Mechanical Seal / Lube Oil Specification (MEC-019); additional rotating-equipment rows under DEL-091-05 | 26020-Package_Requirements.docx package heading 44; Vendor Engineering Deliverables table |
| Additional categories | Further vendor document category groups (electrical, instrumentation, piping, structural, HSE, commissioning/turnover) are carried as `Vendor Documentation Category Evidence` rows where the source vendor-document table requires them | GATE-07 ARTIFACT_REGISTER.csv; full row enumeration TBD (location TBD — depends on inaccessible DOCX heading 44 text) |
| Turnover records | Manufacturing Record Book / Vendor Data Book (QLT-021); Inspection Release Certificate (QLT-020); Final Vendor Data Book (PRQ-016) | 26020-Package_Requirements.docx package heading 44; Vendor Engineering Deliverables table |

Exact text and per-row required/optional flagging of the source `Vendor Engineering Deliverables` table is **location TBD** — the source DOCX (`_Sources/26020-Package_Requirements.docx`) is not locally accessible as text in this run. The snapshot ARTIFACT_REGISTER is the authoritative derivative.

## References

- `_REFERENCES.md` (deliverable-local pointer set)
- GATE-07 ARTIFACT_REGISTER (`_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/ARTIFACT_REGISTER.csv`) — DEL-091-05 rows
- GATE-07 DELIVERABLE_REGISTER (same snapshot)
- GATE-07 PROJECT_DECOMP.md — Gate 5 deliverable basis and DEC-004/DEC-006/DEC-012
- SOW-0185, SOW-0186, SOW-0187, SOW-0188 (snapshot scope rows)
- `_Sources/26020-Package_Requirements.docx` package heading 44 — Vendor Engineering Deliverables table (**source slice location TBD; DOCX not locally readable as text in this run**)
