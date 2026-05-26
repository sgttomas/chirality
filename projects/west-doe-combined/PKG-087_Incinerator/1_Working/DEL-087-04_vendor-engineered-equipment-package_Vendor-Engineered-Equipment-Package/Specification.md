# Specification — Vendor Engineered Equipment Package (DEL-087-04)

> Normative requirements for the Package Vendor production unit that engineers, designs, and supplies the PKG-087 Incinerator equipment package.

## Scope

### Includes

This specification governs the **Package Vendor** scope for PKG-087 Incinerator:

- Package engineering for the incinerator system (knockout drum, transfer pump, low pressure flare stack, blower, ancillaries, controls). [`PACKAGE_REGISTER.csv` ScopeNotes; `PACKAGE_REGISTER.csv` Description]
- Package design (process, mechanical, instrumentation/controls integral to the package, package electrical to the vendor terminal points, package structural elements integral to the skid/assembly). [`PACKAGE_REGISTER.csv` Description; `OBJECTIVE_REGISTER.csv` OBJ-004]
- Fabrication / supply of the physical equipment package. [`PACKAGE_REGISTER.csv` Description]
- Vendor documentation set required by the EPC Package Datasheet and source vendor-document tables. [`OBJECTIVE_REGISTER.csv` OBJ-010; `DELIVERABLE_REGISTER.csv` DEL-087-05]
- Compliance with the EPC Scope of Work (DEL-087-01) and Package Datasheet (DEL-087-02) interface and design requirements. [`DELIVERABLE_REGISTER.csv` DEL-087-01, DEL-087-02; `_CONTEXT.md` Scope]

### Excludes

- Integration of the package into the wider facility (interfaces, tie-ins, constructability, procurement / construction coordination) — owned by EPC Integrator. [`PACKAGE_REGISTER.csv` Description; `OBJECTIVE_REGISTER.csv` OBJ-004]
- Construction work package and tie-in execution — covered by DEL-087-03. [`DELIVERABLE_REGISTER.csv` DEL-087-03]
- Vendor document turnover register and submittals tracking — covered by DEL-087-05 (vendor produces the documents; turnover record is a separate deliverable). [`DELIVERABLE_REGISTER.csv` DEL-087-05]
- EPC vendor package review and acceptance — covered by DEL-087-06. [`DELIVERABLE_REGISTER.csv` DEL-087-06]
- Civil, structural, electrical infrastructure, controls infrastructure, utility tie-ins, and fire & gas detection design **outside** the package skid — owned by EPC Integrator. [`OBJECTIVE_REGISTER.csv` OBJ-005, OBJ-006, OBJ-007, OBJ-008]
- Package-specific exclusions stated in source materials: TBD (none stated). [`PACKAGE_REGISTER.csv` Exclusions]

## Requirements

### R1 — Package Constituents

R1.1 The Package Vendor SHALL provide the following equipment as a single coordinated package: one (1) incinerator knockout drum `V-6900-1`; one (1) incinerator knockout drum transfer pump `P-6900-1`; one (1) incinerator low pressure flare stack `FL-6920-1`; one (1) incinerator blower `B-6920-1`; and the self-framing building to be erected at site. [`26020-Package_Requirements.docx` package heading 40 (Major Included Equipment, slice 510-515); `PACKAGE_REGISTER.csv` ScopeNotes]

