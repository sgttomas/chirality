# Specification: DEL-084-04 — Vendor Engineered Equipment Package (Fuel Gas Skid)

> Pass 1/2 draft. Requirements are derived from accessible DBM source slices. Where the source
> uses `TBC`/`TBD`, this specification preserves that disposition rather than inventing values.
> Inferred items are labeled `ASSUMPTION`. See `Guidance.md` Conflict Table for CONFLICT C-01
> (package-name vs. equipment-tag location).

## Scope

### In scope (this deliverable)
- Vendor-engineered, vendor-supplied, physically fabricated fuel-gas skid package and its
  vendor design basis and datasheet set, satisfying EPC Scope of Work items `SOW-0095` through
  `SOW-0098` and the EPC Package Datasheet (`DEL-084-02`).
- Skid mechanical equipment: low-pressure fuel-gas scrubber, low-pressure fuel-gas heater,
  fuel-gas regulators with sparing, local filtration, piping within battery limits, valves,
  instrumentation, controls, electrical, package building/enclosure (as applicable), and
  associated structural steel and skid base.
- Vendor engineering, design calculations, fabrication, factory acceptance testing,
  documentation, and turnover information feeding `DEL-084-05` (Vendor Document Turnover
  Package) and `DEL-084-06` (EPC Vendor Package Review and Acceptance). (ASSUMPTION:
  package-internal flow; not explicitly declared in `_DEPENDENCIES.md`.)

### Out of scope (for this deliverable)
- EPC Scope of Work authorship (`DEL-084-01`) and EPC Package Datasheet authorship
  (`DEL-084-02`).
- Construction Work Package (`DEL-084-03`).
- Installation, tie-in piping beyond the skid battery limit, foundations, area paving,
  cross-facility distribution, sales-gas splitter and emergency buyback regulator station
  (per 4-25 DBM "Emergency Buyback and Purge", these are installed in the sales gas
  splitter building, not on this skid; ASSUMPTION).
- Instrument-air supply (4-25 consolidated package per 4-25 DBM "Instrument Air"; 3-25
  has no local instrument-air compressor per SCA-006).
- Flare, drains, and emergency power equipment outside the skid battery limit.

## Requirements

> Each requirement cites its supporting source slice. Where the cited source itself
> labels the value `TBC`/`TBD`, the requirement is carried forward as such.

### R-FG-01 — Service and Sizing
- R-FG-01.1: The package shall deliver low-pressure fuel gas to plant users including
  TEG stripping, blanketing, purge, dilution/enrichment gas, building heaters,
  emergency-generator fuel, flare pilots/purge, and compressor purge/sweep gas.
  (Source: 4-25 DBM "Utilities Overview" / "Fuel Gas Basis"; 3-25 DBM "Fuel Gas".)
- R-FG-01.2: LP fuel-gas system normal total flow basis: 1.382 MMSCFD (39.13 e3m3/d);
  design flow: > 1.5 MMSCFD (> 42.5 e3m3/d), value `TBC` per source.
  (Source: 3-25 DBM "Fuel Gas".)
- R-FG-01.3: Emergency-generator fuel-gas design flow shall be 0.468 MMSCFD
  (13.2 e3m3/d), `TBC` in detailed engineering; start-gas flow shall be 3.6 MMSCFD for
  30 seconds, `TBC`. (Source: 4-25 DBM "Fuel Gas Equipment and Controls".)
- R-FG-01.4: Piping and vessels shall accommodate the simultaneous emergency-generator
  start-gas case and the design operating case, because generator testing may occur at
  design operating conditions. (Source: 4-25 DBM "Fuel Gas Equipment and Controls".)

### R-FG-02 — Pressure and Source
- R-FG-02.1: The package shall accept fuel gas at supply pressures consistent with the
  pipeline sources listed in `Datasheet.md` "Pressure/Flow Basis" (Enbridge normal
  5,171 kPag / max 5,516 kPag, MAWP 9,928 kPag; Alliance normal 5,516 kPag / max
  8,274 kPag, MAWP 9,928 kPag). (Source: 3-25 DBM "Fuel Gas".)
