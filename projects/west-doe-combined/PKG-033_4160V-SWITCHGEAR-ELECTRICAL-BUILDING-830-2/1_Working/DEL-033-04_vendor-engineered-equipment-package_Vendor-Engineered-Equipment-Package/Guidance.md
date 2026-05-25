# Guidance: DEL-033-04_vendor-engineered-equipment-package

## Purpose

This guidance supports the Package Vendor production unit (engineering, design, fabrication/supply, and physical equipment) for the 4160V SWITCHGEAR ELECTRICAL BUILDING (830-2) package, `PKG-033`. The deliverable converts the accepted EPC Scope of Work and EPC Package Datasheet into a vendor-engineered 4160 V switchgear electrical building with a defendable design basis and supplied equipment. EPC integration review is performed downstream (`DEL-033-06`).

## Principles

- **Vendor inputs are EPC outputs.** Vendor design starts from `DEL-033-01` (Scope of Work) and `DEL-033-02` (Package Datasheet). The vendor shall not invent package scope outside those inputs.
- **Responsibility split is preserved.** Package engineering, design, vendor documentation, and physical equipment belong to the Package Vendor. Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration belong to the EPC Integrator.
- **Source-anchored values only.** Where accessible source slices (03-25 DBM electrical and civil sections, 04-25 DBM electrical-building practice, Gate 7 registers, workbook row 35) define a value or constraint, the vendor design shall reflect it. Where source is silent, values remain `TBD` for vendor data to close — not for invention by drafting.
- **Interfaces drive design, not the reverse.** All twelve interfaces listed in `INTERFACE_REGISTER.csv` for `PKG-033` are inputs to vendor engineering, not items the vendor may redefine.
- **Facility incoming-power scope stays facility.** The 13.8 kV utility supply, 13.8 kV main switchgear, and 13.8 kV-to-4.16 kV / 12 MVA step-down transformer are facility-scope; the vendor designs the 4160 V switchgear/building downstream of the building boundary.

## Considerations

- **Service basis.** The 03-25 DBM System Voltages table fixes 4,160 V, 3 phase, 3 wire, 60 Hz, LRG for the MV service supporting AC inverter-drive motors 250 hp-5,500 hp; the vendor design shall start there.
- **MCC functional features.** The 4160 V MCC must support field-fused contactors, motor protection relays, and an EtherNet link to the plant PLC central control panel. SCA-001 VE #34 / VE #37 effects (VFD starting for KM-2150/KM-2250; capacitor-bank removal where VFDs are present) are facility-level decisions the vendor shall accommodate but not redefine.
- **Building tag identity.** Workbook row 35 names the package "(830-2)". The 04-25 Buildings schedule lists "830-1 4.16kV Acid Gas / Overheads Compressor Electrical Building" but not an "830-2" tag. Treat "830-2" as the authoritative package identity from workbook row 35; the cross-facility tag relationship is for EPC integration to clarify.
- **Area classification and HVAC.** Electrical buildings shall be placed in general-purpose areas with HVAC/ventilation coordinated with classification and controls. n+1 HVAC sizing is 04-25 practice; applicability to 03-25 building "830-2" is for the EPC project specification to confirm.
- **Raceway and segregation.** Segregation of 13.8 kV / 4.16 kV / 600 V power from control/instrument circuits and the cable-tray/conduit/grounding/bonding basis follow project electrical specifications and detailed design.
- **Foundation and anchorage.** Electrical buildings require equipment-specific foundation/anchorage checks against geotechnical, equipment-load, snow/wind/seismic, frost, vibration, settlement, and maintenance-access criteria.

## Trade-offs

- **Modular prefabricated building vs. site-built building.** The 04-25 DBM uses prefabricated modular buildings; modular construction simplifies shop fabrication and shipping but constrains footprint and door-opening dimensions. Site-built construction relaxes those constraints but extends schedule and integration scope. Resolution depends on project electrical specifications and EPC integration.
- **Bottom cable entry vs. alternative entries.** Bottom-entry on piles is the 04-25 default; alternative entries may suit site-specific drainage or grading conditions for 830-2 but require coordination with the Grading / Site Drainage / Spill Containment and Structural / Foundations / Supports interfaces.
- **Vendor-scope HVAC vs. facility HVAC.** Building HVAC may be vendor-supplied within the package or coordinated as an EPC-supplied service through the Building HVAC / Services interface. The split affects scope, controls integration, and warranty boundaries.
- **Switchgear lineup configuration.** Single-lineup vs. multi-lineup arrangements affect footprint, maintenance access, arc-flash exposure, and ride-through during maintenance; selection follows facility studies and integration decisions, not drafting.

## Examples

- A vendor 4160 V switchgear electrical building production unit including the switchgear lineup, MCC equipment (with fused contactors, motor protection relays, and EtherNet to the plant PLC), distribution equipment, building HVAC/ventilation, internal cable tray, conduit, and grounding tie-ins — supplied with the design basis and datasheet set referenced by Gate 7 artifacts. (ASSUMPTION: representative configuration; actual configuration set by vendor data.)
- A vendor design basis documenting the twelve interface positions for `PKG-033` and the vendor's response to each at the building boundary.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CFL-033-04-001 | Workbook row 35 names the package "(830-2)" but the 04-25 Buildings schedule enumerates "830-1 4.16kV Acid Gas / Overheads Compressor Electrical Building" without an "830-2" tag, and the 03-25 DBM does not enumerate the "830-2" tag explicitly. | Workbook Packages row 35 (package name) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Buildings schedule | Datasheet identification / building tag basis; Specification REQ-033-04-013 | Treat "830-2" as the authoritative package identity from workbook row 35; cross-facility tag relationship to "830-1" is `TBD` and is for EPC integration to clarify. | TBD |
| CFL-033-04-002 | Switchgear bus rating, short-circuit rating, breaker count/frame size, arc-flash class, and building footprint are not defined for `PKG-033` in accessible sources. | Workbook Packages row 35 | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Electrical Buildings / 4160V MCC (general basis only) | Datasheet attributes; Specification REQ-033-04-013 | Record switchgear lineup, ratings, breaker schedule, arc-flash class, and footprint as `TBD` to be closed by vendor data; do not invent values. | TBD |
| CFL-033-04-003 | Installation plot location for building "830-2" is not assigned by accessible sources; the 03-25 DBM places electrical buildings in general-purpose areas without a plot assignment for `PKG-033`. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Area Classification; Electrical Buildings | Gate 7 registers (silent on `PKG-033` plot location) | Datasheet construction; Specification REQ-033-04-009; Guidance Considerations | Defer plot-location decision to EPC integration; vendor design accommodates a general-purpose-area location until resolved. | TBD |
| CFL-033-04-004 | HVAC sizing basis (n+1 per 04-25 DBM) is not explicitly carried by the 03-25 DBM for building "830-2". | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings (n+1 HVAC) | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Electrical Buildings (HVAC coordination only) | Datasheet attributes (Building HVAC basis); Specification REQ-033-04-009 | Carry n+1 HVAC as the proposed default with applicability `TBD`; confirm through project electrical specifications during EPC integration. | TBD |
