# Specification — DEL-066-05 Vendor Document Turnover Package

## Scope

### In scope
- Vendor-produced document register/index for the 4-25 condensate storage tank package (26020-01-PT-19-004; tanks TK-9110-1 through TK-9150-1).
- All vendor engineering, quality, manufacturing, inspection, hydrotest/SAT, IOM, spares, logistics, and final documentation submittals required by the source Vendor Engineering Deliverables list.
- Submittal control (transmittals, revisions, status codes, hold/approve/work-from cycle).
- Turnover records (Manufacturing Record Book, Inspection Release Certificate, Final Vendor Data Book) at completion of fabrication, hydrotest, and site acceptance.
- EPC Integrator interface/integration review and document acceptance log.

### Out of scope
- Production of the physical tanks themselves (covered by DEL-066-04 Vendor Engineered Equipment Package).
- EPC-Integrator-authored Scope of Work, Package Datasheet, and Construction Work Package (DEL-066-01, -02, -03).
- Final EPC package acceptance authority (DEL-066-06 EPC Vendor Package Review and Acceptance).
- Authoring the deliverable lists themselves; this deliverable consumes the lists fixed by the source package specification and the EPC Package Datasheet.

## Requirements

| Req ID | Requirement | Source | Verification |
|---|---|---|---|
| R-01 | The vendor shall produce and maintain a Vendor Document Index (PRQ-009) covering every document listed below and any additional documents required by the executed RFQ. | 26020-Package_Requirements.docx §26020-01-PT-19-004 "Vendor Engineering Deliverables" — Core vendor documents | Verify index lists every required document ID, current revision, status, and submittal date. |
| R-02 | The vendor shall follow a documented Vendor Document Control Procedure (DOC-008). | Same source | Verify procedure exists, is current, and is being applied to live submittals. |
| R-03 | The vendor shall produce a Supplier Quality Plan (QLT-006) and an Inspection and Test Plan (QLT-003) covering tank shell, bottom, roof, nozzles, internals, and appurtenances. | Same source | Witness/hold points executed per the ITP; ITP signed off. |
| R-04 | Material Test Reports and Certificates (QLT-013) shall be provided for shell, bottom, roof, and pressure/leak-tight components. | Same source | MTRs match material specs in MEC-005/MEC-011. |
| R-05 | An Inspection Release Certificate (QLT-020) shall be issued before shipment of shop-fabricated components (or before site-erection turnover for field-erected tanks). | Same source | Signed IRC included in turnover package. |
| R-06 | A Manufacturing Record Book / Vendor Data Book (QLT-021) shall be assembled and submitted. | Same source | MRB completeness check against the document index. |
| R-07 | A Logistics / Shipping Plan (PRQ-013) shall be issued before shipping shop-fabricated sub-assemblies and field-erection materials. | Same source | Plan reviewed and accepted by EPC Integrator. |
| R-08 | A Spare Parts Interchangeability Record (PRQ-015) shall be provided. | Same source | SPIR submitted; covers commissioning and operating spares (ASSUMPTION on duration; vendor RFQ governs). |
| R-09 | A Final Supplier Documentation / Vendor Data Book (PRQ-016) shall be the definitive turnover deliverable. | Same source | Final VDB accepted by EPC Integrator. |
| R-10 | Mechanical discipline documents MEC-001..MEC-025 shall be submitted per the source list (Design Basis, Equipment List, Data Sheets, Specifications, Calculations, GA Drawings, Installation/Setting Drawings, Lifting Study, FAT Procedure & Report, Final Mechanical VDB, Spares/Special Tools, IOM Manual). | 26020-Package_Requirements.docx §26020-01-PT-19-004 "Vendor Engineering Deliverables" — Core package engineering | Document-by-document acceptance log; FAT/hydrotest report attached and signed. |
| R-11 | Storage-tank documents MEC-005 (Static Equipment Specifications) and MEC-011 (Storage Tank Data Sheets) shall be submitted for each of the five condensate tanks. | Same source — Storage tanks | Tank data sheets reconcile to MEC-003 equipment data sheets and to the DBM tank roster (TK-9110-1..TK-9150-1). |
| R-12 | Relief and flare design documents PRO-014..PRO-018 shall be submitted (Design Basis, PSV Sizing Calcs, RV Data Sheets, Flare Load Summary, Blowdown Study) addressing PVRV/EPRV sizing and VRU header connection. | Same source — Relief/flare/vent design; 4-25_Deepcut_DBM.md line 1663 (PVRV/EPRV; VRU suction header; API 2000 for blanket gas rates) | PSV/PVRV data sheets and sizing tied to interface declared "Relief/Flare/Vent = Yes" in source Physical Interface Summary. |
| R-13 | Process piping documents (PRO-008 P&IDs; PIP-003 Line List; PIP-004 Tie-In List; PIP-006/007/008/009 GA, plans, isometrics; PIP-017 MTO; PIP-018 Valve Data Sheets; PIP-024 Hydrotest packages; PIP-025 Cleaning Procedure; PIP-028 Piping As-Builts) shall be submitted. | Same source — Process piping interfaces | Tie-In List reconciles with EPC Construction Work Package (DEL-066-03). |
| R-14 | Drainage/containment documents PRO-023 (Process Sewer / Closed Drain Design Basis) and CIV-014 (Bund/Dike/Secondary Containment Drawings) shall be submitted. | Same source — Drainage/containment interfaces; source Physical Interface Summary — Drain/Containment = Yes | Drains traced to closed-drain header per EPC Construction Work Package; bund/dike drawings reconcile with civil grading. |
| R-15 | Electrical, lighting, EHT, and grounding documents (ELE-017 Lighting Layout; ELE-012 Grounding Study; ELE-019 Earthing/Bonding Layout) shall be submitted. | Same source — Electrical, lighting, EHT, grounding; source Physical Interface Summary — Electrical Power = No; Lighting = Yes; EHT = No; Grounding = Yes | Documents reconcile to declared interface table. No tank-power scope expected (per source "Electrical Power = No"); confirm via Conflict Table if tank-level instrument power is required. |
| R-16 | Cathodic protection documents PLN-015 (Corrosion Protection Design Basis) and PLN-016 (Cathodic Protection Design Package) shall be submitted. | Same source — Cathodic protection interfaces; source Physical Interface Summary — Cathodic Protection = Yes | CP package addresses tank-bottom underside protection scheme and external metal grounding compatibility. |
| R-17 | Instrumentation and controls documents (INS-002, INS-003, INS-005, INS-006, INS-008, INS-009, INS-010, INS-011, INS-016, INS-017, INS-018, INS-025, INS-029, CTL-003, CTL-005, CTL-006, CTL-026) shall be submitted. | Same source — Instrumentation and controls interfaces; source Physical Interface Summary — I&C/Control Cabling = Yes | Loop diagrams, hook-ups, and I/O list reconcile with DCS architecture; vendor interface spec (CTL-026) accepted by EPC. |
| R-18 | Structural documents (STR-001, STR-002, STR-004, STR-005, STR-006, STR-011, STR-012, STR-013, STR-014, STR-020) shall be submitted. | Same source — Structural, foundations, supports, access | Foundation drawings and anchor-bolt embedment reconcile with civil ring-wall / pile design; lifting/transport analysis covers erection sequence. |
| R-19 | Civil grading and spill-containment interface documents (CIV-003, CIV-004, CIV-015, CIV-019) shall be submitted where vendor scope crosses the bund boundary. | Same source — Civil grading / spill containment interfaces; source Physical Interface Summary — Grading/Site Drainage/Spill Containment = Yes | Grading and retention-basin design reconcile with bund/dike drawings (CIV-014) and process closed-drain (PRO-023). |
| R-20 | All submittals shall identify document ID, title, revision, status code, transmittal number, and date; revision history shall be preserved. | ASSUMPTION (industry-standard document control; specific status code set TBD) | Sample audit of any five submittals. |
| R-21 | The turnover package shall be submitted to and accepted by the EPC Integrator. Acceptance is recorded in DEL-066-06 EPC Vendor Package Review and Acceptance. | DELIVERABLE_REGISTER.csv (Gate-07) — DEL-066-05 and DEL-066-06 | Acceptance log signed by EPC Integrator. |