- R-FG-02.2: Buyback fuel-gas system MAOP estimate shall be 9,928 kPag; the vendor
  design shall verify final MAOP in detailed engineering. (Source: 4-25 DBM
  "Emergency Buyback and Purge".)
- R-FG-02.3: The emergency-generator fuel-gas supply pressure shall be less than 66 psig
  during normal operation to maintain general-purpose electrical classification
  compliance. (Source: 4-25 DBM "Fuel Gas Equipment and Controls".)

### R-FG-03 — Heater
- R-FG-03.1: The LP fuel-gas heater shall be an electric resistance heater controlled
  by SCR. (Source: 4-25 DBM "Fuel Gas Equipment and Controls".)
- R-FG-03.2: The heater shall be sized for maximum sales-compressor discharge pressure
  and winter ambient buyback gas conditions. Heater duty is `TBD`. (Source: same.)
- R-FG-03.3: The heater shall include a skin-temperature thermocouple override and a
  gas outlet temperature control to prevent overheating under stagnant-gas conditions.
  (Source: same.)

### R-FG-04 — Scrubber
- R-FG-04.1: The LP fuel-gas scrubber shall remove condensed liquids before
  distribution to all users. (Source: 4-25 DBM "Fuel Gas Equipment and Controls"; 3-25
  DBM "Fuel Gas".)
- R-FG-04.2: The scrubber shall be designed for fuel-gas system design flow at design
  operating pressure, using a maximum K factor of 0.35 Imperial with operating-pressure
  derating. (Source: 4-25 DBM "Fuel Gas Equipment and Controls"; consistent K = 0.35
  in 3-25 DBM "Fuel Gas" for V-3210-2.)
- R-FG-04.3: Condensed liquids shall route to the designated slop tank (`TK-9130-1`
  per 4-25 DBM; `TK-9130-2` per 3-25 DBM — the applicable destination depends on the
  final reconciliation in CONFLICT C-01).

