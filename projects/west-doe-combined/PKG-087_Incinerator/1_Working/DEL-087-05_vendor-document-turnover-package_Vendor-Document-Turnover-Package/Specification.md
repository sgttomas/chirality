# Specification — DEL-087-05 Vendor Document Turnover Package

## Scope

### In scope
- Vendor-produced document register/index for the Incinerator package (26020-Package_Requirements.docx package heading 40).
- All vendor engineering, quality, manufacturing, inspection, FAT/SAT, IOM, spares, logistics, emissions/permit, and final documentation submittals required by the source Vendor Engineering Deliverables list for this package.
- Submittal control (transmittals, revisions, status codes, hold/approve/work-from cycle).
- Turnover records (Manufacturing Record Book, Inspection Release Certificate, Final Vendor Data Book) at completion of FAT, shipping, and site acceptance.
- EPC Integrator interface/integration review and document acceptance log.

### Out of scope
- Production of the physical incinerator equipment package itself (covered by DEL-087-04 Vendor Engineered Equipment Package).
- EPC-Integrator-authored Scope of Work, Package Datasheet, and Construction Work Package (DEL-087-01, -02, -03).
- Final EPC package acceptance authority (DEL-087-06 EPC Vendor Package Review and Acceptance).
- Authoring the deliverable lists themselves; this deliverable consumes the lists fixed by the source package specification and the EPC Package Datasheet.
- Authoring shared-facility service-split rulings between 3-25 and 4-25 for incinerator load allocation (governed elsewhere; see 3-25_Comp_and_Liquids_DBM.md §SEC-08).

## Requirements

