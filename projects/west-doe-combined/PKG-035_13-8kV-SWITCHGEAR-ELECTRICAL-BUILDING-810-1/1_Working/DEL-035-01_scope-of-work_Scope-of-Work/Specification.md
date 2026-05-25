# Specification: DEL-035-01 Scope of Work

## Scope

This deliverable defines the EPC Integrator scope of work for PKG-035, the workbook-defined Electrical package named `13.8kV SWITCHGEAR ELECTRICAL BUILDING (810-1)`, WBS 01, tracking number `26020-01-30-026`.

The Scope of Work shall cover:

- package identity, source basis, and workbook row traceability;
- package function as the plant main 13.8 kV power distribution center and its whole-facility integration narrative;
- tagged building identifier `810-1` and the housed electrical equipment scope (MCCs, switchgear, distribution equipment, and associated HVAC/ventilation systems);
- responsibility split between Package Vendor and EPC Integrator;
- applicable package interfaces: Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports;
- scope boundaries, assumptions, TBDs, and open items required for downstream package datasheet, construction work package, vendor package production, vendor document turnover, and EPC acceptance.

The Scope of Work shall not assign package engineering, package design, vendor documentation production, or physical equipment package supply to the EPC Integrator. Gate 7 assigns those responsibilities to the Package Vendor and assigns facility-level integration/interface responsibilities to the EPC Integrator.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| SOW-035-01 | The Scope of Work shall identify PKG-035, workbook ID 35, workbook row 37, WBS 01, tracking number `26020-01-30-026`, package name `13.8kV SWITCHGEAR ELECTRICAL BUILDING (810-1)`, and discipline Electrical. | Compare against workbook Packages row 37 and Gate 7 `PACKAGE_REGISTER.csv` row PKG-035. |
| SOW-035-02 | The Scope of Work shall state that the package is vendor-owned for package engineering, package design, vendor documentation, and physical equipment package supply. | Compare against Gate 7 `PACKAGE_REGISTER.csv` row PKG-035. |
| SOW-035-03 | The Scope of Work shall state that the EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | Compare against Gate 7 `PACKAGE_REGISTER.csv` row PKG-035. |
| SOW-035-04 | The Scope of Work shall include the twelve source-supported interface categories listed in workbook Packages row 37 and Gate 7 `INTERFACE_REGISTER.csv` for PKG-035. | Compare against workbook Packages row 37 and Gate 7 `INTERFACE_REGISTER.csv` PKG-035 rows. |
| SOW-035-05 | The Scope of Work shall describe the package function as the plant main 13.8 kV power distribution center fed from a BC Hydro 25 kV supply through a 25 kV/13.8 kV, 50 MVA utility-supplied transformer, with the 13.8 kV bus sized for the full facility scope. | Compare against `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` 13.8 kV switchgear narrative (lines 2917-2919). |
| SOW-035-06 | The Scope of Work shall identify radial distribution from the 13.8 kV switchgear to the 6.9 kV, 4.16 kV, 600 V, and 4.16 kV / 600 V downstream electrical buildings listed in the DBM. | Compare against `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` 13.8 kV switchgear narrative (lines 2919-2925). |
| SOW-035-07 | The Scope of Work shall state the medium-voltage system basis as 13.8 kV, 3 phase, 3 wire, 60 Hz, low-resistance grounded. | Compare against `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` System Voltages table (lines 2933-2934). |
| SOW-035-08 | The Scope of Work shall identify the 810-1 building as a Shop-delivered pre-engineered electrical building housing MCCs, switchgear, distribution equipment, and associated HVAC/ventilation systems, with area classification, HVAC, and remote distribution centres coordinated with hazardous area classification and controls architecture. | Compare against `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Electrical Buildings table and `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` electrical buildings narrative. |
| SOW-035-09 | The Scope of Work shall flag the 03-25 / 04-25 shared distribution scope and identify incoming power metering, protection coordination, and emergency / standby power scope split as items to be confirmed during detailed engineering. | Compare against `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` 13.8 kV switchgear narrative (line 2927). |
| SOW-035-10 | The Scope of Work shall mark unsupported package-specific design values as `TBD`, including switchgear ratings, bus continuous current, short-circuit rating, breaker count, lineup configuration, building dimensions, structural loads, HVAC heat load, and fire & gas device list. | Review against accessible sources and confirm no unsupported values are introduced. |
| SOW-035-11 | The Scope of Work shall preserve anticipated artifacts: package scope of work, tagged equipment and package identity list, package function and integration narrative, and responsibility assignment record. | Compare against `_CONTEXT.md` Anticipated Artifacts. |
| SOW-035-12 | The Scope of Work shall identify no declared critical upstream or downstream dependencies unless `_DEPENDENCIES.md` is later updated. | Compare against `_DEPENDENCIES.md` declared lists. |

## Standards

| Standard / basis | Status |
|---|---|
| Gate 7 PROJECT_DECOMP snapshot | Authoritative accepted decomposition basis for package, deliverable, objective, artifact, scope, and interface registers. |
| Workbook Packages row 37 | Authoritative source row for package identity and interface flags. |
| DBM-Deepcut 4-25 electrical basis | Accessible facility-level source for 13.8 kV switchgear function, System Voltages, and 810-1 building identity. |
| DBM-Comp_and_Liquids 3-25 electrical basis | Accessible facility-level source for electrical building housed equipment and coordination requirements. |
| Package-specific MV switchgear standards (e.g., IEEE C37 family) and vendor specifications | TBD; not present in accessible source slices for this deliverable; location TBD. |

## Verification

- Verify identity fields against workbook Packages row 37 and Gate 7 `PACKAGE_REGISTER.csv`.
- Verify deliverable role against Gate 7 `PROJECT_DECOMP.md` mandatory EPC anchor deliverable basis.
- Verify responsibility split against Gate 7 `PACKAGE_REGISTER.csv` row PKG-035.
- Verify interface list against workbook row 37 and Gate 7 `INTERFACE_REGISTER.csv` rows for PKG-035.
- Verify the package function narrative (utility feed, transformer step-down, radial distribution, downstream targets, shared 03-25 / 04-25 scope) against the DBM-Deepcut 13.8 kV switchgear narrative.
- Verify medium-voltage system parameters against the DBM-Deepcut System Voltages table.
- Verify building identity and housed equipment against DBM-Deepcut Electrical Buildings table and DBM-Comp_and_Liquids electrical buildings narrative.
- Confirm each package-specific technical value is source-supported or marked `TBD`.

## Documentation

The Scope of Work package shall produce or preserve:

- package scope of work;
- tagged equipment and package identity list, with tag values marked `TBD` when unavailable;
- package function and integration narrative (utility feed, transformer step-down, 13.8 kV bus, radial distribution to downstream buildings, shared 03-25 / 04-25 scope);
- responsibility assignment record;
- interface basis for the twelve source-supported interface categories;
- list of source limitations, TBDs, assumptions, and human ruling items.
