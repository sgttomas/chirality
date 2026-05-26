# Specification — DEL-087-03 Construction Work Package (PKG-087 Incinerator)

## Scope

### In scope

The EPC Integrator Construction Work Package (CWP) shall describe how the PKG-087 Incinerator package is physically installed, built, inspected, turned over, and tied into the larger facility systems (`_CONTEXT.md` Scope). Equipment in package per source: incinerator knockout drum, knockout drum transfer pump, low pressure flare stack, and incinerator blower (PACKAGE_REGISTER.csv PKG-087).

The CWP shall cover the twelve declared facility interfaces for PKG-087 listed in `INTERFACE_REGISTER.csv`:

- Process Piping (IFC-3FF4A46502)
- Utility Piping (IFC-B01B4DDC89)
- Relief / Flare / Vent (IFC-DBC4027D02)
- Drain / Containment (IFC-2BACDFA5F1)
- Electrical Power (IFC-D8FC238CE8)
- Grounding / Bonding (IFC-FD13F602FB)
- Area / Exterior Lighting (IFC-1892D97798)
- I&C / Control Cabling (IFC-5ED2CD719C)
- Building HVAC / Services (IFC-588E647FEE)
- Fire & Gas / Safety Systems (IFC-F147F6DD86)
- Maintenance Access (IFC-A18F15D335)
- Structural / Foundations / Supports (IFC-23A65D01E5)

The CWP shall cover SOW-0111, SOW-0112, SOW-0113, SOW-0114 (`_CONTEXT.md`).

### Out of scope

- Package engineering, package design, vendor documentation, and physical equipment supply — owned by the Package Vendor (PACKAGE_REGISTER.csv PKG-087 split-of-responsibility).
- Permit-final emissions tabulation (DBM source explicitly defers permit-final values; `3-25_Comp_and_Liquids_DBM.md` line 555).
- Package-specific exclusions: TBD; no package-specific exclusions stated in source materials (PACKAGE_REGISTER.csv PKG-087 Exclusions field).

## Requirements

| Req ID | Requirement | Source | Notes |
|---|---|---|---|
| R-087-03-01 | The CWP shall identify all package tagged equipment (knockout drum, transfer pump, LP flare stack, blower) with installation sequence and method statements. | PACKAGE_REGISTER.csv PKG-087 (equipment list) | ASSUMPTION on requirement form (CWP type convention); equipment list is sourced. |
| R-087-03-02 | The CWP shall include an installation and tie-in workface plan covering each of the twelve declared interfaces in §Scope. | `_CONTEXT.md` Anticipated Artifacts; INTERFACE_REGISTER.csv | Interface list is sourced. |
| R-087-03-03 | The CWP shall include a construction interface and turnover checklist. | `_CONTEXT.md` Anticipated Artifacts | |
| R-087-03-04 | Tie-in to the Relief / Flare / Vent system shall preserve the spent-caustic storage tank flame-arrestor vent path to the incinerator header. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 402 | Source-anchored. |
| R-087-03-05 | The CWP shall reflect that the incinerator is a shared-interface system between the 03-25 (Comp & Liquids) and 04-25 (Gas Plant) facilities; final service allocation is an open interface item. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 56, 547 | Open allocation — see Conflict Table. |
| R-087-03-06 | Utility Piping tie-ins (fuel gas, instrument air, electrical power) shall reflect that fuel gas, instrument air, and electrical power are shared cross-facility utilities with the 04-25 gas plant; instrument air compression is supplied from 04-25. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 56 | Source-anchored. |
| R-087-03-07 | Material restrictions: aluminum shall not be used where caustic exposure may occur (caustic building); incinerator package materials in caustic-impacted service shall comply. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 402 | Source-anchored; applicability to incinerator package itself is ASSUMPTION (DBM clause is stated for the caustic building). |
| R-087-03-08 | Tie-in design pressures, temperatures, and flow rates per interface | TBD (not in accessible sources — `26020-01-PT-RFQ-25-003_Incinerator.docx` not accessible; location TBD) | TBD per interface. |
| R-087-03-09 | Inspection and test plan (ITP) for installation steps | TBD (not in accessible sources) | location TBD. |
| R-087-03-10 | Hazardous area classification compliance for installed equipment | TBD (not in accessible sources) | location TBD. |
| R-087-03-11 | Structural / foundation loading, anchor patterns, grout requirements per the package datasheet (DEL-087-02). | DEL-087-02_package-datasheet (sibling deliverable, downstream input) | ASSUMPTION on hand-off mechanism; values TBD. |

## Standards

| Standard / Code | Applicability | Status |
|---|---|---|
| TBD (no specific codes named in accessible source slices) | All construction installation work | location TBD |
| Project specifications referenced by `26020-Package_Requirements.docx` package heading 40 | Vendor / EPC package requirements | document referenced but not locally readable; location TBD |
| Project Bid Docs `26020-01-PT-RFQ-25-003_Incinerator.docx` | Package basis | not locally accessible; location TBD |

ASSUMPTION: Applicable construction codes (e.g., ASME B31.3 for process piping, NEC/CEC for electrical, AWS D1.1 for structural welding, NFPA for fire & gas) are likely applicable based on discipline (Mechanical) and interface set; clause-level requirements not derived without accessible source text.

## Verification

| Req ID | Verification approach | Artifact |
|---|---|---|
| R-087-03-01 | Document review against PACKAGE_REGISTER.csv PKG-087 equipment list | Construction work package (Equipment Installation Index) |
| R-087-03-02 | Coverage matrix: 12 declared interfaces × workface plan sections | Installation and tie-in workface plan |
| R-087-03-03 | Turnover walk-down against checklist | Construction interface and turnover checklist |
| R-087-03-04 | Field verification of flame-arrestor vent path continuity | Tie-in punch list / mechanical completion record |
| R-087-03-05 | Interface agreement record between 03-25 and 04-25 owners | Interface register entry resolution (open) |
| R-087-03-06 | Utility tie-in agreement check vs. 04-25 supply | Utility tie-in record |
| R-087-03-07 | Material certificate review (MTR) for caustic-exposed components | MTR file |
| R-087-03-08..11 | TBD pending source resolution | TBD |

## Documentation

Required artifacts produced under this deliverable (from `_CONTEXT.md` Anticipated Artifacts):

- Construction work package (top-level package document)
- Installation and tie-in workface plan
- Construction interface and turnover checklist

Inputs consumed (sibling / upstream):

- DEL-087-01 Scope of Work (sibling) — package scope, tagged equipment list, integration narrative
- DEL-087-02 Package Datasheet (sibling) — vendor handoff data, design criteria, interface requirements matrix
- DEL-087-04 Vendor Engineered Equipment Package — vendor design basis (downstream input for vendor-supplied installation data)
