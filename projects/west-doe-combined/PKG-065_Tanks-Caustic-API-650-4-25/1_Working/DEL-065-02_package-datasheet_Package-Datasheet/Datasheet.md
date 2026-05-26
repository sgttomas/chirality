# Datasheet — DEL-065-02 Package Datasheet (PKG-065 Tanks, Caustic (API 650) 4-25)

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | DEL-065-02_package-datasheet | _CONTEXT.md |
| Name | Package Datasheet | _CONTEXT.md |
| ParentPackageID | PKG-065 | _CONTEXT.md |
| Package Name | Tanks, Caustic (API 650) 4-25 | _CONTEXT.md |
| Facility | West Doe Deepcut expansion, 04-25 | DBM-Deepcut/4-25_Deepcut_DBM.md §1 (lines 5-22) |
| Discipline | Mechanical | _CONTEXT.md |
| Type | EPC Package Datasheet | _CONTEXT.md |
| Responsible Party | EPC Integrator | _CONTEXT.md |
| Governing Code (package title) | API 650 | _CONTEXT.md / package title; ASSUMPTION the package-title "API 650" governs caustic tank shell design |
| Source basis | Workbook Packages row 87; 26020-Package_Requirements.docx package heading 20 (location TBD — binary source not locally accessible) | _REFERENCES.md |

## Attributes (Equipment in Package)

The package contains two atmospheric caustic tanks serving the NGL non-regenerative caustic treating (Mercaptan Treating Unit, MTU). Quantities and service per `4-25_Deepcut_DBM.md` §"NGL Mercaptan Treating" (lines 1511-1566) and §"Disulphide Oil, Spent Caustic, and Waste Amine" (lines 526-532).

| Tag/Item | Service | Quantity | Nominal Size | Source |
|---|---|---|---|---|
| Fresh caustic storage tank | Fresh 50 wt% NaOH receipt/storage; truck-in capable | 1 | 400 bbl | DBM §MTU (line 1528, 1562) |
| Spent caustic storage tank | Spent caustic accumulation; truck-out for off-site disposal | 1 | 400 bbl | DBM §MTU (line 1529); §Spent Caustic (line 530) |
| Tag numbers | TBD | — | — | Not locally available in DBM; obtain from equipment list (location TBD) |

## Conditions (Process / Design Basis)

| Attribute | Value | Source |
|---|---|---|
| Service fluid (fresh) | 50 wt% NaOH (sodium hydroxide) | DBM §MTU line 1526 |
| Service fluid (circulating) | 14.7 wt% NaOH, to be confirmed | DBM §MTU line 1527 |
| Service fluid (spent) | Spent NaOH solution (contains absorbed mercaptans / sulphide species) | DBM §MTU lines 1511-1513 |
| Fresh caustic tank design specific gravity | 1.75 (TBC) | DBM §MTU line 1562 |
| Spent caustic tank design SG | TBD | Not stated in DBM |
| Operating temperature | Heated; minimum downstream caustic solution 80 degF (26.7 degC) referenced at deethanizer bottoms cooler | DBM line 1338, 1552 (caustic freeze/crystallization risk) |
| Storage location | Indoors (within or adjacent to MTU building) — caustic-containing equipment segregated | DBM line 1552 |
| Tank type | Atmospheric, heated, insulated | DBM line 1562 |
| Fresh caustic tank vapour space | Fuel-gas blanket; NOT connected to VRU header (to avoid VRU vapour contamination) | DBM line 1562 |
| Spent caustic tank vapour space | Low-pressure fuel-gas blanket; vent connected to incinerator header; flame arrestor backflash protection | DBM line 1562 |
| Maximum fill | TBD (DBM produced-water tank rule of 90% w/ thermal expansion review is not necessarily applicable to caustic; ASSUMPTION-eligible if extended) | DBM line 519 (produced-water context only) |
| Design code (shell) | API 650 | Package title (governing code per package designation); location TBD in 26020-Package_Requirements.docx heading 20 |
| Atmospheric tank spacing basis | NFPA 30 Table 22.4.2.1 (between atmospheric tanks 2.35 m / 7.72 ft); other separations per OGAOM §9.6.15 and API 2510 | DBM lines 265-298 |

## Construction (Materials, Coatings, Appurtenances)

| Item | Requirement | Source |
|---|---|---|
| Tank material | Polymer or other caustic-compatible material; specific selection is a detailed-engineering TBD | DBM line 1566 |
| Prohibited materials | No aluminum within the caustic building | DBM line 1566 |
| Insulation cladding / straps in caustic exposure areas | Stainless steel | DBM line 1566 |
| Heating | Required (caustic freezing/crystallization risk) | DBM line 1552, 1562 |
| Insulation | Required (external) | DBM line 1562 |
| Pressure / vacuum protection | PVRV per tank (read across from produced-water tank basis line 524; ASSUMPTION as applied to caustic tanks pending detailed engineering); EPRV sizing review during DE | DBM line 524 (produced-water analogy — ASSUMPTION for caustic) |
| Spent caustic backflash protection | Flame arrestor on incinerator-header tie-in | DBM line 1562 |
| Truck loading/unloading | Fresh tank: truck-in capable. Spent tank: truck-out capable. | DBM line 1562 |
| Building floor material | Detailed-engineering TBD | DBM line 1566 |
| Safety showers | Required in MTU building; quantity and location TBD; discrete control-room alert on activation required | DBM line 1552 |

## References

- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (locally accessible) — §"NGL Mercaptan Treating Unit", §"Disulphide Oil, Spent Caustic, and Waste Amine", §"Atmospheric Tank and General Plant Spacing"
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/26020-Package_Requirements.docx` heading 20 — binary; NOT locally readable as text; content marked `location TBD` where it would govern
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/26020-Packages_Interfaces_4_export.xlsx` — binary; NOT locally readable as text; interface matrix items marked `location TBD`
- Decomposition GATE-07 snapshot: deliverable, package, objective-deliverable, interface, and artifact registers
- API 650 (atmospheric tank design code) — governing standard per package title; full text not locally available; `location TBD`
- NFPA 30, API 2510, OGAOM §9.6.15 — separation/spacing basis cited via DBM
