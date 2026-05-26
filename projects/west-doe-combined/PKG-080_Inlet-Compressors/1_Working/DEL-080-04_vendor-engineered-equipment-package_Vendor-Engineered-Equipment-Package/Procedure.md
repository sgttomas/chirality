# Procedure: DEL-080-04 — PKG-080 Inlet Compressors Vendor Engineered Equipment Package

> Interpretation: This procedure describes how the Package Vendor produces the engineered equipment package deliverable (engineering, design, fabrication/supply, FAT, turnover) and how the EPC Integrator interacts with that production. Operating procedures for the running compressor packages are produced by the vendor as the IOM Manual (MEC-025) and are not duplicated here.

## Purpose

Define the procedural steps and required records by which the Package Vendor delivers the engineered inlet compressor package, with EPC Integrator integration coordination, such that the package can be accepted by DEL-080-06 (EPC Vendor Package Review and Acceptance) and turned over via DEL-080-05 (Vendor Document Turnover Package).
Source: `_CONTEXT.md`; heading 33 "Vendor Engineering Deliverables".

## Prerequisites

| Prerequisite | Source / Status |
|---|---|
| EPC Scope of Work issued (DEL-080-01) | Sibling deliverable in PKG-080; no formal upstream edge declared in `_DEPENDENCIES.md` (PREPARATION declared no upstream) — ASSUMPTION that DEL-080-01 logically precedes |
| EPC Package Datasheet issued (DEL-080-02) | Sibling deliverable in PKG-080; same ASSUMPTION as above |
| DBM SEC-05 process basis frozen at SCA-001 / SCA-002 supersession state | DBM SEC-05 "Superseded Content Controls" |
| Vendor selection complete | Outside this deliverable; required before kickoff |
| Site environmental basis (SEC-02 ambient, geotechnical) available to vendor | DBM SEC-02 |
| Pressure equipment registration jurisdiction confirmed (BC ASSUMPTION) | DBM SEC-01; `location TBD` for AHJ |

## Steps

### S1 — Vendor Kickoff and Basis Reconciliation
1. EPC Integrator issues the EPC Scope of Work and EPC Package Datasheet to the Package Vendor.
2. Vendor and EPC jointly reconcile open conflicts captured in `Guidance.md` Conflict Table (Conflict-01 model designation; Conflict-02 pressure basis; Conflict-03 recycle valve failure action; Conflict-04 NACE clause-level requirement).
3. Vendor confirms reading of DBM SEC-05 and heading 33 source slices.
Verification: Kickoff meeting minutes; conflict-disposition log.

### S2 — Mechanical Design Basis and Equipment List
1. Vendor produces MEC-001 Mechanical Design Basis aligned with DBM SEC-05.
2. Vendor produces MEC-002 Mechanical Equipment List for the package.
3. Vendor produces MEC-003 / MEC-008 Compressor Data Sheets (process and mechanical).
4. Vendor produces MEC-004 Rotating Equipment Specifications and MEC-019 Mechanical Seal / Lube Oil Specification.
Verification: EPC review against R-080-04-001 through R-080-04-006.

### S3 — Calculations and Detailed Mechanical Design
1. Vendor produces MEC-006 Package Equipment Specifications and MEC-014 Mechanical Calculation Package.
2. Vendor produces MEC-016 Equipment General Arrangement Drawing and MEC-017 Installation / Setting Drawings.
3. Vendor produces MEC-018 Lifting / Handling Study for major equipment.
4. Vendor produces STR-001 Structural Design Basis, STR-004 Structural Calc Package, STR-005 Foundation Design Calcs, STR-006 Foundation Drawings, STR-011 Platform/Access Drawings, STR-012 Module Structural Drawings, STR-013 Anchor Bolt/Embedment Drawings, STR-014 Lifting Lug/Transport Analysis, STR-020 Structural MTO.
Verification: EPC structural and mechanical review.

### S4 — Process Piping, Instrumentation, Relief
1. Vendor produces PRO-008 P&IDs for the package.
2. Vendor produces PIP-003 Piping Line List, PIP-004 Tie-In List, PIP-006 Piping General Arrangement, PIP-007 Piping Plans/Sections, PIP-008 Isometric Drawings, PIP-009 Fabrication Isometrics with BOM, PIP-017 Piping MTO, PIP-018 Valve Data Sheets, PIP-020/021 Heat Tracing schedules and interface packages, PIP-024 Hydrotest Packages, PIP-025 Flushing/Cleaning/Drying Procedure.
3. Vendor produces relief design set: PRO-014 Relief and Flare Design Basis, PRO-015 PSV Sizing, PRO-016 Relief Valve Data Sheets, PRO-017 Flare Load Summary, PRO-018 Blowdown / Depressurization Study.
4. Vendor produces utility set: PRO-011 Utility Summary; drainage/containment items PRO-023, CIV-014 as applicable.
5. Vendor produces instrumentation set: INS-002, INS-003, INS-005, INS-006, INS-008, INS-009, INS-010, INS-011, INS-016, INS-017, INS-018, INS-025; controls set: CTL-003 Control Narrative, CTL-005 Cause and Effect Matrix, CTL-006 DCS I/O List, CTL-026 Package Vendor Interface Specification.
Verification: EPC interface review against R-080-04-008 and R-080-04-012.

