# Guidance: DEL-035-02_package-datasheet

## Purpose

The Package Datasheet exists to convert the accepted Gate 7 package basis for `PKG-035` into a source-supported technical handoff document. It should let the Package Vendor understand the EPC integration basis for the 13.8kV SWITCHGEAR ELECTRICAL BUILDING (810-1) — the plant main power distribution center — while keeping EPC-owned facility interfaces distinct from vendor-owned package design.

## Principles

- Preserve source spelling and identity. The package name is carried as "13.8kV SWITCHGEAR ELECTRICAL BUILDING (810-1)" because that is the workbook and Gate 7 register spelling.
- Treat workbook interface `X` facts as evidence under the Package Datasheet, not as separate deliverables.
- Keep vendor-owned design work (switchgear lineup, building, internal equipment) with the Package Vendor and facility-level integration with the EPC Integrator.
- Use the DBM electrical basis at the level it supports: voltage class, grounding system, building construction, downstream distribution targets, cable specification, area classification, and HVAC redundancy.
- Use `TBD` for switchgear bus ampacity, short-circuit ratings, breaker count/ratings, protective relaying, arc-flash energy results, plot-plan location, and final in-building equipment population until detailed studies or vendor data resolve them.

## Considerations

The DBM identifies the 13.8 kV switchgear as the plant main power distribution center, fed from a 25 kV to 13.8 kV, 50 MVA utility-supplied transformer, with the bus sized for the full facility scope. The 810-1 building is identified in the DBM building/module list as shop-fabricated. These two facts anchor the datasheet identity and function without overreaching into vendor-owned ratings.

Downstream distribution targets (6.9 kV inlet/sales compressor, 4.16 kV acid gas/overheads, 600 V acid gas, 600 V sales/overheads, and 4.16 kV/600 V general area/tank farm/process electrical buildings) are explicit in the DBM and should be carried verbatim so the vendor understands the radial-feed scope.

The DBM Electrical Buildings slice gives substantial building-construction basis: prefabricated/modular, general-purpose area, n+1 HVAC, elevated on piles, bottom cable entry, TECK/ACIC wiring, EMT conduit between adjacent equipment, removable equipment-door transoms. These are usable as datasheet basis without further interpretation. Detailed dimensions and HVAC sizing remain `TBD`.

Grounding and bonding are applicable interface topics. The DBM facility basis (two-point grounding for major equipment, pile-electrode network with #2/0 main conductor, ground wells at electrical buildings) is directly applicable to this package. Conductor sizes specific to the switchgear and detailed bonding routing remain detailed-design items.

The standby power story has changed since earlier project iterations: the prior centralized 13.8 kV emergency generator has been eliminated in favor of low-voltage TOU standby generators at the 600 V MCC level. The datasheet should record this so the vendor does not provision a 13.8 kV emergency-generator interface that is no longer in scope.

The package-specific Word requirements source did not produce a PKG-035 detailed-requirements match accessible during this run; therefore, vendor-facing detailed switchgear and arc-flash content should remain conservative until those source slices are resolved.

## Trade-offs

| Topic | Conservative position | Reason |
|---|---|---|
| Bus ampacity / short-circuit rating | Mark `TBD`. Carry only the qualitative "sized for the full facility scope" statement. | DBM does not state numeric values; values depend on facility load-flow and short-circuit studies (DBM lines 2900-2902). |
| Protective relaying / arc-flash | Mark `TBD`. Note that relay coordination and arc-flash energy study are required. | DBM identifies study need but does not give settings or hazard boundaries. |
| 810-1 plot-plan location | Mark `TBD`; state DBM places electrical buildings in general purpose areas. | DBM does not pin 810-1 to a specific coordinate. |
| In-building equipment population | Carry DBM list of "may house" equipment; mark final list as detailed-design `TBD`. | DBM says equipment is included "as required by detailed design" (line 2973). |
| Standby power interface | Record TOU LV standby generators at 600 V MCC with transfer switches; explicitly note 13.8 kV emergency-generator concept eliminated. | DBM Standby Power slice (line 2943) is unambiguous. |
| Cross-facility distribution to 03-25 | Carry the sub-feed fact; do not invent the metering or boundary protection. | DBM (line 2927) and 3-25 DBM (line 740) describe sub-feed but leave metering/protection split TBD. |

## Examples

- Acceptable datasheet entry: "Bus: 13.8 kV, 3 phase, 3 wire, 60 Hz, low-resistance grounded, sized for the full facility scope. Source: DBM Power System and System Voltages table."
- Acceptable source-gap entry: "Switchgear short-circuit withstand rating: TBD. Depends on facility short-circuit study."
- Acceptable interface entry: "Building HVAC: n+1, sized to tolerate failure of one unit. Source: DBM Electrical Buildings."
- Not acceptable without new source: "13.8 kV bus rated 3000 A, 50 kA, with 12 outgoing breakers and a 25 ms arc-flash incident energy of 8 cal/cm^2." The accessible source set does not establish these values.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-035-02-001 | The DBM Power System describes a single "13.8 kV switchgear" as the plant main power distribution center, while the 03-25 DBM refers to a "04-25 13.8 kV Main Switchgear Electrical Building" as the source of the 03-25 sub-feed. Whether the PKG-035 810-1 building is the same physical asset as the "04-25 Main Switchgear Electrical Building" is not stated explicitly. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Power System (lines 2917-2925, 2927) | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, line 740 | Datasheet Attributes (cross-facility distribution); Specification REQ-035-02-006 | Treat PKG-035 / 810-1 as the plant main 13.8 kV switchgear that also sub-feeds 03-25; await confirmation. | TBD |
| HRR-035-02-002 | Numeric switchgear ratings (bus ampacity, short-circuit, breaker count, arc-flash results) and 810-1 plot-plan location are not present in any accessible source slice for this package. | Workbook Packages row 37 | `_Sources/26020-Package_Requirements.docx` (no accessible PKG-035 detailed-requirements match) | Datasheet Construction; Specification REQ-035-02-012 | Keep numeric ratings and location `TBD` until detailed engineering studies and package-specific requirements are accepted. | TBD |
