# Datasheet: DEL-106-01_scope-of-work — Scope of Work

> Descriptive datasheet for the EPC Integrator Scope of Work covering PKG-106
> "Yard Lighting". All non-trivial values are cited to their source slice;
> missing values are marked `TBD`, inferences as `ASSUMPTION`.

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-106-01_scope-of-work` | `_CONTEXT.md` Identity |
| Name | Scope of Work | `_CONTEXT.md` Identity |
| ParentPackageID | `PKG-106` | `_CONTEXT.md` Identity |
| ParentWorkbookID | 106 | `_CONTEXT.md` Identity |
| PackageName | Yard Lighting | `_CONTEXT.md` Identity; `PACKAGE_REGISTER.csv` row `PKG-106` |
| Discipline | Electrical | `_CONTEXT.md` Identity; `PACKAGE_REGISTER.csv` row `PKG-106` |
| Type | EPC Scope of Work | `_CONTEXT.md` Identity |
| ResponsibleParty | EPC Integrator (this SOW); Package Vendor owns package engineering/design/equipment per the responsibility model | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` ResponsibilityModel |
| WBS | TBD (workbook WBS column blank for PKG-106) | `PACKAGE_REGISTER.csv` row `PKG-106` (**TBD**) |
| CoA Tracking | 26020-01-30-001 | `PACKAGE_REGISTER.csv` row `PKG-106` |
| Workbook source row | Packages row 12 | `_CONTEXT.md` Source Reference; `PACKAGE_REGISTER.csv` |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Scope item covered | `SOW-0011` (IN scope) | `SCOPE_LEDGER.csv` row `SOW-0011` |
| Supported objectives | `OBJ-001`, `OBJ-004`, `OBJ-005`, `OBJ-009`, `OBJ-010` (PACKAGE_HEURISTIC; **ASSUMPTION** at deliverable-ID granularity) | `_CONTEXT.md` Supports Objectives; `OBJECTIVE_PACKAGE_MAP.csv` |
| Package function (workbook) | Workbook-defined vendor-owned Electrical package for "Yard Lighting" under WBS TBD; Package Vendor owns engineering/design/equipment; EPC Integrator owns facility integration | `PACKAGE_REGISTER.csv` row `PKG-106` (Description; SourceRefRaw) |
| Applicable interface types | Electrical Power; Grounding / Bonding; Area / Exterior Lighting | `PACKAGE_REGISTER.csv` row `PKG-106`; `INTERFACE_REGISTER.csv` `IFC-6FCF1B30D6`, `IFC-DA0D60681B`, `IFC-ED86F51087` |
| Tagged major equipment | TBD — `PACKAGE_REGISTER.csv` row `PKG-106` does not enumerate specific yard-lighting equipment (no MajorEquipment text supplied for this row); detailed equipment expected from Package Vendor design | `PACKAGE_REGISTER.csv`; **TBD** |
| Vendor / sub-package ownership model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; EPC Integrator owns integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration | `PACKAGE_REGISTER.csv` ResponsibilityModel |
| Package-specific exclusions | TBD; no package-specific exclusions stated in source materials | `PACKAGE_REGISTER.csv` row `PKG-106` |
| Discipline basis section | DBM-Deepcut SEC-12 "Electrical Basis", subsection "Lighting and Receptacles" (lines 3027-3035) and DBM-Comp_and_Liquids SEC-12 "Electrical Buildings, Raceways, Lighting, and Heat Tracing" (lines 764-770) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` |
| Construction-scope characterization (Deepcut DBM) | "Area lighting" is listed within the Tourmaline field construction scope table (DBM-Deepcut SEC-04, line 120). This conflicts with the workbook framing of PKG-106 as a vendor-owned package; recorded in the Conflict Table. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 120 |

## Conditions

Site/environmental conditions governing this scope are inherited from facility
basis (not restated as deliverable values).

| Condition | Value | Source |
|---|---|---|
| Lamp/luminaire technology | LED type to minimize electrical demand and maintenance | DBM-Deepcut SEC-12 "Lighting and Receptacles", line 3029 |
| Outdoor / process-area fixture type | LED fixtures for process area and outdoor lighting | DBM-Deepcut SEC-12, line 3031 |
| General-purpose lighting supply | 120/208 V from the nearest power distribution centre | DBM-Deepcut SEC-12, line 3029 |
| Hazardous-area suitability | Lighting fixtures shall be suitable for the area classification in which they are installed | DBM-Deepcut SEC-12, line 3029 |
| Light-pollution / regulatory controls | LED fixtures; selective minimization of exterior lighting to working areas; downward illumination (downcast floodlights); prohibition of horizontally aimed floodlights; photocell or switch control; lighting mast poles located away from pad edge where mast poles are required | DBM-Deepcut SEC-12, line 3035 |
| Emergency lighting basis | LED fixtures with battery backup as required by building codes; at least two emergency lighting fixtures in each building for power-outage conditions | DBM-Deepcut SEC-12, line 3031 |
| Minimum ambient (affects outdoor enclosures, gaskets, drivers) | -40 deg C minimum ambient governs exposed equipment, package buildings, control panels, instrumentation, and field devices | DBM-Comp_and_Liquids SEC-04 line 145 (cross-reference for outdoor electrical equipment) |
| Lighting design scope statement (Comp/Liquids basis) | "Lighting, receptacles, electric heat tracing, building heaters, and cathodic protection are part of the electrical design scope." | DBM-Comp_and_Liquids SEC-12 "Electrical Buildings, Raceways, Lighting, and Heat Tracing", line 770 |
| Specific illuminance levels (lux) by area | TBD — not enumerated in locally accessible source slices | `location TBD` |
| Pole heights, mast counts, spacing | TBD — not enumerated in locally accessible source slices | `location TBD` |
| Photometric calculation basis | TBD — not enumerated in locally accessible source slices | `location TBD` |

## Construction (Material and Code Basis)

Materials and codes applicable to "Yard Lighting" as drawn from the project
electrical basis:

| Item | Requirement | Source |
|---|---|---|
| Governing electrical code | Canadian Electrical Code (CEC), with conduit/wiring methods and hazardous-area sealing complying with CEC and the applicable area classification | DBM-Deepcut SEC-12, line 3025 |
| Fixture/luminaire technology | LED (general purpose, process area, outdoor, MCC room, emergency) | DBM-Deepcut SEC-12, lines 3029, 3031 |
| Outdoor wiring method | ASSUMPTION: rigid conduit or direct-buried/duct-bank consistent with CEC and area classification; SEC-12 specifies rigid conduit for building lighting (line 3025) but does not explicitly state the outdoor yard-lighting wiring method | DBM-Deepcut SEC-12, line 3025; **ASSUMPTION** |
| GFI protection (outdoor receptacles, related to yard electrical work) | Outdoor receptacles in hazardous and non-hazardous areas shall be fed from GFI breakers unless receptacles with integral GFI and local reset are advantageous | DBM-Deepcut SEC-12, line 3033 |
| Detailed fixture catalog / wattages / IES files | TBD — vendor design output | `location TBD` |
| Specific lighting standards (e.g., IES RP-, IEEE 1100, CSA C22.2 fixture standards) | TBD — not enumerated in locally accessible source slices | `location TBD` |

## Anticipated Artifacts (this deliverable produces)

- Package scope of work (`ART-1D00D7FAE6`)
- Tagged equipment and package identity list (`ART-508A45C565`)
- Package function and whole-facility integration narrative (`ART-C1764AFD92`)
- Package responsibility assignment record (`ART-27C44AFC19`)

Source: `ARTIFACT_REGISTER.csv` rows scoped to `DEL-106-01_scope-of-work`.

## References

- `_CONTEXT.md`
- `_REFERENCES.md`
- `_Decomposition/.../GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv`
- `_Decomposition/.../GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv`
- `_Decomposition/.../GATE-07_Final_Published_2026-05-24/SCOPE_LEDGER.csv`
- `_Decomposition/.../GATE-07_Final_Published_2026-05-24/ARTIFACT_REGISTER.csv`
- `_Decomposition/.../GATE-07_Final_Published_2026-05-24/INTERFACE_REGISTER.csv`
- `_Decomposition/.../GATE-07_Final_Published_2026-05-24/OBJECTIVE_REGISTER.csv`
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (SEC-12 Lighting and Receptacles; SEC-04 construction-scope characterization)
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (SEC-12 Electrical Buildings, Raceways, Lighting, and Heat Tracing; SEC-04 ambient)
- `_Sources/26020-Package_Requirements.docx` — `location TBD` (not parsed in this run)
- `_Sources/26020-Packages_Interfaces_4_export.xlsx` row 12 — `location TBD` (xlsx not opened in this run)
