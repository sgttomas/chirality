# Guidance — DEL-086-03 Construction Work Package (Flare Stack, Low Pressure)

> Directional guidance for preparing and executing the LP Flare Stack Construction Work Package. Rationale is grounded in DBM source slices where available; otherwise items are `TBD` or labeled `ASSUMPTION`.

## Purpose

PKG-086 is the LP flare element of the shared facility flare system. The LP element does not stand alone: it physically piggy-backs on the common HP/Cryo flare stack physically located at 03-25 and shared with 04-25 (DBM-Deepcut `4-25_Deepcut_DBM.md` line 2030-2031; DBM-Comp_and_Liquids `3-25_Comp_and_Liquids_DBM.md` line 497). The Construction Work Package exists to make explicit how this shared, multi-service relief element is built, tied in, inspected, and turned over without ambiguity between PKG-085 (HP) and PKG-086 (LP) construction scopes and between the 03-25 and 04-25 facility owners.

## Principles

1. **Source authority over convention.** Where the DBMs state values (header sizes, radiation limits, KO drum tagging, fuel-gas LHV), those values govern. Generic flare-construction practice may be invoked for unstated items, but must be flagged `ASSUMPTION` until the source-of-truth installation specification is issued.
2. **Construction respects the shared-stack reality.** PKG-085 (HP) and PKG-086 (LP) share the same physical stack structure (DBM-Deepcut line 2030-2031). Construction sequencing, scaffolding, NDE access, and turnover must be coordinated with PKG-085 to avoid double-handling.
3. **Header drainage and freeze protection are first-class construction concerns.** LP wet relief headers and the VRU-suction-to-flare bypass must free-drain to the LP KO drum without traps (DBM-Deepcut line 1787). Heat-tracing/insulation of LP wet headers is treated as required pending explicit LP source language (location TBD; see Conflict Table item C-2).
4. **Smokeless and radiation performance are construction commitments, not just design intents.** The OGPFR radiation limits (<= 9 kW/m^2 inside boundary; <= 5 kW/m^2 outside) and the Ringelmann 1 smokeless target are how this package will be judged after installation (DBM-Deepcut lines 285-286, 2031, 2050, 2057).
5. **Open items are visible, not hidden.** LP element OD, final stack height, pilot/purge rates, and LP-element-specific dimensional and air-assist parameters are TBD/TBC in the DBM (DBM-Deepcut lines 1892, 2031; DBM-Comp_and_Liquids line 499) and shall remain explicitly flagged in the CWP until vendor-issued data closes them.

## Considerations

| Topic | Consideration | Source / Note |
|---|---|---|
| Shared 03-25/04-25 service split | The exact LP service-split between 03-25 and 04-25 is an open interface item; CWP must reference the current allocation rather than re-invent it. | DBM-Comp_and_Liquids line 56 |
| LP services received | TEG regen, VRU (incl. V-ball suction bypass), compressor seal pots; on Deepcut side also amine regen, mole-sieve regen contaminated blowdown, primary seal vents. | DBM-Comp_and_Liquids line 499; DBM-Deepcut lines 1781, 1787, 1801, 1702, 2029 |
| KO drum tag inconsistency | DBM-Comp_and_Liquids cites V-3900-2 (with pump P-3900-2); DBM-Deepcut cites V-3900-1 (with pump P-3900-1). Treat as Conflict C-1 below; do not pick silently. | DBM-Comp_and_Liquids line 499 vs DBM-Deepcut line 2029 |
| Stack geometry | Common HP/Cryo element 660 mm OD x 200 ft tall (TBC); LP element OD TBD. CWP scaffolding/lift basis cannot be finalized until OD is set. | DBM-Deepcut line 2030-2031 |
| Pilot/purge gas | Both HP/Cryo and LP pilot/purge gas rates are TBC. Pilot gas tie-in sizing and metering should be roughed in with margin. | DBM-Deepcut lines 1891-1892 |
| Fuel-gas LHV | Supplemental fuel gas required so blended LHV >= 20 MJ/Sm^3 at the stack. Construction must include the supplemental fuel tie-in and metering. | DBM-Deepcut line 2033 |
| Staggered blowdown | Detailed engineering should consider staggered blowdown to limit simultaneous load on the common stack; CWP should anticipate associated logic-test scope at commissioning. | DBM-Deepcut line 2046 |
| 26020 package requirements | The package-level construction requirements in `26020-Package_Requirements.docx` (heading 39) and the workbook row 59 are referenced by the decomposition but are not currently in locally readable text form. CWP authoring should extract those slices before final issue. | `_REFERENCES.md`; `_CONTEXT.md` Source Reference |

