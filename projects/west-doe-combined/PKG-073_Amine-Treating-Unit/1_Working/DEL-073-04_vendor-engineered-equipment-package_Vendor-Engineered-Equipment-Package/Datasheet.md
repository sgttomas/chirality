# Datasheet — Vendor Engineered Equipment Package (DEL-073-04)

> Pass 1/Pass 2 draft. Source-grounded where the locally accessible Deepcut Design Basis Memorandum (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-06 "Amine Treating Basis") supports specific values. Other values marked `TBD` or `ASSUMPTION` per the four-documents skill.
>
> NOTE on source availability: The decomposition row cites `26020-Package_Requirements.docx package heading 27`. The .docx is present in `_Sources/` but is a binary file and is NOT locally accessible as parseable text. Anchoring is done against the Deepcut DBM, which is the locally accessible authoritative process basis for the 04-25 Amine Treating Unit (PKG-073). Items that would have been confirmed by the package-requirements heading are left as `location TBD`.

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-073-04_vendor-engineered-equipment-package` | `_CONTEXT.md` |
| Name | Vendor Engineered Equipment Package | `_CONTEXT.md` |
| ParentPackageID | `PKG-073` (Amine Treating Unit) | `_CONTEXT.md` |
| Facility | 04-25 Deep Cut Gas Plant (West Doe Deepcut expansion) | DBM-Deepcut SEC-01 (Facility Identity) |
| Workbook row | Packages row 49 | `_CONTEXT.md` / DELIVERABLE_REGISTER |
| Discipline | Mechanical (vendor-led, EPC integration review) | `_CONTEXT.md` |
| Production-unit type | Vendor Package Production Unit | `_CONTEXT.md` |
| Responsible party | Package Vendor (engineering/design/equipment); EPC Integrator integration review | `_CONTEXT.md` |
| Covered SOW items | SOW-0051, SOW-0052, SOW-0053, SOW-0054 | `_CONTEXT.md` |
| Supported objectives | OBJ-001, OBJ-003 through OBJ-010 (ASSUMPTION — package-grouping heuristic) | `_CONTEXT.md`; OBJECTIVE_DELIVERABLE_MAP |

## Package Function (Attributes)

| Attribute | Value | Source |
|---|---|---|
| Unit purpose | Remove H2S from high-pressure inlet gas with controlled CO2 slip using an MDEA-based solvent | DBM-Deepcut SEC-06 §"Amine Treating Basis" → "Process Description" (L1141) |
| Solvent | MDEA-based (selective) | DBM-Deepcut SEC-06 §"Process Description" (L1141); SEC-01 (L41) |
| Sweet gas H2S target | ≤4 ppmv at absorber outlet | DBM-Deepcut SEC-06 §"Amine Design Values" (L1156) |
| Sales-gas CO2 driver | ≤2 mol% CO2 (governs MDEA CO2-slip selection) | DBM-Deepcut SEC-06 §"Amine Design Values" (L1158) |
| Inlet H2S basis | ~1.0 mol% H2S at plant inlet (may vary with SOC discharge blend) | DBM-Deepcut SEC-06 §"Amine Design Values" (L1159) |
| Mercaptan recovery | 0% (no process design credit) | DBM-Deepcut SEC-06 §"Amine Design Values" (L1157) |

## Design / Operating Conditions

| Parameter | Value | Source |
|---|---|---|
| Raw inlet flow, summer | Low 300 MMSCFD; normal/high/design 307.5 MMSCFD | DBM-Deepcut SEC-06 (L1150) |
| Raw inlet flow, winter | Low 300 MMSCFD; normal/high/design 312.0 MMSCFD | DBM-Deepcut SEC-06 (L1151) |
| Inlet temperature | Winter 36.8 °C (98.3 °F); summer 44.1 °C (111.3 °F) | DBM-Deepcut SEC-06 (L1152) |
| Operating pressure | Normal/design 7722 kPag; low operating pressure TBD | DBM-Deepcut SEC-06 (L1155) |
| Hydrate margin | Maintain inlet ≈6 °C above expected hydrate T; no methanol provisions in amine area | DBM-Deepcut SEC-06 (L1153) |
| HC dewpoint margin | Maintain inlet ≈6 °C above expected HC dewpoint | DBM-Deepcut SEC-06 (L1154) |
| Site design ambient | −40 °C to +35 °C | DBM-Deepcut SEC-02 (L198) |

## Construction / Equipment Composition

The deliverable is the physical vendor-engineered package consisting of (at minimum) the items below. Source: DBM-Deepcut SEC-06 §"Module and Package Configuration" (L1131–L1132) and §"Amine Equipment and Design Requirements" (L1163–L1179).

| Function | Configuration | Source |
|---|---|---|
| Amine inlet gas filter/coalescers | 2 × 100% | L1165 |
| Amine absorbers | 2 × 50%, upflow contacting, top demister | L1166 |
| Sweet gas scrubber | Not included as a separate downstream item in current basis | L1167 |
| Amine flash tank | ~60 psig; HC skim box; manual HC drain | L1168 |
| Anti-foam / chemical injection | Pump flow rate TBD | L1169 |
| Amine filtration | Full-flow rich-amine particle filter @ 5 µm nominal; 25% lean-amine slipstream through carbon + 5 µm; LP fuel-gas purge before opening | L1170 |
| Lean/rich amine exchangers | 2 × 50% plate-and-frame | L1171 |
| Lean amine cooler | Cools to 15 °F above absorber inlet T or 110 °F (whichever lower); warm-air recirculation and plenum heat | L1172 |
| Amine surge tank | ~30 min surge at design circulation; insulation; LP fuel-gas blanket; coating; heater; truck-out; secondary containment | L1173 |
| Amine booster pumps | 2 × 115%; single-stage vertical inline; single mechanical seal | L1174 |
| Amine charge pumps | 3 × 57.5%; API-610 multi-stage horizontal centrifugal axial split (model TBC) | L1175 |
| Amine regenerator | 20 actual trays (18 for stripping); ≤70% jet/downcomer flood; two water-wash stages | L1176 |
| Amine reboiler | BKU kettle; hot oil; 350 °F supply; skin ≤350 °F to limit degradation | L1177 |
| Amine reflux condenser & accumulator | Partial condenser to 110 °F; demister; HC skim; reflux-water purge; auto pressure control to LP flare; dilution-gas review for high-CO2 acid gas | L1178 |
| Amine reflux pumps | 2 × 115%; single-stage vertical inline; single mechanical seal | L1179 |
| Module 520 (HP filtration, sweetening, TEG dehy) | Includes amine inlet coalescers, amine absorbers (interface module) | L1131 |
| Module 530 (Amine regeneration module/building) | Houses flash drum, filters, reboiler, regenerator, surge tank, pumps, make-up storage, slop tank | L1132 |

## References

- `_REFERENCES.md`
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — SEC-01, SEC-02, SEC-06 (locally accessible authoritative basis)
- `26020-Package_Requirements.docx` package heading 27 — cited by decomposition; **location TBD** (binary not parseable in this environment)
- GATE-07 PROJECT_DECOMP snapshot — DELIVERABLE_REGISTER row for DEL-073-04

## Open / TBD Items

- Sweet gas H2S target met against `1.0 mol%` inlet H2S — vendor must demonstrate by simulation (TBD pending vendor process design).
- Low operating pressure — TBD.
- Amine surge tank design SG, design pressure, and vent flow — TBD/TBC.
- Anti-foam injection pump flow rate — TBD.
- Amine charge pump model — TBC.
- Material selection at low H2S/CO2 ratios — TBD review required.
- Final mercaptan adsorption credit (incidental at low H2S loading) — not credited in design.
- Confirmation against `26020-Package_Requirements.docx` heading 27 — **TBD** (source not locally parseable).
