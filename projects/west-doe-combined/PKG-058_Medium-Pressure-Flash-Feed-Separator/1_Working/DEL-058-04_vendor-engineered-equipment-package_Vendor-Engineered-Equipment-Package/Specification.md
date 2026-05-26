# Specification — DEL-058-04 Vendor Engineered Equipment Package (Medium Pressure Flash Feed Separator)

## Scope

This specification governs the Package Vendor production unit for engineering, design, fabrication/supply, and physical delivery of the Medium Pressure Flash Feed (MPFF) Separator package (vessels V-7110-1 and V-7310-1; heater bundle E-7120-1 and parallel if retained; associated modules 710-1 and 730-1; building enclosure; instrumentation; internals) developed from the EPC Scope of Work (`DEL-058-01`) and the EPC Package Datasheet (`DEL-058-02`).

Includes:
- Vendor engineering and design of vessels, heater bundle (if retained), internals (Mistex), building, instrumentation, and shipped-loose items.
- Fabrication, supply, and delivery of the physical equipment package.
- Vendor design basis and vendor datasheet set.

Excludes (per `_CONTEXT.md`, decomposition, and DBM):
- Construction Work Package (covered by `DEL-058-03`).
- Vendor Document Turnover (covered by `DEL-058-05`).
- EPC review/acceptance (covered by `DEL-058-06`).
- Unit-specific process descriptions, equipment datasheets prepared by the EPC, pressure-relief calculations, instrumentation design, electrical design, civil layout — these are not displaced by vendor package design (DBM-Deepcut, "This section does not replace...").

## Requirements

### R1. Source-anchored interface to EPC inputs
- R1.1 The vendor package shall be developed from the EPC Scope of Work (`DEL-058-01`) and Package Datasheet (`DEL-058-02`). [Source: `_CONTEXT.md`; decomposition row 71]
- R1.2 Where a unit-specific section or vendor requirement provides a stricter requirement, the stricter or more specific requirement shall govern. [Source: DBM-Deepcut `4-25_Deepcut_DBM.md`]

### R2. Process design envelope
- R2.1 Each MPFF separator shall be sized for a design pressure of 1724 kPag. [Source: DBM-Deepcut MPFF Operating and Capacity Basis]
- R2.2 Each MPFF separator shall provide a minimum of 10 minutes of liquid residence time between the weir height and NLL-interface. [Source: DBM-Deepcut MPFF feed conditions]
- R2.3 Internals shall be Mistex type; no internal coating is specified. [Source: DBM-Deepcut MPFF feed conditions]
- R2.4 The package shall accommodate MPFF overhead vapour pressure-regulated to SOC third-stage suction. [Source: DBM-Deepcut MPFF feed conditions]
- R2.5 Provision shall be made for LP fuel gas purge regulated to maintain MPFF pressure above the downstream stabilizer flash/feed separator and to enable sour-gas sweeping during maintenance. [Source: DBM-Deepcut MPFF feed conditions]
- R2.6 An automated blowdown valve shall be provided. [Source: DBM-Deepcut MPFF feed conditions]
- R2.7 Methanol injection capability shall be provided upstream of the MPFF inlet level/pressure control valve as a hydrate-suppression safeguard, pending confirmation of upstream HEX outlet temperatures. [Source: DBM-Deepcut MPFF feed conditions]
- R2.8 ASSUMPTION: Design operating temperature of 40 deg C is assumed pending detailed engineering confirmation (TBC). [Source: DBM-Deepcut MPFF feed conditions]
- R2.9 MPFF inlet temperatures, low/expected-high operating pressures, and per-separator flow values are TBD in the source basis. The vendor shall reserve nozzle/sizing margin to absorb resolution of these TBDs during detailed engineering. [Source: DBM-Deepcut MPFF Operating and Capacity Basis]

### R3. Sparing and isolation
- R3.1 Sparing basis is 2 x 100% normal; there is no sparing for the off-design line-pack maximum-flow scenario. [Source: DBM-Deepcut MPFF and Stabilizer Train Relationship; Sparing table]
- R3.2 Each MPFF package shall be isolatable on a unit basis so it may be removed from service while the other train continues to operate. [Source: DBM-Deepcut parallel-package isolation paragraph]

