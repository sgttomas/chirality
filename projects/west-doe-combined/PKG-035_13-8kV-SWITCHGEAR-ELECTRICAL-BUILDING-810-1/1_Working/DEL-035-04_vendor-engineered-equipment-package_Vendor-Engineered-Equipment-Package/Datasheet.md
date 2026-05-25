# Datasheet: DEL-035-04 — Vendor Engineered Equipment Package

> Pass 1/Pass 2 draft. Source-grounded values are cited inline. Unsupported items are marked `TBD` and routed to `Guidance.md` Conflict Table when human ruling is required.

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-035-04_vendor-engineered-equipment-package` |
| Name | Vendor Engineered Equipment Package |
| ParentPackageID | `PKG-035` |
| Workbook Row | 37 |
| Package Tag | `26020-01-30-026` |
| Package Name | 13.8kV SWITCHGEAR ELECTRICAL BUILDING (810-1) |
| Discipline | Electrical |
| WBS | 01 |
| ResponsibleParty | Package Vendor (engineering / design / equipment) with EPC Integrator integration review |
| Type | Vendor Package Production Unit |
| Scope Items Covered | `SOW-0036` |
| Supports Objectives | `OBJ-001`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` (PACKAGE_HEURISTIC, ASSUMPTION) |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Plant power role | Plant main power distribution center for the West Doe Deepcut expansion | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (Facility electrical system) |
| Nominal MV bus voltage | 13.8 kV, 3-phase, 3-wire, 60 Hz, low-resistance grounded | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (Medium-voltage services) |
| Upstream supply | Fed from utility 25 kV → 25 kV/13.8 kV 50 MVA utility-supplied transformer | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (Facility electrical system); incoming 25 kV is TBC in source |
| Bus sizing basis | Sized for the full facility scope | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |
| Downstream distribution | Radial feeds via step-down transformers to 6.9 kV, 4.16 kV, 600 V electrical buildings (820-1, 830-1, 840-1, 850-1, 860-1) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (Electrical Buildings, radial distribution list) |
| Build mode | Shop-built (modular prefabricated electrical building) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (Electrical Buildings; "810-1 13.8kV Switchgear Electrical Building — Shop") |
| Equipment housed (per electrical building basis) | 13.8 kV main switchgear; medium-voltage MCC, RVSS, VFDs; 600 V MCCs; 120 V AC UPS w/ batteries; 125 V DC UPS w/ batteries; distribution transformers; panelboards; contactor panels; PLC panels; network racks (as required by detailed design) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (Electrical Buildings) |
| Indicative MV switchgear count (facility list) | "Medium Voltage Switchgear" qty 1 on ELC-QAS-000007-001; "Low Voltage Switchgear" qty 2 on ELC-QAS-000006-001 — facility-level entries; allocation to PKG-035 not asserted | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (electrical QAS list) |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Area classification | Electrical buildings located in general purpose areas | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |
| Climate / HVAC | Climate controlled, HVAC sized n+1 | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (Electrical Buildings) |
| Cable entry | Bottom entry of incoming and outgoing power cables; building elevated on piles to provide cable tray space beneath | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |
| Building wiring | TECK and ACIC cables; EMT conduit between adjacent panels; outdoor GFI receptacle for exterior maintenance | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |
| Door sizing | Equipment doors sized for, or with removable transoms allowing, removal of the largest equipment | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |
| Grounding | Major electrical equipment directly connected to ground grid at two points; ground wells with bolted test connections | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |
| Separation | Distance between fired heater and electrical building 25 m (82 ft), per OGAOM Sec. 9.6.15 | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |
| Detailed ratings (short-circuit, BIL, continuous current, IP/NEMA) | `TBD` — not stated in accessible source slices | location TBD |

## Construction

| Element | Value | Source |
|---|---|---|
| Build site | Shop-built per electrical building shop/field table entry for 810-1 | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |
| Building type | Prefabricated, modular electrical building | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |
| Foundation | Elevated, pile-supported per electrical building basis | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |
| Vendor responsibility | Package engineering, package design, vendor documentation, and physical equipment package | `PACKAGE_REGISTER.csv` PKG-035 row 37 |
| EPC Integrator responsibility | Facility integration: interfaces, tie-ins, constructability, procurement/construction coordination, facility-level integration | `PACKAGE_REGISTER.csv` PKG-035 row 37 |
| Applicable interface types | Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports | `PACKAGE_REGISTER.csv` PKG-035 |
| Tagged components / model selections | `TBD` — vendor selection; not present in accessible source slices |  |

## References

- `_REFERENCES.md` (this deliverable)
- `_CONTEXT.md` (this deliverable)
- Gate 7 PROJECT_DECOMP snapshot: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
- `PACKAGE_REGISTER.csv` row `PKG-035`
- `DELIVERABLE_REGISTER.csv` row `DEL-035-04`
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (Electrical Buildings; Facility electrical system; Medium-voltage services; QAS lists; shop/field table)
- `_Sources/26020-Package_Requirements.docx` (not parsed in this pass; binary docx — content not opened during P1/P2)
