# Datasheet — DEL-063-02 Package Datasheet (PKG-063 Tanks, DSO (API 650))

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | DEL-063-02_package-datasheet | _CONTEXT.md |
| Name | Package Datasheet | _CONTEXT.md |
| ParentPackageID | PKG-063 | _CONTEXT.md |
| ParentWorkbookID | 63 | _CONTEXT.md |
| PackageName | Tanks, DSO (API 650) | _CONTEXT.md; PACKAGE_REGISTER.csv (row PKG-063) |
| Discipline | Mechanical | _CONTEXT.md; PACKAGE_REGISTER.csv |
| Type | EPC Package Datasheet | _CONTEXT.md |
| ResponsibleParty | EPC Integrator | _CONTEXT.md; PACKAGE_REGISTER.csv |
| Tag / Identifier | 26020-01-PT-19-001 - Tanks, DSO | PACKAGE_REGISTER.csv (PKG-063, CoA tracking number) |
| WBS | 01 | PACKAGE_REGISTER.csv (PKG-063) |
| Source basis (Word) | 26020-Package_Requirements.docx package heading 18 | PACKAGE_REGISTER.csv; ARTIFACT_REGISTER.csv |
| Source basis (Workbook) | Workbook Packages row 90 | PACKAGE_REGISTER.csv |
| Source basis (DBM) | DBM-Deepcut/4-25_Deepcut_DBM.md | PACKAGE_REGISTER.csv |

## Attributes

Major included equipment (one item; package scope is a single tank):

| Attribute | Value | Source |
|---|---|---|
| Item No. | DSO Storage Tank | ARTIFACT_REGISTER.csv ART-966875EFC3 (`Major included equipment evidence`); 26020-Package_Requirements.docx heading 18 |
| Quantity | 1 | DBM-Deepcut/4-25_Deepcut_DBM.md ("Disulphide oil storage — 1 x 400 bbl tank"); ARTIFACT_REGISTER.csv ART-966875EFC3 |
| Nominal capacity | 400 bbl | ARTIFACT_REGISTER.csv ART-966875EFC3; DBM-Deepcut/4-25_Deepcut_DBM.md §"Disulphide Oil, Spent Caustic, and Waste Amine" |
| Design code | Modified API 650 | ARTIFACT_REGISTER.csv ART-966875EFC3 (`Design & fabrication to modified API 650`); 26020-Package_Requirements.docx heading 18 |
| Tank class | Atmospheric pressure tank | ARTIFACT_REGISTER.csv ART-966875EFC3; DBM-Deepcut/4-25_Deepcut_DBM.md (§DSO storage tank is atmospheric) |
| Design pressure | 32 oz | ARTIFACT_REGISTER.csv ART-966875EFC3 |
| Design vacuum | 1.0 oz | ARTIFACT_REGISTER.csv ART-966875EFC3 |
| Heater minimum maintained temperature | 32.2 °C (90 °F) | ARTIFACT_REGISTER.csv ART-966875EFC3 (`c/w heater at 32.2 °C (90 °F) minimum. Vendor to design heater.`) |
| Heater design responsibility | Vendor (Package Vendor) | ARTIFACT_REGISTER.csv ART-966875EFC3 |
| Internal coating | Floor, walls, roof internally coated | ARTIFACT_REGISTER.csv ART-966875EFC3 |
| Insulation | Insulated to maintain DSO above pour point for truck-out and handling | ARTIFACT_REGISTER.csv ART-966875EFC3 |
| Minimum (pour-point related) temperature | TBD | ARTIFACT_REGISTER.csv ART-966875EFC3 (`Minimum temperature TBD`) |
| Fluid specific gravity (design) | 1.75 (TBC) | DBM-Deepcut/4-25_Deepcut_DBM.md (`DSO tank design specific gravity is 1.75 TBC`) |
| Tank vent / overpressure path | Off-gas routed to incinerator header | DBM-Deepcut/4-25_Deepcut_DBM.md ("Vapours from the spent caustic storage tank and DSO off-gas flow to the incinerator") |
| Backflash protection | Flame arrestor on incinerator-header connection | DBM-Deepcut/4-25_Deepcut_DBM.md ("protected against backflash with a flame arrestor") |
| Blanket gas | Low-pressure fuel gas blanket | DBM-Deepcut/4-25_Deepcut_DBM.md ("blanketed with low-pressure fuel gas") |
| Truck-out provision | Yes (truck-out for disposal) | DBM-Deepcut/4-25_Deepcut_DBM.md (`truck-out and disposal`); ARTIFACT_REGISTER.csv ART-966875EFC3 |
| Alternate disposal path | Pumping DSO into C5+ product — to be reviewed during detailed engineering | DBM-Deepcut/4-25_Deepcut_DBM.md (`Pumping DSO to C5+ product is subject to detailed-engineering review`) |

