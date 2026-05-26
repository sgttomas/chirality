# Datasheet — DEL-059-05 Vendor Document Turnover Package (PKG-059 Storage Bullets)

> Pass 1/P2 draft. Source-grounded from `_REFERENCES.md` and the GATE-07 PROJECT_DECOMP snapshot. Items not supported by accessible source slices are marked `TBD` or `ASSUMPTION`.

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-059-05_vendor-document-turnover-package` | `_CONTEXT.md`; DELIVERABLE_REGISTER.csv row 466 |
| Name | Vendor Document Turnover Package | `_CONTEXT.md`; DELIVERABLE_REGISTER.csv row 466 |
| ParentPackageID | `PKG-059` | `_CONTEXT.md`; PACKAGE_REGISTER.csv row 83 |
| ParentWorkbookID | 59 | PACKAGE_REGISTER.csv row 83 |
| PackageName | Storage Bullets | PACKAGE_REGISTER.csv row 83 |
| Equipment Tag (RFQ) | 26020-01-PT-17-007 — Pressure Vessels (Storage Bullets) | PACKAGE_REGISTER.csv row 83 (Equipment Tag) |
| Primary Tagged Equipment | Two unstable condensate storage bullets and sixteen LPG product storage bullets (each 3658 mm ID x 42494 mm S/S, nominally 454 m3 / 120,000 US gal at 84% maximum volume, design 1724 kPag at 66 C and full vacuum) | PACKAGE_REGISTER.csv row 83 (Scope); SCOPE_LEDGER.csv SOW-0183 |
| Discipline | Mechanical | `_CONTEXT.md`; PACKAGE_REGISTER.csv row 83 |
| Deliverable Type | Vendor Document Turnover | DELIVERABLE_REGISTER.csv row 466 |
| ResponsibleParty | Package Vendor (vendor documentation) with EPC Integrator interface/integration review | DELIVERABLE_REGISTER.csv row 466; `_CONTEXT.md` |
| Covers Scope Items | SOW-0181; SOW-0182; SOW-0183; SOW-0184 | DELIVERABLE_REGISTER.csv row 466 |
| Supports Objectives | OBJ-001; OBJ-003; OBJ-004; OBJ-005; OBJ-006; OBJ-007; OBJ-008; OBJ-009; OBJ-010 (ASSUMPTION: PACKAGE_HEURISTIC association) | DELIVERABLE_REGISTER.csv row 466; OBJECTIVE_SCOPE_MAP.csv PKG-059 rows |

## Attributes

### Production-Unit Character

| Attribute | Value | Source |
|---|---|---|
| Production unit role | Single Package Vendor production unit covering vendor document register, submittals, source-required vendor documentation, and turnover records, with EPC Integrator review | DELIVERABLE_REGISTER.csv row 466 (Description) |
| Anticipated artifacts | Vendor document register; vendor document submittals; source vendor document table rows as artifacts where available; turnover records | DELIVERABLE_REGISTER.csv row 466 (AnticipatedArtifacts); `_CONTEXT.md` |
| Decomposition note | Individual source document rows remain artifacts/evidence, not separate deliverables | DELIVERABLE_REGISTER.csv row 466 (Notes) |
| Authority basis | Workbook Packages row 83; `26020-Package_Requirements.docx` package heading 14 (Vendor Engineering Deliverables table for the Storage Bullets package); ARTIFACT_REGISTER.csv DEL-059-05 rows (93 rows) | `_CONTEXT.md`; `_REFERENCES.md`; ARTIFACT_REGISTER.csv |

### Vendor Document Register — Source Categories

Categories sourced from ARTIFACT_REGISTER.csv (PKG-059 DEL-059-05 category rows).

| Category | Source |
|---|---|
| Core vendor documents | ARTIFACT_REGISTER.csv ART-17A17ABBAB |
| Core package engineering | ARTIFACT_REGISTER.csv ART-F8AB7F3145 |
| Static pressure equipment | ARTIFACT_REGISTER.csv ART-1589E3D655 |
| Relief / flare / vent design | ARTIFACT_REGISTER.csv ART-AB739621CA |
| Process piping interfaces | ARTIFACT_REGISTER.csv ART-074381B52B |
| Drainage / containment interfaces | ARTIFACT_REGISTER.csv ART-5E3A738B03 |
| Electrical / lighting / EHT / grounding | ARTIFACT_REGISTER.csv ART-CBF9F63F32 |
| Instrumentation and controls interfaces | ARTIFACT_REGISTER.csv ART-A531C12586 |
| Structural / foundations / supports / access | ARTIFACT_REGISTER.csv ART-8B531FF412 |
| Civil grading / spill containment interfaces | ARTIFACT_REGISTER.csv (DEL-059-05 civil category row) |

### Vendor Documents (Source-Listed, Carried as Artifact Rows)

Each item below is a source-listed vendor document carried under this deliverable. Vendor-supplied submittals become turnover evidence at acceptance.

| Vendor Document | Category | Source |
|---|---|---|
| Vendor Document Index | Core vendor documents | ARTIFACT_REGISTER.csv ART-3E0A93243E |
| Vendor Document Control Procedure | Core vendor documents | ARTIFACT_REGISTER.csv ART-D4D95E703A |
| Supplier Quality Plan | Core vendor documents | ARTIFACT_REGISTER.csv ART-28175E803C |
| Inspection and Test Plan (ITP) | Core vendor documents | ARTIFACT_REGISTER.csv ART-80332A9924 |
| Material Test Reports / Certificates | Core vendor documents | ARTIFACT_REGISTER.csv ART-60FC16E7C0 |
| Inspection Release Certificate | Core vendor documents | ARTIFACT_REGISTER.csv ART-82530395D7 |
| Manufacturing Record Book / Vendor Data Book | Core vendor documents | ARTIFACT_REGISTER.csv ART-7C5F07E441 |
| Logistics / Shipping Plan | Core vendor documents | ARTIFACT_REGISTER.csv ART-AAAB57B1FE |
| Spare Parts Interchangeability Record (SPIR) | Core vendor documents | ARTIFACT_REGISTER.csv ART-6EFF59CC86 |
| Vendor Data Book / Final Supplier Documentation | Core vendor documents | ARTIFACT_REGISTER.csv ART-FD677DDDB8 |
| Mechanical Design Basis | Core package engineering | ARTIFACT_REGISTER.csv ART-8418BB3330 |
| Mechanical Equipment List | Core package engineering | ARTIFACT_REGISTER.csv ART-92C4A803B2 |
| Mechanical Equipment Data Sheets | Core package engineering | ARTIFACT_REGISTER.csv ART-6499787236 |
| Package Equipment Specifications | Core package engineering | ARTIFACT_REGISTER.csv ART-205C556E59 |
| Mechanical Calculation Package | Core package engineering | ARTIFACT_REGISTER.csv ART-E971FA5092 |
| Equipment General Arrangement Drawing | Core package engineering | ARTIFACT_REGISTER.csv ART-1717DCA27C |
| Equipment Installation / Setting Drawings | Core package engineering | ARTIFACT_REGISTER.csv ART-F74A8AE436 |
| Lifting / Handling Study for Major Equipment | Core package engineering | ARTIFACT_REGISTER.csv ART-C5E7A42FE8 |
| Equipment FAT / Performance Test Procedure | Core package engineering | ARTIFACT_REGISTER.csv ART-0D1E51ADA7 |
| Equipment FAT / Performance Test Report | Core package engineering | ARTIFACT_REGISTER.csv ART-5098C5E6CC |
| Vendor Data Book / Mechanical Final Documentation | Core package engineering | ARTIFACT_REGISTER.csv ART-1911A026CA |
| Mechanical Spares / Special Tools Requirements | Core package engineering | ARTIFACT_REGISTER.csv ART-66D76789A5 |
| Mechanical Equipment IOM Manual | Core package engineering | ARTIFACT_REGISTER.csv ART-F9AA306B35 |
| Static Equipment Specifications | Static pressure equipment | ARTIFACT_REGISTER.csv ART-0991FCA915 |
| Pressure Vessel Data Sheets | Static pressure equipment | ARTIFACT_REGISTER.csv ART-0D727DA4B4 |
| Pressure Equipment Registration Package | Static pressure equipment | ARTIFACT_REGISTER.csv ART-01EEC704CB |
| Relief and Flare Design Basis | Relief / flare / vent design | ARTIFACT_REGISTER.csv ART-3DDFDEB4CF |
| PSV / Pressure Relief Sizing Calculations | Relief / flare / vent design | ARTIFACT_REGISTER.csv ART-FEBD5A09B8 |
| Relief Valve Data Sheets | Relief / flare / vent design | ARTIFACT_REGISTER.csv ART-666608E5C5 |
| Flare Load Summary / Flare System Study | Relief / flare / vent design | ARTIFACT_REGISTER.csv ART-2387C23874 |
| Blowdown / Depressurization Study | Relief / flare / vent design | ARTIFACT_REGISTER.csv ART-34A9808598 |
| Piping and Instrumentation Diagrams (P&IDs) | Process piping interfaces | ARTIFACT_REGISTER.csv ART-19D47BD356 |
| Piping Line List | Process piping interfaces | ARTIFACT_REGISTER.csv ART-A6F24F8217 |
| Tie-In List / Tie-In Scope Sheets | Process piping interfaces | ARTIFACT_REGISTER.csv ART-D44A00448D |
| Equipment Arrangement / Piping General Arrangement | Process piping interfaces | ARTIFACT_REGISTER.csv ART-6339770319 |
| Piping Plans and Sections | Process piping interfaces | ARTIFACT_REGISTER.csv ART-2BCB6FB9F3 |
| Piping Isometric Drawings | Process piping interfaces | ARTIFACT_REGISTER.csv ART-40CD95CD5A |
| Fabrication Isometrics with BOM | Process piping interfaces | ARTIFACT_REGISTER.csv ART-6D1105FBB0 |
| Piping MTO / Material Take-Off | Process piping interfaces | ARTIFACT_REGISTER.csv ART-FDF078B13E |
| Valve Data Sheets | Process piping interfaces | ARTIFACT_REGISTER.csv ART-D5799064A3 |
| Hydrotest / Pressure Test Packages | Process piping interfaces | ARTIFACT_REGISTER.csv ART-8399187148 |
| Flushing / Cleaning / Drying Procedure | Process piping interfaces | ARTIFACT_REGISTER.csv ART-470E0A3A4F |
| Piping As-Built Drawings | Process piping interfaces | ARTIFACT_REGISTER.csv ART-5C7FD3C46B |
| Process Sewer / Closed Drain Design Basis | Drainage / containment interfaces | ARTIFACT_REGISTER.csv ART-696FE43CDC |
| Bund / Dike / Secondary Containment Drawings | Drainage / containment interfaces | ARTIFACT_REGISTER.csv ART-7571ACB526 |
| Lighting Layout Drawings | Electrical / lighting / EHT / grounding | ARTIFACT_REGISTER.csv ART-4A2D4E42A4 |
| Electrical Heat Tracing Design Package | Electrical / lighting / EHT / grounding | ARTIFACT_REGISTER.csv ART-DF3CF13F2E |
| Piping Insulation / Heat Tracing Schedule | Electrical / lighting / EHT / grounding | ARTIFACT_REGISTER.csv ART-3C8B36C67C |
| Piping Heat Tracing Interface Package | Electrical / lighting / EHT / grounding | ARTIFACT_REGISTER.csv ART-F2FD95B33D |
| Grounding / Earthing Study | Electrical / lighting / EHT / grounding | ARTIFACT_REGISTER.csv ART-31FC8CD884 |
| Earthing / Bonding Layout Drawings | Electrical / lighting / EHT / grounding | ARTIFACT_REGISTER.csv ART-578930A95F |
| Instrument Index | Instrumentation and controls interfaces | ARTIFACT_REGISTER.csv ART-4FE06A0280 |
| Instrument Data Sheets | Instrumentation and controls interfaces | ARTIFACT_REGISTER.csv ART-77D8083958 |
| Instrument Location Plans | Instrumentation and controls interfaces | ARTIFACT_REGISTER.csv ART-A70C0ADAF3 |
| Instrument Hook-Up Drawings | Instrumentation and controls interfaces | ARTIFACT_REGISTER.csv ART-EF91E6AF50 |
| Instrument Loop Diagrams | Instrumentation and controls interfaces | ARTIFACT_REGISTER.csv ART-6976680445 |
| Instrument Wiring / Termination Diagrams | Instrumentation and controls interfaces | ARTIFACT_REGISTER.csv ART-6551E34504 |
| Junction Box / Marshalling Drawings | Instrumentation and controls interfaces | ARTIFACT_REGISTER.csv ART-ADB94ED7F4 |
| Instrument Cable Schedule | Instrumentation and controls interfaces | ARTIFACT_REGISTER.csv ART-095A680A46 |
| Control Valve Data Sheets | Instrumentation and controls interfaces | ARTIFACT_REGISTER.csv ART-C3D3D5B100 |
| On-Off / Shutdown Valve Data Sheets | Instrumentation and controls interfaces | ARTIFACT_REGISTER.csv ART-CC0C2037D0 |
| Instrument I/O List | Instrumentation and controls interfaces | ARTIFACT_REGISTER.csv ART-5203454B4F |
| Instrument MTO / Quantity Take-Off | Instrumentation and controls interfaces | ARTIFACT_REGISTER.csv ART-7D8961466C |
| Instrument As-Built Drawings | Instrumentation and controls interfaces | ARTIFACT_REGISTER.csv ART-E152764041 |
| Control Narrative / Functional Specification | Instrumentation and controls interfaces | ARTIFACT_REGISTER.csv ART-71EC69437A |
| Cause and Effect Matrix | Instrumentation and controls interfaces | ARTIFACT_REGISTER.csv ART-FFC5801D6D |
| DCS I/O List | Instrumentation and controls interfaces | ARTIFACT_REGISTER.csv ART-BDF9704291 |
| Package Vendor Interface Specification | Instrumentation and controls interfaces | ARTIFACT_REGISTER.csv ART-1954E2904C |
| Structural Design Basis | Structural / foundations / supports / access | ARTIFACT_REGISTER.csv ART-C6F5DE52D8 |
| Structural General Arrangement Drawings | Structural / foundations / supports / access | ARTIFACT_REGISTER.csv ART-C12C2E5967 |
| Structural Calculation Package | Structural / foundations / supports / access | ARTIFACT_REGISTER.csv (DEL-059-05 structural row) |
| Foundation Design Calculations | Structural / foundations / supports / access | ARTIFACT_REGISTER.csv (DEL-059-05 structural row) |
| Foundation Drawings | Structural / foundations / supports / access | ARTIFACT_REGISTER.csv (DEL-059-05 structural row) |
| Platform / Access Structure Drawings | Structural / foundations / supports / access | ARTIFACT_REGISTER.csv (DEL-059-05 structural row) |
| Module Structural Drawings | Structural / foundations / supports / access | ARTIFACT_REGISTER.csv (DEL-059-05 structural row) |
| Anchor Bolt / Embedment Drawings | Structural / foundations / supports / access | ARTIFACT_REGISTER.csv (DEL-059-05 structural row) |
| Lifting Lug / Transport Analysis | Structural / foundations / supports / access | ARTIFACT_REGISTER.csv (DEL-059-05 structural row) |
| Structural MTO / Quantity Take-Off | Structural / foundations / supports / access | ARTIFACT_REGISTER.csv (DEL-059-05 structural row) |
| Grading Plan | Civil grading / spill containment interfaces | ARTIFACT_REGISTER.csv (DEL-059-05 civil row) |
| Drainage / Stormwater Management Report | Civil grading / spill containment interfaces | ARTIFACT_REGISTER.csv (DEL-059-05 civil row) |
| Retention Pond / Containment Basin Design | Civil grading / spill containment interfaces | ARTIFACT_REGISTER.csv (DEL-059-05 civil row) |
| Civil MTO / Quantity Take-Off | Civil grading / spill containment interfaces | ARTIFACT_REGISTER.csv (DEL-059-05 civil row) |

## Conditions

| Parameter | Value | Source |
|---|---|---|
| Document submittal medium | TBD — not stated in accessible source slice | location TBD |
| Submittal language | TBD | location TBD |
| Submittal units convention | ASSUMPTION: SI primary with imperial parenthetical (project convention from DBM) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (general project convention) |
| Required review cycles per document class | TBD | location TBD |
| Code-stamp / registration requirements | Pressure equipment registration applies (each bullet designed for 1724 kPag at 66 C and full vacuum) | SCOPE_LEDGER.csv SOW-0183; ARTIFACT_REGISTER.csv ART-01EEC704CB (Pressure Equipment Registration Package) |
| LPG blanket gas / vapour equalization | LPG bullets require vapour equalization without pockets; butane storage requires blanket gas | SCOPE_LEDGER.csv SOW-0184 |
| Foundations / DCS integration / electrical supply | By others (out of vendor package) | SCOPE_LEDGER.csv SOW-0184 |

## Construction

This deliverable is documentation, not physical construction. "Construction" describes how the documentation package is assembled.

| Element | Value | Source |
|---|---|---|
| Assembly basis | Vendor document register populated from the source `Vendor Engineering Deliverables` table in `26020-Package_Requirements.docx` heading 14 | `_REFERENCES.md`; ARTIFACT_REGISTER.csv ART-EFEEB372EC |
| Category structure | 10 source categories (see Vendor Document Register — Source Categories above) | ARTIFACT_REGISTER.csv (DEL-059-05 category rows) |
| Source row carry-over | Each source vendor-document row is retained as an artifact row (ART-* IDs) rather than promoted to a separate deliverable | DELIVERABLE_REGISTER.csv row 466 (Notes) |
| EPC review interface | EPC Integrator review for facility-level integration is tracked under DEL-059-06 EPC Vendor Package Review and Acceptance | DELIVERABLE_REGISTER.csv row 467 |
| Turnover record set | Final Vendor Data Book / Final Supplier Documentation aggregating accepted submittals | ARTIFACT_REGISTER.csv ART-FD677DDDB8 |

## References

- `_CONTEXT.md` (deliverable identity, scope, anticipated artifacts)
- `_REFERENCES.md` (authoritative decomposition basis and source pointers)
- `_DEPENDENCIES.md` (declared coordination state)
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` row 466
- Same snapshot — `PACKAGE_REGISTER.csv` row 83
- Same snapshot — `SCOPE_LEDGER.csv` rows SOW-0181 through SOW-0184
- Same snapshot — `ARTIFACT_REGISTER.csv` DEL-059-05 rows (93 rows)
- Same snapshot — `OBJECTIVE_SCOPE_MAP.csv` PKG-059 rows
- Source slice: Workbook Packages row 83; `_Sources/26020-Package_Requirements.docx` package heading 14 — carried via decomposition extraction; original `.docx` not opened directly. location TBD for direct slice extraction.
- Word source reference: `Bid Docs/Budgetary/26020-01-PT-RFQ-17-007-_Storage_Bullets.docx` (PACKAGE_REGISTER.csv row 83 Source column)
