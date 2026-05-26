# Datasheet — DEL-098-04 Vendor Engineered Equipment Package

> Descriptive data for the Package Vendor production unit: engineering, design, fabrication/supply, and the physical equipment package for PKG-098 "Tanks, Sour Water (API 650) 3-25".

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-098-04_vendor-engineered-equipment-package` |
| Name | Vendor Engineered Equipment Package |
| ParentPackageID | `PKG-098` |
| PackageName | Tanks, Sour Water (API 650) 3-25 |
| Discipline | Mechanical |
| Type | Vendor Package Production Unit |
| ResponsibleParty | Package Vendor (engineering / design / equipment) with EPC Integrator integration review |
| Covers Scope Items | SOW-0221; SOW-0222; SOW-0223; SOW-0224 |
| Supports Objectives | OBJ-002; OBJ-003; OBJ-004; OBJ-005; OBJ-006; OBJ-007; OBJ-008; OBJ-009; OBJ-010 (ASSUMPTION — package-grouping heuristic, see `_CONTEXT.md`) |

## Attributes

### Tagged Equipment Within Package Scope

Source: SCOPE_LEDGER row SOW-0223 (`26020-Package_Requirements.docx` package heading 50; Major included equipment).

| Item | Qty | Nominal Capacity | Tags | Service |
|---|---|---|---|---|
| Item 1 — Sour Produced Water Storage Tanks | 3 | 3,800 bbl each | TK-9030-2, TK-9040-2, TK-9050-2 | Sour produced water storage |
| Item 2 — Sour Inlet Produced Water Storage Tanks | 2 | 3,800 bbl each | TK-9010-2, TK-9020-2 | Sour inlet produced water storage |
| Item 3 — Produced Water Storage Tanks | 2 | 3,800 bbl each | TK-9010-1, TK-9020-1 | Produced water storage (service classification — see Conflict C-1 in Guidance) |

Total: 7 tanks at 3,800 bbl nominal capacity.

### Common Construction Features (applies to Items 1–3)

Source: SCOPE_LEDGER row SOW-0223.

| Attribute | Value |
|---|---|
| Code of Construction | Modified API 650 |
| Internal coating | Devchem 253 applied to floor, walls, and roof |
| External insulation | Yes |
| External heating | Electric heating |
| Skim system | Kennilworth type HCL float skim system, one per tank |

Cross-reference: 3-25 DBM "Produced-Water Storage, Treatment, and Transfer" section confirms "API-650 Modified atmospheric tanks, externally insulated and heated, with Devchem 253 internal coating."

## Conditions

Source: SCOPE_LEDGER row SOW-0224 (`26020-Package_Requirements.docx` package heading 50; Scope notes and open items).

| Parameter | Operating | Design |
|---|---|---|
| Pressure | Atmospheric | 32 oz test pressure |
| Temperature (Items 1, 3) | 10 °C | -40 °C (min) / 60 °C (max) |
| Temperature (Item 2) | TBD (per source) | -40 °C (min) / 60 °C (max) |
| Capacity / design throughput | See Appendix A of source package (location TBD; not present in locally accessible slices) | — |
| Driver | TBD (per source) | — |

Site ambient basis (context — 3-25 DBM): -40 °C minimum ambient governs exposed equipment, package buildings, control panels, instrumentation, and field devices unless a more severe process or vendor condition applies.

### Service Fluid Basis (context from 3-25 DBM)

| Item | Value | Source |
|---|---|---|
| Produced-water density (pump basis) | 1.18 SG | 3-25 DBM "Liquids Hub Design Basis" table |
| Produced-water tank design SG | 1.25 (TBC) | 3-25 DBM "Liquids Hub Design Basis" table; "Produced-Water Storage, Treatment, and Transfer" |
| H2S service | ASSUMPTION (implied by "sour" classification; sour-service materials and corrosion allowance per applicable code — location TBD in source) | — |

## Construction

| Item | Basis | Notes |
|---|---|---|
| Tank design / fabrication | Modified API 650 | SOW-0223 |
| Internal coating | Devchem 253 (floor, walls, roof) | SOW-0223; DBM confirms |
| Insulation | External | SOW-0223 |
| Heat tracing / heating | External electric heating | SOW-0223; DBM confirms |
| Skim system | Kennilworth HCL float, one per tank | SOW-0223 |
| Foundations | By Others (excluded from vendor scope) | SOW-0224 |
| Site mounting of tanks | By Others | SOW-0224 |
| Electrical / Instrumentation | By Others | SOW-0224 |
| Platforms, staircase, etc. | By Others | SOW-0224 |
| Material selection / metallurgy | TBD — sour-service review required (ASSUMPTION) | — |
| Corrosion allowance | TBD (location TBD in source) | — |
| Manway / venting / drainage details | TBD (location TBD in source) | — |

## References

- `_REFERENCES.md` (this deliverable)
- SCOPE_LEDGER source slices: SOW-0221, SOW-0222, SOW-0223, SOW-0224 — `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/SCOPE_LEDGER.csv`
- DELIVERABLE_REGISTER — `_Decomposition/.../GATE-07.../DELIVERABLE_REGISTER.csv` row DEL-098-04
- Design Basis Memorandum (3-25) "Liquids Hub Design Basis" and "Produced-Water Storage, Treatment, and Transfer" — `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`
- Underlying source (not locally readable as text): `_Sources/26020-Package_Requirements.docx` package heading 50; Appendix A (capacity / throughput) — **location TBD** for full text
- Packages/Interfaces export (not locally readable as text): `_Sources/26020-Packages_Interfaces_4_export.xlsx`
