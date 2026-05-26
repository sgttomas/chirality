# Specification — DEL-049-05 Vendor Document Turnover Package

## Scope

### In scope
- Vendor-produced document register/index for the Sales Gas Booster Compressor package (26020-01-PT-12-004).
- All vendor engineering, quality, manufacturing, inspection, FAT/SAT, IOM, spares, logistics, and final documentation submittals required by the source Vendor Engineering Deliverables list.
- Submittal control (transmittals, revisions, status codes, hold/approve/work-from cycle).
- Turnover records (Manufacturing Record Book, Inspection Release Certificate, Final Vendor Data Book) at completion of FAT, shipping, and site acceptance.
- EPC Integrator interface/integration review and document acceptance log.

### Out of scope
- Production of the physical equipment package itself (covered by DEL-049-04 Vendor Engineered Equipment Package).
- EPC-Integrator-authored Scope of Work, Package Datasheet, and Construction Work Package (DEL-049-01, -02, -03).
- Final EPC package acceptance authority (DEL-049-06 EPC Vendor Package Review and Acceptance).
- Authoring the deliverable lists themselves; this deliverable consumes the lists fixed by the source package specification and the EPC Package Datasheet.

## Requirements

| Req ID | Requirement | Source | Verification |
|---|---|---|---|
| R-01 | The vendor shall produce and maintain a Vendor Document Index (PRQ-009) covering every document listed below and any additional documents required by the executed RFQ. | 26020-Package_Requirements.docx §26020-01-PT-12-004 "Vendor Engineering Deliverables" — Core vendor documents | Verify index lists every required document ID, current revision, status, and submittal date. |
| R-02 | The vendor shall follow a documented Vendor Document Control Procedure (DOC-008). | Same source | Verify procedure exists, is current, and is being applied to live submittals. |
| R-03 | The vendor shall produce a Supplier Quality Plan (QLT-006) and an Inspection and Test Plan (QLT-003) covering the compressor package, motor, air cooler, suction scrubbers, packing vent/drain pot, seal pot transfer pump, and filter coalescer. | 26020-Package_Requirements.docx §26020-01-PT-12-004 "Major Included Equipment" + "Vendor Engineering Deliverables" | Witness/hold points executed per the ITP; ITP signed off. |
| R-04 | Material Test Reports and Certificates (QLT-013) shall be provided for pressure-retaining components. | Same source | MTRs match material specs in MEC-005/MEC-009. |
| R-05 | An Inspection Release Certificate (QLT-020) shall be issued before shipment. | Same source | Signed IRC included in turnover package. |
| R-06 | A Manufacturing Record Book / Vendor Data Book (QLT-021) shall be assembled and submitted. | Same source | MRB completeness check against the document index. |
| R-07 | A Logistics / Shipping Plan (PRQ-013) shall be issued before shipping. | Same source | Plan reviewed and accepted by EPC Integrator. |
| R-08 | A Spare Parts Interchangeability Record (PRQ-015) shall be provided. | Same source | SPIR submitted, covers commissioning and 2-year operating spares (ASSUMPTION on duration; vendor RFQ governs). |
| R-09 | A Final Supplier Documentation / Vendor Data Book (PRQ-016) shall be the definitive turnover deliverable. | Same source | Final VDB accepted by EPC Integrator. |
| R-10 | Mechanical discipline documents MEC-001..MEC-025 shall be submitted per the source list (Design Basis, Equipment List, Data Sheets, Specifications, Calculations, GA Drawings, Installation/Setting Drawings, Lifting Study, FAT Procedure & Report, Final Mechanical VDB, Spares/Special Tools, IOM Manual). | 26020-Package_Requirements.docx §26020-01-PT-12-004 "Vendor Engineering Deliverables" — Core package engineering | Document-by-document acceptance log; FAT report attached and signed. |
| R-11 | Rotating-equipment documents MEC-004, MEC-008, MEC-019, ELE-011 (Motor Starting Study), and REG-022 (Pressure Equipment Registration Package) shall be submitted. | Same source — Rotating equipment / compressors | Items present, signed, and pressure-equipment registration accepted by applicable jurisdiction (jurisdiction TBD). |
| R-12 | Static pressure equipment documents MEC-005 (Static Equipment Specifications) and MEC-009 (Pressure Vessel Data Sheets) shall be submitted for the suction scrubbers, packing vent/drain pot, and seal pot to the extent they are pressure vessels. | Same source — Static pressure equipment | Vessel data sheets reconcile to MEC-003 equipment data sheets. |
| R-13 | Heat-transfer equipment document MEC-010 (Heat Exchanger Data Sheets) shall be submitted for the forced-air intercoolers. | Same source — Heat transfer equipment | Data sheet matches API 661 forced-air cooler basis. |
| R-14 | Relief and flare design documents PRO-014..PRO-018 shall be submitted (Design Basis, PSV Sizing Calcs, RV Data Sheets, Flare Load Summary, Blowdown Study). | Same source — Relief / flare / vent design | PSV data sheets and sizing tied to interface declared in §"Physical Interface Summary" — Relief/Flare/Vent = Yes. |
| R-15 | Process piping documents (PRO-008 P&IDs; PIP-003 Line List; PIP-004 Tie-In List; PIP-006/007/008/009 GA, plans, isometrics; PIP-017 MTO; PIP-018 Valve Data Sheets; PIP-024 Hydrotest packages; PIP-025 Cleaning Procedure; PIP-028 Piping As-Builts) shall be submitted. | Same source — Process piping interfaces | Tie-In List reconciles with EPC Construction Work Package (DEL-049-03). |
| R-16 | Utility piping summary PRO-011 (Utility Summary / Consumption Report) shall be submitted. | Same source — Utility piping interfaces | Consumption matches Package Datasheet (DEL-049-02). |
| R-17 | Drainage/containment documents PRO-023 (Process Sewer / Closed Drain Design Basis) and CIV-014 (Bund/Dike/Secondary Containment Drawings) shall be submitted where the package has drain interfaces. | Same source — Drainage / containment interfaces; §"Physical Interface Summary" — Drain/Containment = Yes | Drains traced to closed-drain header per EPC Construction Work Package. |
| R-18 | Electrical, lighting, EHT, and grounding documents (ELE-002 Load List; ELE-003 SLDs; ELE-014 Cable Schedule; ELE-015 Cable Tray Routing; ELE-016 Layout Drawings; ELE-020 Equipment Data Sheets; ELE-027 Installation Details; ELE-028 Interconnection Diagrams; ELE-029 FAT/SAT Procedure; ELE-030 Test Records / Energization Package; ELE-017 Lighting Layout; ELE-018 EHT Design Package; PIP-020 Insulation/Heat Tracing Schedule; PIP-021 Piping Heat Tracing Interface Package; ELE-012 Grounding Study; ELE-019 Earthing/Bonding Layout) shall be submitted per source. | Same source — Electrical, lighting, EHT, grounding | Documents reconcile to interface table; motor starting study consistent with 6,700 hp / 4,000 V driver basis (DBM) vs the lower 1,000 kW driver basis in RFQ — see Conflict Table in Guidance.md. |
| R-19 | All submittals shall identify document ID, title, revision, status code, transmittal number, and date; revision history shall be preserved. | ASSUMPTION (industry-standard document control; specific status code set TBD) | Sample audit of any five submittals. |
| R-20 | The turnover package shall be submitted to and accepted by the EPC Integrator. Acceptance is recorded in DEL-049-06 Vendor Document Review Log and Acceptance Checklist. | DELIVERABLE_REGISTER.csv (Gate-07) — DEL-049-05 and DEL-049-06 | Acceptance log signed by EPC Integrator. |

