# Datasheet — DEL-052-02 Package Datasheet (PKG-052 Inlet / TEG Dehy Cross Exchanger)

> EPC Integrator package datasheet for the Inlet / TEG Dehy Cross Exchanger package. Values are source-grounded where available; missing values are marked `TBD`; inferences are labeled `ASSUMPTION`.

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | DEL-052-02_package-datasheet | `_CONTEXT.md` |
| Deliverable name | Package Datasheet | `_CONTEXT.md` |
| Parent package ID | PKG-052 | `_CONTEXT.md`; PACKAGE_REGISTER.csv row 62 |
| Parent workbook ID | 52 | `_CONTEXT.md` |
| Package name | Inlet / TEG Dehy Cross Exchanger | PACKAGE_REGISTER.csv row 62 |
| WBS | 01 | PACKAGE_REGISTER.csv row 62 |
| Package tag (lead RFQ) | 26020-01-PT-16-001 | PACKAGE_REGISTER.csv row 62 (Lead Equipment Tag) |
| Source RFQ document | Bid Docs/Budgetary/26020-01-PT-RFQ-16-001-Heat_Ex_ST.docx | PACKAGE_REGISTER.csv row 62 (Word Source Basis); local markdown not available |
| Discipline | Mechanical | `_CONTEXT.md` |
| Type | EPC Package Datasheet | `_CONTEXT.md` |
| Responsible party | EPC Integrator | `_CONTEXT.md` |
| Package vendor scope | Package engineering, package design, vendor documentation, physical equipment package | PACKAGE_REGISTER.csv row 62 (Responsibility) |
| EPC Integrator scope | Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, facility-level integration | PACKAGE_REGISTER.csv row 62 (Responsibility) |

## Tagged Equipment

| Tag | Description | Quantity | Source |
|---|---|---:|---|
| E-5718-1 | Inlet / TEG Dehy Cross Exchanger; shell-and-tube; TEMA "R" BEM | 1 | PACKAGE_REGISTER.csv row 62 (Description); DBM-Deepcut/4-25_Deepcut_DBM.md §"Inlet / TEG Dehy Cross Exchanger" (lines 595-606); §Equipment table (line 2586) |

## Process Function

Cold sour gas from the inlet separator flows to the TEG heat exchanger, where it exchanges heat with the warm-side process stream; the (now warmed) sour gas flows to the inlet compressors and downstream gas treating. The exchanger heats inlet separator overhead gas and cools a downstream warm process gas stream before that warm-side gas flows to process-gas molecular-sieve inlet filter/coalescers.

Source: PACKAGE_REGISTER.csv row 62 (Description); DBM-Deepcut/4-25_Deepcut_DBM.md §"Inlet / TEG Dehy Cross Exchanger" (line 606); §Process Description (lines 1119-1120, 1193).

CONFLICT: Warm-side stream identity is unresolved between (a) dehydrated overhead gas from the TEG contactor and (b) warm sweet gas leaving the amine sweetening unit. See `Guidance.md` Conflict Table.

## Design Attributes (E-5718-1)

| Attribute | Value | Source |
|---|---|---|
| Equipment class | Heat exchanger, shell-and-tube | DBM-Deepcut/4-25_Deepcut_DBM.md §"Inlet / TEG Dehy Cross Exchanger" (line 597); §Equipment table (line 2537) |
| TEMA type | TEMA "R" BEM | PACKAGE_REGISTER.csv row 62 (Description); DBM section text uses generic "BEM type described in the DBM source" — ASSUMPTION: TEMA "R" BEM per register row |
| Quantity | 1 | DBM table (line 601); §Equipment table (line 2586) |
| Service | Inlet sour gas (cold side) vs. warm-side process gas (identity TBD — see Conflict Table) | DBM section text (line 606) |
| Duty | 5,514.3 kW (18.82 MMBTU/hr) | PACKAGE_REGISTER.csv row 62 (Description) |
| Design pressure | 9,756 kPag (1,415 psig) | DBM table (line 603) |
| Design temperature | 66 °C | DBM table (line 604) |
| Tube-side fluid | Sour gas (per process function) | ASSUMPTION from DBM process narrative (lines 606, 1119-1120, 1193); not explicitly assigned in source |
| Shell-side fluid | Warm-side process gas (identity TBD) | ASSUMPTION; warm-side stream identity unresolved |
| Operating pressures | TBD | Not stated in accessible source slices |
| Operating temperatures | TBD | Not stated in accessible source slices |
| Mass flow rates (per side) | TBD | Not stated in accessible source slices |
| Allowable pressure drop | TBD | Not stated in accessible source slices |
| Materials of construction | TBD | Not stated in accessible source slices; deferred to RFQ/vendor selection |
| Corrosion allowance | TBD | Not stated in accessible source slices |
| Tube count / pitch / OD | TBD | Vendor scope per package responsibility split |
| Heat transfer area | TBD | Vendor scope; design data not in DBM section |
| Insulation | TBD | Not stated in accessible source slices |
| Nozzle sizes/ratings | TBD | Not stated in accessible source slices |

