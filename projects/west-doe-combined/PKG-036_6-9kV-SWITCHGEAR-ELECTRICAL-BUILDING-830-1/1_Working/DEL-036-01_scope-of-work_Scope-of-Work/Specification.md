# Specification: DEL-036-01_scope-of-work

## Scope

### In scope
- Mandatory EPC Integrator Scope of Work for `PKG-036` "6.9kV SWITCHGEAR ELECTRICAL BUILDING (830-1)" as defined in Workbook Packages row 38 and carried in `SCOPE_LEDGER.csv` row `SOW-0037`.
- Tagged equipment and package identity record for the workbook-defined package (CoA tracking number `26020-01-30-027`, WBS `01`, discipline Electrical).
- Package function and whole-facility integration narrative for the medium-voltage (6.9 kV) distribution role within the facility electrical system.
- Package responsibility assignment record: Package Vendor owns engineering, design, vendor documentation, and the physical equipment package; EPC Integrator owns facility integration and interfaces.

### Out of scope
- Vendor-internal package engineering, fabrication, and assembly content (covered by `DEL-036-04_vendor-engineered-equipment-package`).
- Technical handoff datasheet content for vendor engineering (covered by `DEL-036-02_package-datasheet`).
- Construction/turnover workface content (covered by `DEL-036-03_construction-work-package`).
- Vendor document turnover content (covered by `DEL-036-05_vendor-document-turnover-package`).
- EPC vendor package review and acceptance content (covered by `DEL-036-06_epc-vendor-package-review-and-acceptance`).
- Any package-specific exclusions beyond the workbook row: none stated in source materials (`PACKAGE_REGISTER.csv` row `PKG-036`).

## Requirements

