# Guidance: DEL-046-04 — Vendor Engineered Equipment Package (Acid Gas Compressors)

## Purpose

The Vendor Engineered Equipment Package is the physical AGI compressor package(s) plus the engineering, design, and vendor documentation produced to deliver them. It exists so that the EPC Integrator receives a complete, vendor-warranted package that:

- compresses water-saturated acid gas (H2S + CO2) from amine regeneration to disposal-well injection pressure, and
- integrates cleanly into the 04-25 facility through declared interface types (process piping, utilities, relief/flare/vent, drains, electrical, controls, structural, HVAC, F&G).

(Sources: _CONTEXT.md scope; PACKAGE_REGISTER row PKG-046; DBM-Deepcut SEC-05.)

This deliverable does NOT cover facility-level integration (EPC Integrator scope), the acid gas disposal pipeline, or the disposal well/reservoir (excluded per DBM-Deepcut §System Boundaries).

## Principles

1. **Source-driven, vendor-engineered.** Process basis is set by the DBM (SEC-05); vendor delivers detailed engineering and the physical package consistent with that basis. Where the DBM is silent or marks TBC, the vendor proposes; the EPC Integrator and human authority confirm.
2. **Sour service first.** H2S concentration in the design case (~73 mol%) governs metallurgy, sealing, leak-minimization, and venting design at every level (exclusion of adjustable volume pockets, exclusion of manual isolation on recycle valves, sweet-gas purge before maintenance, packing-vent recovery, lube-injection into the disposal well).
3. **Designed-for-turndown and start-up.** Composition, flow, and pressure ranges shift across Design, Start-up, and High-CO2 cases. Recycle, VFD turndown, scrubber sizing, and cooler controls must hold operability across this envelope.
4. **Cold-climate operability.** -40 deg C ambient governs winterization (warm-air recirculation, heat-medium heating on coolers, building heating, freeze protection of small-bore drain/vent piping).
5. **Hydrate prevention discipline.** Recycle is also used to drop out water from 4th-stage suction; aftercooler to injection pipeline must be controlled to 8.3 deg C above maximum ambient; methanol injection provisions on the package; vendor confirms inhibition strategy in detailed engineering.
6. **Interface clarity over scope creep.** The vendor package boundary is set by the interface-type enumeration in the PACKAGE_REGISTER. Anything across that boundary is EPC Integrator integration scope.

## Considerations

- **Configuration choice.** The DBM detailed basis is 2x100% + 1 spare. A 3x50% alternative is recorded as TBD. The chosen configuration impacts compressor sizing, footprint, electrical load, control system, and spares strategy. (Conflict Table C-1.)
- **Compressor model conflict.** Ariel KBT/6 in detailed basis vs. KBK/6 in another DBM reference. Model selection drives frame size, cylinder availability for the staged pressures, and pulsation behavior. (Conflict Table C-2.)
- **5th-stage discharge pressure conflict.** 1,200 psig normal operating basis vs. 1,500 psig design-discharge reference. Picking the wrong number cascades into MAWP, pipeline hydraulic margin, and pulsation/torsional analysis assumptions. (Conflict Table C-3.)
- **Disposal well pressure data is owned by Tourmaline.** Lifetime operating envelope cannot be fully bounded until Design/Min/Max disposal well pressure values are confirmed. End-of-life pressure especially affects 5th-stage rod loads and the spare-strategy assumption.
- **Dry-out case is TBC.** Operational scenarios (start-up after blowdown, depressurization) need a dry-out case to confirm scrubber and seal behavior; flag for vendor proposal review.
- **Mercaptan condensation risk.** Low-temperature mercaptan condensation can affect dehydration, recycle rate, and compressor efficiency; warrants vendor analysis under the High-CO2 / cold cases.
- **Acid gas dehydration.** Recycle-to-35-to-60 lb H2O/MMSCF is to be considered if required by the disposal system; not a fixed requirement, but a vendor evaluation item with disposal-well interface input.
- **Recycle valve sizing corner case.** 100% capacity at minimum driver speed + maximum suction pressure + minimum pipeline pressure - fail-open is the design corner; vendor sizing must demonstrate this combination explicitly.
- **Adjustable volume pockets and manual isolation valves were intentionally excluded.** Do not re-introduce them in vendor proposal review without a documented leak-management trade-off.
- **Lube oil is consumed to the disposal well.** Drives lube selection, consumption rate disclosure, and any environmental/regulatory implications at the disposal interface.
- **Standards referenced as ASSUMPTION.** NACE MR0175/ISO 15156 and API 618 are industry-default for this service but were not located in the DBM source slice as explicit clauses — confirm in detailed engineering and pin the edition.