## Process Conditions Context (facility-level, not exchanger-specific)

| Parameter | Value | Source |
|---|---|---|
| Inlet separator total design vapour flow | 300 MMSCFD | DBM-Deepcut/4-25_Deepcut_DBM.md §"Inlet Pipeline Pressure and Flow" (line 622) |
| Facility inlet design flow (Winter) | 308 MMSCFD | Same table (line 620) |
| Inlet gathering design operating pressure | 653 psig | Same section (line 626) |
| Inlet gathering MAOP basis | 1,300 psig (90% of assumed upstream MAOP 1,440 psig — to be validated) | Same section (line 628) |
| Plant gate design pressure (downstream of inlet separator inlet PCV) | 1,360 psig to J-T valve/expander outlet (600# flanges at 200 °F basis) | Same section (line 628) |
| Inlet service (downstream) compressor suction | 4,309 kPag (625 psig) | DBM §"Inlet Compression" (line 889) |
| Inlet service compressor discharge | 7,791 kPag (1,130 psig) | DBM §"Inlet Compression" (line 889) |

## Construction / Integration

| Item | Value | Source |
|---|---|---|
| Skid / package boundary | Package includes the exchanger plus accompanying piping/instrumentation and skid | PACKAGE_REGISTER.csv row 62 (Description) |
| Module assignment (warm-side context) | Module 520 — high-pressure gas filtration, sweetening, and TEG dehydration | DBM-Deepcut/4-25_Deepcut_DBM.md §Module Equipment (line 1131) |
| Plot / foundations | TBD — facility-level integration | EPC Integrator scope |
| Piping tie-in points | TBD; declared interface types listed below | PACKAGE_REGISTER.csv row 62 (Applicable interface types) |

## Applicable Interface Types (PKG-052)

Source: PACKAGE_REGISTER.csv row 62 (Applicable interface types).

- Process Piping
- Utility Piping
- Drain / Containment
- EHT (Electric Heat Trace)
- Grounding / Bonding
- Area / Exterior Lighting
- I&C / Control Cabling
- Maintenance Access
- Structural / Foundations / Supports

## Package Interface Requirements Matrix

| Interface type | EPC Integrator responsibility | Package Vendor responsibility | Tie-in / boundary | Notes |
|---|---|---|---|---|
| Process Piping | Tie-in design; field routing; isolation philosophy | Package nozzles, package internal piping, terminal points | TBD (location/elevation) | Cold-side inlet from inlet separator overhead; cold-side outlet to inlet compression. |
| Utility Piping | Supply route to skid edge | Skid internal headers | TBD | Utility list TBD; not stated in accessible sources. |
| Drain / Containment | Drain header tie-in; containment grading | Skid drip pans, low-point drains | TBD | DBM does not specify per-package drain points. |
| EHT (Electric Heat Trace) | Power, control, supervision | Heat-trace-ready surfaces, terminations on skid | TBD | Per declared interface; per-line need TBD. |
| Grounding / Bonding | Grid ties; equipotential | Bonding lugs on skid steel and equipment | TBD | TBD per equipment list. |
| Area / Exterior Lighting | Lighting layout in package area | Lighting fixtures on skid (if any) | TBD | Standard PKG-052 interface; specifics TBD. |
| I&C / Control Cabling | Cable tray routing to skid edge; DCS/PLC integration | Skid junction boxes, instrument loops, vendor PLC (if any) | TBD | Loop list TBD; not stated in accessible sources. |
| Maintenance Access | Plot space, lay-down, lifting plan | Lifting lugs, tube-bundle pull length declaration | TBD | Tube-bundle pull length TBD; vendor input required. |
| Structural / Foundations / Supports | Civil foundations, anchor design | Skid base, anchor pattern, base loads | TBD | Anchor loads and skid GA TBD; vendor scope. |

## References

- `_CONTEXT.md`
- `_REFERENCES.md`
- PACKAGE_REGISTER.csv row 62 — `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv`
- DELIVERABLE_REGISTER.csv row 337 — same snapshot
- DBM-Deepcut/4-25_Deepcut_DBM.md, §"Inlet / TEG Dehy Cross Exchanger" (line 595 ff.); §"Inlet Pipeline Pressure and Flow"; §Module 520 equipment list; §Equipment table (lines 2537, 2586) — `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`
- 26020-Package_Requirements.docx package heading 7 — location TBD (not converted to local markdown)
- 26020-01-PT-RFQ-16-001-Heat_Ex_ST.docx — location TBD (not converted to local markdown)
