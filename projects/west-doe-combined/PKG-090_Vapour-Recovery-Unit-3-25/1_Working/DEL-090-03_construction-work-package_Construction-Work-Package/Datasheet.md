# Datasheet: DEL-090-03 — Construction Work Package (Vapour Recovery Unit 3-25)

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-090-03_construction-work-package` |
| Name | Construction Work Package |
| ParentPackageID | `PKG-090` |
| PackageName | Vapour Recovery Unit 3-25 |
| Discipline | Mechanical |
| Type | EPC Construction Work Package |
| ResponsibleParty | EPC Integrator |
| Source basis | `_Sources/26020-Package_Requirements.docx`, section `26020-01-PT-12-002 - Vapour Recovery Unit`; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-06 "Vapour Recovery" |

## Attributes (package being installed)

| Attribute | Value | Source |
|---|---|---|
| Service | Sour gas vapour recovery (collects vapours from condensate and produced-water tanks and selected process vents) | DBM 3-25 SEC-06 "Vapour Recovery"; `26020-01-PT-12-002 / Basic Scope` |
| Train arrangement | Two (2) 100% capacity trains, lead-lag, both housed in one building | `26020-01-PT-12-002 / Basic Scope` |
| Compressor type | Two-stage rotary vane, positive displacement (Ro-Flo) | `26020-01-PT-12-002 / Major Included Equipment` |
| Compressor model (package vendor source) | Ro-Flo 17S/217M | `26020-01-PT-12-002 / Basic Scope` |
| Compressor model (decomposition register) | Ro-Flo 12S/212M | `PACKAGE_REGISTER.csv` row PKG-090 — CONFLICT, see Guidance Conflict Table |
| Driver | 200 HP VFD electric motor; one motor per train drives both stages | `26020-01-PT-12-002 / Major Included Equipment`; DBM SEC-06 |
| Sour service basis | 0.3557 mol% H2S, 0.9434 mol% CO2; NACE designation applies | `26020-01-PT-12-002 / Major Included Equipment` |
| Seal arrangement | Dual mechanical pressurized barrier seal (Plan 53 type), fuel-gas buffered; alarms and primary vent to LP flare | `26020-01-PT-12-002 / Major Included Equipment` |
| Discharge routing | VRU discharge to 04-25 SOC suction (no local 03-25 SOC retained under SCA-002) | DBM SEC-06 "Vapour Recovery"; SEC-04 SCA reconciliation |
| Recycle / suction-pressure control | Second-stage discharge to first-stage suction; sized for 100% flow at minimum driver speed and lowest discharge pressure | DBM SEC-06 |
| Make-up / blanket gas | LP fuel-gas regulator maintains minimum suction pressure at maximum turndown | DBM SEC-06 |
| LP flare bypass | V-ball valve on VRU suction header, operated by VRU suction pressure | DBM SEC-06 |
| Suction header drainage | Free-drain or slope toward flare KO interface per detailed design | DBM SEC-06 |

## Conditions (construction context)

| Attribute | Value | Source |
|---|---|---|
| Site | 03-25 West Doe Compressor Station and Liquids Hub, LSD 03-25-80-15 W6M, north of Dawson Creek, BC | DBM SEC-02 |
| Site elevation | 673 m AMSL | DBM SEC-02 |
| Facility context | Brownfield sour-gas compressor station integrated with condensate and produced-water liquids hub | DBM SEC-01 |
| Project phase | EPC integration (construction and tie-in of vendor-supplied package into 03-25 facility) | `_CONTEXT.md` Scope; `PACKAGE_REGISTER.csv` PKG-090 split |
| Owner split | Package vendor: package engineering, design, vendor documentation, physical equipment package. EPC Integrator: integration into the process facility (interfaces, tie-ins, constructability, procurement/construction coordination, facility-level integration). | `PACKAGE_REGISTER.csv` PKG-090 |
| By-others items (not in vendor package scope, EPC handles) | Shipping compressor packages to site, installation on piles, tie-in piping, electrical, instrumentation | `26020-01-PT-12-002` package scope-notes table |

## Construction Interfaces (applicable per Package Requirements)

| Interface Type | Applicability | Source |
|---|---|---|
| Process Piping | Yes | `26020-01-PT-12-002 / Physical Interface Summary` |
| Utility Piping | Yes | same |
| Relief / Flare / Vent | Yes | same |
| Drain / Containment | Yes | same |
| Electrical Power | Yes | same |
| Area / Exterior Lighting | Yes | same |
| EHT (electric heat trace) | Yes | same |
| Grounding / Bonding | Yes | same |
| Cathodic Protection | No | same |
| I&C / Control Cabling | Yes | same |
| Communications / Network | No | same |
| Building HVAC / Services | No (per Package Requirements row); see CONFLICT note | same; `PACKAGE_REGISTER.csv` lists HVAC as applicable — CONFLICT, see Guidance |
| Fire & Gas / Safety Systems | Yes | same |
| Maintenance Access | Yes | same |
| Grading / Site Drainage / Spill Containment | No | same |
| Structural / Foundations / Supports | Yes | same |
| Product Loading | No | same |
| Pipeline / Pigging | No | same |

## Anticipated Construction Artifacts

| Artifact | Notes | Source |
|---|---|---|
| Construction work package | Master execution document for the VRU 3-25 install | `_CONTEXT.md` Anticipated Artifacts |
| Installation and tie-in workface plan | Workface-level sequencing for setting trains on piles and tying piping/utilities | `_CONTEXT.md` Anticipated Artifacts |
| Construction interface and turnover checklist | EPC ↔ vendor and EPC ↔ commissioning turnover gates | `_CONTEXT.md` Anticipated Artifacts |

## Covered Scope and Supported Objectives

| Field | Value |
|---|---|
| Covers Scope Items | `SOW-0249`, `SOW-0250`, `SOW-0251`, `SOW-0252` (`_CONTEXT.md`) |
| Supports Objectives | `OBJ-002`, `OBJ-003`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` (`_CONTEXT.md`; ASSUMPTION — PACKAGE_HEURISTIC association) |

## References

- `_CONTEXT.md`
- `_REFERENCES.md`
- `_DEPENDENCIES.md`
- `_Sources/26020-Package_Requirements.docx`, section `26020-01-PT-12-002 - Vapour Recovery Unit`
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-06 "Vapour Recovery"
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv` row `PKG-090`
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` row `DEL-090-03_construction-work-package`

TBD items (no local source slice):
- Detailed lift weights, pile design loads, and module split dimensions for the VRU building — location TBD (vendor MEC-018 Lifting/Handling Study not yet available).
- Final failure-action of recycle control valves — flagged TBC in DBM SEC-05; treat as TBD for VRU recycle valve until vendor confirms.
