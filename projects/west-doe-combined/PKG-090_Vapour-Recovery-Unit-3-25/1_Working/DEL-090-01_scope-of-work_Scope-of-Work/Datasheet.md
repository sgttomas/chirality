# Datasheet — DEL-090-01 Scope of Work (PKG-090 Vapour Recovery Unit 3-25)

> Descriptive document. Source-grounded values only; missing values are `TBD`. Inferred values are labelled `ASSUMPTION`.

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-090-01_scope-of-work` | `_CONTEXT.md` |
| Deliverable Name | Scope of Work | `_CONTEXT.md` |
| ParentPackageID | `PKG-090` | `_CONTEXT.md` |
| Package Name | Vapour Recovery Unit 3-25 | `_CONTEXT.md` |
| Workbook Row | 100 | PACKAGE_REGISTER.csv row 100 |
| WBS | 03 | PACKAGE_REGISTER.csv row 100 |
| Tag (package) | `26020-03-12-001` | PACKAGE_REGISTER.csv row 100 |
| Document Number (package) | `26020-03-PT-12-001 - Vapour Recovery Unit` | PACKAGE_REGISTER.csv row 100 |
| Discipline | Mechanical | `_CONTEXT.md`; PACKAGE_REGISTER.csv row 100 |
| Deliverable Type | EPC Scope of Work | `_CONTEXT.md` |
| Responsible Party | EPC Integrator | `_CONTEXT.md` |
| Covers Scope Items | `SOW-0249`, `SOW-0250`, `SOW-0251`, `SOW-0252` | `_CONTEXT.md`; DELIVERABLE_REGISTER.csv row 564 |
| Supports Objectives | `OBJ-002`, `OBJ-003`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` | `_CONTEXT.md`; DELIVERABLE_REGISTER.csv row 564 (ASSUMPTION via PACKAGE_HEURISTIC) |

## Attributes

### Package Function

| Attribute | Value | Source |
|---|---|---|
| Process function | Vapour recovery: collect vapours from condensate and produced-water tank systems and selected process vents; compress for routing to 04-25 SOC suction per SCA-002. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-06 §Vapour Recovery |
| Configuration | Two (2) 100% capacity VRU compressor packages in lead-lag, both housed in one building. | `_Sources/.../3-25_Comp_and_Liquids_DBM.md` SEC-06 §Vapour Recovery; PACKAGE_REGISTER.csv row 100 |
| Compressor type | Two-stage Ro-Flo 12S/212M positive-displacement rotary vane compressor (one per train). | PACKAGE_REGISTER.csv row 100 |
| Driver | 200 HP VFD electric motor (one per train). | PACKAGE_REGISTER.csv row 100; DBM SEC-06 §Vapour Recovery |
| Service | Sour service. | PACKAGE_REGISTER.csv row 100 |
| Train redundancy | 2 x 100% lead-lag | PACKAGE_REGISTER.csv row 100; DBM SEC-06 §Vapour Recovery |
| Discharge routing | To 04-25 SOC suction (no local 03-25 SOC retained, per SCA-002). | DBM SEC-06 §Vapour Recovery; SEC-01 supersession table |

### Tagged Equipment (package identity list)

| Item | Tag / Qty | Source |
|---|---|---|
| VRU compressor package – Train A | Qty 1; tag `TBD` | DBM SEC-06 §Vapour Recovery (qty); package tag location `TBD` (`26020-Package_Requirements.docx` heading 43 location TBD) |
| VRU compressor package – Train B | Qty 1; tag `TBD` | DBM SEC-06 §Vapour Recovery (qty); package tag location `TBD` |
| VRU building (single building housing both trains) | Qty 1; tag `TBD` | PACKAGE_REGISTER.csv row 100 |
| VRU recycle valve (per train) | Qty 2 (one per train) | DBM SEC-06 §Vapour Recovery |
| VRU suction header LP-flare bypass V-ball valve | Qty `TBD` | DBM SEC-06 §Vapour Recovery |
| Make-up / blanket-gas regulator (from LP fuel gas) | Qty `TBD` | DBM SEC-06 §Vapour Recovery |

Detailed sub-component tag list `TBD` — derive from vendor engineered package documentation (DEL-090-04) when issued.

## Conditions

| Condition | Value | Source |
|---|---|---|
| Site | LSD 03-25-80-15 W6M, north of Dawson Creek, BC | DBM SEC-02 §Site |
| Site elevation | 673 m AMSL | DBM SEC-02 |
| Service | Sour gas (vapours from sour condensate and produced-water tanks, plus selected process vents) | DBM SEC-06 §Vapour Recovery; PACKAGE_REGISTER.csv row 100 |
| Discharge destination | 04-25 SOC suction (per SCA-002) | DBM SEC-06; SEC-01 |
| Suction-pressure control | VRU recycle valve sized for 100% flow at minimum driver speed and lowest discharge pressure; make-up/blanket-gas regulator from LP fuel gas maintains minimum suction pressure at maximum turndown. | DBM SEC-06 §Vapour Recovery |
| LP flare bypass | Suction header V-ball valve operated by VRU suction pressure | DBM SEC-06 §Vapour Recovery |
| LP fuel-gas source | Plant LP fuel-gas system (from 04-25 plant sales-gas splitter / Alliance secondary) | DBM SEC-07 §Fuel Gas |
| Capacity (flow rates, suction/discharge pressures) | `TBD` (location TBD — `26020-03-PT-RFQ-12-001_VRU_1_R0.docx` and `26020-Package_Requirements.docx` heading 43 not locally extracted in text-readable form) | Source location TBD |

## Construction

| Item | Value | Source |
|---|---|---|
| Building | Single building houses both trains | PACKAGE_REGISTER.csv row 100 |
| Modularisation | `TBD` | location TBD |
| Foundations / supports | EPC Integrator scope (interface type: Structural / Foundations / Supports) | PACKAGE_REGISTER.csv row 100 (interface types) |
| Applicable interface types (EPC Integrator scope) | Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports | PACKAGE_REGISTER.csv row 100 |
| Material selection | `TBD` (sour-service materials selection to be defined in DEL-090-02 Package Datasheet and DEL-090-04 Vendor Engineered Equipment Package) | location TBD |

## References

- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` — SEC-01 (Facility Overview / Supersession), SEC-06 (Liquids Hub Process … and Vapour Recovery — §Vapour Recovery), SEC-07 (Utilities — Fuel Gas).
- `_Sources/26020-Package_Requirements.docx` — package heading 43 (location TBD; docx not locally extracted as text).
- `_Decomposition/.../GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv` — row 100 (PKG-090).
- `_Decomposition/.../GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` — row 564 (DEL-090-01).
- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` (deliverable-local).

## Notes

- Bid-docs source `Bid Docs/Budgetary/26020-03-PT-RFQ-12-001_VRU_1_R0.docx` referenced by the package register row was NOT located under the accessible `_Sources/` tree; capacity, sizing, and detailed equipment-list values from that document are therefore `TBD` pending source access.
