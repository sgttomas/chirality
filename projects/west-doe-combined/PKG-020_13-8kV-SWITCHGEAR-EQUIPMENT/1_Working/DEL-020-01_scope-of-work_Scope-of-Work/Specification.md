# Specification: DEL-020-01 Scope of Work

## Scope

This deliverable defines the EPC Integrator Scope of Work for PKG-020, the workbook-defined Electrical package named `13.8kV SWITCHGEAR EQUIPMENT`, WBS 01, CoA tracking number `26020-01-30-011`.

The Scope of Work shall cover:

- package identity, source basis, and workbook row traceability;
- package function and whole-facility integration narrative (plant 13.8 kV main power distribution center fed by the BC Hydro 25 kV utility supply through a 25 kV / 13.8 kV / 50 MVA utility transformer, distributing radially to the facility's named medium- and low-voltage electrical buildings per the DBM electrical basis);
- tagged equipment where source-supported;
- responsibility split between Package Vendor and EPC Integrator;
- applicable package interfaces: Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports;
- scope boundaries, assumptions, TBDs, and open items required for the downstream Package Datasheet, Construction Work Package, Vendor Engineered Equipment Package, Vendor Document Turnover Package, and EPC Vendor Package Review and Acceptance.

The Scope of Work shall not assign package engineering, package design, vendor documentation production, or physical equipment package supply to the EPC Integrator. Gate 7 assigns those responsibilities to the Package Vendor and assigns facility-level integration/interface responsibilities to the EPC Integrator.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| SOW-020-01 | The Scope of Work shall identify PKG-020, workbook ID 20, workbook row 22, WBS 01, tracking number `26020-01-30-011`, package name `13.8kV SWITCHGEAR EQUIPMENT`, and discipline Electrical. | Compare against workbook Packages row 22 and Gate 7 `PACKAGE_REGISTER.csv` row PKG-020. |
| SOW-020-02 | The Scope of Work shall state that the package is vendor-owned for package engineering, package design, vendor documentation, and physical equipment package supply. | Compare against Gate 7 `PACKAGE_REGISTER.csv` row PKG-020. |
| SOW-020-03 | The Scope of Work shall state that the EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | Compare against Gate 7 `PACKAGE_REGISTER.csv` row PKG-020. |
| SOW-020-04 | The Scope of Work shall include the six source-supported interface categories: Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports. | Compare against workbook Packages row 22, Gate 7 `PACKAGE_REGISTER.csv` row PKG-020, and Gate 7 `INTERFACE_REGISTER.csv` rows for PKG-020. |
| SOW-020-05 | The Scope of Work shall describe PKG-020 as the plant 13.8 kV main power distribution center fed by a 25 kV / 13.8 kV / 50 MVA utility-supplied transformer downstream of the BC Hydro 25 kV utility supply, distributing radially through step-down transformers to the named electrical buildings (6.9 kV Inlet/Sales Compressor; 4.16 kV Acid Gas/Overheads Compressor; 600 V Acid Gas Compressor; 600 V Sales/Overheads Compressor; 4.16 kV/600 V General Area/Tank Farm/Process). | Compare against `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Power System section. |
| SOW-020-06 | The Scope of Work shall reference the 13.8 kV system basis (3 phase, 3 wire, 60 Hz, low-resistance grounded) only as facility context and shall not derive package-specific bus, breaker, or protection ratings from it. | Compare against `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` System Voltages table. |
| SOW-020-07 | The Scope of Work shall mark unsupported package-specific design values as `TBD`, including bus continuous current rating, short-circuit interrupting rating, BIL, breaker count, lineup arrangement, control voltage source, enclosure type, dimensions, weights, environmental rating, relay/protection settings, arc-flash boundaries, and coordination tables. | Review against accessible sources and confirm no unsupported values are introduced. |
| SOW-020-08 | The Scope of Work shall state that the 13.8 kV switchgear is not the standby-power tie-in point for this facility scope, because the DBM moves standby power to TOU generators at the 600 V MCC level via transfer switches. | Compare against `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Standby Power paragraph. |
| SOW-020-09 | The Scope of Work shall preserve anticipated artifacts: package scope of work, tagged equipment and package identity list, package function and integration narrative, and responsibility assignment record. | Compare against `_CONTEXT.md` Anticipated Artifacts and Gate 7 `ARTIFACT_REGISTER.csv` rows for DEL-020-01. |
| SOW-020-10 | The Scope of Work shall identify no declared critical upstream or downstream dependencies unless `_DEPENDENCIES.md` is later updated. | Compare against `_DEPENDENCIES.md` declared lists. |
| SOW-020-11 | The Scope of Work shall not assert specific switchgear equipment tags (for example, the DBM-listed "Medium Voltage Switchgear, qty 1" `ELC-QAS-000007-001` or the "810-1 13.8kV Switchgear Electrical Building" line item) as PKG-020 tagged equipment unless the source allocation is confirmed; otherwise tagged equipment shall remain `TBD` and the allocation question carried as a human ruling item. | Compare against workbook Packages row 22, Gate 7 `PACKAGE_REGISTER.csv` row PKG-020, and `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` electrical equipment and trace appendix sections; confirm Conflict HR-020-01-02. |
| SOW-020-12 | The Scope of Work shall identify the "Relay coordination and arc-flash energy study" and "Load-flow study" required by the DBM as facility-level studies whose PKG-020 inputs/outputs are TBD, and shall not prescribe study results. | Compare against `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` electrical studies paragraphs. |

## Standards

| Standard / basis | Status |
|---|---|
| Gate 7 PROJECT_DECOMP snapshot | Authoritative accepted decomposition basis for package, deliverable, objective, artifact, scope, and interface registers. |
| Workbook Packages row 22 | Authoritative source row for package identity and interface flags. |
| DBM Deepcut electrical basis (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`) | Accessible facility-level source for Power System, System Voltages, Standby Power, Transformers, Motor Control, Electrical Buildings, Grounding and Bonding, and Cable Specifications. |
| Canadian Electrical Code (CEC) | Referenced by the DBM for grounding sizing, transformer spacing, conduit, and area-classification practices; CEC clause text is not directly accessible in the source set (location TBD). |
| BC Hydro utility distribution basis | Referenced by the DBM as the 25 kV utility supply feeding the 50 MVA utility transformer; BC Hydro tariff/standards documents are not directly accessible (location TBD). |
| API RP-505 | Referenced by the DBM for Zone 2 area classification; clause text not directly accessible (location TBD). |
| `_Sources/26020-Package_Requirements.docx` | Searched for package-specific 13.8 kV switchgear content; no PKG-020 match accessible in this run. |

## Verification

- Verify identity fields against workbook Packages row 22 and Gate 7 `PACKAGE_REGISTER.csv` row PKG-020.
- Verify deliverable role against Gate 7 `PROJECT_DECOMP.md` mandatory EPC anchor deliverable basis.
- Verify responsibility split against Gate 7 `PACKAGE_REGISTER.csv` row PKG-020.
- Verify interface list against workbook row 22, Gate 7 `PACKAGE_REGISTER.csv` PKG-020 interface columns, and Gate 7 `INTERFACE_REGISTER.csv` PKG-020 rows.
- Verify 13.8 kV facility context (utility supply, transformer, radial distribution, system voltages, grounding, standby-power non-tie-in basis, housing in modular electrical buildings) against the DBM Deepcut Power System, System Voltages, Standby Power, Grounding and Bonding, and Electrical Buildings sections.
- Confirm each package-specific technical value (bus, breaker, BIL, dimensions, protection, arc-flash) is source-supported or marked `TBD`.
- Confirm tagged-equipment allocation (Medium Voltage Switchgear `ELC-QAS-000007-001`; "810-1 13.8kV Switchgear Electrical Building") is carried as a human ruling item rather than asserted.
- Confirm cross-document terminology preserves the accepted package name spelling `13.8kV SWITCHGEAR EQUIPMENT`.

## Documentation

The Scope of Work package shall produce or preserve:

- package scope of work;
- tagged equipment and package identity list, with tag values marked `TBD` when allocation is unconfirmed;
- package function and whole-facility integration narrative grounded in the DBM Power System section;
- responsibility assignment record;
- interface basis for Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports;
- list of source limitations, TBDs, assumptions, and human ruling items.
