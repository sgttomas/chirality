# Datasheet — DEL-068-04 Vendor Engineered Equipment Package (TEG Dehydration Unit)

## Identification

| Field | Value |
|---|---|
| DeliverableID | DEL-068-04_vendor-engineered-equipment-package |
| Name | Vendor Engineered Equipment Package |
| ParentPackageID | PKG-068 |
| PackageName | TEG Dehydration Unit |
| Discipline | Mechanical |
| Type | Vendor Package Production Unit |
| ResponsibleParty | Package Vendor (engineering/design/equipment) with EPC Integrator integration review |
| Workbook Reference | Packages row 97; 26020-Package_Requirements.docx package heading 23 |

## Attributes — TEG Dehydration Unit

(Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-05 "TEG Dehydration Basis" and "TEG Package Equipment")

| Attribute | Basis | Source Reference |
|---|---|---|
| Service | Sour-gas dehydration downstream of inlet compression, prior to export to 04-25 system | SEC-05 / TEG Dehydration Basis |
| Capacity configuration | One-by-100 percent TEG unit | SEC-05 / TEG Dehydration Basis |
| Normal / design gas flow | 82.5 MMSCFD | SEC-05 / TEG Dehydration Basis table |
| Maximum gas flow | TBC | SEC-05 / TEG Dehydration Basis table |
| Inlet pressure — low | 4,502 kPag | SEC-05 / TEG Dehydration Basis table |
| Inlet pressure — normal | 5,378 kPag | SEC-05 / TEG Dehydration Basis table |
| Inlet pressure — design | 4,502 kPag | SEC-05 / TEG Dehydration Basis table |
| Inlet pressure — maximum | 6,205 kPag | SEC-05 / TEG Dehydration Basis table |
| Expected inlet temperature | 110 deg F | SEC-05 / TEG Dehydration Basis table |
| Contactor inlet temperature | 10 to 15 deg F above highest operating hydrate/condensation concern | SEC-05 / TEG Dehydration Basis table |
| Outlet water content | Not more than 4 lb H2O/MMSCF | SEC-05 / TEG Dehydration Basis table |
| Contactor turndown | 3:1 TBC | SEC-05 / TEG Dehydration Basis table |
| Regeneration turndown | 2:1 | SEC-05 / TEG Dehydration Basis table |
| H2S in process gas (compressor composition) | Approximately 0.296 mol% | SEC-05 / Compression Design Conditions |

## Conditions

| Condition | Value | Source Reference |
|---|---|---|
| Upstream interface | Second-stage compressor discharge at 800 psig under SCA-002 basis | SEC-05 / Compression Design Conditions |
| Downstream interface | Compressed sour gas export to 04-25 Deep Cut Gas Plant inlet system | SEC-05 / TEG Dehydration Basis; DBM facility narrative |
| Flash gas routing | Pressure-regulated to 04-25 SOC first-stage suction under current SCA basis | SEC-05 / TEG Package Equipment |
| Contactor blowdown | Automated to HP flare | SEC-05 / TEG Dehydration Basis |
| Hydrocarbon liquids (flash drum) | Manual drain to produced-water drain | SEC-05 / TEG Package Equipment |
| Makeup tank | Atmospheric, fuel-gas blanketed, heated/insulated, not connected to VRU | SEC-05 / TEG Package Equipment |
| LP flare consumers (regeneration) | TEG regeneration routes to LP flare via LP KO drum V-3900-2 | SEC-08 utility narrative |
| Fuel-gas user | TEG stripping is a listed LP fuel-gas user | Utility Integration Basis |
| Produced water contaminants involving TEG | TEG identified among produced water contaminants in current source set | SEC-05 / SEC-06 narrative |

## Construction — Major Equipment in TEG Package

(Source: SEC-05 "TEG Package Equipment")

| Equipment Item | Configuration / Notes | Source Reference |
|---|---|---|
| Inlet filter coalescer | 1 x 100 percent; manual bypass and isolation; manual blowdown at coalescer | SEC-05 / TEG Package Equipment |
| Contactor | Structured packed, at least three theoretical stages; Fs not more than 3.0; inlet and outlet demisters required; 1 x 100 percent | SEC-05 / TEG Dehydration Basis; Equipment Count Table |
| Level pot | Listed in TEG package equipment | SEC-05 / TEG Package Equipment |
| Contactor blowdown valve | Automated to HP flare | SEC-05 / TEG Dehydration Basis |
| Cooler (lean TEG cooler) | Listed in TEG package equipment | SEC-05 / TEG Package Equipment |
| Flash drum | Separates hydrocarbon vapour, water vapour, and TEG; flash gas to 04-25 SOC first-stage suction | SEC-05 / TEG Package Equipment |
| Solids filters (full-flow) | 5 micron full-flow rich TEG solids filtration | SEC-05 / TEG Package Equipment |
| Charcoal filter (carbon/particle) | 20 percent slipstream through carbon/particle filtration | SEC-05 / TEG Package Equipment |
| Lean/rich exchanger | Listed in TEG package equipment | SEC-05 / TEG Package Equipment |
| Rich TEG solids filter | Listed in TEG package equipment | SEC-05 / TEG Package Equipment |
| TEG pumps | 2 x 100 percent rotary gear or positive-displacement pumps; single mechanical seals | SEC-05 / TEG Package Equipment; Equipment Count Table |
| Still column | Listed in TEG package equipment | SEC-05 / TEG Package Equipment |
| Stripping column | Listed in TEG package equipment | SEC-05 / TEG Package Equipment |
| Reflux condenser | Listed in TEG package equipment | SEC-05 / TEG Package Equipment |
| Reboiler | Uses LP fuel gas for stripping per utility basis | SEC-05; Utility Integration Basis |
| Surge drum | 30 minutes retention at 50 psig | SEC-05 / TEG Package Equipment |
| Regen cooler | Listed in TEG package equipment | SEC-05 / TEG Package Equipment |
| Regen overhead scrubber | Listed in TEG package equipment | SEC-05 / TEG Package Equipment |
| Regen overhead pumps | Listed in TEG package equipment | SEC-05 / TEG Package Equipment |
| Makeup tank | Atmospheric, fuel-gas blanketed, heated/insulated, not connected to VRU | SEC-05 / TEG Package Equipment |
| Makeup pump | Listed in TEG package equipment | SEC-05 / TEG Package Equipment |

Equipment-level mechanical sizing details (vessel diameters, heights, MAWP/MDMT, materials, head types, internals manufacturer) are TBD pending vendor engineering; source does not enumerate vessel-level mechanical design at this stage.

## Scope Coverage

This vendor production unit covers SOW items: SOW-0237, SOW-0238, SOW-0239, SOW-0240 (per `_CONTEXT.md`). Specific SOW row text TBD (source slice not extracted into the deliverable folder).

## References

- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` — SEC-05 (Inlet Compression and Sour-Gas Dehydration), Utility Integration Basis, Equipment Count Table
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` — row DEL-068-04
- `_Sources/26020-Package_Requirements.docx` — package heading 23 (location TBD; binary not directly readable in this run)
- `_Sources/26020-Packages_Interfaces_4_export.xlsx` — Packages row 97 (location TBD; binary not directly readable)
