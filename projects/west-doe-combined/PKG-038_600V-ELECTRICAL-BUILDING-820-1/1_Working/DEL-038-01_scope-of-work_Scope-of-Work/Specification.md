# Specification: DEL-038-01 Scope of Work

## Scope

This deliverable defines the EPC Integrator Scope of Work for PKG-038, the workbook-defined Electrical package named `600V ELECTRICAL BUILDING (820-1)`, WBS 01, CoA tracking number `26020-01-30-029`.

The Scope of Work shall cover:

- package identity, source basis, and workbook row traceability;
- package function and whole-facility integration narrative (a 600 V class prefabricated electrical building integrated into the facility electrical distribution per the DBM electrical buildings basis);
- tagged equipment where source-supported, with allocation to a specific site building number (820-1 / 840-1 / 850-1 / 860-1) carried as a human ruling item;
- responsibility split between Package Vendor and EPC Integrator;
- the twelve applicable package interfaces flagged by the workbook and Gate 7 registers: Utility Piping, Drain / Containment, Electrical Power, Grounding / Bonding, Area / Exterior Lighting, I&C / Control Cabling, Communications / Network, Building HVAC / Services, Fire & Gas / Safety Systems, Maintenance Access, Grading / Site Drainage / Spill Containment, and Structural / Foundations / Supports;
- scope boundaries, assumptions, TBDs, and open items required for downstream package datasheet, construction work package, vendor package production, vendor document turnover, and EPC acceptance.