| Req ID | Requirement | Source | Verification |
|---|---|---|---|
| R-01 | The vendor shall produce and maintain a Vendor Document Index (PRQ-009) covering every document listed below and any additional documents required by the executed RFQ. | 26020-Package_Requirements.docx heading 40 "Vendor Engineering Deliverables" (location TBD; project-wide convention) | Verify index lists every required document ID, current revision, status, and submittal date. |
| R-02 | The vendor shall follow a documented Vendor Document Control Procedure (DOC-008). | Same source / convention | Verify procedure exists, is current, and is being applied to live submittals. |
| R-03 | The vendor shall produce a Supplier Quality Plan (QLT-006) and an Inspection and Test Plan (QLT-003) covering the incinerator burner/pilot system, refractory or thermal protection, stack, knock-out drum, supplemental fuel-gas piping, and any waste-heat or quench provisions. | 26020-Package_Requirements.docx heading 40 (location TBD); 3-25_Comp_and_Liquids_DBM.md §"Incinerator Interface" (KO drum mention) | Witness/hold points executed per the ITP; ITP signed off. |
| R-04 | Material Test Reports and Certificates (QLT-013) shall be provided for pressure-retaining components (e.g., KO drum) and for high-temperature components (e.g., burner internals, stack). | Same source / convention | MTRs match material specs in MEC-005/MEC-009 (vessels) and MEC-011/MEC-012 (fired equipment). |
| R-05 | An Inspection Release Certificate (QLT-020) shall be issued before shipment. | Same source / convention | Signed IRC included in turnover package. |
| R-06 | A Manufacturing Record Book / Vendor Data Book (QLT-021) shall be assembled and submitted. | Same source / convention | MRB completeness check against the document index. |
| R-07 | A Logistics / Shipping Plan (PRQ-013) shall be issued before shipping. | Same source / convention | Plan reviewed and accepted by EPC Integrator. |
| R-08 | A Spare Parts Interchangeability Record (PRQ-015) shall be provided covering commissioning spares and operating spares (operating duration TBD per RFQ — ASSUMPTION). | Same source / convention | SPIR submitted; coverage confirmed against RFQ. |
| R-09 | A Final Supplier Documentation / Vendor Data Book (PRQ-016) shall be the definitive turnover deliverable. | Same source / convention | Final VDB accepted by EPC Integrator. |
| R-10 | Mechanical discipline documents MEC-001..MEC-025 shall be submitted per the source list (Design Basis, Equipment List, Data Sheets, Specifications, Calculations, GA Drawings, Installation/Setting Drawings, Lifting Study, FAT Procedure & Report, Final Mechanical VDB, Spares/Special Tools, IOM Manual). | 26020-Package_Requirements.docx heading 40 "Vendor Engineering Deliverables" — Core package engineering (location TBD; project-wide convention) | Document-by-document acceptance log; FAT report attached and signed. |
| R-11 | Fired/combustion equipment documents (MEC-011 Fired Equipment Specifications, MEC-012 Burner / Pilot / Ignition Data Sheets, MEC-013 Fired Equipment Performance / Emissions Test Procedure) shall be submitted. | 26020-Package_Requirements.docx heading 40 (location TBD) — fired equipment is the defining package character | Items present and signed; emissions test procedure aligns with PRO-024 permit basis. |
| R-12 | Emissions / permit documentation (PRO-024 Emissions Compliance Calculation / Permit Package) shall be submitted. Permit values themselves are owner/regulator-driven; vendor supplies engineering basis (combustion calculations, expected emissions per source/feed, stack height/diameter rationale, dispersion inputs where in scope). | 3-25_Comp_and_Liquids_DBM.md §SEC-08 (line 555) — "final emissions section requires confirmation of ... incinerator service split ... and any regulatory emissions permit values" | Emissions package reconciles to PRO-024 owner permit and to expected stack performance per MEC-013. |
| R-13 | Pressure equipment registration documentation (REG-022) shall be submitted for the upstream knock-out drum and any other pressure-retaining components meeting applicable jurisdictional thresholds. | 3-25_Comp_and_Liquids_DBM.md §"Incinerator Interface" (KO drum); project-wide REG-022 convention | Jurisdictional acknowledgment letter on file (jurisdiction TBD — see Guidance Conflict Table C-02). |
| R-14 | Relief and vent design documents (PRO-014..PRO-018 as applicable; at minimum PRO-014 Design Basis and PRO-015/PRO-016 PSV sizing/data sheets for any PSV-protected vessels in the package; flame arrestor / detonation arrestor data sheet for incinerator-header tie-ins) shall be submitted. | 3-25_Comp_and_Liquids_DBM.md (lines 402, 1561-1564) — spent-caustic and DSO tanks vent to incinerator through flame arrestors; the vendor package boundary for these arrestors is TBD | PSV/arrestor sizing tied to declared relief loads; reconciled to upstream tank vent system. |
| R-15 | Process piping documents (PRO-008 P&IDs; PIP-003 Line List; PIP-004 Tie-In List; PIP-006/007/008/009 GA, plans, isometrics; PIP-017 MTO; PIP-018 Valve Data Sheets; PIP-024 Hydrotest packages; PIP-025 Cleaning Procedure; PIP-028 Piping As-Builts) for incinerator header inlet, supplemental fuel-gas supply, purge, and any quench/water injection piping shall be submitted. | 26020-Package_Requirements.docx heading 40 "Physical Interface Summary" (location TBD; process and utility piping interfaces inferred from DBM) | Tie-In List reconciles with EPC Construction Work Package (DEL-087-03). |
| R-16 | Utility piping documents (PRO-011 Utility Summary / Consumption Report) shall be submitted, including supplemental fuel-gas consumption and instrument-air demand. | 3-25_Comp_and_Liquids_DBM.md (line 1572) — "Supplemental fuel gas rate, incinerator flow basis ... remain TBD"; project-wide utility-summary convention | Consumption matches Package Datasheet (DEL-087-02). |
| R-17 | Drainage/containment documents (PRO-023 Process Sewer / Closed Drain Design Basis; CIV-014 Bund/Dike/Secondary Containment Drawings) shall be submitted where the package has drain interfaces (KO drum liquid drain at minimum). | 26020-Package_Requirements.docx heading 40 "Physical Interface Summary" (location TBD); KO drum drain inferred from DBM | Drains traced to closed-drain header per EPC Construction Work Package. |
| R-18 | Electrical, controls, fire & gas, lighting, EHT, and grounding documents (ELE-002 Load List; ELE-003 SLDs; ELE-014 Cable Schedule; ELE-015 Cable Tray Routing; ELE-016 Layout Drawings; ELE-020 Equipment Data Sheets for ignition/BMS controllers and any local pumps/fans; ELE-027 Installation Details; ELE-028 Interconnection Diagrams; ELE-029 FAT/SAT Procedure including Burner Management System; ELE-030 Test Records / Energization Package; ELE-017 Lighting Layout; ELE-018 EHT Design Package for any heat-traced incinerator-header or pilot-gas piping; PIP-020 Insulation/Heat Tracing Schedule; PIP-021 Piping Heat Tracing Interface Package; ELE-012 Grounding Study; ELE-019 Earthing/Bonding Layout; ICA-xxx Burner Management System / Safety Instrumented Function documentation) shall be submitted per source. | 26020-Package_Requirements.docx heading 40 "Physical Interface Summary" (location TBD); BMS/SIF is industry-standard for fired equipment (ASSUMPTION pending heading-40 confirmation) | Documents reconcile to interface table; BMS SIF documentation independently reviewed by EPC functional-safety reviewer. |
| R-19 | All submittals shall identify document ID, title, revision, status code, transmittal number, and date; revision history shall be preserved. | ASSUMPTION (industry-standard document control; specific status code set TBD) | Sample audit of any five submittals. |
| R-20 | The turnover package shall be submitted to and accepted by the EPC Integrator. Acceptance is recorded in DEL-087-06 Vendor Document Review Log and Acceptance Checklist. | DELIVERABLE_REGISTER.csv (Gate-07) — DEL-087-05 and DEL-087-06 | Acceptance log signed by EPC Integrator. |

