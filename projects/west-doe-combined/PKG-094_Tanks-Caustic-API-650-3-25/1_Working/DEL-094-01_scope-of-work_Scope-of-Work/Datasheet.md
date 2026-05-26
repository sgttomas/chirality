# Datasheet — DEL-094-01 Scope of Work, PKG-094 Tanks, Caustic (API 650) 3-25

> Descriptive datasheet for the EPC Integrator Scope of Work production unit. Values are source-grounded; missing values are marked `TBD`; inferences are labeled `ASSUMPTION`.

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-094-01_scope-of-work` | `_CONTEXT.md` |
| Deliverable Name | Scope of Work | `_CONTEXT.md` |
| Parent Package ID | `PKG-094` | `_CONTEXT.md` |
| Parent Workbook ID | 94 | `_CONTEXT.md` |
| Package Name | Tanks, Caustic (API 650) 3-25 | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Discipline | Mechanical | `_CONTEXT.md` |
| Deliverable Type | EPC Scope of Work | `_CONTEXT.md` |
| Responsible Party | EPC Integrator | `_CONTEXT.md` |
| Source Reference | Workbook Packages row 86; 26020-Package_Requirements.docx package heading 46 | `_CONTEXT.md` |
| Decomposition Snapshot | GATE-07_Final_Published_2026-05-24 (PROJECT_DECOMP) | `_REFERENCES.md` |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Covers Scope Items | SOW-0193; SOW-0194; SOW-0195; SOW-0196 | `_CONTEXT.md`; `SCOPE_LEDGER.csv` |
| Supports Objectives | OBJ-002; OBJ-003; OBJ-004; OBJ-005; OBJ-006; OBJ-007; OBJ-008; OBJ-009; OBJ-010 (ASSUMPTION: PACKAGE_HEURISTIC association) | `_CONTEXT.md`; `OBJECTIVE_PACKAGE_MAP.csv` |
| Package WBS | 03 | `OBJECTIVE_PACKAGE_MAP.csv` |
| Facility Site | LSD 03-25-80-15 W6M, north of Dawson Creek, BC | `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (Site basis) |
| Anticipated Artifacts | Package scope of work; tagged equipment and package identity list; package function and integration narrative; responsibility assignment record | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |

## Tagged Equipment (from source)

| Tag | Description | Quantity | Nominal Capacity | Design Pressure | Notes | Source |
|---|---|---|---|---|---|---|
| TK-6930-2 | Spent Caustic Storage Tank — receives spent caustic from Mercaptan Treating Unit (level-controlled) | 1 | 400 bbl | 32 oz / 1.0 oz Vacuum (atmospheric) | Modified API 650; c/w heater at 32.2 °C (90 °F) minimum, vendor-designed heater | `SCOPE_LEDGER.csv` SOW-0195 |
| Fresh Caustic Tank (tag TBD) | Stores and supplies fresh caustic solution to the caustic treatment unit | 1 | 400 bbl (ASSUMPTION: same basis as Item 2 in SOW-0196) | Atmospheric (32 oz / 1.0 oz vacuum — ASSUMPTION by parallel to TK-6930-2) | Per DBM: atmospheric 32 oz with LP fuel-gas blanket, heating, insulation | `SCOPE_LEDGER.csv` SOW-0194/0196; DBM section "Caustic Mercaptan Treating Package" |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Service — Fresh Caustic | Storage and supply of fresh caustic to caustic treatment unit | `SCOPE_LEDGER.csv` SOW-0194 |
| Service — Spent Caustic | Receipt and safe storage of spent caustic from pressurized caustic drain drum | `SCOPE_LEDGER.csv` SOW-0194 |
| Caustic Solution Basis | 50 wt% NaOH/H2O, SG 1.75 TBC | DBM 3-25 section "Caustic Mercaptan Treating" |
| Design Pressure | Atmospheric, 32 oz / 1.0 oz vacuum | `SCOPE_LEDGER.csv` SOW-0195/0196 |
| Design Temperature (low) | Minimum ambient temperature (site basis -40 °C per DBM) | `SCOPE_LEDGER.csv` SOW-0196; DBM site basis |
| Heating | Heater minimum 32.2 °C (90 °F); vendor to design heater | `SCOPE_LEDGER.csv` SOW-0195 |
| Insulation/Blanket | LP fuel-gas blanket, heating, insulation (per DBM) | DBM 3-25 |
| Capacity / Throughput | TBC (source: "Capacity/design throughput: TBC") | `SCOPE_LEDGER.csv` SOW-0196 |
| Flow Rate (Item 1 / Item 2) | TBD | `SCOPE_LEDGER.csv` SOW-0196 |
| Spent Caustic Tank Vent | Vents through flame arrestor to incinerator header; supports truck-out | DBM 3-25 |
| Fresh Caustic VRU Connection | Not connected to VRU | DBM 3-25 |

## Construction

| Item | Value | Source |
|---|---|---|
| Tank Standard | Modified API 650 (atmospheric) | `SCOPE_LEDGER.csv` SOW-0195 |
| Material / Coating | TBC — "caustic tank material/coating details remain TBC" | DBM 3-25 |
| Material Restriction | Aluminum shall not be used in the caustic building | DBM 3-25 |
| Foundations / Mounting | By others (excluded from package scope) | `SCOPE_LEDGER.csv` SOW-0196 |
| Electrical / Instrumentation | By others | `SCOPE_LEDGER.csv` SOW-0196 |
| Platforms / Staircase | By others | `SCOPE_LEDGER.csv` SOW-0196 |

## Cross-Facility Interfaces (PKG-094 → other systems)

Interfaces from `INTERFACE_REGISTER.csv` for PKG-094:

| Interface ID | Discipline / Topic |
|---|---|
| IFC-12C92E9A0A | Process Piping |
| IFC-AFD520D296 | Relief / Flare / Vent |
| IFC-DA053E0FE2 | Drain / Containment |
| IFC-35E994F2DE | Grounding / Bonding |
| IFC-946F48A91C | Area / Exterior Lighting |
| IFC-7EBC5D8325 | Cathodic Protection |
| IFC-15D9C87C0A | I&C / Control Cabling |
| IFC-61D7941475 | Grading / Site Drainage / Spill Containment |
| IFC-94BBAEE00A | Structural / Foundations / Supports |

(All present-confirmed for PKG-094 per the GATE-07 INTERFACE_REGISTER.)

## References

- `_CONTEXT.md` (deliverable-local)
- `_REFERENCES.md` (deliverable-local)
- GATE-07 PROJECT_DECOMP snapshot:
  - `DELIVERABLE_REGISTER.csv`
  - `SCOPE_LEDGER.csv` (SOW-0193, SOW-0194, SOW-0195, SOW-0196)
  - `INTERFACE_REGISTER.csv`
  - `OBJECTIVE_PACKAGE_MAP.csv`
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`
- `_Sources/26020-Package_Requirements.docx` (package heading 46) — referenced; local text extraction not performed in this run.