The Scope of Work shall not assign package engineering, package design, vendor documentation production, or physical equipment package supply to the EPC Integrator. Gate 7 assigns those responsibilities to the Package Vendor and assigns facility-level integration and interface responsibilities to the EPC Integrator.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| SOW-038-01 | The Scope of Work shall identify PKG-038, workbook ID 38, workbook row 40, WBS 01, CoA tracking number `26020-01-30-029`, package name `600V ELECTRICAL BUILDING (820-1)`, and discipline Electrical. | Compare against workbook Packages row 40 and Gate 7 `PACKAGE_REGISTER.csv` row PKG-038. |
| SOW-038-02 | The Scope of Work shall state that the package is vendor-owned for package engineering, package design, vendor documentation, and physical equipment package supply. | Compare against Gate 7 `PACKAGE_REGISTER.csv` row PKG-038. |
| SOW-038-03 | The Scope of Work shall state that the EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | Compare against Gate 7 `PACKAGE_REGISTER.csv` row PKG-038. |
| SOW-038-04 | The Scope of Work shall include all twelve source-supported interface categories: Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports. | Compare against workbook Packages row 40 and Gate 7 `INTERFACE_REGISTER.csv` PKG-038 rows. |
| SOW-038-05 | The Scope of Work shall reference DBM facility-level low-voltage electrical context (600 V, 3 phase, 3 wire, 60 Hz, high-resistance grounded with 5 A continuous resistor; 600 V MCC basis with VFDs in the MCC lineup; radial 13.8 kV step-down distribution to the 600 V electrical buildings) only as facility context, without converting it into package-specific design values. | Compare against `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2917-2925, 2934-2937, 2959. |
| SOW-038-06 | The Scope of Work shall reference the DBM electrical-building housing scope (potential housing of MV switchgear/MCC/VFD, 600 V MCCs, 120 V AC and 125 V DC UPS systems, distribution transformers and panelboards, contactor panels, PLC panels, network racks), n+1 HVAC sizing, bottom-entry cable routing on elevated/pile-supported buildings, and TECK/ACIC/EMT cable/conduit basis, without prescribing package-specific equipment counts or ratings. | Compare against `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2971-2979. |
| SOW-038-07 | The Scope of Work shall reference the DBM grounding basis applicable to the 600 V electrical building (5 A high-resistance grounding for the 600 V transformer; ground/resistor fault detection at the 600 V MCC; alarm-only ground-fault protection on 600 V systems; two-point ground grid connection; ground wells at transformers / electrical buildings) without prescribing package-specific grounding conductor sizes. | Compare against `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2985, 2989. |
| SOW-038-08 | The Scope of Work shall reference the standby-power interface (TOU low-voltage standby generators on the 600 V MCC with transfer switches feeding both 04-25 and 03-25 critical loads) as an interface only, with generator selection, switchgear assignment, transfer-switch configuration, fuel selection, battery/charger sizing, and diesel storage marked TBD. | Compare against `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2076, 2080, 2084, 2943, 2164, 1836. |
| SOW-038-09 | The Scope of Work shall mark unsupported package-specific design values as `TBD`, including specific equipment counts, MCC/UPS/transformer ratings, panel schedules, building dimensions and weights, footprint, and support loads. | Review against accessible sources and confirm no unsupported values are introduced. |
| SOW-038-10 | The Scope of Work shall surface the apparent discrepancy between the workbook package name `600V ELECTRICAL BUILDING (820-1)` and the DBM electrical-building list (820-1 = 6.9 kV Inlet/Sales Compressor Electrical Building; 600 V electrical buildings are 840-1, 850-1, and 860-1) as an open item for human ruling, and shall not silently normalize either value. | Compare against Gate 7 `PACKAGE_REGISTER.csv` row PKG-038 and `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2811-2816, 2921-2925; confirm Conflict HR-038-01-01 is carried. |
| SOW-038-11 | The Scope of Work shall preserve anticipated artifacts: package scope of work, tagged equipment and package identity list, package function and integration narrative, and responsibility assignment record. | Compare against `_CONTEXT.md` Anticipated Artifacts and Gate 7 `ARTIFACT_REGISTER.csv` rows for DEL-038-01_scope-of-work. |
| SOW-038-12 | The Scope of Work shall identify no declared critical upstream or downstream dependencies unless `_DEPENDENCIES.md` is later updated. | Compare against `_DEPENDENCIES.md` declared lists. |

## Standards

| Standard / basis | Status |
|---|---|
| Gate 7 PROJECT_DECOMP snapshot | Authoritative accepted decomposition basis for package, deliverable, objective, artifact, scope, and interface registers. |
| Workbook Packages row 40 | Authoritative source row for package identity and interface flags. |
| DBM Deepcut electrical basis | Accessible facility-level source for LV (600 V) electrical context, MCC and VFD basis, electrical-building housing scope, HVAC, cable entry, cabling, and grounding. |
| Canadian Electrical Code (CEC) | Referenced by the DBM as governing MCC-to-process spacing (7.5 m) and electrical installation basis. Clause locations TBD. |
| OGAOM Sec. 9.6.15 | Referenced by the DBM as governing 25 m spacing between fired heaters and electrical buildings. Direct OGAOM text not accessible. |
| Project electrical specifications (ELC-QAS series, e.g., ELC-QAS-000006-001 Low Voltage Switchgear, ELC-QAS-000009-001 Low Voltage Motor Control Centers) | Referenced by the DBM specification list; specification document locations TBD. |
| Area classification standards | Electrical buildings located in general purpose areas per DBM; package-specific classification confirmation TBD. |

## Verification

- Verify identity fields against workbook Packages row 40 and Gate 7 `PACKAGE_REGISTER.csv` row PKG-038.
- Verify deliverable role against Gate 7 `PROJECT_DECOMP.md` mandatory EPC anchor deliverable basis and Gate 7 `DELIVERABLE_REGISTER.csv` row DEL-038-01_scope-of-work.
- Verify responsibility split against Gate 7 `PACKAGE_REGISTER.csv` row PKG-038.
- Verify interface list against workbook row 40 and Gate 7 `INTERFACE_REGISTER.csv` PKG-038 rows; all twelve interface facts must be present.
- Verify LV electrical context, electrical-building housing scope, HVAC, cabling, and grounding statements against the DBM Deepcut electrical sections; confirm facility-context language has not been promoted to package-specific design values.
- Confirm each package-specific technical value is source-supported or marked `TBD`.
- Confirm the workbook name (`820-1`) vs DBM building list (820-1 = 6.9 kV; 600 V buildings are 840-1 / 850-1 / 860-1) discrepancy is carried as a human ruling item.
- Confirm cross-document terminology preserves the source package name spelling.

## Documentation

The Scope of Work package shall produce or preserve:

- package scope of work;
- tagged equipment and package identity list, with tag values marked `TBD` when unavailable and the 820-1 site number carried as the workbook identity with the discrepancy flagged;
- package function and integration narrative covering the 600 V electrical building role within the facility electrical backbone;
- responsibility assignment record;
- interface basis for all twelve applicable interface categories;
- list of source limitations, TBDs, assumptions, and human ruling items.
