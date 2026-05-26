# Specification — DEL-060-03 Construction Work Package

## Scope

This Construction Work Package (CWP) specifies the EPC Integrator-authored basis for physically installing, building, inspecting, turning over, and tying the PKG-060 Tank Farm Pump Building (facility 04-25) package into the larger West Doe Deepcut facility process, utility, electrical, controls, civil/structural, and safety systems (SourcePath: `_CONTEXT.md`; `PACKAGE_REGISTER.csv` PKG-060).

In scope:

- Installation, hookup, and tie-in of the vendor-supplied tank farm pump package: (2x) Water Transfer Pumps; (2x) Condensate Transfer Pumps; (1x) Condensate Recycle Pump with strainer; (2x) process water transfer pumps; (2x) fresh caustic transfer pumps; and the self-framing site-erected pump building (`SCOPE_LEDGER.csv` SOW-0191).
- Workface planning evidence connecting the package to adjacent process piping, utility piping, relief/flare/vent, drain/containment, electrical power, EHT, grounding/bonding, area/exterior lighting, cathodic protection, I&C/control cabling, building HVAC/services, fire & gas/safety systems, maintenance access, and structural/foundations/supports systems (`INTERFACE_REGISTER.csv` PKG-060 rows; `PACKAGE_REGISTER.csv` PKG-060 Applicable interface types).
- Construction interface, inspection, and turnover evidence supporting acceptance of the approved package by EPC Integrator and Owner (`ARTIFACT_REGISTER.csv` ART-4CE1B9B840).

Excluded (by source basis):

- Package engineering, design, vendor documentation, and the physical equipment package itself (assigned to the Package Vendor per `PACKAGE_REGISTER.csv` PKG-060; carried in DEL-060-04 and DEL-060-05).
- DCS integration, foundations, and electrical supply to the MCC are stated "by others" at the vendor boundary (`SCOPE_LEDGER.csv` SOW-0192); CWP coordinates these scopes but does not redefine their assignment.
- Detailed design of the construction tie-in interfaces beyond what the DBM and decomposition establish (TBD per discipline closeout).

## Requirements

| ReqID | Requirement | Source / Basis |
|---|---|---|
| REQ-CWP-01 | The CWP shall describe physical installation, build, inspection, turnover, and tie-in of PKG-060 into the larger facility systems. | `_CONTEXT.md` Scope; `DELIVERABLE_REGISTER.csv` DEL-060-03 description |
| REQ-CWP-02 | The CWP shall include the construction work package, the installation and tie-in workface plan, and the construction interface and turnover checklist as deliverable artifacts. | `_CONTEXT.md` Anticipated Artifacts; `ARTIFACT_REGISTER.csv` ART-F8F13A9988, ART-538DFF5CDE, ART-4CE1B9B840 |
| REQ-CWP-03 | The CWP shall assign Tourmaline field construction scope to grading/piling/foundations, module shipping/off-loading, setting modules and equipment on foundations, mechanical hookup, installation of shipped-loose components, home-run cable installation, electrical terminations, and area lighting, consistent with the DBM construction responsibility basis. | DBM-Deepcut SEC-01 Construction Responsibility |
| REQ-CWP-04 | The CWP shall flag interconnecting piping to ISBL/OSBL tie-in points as an external interface whose responsibility is to be confirmed per tie-in. | DBM-Deepcut SEC-01 |
| REQ-CWP-05 | The CWP shall require joint planning with the Package Vendor and Owner for tie-ins to existing or related facilities; tie-in timing shall be established as the project progresses. | DBM-Deepcut SEC-01 |
| REQ-CWP-06 | The construction interface and turnover checklist shall enumerate each applicable PKG-060 interface type from `INTERFACE_REGISTER.csv` (Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; Cathodic Protection; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports) and capture sign-off per interface. | `INTERFACE_REGISTER.csv` PKG-060 rows; `PACKAGE_REGISTER.csv` PKG-060 |
| REQ-CWP-07 | Construction execution shall be planned for design ambient conditions of -40 °C minimum / +35 °C maximum, with extreme ambient -49.2 °C / +38.9 °C considered for cold-weather construction restrictions. | DBM-Deepcut SEC-02.2 |
| REQ-CWP-08 | Construction electrical hookup shall reflect 575 V / 3 ph / 60 Hz motor supply from a 600 V MCC, DOL or VFD start, and local H-O-A or On-Off control at each pump, consistent with the package datasheet basis. | `SCOPE_LEDGER.csv` SOW-0192 |
| REQ-CWP-09 | Construction sequencing shall recognize that DCS integration, foundations, and electrical supply to the MCC are external to the package vendor scope and shall coordinate these with the EPC Integrator and Owner. | `SCOPE_LEDGER.csv` SOW-0192 |
| REQ-CWP-10 | Independent metering and mass-balance accountability shall be preserved for any facility interfaces installed by this CWP that cross facility boundaries (e.g., to 03-25 or existing-facility systems). | DBM-Deepcut SEC-01 Existing-Facility Interfaces and Metering |
| REQ-CWP-11 | Caustic-service pump installation shall preclude aluminium materials in installed interfacing components (gaskets, supports in contact with media, etc.). ASSUMPTION: extends the vendor "no aluminium" rule to the installed boundary. | `SCOPE_LEDGER.csv` SOW-0191 (ASSUMPTION on installation extension) |
| REQ-CWP-12 | Cold-weather construction methods shall be applied where ambient is below -19 °C (historical minimum), consistent with the design basis cold start condition. ASSUMPTION: practical threshold inferred from DBM historical minimum; exact threshold TBD. | DBM-Deepcut SEC-02.2 (ASSUMPTION) |

