# Datasheet — DEL-088-02 Package Datasheet (Caustic Treating, Condensate Mercaptan Removal)

`epistemic-status: DRAFT (Pass 1+2)`

## Identification

| Field | Value | Provenance |
|---|---|---|
| DeliverableID | `DEL-088-02_package-datasheet` | `_CONTEXT.md` |
| ParentPackageID | `PKG-088` | `_CONTEXT.md` |
| Package Tag | `26020-02-PT-27-001` | PACKAGE_REGISTER.csv (PKG-088 row) |
| Package Name | Caustic Treating (Condensate Mercaptan Removal) | `_CONTEXT.md`; PACKAGE_REGISTER.csv |
| Discipline | Mechanical | `_CONTEXT.md`; PACKAGE_REGISTER.csv |
| WBS | 02 | PACKAGE_REGISTER.csv (PKG-088) |
| Type | EPC Package Datasheet | `_CONTEXT.md` |
| Responsible Party | EPC Integrator | `_CONTEXT.md` |
| Vendor Reference (budgetary go-by) | Millenia Proposal 7304 Rev. 0 | PACKAGE_REGISTER.csv source-basis field |

## Attributes

| Attribute | Value | Provenance |
|---|---|---|
| Treating technology | Non-regenerative caustic mercaptan treating (Merichem or equivalent) | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` §"Condensate Mercaptan Treating" |
| Feed | Stabilized C5+ condensate returned from 04-25 MPFS/stabilization to the 03-25 Liquids Hub | DBM §Overview; §"Products and Downstream Routing" |
| Treating capacity | 20,000 bbl/d C5+ | DBM §"Condensate Mercaptan Treating" |
| Regeneration | Not included in 03-25 basis | DBM §"Condensate Mercaptan Treating" |
| DSO entrainment — expected | 30 ppmw S | DBM §"Condensate Mercaptan Treating" |
| DSO entrainment — design | 50 ppmw S (TBC vendor) | DBM §"Condensate Mercaptan Treating" |
| Extractable compounds | H2S, CO2, methyl/ethyl/propyl/butyl mercaptans | DBM §"Condensate Mercaptan Treating" |
| Volatile mercaptan species in basis | Methyl mercaptan; ethyl mercaptan; dimethyl sulphide; 2-propanethiol; n-propyl mercaptan; methyl ethyl sulphide (low/high values TBC where not provided) | DBM §"Products and Downstream Routing" |
| Caustic solution basis | 50 wt% NaOH/H2O; SG 1.75 (TBC) | DBM §"Condensate Mercaptan Treating" |

## Conditions

| Condition | Value | Provenance |
|---|---|---|
| Fresh & spent caustic tank type | Atmospheric 32 oz tanks with LP fuel-gas blanket, heating, and insulation | DBM §"Condensate Mercaptan Treating" |
| Spent caustic tank venting | Through flame arrestor to incinerator header; supports truck-out | DBM §"Condensate Mercaptan Treating" |
| Fresh caustic VRU connection | Fresh caustic is NOT connected to VRU | DBM §"Condensate Mercaptan Treating" |
| Aluminum prohibition | Aluminum SHALL NOT be used in caustic building | DBM §"Condensate Mercaptan Treating" |
| Caustic tank material / coating | TBC | DBM §"Condensate Mercaptan Treating" (explicit TBC) |
| Instrument-air — caustic oxidation demand | 214 SCFM TBC | DBM §"Instrument Air" |
| LP fuel-gas service to package | Caustic treating overhead dilution and enrichment-gas service from LP fuel gas | DBM §"Fuel Gas" preamble (caustic treating listed under LP fuel-gas users) |
| Operating temperature / pressure | TBD (not stated in accessible source slice) | TBD — vendor datasheet not locally accessible |
| Spent caustic disposition | Truck-out from spent caustic tank (off-site disposal route TBD) | DBM §"Condensate Mercaptan Treating" |
| DSO disposition | DSO tank included in package; downstream routing TBD | DBM §"Condensate Mercaptan Treating" |

## Construction

| Construction Item | Description | Provenance |
|---|---|---|
| Major equipment included in package | Caustic C5+ contactor; pre-heater; caustic outlet filter; water wash; DSO tank; spent-caustic tank; fresh-caustic tank; fresh-water tank | DBM §"Condensate Mercaptan Treating" |
| Interfaces to facility — incinerator | Overhead, dilution, and enrichment-gas tie-ins to the incinerator | DBM §"Condensate Mercaptan Treating" |
| Interfaces to facility — utilities | LP fuel-gas blanket/heating for caustic tanks; instrument air for caustic oxidation; sweetened condensate routing to product storage | DBM §"Condensate Mercaptan Treating"; §"Instrument Air"; §"Fuel Gas" |
| Applicable interface types (package scope) | Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports | PACKAGE_REGISTER.csv (PKG-088 "Applicable interface types") |
| Vendor responsibility | Package engineering, package design, vendor documentation, physical equipment package | PACKAGE_REGISTER.csv (PKG-088 narrative) |
| EPC Integrator responsibility | Integration into the functional process facility — interfaces, tie-ins, constructability, procurement/construction coordination, facility-level integration | PACKAGE_REGISTER.csv (PKG-088 narrative) |

## References

- `_REFERENCES.md` (deliverable-local)
- `_CONTEXT.md` (deliverable-local)
- PACKAGE_REGISTER.csv — Gate 7 snapshot, PKG-088 row
- DELIVERABLE_REGISTER.csv — Gate 7 snapshot, DEL-088-02 row
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` — §"Condensate Mercaptan Treating"; §"Products and Downstream Routing"; §"Instrument Air"; §"Fuel Gas"
- `_Sources/26020-Package_Requirements.docx` package heading 41 — referenced by `_CONTEXT.md` and PACKAGE_REGISTER.csv; ASSUMPTION: not locally readable in markdown form (binary `.docx`); package-section detail therefore deferred to TBD where DBM does not provide coverage
- `_Sources/26020-Packages_Interfaces_4_export.xlsx` — referenced by decomposition; ASSUMPTION: not locally readable in plain text; specific interface rows deferred to TBD
