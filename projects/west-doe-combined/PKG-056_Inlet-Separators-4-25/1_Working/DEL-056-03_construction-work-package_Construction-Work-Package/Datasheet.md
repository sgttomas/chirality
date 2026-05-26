# Datasheet — DEL-056-03 Construction Work Package (PKG-056 Inlet Separators 4-25)

## Identification

| Field | Value |
|---|---|
| DeliverableID | DEL-056-03_construction-work-package |
| Deliverable Name | Construction Work Package |
| Parent Package | PKG-056 (Inlet Separators 4-25) |
| Workbook row | 68 |
| Discipline | Mechanical |
| Deliverable Type | EPC Construction Work Package |
| Responsible Party | EPC Integrator |
| Facility | West Doe 04-25 Deepcut Gas Plant Expansion (300 MMSCFD) |
| WBS | 01 |
| Package SOWs covered | SOW-0127, SOW-0128, SOW-0129, SOW-0130 |
| Objectives supported | OBJ-001, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 (ASSUMPTION: package-heuristic association per `_CONTEXT.md`) |

## Attributes

| Field | Value | Source |
|---|---|---|
| Package physical scope | Two (2) identical horizontal three-phase HP inlet separators with plot provision for a future third | PACKAGE_REGISTER.csv PKG-056; DBM SEC-04 (`4-25_Deepcut_DBM.md`) |
| Vessel size (each) | 9 ft ID x 40 ft S/S | DBM SEC-04 / Functional Configuration / Inlet Separation |
| Per-separator design pressure | 9,377 kPag | DBM SEC-04 / Inlet Separator Design Parameters |
| Process function | Receives raw inlet gas and separates sour natural gas, sour raw condensate, and sour water | PACKAGE_REGISTER.csv PKG-056 |
| Internal coating | Devchem 253 (vessel internal); piping not coated | DBM SEC-04 |
| Mist eliminator | Vertical high-performance mesh/vane (subject to operations review) | DBM SEC-04 |
| Per-separator gas design rate | 125 to 150 MMSCFD | DBM SEC-04 / Inlet Separator Design Parameters |
| Slug capacity per separator | 31.8 m3 or 33.9 m3 (CONFLICT — see Guidance) | DBM SEC-04 |
| Inlet pressure control | At minimum two parallel balanced-globe inlet PCVs per separator; hardened trim recommended; design dP <=5 psid | DBM SEC-04 |
| Liquid outlet heater | One per inlet separator package (two total at 04-25 under installed basis) | DBM SEC-04 |
| Construction responsibility (field) | Tourmaline Oil Corporation field construction (modular setting, mechanical hookup, interconnecting piping, installation of shipped-loose components, terminations) | DBM SEC-01 Construction Responsibility table |
| Tie-in interface types | Process Piping; Utility Piping; Relief/Flare/Vent; Drain/Containment; EHT; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Fire & Gas/Safety Systems; Maintenance Access; Structural/Foundations/Supports | PACKAGE_REGISTER.csv PKG-056 |

## Conditions

| Item | Value | Source |
|---|---|---|
| Service | Sour wet inlet gas (H2S-bearing) | DBM SEC-04 |
| Inlet pipeline operating envelope | Low/Design 653 psig; Normal-high 725 psig; Max 1300 psig (90% of assumed 1440 psig upstream MAOP, MAWP TBC) | DBM SEC-04 / Inlet Pipeline Pressure and Flow |
| Two-phase inlet possible | Yes — winter/cool-down condensation; methanol injection upstream may be required | DBM SEC-04 |
| Construction phasing | One phase, single train | DBM SEC-01 |
| Site | West Doe Complex, facility 04-25 | DBM SEC-01 |
| Hazardous-area classification | TBD (location TBD in deliverable-local sources) |  |
| Site climatic basis | TBD (DBM SEC-02 Site Data Basis not extracted into this kit) |  |

## Construction

| Element | Statement | Source |
|---|---|---|
| Modular assembly | Package vendor delivers shop-assembled equipment package; field activities include off-loading, setting on foundations, and mechanical hookup | DBM SEC-01 Construction Responsibility; PACKAGE_REGISTER.csv PKG-056 |
| Foundations & supports | Tourmaline field construction scope (grading, piling, foundations) | DBM SEC-01 |
| Interconnecting piping | Field-installed by Tourmaline to ISBL/OSBL tie-in points; per-tie-in responsibility to be confirmed | DBM SEC-01 |
| Shipped-loose items | Field installation of shipped-loose instruments, valves, components (Tourmaline scope) | DBM SEC-01 |
| Cabling | Field installation of home-run cables and electrical terminations (Tourmaline scope) | DBM SEC-01 |
| Inspection/Test Plan (ITP) | TBD — to be developed by EPC Integrator |  |
| Turnover checklist | TBD — to be developed by EPC Integrator (anticipated artifact) | `_CONTEXT.md` Anticipated Artifacts |
| Workface plan | Required as an anticipated artifact (installation and tie-in workface plan) | `_CONTEXT.md` Anticipated Artifacts |

## References

- PACKAGE_REGISTER.csv row PKG-056 — `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv`
- DELIVERABLE_REGISTER.csv row DEL-056-03 — same snapshot folder
- DBM-Deepcut SEC-01 Project and Document Basis (Construction Responsibility table) — `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`
- DBM-Deepcut SEC-04 Inlet, Separation, Stabilization, and Stabilizer Overheads Basis — same file
- 26020-Package_Requirements.docx package heading 11 — `_Sources/26020-Package_Requirements.docx` (location TBD; binary not directly readable in this run)
- Deliverable `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`