## Standards

| Standard | Applicability | Location |
|---|---|---|
| API 661 | Forced-air intercooler basis | 26020-Package_Requirements.docx §26020-01-PT-12-004 "Major Included Equipment" (Air Cooler) |
| NEMA MG 1 | Compressor motor testing/labeling | 4-25_Deepcut_DBM.md "Sales Gas Booster Compressor Basis" |
| Local pressure equipment registration code (e.g., ABSA in Alberta) | Pressure equipment registration package REG-022 | ASSUMPTION (jurisdiction TBD; West Doe site implies Alberta but not confirmed in accessible source slice) |
| Vendor RFQ-imposed codes/standards (additional) | Per RFQ | TBD — `RFQ/Bid Docs/26020-01-PT-RFQ-12-004-Sales Booster Comp.docx` not parsed in this run |

## Verification

| Verification Method | Used For |
|---|---|
| Document-level review and status coding (work-from / approved / not-approved / for-info) | All vendor engineering submittals |
| Witness/hold inspection per ITP | QLT-003, QLT-013, QLT-020 |
| FAT execution and report | MEC-021, MEC-022, ELE-029 |
| Pre-shipment inspection release | QLT-020 |
| Manufacturing Record Book audit (completeness vs index) | QLT-021 |
| Site Acceptance Test / energization | ELE-029, ELE-030 |
| Final Vendor Data Book acceptance | PRQ-016, MEC-023 |
| EPC Integrator acceptance log | All; recorded in DEL-049-06 |

## Documentation

Outputs of this deliverable:
- Vendor Document Index (PRQ-009) — controlled register of every required document with current status.
- Submitted vendor documents per Requirements R-01..R-18.
- Transmittal records (incoming and outgoing).
- Turnover records: QLT-020 IRC, QLT-021 MRB, PRQ-016 Final VDB, MEC-023 Mechanical Final Documentation VDB.
- EPC Integrator review/acceptance log (DEL-049-06 consumes this; this deliverable supplies the documents).
