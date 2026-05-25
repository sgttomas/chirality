# Guidance: DEL-014-01 Scope of Work

## Purpose

This Scope of Work exists to give the EPC Integrator a bounded, source-traceable package integration basis for PKG-014 before the downstream package datasheet (DEL-014-02), construction work package (DEL-014-03), vendor package production (DEL-014-04), vendor document turnover (DEL-014-05), and EPC vendor package review and acceptance (DEL-014-06) proceed.

The source basis is intentionally narrow. Workbook row 16 establishes the package identity and interface flags; Gate 7 establishes the mandatory EPC anchor deliverable and the Package Vendor / EPC Integrator responsibility split; the DBM sources provide facility-level LV/lighting service context, the building exhaust-fan/heater control context, and the contactor-panel housing context. Package-specific contactor-panel design details remain `TBD` unless later source material provides them.

## Principles

- Preserve the source spelling `CONTACTOR PANELS - LIGHTING / EXHAUST FAN CONTACTOR PANELS - LOW VOLTAGE` in identity fields because it is the accepted workbook/Gate 7 package name.
- Treat the Scope of Work as an EPC integration document, not a vendor design document.
- Keep Package Vendor responsibilities (package engineering/design/equipment/vendor documentation) separate from EPC Integrator responsibilities (facility integration, interfaces, tie-ins, constructability, procurement/construction coordination).
- Include only source-supported package interfaces (the seven Gate 7 flagged categories).
- Use the DBM LV (600 V HRG), lighting/utility (120/208 V), and contactor-panel housing statements as facility context only; do not infer panel counts, lineup, enclosure ratings, or load schedules from them.
- Prefer `TBD` over inferred technical values where accessible sources do not provide package-specific detail.

## Considerations

The package title indicates contactor panels for lighting and exhaust-fan control at low voltage. The DBM identifies the 600 V LV system (HRG, 5A continuous) as serving motors, lighting transformers, building heaters, and UPS > 10 kVA; and the 120/208 V system as serving lighting, receptacles, heat trace, small motors, and UPS <= 10 kVA. DBM Deepcut further states that 208/120 V AC serves building exhaust fans and building heater blower fans, and that electrical buildings shall house 208/120 V contactor panels. This collectively supports describing the package as low-voltage lighting and exhaust-fan contactor panels integrated into the electrical-building lineup, fed from the LV/lighting-utility system.

It does not support deciding how many contactor panels are required, which lighting branches or exhaust fans they serve, what enclosure ratings apply, or what control wiring counts are needed. The Remote I/O note ("Remote I/O nodes may also support building exhaust fan and heater controls") is permissive, not prescriptive; control architecture for PKG-014 contactor panels is TBD pending vendor design.

The Gate 7 interface basis flags seven categories (Electrical Power, Grounding / Bonding, Area / Exterior Lighting, I&C / Control Cabling, Communications / Network, Maintenance Access, Structural / Foundations / Supports). These should drive the SOW boundary narrative and later construction coordination; they should not be expanded unless later accepted sources add them.

## Trade-offs

| Topic | Conservative treatment | Risk if overstated |
|---|---|---|
| Package function | Describe as low-voltage contactor panels for lighting and exhaust-fan control housed in the facility electrical building lineup; keep specific load assignments and panel counts `TBD`. | The SOW could allocate loads or define vendor lineup before vendor data is available. |
| EPC responsibility | State facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and acceptance review only. | EPC scope could absorb vendor package engineering or panel design. |
| Technical values | Use only source-supported values; mark all panel-specific design parameters `TBD`. | Unsupported values would propagate into datasheets, procurement, and construction. |
| Control architecture | Note Remote I/O exhaust-fan/heater control as a permissive DBM statement; do not commit PKG-014 to a specific control topology. | A premature commitment would constrain vendor solutions. |
| Source name | Preserve the long source-spelling package name with the literal `/` separators. | Normalizing the name could break register traceability. |

## Examples

- Acceptable SOW language: "PKG-014 is the workbook-defined Electrical package `CONTACTOR PANELS - LIGHTING / EXHAUST FAN CONTACTOR PANELS - LOW VOLTAGE`, WBS 02, tracking number `26020-02-30-005`; the Package Vendor owns package engineering/design/equipment and the EPC Integrator owns facility integration and interface coordination."
- Acceptable SOW language: "Package-specific contactor-panel counts, lineup, enclosure ratings, lighting branches, exhaust-fan loads, and control wiring counts are TBD pending vendor/source data."
- Avoid: "The EPC Integrator shall design the contactor panels." Gate 7 assigns package engineering and design to the Package Vendor.
- Avoid: "Each contactor panel shall be rated [specific amperage] and serve [specific exhaust fans]." No accessible source slice supports those values.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| HR-014-01-001 | Package-specific contactor-panel design values (counts, ratings, enclosure, lineup, branch assignments, control wiring counts) are not exposed in accessible sources. | Workbook Packages row 16 gives identity and interface flags only. | DBM Comp and Liquids and DBM Deepcut give only facility-level LV/lighting service context and a general contactor-panel housing statement. | Datasheet Conditions, Specification Requirements, Procedure Steps. | Treat DBM statements as facility context and keep package-specific technical values `TBD` pending vendor/source data. | TBD |
| HR-014-01-002 | The DBM Remote I/O note that "Remote I/O nodes may also support building exhaust fan and heater controls" is permissive, but PKG-014 control topology is not explicitly defined. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` Remote I/O note. | No accessible PKG-014-specific control architecture source. | Specification SOW-014-06; Datasheet Conditions row on building exhaust-fan control. | Carry the DBM note as context only; do not commit PKG-014 to Remote-I/O-mediated control until vendor design and EPC review confirm. | TBD |