### S5 — Electrical and Safety
1. Vendor produces ELE-002, ELE-003, ELE-011 (Motor Starting Study), ELE-014, ELE-015, ELE-016, ELE-017 (Lighting), ELE-018 (EHT), ELE-019 (Earthing/Bonding), ELE-020, ELE-027, ELE-028, ELE-029 (FAT/SAT), ELE-030 (Test Records); ELE-012 Grounding/Earthing Study.
2. Vendor produces fire & gas / technical safety set: TSF-002 F&G Philosophy, TSF-003 F&G Mapping, TSF-004 Detector Layouts, TSF-009 SIL Determination, TSF-011 Safety Requirements Specification, TSF-013 Supplier SIL/Safety Manual, TSF-023 Occupied Building Risk Assessment, TSF-028 Emergency Response Plan Inputs.
3. Vendor produces building/code interfaces: PRO-024, REG-021 (Fire/Building Code Compliance), STR-002 (Structural GA).
Verification: EPC electrical and TSF review.

### S6 — Quality, Procurement, Manufacturing
1. Vendor issues PRQ-009 Vendor Document Index and DOC-008 Vendor Document Control Procedure.
2. Vendor issues QLT-006 Supplier Quality Plan and QLT-003 Inspection and Test Plan.
3. Vendor procures and fabricates per approved deliverables; logs QLT-013 Material Test Reports and QLT-020 Inspection Release Certificate per ITP.
4. Vendor maintains QLT-021 Manufacturing Record Book.
Verification: Witness/hold points per QLT-003.

### S7 — Factory Acceptance Test (FAT)
1. Vendor issues MEC-021 Equipment FAT / Performance Test Procedure for EPC review/approval.
2. Vendor executes FAT with EPC witness (where designated in MEC-021/QLT-003).
3. Vendor issues MEC-022 Equipment FAT / Performance Test Report.
Verification: Acceptance against R-080-04-001 through R-080-04-006 and R-080-04-010.

### S8 — Logistics, Shipping, Spares
1. Vendor issues PRQ-013 Logistics / Shipping Plan consistent with three-piece transport (R-080-04-007).
2. Vendor issues PRQ-015 SPIR (Spare Parts Interchangeability Record) and MEC-024 Spares / Special Tools Requirements.
3. Vendor ships in accordance with PRQ-013; updates ELE-030 with energization-readiness records as applicable.

### S9 — Pressure Equipment Registration
1. Vendor issues REG-022 Pressure Equipment Registration Package for the applicable AHJ (BC — ASSUMPTION; AHJ `location TBD`).
2. Vendor obtains registration / acceptance prior to in-service operation.
Verification: AHJ acceptance evidence in REG-022.

### S10 — Documentation Turnover Handoff
1. Vendor issues PRQ-016 Vendor Data Book / Final Supplier Documentation and MEC-023 Vendor Data Book / Mechanical Final Documentation.
2. Vendor issues MEC-025 Mechanical Equipment IOM Manual.
3. Vendor releases the final document set to DEL-080-05 (Vendor Document Turnover Package) for compilation and handover.
Verification: PRQ-009 index reconciled to delivered documents; DEL-080-05 acceptance.

### S11 — EPC Vendor Package Review and Acceptance
1. EPC Integrator executes DEL-080-06 review and acceptance of the engineered package against this Specification.
Verification: DEL-080-06 acceptance record.

## Verification

- Each deliverable in the heading-33 list is produced and reconciled to PRQ-009 Vendor Document Index.
- FAT (MEC-022) demonstrates per-package capacity 40 MMSCFD across the operating envelope.
- Material certificates (QLT-013) demonstrate NACE compliance for all wetted/pressure-bearing components.
- Pressure equipment registration (REG-022) is accepted by the AHJ before in-service operation.
- All open conflicts in `Guidance.md` Conflict Table have a recorded disposition before FAT.

## Records

Required records produced by this procedure (vendor engineering deliverable set, per heading 33):

**Core vendor documents:** PRQ-009, DOC-008, QLT-006, QLT-003, QLT-013, QLT-020, QLT-021, PRQ-013, PRQ-015, PRQ-016.
**Core package engineering:** MEC-001, MEC-002, MEC-003, MEC-006, MEC-014, MEC-016, MEC-017, MEC-018, MEC-021, MEC-022, MEC-023, MEC-024, MEC-025.
**Rotating equipment / compressors:** MEC-004, MEC-008, MEC-019, ELE-011, REG-022.
**Relief / flare / vent design:** PRO-014, PRO-015, PRO-016, PRO-017, PRO-018.
**Process piping interfaces:** PRO-008, PIP-003, PIP-004, PIP-006, PIP-007, PIP-008, PIP-009, PIP-017, PIP-018, PIP-024, PIP-025, PIP-028.
**Utility piping interfaces:** PRO-011.
**Drainage / containment interfaces:** PRO-023, CIV-014.
**Electrical, lighting, EHT, grounding:** ELE-002, ELE-003, ELE-014, ELE-015, ELE-016, ELE-020, ELE-027, ELE-028, ELE-029, ELE-030, ELE-017, ELE-018, PIP-020, PIP-021, ELE-012, ELE-019.
**Instrumentation and controls interfaces:** INS-002, INS-003, INS-005, INS-006, INS-008, INS-009, INS-010, INS-011, INS-016, INS-017, INS-018, INS-025, INS-029, CTL-003, CTL-005, CTL-006, CTL-026.
**Building / HVAC / code interfaces:** PRO-024, TSF-023, REG-021, STR-002, STR-012.
**Fire and gas / technical safety interfaces:** TSF-002, TSF-003, TSF-004, TSF-009, TSF-011, TSF-013, TSF-028.
**Structural, foundations, supports, access:** STR-001, STR-004, STR-005, STR-006, STR-011, STR-013, STR-014, STR-020.

Source: `_Sources/26020-Package_Requirements.docx` package heading 33 "Vendor Engineering Deliverables".