### R4. Heater bundle (conditional)
- R4.1 If the MPFF hydrocarbon liquid heater bundle is retained, it shall be a U-bundle/BKU-type arrangement with heat medium on the tube side. [Source: DBM-Deepcut MPFF feed conditions]
- R4.2 Original sizing basis (retained for nozzle reservation): maintain 140 deg F in the MPFF and 87 deg F at 50 psig in the downstream LP flash feed, with 10% excess surface area for the line-pack scenario. [Source: DBM-Deepcut MPFF feed conditions]
- R4.3 350 deg F heat-medium supply basis, tube-sheet seal-weld requirements, and bundle retention/de-rating/removal are TBC after thermal re-simulation. Vessel nozzle provisions shall be preserved until disposition is confirmed. [Source: DBM-Deepcut MPFF feed conditions]

### R5. Site basis
- R5.1 Equipment, package buildings, control panels, instrumentation, and field devices shall be suitable for -40 deg C minimum ambient unless a more severe process or vendor condition applies. [Source: DBM-Comp_and_Liquids `3-25_Comp_and_Liquids_DBM.md` site basis]
- R5.2 Equipment metallurgy where affected by low temperature shall comply with the site minimum ambient basis. [Source: DBM-Comp_and_Liquids site basis]

### R6. Building enclosure
- R6.1 The MPFF package shall be configured similarly to the inlet separator, with a self-framing building enclosing instrumentation and one end of the vessel. [Source: DBM-Deepcut MPFF feed conditions]

### R7. Mechanical packaging discipline
- R7.1 Mechanical packages shall be organized to preserve clear scope boundaries among process vendors, electrical/controls systems, field construction, and cross-facility utility interfaces. [Source: DBM-Comp_and_Liquids]
- R7.2 Vendor deliverables associated with the package shall include datasheets, cause-and-effect inputs, utility load summaries, relief/load data, field tie-in lists, operating and design envelopes, sparing philosophy, materials and coating basis, maintenance access, shipped-loose item lists, and vendor document registers. [Source: DBM-Comp_and_Liquids]

### R8. Objective alignment (context, not stand-alone requirement)
- R8.1 The vendor package supports objectives `OBJ-001`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` via package-grouping heuristic (ASSUMPTION). [Source: `_CONTEXT.md`; GATE-07 OBJECTIVE_DELIVERABLE_MAP]

## Standards

- Site standards and applicable codes — location TBD (the deliverable `_REFERENCES.md` does not list specific governing standard editions for this vessel package). The DBM references `ISO 13631 / API SPEC 11P, 1st Edition` for packaged reciprocating gas compressors (not applicable to MPFF separators), so no MPFF-specific code citation is asserted here. [Source: DBM-Deepcut standards table]
- All standards referenced by the EPC Package Datasheet (`DEL-058-02`) flow down to this specification (location TBD until `DEL-058-02` is published).

## Verification

| Requirement | Verification approach |
|---|---|
| R2.1 design pressure | Design review against DBM value; ASME-stamp / equivalent pressure-vessel certification per vendor jurisdiction (location TBD) |
| R2.2 residence time | Vessel sizing calculation; geometry check against weir-to-NLL-interface metric |
| R2.3 internals Mistex | Mechanical internals datasheet review |
| R2.4 / R2.5 overhead and purge tie-ins | P&ID review against SOC third-stage suction and LP fuel-gas tie-in; nozzle list confirmation |
| R2.6 automated blowdown | Cause-and-effect review; FAT of automated blowdown valve and trip logic |
| R2.7 methanol injection | P&ID and nozzle review; injection-point geometry check |
| R2.8 / R2.9 TBD parameters | Open-item register; nozzle/sizing margin documented; tracked through EPC review (`DEL-058-06`) |
| R3 sparing/isolation | Layout/P&ID isolation philosophy review |
| R4 heater bundle | Conditional: thermal re-simulation outcome documented; if retained, BKU mechanical certification and tube-sheet seal-weld inspection records |
| R5 site basis | Materials and rating certificates demonstrating -40 deg C suitability; vendor low-temperature impact testing records |
| R6 building | Building drawings/structural review |
| R7 packaging discipline | Vendor document register review during EPC acceptance (`DEL-058-06`) |

Final verification and integration sign-off is performed by `DEL-058-06_epc-vendor-package-review-and-acceptance` and is not in scope of this deliverable.

## Documentation

Anticipated artifacts (from `_CONTEXT.md`):
- Vendor engineered physical equipment package (the physical equipment itself, plus packaged subassemblies)
- Vendor package design basis and datasheet set

Required vendor documentation set (from DBM-Comp_and_Liquids mechanical packaging discipline):
- Datasheets
- Cause-and-effect inputs
- Utility load summaries
- Relief/load data
- Field tie-in lists
- Operating and design envelopes
- Sparing philosophy
- Materials and coating basis
- Maintenance access drawings
- Shipped-loose item lists
- Vendor document register (cross-listed under `DEL-058-05` for turnover)