## Conditions

| Parameter | Value | Source |
|---|---|---|
| Process function | Receives separated DSO from the DSO separator (level-controlled) within the caustic regeneration system | PACKAGE_REGISTER.csv PKG-063 (`Process function`) |
| Service fluid | Disulphide oil (DSO) — by-product of NGL non-regenerative caustic treating | DBM-Deepcut/4-25_Deepcut_DBM.md §"Disulphide Oil, Spent Caustic, and Waste Amine" |
| Operating pressure | Atmospheric | DBM-Deepcut/4-25_Deepcut_DBM.md; ARTIFACT_REGISTER.csv ART-966875EFC3 |
| Operating temperature (minimum maintained) | ≥ 32.2 °C (90 °F) via tank heater | ARTIFACT_REGISTER.csv ART-966875EFC3 |
| Pour point of contents | TBD; insulation/heater sized to keep DSO above pour point | ARTIFACT_REGISTER.csv ART-966875EFC3 |
| Site location | 04-25 Deep Cut Gas Plant; DSO off-gas to incinerator physically located at 3-25 facility | DBM-Deepcut/4-25_Deepcut_DBM.md ("incinerator is physically located at the 3-25 facility... services the 4-25 NGL mercaptan treating system") |
| Knock-out drum upstream of incinerator | Provided (separates free liquids before incinerator) — owned by incinerator scope, not this package | DBM-Deepcut/4-25_Deepcut_DBM.md |

## Construction

Battery limits / interface requirements (carried as evidence per K-PROV-1; one row per workbook X-column interface fact for PKG-063):

| Interface ID | Interface Type | Applicable | Source |
|---|---|---|---|
| IFC-B8225E1CAC | Process Piping | YES | INTERFACE_REGISTER.csv |
| IFC-55319DFCC3 | Relief / Flare / Vent | YES | INTERFACE_REGISTER.csv |
| IFC-976437DD6E | Drain / Containment | YES | INTERFACE_REGISTER.csv |
| IFC-F0E7550CA2 | Grounding / Bonding | YES | INTERFACE_REGISTER.csv |
| IFC-BDDC5F17F1 | Area / Exterior Lighting | YES | INTERFACE_REGISTER.csv |
| IFC-89C542835E | Cathodic Protection | YES | INTERFACE_REGISTER.csv |
| IFC-289323FEB4 | I&C / Control Cabling | YES | INTERFACE_REGISTER.csv |
| IFC-391B72231B | Grading / Site Drainage / Spill Containment | YES | INTERFACE_REGISTER.csv |
| IFC-DFD52CFB01 | Structural / Foundations / Supports | YES | INTERFACE_REGISTER.csv |

Construction-relevant notes:
- Tank shell, floor, roof: design & fabrication to modified API 650 (ASSUMPTION: "modified" deviations from API 650 are vendor-proposed and EPC-accepted; explicit modifications not enumerated in available source slices — `location TBD` in 26020-Package_Requirements.docx heading 18). Source: ARTIFACT_REGISTER.csv ART-966875EFC3.
- Foundation, supports, grounding/bonding pad, cathodic protection, drain/containment (curb/dyke/sump), and area lighting are EPC-integrator-owned interface scope items, not vendor scope. Source: PACKAGE_REGISTER.csv PKG-063 (`EPC Integrator owns integration into the functional process facility, including interfaces, tie-ins...`).

## References

- `_CONTEXT.md` (deliverable-local)
- `_REFERENCES.md` (deliverable-local)
- `_DEPENDENCIES.md` (deliverable-local)
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` — row `DEL-063-02_package-datasheet`
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv` — row `PKG-063`
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/ARTIFACT_REGISTER.csv` — artifacts mapped to `DEL-063-02_package-datasheet`
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/INTERFACE_REGISTER.csv` — interfaces for `PKG-063`
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — §"Disulphide Oil, Spent Caustic, and Waste Amine"; `Disulphide oil storage — 1 x 400 bbl tank`; DSO tank description (atmospheric, heated, insulated, flame-arrestor, fuel-gas blanket, SG 1.75 TBC)
- `_Sources/26020-Package_Requirements.docx` — package heading 18 (`location TBD` for detailed clause-level text; binary not opened in this pass)
- `_Sources/Bid Docs/_Budgetary/26020-01-PT-RFQ-19-001_Tanks_DSO_R0.docx` — listed in PACKAGE_REGISTER.csv as Word Source Basis; **not locally accessible during this pass** (path not present under `_Sources/`); content `location TBD`