R1.2 The package SHALL meet the source-stated equipment data, including (at minimum):
- `V-6900-1`: 2,896 mm (114") ID x 9,144 mm (30') S/S; design pressure 345 kPag; design temperature -45.5 deg C / 260 deg C; corrosion allowance 1.59 mm;
- `P-6900-1`: vertical inline centrifugal, 70 USGPM, 5 hp, 575V/3Ph/60Hz motor, Class I Div 2;
- `FL-6920-1`: NPS 6 x 54,861 mm (180') tall; sized for max relief rate from tank farm and VRU;
- `B-6920-1`: ARR-4 discharge, TEFC 405T frame, 74 kW (100 hp), 575V/3Ph/60Hz, 1800 rpm, Type VJ Class II.
[`26020-Package_Requirements.docx` package heading 40 (Major Included Equipment, slice 510-515)]

R1.3 Final equipment tag numbers, where they differ from the source-stated tags, SHALL conform to the tags issued by the EPC Scope of Work (DEL-087-01) and Package Datasheet (DEL-087-02). [ASSUMPTION — derived from the EPC handoff model in `OBJECTIVE_REGISTER.csv` OBJ-004 and the deliverable chain in `DELIVERABLE_REGISTER.csv`]

### R2 — Process Function

R2.1 The package SHALL destruct vent streams routed to the incinerator header, including (at minimum) vapours from the spent caustic storage tank and the C5+ caustic treating overhead/dilution/enrichment-gas interfaces. [`_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 400, 402]

R2.2 The package SHALL accommodate the shared-interface allocation between 03-25 and 04-25. The exact 03-25 / 04-25 service split is an open interface item and SHALL be reconciled with the EPC Integrator via the Package Datasheet (DEL-087-02) prior to package design freeze. [`_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 56, 547]

R2.3 The package design throughput SHALL satisfy the caustic-oxidation demand of 214 SCFM (TBC) plus any additional shared-interface loads confirmed by the EPC Integrator, and the incinerator stack `FL-6920-1` SHALL be sized for the maximum relief rate from the tank farm and the VRU. [`_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 477; `26020-Package_Requirements.docx` package heading 40 (Major Included Equipment, slice 510-515)]

### R3 — Materials, Mechanical, and Environmental

R3.1 Aluminum SHALL NOT be used in caustic-wetted service or in the caustic building. [`_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 402]

R3.2 The package SHALL be designed for facility ambient design conditions including -40 deg C winter operation; winterisation provisions SHALL be vendor-engineered. [`_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 696]

R3.3 Caustic drain interface from the package (where applicable) SHALL terminate consistent with the facility caustic drain basis: minimum drain-header rating 300# ANSI, maximum drain temperature 121 deg C / 250 deg F (TBC), pressure segregation reviewed in HAZOP. [`_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 493]

R3.4 The spent-caustic vent path to the incinerator header SHALL preserve the flame-arrestor configuration defined in the facility basis. [`_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 402]

### R4 — Interfaces

R4.1 The package SHALL present clearly defined terminal points for each applicable facility interface category. Each interface type below is applicable per the GATE-07 register and SHALL appear in the vendor interface schedule:

- Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports.

[`INTERFACE_REGISTER.csv` (PKG-087 rows IFC-3FF4A46502 through IFC-23A65D01E5)]

R4.2 The Package Vendor SHALL provide loads, anchorage details, lift points, and access requirements sufficient for the EPC Integrator to design foundations, supports, electrical infeed, and maintenance access. [ASSUMPTION — division of responsibility per `OBJECTIVE_REGISTER.csv` OBJ-004 / OBJ-008]

### R5 — Controls, Instrumentation, and Safety

R5.1 Package-integral controls SHALL provide signals, alarms, and shutdowns suitable for integration into the EPC controls topology defined under OBJ-006 (final cause-and-effect and shutdown interfaces issued by the EPC Integrator). [`OBJECTIVE_REGISTER.csv` OBJ-006]

R5.2 The package SHALL accommodate fire & gas detection at the package boundary (LEL, H2S, methyl mercaptan, and fire detection devices) consistent with facility process hazards and detection coverage; detector quantity, tag list, set points, voting logic, placement, and calibration are TBD pending detailed design and safety studies. [`_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 838]

### R6 — Sour Service, Safety, Emissions

R6.1 The package SHALL be designed consistent with facility sour-service, relief, flare, blowdown, drain/containment, fire/gas, shutdown, environmental, emissions, and regulatory requirements as carried by OBJ-009. [`OBJECTIVE_REGISTER.csv` OBJ-009]

R6.2 Final emissions/permit values, incinerator service split, and flare relief / blowdown loads SHALL be confirmed with the EPC Integrator before the package design is frozen for permit-final emissions tables. [`_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 555]

### R7 — Operability, Maintainability, Turnover

R7.1 The package SHALL include operability, maintainability, sparing, isolation, and winterization features adequate for the facility handoff under OBJ-010. [`OBJECTIVE_REGISTER.csv` OBJ-010]

R7.2 The Package Vendor SHALL produce the vendor documentation set required for turnover via DEL-087-05; the EPC vendor package review and acceptance (DEL-087-06) is the acceptance gate. [`DELIVERABLE_REGISTER.csv` DEL-087-05, DEL-087-06]

## Standards

| Standard / Code Category | Status | Source |
|---|---|---|
| Sour-service / safety / relief / flare / blowdown / drain / containment / fire & gas / shutdown / environmental / emissions / regulatory codes | Applicable as carried by OBJ-009; specific governing standards list is not stated explicitly in the locally accessible source slice (`26020-Package_Requirements.docx` package heading 40, slice 510-521 contains Basic Scope and Major Included Equipment only; broader standards lists in the same source remain location TBD) | `OBJECTIVE_REGISTER.csv` OBJ-009; `_REFERENCES.md`; `26020-Package_Requirements.docx` package heading 40 |
| Pressure piping / vessel codes (e.g. ASME B31.3, ASME VIII for the knockout drum) | ASSUMPTION (typical for sour-service vent/oxidiser packages); the locally accessible slice cites equipment design pressure / temperature / corrosion allowance but does not name a vessel code | ASSUMPTION; `26020-Package_Requirements.docx` package heading 40 (Major Included Equipment) |
| Drain-header rating | 300# ANSI minimum | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 493 |
| Caustic-service material constraints | Aluminum prohibited in caustic service / caustic building | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 402 |
| Site environmental basis | -40 deg C ambient design | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 696 |
| Vendor documentation list | Per `26020-Package_Requirements.docx` vendor document tables (location TBD; slice not locally accessible) | `_REFERENCES.md`; `OBJECTIVE_REGISTER.csv` OBJ-010 |

## Verification

| Requirement | Verification Approach |
|---|---|
| R1 — Package constituents | Inspection of vendor equipment list vs. EPC Scope of Work (DEL-087-01) / Package Datasheet (DEL-087-02) tagged equipment list. |
| R2 — Process function | Review of vendor heat & material balance, P&IDs, and capacity calculations vs. caustic-oxidation demand and shared-interface allocation. |
| R3 — Materials / mechanical / environmental | Material test reports, mill certificates, coating reports; cold-weather design review (winterisation); HAZOP for drain interface. |
| R4 — Interfaces | Interface schedule review against `INTERFACE_REGISTER.csv` PKG-087 rows; terminal-point check against Package Datasheet. |
| R5 — Controls and safety | Vendor cause-and-effect, alarm/shutdown matrix review; integration test with EPC controls topology; F&G coverage study. |
| R6 — Sour service / emissions | Sour-service material selection review; emissions calculation review; regulatory permit cross-check. |
| R7 — Operability / turnover | Vendor document review log (DEL-087-05); EPC vendor package review and acceptance evidence (DEL-087-06). |

## Documentation

The Package Vendor SHALL deliver the following documentation (final list governed by `26020-Package_Requirements.docx` vendor document tables — location TBD):

- Vendor package design basis and datasheet set (anticipated artifact, this deliverable). [`_CONTEXT.md` Anticipated Artifacts]
- Vendor engineered physical equipment package (anticipated artifact, this deliverable). [`_CONTEXT.md` Anticipated Artifacts]
- Vendor document register and submittals (consumed by DEL-087-05). [`DELIVERABLE_REGISTER.csv` DEL-087-05]
- Process flow diagrams, P&IDs, equipment datasheets, instrument index, cause-and-effect matrix, electrical single-line(s) at package boundary, layout / general arrangement drawings, structural / foundation loads, lifting and shipping drawings, operating and maintenance manuals, spare parts list, test certificates and FAT records — ASSUMPTION (typical vendor package submittal set; confirm against source vendor-document tables). [ASSUMPTION; location TBD]
