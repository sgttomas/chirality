# Guidance: DEL-031-03_construction-work-package — Construction Work Package

## Purpose

The Construction Work Package for `PKG-031` (Transformer TXP-8500-1, 3 MVA 13.8 kV / 600 V step-down distribution transformer) provides the EPC Integrator's authoritative installation, tie-in, inspection, and turnover basis for transferring a vendor-engineered transformer package into the functional 04-25 facility. It exists to translate package-vendor scope and workbook interface facts into field-executable construction work fronts with controlled responsibility hand-offs.

## Principles

- **Responsibility clarity.** Package Vendor owns package engineering, design, vendor documentation, and the physical equipment package. The EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. (`PACKAGE_REGISTER.csv` `PKG-031`)
- **Field-construction assignment.** Off-loading, setting, mechanical hookup, shipped-loose installation, electrical terminations, home-run cabling, area lighting, and demolition where required are Tourmaline field construction scope. (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, lines 101-125)
- **Interface-driven CWP.** Workbook interface facts (Electrical Power, Grounding/Bonding, Lighting, I&C, Comms, Maintenance Access, Structural) define the work fronts that the CWP must close.
- **Cross-discipline coordination first.** Package buildings, MCC interfaces, RIO interfaces, heat tracing, HVAC, fire/gas detection, and drain/vent tie-ins shall be coordinated with civil, electrical, controls, and instrumentation sections before construction. (`_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, line 619)
- **Plot-plan and register alignment before IFC.** Final CWP and miscellaneous facilities list shall be aligned with the plot plan, equipment list, and CWP register before issue for construction. (`_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, line 661)

## Considerations

- **Geotechnical maturity.** Until the final geotechnical report is accepted, foundation and pile values are placeholders; the CWP should sequence civil work to absorb late changes without rework on the transformer pad.
- **Power/control circuit separation.** Cable routing must preserve separation per DBM (line 768) — coordinate tray/conduit layout with controls and instrumentation early to avoid retro-fits at tie-in time.
- **Local control station.** Although TXP-8500-1 is a passive transformer, downstream 600 V MCC motors require adjacent local control stations hard-wired by field construction (line 760). The CWP should pre-coordinate this with the MCC CWP.
- **Tie-in timing.** Tie-ins to existing or related facilities require joint planning, with timing established as the project progresses (line 127). Sequencing constraints between the 13.8 kV primary feed energization and 600 V MCC commissioning are TBD.

## Trade-offs

- **Outdoor pad vs electrical-building installation.** Source material confirms electrical-building UPS systems and outdoor pad-mount conventions but does not assign TXP-8500-1 to a specific location. The CWP must defer pad-vs-building scope until detailed design assigns the installation location; both options carry different construction sequencing and weather-protection constraints.
- **Modular vs stick-built tie-in.** The DBM emphasizes modular construction (`_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, line 233) but local control stations and home-run cabling remain stick-built field activity; the CWP should make this split explicit.

## Examples

- Local control stations adjacent to each motor served by the 600 V MCC, hard-wired back to the MCC starter circuit by the field construction contractor (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, line 760).
- Two-point ground-grid connection for the distribution transformer with separately sized copper ground conductors per CEC (DBM grounding paragraphs).

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CFL-031-03-001 | The DBM transformer reference (line 745) names "13.8 kV to 600V, 3 MVA" only; workbook row 33 names "13.8kV/600/347V" (including 347 V neutral phase). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, line 745 | Workbook Packages row 33 (package name) | Datasheet Identification; Spec REQ-031-03-01 | Treat workbook row 33 as authoritative for nameplate (3-phase 600/347 V wye); DBM line 745 is a shorthand reference. | TBD |
| CFL-031-03-002 | Installation-location authority is unassigned in accessible sources; DBM mentions electrical buildings housing UPS/distribution but does not assign TXP-8500-1. | DBM electrical-buildings paragraph | Workbook row 33 (no location field) | Datasheet Construction; Spec REQ-031-03-12 | Carry installation location as ASSUMPTION/TBD; resolve via detailed design package. | TBD |
