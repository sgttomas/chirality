# Guidance: DEL-020-02_package-datasheet

## Purpose

The Package Datasheet exists to convert the accepted Gate 7 package basis for `PKG-020` into a source-supported technical handoff document for the 13.8 kV switchgear that serves as the plant main power distribution center. It should give the Package Vendor a clear EPC integration basis while keeping facility-level interfaces distinct from vendor-owned switchgear design.

## Principles

- Preserve source spelling and identity. The package name is carried as "13.8kV SWITCHGEAR EQUIPMENT" because that is the workbook and Gate 7 register spelling.
- Treat workbook interface `X` facts as evidence under the Package Datasheet, not as separate deliverables.
- Keep vendor-owned switchgear design (breaker count, ratings, lineup, internal protection scheme, arc-flash mitigation) with the Package Vendor; keep facility-level integration (utility tie-in, downstream feeders, grounding to the plant grid, building housing, control-power UPS interface, I&C and network cabling) with the EPC Integrator.
- Use `TBD` for breaker count and ratings, bus ampacity, short-circuit/withstand rating, metering scheme, relaying/protection coordination, and arc-flash mitigation until ELC-QAS-000007-001 text or vendor data is accepted.
- Anchor system-level statements (utility supply, system voltages, radial distribution to electrical buildings, grounding basis, standby-power policy, cable specifications, housing) directly in the DBM electrical basis slices.

## Considerations

The DBM electrical basis treats the 13.8 kV switchgear as the plant main power distribution center. It is fed from a 25 kV to 13.8 kV, 50 MVA utility-supplied transformer and steps facility power down through a defined set of radial feeders to named downstream electrical buildings. The bus shall be sized for the full facility scope, which means the datasheet should make the facility-wide load and downstream feeder list visible to the vendor even though the numeric bus ampacity is `TBD`.

Standby-power policy is materially different from earlier project versions. The current basis places standby generation at the 600 V MCC level with transfer switches, and explicitly replaces the prior centralized 13.8 kV / 3 MW emergency-generator concept for both 04-25 and 03-25. The datasheet should make sure the vendor does not design the 13.8 kV switchgear around a non-existent centralized 13.8 kV emergency generator.

Grounding is a defined facility-level interface. The utility transformer is grounded via a 200 A, 10 s neutral grounding resistor and operates as a tripping system; the plant grounding system uses driven piles with a #2/0 green insulated main conductor and two-point grounding at major equipment. The datasheet should require the switchgear to be integrated into this grounding scheme without overstating package-specific conductor sizing.

Control power for medium-voltage breaker control circuits and protective relays comes from 120 VAC / 125 VDC UPS systems. This is an explicit interface to the UPS package(s) and should be carried as such.

Housing is in a prefabricated electrical building (810-1) located in a general-purpose area, with n+1 HVAC and bottom cable entry. The datasheet should communicate the building basis but should not specify internal arrangement that is the building/vendor's design responsibility.

The 03-25 facility is sub-fed from the 04-25 13.8 kV Main Switchgear Electrical Building. This is the only explicit cross-facility tie at 13.8 kV; the datasheet should carry it as an interface, not as a separate deliverable.

## Trade-offs

| Topic | Conservative position | Reason |
|---|---|---|
| Breaker count, ratings, lineup | Mark `TBD` and defer to ELC-QAS-000007-001 and vendor data. | DBM does not enumerate per-feeder breaker configuration; project spec is the authority. |
| Bus ampacity / short-circuit rating | Mark `TBD`; carry the "sized for full facility scope" qualitative requirement. | DBM states sizing intent but does not give a numeric value; load study is detailed engineering. |
| Standby generator at 13.8 kV | Explicitly excluded; do not design around it. | DBM explicitly replaced this concept with LV standby generation. |
| Metering/protection coordination | Mark `TBD`; carry the requirement that boundary metering and coordination studies be confirmed during detailed engineering. | DBM defers these to detailed engineering. |
| Arc-flash mitigation | Mark `TBD`; require compliance with project specs. | No package-specific arc-flash basis is stated in accessible sources. |
| 25 kV utility voltage | Carry as "25 kV (TBC)" per DBM. | DBM marks the incoming utility voltage as to-be-confirmed. |

## Examples

- Acceptable datasheet entry: "Bus electrical basis: 13.8 kV, 3 phase, 3 wire, 60 Hz, low-resistance grounded. Source: DBM-Deepcut SEC-12 System Voltages."
- Acceptable source-gap entry: "Bus continuous ampacity: TBD pending facility load study and ELC-QAS-000007-001 detailed selection."
- Not acceptable without new source: "13.8 kV switchgear interrupting rating shall be 40 kA at 13.8 kV." The accessible source set does not establish this value.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-020-02-001 | DBM Power System states the incoming utility voltage is "25 kV (TBC)", but the equipment list and other paragraphs assume a fixed 25 kV/13.8 kV utility transformer. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Power System (line 2917) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, modular building / utility transformer references | Datasheet Attributes (Incoming source); Specification Requirements REQ-020-02-004 | Carry incoming utility voltage as "25 kV (TBC)" until BC Hydro confirmation; do not assert a fixed value. | TBD |
| HRR-020-02-002 | The accessible source set does not contain a PKG-020-specific match in `26020-Package_Requirements.docx`; detailed switchgear configuration (breakers, ratings, metering, relaying, arc-flash) is therefore unsupported at the package level. | `_REFERENCES.md`; `_Sources/26020-Package_Requirements.docx` (no PKG-020 match confirmed) | DBM-Deepcut SEC-12 Table 12-1 (line 2880, ELC-QAS-000007-001 Medium Voltage Switchgear) | Datasheet Construction; Specification REQ-020-02-014 | Defer detailed switchgear configuration to ELC-QAS-000007-001 and vendor package data; keep `TBD` in the datasheet. | TBD |
| HRR-020-02-003 | Standby-power policy was revised: the prior centralized 13.8 kV / 3 MW emergency-generator concept has been replaced by LV-MCC standby generation with transfer switches. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Standby Power (line 2943); `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (lines 505, 762) | Historical/legacy 13.8 kV emergency-generator concept implied by older project narrative | Datasheet Attributes (Standby/emergency role); Specification REQ-020-02-008 | Datasheet shall not include centralized 13.8 kV emergency-generator provisions; defer to LV standby package(s). | TBD |
