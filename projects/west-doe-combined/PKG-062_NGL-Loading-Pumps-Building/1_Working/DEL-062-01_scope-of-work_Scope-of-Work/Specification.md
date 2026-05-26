# Specification — DEL-062-01 Scope of Work (PKG-062 NGL Loading Pumps Building)

## Scope

### In Scope
- A single EPC Integrator Scope of Work that anchors PKG-062 (NGL Loading Pumps Building) as a flat, vendor-responsible Mechanical package within WBS 01 (source: SCOPE_LEDGER SOW-0153).
- Identification of the package function: move LPG product from storage to LPG Truck Loading via four identical, parallel rotary vane pumps (source: SCOPE_LEDGER SOW-0154; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2610).
- Definition of tagged equipment: P-9510-1, P-9520-1, P-9530-1, P-9540-1 — Blackmer Model LGL4B rotary vane pumps (source: SCOPE_LEDGER SOW-0155; DBM line 2610).
- Statement of responsibility split: Package Vendor owns engineering/design/equipment; EPC Integrator owns facility integration (source: SCOPE_LEDGER SOW-0153).
- Statement of the package boundary including "By Others" exclusions: DCS integration, foundations, and electrical supply to MCC (source: SCOPE_LEDGER SOW-0156).
- Whole-facility integration narrative linking PKG-062 to the 04-25 Deepcut DBM's NGL loading function (source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 73).

### Excluded From This Deliverable
- Detailed datasheet content for the package as a vendor handoff (belongs to DEL-062-02, Package Datasheet).
- Construction installation/tie-in plan (belongs to DEL-062-03).
- Vendor engineered equipment package (DEL-062-04), vendor document turnover (DEL-062-05), and EPC vendor package review/acceptance (DEL-062-06).
- DCS integration, foundations, and electrical supply to MCC (By Others per SOW-0156).

## Requirements

### R-SOW-01 — Package Identity
The Scope of Work shall identify PKG-062 by ParentPackageID, name "NGL Loading Pumps Building", workbook row 76, and source heading "26020-Package_Requirements.docx package heading 16" (source: SCOPE_LEDGER SOW-0153, SOW-0154; `_CONTEXT.md`).

### R-SOW-02 — Tagged Equipment List
The Scope of Work shall list the tagged equipment: P-9510-1, P-9520-1, P-9530-1, P-9540-1 (4 Blackmer Model LGL4B rotary vane pumps configured in parallel) (source: SCOPE_LEDGER SOW-0154, SOW-0155; DBM line 2610).

### R-SOW-03 — Package Function Narrative
The Scope of Work shall state the package function: pumps move LPG product from storage to LPG Truck Loading (source: SCOPE_LEDGER SOW-0154).

### R-SOW-04 — Performance Envelope
The Scope of Work shall record the per-pump capacity envelope: 68 m3/hr @ 345 kPad (300 USGPM @ 50 psid) TBC TDH; operating and design conditions TBC (source: SCOPE_LEDGER SOW-0155, SOW-0156).

### R-SOW-05 — Driver and Local Control
The Scope of Work shall record the driver and local-control basis: 575 V / 3 Ph / 60 Hz electric motors fed from 600 V MCC, sized for inlet stabilizer composition density at -40 C start-up, with local H-O-A or On-Off switch (source: SCOPE_LEDGER SOW-0156).

### R-SOW-06 — Building Provision
The Scope of Work shall record that a self-framing building will be erected at site (source: SCOPE_LEDGER SOW-0155).

### R-SOW-07 — Responsibility Split
The Scope of Work shall state the responsibility split between Package Vendor and EPC Integrator (source: SCOPE_LEDGER SOW-0153).

### R-SOW-08 — By-Others Exclusions
The Scope of Work shall explicitly state the By Others items: DCS integration, foundations, and electrical supply to MCC (source: SCOPE_LEDGER SOW-0156).

### R-SOW-09 — Facility Integration Narrative
The Scope of Work shall position PKG-062 within the overall 04-25 Deepcut facility, describing how the loading pumps interface with NGL storage upstream and truck-loading stations downstream (source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 73, 2610).

### R-SOW-10 — Coverage of SOW Items
The Scope of Work shall trace to and cover SOW-0153, SOW-0154, SOW-0155, and SOW-0156 (source: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row 420).

### R-SOW-11 — Objective Linkage
The Scope of Work shall record the objectives supported by PKG-062 (ASSUMPTION: package-grouping heuristic): OBJ-001, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 (source: `OBJECTIVE_SCOPE_MAP.csv`).

## Standards

| Standard / Source | Applicability | Location |
|---|---|---|
| `26020-Package_Requirements.docx` package heading 16 | Authoritative scope source for PKG-062 | location TBD (full document slice not locally extracted; SCOPE_LEDGER carries the cited fragments) |
| 4-25 Deepcut DBM | Whole-facility design basis defining the NGL loading function | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |
| Blackmer LGL4B vendor literature | Pump model basis | not locally accessible — TBD |
| API/CSA codes governing rotary vane LPG pumps and self-framing buildings | Not stated by source | TBD — to be confirmed in Package Datasheet (DEL-062-02) |

## Verification

| Requirement | Verification Approach |
|---|---|
| R-SOW-01 | Cross-check the SOW identity fields against `_CONTEXT.md` and `DELIVERABLE_REGISTER.csv` row 420. |
| R-SOW-02 | Cross-check tag list against `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2610 and SCOPE_LEDGER SOW-0155. |
| R-SOW-03 | Cross-check narrative against SCOPE_LEDGER SOW-0154 wording. |
| R-SOW-04 | Cross-check numeric values against SCOPE_LEDGER SOW-0155, SOW-0156; mark TBC where source marks TBC. |
| R-SOW-05 | Cross-check driver/control statements against SCOPE_LEDGER SOW-0156. |
| R-SOW-06 | Cross-check against SCOPE_LEDGER SOW-0155 ("Self-framing building..."). |
| R-SOW-07 | Cross-check against SCOPE_LEDGER SOW-0153 statement of vendor/EPC roles. |
| R-SOW-08 | Cross-check against SCOPE_LEDGER SOW-0156 By Others list. |
| R-SOW-09 | Cross-check that the SOW narrative cites the 4-25 Deepcut DBM as the upstream design basis (DBM line 73 narrative). |
| R-SOW-10 | Coverage check against SOW-0153 through SOW-0156 in SCOPE_LEDGER. |
| R-SOW-11 | Coverage check against OBJECTIVE_SCOPE_MAP rows for PKG-062; record ASSUMPTION marker pending human ruling. |

## Documentation

The deliverable artifact set required by `_CONTEXT.md`:
- Package scope of work narrative
- Tagged equipment and package identity list
- Package function and integration narrative
- Responsibility assignment record

These four artifacts may be combined into a single Scope of Work document or kept as labeled sections of one document; the artifact identity is preserved in the section headings.