## Trade-offs

| Trade-off | Direction A | Direction B | Notes |
|---|---|---|---|
| Configuration | 2x100% + 1 spare (detailed basis) | 3x50% alternative (TBD) | Spare strategy and CAPEX vs. operational flexibility |
| Capacity control | VFD speed only | VFD + recycle (selected) | Selected supports no-flow scenarios without unloaders |
| Pulsation control | Adjustable volume pockets | Excluded (selected) | Selected reduces leak points at H2S cost-of-failure |
| Recycle isolation | Manual isolation valves | Excluded (selected) | Selected minimizes leak paths; serviceability impact |
| Dehydration scheme | In-package dehydration | Recycle-only dehydration (current) | Disposal well requirements may force change |
| Disposal metering | Low-pressure pre-comp | High-pressure post-comp Coriolis (selected) | Lower water content, smaller dP penalty |
| Vendor scope of integration | Skid-only delivery | Modular building (typical) | DBM does not state explicitly for AGI — ASSUMPTION |

## Examples

- **Start-up case dimensioning.** DBM gives 1.5 MMSCFD/unit at 0.603 MMSCFD total start-up flow. Vendor must show that scrubbers, recycle valves, and cooler control hold at this flow with composition shifted to the Start-up column (CO2 41.5 mol%, H2S 49.7 mol%, C1 1.89 mol%).
- **High-CO2 case rod loading.** Composition swap drives different MW, k-value, and discharge temperatures; vendor confirms rod load and frame fatigue under this case at design discharge pressure.
- **Cold-start example.** -40 deg C ambient start; recycle drives gas through coolers; warm-air recirculation and heat-medium prevent cooler freeze; sequenced loading per automated procedure.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-1 | AGI configuration: 2x100% + 1 spare vs. 3x50% alternative | DBM-Deepcut SEC-05 §Acid Gas Compressor Design Conditions (line ~994; "Two 100% acid gas compressor packages plus one spare compressor; possible three x 50% alternative TBD") | DBM-Deepcut SEC-05 same line records both | Datasheet "Configuration"; Specification R-...-001; Guidance Principles/Considerations | PROPOSAL: 2x100% + 1 spare (detailed basis) | TBD |
| C-2 | Compressor model: Ariel KBT/6 vs. KBK/6 | DBM-Deepcut SEC-05 §Acid Gas Compressor Design Conditions ("Ariel KBT/6, five-stage separable reciprocating compressor; conflicting KBK/6 reference remains TBD") | DBM-Deepcut elsewhere referencing KBK/6 (location TBD) | Datasheet attributes; Specification R-...-002 | PROPOSAL: KBT/6 detailed basis pending OEM confirmation | TBD |
| C-3 | 5th-stage discharge pressure: 1,200 psig normal vs. 1,500 psig design-discharge | DBM-Deepcut SEC-05 §Acid Gas Compressor Design Conditions ("1,200 psig normal, expander mode, and J-T mode") | DBM-Deepcut SEC-05 same paragraph ("1,500 psig design-discharge reference unresolved") | Datasheet Attributes & MAWP table; Specification R-...-007, R-...-008 | PROPOSAL: 1,200 psig normal operating; 1,500 psig retained as design-discharge ceiling pending verification | TBD |
| C-4 | Acid gas dehydration requirement | DBM-Deepcut SEC-05 ("dehydration by recycle to 35-60 lb H2O/MMSCF to be considered if required by the disposal system") | Disposal well/pipeline requirements pending Tourmaline | Specification scope; Guidance Considerations | PROPOSAL: defer to detailed engineering when disposal-well data is available | TBD |
| C-5 | Methanol injection capacities for AGI compressor package | DBM-Deepcut Hydrate-Inhibition table ("acid-gas compressor package has methanol injection provisions TBD") | None | Specification R-...-018 | PROPOSAL: vendor proposes capacity in detailed engineering | TBD |
