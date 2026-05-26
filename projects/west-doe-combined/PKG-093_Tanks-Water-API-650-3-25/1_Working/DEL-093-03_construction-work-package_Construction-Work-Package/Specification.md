# Specification — DEL-093-03 Construction Work Package (PKG-093)

> Normative requirements for the EPC Construction Work Package deliverable that governs how PKG-093 (two 3,800 bbl API 650 sweet produced-water storage tanks, TK-9060-2 and TK-9070-2) will be physically installed, inspected, turned over, and integrated into the 03-25 facility.

## Scope

In scope:
- Construction Work Package narrative covering site receipt, erection, hydrotesting, inspection, mechanical completion, and turnover for the two sweet produced-water tanks (TK-9060-2, TK-9070-2) and their package-side equipment (PACKAGE_REGISTER.csv row PKG-093).
- Installation and tie-in workface plan covering the nine declared package interface types: Process Piping; Relief/Flare/Vent; Drain/Containment; Grounding/Bonding; Area/Exterior Lighting; Cathodic Protection; I&C/Control Cabling; Grading/Site Drainage/Spill Containment; Structural/Foundations/Supports (PACKAGE_REGISTER.csv row PKG-093).
- Construction interface and turnover checklist evidencing mechanical completion and EPC acceptance of vendor-supplied package equipment.

Out of scope:
- Package engineering, package design, and vendor documentation for the physical equipment package — these are Package Vendor scope (PACKAGE_REGISTER.csv row PKG-093).
- Operating procedures for the produced-water system once handed over to operations.
- Detailed design of the H2O2 treatment package (separate equipment; see DBM produced-water section).

## Requirements

| Req ID | Requirement | Basis / Source |
|---|---|---|
| R-093-03-01 | The Construction Work Package shall identify the two sweet produced-water storage tanks TK-9060-2 and TK-9070-2 by tag and indicate they are 3,800 bbl each. | PACKAGE_REGISTER.csv row PKG-093 |
| R-093-03-02 | Tank shell, bottom, and roof erection shall conform to API 650. (Clause-level acceptance criteria TBD — `location TBD` in 26020-Package_Requirements.docx package heading 45.) | PACKAGE_REGISTER.csv row PKG-093; ASSUMPTION on clause set |
| R-093-03-03 | Foundations and tank-pad design shall accommodate the facility design basis of -40 deg C minimum ambient and tank design SG 1.25 (TBC). | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` Site Basis; Raw Gas and Water Design Conditions |
| R-093-03-04 | Construction shall provide tie-ins for all nine declared interface types listed in PKG-093 (process piping; relief/flare/vent; drain/containment; grounding/bonding; area lighting; CP; I&C cabling; grading/drainage/spill containment; structural/foundations/supports). | PACKAGE_REGISTER.csv row PKG-093 |
| R-093-03-05 | A Construction Interface and Turnover Checklist shall be produced; each item closed with documented evidence prior to mechanical-completion turnover. | DELIVERABLE_REGISTER.csv row DEL-093-03 (artifact list) |
| R-093-03-06 | Hydrostatic testing of each tank shall be performed per API 650 prior to insulation, coating finish, and tie-in commissioning. | ASSUMPTION (API 650 conventional requirement); clause `location TBD` |
| R-093-03-07 | Settlement survey shall be performed during and after hydrotest; acceptance limits per API 650 (`location TBD`). | ASSUMPTION; clause `location TBD` |
| R-093-03-08 | Containment, drainage routing, and spill containment shall be installed and turned over consistent with the package's declared drain/containment and grading/spill-containment interfaces. | PACKAGE_REGISTER.csv row PKG-093 |
| R-093-03-09 | Cathodic protection and grounding/bonding interfaces shall be installed, tested, and recorded prior to mechanical completion. | PACKAGE_REGISTER.csv row PKG-093 |
| R-093-03-10 | The Construction Work Package shall identify and resolve EPC/Vendor split-of-supply items at every tie-in (terminal connection point) and record them in the Construction Interface Register entries for PKG-093. | PACKAGE_REGISTER.csv row PKG-093 (boundary statement) |
| R-093-03-11 | All exposed package equipment, instrumentation, panels, and field devices in scope of this construction work package shall be specified, installed, and protected for the -40 deg C minimum ambient unless a more severe process or vendor condition applies. | DBM Site Basis |

Requirements R-093-03-02, R-093-03-06, and R-093-03-07 are flagged ASSUMPTION pending text-accessible review of 26020-Package_Requirements.docx package heading 45 and/or API 650.

## Standards

| Standard | Applies To | Location |
|---|---|---|
| API 650, Welded Tanks for Oil Storage | Tank fabrication, erection, hydrostatic test, inspection, settlement survey | location TBD (clause-level slice not text-accessible this run) |
| 26020-Package_Requirements.docx package heading 45 | Package-specific scope/requirements for PKG-093 | binary source; location TBD |
| NBCC 2020 (Dawson Creek IDF) | Civil drainage and surface-water management for tank pad area | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` Site Basis |
| Site basis (cold climate, -40 deg C) | Winterization, heat tracing, materials | DBM Site Basis |

## Verification

| Req | Verification approach |
|---|---|
| R-093-03-01 | Document review against PKG-093 register; tag check on shop drawings and as-built tank nameplates. |
| R-093-03-02 | Inspection records per API 650 (welder qualifications, NDE, hydrotest); clause-level checklist TBD. |
| R-093-03-03 | Geotech and foundation design review records; cold-weather concrete plan. |
| R-093-03-04 | Tie-in punch list complete and signed in Construction Interface and Turnover Checklist. |
| R-093-03-05 | Signed checklist on file prior to mechanical completion. |
| R-093-03-06 | Hydrotest report (volume, duration, acceptance) per API 650. |
| R-093-03-07 | Survey reports during fill, after fill, after drain; acceptance per API 650 (TBD). |
| R-093-03-08 | Walkdown record of containment and drainage; commissioning checks. |
| R-093-03-09 | CP commissioning record; ground-resistance test results. |
| R-093-03-10 | Construction Interface Register entries closed with EPC/Vendor sign-off. |
| R-093-03-11 | Cold-weather equipment specification review; heat-tracing commissioning record. |

## Documentation

The deliverable shall produce the following documented artifacts (per DELIVERABLE_REGISTER.csv row DEL-093-03):

- Construction Work Package narrative
- Installation and Tie-in Workface Plan
- Construction Interface and Turnover Checklist

Supporting records expected during execution:

- Hydrotest record per tank
- Settlement survey records
- Weld and NDE inspection records (API 650 scope)
- CP commissioning record
- Grounding/bonding test record
- Foundation pour and cold-weather concrete records
- Tie-in punch list and as-built mark-ups
