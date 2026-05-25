# Specification: DEL-022-01 Scope of Work

## Scope

This deliverable defines the EPC Integrator scope of work for PKG-022, the workbook-defined Electrical package named `5kV SWITCHGEAR EQUIPMENT`, WBS 01, tracking number `26020-01-30-013`.

The Scope of Work shall cover:

- package identity, source basis, and workbook row traceability;
- package function and whole-facility integration narrative (medium-voltage switchgear lineup within the Deepcut facility electrical distribution per the DBM electrical basis);
- tagged equipment where source-supported;
- responsibility split between Package Vendor and EPC Integrator;
- applicable package interfaces: Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports;
- scope boundaries, assumptions, TBDs, and open items required for downstream package datasheet, construction work package, vendor package production, vendor document turnover, and EPC acceptance.

The Scope of Work shall not assign package engineering, package design, vendor documentation production, or physical equipment package supply to the EPC Integrator. Gate 7 assigns those responsibilities to the Package Vendor and assigns facility-level integration/interface responsibilities to the EPC Integrator.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| SOW-022-01 | The Scope of Work shall identify PKG-022, workbook ID 22, workbook row 24, WBS 01, tracking number `26020-01-30-013`, package name `5kV SWITCHGEAR EQUIPMENT`, and discipline Electrical. | Compare against workbook Packages row 24 and Gate 7 `PACKAGE_REGISTER.csv` row PKG-022. |
| SOW-022-02 | The Scope of Work shall state that the package is vendor-owned for package engineering, package design, vendor documentation, and physical equipment package supply. | Compare against Gate 7 `PACKAGE_REGISTER.csv` row PKG-022. |
| SOW-022-03 | The Scope of Work shall state that the EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | Compare against Gate 7 `PACKAGE_REGISTER.csv` row PKG-022. |
| SOW-022-04 | The Scope of Work shall include the six source-supported interface categories: Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports. | Compare against workbook Packages row 24 and Gate 7 `PACKAGE_REGISTER.csv` row PKG-022. |
| SOW-022-05 | The Scope of Work shall reference Deepcut facility MV electrical context (13.8 kV main distribution; 6.9 kV and 4.16 kV process MV services; 5 kV-class insulation for 4.16 kV cables) only as facility context, without converting it into package-specific switchgear design values. | Compare against DBM Deepcut lines 2917-2925, 2935-2936, 3007-3009. |
| SOW-022-06 | The Scope of Work shall mark unsupported package-specific design values as `TBD`, including bus voltage and rating, short-circuit rating, breaker type, lineup configuration, BIL, neutral grounding implementation, enclosure, cooling, environmental rating, weights, dimensions, footprint, and support loads. | Review against accessible sources and confirm no unsupported values are introduced. |
| SOW-022-07 | The Scope of Work shall surface the apparent ambiguity between the package name "5kV SWITCHGEAR EQUIPMENT" and the DBM facility MV bus voltages (13.8 kV / 6.9 kV / 4.16 kV with 5 kV-class cable insulation for the 4.16 kV system) as an open item for human ruling, and shall not silently normalize the package name to any specific facility bus. | Compare against Gate 7 `PACKAGE_REGISTER.csv` row PKG-022 and DBM Deepcut lines 2917-2925, 2935-2936, 3009; confirm Conflict Table HR-022-01-01 is carried. |
| SOW-022-08 | The Scope of Work shall preserve anticipated artifacts: package scope of work, tagged equipment and package identity list, package function and integration narrative, and responsibility assignment record. | Compare against `_CONTEXT.md` Anticipated Artifacts and Gate 7 `ARTIFACT_REGISTER.csv`. |
| SOW-022-09 | The Scope of Work shall identify no declared critical upstream or downstream dependencies unless `_DEPENDENCIES.md` is later updated. | Compare against `_DEPENDENCIES.md` declared lists. |
| SOW-022-10 | The Scope of Work shall not assert tagged equipment, fed loads, electrical-building assignment, or relationship to PKG-037 (5kV Switchgear Electrical Building 880-1) unless source material confirms the allocation; otherwise tagged equipment and building/location association shall remain `TBD`. | Compare against workbook Packages row 24 and Gate 7 PKG-022 / PKG-037 rows; confirm Conflict Table HR-022-01-02 is carried. |

## Standards

| Standard / basis | Status |
|---|---|
| Gate 7 PROJECT_DECOMP snapshot | Authoritative accepted decomposition basis for package, deliverable, objective, artifact, scope, and interface registers. |
| Workbook Packages row 24 | Authoritative source row for package identity and interface flags. |
| DBM Deepcut electrical basis | Accessible facility-level source for MV electrical context (13.8 kV main distribution, 6.9 kV / 4.16 kV process MV services, MV cable insulation classes). |
| IEEE / ANSI / NEMA MV switchgear standards (e.g., ANSI/IEEE C37 series, NEMA SG) | Not directly enumerated in accessible source slices for PKG-022; specific governing project specifications are TBD; location TBD. |
| CSA / Provincial electrical code basis | Not directly cited in the accessible PKG-022 source slices; project-level applicability assumed; location TBD. |

## Verification

- Verify identity fields against workbook Packages row 24 and Gate 7 `PACKAGE_REGISTER.csv`.
- Verify deliverable role against Gate 7 `PROJECT_DECOMP.md` mandatory EPC anchor deliverable basis.
- Verify responsibility split against Gate 7 `PACKAGE_REGISTER.csv` row PKG-022.
- Verify interface list against workbook row 24 and Gate 7 `PACKAGE_REGISTER.csv` PKG-022 interface columns.
- Verify MV electrical context against the DBM Deepcut electrical sections; confirm facility-context language has not been promoted to package design values.
- Confirm each package-specific technical value is source-supported or marked `TBD`.
- Confirm the 5 kV designation / facility bus alignment question is carried as a human ruling item.
- Confirm the PKG-022 / PKG-037 relationship is carried as TBD rather than silently assumed.
- Confirm cross-document terminology preserves the source package name spelling.

## Documentation

The Scope of Work package shall produce or preserve:

- package scope of work;
- tagged equipment and package identity list, with tag values marked `TBD` when unavailable;
- package function and integration narrative;
- responsibility assignment record;
- interface basis for Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports;
- list of source limitations, TBDs, assumptions, and human ruling items.
