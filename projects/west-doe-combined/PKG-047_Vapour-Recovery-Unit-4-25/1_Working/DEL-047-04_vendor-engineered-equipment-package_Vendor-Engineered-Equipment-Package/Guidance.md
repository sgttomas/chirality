# Guidance — DEL-047-04 Vendor Engineered Equipment Package (VRU 4-25)

## Purpose

The Vendor Engineered Equipment Package is the Package Vendor's production unit for PKG-047 Vapour Recovery Unit 4-25. It exists so that the EPC Integrator's Scope of Work (DEL-047-01) and Package Datasheet (DEL-047-02) are converted into a fully engineered, fabricated, sour-service VRU compressor package that can be installed and integrated into the West Doe Deepcut (04-25) plant. (Source: DELIVERABLE_REGISTER.csv DEL-047-04; PACKAGE_REGISTER.csv PKG-047.)

The VRU's facility function is to capture hydrocarbon vapours from storage tanks and low-pressure process vapour sources, compress and cool them, and discharge recovered vapour to the stabilizer overheads compressor first-stage suction. Both 04-25 and 03-25 VRU discharges route to the 04-25 stabilizer overheads compressor first-stage suction. (Source: DBM 4-25, "Vapour Recovery Unit".)

## Principles

- **Source-anchored engineering.** Vendor engineering shall be grounded in the EPC Package Datasheet (DEL-047-02) and the project Scope of Work (DEL-047-01). Where DBM 4-25 provides design conditions (capacity, pressures, composition), they shall be honored or formally reconciled. (Source: package architecture, DELIVERABLE_REGISTER.csv.)
- **Sour-service discipline.** Inlet composition includes H2S 0.3557 mol% plus mercaptans, disulphides, and CS2; all wetted materials, seals, and gasketing shall be selected accordingly. (Source: DBM 4-25, VRU Inlet Composition.)
- **Condensation risk management.** Heavy VRU composition and the first-stage cooler discharge below dewpoint (48.9 °C vs 52.7 °C) create condensation at the first-stage intercooler outlet. Scrubber sizing, cooler control, and drain provisions shall design for this condition rather than treat it as off-design. (Source: DBM 4-25, VRU Scrubbing/Cooling/Blowdown/Controls.)
- **Lead-lag operability.** The 2 x 100% architecture is intended to permit on-line maintenance and continuous tank-vapour recovery; the package controls and sweet-gas purge connection support train isolation without facility upset. (Source: DBM 4-25.)
- **Tank-vapour space protection.** The design intent of the suction header to flare valve, recycle valve, make-up gas regulator, and pressure setpoint ladder is to minimize the risk of atmospheric tank EPRV/PVRV opening. Vendor controls shall not undermine this intent. (Source: DBM 4-25.)

## Considerations

- **Driver rating is unsettled.** The package summary cites 200 hp VFD motors, but the DBM explicitly flags a 200 hp / 300 hp conflict requiring ruling. Vendor selections (motor, VFD, electrical room loads) shall not be frozen against 200 hp until the conflict is resolved. (Source: PACKAGE_REGISTER.csv; DBM 4-25, VRU Configuration; Interfaces / Open Design.)
- **Building arrangement is unsettled.** The package summary describes both trains in one building; the DBM describes each VRU in an individual building. Civil/structural, HVAC, electrical area-classification, and fire/gas designs all depend on the resolution. (Source: PACKAGE_REGISTER.csv; DBM 4-25.)
- **Pressure setpoint ladder is binding on controls.** The 1 oz / 2 oz / 2.5 oz / 3 oz / 5 oz / 8 oz / 16 oz inlet-pressure setpoint actions are explicit in the DBM and should be implemented as the package control philosophy rather than as advisory values. (Source: DBM 4-25, VRU inlet pressure table.)
- **Capacity values are mostly TBC.** Design capacity (1.5 MMSCFD per train) and per-source flows are TBC and to be reviewed in detailed engineering; vendor sizing margins should remain explicit. (Source: DBM 4-25, VRU inlet capacity table; gas-source table.)
- **MAWP and design temperatures.** Suction MAWPs and all VRU system-point design temperatures are TBC; vendor MAWP/temperature selections shall be reconciled to project equipment-class basis before final design. (Source: DBM 4-25, VRU system MAWP table.)
- **Interface scope owned by EPC.** Per PACKAGE_REGISTER.csv responsibility text, integration (tie-ins, constructability, procurement/construction coordination, facility-level integration) is EPC Integrator scope; vendor should expose, not absorb, facility-level decisions through the interface types listed for PKG-047.

