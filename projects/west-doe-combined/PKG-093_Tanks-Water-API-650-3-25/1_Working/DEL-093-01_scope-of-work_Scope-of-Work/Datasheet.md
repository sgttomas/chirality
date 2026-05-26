# Datasheet — DEL-093-01 Scope of Work (PKG-093 Tanks, Water (API 650) 3-25)

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | DEL-093-01_scope-of-work | `_CONTEXT.md` |
| Deliverable Name | Scope of Work | `_CONTEXT.md` |
| Parent Package | PKG-093 — Tanks, Water (API 650) 3-25 | PACKAGE_REGISTER.csv row PKG-093 |
| Workbook Row | 95 | PACKAGE_REGISTER.csv; `_CONTEXT.md` |
| WBS | 03 | PACKAGE_REGISTER.csv |
| Discipline | Mechanical | PACKAGE_REGISTER.csv; `_CONTEXT.md` |
| Type | EPC Scope of Work | `_CONTEXT.md` |
| Responsible Party | EPC Integrator | `_CONTEXT.md`; PACKAGE_REGISTER.csv |
| Vendor Tag / RFQ | 26020-03-PT-19-001 — Tanks, Water | PACKAGE_REGISTER.csv |
| Covers Scope Items | SOW-0229; SOW-0230; SOW-0231; SOW-0232 | `_CONTEXT.md`; SCOPE_LEDGER.csv |
| Supports Objectives | OBJ-002; OBJ-003; OBJ-004; OBJ-005; OBJ-006; OBJ-007; OBJ-008; OBJ-009; OBJ-010 | `_CONTEXT.md` (ASSUMPTION: PACKAGE_HEURISTIC) |

## Attributes — Package Identity and Function

| Attribute | Value | Source |
|---|---|---|
| Package Function | Sweet Produced Water and Process Water storage | SOW-0230 (26020-Package_Requirements.docx heading 45, Basic scope) |
| Process Service | Sweet Produced Water; Process Water | SOW-0230 |
| Source of Service | Sweet produced-water from comp station and cryo (4-25) flows | SOW-0232 (Scope notes and open items) |
| Whole-Facility Role | Provides sweet produced-water and process-water storage at 03-25 Liquids Hub | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md §"Produced-Water Storage, Treatment, and Transfer" |

## Attributes — Tagged Equipment List

| Item No. | Tag | Description | Qty | Capacity | Source |
|---|---|---|---|---|---|
| 1 | TK-9060-2 | Sweet Produced Water Storage Tank | 1 | 3,800 bbl | SOW-0230; SOW-0231 |
| 1 | TK-9070-2 | Sweet Produced Water Storage Tank | 1 | 3,800 bbl | SOW-0230; SOW-0231 |
| 2 | (TBD) | Second item referenced in source; design parameters TBD | TBD | TBD | SOW-0232 (Item No. 2 design flow / temperature TBD) |

ASSUMPTION: Item No. 2 is referenced in SOW-0232 without tag, capacity, or full design conditions. Tag assignment and capacity remain `TBD` pending source clarification (see Guidance Conflict Table CT-02).

## Conditions — Design and Operating Basis

| Parameter | Item No. 1 Value | Item No. 2 Value | Source |
|---|---|---|---|
| Design Flow | 15,300 kg/h; 3,584 Am3/d from comp station; 240 Am3/d from cryo | TBD | SOW-0232 |
| Operating Pressure | Atmospheric | Atmospheric (ASSUMPTION: same service) | SOW-0232 |
| Operating Temperature | 5 °C | TBD | SOW-0232 |
| Design Pressure | 32 oz test pressure | 32 oz test pressure (ASSUMPTION) | SOW-0232 |
| Design Temperature (min) | -40 °C | -40 °C (ASSUMPTION) | SOW-0232 |
| Design Temperature (max) | 60 °C | 60 °C (ASSUMPTION) | SOW-0232 |
| Fluid SG (tank design) | 1.25 TBC | TBD | DBM 3-25_Comp_and_Liquids §Produced-Water Storage |
| Fluid SG (pump basis) | 1.18 | TBD | DBM 3-25_Comp_and_Liquids §Produced-Water Storage — CONFLICT (see Guidance CT-01) |
| Volume (dimensional) | TBD | TBD | SOW-0231 (volume: TBD) |

## Construction — Major Included Equipment Features

| Feature | Specification | Source |
|---|---|---|
| Code / Standard | Modified API 650 | SOW-0231; DBM §Produced-Water Storage |
| External Insulation | Required | SOW-0231; DBM |
| Heating | Heater required to prevent freezing | SOW-0231; DBM |
| Blanket Gas | LP fuel-gas blanket for vacuum prevention in winter, per API-2000 | SOW-0231 |
| Internal Coating | Devchem 253 on floors, walls, roofs | SOW-0231; DBM |
| Skim System | Kennilworth-type HCL float skim system, one per tank | SOW-0231 |
| Skim Float Design SG | <= 0.67 | SOW-0231 |
| Fluid Classification | Non-sour produced water | SOW-0231 |

## Construction — Excluded by Package Vendor (By Others)

Per SOW-0232 "By others": Foundations; tank mounting at site; electrical / instrumentation; platforms; staircase; etc. EPC Integrator and other discipline packages own these.

## Interface Types Applicable

Process Piping; Relief / Flare / Vent; Drain / Containment; Grounding / Bonding; Area / Exterior Lighting; Cathodic Protection; I&C / Control Cabling; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports. (Source: PACKAGE_REGISTER.csv row PKG-093.)

## Responsibility Split

| Party | Responsibility | Source |
|---|---|---|
| Package Vendor | Package engineering, package design, vendor documentation, physical equipment package | PACKAGE_REGISTER.csv; SOW-0229 |
| EPC Integrator | Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, facility-level integration | PACKAGE_REGISTER.csv; SOW-0229 |

## References

- `_REFERENCES.md`
- DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md (§ Produced-Water Storage, Treatment, and Transfer)
- PROJECT_DECOMP GATE-07 snapshot: SCOPE_LEDGER.csv (SOW-0229..SOW-0232); DELIVERABLE_REGISTER.csv (DEL-093-01); PACKAGE_REGISTER.csv (PKG-093)
- 26020-Package_Requirements.docx package heading 45 (location TBD — accessed via SCOPE_LEDGER extracted text)
- Bid Docs/Budgetary/26020-03-PT-RFQ-19-001 — Water Tanks.docx (location TBD)
