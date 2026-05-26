# Datasheet — DEL-056-05 Vendor Document Turnover Package (PKG-056 Inlet Separators 4-25)

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-056-05_vendor-document-turnover-package` | `_CONTEXT.md` |
| Name | Vendor Document Turnover Package | `_CONTEXT.md` |
| ParentPackageID | `PKG-056` | `_CONTEXT.md` |
| ParentWorkbookID | 56 | `_CONTEXT.md` |
| Package Name | Inlet Separators 4-25 | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row 68 |
| Facility | West Doe Deepcut expansion (04-25) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |
| Discipline | Mechanical | `_CONTEXT.md` |
| Deliverable Type | Vendor Document Turnover | `_CONTEXT.md` |
| Responsible Party | Package Vendor (vendor documentation), with EPC Integrator interface/integration review | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row for DEL-056-05 |
| Source Basis | Workbook Packages row 68; `26020-Package_Requirements.docx` package heading 11 | `_CONTEXT.md`; `_REFERENCES.md` |
| Scope Items Covered | `SOW-0127`, `SOW-0128`, `SOW-0129`, `SOW-0130` | `_CONTEXT.md` |
| Supports Objectives | `OBJ-001`, `OBJ-003`–`OBJ-010` (ASSUMPTION: PACKAGE_HEURISTIC) | `_CONTEXT.md`; `OBJECTIVE_DELIVERABLE_MAP.csv` |

## Attributes (Turnover Package Composition)

The package is a vendor-authored deliverable set that documents, in turnover form, all engineering, design, fabrication, inspection, test, certification, and operating information required to receive, install, commission, operate, and maintain the inlet separator packages.

| Attribute | Value | Source |
|---|---|---|
| Vendor authority | Package Vendor owns package engineering, package design, and vendor documentation | `PACKAGE_REGISTER.csv` row 68; mirrored in `DELIVERABLE_REGISTER.csv` row for DEL-056-05 |
| Integrator authority | EPC Integrator reviews vendor documents for integration/interface acceptance | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row for DEL-056-05 |
| Required register | Vendor document register (master index of all vendor documents and their status) | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` §Mechanical packages (line ~617) — "Package deliverables shall include … vendor document registers" |
| Required content (cross-package basis) | Datasheets, cause-and-effect inputs, utility load summaries, relief/load data, field tie-in lists, operating and design envelopes, sparing philosophy, materials and coating basis, maintenance access, shipped-loose item lists, and vendor document registers | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 617 |
| Package-specific source heading | `26020-Package_Requirements.docx` package heading 11 — location TBD (DOCX content not locally extracted to markdown at time of drafting) | `_CONTEXT.md`; `_REFERENCES.md` |
| Submittal lifecycle | Issue-for-Review → Issue-for-Approval → Issue-for-Construction → As-Built / Turnover (ASSUMPTION: standard vendor submittal lifecycle; package-specific lifecycle requirements TBD pending `26020-Package_Requirements.docx` heading 11 extraction) | ASSUMPTION |
| Turnover records | Final inspection records, hydrotest/pressure-test records, NDE records, coating inspection records, factory acceptance test records, certified material test reports, weld maps, calibration certificates, nameplate photos, and as-built drawings (ASSUMPTION: typical mechanical-package turnover record set; package-specific list TBD) | ASSUMPTION; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 617 |

## Conditions (Applicability)

| Item | Value | Source |
|---|---|---|
| Applies to equipment | Two (2) horizontal three-phase HP inlet separators (V-1600-1, V-1700-1) and associated package equipment (PCVs, weirs, mist eliminators, liquid outlet heaters, self-framing buildings) | `ARTIFACT_REGISTER.csv` (ART-ECFD6FDCD9); `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §Inlet separator system |
| Coating | Devchem 253 internal coating on vessels (excluding piping) — coating inspection records expected as turnover content | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 646 |
| Pressure design basis | Inlet skid 600# flange equivalence; inlet PCV-upstream MAWP matched to upstream pipeline (1440 psig assumed); downstream 1360 psig — pressure-test and material records align to these bases | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 628 |
| Quantity conflict carried | Current basis is two installed packages; legacy references describe four inlet separator packages — unresolved | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 589 |

## Construction (Submittal / Document Categories Anticipated)

The vendor document set is anticipated to include the following categories. The package-specific required-deliverables list lives in `26020-Package_Requirements.docx` heading 11 (location TBD until that source is extracted) and shall govern when available.

| Category | Examples | Notes |
|---|---|---|
| Engineering | Equipment datasheets, process datasheets, sizing calculations, mechanical calculations, pressure-vessel calculations, relief-load contributions | Cross-references DEL-056-02 Package Datasheet; ASSUMPTION on contents pending heading 11 |
| Design | GA drawings, plot/elevation drawings, P&IDs (vendor portion), instrument loop diagrams, electrical schematics, cable schedules, junction-box layouts, building drawings (self-framing enclosure) | ASSUMPTION pending heading 11 |
| Fabrication & QA | Material test reports, weld procedure specifications (WPS/PQR), welder qualification records, NDE reports (RT/UT/MT/PT), heat-treatment records, coating-application QA, hydrotest reports | ASSUMPTION; supported by DBM §Inlet separator coating/construction (line 646) |
| Inspection & Certification | ASME Code stamp documentation, CRN/jurisdictional registration certificates, third-party inspection reports, nameplate photos | ASSUMPTION pending heading 11 |
| Test | Factory acceptance test (FAT) procedures and records, instrument calibration certificates, site acceptance test (SAT) inputs | ASSUMPTION pending heading 11 |
| Operating & Maintenance | Operating manuals, maintenance manuals, spare-parts lists, lubrication schedules, special-tool lists, vendor recommended spares | ASSUMPTION pending heading 11 |
| Interface deliverables | Cause-and-effect inputs, utility load summaries, relief/load data, field tie-in lists, shipped-loose item lists | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 617 |
| Register | Master vendor document register (VDR) including document number, title, revision, status, transmittal, date, and EPC review code | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 617 |
| As-Built & Turnover | Marked-up as-built drawings, final certified drawings, redlines, turnover record book, certificate of conformance | ASSUMPTION pending heading 11 |

## References

- `_CONTEXT.md`
- `_REFERENCES.md`
- `_DEPENDENCIES.md`
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv`
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/ARTIFACT_REGISTER.csv`
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (line ~617 — package deliverable basis)
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (inlet separator system context)
- `_Sources/26020-Package_Requirements.docx` package heading 11 — **location TBD** (DOCX not extracted to markdown at time of drafting; package-specific required-deliverables list resides here)
