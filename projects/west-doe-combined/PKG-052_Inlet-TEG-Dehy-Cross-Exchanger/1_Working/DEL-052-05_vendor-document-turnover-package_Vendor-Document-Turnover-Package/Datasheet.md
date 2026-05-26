# Datasheet — DEL-052-05 Vendor Document Turnover Package (PKG-052 Inlet / TEG Dehy Cross Exchanger)

> Pass 1/P2 draft. Source-grounded from `_REFERENCES.md` and the Gate 7 PROJECT_DECOMP snapshot. Items not supported by accessible source slices are marked `TBD` or `ASSUMPTION`.

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-052-05_vendor-document-turnover-package` | `_CONTEXT.md`; DELIVERABLE_REGISTER.csv row 340 |
| Name | Vendor Document Turnover Package | `_CONTEXT.md`; DELIVERABLE_REGISTER.csv row 340 |
| ParentPackageID | `PKG-052` | `_CONTEXT.md`; PACKAGE_REGISTER.csv row 62 |
| ParentWorkbookID | 52 | PACKAGE_REGISTER.csv row 62 |
| PackageName | Inlet / TEG Dehy Cross Exchanger | PACKAGE_REGISTER.csv row 62 |
| Equipment Tag (RFQ) | 26020-01-PT-16-001 — Inlet TEG Cross Exchanger | PACKAGE_REGISTER.csv row 62 (Equipment Tag) |
| Primary Tagged Equipment | E-5718-1 (Inlet / TEG Dehy Cross Exchanger, TEMA 'R' BEM) | PACKAGE_REGISTER.csv row 62 (Scope); SCOPE_LEDGER.csv SOW-0104 |
| Discipline | Mechanical | `_CONTEXT.md`; PACKAGE_REGISTER.csv row 62 |
| Deliverable Type | Vendor Document Turnover | DELIVERABLE_REGISTER.csv row 340 |
| ResponsibleParty | Package Vendor (vendor documentation) with EPC Integrator interface/integration review | DELIVERABLE_REGISTER.csv row 340; `_CONTEXT.md` |
| Covers Scope Items | SOW-0103; SOW-0104; SOW-0105; SOW-0106 | DELIVERABLE_REGISTER.csv row 340 |
| Supports Objectives | OBJ-001; OBJ-003; OBJ-004; OBJ-005; OBJ-006; OBJ-007; OBJ-008; OBJ-009; OBJ-010 (ASSUMPTION: PACKAGE_HEURISTIC association) | DELIVERABLE_REGISTER.csv row 340; OBJECTIVE_SCOPE_MAP.csv PKG-052 rows |

## Attributes

### Production-Unit Character

| Attribute | Value | Source |
|---|---|---|
| Production unit role | Single Package Vendor production unit covering vendor document register, submittals, source-required vendor documentation, and turnover records, with EPC Integrator review | DELIVERABLE_REGISTER.csv row 340 (Description) |
| Anticipated artifacts | Vendor document register; vendor document submittals; source vendor document table rows as artifacts where available; turnover records | DELIVERABLE_REGISTER.csv row 340 (AnticipatedArtifacts); `_CONTEXT.md` |
| Decomposition note | Individual source document rows remain artifacts/evidence, not separate deliverables | DELIVERABLE_REGISTER.csv row 340 (Notes) |
| Authority basis | Workbook Packages row 62; `26020-Package_Requirements.docx` package heading 7 (Vendor Engineering Deliverables table); ARTIFACT_REGISTER.csv DEL-052-05 rows | `_CONTEXT.md`; `_REFERENCES.md`; ARTIFACT_REGISTER.csv |

### Vendor Document Register — Source Categories

Categories sourced from ARTIFACT_REGISTER.csv (PKG-052 DEL-052-05 category rows).

| Category | Source |
|---|---|
| Core vendor documents | ARTIFACT_REGISTER.csv ART-23228635C4 |
| Core package engineering | ARTIFACT_REGISTER.csv (DEL-052-05 category row) |
| Heat transfer equipment | ARTIFACT_REGISTER.csv (DEL-052-05 category row) |
| Process package design | ARTIFACT_REGISTER.csv (DEL-052-05 category row) |
| Process piping interfaces | ARTIFACT_REGISTER.csv (DEL-052-05 category row) |
| Drainage / containment interfaces | ARTIFACT_REGISTER.csv (DEL-052-05 category row) |
| Electrical | ARTIFACT_REGISTER.csv (DEL-052-05 category row) |
| Instrumentation and controls interfaces | ARTIFACT_REGISTER.csv (DEL-052-05 category row) |
| Structural | ARTIFACT_REGISTER.csv (DEL-052-05 category row) |

### Vendor Documents (Source-Listed, Carried as Artifact Rows)

Each item below is a source-listed vendor document carried under this deliverable. Vendor-supplied submittals become turnover evidence at acceptance.

| Vendor Document | Category | Source |
|---|---|---|
| Vendor Document Index | Core vendor documents | ARTIFACT_REGISTER.csv ART-FF916F10D3 |
| Vendor Document Control Procedure | Core vendor documents | ARTIFACT_REGISTER.csv ART-B9AFEA01D9 |
| Supplier Quality Plan | Core vendor documents | ARTIFACT_REGISTER.csv ART-7F6D2A9FFC |
| Inspection and Test Plan (ITP) | Core vendor documents | ARTIFACT_REGISTER.csv ART-23F5BF5334 |
| Material Test Reports / Certificates | Core vendor documents | ARTIFACT_REGISTER.csv ART-20E0FEF8E1 |
| Inspection Release Certificate | Core vendor documents | ARTIFACT_REGISTER.csv ART-39C7985DAC |
| Manufacturing Record Book / Vendor Data Book | Core vendor documents | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Logistics / Shipping Plan | Core vendor documents | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Spare Parts Interchangeability Record (SPIR) | Core vendor documents | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Vendor Data Book / Final Supplier Documentation | Core vendor documents | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Mechanical Design Basis | Core package engineering | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Mechanical Equipment List | Core package engineering | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Mechanical Equipment Data Sheets | Core package engineering | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Package Equipment Specifications | Core package engineering | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Mechanical Calculation Package | Core package engineering | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Equipment General Arrangement Drawing | Core package engineering | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Equipment Installation / Setting Drawings | Core package engineering | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Lifting / Handling Study for Major Equipment | Core package engineering | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Equipment FAT / Performance Test Procedure | Core package engineering | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Equipment FAT / Performance Test Report | Core package engineering | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Vendor Data Book / Mechanical Final Documentation | Core package engineering | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Mechanical Spares / Special Tools Requirements | Core package engineering | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Mechanical Equipment IOM Manual | Core package engineering | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Static Equipment Specifications | Heat transfer equipment | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Heat Exchanger Data Sheets | Heat transfer equipment | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Pressure Equipment Registration Package | Heat transfer equipment | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Process Flow Diagram (PFD) | Process package design | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Heat and Material Balance | Process package design | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Process Description / Operating Philosophy | Process package design | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Piping and Instrumentation Diagrams (P&IDs) | Process package design | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Major Equipment Process Data Sheets | Process package design | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Utility Summary / Utility Consumption Report | Process package design | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Line Sizing / Hydraulic Calculation Package | Process package design | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Process Control Philosophy | Process package design | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Operating Guidelines / Startup-Shutdown Narrative | Process package design | ARTIFACT_REGISTER.csv (DEL-052-05) |
| HAZOP / PHA Technical Input Package | Process package design | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Process Safety Information (PSI) Package | Process package design | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Process As-Built PFD/P&ID Package | Process package design | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Piping Line List | Process piping interfaces | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Tie-In List / Tie-In Scope Sheets | Process piping interfaces | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Equipment Arrangement / Piping General Arrangement | Process piping interfaces | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Piping Plans and Sections | Process piping interfaces | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Piping Isometric Drawings | Process piping interfaces | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Fabrication Isometrics with BOM | Process piping interfaces | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Piping MTO / Material Take-Off | Process piping interfaces | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Valve Data Sheets | Process piping interfaces | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Hydrotest / Pressure Test Packages | Process piping interfaces | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Flushing / Cleaning / Drying Procedure | Process piping interfaces | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Piping As-Built Drawings | Process piping interfaces | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Process Sewer / Closed Drain Design Basis | Drainage / containment interfaces | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Bund / Dike / Secondary Containment Drawings | Drainage / containment interfaces | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Lighting Layout Drawings | Electrical | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Electrical Heat Tracing Design Package | Electrical | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Piping Insulation / Heat Tracing Schedule | Electrical | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Piping Heat Tracing Interface Package | Electrical | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Grounding / Earthing Study | Electrical | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Earthing / Bonding Layout Drawings | Electrical | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Instrument Index | Instrumentation and controls interfaces | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Instrument Data Sheets | Instrumentation and controls interfaces | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Instrument Location Plans | Instrumentation and controls interfaces | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Instrument Hook-Up Drawings | Instrumentation and controls interfaces | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Instrument Loop Diagrams | Instrumentation and controls interfaces | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Instrument Wiring / Termination Diagrams | Instrumentation and controls interfaces | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Junction Box / Marshalling Drawings | Instrumentation and controls interfaces | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Instrument Cable Schedule | Instrumentation and controls interfaces | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Control Valve Data Sheets | Instrumentation and controls interfaces | ARTIFACT_REGISTER.csv (DEL-052-05) |
| On-Off / Shutdown Valve Data Sheets | Instrumentation and controls interfaces | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Instrument I/O List | Instrumentation and controls interfaces | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Instrument MTO / Quantity Take-Off | Instrumentation and controls interfaces | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Instrument As-Built Drawings | Instrumentation and controls interfaces | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Control Narrative / Functional Specification | Instrumentation and controls interfaces | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Cause and Effect Matrix | Instrumentation and controls interfaces | ARTIFACT_REGISTER.csv (DEL-052-05) |
| DCS I/O List | Instrumentation and controls interfaces | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Package Vendor Interface Specification | Instrumentation and controls interfaces | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Structural Design Basis | Structural | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Structural General Arrangement Drawings | Structural | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Structural Calculation Package | Structural | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Foundation Design Calculations | Structural | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Foundation Drawings | Structural | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Platform / Access Structure Drawings | Structural | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Module Structural Drawings | Structural | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Anchor Bolt / Embedment Drawings | Structural | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Lifting Lug / Transport Analysis | Structural | ARTIFACT_REGISTER.csv (DEL-052-05) |
| Structural MTO / Quantity Take-Off | Structural | ARTIFACT_REGISTER.csv (DEL-052-05) |

## Conditions

| Parameter | Value | Source |
|---|---|---|
| Document submittal medium | TBD — not stated in accessible source slice | location TBD |
| Submittal language | TBD | location TBD |
| Submittal units convention | ASSUMPTION: SI primary with imperial parenthetical (project convention from DBM) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (general project convention) |
| Required review cycles per document class | TBD | location TBD |
| Code-stamp / registration requirements | Pressure equipment registration applies (E-5718-1 at 9,756 kPag design pressure) | SCOPE_LEDGER.csv SOW-0106; ARTIFACT_REGISTER.csv (Pressure Equipment Registration Package row) |

## Construction

This deliverable is documentation, not physical construction. "Construction" describes how the documentation package is assembled.

| Element | Value | Source |
|---|---|---|
| Assembly basis | Vendor document register populated from the source `Vendor Engineering Deliverables` table in `26020-Package_Requirements.docx` heading 7 | `_REFERENCES.md`; ARTIFACT_REGISTER.csv ART-D6A6BE00E1 |
| Category structure | 9 source categories (see Vendor Document Register — Source Categories above) | ARTIFACT_REGISTER.csv (DEL-052-05 category rows) |
| Source row carry-over | Each source vendor-document row is retained as an artifact row (ART-* IDs) rather than promoted to a separate deliverable | DELIVERABLE_REGISTER.csv row 340 (Notes) |
| EPC review interface | EPC Integrator review for facility-level integration is tracked under DEL-052-06 EPC Vendor Package Review and Acceptance | DELIVERABLE_REGISTER.csv row 341 |
| Turnover record set | Final Vendor Data Book / Final Supplier Documentation aggregating accepted submittals | ARTIFACT_REGISTER.csv (DEL-052-05 Vendor Data Book row) |

## References

- `_CONTEXT.md` (deliverable identity, scope, anticipated artifacts)
- `_REFERENCES.md` (authoritative decomposition basis and source pointers)
- `_DEPENDENCIES.md` (declared coordination state)
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` row 340
- Same snapshot — `PACKAGE_REGISTER.csv` row 62
- Same snapshot — `SCOPE_LEDGER.csv` rows SOW-0103 through SOW-0106
- Same snapshot — `ARTIFACT_REGISTER.csv` DEL-052-05 rows
- Same snapshot — `OBJECTIVE_SCOPE_MAP.csv` PKG-052 rows
- Source slice: Workbook Packages row 62; `_Sources/26020-Package_Requirements.docx` package heading 7 (Vendor Engineering Deliverables table) — carried via decomposition extraction; original `.docx` not opened directly
