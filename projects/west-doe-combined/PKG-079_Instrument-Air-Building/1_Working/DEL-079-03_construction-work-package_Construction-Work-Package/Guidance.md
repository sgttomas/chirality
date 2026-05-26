# Guidance — DEL-079-03 Construction Work Package (Instrument Air Building)

> Directional guidance for producing and applying the Construction Work Package (CWP) for the PKG-079 Instrument Air Building package. Not normative — see Specification.md.

## Purpose

The CWP exists to bridge engineering and field execution for a vendor-supplied skid-mounted instrument air package whose engineering/design/equipment is owned by the Package Vendor and whose facility integration is owned by the EPC Integrator (per SCOPE_LEDGER SOW-0131). Because SOW-0134 places several physical interfaces — shipping, pile installation, tie-in piping, electrical connections, mounting platform, stairs — explicitly with "others," the CWP must enable those parties as much as it directs the EPC Integrator's own crews.

## Principles

1. **Treat the package as a delivered skid + interfaces.** The vendor delivers a functional unit; CWP value is concentrated at the interfaces. Source: SCOPE_LEDGER SOW-0131, SOW-0134.
2. **Design pressures define the test envelope.** The combination of PSV set (948 kPag), system design max (1034 kPag), minimum operating (551 kPag), and facility shutdown (482 kPag) determines tie-in piping pressure test selection and isolation boundaries. Source: SCOPE_LEDGER SOW-0133, SOW-0134.
3. **Dew point is the only delivered-air acceptance metric in source.** The -73.3 °C at 1000 kPag value is the package's air-quality contract; build commissioning around verifying it. Source: SCOPE_LEDGER SOW-0133.
4. **Non-classified motor area drives a simpler hazardous-area boundary statement.** Document the boundary explicitly so downstream operators can rely on it. Source: SCOPE_LEDGER SOW-0134.
5. **Plan around redundant compressor + redundant dryer towers.** The dryer is 2-tower regenerative (one operating, one regenerating), and the spec calls for two compressors. Sequence installation, commissioning, and turnover so that a single-train check is possible. Source: SCOPE_LEDGER SOW-0132, SOW-0133.

## Considerations

- **Interface ownership clarity.** The CWP should restate the "by others" list verbatim from SOW-0134 to prevent silent re-assignment of scope at the workface.
- **Pile/foundation coordination.** Pile installation is "by others"; CWP must obtain hold-down templates, grout schedule, and pile-cap elevation tolerances from the foundation party before equipment set. (ASSUMPTION — derived from typical pile-mounted skid installation.)
- **Tie-in piping isolation.** With facility shutdown at 482 kPag and minimum operating at 551 kPag, tie-in cut-ins likely require either a planned facility outage or a verified isolation valve pair with bleeder. (ASSUMPTION.)
- **Motor protection details.** Anti-condensation space heaters must be energized at delivery to prevent winding moisture in -40 °C ambient. (ASSUMPTION — derived from SOW-0134 design temperature.)
- **VFD vs soft starter selection.** Source states "soft starter or VFD ready"; CWP planning should not assume one over the other without confirming the engineered package selection. (Source: SOW-0133.)
- **Mounting platform and stairs.** Although "by others," the CWP should confirm platform/stair geometry accommodates filter change-out, dryer service, and PSV access without scaffolding. (ASSUMPTION.)
- **Receiver sizing.** Wet receiver and after-filter sizing are "by vendor" in SOW-0133, so the CWP cannot pre-fix tie-in elevations until vendor general arrangement is issued. Plan a hold point.
- **Dry receiver option.** SOW-0132 allows "one dry air receiver (or two 50% capacity receivers)." CWP installation sequence must remain valid under either configuration.

## Trade-offs

| Trade-off | Discussion | Source |
|---|---|---|
| Hot tap vs planned outage for tie-in | Hot tap preserves uptime but adds risk and procedural overhead; planned outage simplifies test boundaries but consumes a facility window. | ASSUMPTION |
| Single vs phased turnover | Whole-package turnover after both trains tested is cleaner; phased turnover (one compressor + one dryer tower) accelerates partial use but complicates acceptance records. | ASSUMPTION |
| Witness vs hold for dew point test | A hold guarantees presence; a witness with notification may be acceptable for non-critical timing. | ASSUMPTION |

## Examples

No worked examples are available from accessible sources. `TBD` — to be added once project-specific construction sequencing examples are issued.

## Conflict Table (for human ruling)

No conflicts identified between accessible source slices and the drafted four-document set in this pass.

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority | Human ruling |
|---|---|---|---|---|---|---|
| (none) | — | — | — | — | — | — |