## Trade-offs

- **Recycle vs make-up gas at turndown.** Both the capacity-control recycle valve and the make-up/blanket gas regulator stabilize suction at low load. Vendor logic should sequence them to minimize fuel-gas consumption while protecting the suction setpoint ladder. (Source: DBM 4-25.)
- **Manual vs automatic warm-air recirculation.** Base design is manual louvers; DBM notes automatic recirculation is to be considered to reduce condensation risk. Auto recirculation reduces operator burden and condensate handling at the expense of cost and complexity. (Source: DBM 4-25.)
- **Mist pad vs mesh/vane scrubber internals.** DBM directs mist pads (not mesh/vane). This is conservative for fouling-tolerant sour service but yields lower removal efficiency at high gas loads; sizing K-factor 0.25 (Imperial) with operating-pressure de-rating is the offset. (Source: DBM 4-25.)
- **Sour-service materials selection.** More aggressive materials (e.g., higher alloying) reduce cracking risk and broaden barrier-fluid options but increase cost; selection should be tied to the resolved standards basis (currently location TBD). (ASSUMPTION; location TBD.)

## Examples

- The DBM-stated lead-lag start sequence is exemplified by the inlet-pressure setpoint ladder: at 3 oz the lead VRU is at control setpoint; at 5 oz the second VRU is started; at 8 oz the suction header to flare valve opens; at 16 oz tank thief hatches set the final mechanical relief. (Source: DBM 4-25, VRU inlet pressure table.)
- The recovered-vapour routing pattern is exemplified by: BTEX mixed with stripping gas is recompressed to the plant inlet; recovered liquids are pumped to produced water tanks; water/C5+ tank vapours are compressed and recovered through the package; the package discharge feeds stabilizer overheads compressor first-stage suction. (Source: DBM 4-25, VRU Scrubbing/Cooling/Blowdown/Controls; Interfaces section.)

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted Sections | Proposed Authority (PROPOSAL) | Human Ruling (TBD) |
|---|---|---|---|---|---|---|
| CONF-01 | VRU motor driver rating | PACKAGE_REGISTER.csv PKG-047 summary: "200 HP VFD motor" | DBM-Deepcut/4-25_Deepcut_DBM.md, VRU Configuration: "Motor power: TBD; 200 hp TBC and 300 hp conflict requires ruling" | Datasheet attributes; Specification REQ-4; Guidance considerations; Procedure performance verification | PROPOSAL: hold both values open; do not freeze VRU motor/VFD or electrical-room sizing until EPC Package Datasheet (DEL-047-02) resolves rating. | TBD |
| CONF-02 | Number of buildings housing the two VRU trains | PACKAGE_REGISTER.csv PKG-047 summary: "both housed in one building" | DBM-Deepcut/4-25_Deepcut_DBM.md, VRU Configuration: "Each VRU is installed in an individual building" | Datasheet construction; Specification REQ-2; Guidance considerations; Procedure prerequisites and verification | PROPOSAL: defer to EPC Package Datasheet (DEL-047-02) and Plot Plan. The DBM is the design-basis authority; the package summary is a derived narrative. Lean toward two buildings unless overridden. | TBD |
| CONF-03 | Several VRU values marked TBC/TBD in DBM (suction MAWPs, all design temperatures, driver speed range, per-source flow contributions) | DBM-Deepcut/4-25_Deepcut_DBM.md VRU sections | (No second source locally accessible) | Datasheet process conditions; Specification REQ-6, REQ-11; Procedure verification | PROPOSAL: vendor shall not invent values; resolve through detailed engineering inputs from EPC and update Package Datasheet (DEL-047-02). | TBD |
