# Datasheet — Vendor Engineered Equipment Package (DEL-091-04)

ProvenanceMode: deliverable-local
EpistemicDefault: FACT only when cited; otherwise TBD or ASSUMPTION

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-091-04_vendor-engineered-equipment-package` |
| Name | Vendor Engineered Equipment Package |
| ParentPackageID | `PKG-091` |
| PackageName | Tank Farm Pump Building 3-25 |
| Discipline | Mechanical |
| Type | Vendor Package Production Unit |
| ResponsibleParty | Package Vendor (engineering / design / equipment) with EPC Integrator integration review |
| WBS | 03 |
| Source Tag | 26020-03-PT-18-002 - Tank Farm Pumps |

## Attributes

Major equipment included in the vendor-engineered package (PKG-091 scope as stated in PACKAGE_REGISTER row 84 and the 3-25 DBM):

| Tag/Service | Quantity / Type | Source |
|---|---|---|
| Building drain pump | 1 — pneumatic diaphragm | PACKAGE_REGISTER row 84 (PKG-091); 26020-Package_Requirements.docx heading 44 |
| Water transfer pumps | 2 — radial centrifugal, parallel, pulling from produced-water tanks through bag filter to produced-water pipeline | PACKAGE_REGISTER row 84; DBM 3-25 line 429 (`2 x 100 percent` produced-water transfer pumps) |
| Sour condensate pumps | 2 — vertical inline centrifugal, move sour condensate from sour condensate storage tanks to condensate sweetening feed pumps | PACKAGE_REGISTER row 84 |
| Condensate sweetening feed pumps | 2 — vertical inline centrifugal | PACKAGE_REGISTER row 84 |

Detailed mechanical attributes (head, flow, NPSHa/NPSHr, motor sizing, seal plan, materials of construction, API/ANSI compliance class): `TBD` — not present in locally accessible source slices; carried by the vendor design basis once issued.

## Conditions

| Field | Value | Source |
|---|---|---|
| Site | LSD 03-25-80-15 W6M, north of Dawson Creek, BC; elevation 673 m AMSL | DBM 3-25 lines 12, 85, 89 |
| Service environment | Sour service; produced water and sour/sweet condensate streams; tank-farm exterior service inside a self-framing pump building | DBM 3-25 lines 20, 22, 184, 376–417 |
| Produced-water service basis | 3-25 sour produced water reference: 3,600 m3/d at 10 °C, 150 kPag | DBM 3-25 line 188 |
| Condensate hub throughput | 3,180 m3/d (20,000 bbl/d) stabilized condensate | DBM 3-25 line 376 |
| Sweetening feed condition | Caustic non-regenerative mercaptan treating, 20,000 bbl/d throughput (sets sweetening feed pump duty) | DBM 3-25 line 389 |
| Design temperature/pressure ratings (per pump) | `TBD` (vendor design basis) |
| Area classification, seismic, wind | `TBD` (vendor design basis) |
| Power supply | Electrical Power interface to vendor package — voltage class, motor starter type, VFD requirements `TBD` | PACKAGE_REGISTER row 84 (Electrical Power interface) |
| Building HVAC / services | Building HVAC / Services listed as applicable interface — vendor scope split `TBD` | PACKAGE_REGISTER row 84 |

## Construction

- ASSUMPTION: Pump building is a self-framing modularized package suitable for shop assembly and field set, consistent with 3-25 compressor-package construction philosophy. Confirmation against the Tank Farm Pump Building 3-25 vendor RFQ (`26020-03-PT-RFQ-18-002-Tank Farm Pumps.docx`) `TBD` — RFQ document not locally accessible.
- Major included equipment: see Attributes table.
- Vendor scope split (engineering, design, fabrication/supply, equipment supply) vs. EPC Integrator scope (integration into facility, interfaces, tie-ins, constructability): vendor owns package engineering, package design, vendor documentation, and physical equipment package; EPC Integrator owns facility-level integration and interface management. Source: PACKAGE_REGISTER row 84 (PKG-091).
- Applicable package interface types (vendor must coordinate at the package boundary): Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; Cathodic Protection; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports. Source: PACKAGE_REGISTER row 84.
- Materials of construction, coatings, insulation, EHT classes, fire & gas detection, structural design loads: `TBD` (vendor design basis).

## References

- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` (deliverable-local)
- PROJECT_DECOMP Gate 7 snapshot, `PACKAGE_REGISTER.csv` row 84 (PKG-091)
- PROJECT_DECOMP Gate 7 snapshot, `DELIVERABLE_REGISTER.csv` row 471 (DEL-091-04)
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (lines 7, 20–22, 40, 184–188, 376–417, 429)
- `_Sources/26020-Package_Requirements.docx` package heading 44 — `location TBD` (file not converted/locally readable; source slice not consulted)
- `_Sources/26020-Packages_Interfaces_4_export.xlsx` row 84 (Packages tab) — `location TBD` (not extracted to text)
- `Bid Docs/Budgetary/26020-03-PT-RFQ-18-002-Tank Farm Pumps.docx` — `location TBD` (not locally accessible in `_Sources`)