## Standards

| Standard | Applicability | Location |
|---|---|---|
| OGAOM Sec. 9.6.15 | Flare/incinerator spacing and proximity rules — applies to layout/installation context, not directly to vendor documentation, but vendor GA/installation drawings must support compliance verification | 4-25_Deepcut_DBM.md §2.4 (lines 280, 296, 316) |
| OGPFR Appendix 1, Schedule 1, Sec. 2 | Thermal radiation flux limits for flare-class equipment; applicability to the incinerator stack is **ASSUMPTION pending source confirmation** | 4-25_Deepcut_DBM.md §2.4 (lines 285-286) |
| Local pressure equipment registration code (e.g., ABSA in Alberta, TSBC in BC) | REG-022 pressure equipment registration for KO drum | ASSUMPTION (jurisdiction TBD; site is at Dawson Creek BC per 4-25_Deepcut_DBM.md §2.2 line 188 — implies TSBC, but registration scheme governance for this project is **TBD** — see Guidance C-02) |
| Applicable provincial/federal air emissions regulations | PRO-024 emissions package | TBD — owner/regulator-driven; not stated in accessible vendor-doc source slices |
| NFPA 86 / API 535 / API 537 (fired equipment / burner management) | Fired equipment design and BMS | ASSUMPTION (industry convention for incinerators/fired equipment); source confirmation **TBD** at 26020-Package_Requirements.docx heading 40 |
| Vendor RFQ-imposed codes/standards (additional) | Per RFQ | TBD — vendor RFQ for the Incinerator package not identified in accessible sources this run |

## Verification

| Verification Method | Used For |
|---|---|
| Document-level review and status coding (work-from / approved / not-approved / for-info) | All vendor engineering submittals |
| Witness/hold inspection per ITP | QLT-003, QLT-013, QLT-020 |
| FAT execution and report | MEC-021, MEC-022, MEC-013 (emissions/performance), ELE-029 (BMS SAT/FAT) |
| Pre-shipment inspection release | QLT-020 |
| Manufacturing Record Book audit (completeness vs index) | QLT-021 |
| Site Acceptance Test / energization / burner light-off | ELE-029, ELE-030, MEC-013 |
| Emissions/permit basis reconciliation | PRO-024 vs MEC-013 |
| Final Vendor Data Book acceptance | PRQ-016, MEC-023 |
| EPC Integrator acceptance log | All; recorded in DEL-087-06 |

## Documentation

Outputs of this deliverable:
- Vendor Document Index (PRQ-009) — controlled register of every required document with current status.
- Submitted vendor documents per Requirements R-01..R-18.
- Transmittal records (incoming and outgoing).
- Turnover records: QLT-020 IRC, QLT-021 MRB, PRQ-016 Final VDB, MEC-023 Mechanical Final Documentation VDB.
- Fired-equipment-specific records: MEC-013 emissions/performance test report; ELE-029 BMS SAT/FAT report.
- PRO-024 Emissions Compliance Calculation / Permit Package (vendor engineering basis portion).
- EPC Integrator review/acceptance log (DEL-087-06 consumes this; this deliverable supplies the documents).
