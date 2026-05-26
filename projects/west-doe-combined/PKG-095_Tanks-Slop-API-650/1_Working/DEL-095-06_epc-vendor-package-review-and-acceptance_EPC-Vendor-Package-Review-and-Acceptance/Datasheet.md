# Datasheet — DEL-095-06 EPC Vendor Package Review and Acceptance (Tanks, Slop / API 650 / PKG-095)

> **Document type:** Descriptive datasheet for the EPC Integrator review-and-acceptance deliverable for the PKG-095 Tanks, Slop (API 650) vendor package.
> **Authority basis:** Grounded in the Gate 7 PROJECT_DECOMP snapshot, `_CONTEXT.md`, and the locally accessible 03-25 DBM source slice (`_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`).

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-095-06_epc-vendor-package-review-and-acceptance` | `_CONTEXT.md` |
| Name | EPC Vendor Package Review and Acceptance | `_CONTEXT.md` |
| ParentPackageID | `PKG-095` | `_CONTEXT.md` |
| ParentWorkbookID | 95 | `_CONTEXT.md` |
| PackageName | Tanks, Slop (API 650) | `_CONTEXT.md` |
| Discipline | Mechanical | `_CONTEXT.md` |
| Type | EPC Vendor Package Acceptance | `_CONTEXT.md` |
| ResponsibleParty | EPC Integrator (lead) with Package Vendor input | `_CONTEXT.md` |
| Tag (package) | `26020-03-PT-19-004 - Tanks, Slop` | PACKAGE_REGISTER.csv (PKG-095) |
| Source Reference | Workbook Packages row 91; `26020-Package_Requirements.docx` package heading 47 | `_CONTEXT.md`; PACKAGE_REGISTER.csv |
| Covers Scope Items | SOW-0213; SOW-0214; SOW-0215; SOW-0216 | DELIVERABLE_REGISTER.csv |
| Supports Objectives | OBJ-002 through OBJ-010 | DELIVERABLE_REGISTER.csv (ASSUMPTION: package-heuristic mapping) |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Deliverable role | EPC-integrator review and acceptance evidence against EPC Scope of Work, Package Datasheet, and Construction Work Package | DELIVERABLE_REGISTER.csv (PKG-095 row) |
| Acceptance subject | Vendor-engineered slop tank package supplied under PKG-095 | PACKAGE_REGISTER.csv (PKG-095) |
| Slop service definition | One slop storage tank for off-spec condensate or contaminated hydrocarbon liquids requiring segregation from on-spec condensate product | PACKAGE_REGISTER.csv (PKG-095 description) |
| EPC ownership scope | Integration into the functional process facility; interfaces, tie-ins, constructability, procurement/construction coordination, facility-level integration | PACKAGE_REGISTER.csv (PKG-095) |
| Vendor ownership scope | Package engineering, package design, vendor documentation, physical equipment package | PACKAGE_REGISTER.csv (PKG-095) |
| Applicable interface types | Process Piping; Relief / Flare / Vent; Drain / Containment; Grounding / Bonding; Area / Exterior Lighting; Cathodic Protection; I&C / Control Cabling; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports | PACKAGE_REGISTER.csv (PKG-095) |
| Anticipated artifacts | Vendor document review log; package acceptance checklist; test/inspection evidence; turnover evidence | `_CONTEXT.md`; DELIVERABLE_REGISTER.csv |
| Tank-count basis (analog) | "one slop tank" within the 3-25 condensate storage allocation of eleven 3,800 bbl tanks | `3-25_Comp_and_Liquids_DBM.md` line 406 (ASSUMPTION: PKG-095 is a 3-25 analog; PKG-095 description does not duplicate the bbl size) |
| Related slop service receivers (3-25 basis) | LP fuel-gas scrubber V-3210-2 routes liquids to slop TK-9130-2; LP KO drum V-3900-2 pumps via P-3900-2 to slop; HP KO drum pumps P-4100-2 / P-4150-2 truck-out or transfer to slop | `3-25_Comp_and_Liquids_DBM.md` lines 463, 497, 499 |
| Package-specific exclusions | None stated in source materials (`TBD`) | PACKAGE_REGISTER.csv (PKG-095) |

## Conditions

| Condition | Value | Source / Status |
|---|---|---|
| Site minimum ambient (governs winterization / heat tracing applicability to slop tank) | -40 deg C | `3-25_Comp_and_Liquids_DBM.md` line 145 |
| Heat tracing / freeze protection applicability | Heat tracing supports winterization, freeze protection, tank and drain requirements | `3-25_Comp_and_Liquids_DBM.md` line 770 |
| Design code (datasheet-stated) | API 650 (per package name "Tanks, Slop (API 650)") | `_CONTEXT.md`; PACKAGE_REGISTER.csv |
| Design code (DBM analog) | API-650 Modified, atmospheric, externally insulated and heated, with Devchem 253 internal coating where defined for the produced-water tanks | `3-25_Comp_and_Liquids_DBM.md` line 421 (ASSUMPTION: produced-water tank class is the closest atmospheric-tank analog; slop-specific coating/insulation TBD) |
| Slop tank capacity (bbl) | TBD — DBM source slice does not state a slop-specific tank volume distinct from the 3,800 bbl condensate-tank class | `TBD` |
| Slop tank design SG | TBD | `TBD` |
| Operating/design pressure | TBD (atmospheric per analog) | ASSUMPTION |
| Operating/design temperature | TBD | `TBD` |
| Sour service applicability | TBD — slop receives off-spec condensate and routings from LP fuel-gas scrubber and KO drum systems; sour-service requirements for slop service are not explicitly stated in the available slice | `TBD` |

## Construction

| Item | Value | Source / Status |
|---|---|---|
| Tank type | Atmospheric (per API 650 designation and 3-25 analog) | `_CONTEXT.md`; ASSUMPTION |
| Insulation | External insulation (analog basis) | `3-25_Comp_and_Liquids_DBM.md` line 421 (ASSUMPTION) |
| Heating | Externally heated (analog basis); plus electrical heat tracing as winterization | `3-25_Comp_and_Liquids_DBM.md` lines 421, 770 (ASSUMPTION) |
| Internal coating | Devchem 253 for produced-water tank class; slop-tank coating remains TBD | `3-25_Comp_and_Liquids_DBM.md` line 421 (`TBD` for slop tank) |
| Foundation basis | Tank foundations to be designed against final geotechnical report and snow/wind/seismic / frost / vibration / settlement / maintenance-access criteria | `3-25_Comp_and_Liquids_DBM.md` lines 688, 700 |
| Drain / containment | Slop tank is a destination for slop and drain routing; segregated drain routing to slop / produced-water / caustic / TEG / flare KO systems as applicable | `3-25_Comp_and_Liquids_DBM.md` lines 656, 493 |
| Relief / vent | Vent and relief routing TBD against PKG-095 vendor package; relief interfaces are listed as applicable interface types | PACKAGE_REGISTER.csv (PKG-095); `TBD` |
| Grounding / bonding | Listed as an applicable interface type | PACKAGE_REGISTER.csv (PKG-095) |
| Cathodic protection | Listed as an applicable interface type | PACKAGE_REGISTER.csv (PKG-095); `3-25_Comp_and_Liquids_DBM.md` line 770 |
| Area lighting | Listed as an applicable interface type | PACKAGE_REGISTER.csv (PKG-095) |

## References

- `_CONTEXT.md` (this deliverable)
- `_REFERENCES.md` (this deliverable)
- `_DEPENDENCIES.md` (this deliverable)
- Gate 7 PROJECT_DECOMP snapshot: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
- `DELIVERABLE_REGISTER.csv` (DEL-095-06 row)
- `PACKAGE_REGISTER.csv` (PKG-095 row)
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (3-25 design basis memorandum; closest analog to PKG-095 slop service)
- Source pointers not locally accessible: `26020-Package_Requirements.docx` package heading 47; Workbook Packages row 91 (location TBD beyond the row/heading citation)
