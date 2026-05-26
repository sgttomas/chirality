# Guidance — DEL-047-01 Scope of Work (PKG-047 Vapour Recovery Unit 4-25)

> Directional document. Provides rationale, principles, considerations, and trade-offs. Open conflicts are surfaced in the Conflict Table for human ruling.

## Purpose

This deliverable is the **EPC Integrator anchor Scope of Work** for the 04-25 Vapour Recovery Unit package. Per the project decomposition (PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24, register row 570) it is a mandatory Gate 5 EPC anchor deliverable, defining the package scope, tagged equipment, package function, source basis, boundaries, and whole-facility integration narrative. It exists so that downstream vendor engineering (DEL-047-04), vendor document turnover (DEL-047-05), and EPC review/acceptance (DEL-047-06) have a single authoritative scope reference.

## Principles

1. **Source-grounded scope.** The VRU package scope is anchored to specific source slices of `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (notably §Vapour Recovery Unit, lines 1681-1791). Where the workbook (`26020-Packages_Interfaces_4_export.xlsx` row 101) or `26020-Package_Requirements.docx` heading 2 are not locally extracted into markdown, scope items are still cited but flagged `location TBD` rather than invented.
2. **Function-first description.** The package exists to capture low-pressure hydrocarbon vapours from storage tanks and process sources, recompress them, and route them to the SOC for recycle to the plant amine inlet (DBM line 1683). All requirements support this function.
3. **Boundary discipline.** The VRU package boundary is defined by: (a) downstream tie-in to the 04-25 SOC first-stage suction, (b) upstream vapour sources at tank-farm and process low-pressure points, (c) utilities tie-ins (LP fuel gas blanket/make-up, LP flare bypass and blowdown, electrical power, controls). Boundary exclusions are explicit (fresh caustic tank and TEG make-up tank are **not** on the VRU header — DBM lines 1562, 1232).
4. **Lead-lag with capacity headroom.** The 2 x 100% Ro-Flo configuration reflects a design philosophy of full sparing and capacity headroom (design 1.5 MMSCFD vs winter ~0.42 / summer ~0.58 MMSCFD expected — DBM lines 1694, 1704-1707). This anticipates tank-farm transient swings and future source additions.
5. **Vapour disposition priority.** Recovery (to SOC) > Flare > Vent. The setpoint ladder (1 oz shutdown → 16 oz thief hatch — DBM lines 1722-1730) encodes this priority and biases the system toward recovery under normal operation while protecting against tank overpressure.

## Considerations

### Condensation Risk
First-stage cooler discharge (48.9 °C) is below dewpoint (52.7 °C) at the heavy VRU composition — condensation is expected at the intercooler outlet (DBM line 1779). Detailed engineering must size the second-stage suction scrubber and cooler controls for liquid condensation, and should consider automatic warm-air recirculation (DBM line 1772). This is a known process risk that the Scope of Work must surface to the vendor.

### Heavy and Sour Composition
Inlet composition shows H2S 0.36 mol% plus mercaptans (C1RSH 0.39, C2RSH 1.71, C3RSH 0.30 mol%) and dimethyl/methyl-ethyl sulphides — sour service requirements apply. Material selection (NACE MR0175 / ISO 15156) is `ASSUMPTION:` applicable; `location TBD` for explicit specification. The vendor scope must include sour-service certification.

### Tank-Farm Pressure Control
The header to LP flare bypass (REQ-VRU-012) is the safety backstop preventing atmospheric tank EPRV/PVRV opening. Suction-header hydraulic design (minimise fittings and length, free-drain, dual pressure measurement at first-stage suction and tank-farm) is critical to keep tank vapour-space pressure controlled — this is a layout/routing requirement that must be communicated early to piping/plot plan engineering.

### Cross-Facility Coupling (03-25 ↔ 04-25)
Both 04-25 and 03-25 VRU discharges land at the 04-25 SOC first-stage suction (DBM line 1683). Capacity contributions from 03-25 are listed as TBD in the SOC source table (line 751), and the 03-25 VRU module is not covered here. The interface to 03-25 should be made explicit in the integration narrative and tracked as an external scope dependency.

### Glycol / BTEX Recovery Pathway
TEG regeneration overheads are condensed upstream, with BTEX mixed with stripping gas and recompressed via VRU to plant inlet; recovered liquids go to produced water tanks (DBM line 1781). This recovery pathway is environmental-significant (BTEX emissions control) and must be preserved through scope/vendor definition.

## Trade-offs

| Trade-off | Considerations |
|---|---|
| Manual vs automatic warm-air recirculation | Manual is simpler and cheaper; automatic reduces condensation risk and improves operability at variable ambient conditions (DBM line 1772). |
| Recycle-valve sizing | Sizing for 100% flow at minimum speed / lowest discharge ensures controllability at minimum load; oversizing risks instability at low flow. |
| Header-to-flare valve capacity | Larger capacity reduces tank PVRV risk during VRU outage; smaller capacity reduces flare loading on routine trips. Source mandates "at minimum maximum VRU flow" (DBM line 1789). |
| 200 hp vs 300 hp driver | See Conflict Table CT-01. Higher rating preserves headroom and futureproofs against unknown high-end source rates; lower rating reduces capex and electrical load. |

## Examples

- **Normal operation (expected summer):** Stage 1 ~0.58 MMSCFD, Stage 2 ~0.56 MMSCFD; one VRU online with the second on lead-lag standby; capacity-control recycle valve modulates to hold first-stage suction at the 3 oz control setpoint; make-up fuel gas blanket inactive (DBM lines 1707, 1725, 1727, 1783).
- **Source surge:** Inlet pressure rises to 5 oz → second VRU package auto-starts; if pressure continues toward 8 oz, suction valve/regulator opens to LP flare (DBM lines 1728-1729).
- **VRU outage:** Both compressors down → V-ball control valve on suction header to flare opens, bypassing recovery to LP flare to prevent tank EPRV lift (DBM line 1787).

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| CT-01 | VRU motor power: "200 hp TBC and 300 hp conflict requires ruling" | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §VRU Configuration and Design Parameters (line 1698) | same source records the conflict; no resolving source available | Datasheet §Design Conditions row "Motor power"; Specification REQ-VRU-004 | PROPOSAL: 300 hp to preserve headroom against design 1.5 MMSCFD capacity and 4,000 V driver class | TBD |
| CT-02 | Motor speed range "310 to 760 rpm, TBC" — TBC qualifier indicates unconfirmed range | DBM line 1699 | none | Datasheet §Design Conditions; Specification REQ-VRU-003 | PROPOSAL: retain as TBC until vendor confirms | TBD |
| CT-03 | First/second-stage suction MAWP and design temperatures listed TBC | DBM lines 1732-1737 | none | Datasheet §Design Conditions; Specification REQ-VRU-006 | PROPOSAL: vendor to confirm during detailed engineering | TBD |
| CT-04 | VRU gas-source rates (compressor sweep/purge, sales-booster sweep/purge, produced water, C5+ slop/storage, amine slop/surge tanks) shown TBC | DBM lines 1709-1720 | none | Datasheet §VRU Gas Sources; Specification REQ-VRU-016 | PROPOSAL: vendor + tank-farm engineering reconcile during detailed engineering | TBD |
| CT-05 | Suction-header-to-flare valve capacity stated "to be confirmed but must at minimum handle the maximum VRU flow condition" | DBM line 1789 | none | Specification REQ-VRU-012 | PROPOSAL: size to maximum VRU flow + applicable surge margin | TBD |
| CT-06 | Package requirements source `26020-Package_Requirements.docx` heading 2 not locally extracted; SOW-0253..0256 mapping not literal-text verified | `_REFERENCES.md` Missing/Deferred section | DBM is the surrogate substantive source | All requirements; coverage matrix in Procedure §Records | PROPOSAL: schedule extraction of the package-requirements doc and reconcile any deltas | TBD |
