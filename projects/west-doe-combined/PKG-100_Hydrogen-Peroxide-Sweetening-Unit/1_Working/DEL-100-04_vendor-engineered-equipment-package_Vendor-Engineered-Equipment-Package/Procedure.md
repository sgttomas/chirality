# Procedure — Vendor Engineered Equipment Package (DEL-100-04)

> Operational procedure for producing and accepting the Hydrogen Peroxide Sweetening Unit
> vendor-engineered equipment package. Steps are derived from the source slice
> (`_Sources/26020-Package_Requirements.docx`, package heading 52) and the vendor
> deliverable categories enumerated there; judgment-only steps are marked `TBD`.

## Purpose

To engineer, design, fabricate/supply, document, and turn over a complete and field-ready
Hydrogen Peroxide Sweetening Unit equipment package, with the document set required for
EPC Integrator review and acceptance.

## Prerequisites

| # | Item | Source / Status |
|---|---|---|
| P1 | EPC Scope of Work (`DEL-100-01`) — defining the package scope boundary. | `_CONTEXT.md` Decomposition; sibling deliverable exists. |
| P2 | Package Datasheet (`DEL-100-02`) — defining package design basis values. | `_CONTEXT.md` Decomposition; sibling deliverable. |
| P3 | Accepted package requirements basis (package heading 52). | `_Sources/26020-Package_Requirements.docx` |
| P4 | RFQ basis document `26020-03-PT-RFQ-27-001-H202_Sweet_Unit.docx`. | Referenced; `location TBD` — see Guidance Conflict Table CT-001. |
| P5 | Package PFD (referenced by source). | `location TBD` — see Conflict Table CT-002. |
| P6 | Confirmed site location / project basis (West Doe Liquids Hub). | Source: "Location / Status" |
| P7 | Declared upstream dependencies. | `_DEPENDENCIES.md` — none declared during PREPARATION. |

If any of P4/P5 cannot be obtained, proceed using package heading 52 as the controlling
source and record the gap.

## Steps

### Phase 1 — Engineering and Design

1. **Confirm package requirements basis.** Read package heading 52 in
   `_Sources/26020-Package_Requirements.docx`. Reconcile against EPC SOW and Package
   Datasheet (siblings). Capture any deviations as PROPOSAL with provenance.
2. **Issue vendor Mechanical Design Basis** (`MEC-001`) closing the TBC items:
   - Design pressure and design temperature for the reactor and pressure-bearing
     equipment.
   - Pump capacity (number of pumps, design flow, NPSH).
   - Governing codes (pressure vessel, tank, electrical, fire/building) and
     jurisdictional registration authority. (See Guidance CT-003, CT-004.)
3. **Develop process package design**:
   - PFD (`PRO-004`), P&IDs (`PRO-008`), Heat & Material Balance (`PRO-005`), Process
     Description / Operating Philosophy (`PRO-007`), Major Equipment Process Data Sheets
     (`PRO-010`), Utility Summary (`PRO-011`), Line Sizing (`PRO-012`), Process Control
     Philosophy (`PRO-020`), Startup/Shutdown Narrative (`PRO-025`).
4. **Develop mechanical and equipment design**:
   - Mechanical Equipment List (`MEC-002`), Equipment Data Sheets (`MEC-003`), Package
     Equipment Specifications (`MEC-006`), Calculation Package (`MEC-014`), GA Drawing
     (`MEC-016`), Installation/Setting Drawings (`MEC-017`), Lifting Study (`MEC-018`).
   - For pumps: `MEC-004`, `MEC-007`, `MEC-019`, `PRO-013` (NPSH), `ELE-011` (motor
     starting study).
   - For static pressure equipment (reactors): `MEC-005`, `MEC-009`, `REG-022`
     (Pressure Equipment Registration).
   - For the 400 BBL H₂O₂ storage tank: `MEC-011`.
5. **Develop relief and flare design**: `PRO-014`, `PRO-015`, `PRO-016`, `PRO-017`,
   `PRO-018` per the relief/flare/vent interface applicability ("Yes" in source).
6. **Develop piping interfaces**: `PIP-003`, `PIP-004` (tie-in list and tie-in scope —
   the controlling interface document for "by others" piping), `PIP-006`, `PIP-007`,
   `PIP-008`, `PIP-009`, `PIP-017`, `PIP-018`, `PIP-024`, `PIP-025`.
7. **Develop electrical design** for the 575 V / 600 V MCC interface: `ELE-002`,
   `ELE-003`, `ELE-014`, `ELE-015`, `ELE-016`, `ELE-020`, `ELE-017` (lighting),
   `ELE-018` (EHT), `PIP-020`/`PIP-021` (heat-tracing schedule and interface), `ELE-012`
   (grounding), `ELE-019` (earthing/bonding).
