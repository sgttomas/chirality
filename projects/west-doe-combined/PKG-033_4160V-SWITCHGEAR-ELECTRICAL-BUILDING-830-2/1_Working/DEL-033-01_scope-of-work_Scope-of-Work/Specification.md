# Specification: DEL-033-01 Scope of Work

## Scope

This deliverable defines the EPC Integrator scope of work for PKG-033, the workbook-defined Electrical package named `4160V SWITCHGEAR ELECTRICAL BUILDING (830-2)`, WBS 02, tracking number `26020-02-30-024`.

The Scope of Work shall cover:

- package identity, source basis, and workbook row traceability (workbook Packages row 35);
- package function and whole-facility integration narrative for a 4,160 V switchgear electrical building serving the 03-25 facility;
- tagged equipment where source-supported (TBD pending vendor data);
- responsibility split between Package Vendor and EPC Integrator per Gate 7;
- applicable package interfaces flagged in Gate 7: Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports;
- scope boundaries, assumptions, TBDs, and open items required for downstream package datasheet (DEL-033-02), construction work package (DEL-033-03), vendor engineered equipment package (DEL-033-04), vendor document turnover (DEL-033-05), and EPC vendor package review and acceptance (DEL-033-06).

The Scope of Work shall not assign package engineering, package design, vendor documentation production, or physical equipment package supply to the EPC Integrator. Gate 7 assigns those responsibilities to the Package Vendor and assigns facility-level integration/interface responsibilities to the EPC Integrator.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| SOW-033-01 | The Scope of Work shall identify PKG-033, workbook ID 33, workbook row 35, WBS 02, tracking number `26020-02-30-024`, package name `4160V SWITCHGEAR ELECTRICAL BUILDING (830-2)`, and discipline Electrical. | Compare against workbook Packages row 35 and Gate 7 `PACKAGE_REGISTER.csv` row PKG-033. |
| SOW-033-02 | The Scope of Work shall state that the package is vendor-owned for package engineering, package design, vendor documentation, and physical equipment package supply. | Compare against Gate 7 `PACKAGE_REGISTER.csv` row PKG-033. |
| SOW-033-03 | The Scope of Work shall state that the EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | Compare against Gate 7 `PACKAGE_REGISTER.csv` row PKG-033. |
| SOW-033-04 | The Scope of Work shall include all twelve source-supported interface categories listed in Gate 7 `INTERFACE_REGISTER.csv` PKG-033 rows. | Compare against Gate 7 `INTERFACE_REGISTER.csv` PKG-033 rows. |
| SOW-033-05 | The Scope of Work shall identify the facility electrical service context as 13.8 kV incoming from 04-25 stepped down to 4,160 V via a 13.8 kV / 4.16 kV, 12 MVA transformer feeding the 4160V MCC, and shall state the 4,160 V service basis (3 phase, 3 wire, 60 Hz LRG for process AC inverter-drive motors 250 hp to 5,500 hp), without converting facility-level context into package-specific switchgear design values. | Compare against `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 732-744. |
| SOW-033-06 | The Scope of Work shall mark unsupported package-specific design values as `TBD`, including switchgear lineup, bus rating, short-circuit/withstand rating, breaker count and ratings, protective relaying scheme, enclosure rating, building dimensions, HVAC capacity, ventilation, fire/gas detection, foundation loads, weights, and dimensions. | Review against accessible sources and confirm no unsupported values are introduced. |
| SOW-033-07 | The Scope of Work shall preserve anticipated artifacts: package scope of work, tagged equipment and package identity list, package function and integration narrative, and responsibility assignment record. | Compare against `_CONTEXT.md` Anticipated Artifacts. |
| SOW-033-08 | The Scope of Work shall identify no declared critical upstream or downstream dependencies unless `_DEPENDENCIES.md` is later updated. | Compare against `_DEPENDENCIES.md` declared lists. |
| SOW-033-09 | The Scope of Work shall identify the electrical building scope basis (housing for MCCs, switchgear, distribution equipment, and associated HVAC/ventilation) and the cable/conduit separation basis (separation of 13.8 kV, 4,160 V, and 600 V power circuits from control and instrument circuits). | Compare against `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 764-768. |
| SOW-033-10 | The Scope of Work shall identify hazardous area classification coordination as an integration constraint for building HVAC and electrical equipment selection. | Compare against `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` Area Classification section and Electrical Buildings section. |

## Standards

| Standard / basis | Status |
|---|---|
| Gate 7 PROJECT_DECOMP snapshot | Authoritative accepted decomposition basis for package, deliverable, objective, artifact, scope, and interface registers. |
| Workbook Packages row 35 | Authoritative source row for package identity and interface flags. |
| DBM Comp and Liquids electrical basis | Accessible facility-level source for incoming power, MV service, transformers, 4160V MCC context, electrical building scope, and cable separation. |
| API RP 505 (Class I Zone 2 classification, Gas Groups IIA/IIB) | Cited as facility classification basis in DBM Area Classification section; clause-level requirements TBD; location TBD. |
| Package-specific MV switchgear and electrical building standards (e.g., IEEE C37 series, IEC 62271 series, NFPA 70, NFPA 70E) | TBD — likely applicable (ASSUMPTION); not present in accessible source slices for this deliverable. |

## Verification

- Verify identity fields against workbook Packages row 35 and Gate 7 `PACKAGE_REGISTER.csv`.
- Verify deliverable role against Gate 7 `PROJECT_DECOMP.md` mandatory EPC anchor deliverable basis.
- Verify responsibility split against Gate 7 `PACKAGE_REGISTER.csv` row PKG-033.
- Verify interface list against workbook row 35 and Gate 7 `INTERFACE_REGISTER.csv` rows for PKG-033 (twelve YES interfaces).
- Verify facility electrical service context against the DBM Comp and Liquids System Voltages and Incoming Power and Transformers tables.
- Verify electrical-building and cable-separation basis against the DBM Electrical Buildings, Raceways, Lighting, and Heat Tracing section.
- Confirm each package-specific switchgear/building technical value is source-supported or marked `TBD`.
- Confirm cross-document terminology uses the source spelling `4160V SWITCHGEAR ELECTRICAL BUILDING (830-2)` for identity.

## Documentation

The Scope of Work package shall produce or preserve:

- package scope of work;
- tagged equipment and package identity list, with tag values marked `TBD` when unavailable;
- package function and integration narrative for the 4,160 V switchgear electrical building (830-2);
- responsibility assignment record;
- interface basis for all twelve Gate 7 YES interfaces;
- list of source limitations, TBDs, assumptions, and human ruling items.