## Standards

| Standard | Applicability | Location |
|---|---|---|
| API 650 (modified) | Atmospheric condensate storage tank design and fabrication | 4-25_Deepcut_DBM.md line 1646 "Condensate tank specification — Modified API 650"; 26020-Package_Requirements.docx §26020-01-PT-19-004 "Major Included Equipment" |
| API 2000 | Tank venting / blanket gas sizing | 4-25_Deepcut_DBM.md line 1663 "API 2000 is used for blanket gas rates" |
| Local pressure/atmospheric equipment registration code (e.g., ABSA in Alberta) | If applicable to API 650 modified tanks under the jurisdiction's pressure scope | ASSUMPTION (jurisdiction TBD; West Doe site implies Alberta but not confirmed in accessible source slice) — see Conflict Table |
| Vendor RFQ-imposed codes/standards (additional) | Per RFQ | TBD — 4-25 package RFQ not yet issued per source basis note; analog 3-25 RFQ (`26020-03-PT-RFQ-19-006`) not parsed in this run |

## Verification

| Verification Method | Used For |
|---|---|
| Document-level review and status coding (work-from / approved / not-approved / for-info) | All vendor engineering submittals |
| Witness/hold inspection per ITP | QLT-003, QLT-013, QLT-020 |
| Hydrotest execution and report (in lieu of conventional FAT for field-erected tanks) | MEC-021, MEC-022 (interpreted as hydrotest procedure/report for tank scope) |
| Pre-shipment / pre-erection inspection release | QLT-020 |
| Manufacturing Record Book audit (completeness vs index) | QLT-021 |
| Site Acceptance / commissioning verification (blanket gas, PVRV/EPRV setting, instrumentation loop checks) | INS-008, CTL-005 |
| Final Vendor Data Book acceptance | PRQ-016, MEC-023 |
| EPC Integrator acceptance log | All; recorded in DEL-066-06 |

## Documentation

Outputs of this deliverable:
- Vendor Document Index (PRQ-009) — controlled register of every required document with current status.
- Submitted vendor documents per Requirements R-01..R-19.
- Transmittal records (incoming and outgoing).
- Turnover records: QLT-020 IRC, QLT-021 MRB, PRQ-016 Final VDB, MEC-023 Mechanical Final Documentation VDB.
- EPC Integrator review/acceptance log (DEL-066-06 consumes this; this deliverable supplies the documents).