8. **Develop instrumentation & controls** for the I&C interface ("Yes") and DCS
   integration ("by others"): `INS-002`, `INS-003`, `INS-005`, `INS-006`, `INS-008`,
   `INS-009`, `INS-010`, `INS-011`, `INS-016`, `INS-017`, `INS-018`, `INS-025`,
   `CTL-003`, `CTL-005`, `CTL-006`, `CTL-026` (Package Vendor Interface Specification).
9. **Develop building / HVAC / code package**: `PRO-024`, `TSF-023`, `REG-021`
   (Fire/Building Code), `STR-002`, `STR-012`.
10. **Develop fire & gas / safety**: `TSF-002`, `TSF-003`, `TSF-004`, `TSF-009` (SIL),
    `TSF-011` (SRS), `TSF-013`, `TSF-028`.
11. **Develop structural / foundations / supports / access**: `STR-001`, `STR-004`,
    `STR-005`, `STR-006`, `STR-011`, `STR-013`, `STR-014`, `STR-020`. Coordinate with
    "by others" site foundations.
12. **Conduct HAZOP / PHA technical input package** (`PRO-026`) and produce Process
    Safety Information package (`PRO-027`).

### Phase 2 — Quality and Procurement

13. **Issue Supplier Quality Plan** (`QLT-006`) and **Inspection and Test Plan**
    (`QLT-003`) covering the major equipment items.
14. **Issue Vendor Document Index** (`PRQ-009`) and **Vendor Document Control Procedure**
    (`DOC-008`).
15. **Plan logistics and spares**: `PRQ-013` (Logistics / Shipping Plan), `PRQ-015`
    (Spare Parts Interchangeability Record).

### Phase 3 — Fabrication, Inspection, and Test

16. **Execute fabrication and inspection** per ITP; collect Material Test Reports /
    Certificates (`QLT-013`) and Inspection Release Certificate (`QLT-020`).
17. **Compile Manufacturing Record Book / Vendor Data Book** (`QLT-021`).
18. **Execute Equipment FAT / Performance Test** per `MEC-021`; produce report `MEC-022`.
19. **Execute Electrical FAT/SAT** per `ELE-029`; produce records `ELE-030`.

### Phase 4 — Turnover

20. **Compile final Vendor Data Book** (`PRQ-016`) and Mechanical final documentation
    (`MEC-023`).
21. **Compile IOM Manual** (`MEC-025`) and Spares / Special Tools requirements
    (`MEC-024`).
22. **Submit Pressure Equipment Registration Package** (`REG-022`) to the jurisdictional
    authority (authority `TBD` — see Guidance CT-004).
23. **Hand off the engineered physical equipment package** plus the vendor package design
    basis and datasheet set (the two anticipated artifacts from `_CONTEXT.md`).
24. **Provide As-Built updates** post-installation: `PRO-028`, `PIP-028`, `INS-029`.

## Verification

| Step | Verification |
|---|---|
| 2 (Design Basis) | EPC Integrator review of `MEC-001` confirms closure of TBC items (R-DESN-001, R-DESN-002). |
| 3-11 (Discipline design) | EPC Integrator review of each vendor deliverable per the vendor document index. |
| 12 (HAZOP) | HAZOP closeout report; actions tracked to closure. |
| 13 (ITP) | ITP signoff by EPC Quality. |
| 16-19 (Fab/Test) | Successful FAT and Electrical FAT/SAT; signed test reports. |
| 22 (Registration) | Stamped registration receipt from jurisdictional authority. |
| 23 (Turnover) | Acceptance per `DEL-100-06` (EPC Vendor Package Review and Acceptance). |

Acceptance authority for the package is the EPC Integrator via `DEL-100-06`. Per
governance K-AUTH-1, only humans author binding approvals.

## Records

The procedure produces the following records (consolidated into the Vendor Data Book and
turned over via `DEL-100-05` Vendor Document Turnover Package):

- Mechanical Design Basis (`MEC-001`) — closure of TBC items.
- Complete vendor document set per `Datasheet.md` §"Vendor Engineering Deliverables".
- Manufacturing Record Book (`QLT-021`).
- FAT / Performance Test Report (`MEC-022`); Electrical Test Records (`ELE-030`).
- Pressure Equipment Registration Package (`REG-022`).
- Final Vendor Data Book (`PRQ-016`) / Mechanical Final Documentation (`MEC-023`).
- IOM Manual (`MEC-025`).
- As-Built drawing/document updates (`PRO-028`, `PIP-028`, `INS-029`).
- EPC Integrator acceptance record (recorded under `DEL-100-06`).

Open items recorded for downstream action: Conflict Table entries CT-001..CT-005 in
`Guidance.md`.
