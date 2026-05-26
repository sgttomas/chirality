# Specification: DEL-055-03 — Construction Work Package (LP Flare KO Drum, 4-25)

## Scope

### In Scope

This Construction Work Package (CWP) covers the EPC Integrator activities required to physically install, construct, inspect, turn over, and integrate package PKG-055 (one LP flare knock-out drum V-3900-1 and one LP flare KO drum transfer pump P-3900-1; vendor package tag 26020-01-PT-17-003) into the West Doe Deepcut (4-25) facility. — Sources: `_CONTEXT.md`; PACKAGE_REGISTER.csv row PKG-055; DBM-Deepcut/4-25_Deepcut_DBM.md line 2029.

The CWP covers, at minimum:

- Receiving, setting, and anchoring of the vendor-supplied package skid/vessel and transfer pump.
- Tie-in to the LP flare relief header (508 mm / 20 in) and to all listed interface types: Process Piping; Relief/Flare/Vent; Drain/Containment; Electrical Power; EHT; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Maintenance Access; Structural/Foundations/Supports. — PACKAGE_REGISTER.csv row PKG-055.
- Installation of LP KO drum pump discharge truck-out and low-pressure-header return paths. — DBM line 2029, 1665.
- Electrical heat tracing and insulation of LP flare header sections outside heated buildings, with PSV outlets free-draining into the header (no traps or pockets). — DBM line 2033, 1787.
- Construction interface checklists, workface plans, mechanical-completion punch lists, and turnover documentation handover to commissioning. — `_CONTEXT.md` Anticipated Artifacts.

### Exclusions

- Package engineering, package design, vendor documentation, and physical equipment fabrication — owned by the Package Vendor (covered by DEL-055-04 and DEL-055-05). — PACKAGE_REGISTER.csv row PKG-055.
- Flare stack thermal-radiation regulatory verification — referenced in DBM Sec. 8 and called out as requiring verification during detailed design, not by this CWP. — DBM lines 285-286, 289.
- Specific package-level exclusions: `TBD; no package-specific exclusions stated in source materials.` — PACKAGE_REGISTER.csv row PKG-055.

## Requirements

| ID | Requirement | Source / Authority |
|---|---|---|
| R-CWP-01 | The CWP shall install V-3900-1 and P-3900-1 in accordance with the vendor package drawings and the EPC integration design package. | PACKAGE_REGISTER.csv row PKG-055 (EPC integration ownership). |
| R-CWP-02 | LP flare relief header tie-in shall be 508 mm (20 in) nominal size as defined by the DBM. | DBM-Deepcut line 2029. |
| R-CWP-03 | LP flare header sections outside heated buildings shall be electrically heat traced and insulated for freeze protection. PSV outlets that free-drain into the flare header are exempt from heat tracing per DBM. | DBM-Deepcut line 2033. |
| R-CWP-04 | VRU suction-header-to-flare bypass piping shall be installed in the pipe rack such that the header free-drains without traps or pockets and slopes toward the LP flare KO drum. | DBM-Deepcut line 1787. |
| R-CWP-05 | KO drum location shall maintain ≥10 m (32 ft) from vegetation or other fire hazards. | DBM-Deepcut line 287 (OGAOM Sec. 9.6.15). |
| R-CWP-06 | All interface types listed in the package register (Process Piping; Relief/Flare/Vent; Drain/Containment; Electrical Power; EHT; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Maintenance Access; Structural/Foundations/Supports) shall be physically completed, tested, and signed off via interface punch lists prior to turnover. | PACKAGE_REGISTER.csv row PKG-055. |
| R-CWP-07 | LP KO drum pump (P-3900-1) discharge routing shall include the truck-out connection and the low-pressure-header path to the condensate slop tank, per DBM. | DBM-Deepcut lines 1665, 2029. |
| R-CWP-08 | Construction shall maintain mechanical integrity documentation (welder qualifications, NDE records, pressure-test records, alignment records, torque records) for handover to commissioning. | ASSUMPTION (standard EPC CWP practice); explicit source slice `TBD` (`26020-Package_Requirements.docx` heading 10 not accessible). |
| R-CWP-09 | A construction interface and turnover checklist shall be produced as part of this deliverable. | `_CONTEXT.md` Anticipated Artifacts. |
| R-CWP-10 | An installation and tie-in workface plan shall be produced as part of this deliverable. | `_CONTEXT.md` Anticipated Artifacts. |

## Standards / Governing References

| Reference | Applicability | Local accessibility |
|---|---|---|
| West Doe Deepcut DBM (4-25) | Governing basis-of-design for facility identity, flare system architecture, spacing, and tie-in sizing. | Accessible: DBM-Deepcut/4-25_Deepcut_DBM.md |
| OGAOM Sec. 9.6.15 (Alberta/BC Oil and Gas Activities Operations Manual, flare/incinerator spacing) | Spacing requirements between flare/KO drums and vegetation, roads, tanks. | Cited via DBM; not directly read in this run — location TBD. |
| OGPFR Appendix 1, Schedule 1, Sec. 2 (thermal-radiation flux) | Flare thermal-radiation boundary criteria. | Cited via DBM; not directly read — location TBD. |
| API 2510 (pressurized bullets spacing) | Distance from flare to pressurized bullets. | Cited via DBM; not directly read — location TBD. |
| 26020-Package_Requirements.docx, heading 10 | Project-specific package requirements for this LP KO drum package. | Inaccessible in this run; required clauses are `TBD`. |

## Verification

| Requirement | Verification Method | Records |
|---|---|---|
| R-CWP-01 | Inspection vs. vendor IFC drawings; mechanical-completion walkdown | Mechanical-completion punch list; ITR records |
| R-CWP-02 | Visual inspection; isometric/spool verification; tie-in NDE per piping spec | Piping NDE records; weld map; tie-in punch list |
| R-CWP-03 | EHT continuity test; insulation inspection | EHT commissioning report; insulation QC report |
| R-CWP-04 | Slope verification (level/laser shot); free-drain walkdown | Piping QC slope record |
| R-CWP-05 | Surveyed location vs. plot plan | As-built plot plan; survey report |
| R-CWP-06 | Interface punch list closeout for each interface type | Signed interface checklist per discipline |
| R-CWP-07 | Hydro/pneumatic test of pump discharge piping; routing walkdown | Pressure-test record; routing punch list |
| R-CWP-08 | QA/QC audit of mechanical-integrity documentation pack | Welder logs; NDE reports; pressure-test reports; alignment/torque records |
| R-CWP-09 | Document review and sign-off | Turnover checklist deliverable |
| R-CWP-10 | Document review and sign-off | Workface plan deliverable |

## Documentation (Required Artifacts)

- Construction work package document (this deliverable's primary artifact).
- Installation and tie-in workface plan.
- Construction interface checklist (one per interface type listed in R-CWP-06).
- Turnover (mechanical-completion) checklist with punch list rollup.
- Supporting QC/QA records package (NDE, pressure tests, EHT, alignment, surveys).

Source: `_CONTEXT.md` Anticipated Artifacts; PACKAGE_REGISTER.csv row PKG-055.