| Req ID | Requirement | Source / status |
|---|---|---|
| R-036-01-01 | The Scope of Work shall identify the package by workbook identity: name "6.9kV SWITCHGEAR ELECTRICAL BUILDING (830-1)", workbook ID 36, workbook row 38, CoA tracking number `26020-01-30-027`, WBS `01`, discipline Electrical. | Workbook Packages row 38; `PACKAGE_REGISTER.csv` |
| R-036-01-02 | The Scope of Work shall record the package responsibility split: Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-036` |
| R-036-01-03 | The Scope of Work shall state the package function as a 6.9 kV switchgear electrical building within the facility medium-voltage distribution system (workbook name basis); ASSUMPTION: function relates to 6.9 kV distribution per DBM electrical voltage and service table. | Workbook Packages row 38; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, voltage and service table |
| R-036-01-04 | The Scope of Work shall identify the building tag as `830-1`. CONFLICT: the DBM electrical-buildings list assigns `830-1` to the 4.16 kV Acid Gas / Overheads Compressor Electrical Building and assigns the 6.9 kV building to tag `820-1`. The Scope of Work shall carry the workbook tag (Gate 7 decomposition basis) and flag the source mismatch in the Conflict Table for human ruling. | Workbook Packages row 38; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical-buildings list (rows for 820-1 and 830-1) |
| R-036-01-05 | The Scope of Work shall enumerate the applicable interface types for the package and identify each by `INTERFACE_REGISTER.csv` IFC ID: Utility Piping (`IFC-9188C9FD26`), Drain / Containment (`IFC-628EF275F0`), Electrical Power (`IFC-3B6012818E`), Grounding / Bonding (`IFC-B6F77BBE8A`), Area / Exterior Lighting (`IFC-D49FB38D6F`), I&C / Control Cabling (`IFC-972B08F285`), Communications / Network (`IFC-349D2200D1`), Building HVAC / Services (`IFC-C81A342112`), Fire & Gas / Safety Systems (`IFC-2C313DA749`), Maintenance Access (`IFC-21B90D3691`), Grading / Site Drainage / Spill Containment (`IFC-DC7DB17C89`), Structural / Foundations / Supports (`IFC-BDE626F7DD`). | `INTERFACE_REGISTER.csv` rows for `PKG-036` |
| R-036-01-06 | The Scope of Work shall reference the source basis: Workbook Packages row 38 and `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (electrical design basis sections). | `PACKAGE_REGISTER.csv` row `PKG-036` |
| R-036-01-07 | The Scope of Work shall identify the scope-item linkage as `SOW-0037` and state the IN-scope rationale per the scope ledger. | `SCOPE_LEDGER.csv` row `SOW-0037` |
| R-036-01-08 | The Scope of Work shall record supported objectives `OBJ-001`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` per the objective-deliverable map. | `OBJECTIVE_DELIVERABLE_MAP.csv` rows for `DEL-036-01_scope-of-work` |
| R-036-01-09 | The Scope of Work shall list the anticipated artifacts: package scope of work (`ART-74190901D1`), tagged equipment and package identity list (`ART-380568AF55`), package function and whole-facility integration narrative (`ART-9B0CE2B67A`), and package responsibility assignment record (`ART-4323ADFFB1`). | `ARTIFACT_REGISTER.csv` rows for `DEL-036-01_scope-of-work` |
| R-036-01-10 | The Scope of Work shall not assert package-specific equipment quantities, breaker counts, transformer sizes, MCC line-up details, or building location coordinates that are not supported by an accessible source slice; such items shall be carried as `TBD`. | Source-grounding rule; no accessible package-specific source slice |

## Standards

| Standard | Applicability | Source / status |
|---|---|---|
| Canadian Electrical Code (CEC) | Grounding conductor sizing for distribution transformers, panelboards, and three-phase motors larger than 100 hp; applicability to this Scope of Work is at the facility-integration level. ASSUMPTION: governing code for the facility per DBM. Location TBD beyond the cited paragraph. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding and bonding paragraphs |
| Facility electrical design basis (West Doe Deepcut DBM, electrical section) | Governs facility-level electrical interfaces consumed by the Scope of Work (voltages, distribution architecture, grounding, cable tray/conduit, electrical-building HVAC). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical design basis section |
| `26020-Package_Requirements.docx` | Not parsed as accessible source slice in this run; location TBD for any package-specific clause applicable to PKG-036. | `_Sources/26020-Package_Requirements.docx` (presence only) |

## Verification

| Req ID | Verification approach |
|---|---|
| R-036-01-01 | Cross-check identity fields against `PACKAGE_REGISTER.csv` row `PKG-036` and Workbook Packages row 38. |
| R-036-01-02 | Cross-check responsibility text against `PACKAGE_REGISTER.csv` row `PKG-036` `RESP_MODEL` column. |
| R-036-01-03 | Confirm the function statement against the DBM voltage/service table (6.9 kV row). |
| R-036-01-04 | Confirm the building tag against Workbook Packages row 38 and the DBM electrical-buildings list; verify Conflict Table entry CT-036-01-001 is present in `Guidance.md`. |
| R-036-01-05 | Confirm each IFC ID against `INTERFACE_REGISTER.csv` rows for `PKG-036`. |
| R-036-01-06 | Confirm cited source paths resolve under `_Sources/` and that `_REFERENCES.md` lists them. |
| R-036-01-07 | Cross-check `SCOPE_LEDGER.csv` row `SOW-0037` for IN-scope flag and package linkage. |
| R-036-01-08 | Cross-check `OBJECTIVE_DELIVERABLE_MAP.csv` rows for `DEL-036-01_scope-of-work`. |
| R-036-01-09 | Cross-check `ARTIFACT_REGISTER.csv` rows for `DEL-036-01_scope-of-work`. |
| R-036-01-10 | Inspect all numeric and equipment statements; values without a cited source slice are flagged `TBD`. |

## Documentation

The Scope of Work production unit shall produce the following artifacts (per `ARTIFACT_REGISTER.csv`):

- `ART-74190901D1` — Package scope of work (EPC Scope of Work).
- `ART-380568AF55` — Tagged equipment and package identity list (Tagged Equipment Evidence).
- `ART-9B0CE2B67A` — Package function and whole-facility integration narrative (EPC Integration Narrative).
- `ART-4323ADFFB1` — Package responsibility assignment record (Responsibility Evidence).