## Trade-offs

| Trade-off | Discussion |
|---|---|
| Sequence with PKG-085 erection | Erecting LP element with HP/Cryo element on the shared stack reduces scaffolding/lift cost but constrains schedule float on PKG-086. Recommend joint lift plan with PKG-085. |
| Field run versus pre-routed headers | Pre-routing the LP relief header minimizes hydrotest joints but increases interface-freeze risk while LP service-split (03-25/04-25) remains open. |
| Air-assist blower sizing margin | Sizing for emergency-design Ringelmann 1 at ~5% (TBC) gives smokeless confidence but increases mechanical/electrical install scope. |
| Heat-trace coverage scope | Tracing all LP wet headers conservatively (treating as required per HP rule) increases install cost; deferring until explicit LP language is found risks rework. Recommend conservative scope (see Principle 3). |

## Examples

> Examples are limited to what the accessible source slices actually describe. Generic flare-construction examples are intentionally avoided.

- Example interface set the CWP must address (from INTERFACE_REGISTER.csv PKG-086): Utility Piping (IFC-1C34D7D89E); Relief/Flare/Vent (IFC-EB7F1FB622); Drain/Containment (IFC-E6A8FB7494); Electrical Power (IFC-BBFB496745); Grounding/Bonding (IFC-8EDD15EE39); I&C/Control Cabling (IFC-6480D60C39); Fire & Gas/Safety Systems (IFC-858FFC2D67); Structural/Foundations/Supports (IFC-6C801F708F).
- Example construction-relevant tie-in: VRU-suction-to-LP-flare header — V-ball control valve with downstream check valve (<0.25 psid at design), header free-draining toward LP KO with no traps (DBM-Deepcut line 1787).

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| C-1 | LP flare KO drum and pump tags differ between the two DBMs (V-3900-1/P-3900-1 vs V-3900-2/P-3900-2). | DBM-Deepcut `4-25_Deepcut_DBM.md` line 2029 | DBM-Comp_and_Liquids `3-25_Comp_and_Liquids_DBM.md` lines 499, 584 | Datasheet "Conditions" and "Construction"; Specification R-CWP-04; Procedure prerequisites and verification | PROPOSAL: adopt the tag used in the 03-25 area drawings (likely V-3900-2 since shared stack is physically at 03-25) and note the cross-reference. Confirm against P&ID issue. | TBD |
| C-2 | Heat-tracing/insulation rule is stated for HP flare headers; an explicit LP statement is not located in the accessible source slices. | DBM-Deepcut line 2033 (HP rule) | None located (LP) — `location TBD` | Datasheet "Conditions"; Specification R-CWP-11; Procedure verification | PROPOSAL: apply the same freeze-protection rule to LP wet-service headers as conservative default. | TBD |
| C-3 | The 26020 package requirements document (heading 39) and workbook row 59 are cited as authoritative but are only available as binary files (.docx/.xlsx) locally; their content slices cannot be quoted in this draft. | `_REFERENCES.md` Source Materials | `_Sources/26020-Package_Requirements.docx`; `_Sources/26020-Packages_Interfaces_4_export.xlsx` | All four documents | PROPOSAL: extract `26020-Package_Requirements.docx` heading 39 and workbook row 59 to markdown and re-run this skill (RUN_PASSES: P3_ONLY or FULL) to absorb the slices. | TBD |