### R-FG-05 — Regulators and Filtration
- R-FG-05.1: All fuel-gas regulators shall have at least one installed spare, with a
  minimum 2 x 100% regulator sparing philosophy. (Source: 4-25 DBM "Fuel Gas Equipment
  and Controls".)
- R-FG-05.2: Main fuel-gas regulators shall not be sized on the basis that a single
  regulator carries both full plant fuel-gas demand and emergency-generator start-gas
  demand after the parallel regulator has failed. (Source: same.)
- R-FG-05.3: Regulators shall be individually isolatable for maintenance and shall
  include an outlet pressure-test connection. Pilot-type regulators shall include
  individual pilot isolation where pilots are external. (Source: same.)
- R-FG-05.4: Start-gas regulators shall be quick-acting, internally sensing
  regulators; pilot-type regulators shall not be used for start-gas service. (Source: same.)
- R-FG-05.5: Bulk filtration is not normally required at the package inlet; user-side
  strainers are recommended for construction/start-up particulate. A local fuel-gas
  particulate filter shall be provided at the emergency generator supply. (Source:
  4-25 DBM "Fuel Gas Design Values".)

### R-FG-06 — Environmental and Site Basis
- R-FG-06.1: The package, package building (if any), control panels, instrumentation,
  and field devices shall be suitable for the design ambient envelope -40 deg C to
  +35 deg C unless a stricter package-specific basis is required. (Source: 3-25 DBM
  site basis.)
- R-FG-06.2: Winterization, electrical heat tracing, and building heating provisions
  shall be consistent with the site basis. (Source: 3-25 DBM site basis.)

### R-FG-07 — Materials and Hazard
- R-FG-07.1: Fuel-gas wetted materials shall be compatible with sweet/sour service per
  project material spec. `location TBD` — vendor shall confirm against project material
  governance.
- R-FG-07.2: Methyl-mercaptan toxicity and odour hazards relevant to purge, analyzer,
  and operations practices shall be reflected in package layout and venting design.
  A formal hazard review is required before finalizing purge and analyzer maintenance
  practices. (Source: 3-25 DBM "Fuel-Gas Sulphur and Purge Hazard Basis".)

### R-FG-08 — Documentation and Turnover
- R-FG-08.1: The vendor shall deliver a vendor package design basis and datasheet set
  consistent with the EPC Scope of Work and EPC Package Datasheet. (Source:
  `_CONTEXT.md` "Anticipated Artifacts"; ASSUMPTION on detailed scope, awaiting `.docx`
  heading 37 read.)
- R-FG-08.2: The vendor turnover information shall be sufficient to support
  `DEL-084-05` (Vendor Document Turnover Package) and `DEL-084-06` (EPC Vendor Package
  Review and Acceptance). (ASSUMPTION on inter-deliverable flow.)

## Standards

| Standard / Project Document | Applicable Area | Location |
|---|---|---|
| West Doe Project DBM — 03-25 Compressor Station and Liquids Hub | Site basis, fuel-gas system context | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` |
| West Doe Project DBM — 04-25 Deep Cut Gas Plant | Fuel-gas equipment and controls basis | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |
| `26020-Package_Requirements.docx` heading 37 | Package-specific EPC requirements | `_Sources/26020-Package_Requirements.docx` — `location TBD` (not parsed this run) |
| Sour-service / material governance | Wetted-part materials | `location TBD` |
| Project coating / painting specification | Skid coatings | `location TBD` |
| Project electrical area classification | Generator-supply pressure ceiling and enclosure rating | `location TBD` (see R-FG-02.3 for one DBM-anchored constraint) |
| Pressure-vessel and piping codes (ASSUMPTION: ASME B31.3, ASME Sec. VIII Div. 1) | Vessel/piping design | `location TBD` |

## Verification

| Req ID | Verification Approach |
|---|---|
| R-FG-01.* | Vendor flow/sizing calculations; review against DBM-cited values; FAT records |
| R-FG-02.* | Vendor pressure design and PSV calculations; design verification by EPC during `DEL-084-06` |
| R-FG-03.* | Heater design review (electric/SCR confirmation); FAT verification of skin-T override and outlet-T control; commissioning test of stagnant-gas behaviour |
| R-FG-04.* | Scrubber sizing review (K = 0.35 max with derating); drain routing walkdown; commissioning liquid-knockout check |
| R-FG-05.* | P&ID and isometric review confirming 2 x 100% regulator sparing and isolation/test connections; FAT of start-gas regulator response |
| R-FG-06.* | Cold-weather design review; building/heat-tracing/insulation walkdown |
| R-FG-07.* | Material certifications (MTRs); hazard-review record before final issue |
| R-FG-08.* | Document index review against EPC Scope of Work and Package Datasheet; turnover gate at `DEL-084-05` |

## Documentation

The vendor scope shall produce (at minimum) the following anticipated artifacts:

- Vendor package design basis document.
- Vendor equipment datasheet set covering heater, scrubber, regulators, instrumentation,
  electrical, controls, and skid structural items.
- Vendor P&IDs and process flow diagrams for the package.
- General arrangement, foundation loading, and structural drawings.
- Cause-and-effect / functional description for shutdown and control logic.
- Material test reports, weld records, NDE records, hydrotest records.
- Factory Acceptance Test plan and report.
- Manufacturer data report (MDR) and turnover document index for `DEL-084-05`.

Items not explicitly enumerated in accessible sources are `ASSUMPTION` based on
standard vendor-package convention and shall be confirmed against
`26020-Package_Requirements.docx` heading 37 once parsed.