## Standards

| Standard / Reference | Applicability | Status |
|---|---|---|
| National Building Code of Canada 2020 (Dawson Creek IDF data basis) | Climate-data basis used in construction planning for the self-framing pump building. | Cited in DBM; clause-level requirements `location TBD` |
| API-682 seal plan 14/52 | Governs Condensate Transfer Pump seals; CWP shall verify installed configuration matches. | Cited in `SCOPE_LEDGER.csv` SOW-0191; full standard `location TBD` |
| BC Energy Regulator permit (300 MMSCFD deep cut), incl. Section 12.4 site alteration permit | Construction must respect site alteration permit conditions. | Cited in DBM-Deepcut SEC-01; permit text `location TBD` |
| Owner construction safety and turnover standards | TBD | TBD — not in accessible sources |
| Discipline construction standards (civil, mechanical, electrical, I&C) | TBD per discipline production packages | TBD — not in accessible sources |

## Verification

| ReqID | Verification approach |
|---|---|
| REQ-CWP-01 / REQ-CWP-02 | Document review: CWP, workface plan, and turnover checklist artifacts exist, are linked to PKG-060, and cover install/build/inspect/turnover/tie-in. |
| REQ-CWP-03 | Inspection: Tourmaline field construction sign-off recorded for each in-scope activity. |
| REQ-CWP-04 / REQ-CWP-05 | Interface review: each ISBL/OSBL tie-in has a documented responsibility confirmation and a joint-planning record. |
| REQ-CWP-06 | Checklist audit: every PKG-060 interface type has a turnover record with sign-off. |
| REQ-CWP-07 / REQ-CWP-12 | Construction plan review: cold-weather provisions appear where ambient or schedule warrants. |
| REQ-CWP-08 | Field verification at hookup: motor nameplate, starter configuration, and local control device match the basis. |
| REQ-CWP-09 | Interface coordination evidence with DCS, civil/foundations, and electrical MCC scopes. |
| REQ-CWP-10 | Metering verification: independent meters installed/identified at any cross-facility tie-in. |
| REQ-CWP-11 | Material conformance check: no aluminium in caustic-service interfaces. |

## Documentation

The CWP shall produce, at minimum, the following artifacts (per `ARTIFACT_REGISTER.csv` for DEL-060-03):

- Construction Work Package (ART-F8F13A9988) — integrator-authored package for physical installation, construction, and tie-in to larger systems.
- Installation and Tie-In Workface Plan (ART-538DFF5CDE) — workface planning evidence for installing/building the package and connecting it to adjacent systems.
- Construction Interface and Turnover Checklist (ART-4CE1B9B840) — construction-facing interface, tie-in, inspection, and turnover evidence for the approved package.

Supporting records (TBD location, recorded in CWP):

- Joint tie-in planning meeting minutes.
- Per-interface turnover sign-offs.
- Cold-weather construction plan (when applicable).
- Material conformance records for caustic service.
