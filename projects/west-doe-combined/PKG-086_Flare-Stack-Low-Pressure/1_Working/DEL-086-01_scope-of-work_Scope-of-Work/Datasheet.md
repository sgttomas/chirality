# Datasheet: DEL-086-01_scope-of-work — Scope of Work

> Descriptive datasheet for the EPC Integrator Scope of Work covering Package PKG-086 (Flare Stack — Low Pressure). Values are grounded in the Gate 7 PROJECT_DECOMP snapshot registers; source slices not yet brought into the deliverable folder are marked `location TBD` or `TBD`.

## Identification

| Attribute | Value | Source |
|---|---|---|
| DeliverableID | `DEL-086-01_scope-of-work` | `DELIVERABLE_REGISTER.csv` row DEL-086-01_scope-of-work |
| Deliverable Name | Scope of Work | `DELIVERABLE_REGISTER.csv` |
| Deliverable Type | EPC Scope of Work | `DELIVERABLE_REGISTER.csv` |
| Parent Package | `PKG-086` — Flare Stack (Low Pressure) | `PACKAGE_REGISTER.csv` row PKG-086 |
| Parent Workbook Row | 59 | `PACKAGE_REGISTER.csv` |
| Discipline | Mechanical | `PACKAGE_REGISTER.csv` |
| WBS | 02 | `PACKAGE_REGISTER.csv` |
| Tracking Number | 26020-02-25-002 | `PACKAGE_REGISTER.csv` |
| Responsible Party | EPC Integrator | `DELIVERABLE_REGISTER.csv` |
| Source Basis | Workbook Packages row 59; 26020-Package_Requirements.docx package heading 39 | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Gate Classification | Mandatory Gate 5 EPC anchor deliverable | `DELIVERABLE_REGISTER.csv` Notes |

## Attributes (Package Identity Carried Into the SoW)

| Attribute | Value | Source |
|---|---|---|
| Package Function | Reference/interface package for the LP flare stack and associated LP flare stack blower | `PACKAGE_REGISTER.csv` PKG-086 description |
| Responsibility Model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. EPC Integrator owns integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` PKG-086 responsibility column |
| Major Included Equipment | LP flare stack; air-assist blower; pilot; pilot proving; auto-ignition; supplemental fuel gas/dilution gas provisions; stack interface details | `SCOPE_LEDGER.csv` SOW-0093 (source: 26020-Package_Requirements.docx package heading 39, "Major included equipment") |
| Procurement Authority Note | Both line items identified as 4-25 shared assets excluded from 3-25 DBM scope; procurement authority rests with the 4-25 scope unless the boundary ruling changes | `SCOPE_LEDGER.csv` SOW-0094 |
| Tagged Equipment List (per-tag detail) | TBD — `location TBD` in 26020-Package_Requirements.docx package heading 39 | source slice not yet copied locally |

## Conditions (Operational and Service Conditions)

| Condition | Value | Source |
|---|---|---|
| Service | Low-pressure flare relief and disposal | `PACKAGE_REGISTER.csv` (package name and function); 26020-Package_Requirements.docx package heading 39 |
| Sour-Service Applicability | ASSUMPTION: likely applies — OBJ-009 carries sour-service safety, relief, flare, blowdown, drain/containment requirements across packages | `OBJECTIVE_REGISTER.csv` OBJ-009; source clause `location TBD` |
| Design Flowrates / Composition | TBD — `location TBD` (process basis source slices not yet copied locally) | n/a |
| Design Temperature / Pressure | TBD — `location TBD` | n/a |
| Environmental / Emissions Limits | TBD — `location TBD`; OBJ-009 indicates regulatory/emissions constraints must be carried into package scope | `OBJECTIVE_REGISTER.csv` OBJ-009 |

## Construction (Facility Integration and Interfaces)

| Interface Type | Applicability | Source |
|---|---|---|
| Utility Piping | YES | `INTERFACE_REGISTER.csv` IFC-1C34D7D89E |
| Relief / Flare / Vent | YES | `INTERFACE_REGISTER.csv` IFC-EB7F1FB622 |
| Drain / Containment | YES | `INTERFACE_REGISTER.csv` IFC-E6A8FB7494 |
| Electrical Power | YES | `INTERFACE_REGISTER.csv` IFC-BBFB496745 |
| Grounding / Bonding | YES | `INTERFACE_REGISTER.csv` IFC-8EDD15EE39 |
| I&C / Control Cabling | YES | `INTERFACE_REGISTER.csv` IFC-6480D60C39 |
| Fire & Gas / Safety Systems | YES | `INTERFACE_REGISTER.csv` IFC-858FFC2D67 |
| Structural / Foundations / Supports | YES | `INTERFACE_REGISTER.csv` IFC-6C801F708F |

## Coverage

| Linkage | IDs |
|---|---|
| Covered Scope Ledger Items | `SOW-0091`, `SOW-0092`, `SOW-0093`, `SOW-0094` |
| Supported Objectives | `OBJ-002`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` |
| Sibling Deliverables (same PKG-086) | DEL-086-02 Package Datasheet; DEL-086-03 Construction Work Package; DEL-086-04 Vendor Engineered Equipment Package; DEL-086-05 Vendor Document Turnover Package; DEL-086-06 EPC Vendor Package Review and Acceptance |

## References

- Gate 7 PROJECT_DECOMP snapshot: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
  - `DELIVERABLE_REGISTER.csv` (row `DEL-086-01_scope-of-work`)
  - `PACKAGE_REGISTER.csv` (row `PKG-086`)
  - `SCOPE_LEDGER.csv` (rows `SOW-0091`–`SOW-0094`)
  - `INTERFACE_REGISTER.csv` (rows scoped to `PKG-086`)
  - `OBJECTIVE_REGISTER.csv` (rows `OBJ-002`, `OBJ-004`–`OBJ-010`)
- Upstream source materials referenced by decomposition (not yet brought into deliverable folder; `location TBD`):
  - Workbook Packages row 59 (`_Sources/26020-Packages_Interfaces_4_export.xlsx`)
  - 26020-Package_Requirements.docx package heading 39 (`_Sources/26020-Package_Requirements.docx`)
  - `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (4-25 design basis)
  - `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (3-25 design basis)
