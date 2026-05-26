# Datasheet: DEL-086-05_vendor-document-turnover-package — Vendor Document Turnover Package

> Descriptive datasheet for the Package Vendor's document deliverables (register, submittals, source-required vendor documentation, and turnover records) for PKG-086 (Flare Stack — Low Pressure). Values are grounded in the Gate 7 PROJECT_DECOMP snapshot registers and the locally accessible 4-25 Deepcut DBM source. Source slices not yet copied into the deliverable folder are marked `location TBD` or `TBD`.

## Identification

| Attribute | Value | Source |
|---|---|---|
| DeliverableID | `DEL-086-05_vendor-document-turnover-package` | `DELIVERABLE_REGISTER.csv` row DEL-086-05 |
| Deliverable Name | Vendor Document Turnover Package | `DELIVERABLE_REGISTER.csv` |
| Deliverable Type | Vendor Document Turnover | `DELIVERABLE_REGISTER.csv` |
| Parent Package | `PKG-086` — Flare Stack (Low Pressure) | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Parent Workbook Row | 59 | `_CONTEXT.md` |
| Discipline | Mechanical | `_CONTEXT.md` |
| Responsible Party | Package Vendor (vendor documentation) with EPC Integrator interface/integration review | `DELIVERABLE_REGISTER.csv`; `_CONTEXT.md` |
| Source Basis | Workbook Packages row 59; 26020-Package_Requirements.docx package heading 39 | `_CONTEXT.md`; `_REFERENCES.md` |
| Gate Classification | Additional Gate 5 deliverable; individual source document rows remain artifacts/evidence, not separate deliverables | `DELIVERABLE_REGISTER.csv` Notes |

## Attributes (Document Package Identity)

| Attribute | Value | Source |
|---|---|---|
| Vendor Document Register | Required artifact owned by Package Vendor; tabulates all vendor-issued documents for PKG-086 | `_CONTEXT.md` Anticipated Artifacts |
| Vendor Document Submittals | Vendor-issued document set (drawings, datasheets, calculations, certifications) | `_CONTEXT.md` Anticipated Artifacts |
| Source-Required Vendor Documentation | Vendor documents explicitly required by the source basis (26020 Package Requirements, package heading 39); itemized list — `location TBD` (source slice not yet copied locally) | `_CONTEXT.md`; `_REFERENCES.md` |
| Turnover Records | Records evidencing handover of vendor documentation to EPC Integrator and end client | `_CONTEXT.md` Anticipated Artifacts |
| EPC Integrator Review Role | Interface/integration review of vendor documents (not authorship) | `DELIVERABLE_REGISTER.csv` ResponsibleParty |
| Document Numbering / Index Convention | TBD — `location TBD` in 26020-Package_Requirements.docx package heading 39 | source slice not yet copied locally |

## Conditions (Applicability and Service Context)

| Condition | Value | Source |
|---|---|---|
| Applicable Equipment Scope | LP flare stack, air-assist blower, pilot, pilot proving, auto-ignition, supplemental fuel gas/dilution gas provisions, stack interface details | `SCOPE_LEDGER.csv` SOW-0093 |
| Service Context | Low-pressure flare relief and disposal system serving amine regeneration, TEG regeneration, VRU, reciprocating compressor seal pot, and other LP equipment | `4-25_Deepcut_DBM.md` Section "Low-pressure flare" (line ~2029) |
| Sour-Service Applicability | ASSUMPTION: likely applies — OBJ-009 carries sour-service safety, relief, flare, blowdown, drain/containment requirements across packages | `OBJECTIVE_REGISTER.csv` OBJ-009; source clause `location TBD` |
| Regulatory / Code Documentation Carry-Through | Thermal-radiation flux (OGPFR Appendix 1, Schedule 1, Sec. 2) and spacing (OGAOM Sec. 9.6.15) compliance evidence must appear in vendor documentation | `4-25_Deepcut_DBM.md` Flare and Incinerator Spacing table (lines 276-289) |
| Turnover Acceptance Threshold | TBD — `location TBD` in 26020-Package_Requirements.docx package heading 39 | source slice not yet copied locally |

## Construction (Document-Set Composition — Best-Effort Inferred)

| Document Category | Applicability | Source / Basis |
|---|---|---|
| Vendor Document Register (master index) | YES | `_CONTEXT.md` Anticipated Artifacts |
| Equipment datasheets (LP flare stack, blower, pilot, auto-ignition) | YES | `SCOPE_LEDGER.csv` SOW-0093 |
| Vendor general arrangement / outline drawings | ASSUMPTION (typical vendor package content) | `location TBD` |
| Vendor calculations (radiation, dispersion, structural, smokeless capacity) | ASSUMPTION (typical vendor package content; aligns with DBM radiation flux criteria) | `4-25_Deepcut_DBM.md` lines 285-286; `location TBD` for vendor content |
| Material certifications (MTRs) for SA-106 LP flare stack and associated components | YES (driven by DBM material spec) | `4-25_Deepcut_DBM.md` LP flare materials table (line 2042) |
| Inspection and test plans / reports (ITPs/ITRs) | ASSUMPTION (typical vendor turnover content) | `location TBD` |
| Operating and maintenance manuals | ASSUMPTION (typical vendor turnover content) | `location TBD` |
| Spare parts list | ASSUMPTION (typical vendor turnover content) | `location TBD` |
| Turnover transmittal records | YES | `_CONTEXT.md` Anticipated Artifacts |
| EPC Integrator review log entries (linkage to DEL-086-06) | YES | `DELIVERABLE_REGISTER.csv` DEL-086-06 |

## Coverage

| Linkage | IDs |
|---|---|
| Covered Scope Ledger Items | `SOW-0091`, `SOW-0092`, `SOW-0093`, `SOW-0094` |
| Supported Objectives | `OBJ-002`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` |
| Sibling Deliverables (same PKG-086) | DEL-086-01 Scope of Work; DEL-086-02 Package Datasheet; DEL-086-03 Construction Work Package; DEL-086-04 Vendor Engineered Equipment Package; DEL-086-06 EPC Vendor Package Review and Acceptance |

## References

- `_CONTEXT.md` (this deliverable)
- `_REFERENCES.md` (this deliverable)
- Gate 7 PROJECT_DECOMP snapshot: `DELIVERABLE_REGISTER.csv`, `PACKAGE_REGISTER.csv`, `SCOPE_LEDGER.csv`, `OBJECTIVE_REGISTER.csv`
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (locally accessible)
- `_Sources/26020-Package_Requirements.docx` (binary, source slices not yet copied locally — `location TBD` for heading 39 details)
