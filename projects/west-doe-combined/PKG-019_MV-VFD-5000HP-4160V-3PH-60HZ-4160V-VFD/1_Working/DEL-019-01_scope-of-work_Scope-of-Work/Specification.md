# Specification: DEL-019-01 Scope of Work

## Scope

This deliverable defines the EPC Integrator scope of work for PKG-019, the workbook-defined Electrical package named `MV VFD - 5000HP, 4160V, 3PH, 60HZ - 4160V VFD`, WBS 02, tracking number `26020-02-30-009`.

The Scope of Work shall cover:

- package identity, source basis, and workbook row traceability;
- package function and whole-facility integration narrative (medium-voltage VFD serving the 4160V system per the DBM electrical basis);
- tagged equipment where source-supported;
- responsibility split between Package Vendor and EPC Integrator;
- applicable package interfaces: Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports;
- scope boundaries, assumptions, TBDs, and open items required for downstream package datasheet, construction work package, vendor package production, vendor document turnover, and EPC acceptance.

The Scope of Work shall not assign package engineering, package design, vendor documentation production, or physical equipment package supply to the EPC Integrator. Gate 7 assigns those responsibilities to the Package Vendor and assigns facility-level integration/interface responsibilities to the EPC Integrator.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| SOW-019-01 | The Scope of Work shall identify PKG-019, workbook ID 19, workbook row 21, WBS 02, tracking number `26020-02-30-009`, package name `MV VFD - 5000HP, 4160V, 3PH, 60HZ - 4160V VFD`, and discipline Electrical. | Compare against workbook Packages row 21 and Gate 7 `PACKAGE_REGISTER.csv` row PKG-019. |
| SOW-019-02 | The Scope of Work shall state that the package is vendor-owned for package engineering, package design, vendor documentation, and physical equipment package supply. | Compare against Gate 7 `PACKAGE_REGISTER.csv` row PKG-019. |
| SOW-019-03 | The Scope of Work shall state that the EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | Compare against Gate 7 `PACKAGE_REGISTER.csv` row PKG-019. |
| SOW-019-04 | The Scope of Work shall include the six source-supported interface categories: Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports. | Compare against workbook Packages row 21 and Gate 7 `PACKAGE_REGISTER.csv` row PKG-019. |
| SOW-019-05 | The Scope of Work shall reference facility MV electrical context (13.8 kV / 4.16 kV / 12 MVA transformer and 4160V MCC serving large 4000V motors with VFD starting per SCA-001 VE #34) only as facility context, without converting it into package-specific VFD design values. | Compare against DBM Comp and Liquids lines 324-326, 533, 744-756. |
| SOW-019-06 | The Scope of Work shall mark unsupported package-specific design values as `TBD`, including VFD topology, drive ratings, transformer/reactor configuration, harmonic filtering, cooling, enclosure, environmental rating, weights, dimensions, footprint, and support loads. | Review against accessible sources and confirm no unsupported values are introduced. |
| SOW-019-07 | The Scope of Work shall surface the apparent discrepancy between the package title voltage / horsepower (4160 V / 5000 HP) and the DBM motor basis (4,000 V / ~5,200 HP) as an open item for human ruling, and shall not silently normalize either value. | Compare against Gate 7 `PACKAGE_REGISTER.csv` row PKG-019 and DBM lines 324, 744, 752; confirm Conflict Table HR-019-01-01 is carried. |
| SOW-019-08 | The Scope of Work shall preserve anticipated artifacts: package scope of work, tagged equipment and package identity list, package function and integration narrative, and responsibility assignment record. | Compare against `_CONTEXT.md` Anticipated Artifacts. |
| SOW-019-09 | The Scope of Work shall identify no declared critical upstream or downstream dependencies unless `_DEPENDENCIES.md` is later updated. | Compare against `_DEPENDENCIES.md` declared lists. |
| SOW-019-10 | The Scope of Work shall not assert vendor-allocated tagged equipment (e.g., association with inlet compressor motors `KM-2150` / `KM-2250`) unless source material confirms the allocation; otherwise tagged equipment shall remain `TBD`. | Compare against workbook Packages row 21, Gate 7 PKG-019 rows, and DBM lines 324-326, 533, 752-756. |

## Standards

| Standard / basis | Status |
|---|---|
| Gate 7 PROJECT_DECOMP snapshot | Authoritative accepted decomposition basis for package, deliverable, objective, artifact, scope, and interface registers. |
| Workbook Packages row 21 | Authoritative source row for package identity and interface flags. |
| DBM Comp and Liquids electrical basis | Accessible facility-level source for MV electrical context (4160V MCC, motor basis, starting-VFD requirement). |
| SCA-001 (VE #34, VE #37) | Referenced by DBM as governing starting basis and capacitor-bank removal where VFDs are present; the SCA-001 document text itself is not directly accessible in the source set. |
| NEMA MG1 / inverter-duty motor standards | Referenced by DBM in connection with the driven motor basis; package-level VFD standards (e.g., IEEE 519 harmonics, IEC/UL drive standards) are TBD; location of governing project specifications is TBD. |

## Verification

- Verify identity fields against workbook Packages row 21 and Gate 7 `PACKAGE_REGISTER.csv`.
- Verify deliverable role against Gate 7 `PROJECT_DECOMP.md` mandatory EPC anchor deliverable basis.
- Verify responsibility split against Gate 7 `PACKAGE_REGISTER.csv` row PKG-019.
- Verify interface list against workbook row 21 and Gate 7 `PACKAGE_REGISTER.csv` PKG-019 interface columns.
- Verify MV electrical context against the DBM Comp and Liquids electrical sections; confirm facility-context language has not been promoted to package design values.
- Confirm each package-specific technical value is source-supported or marked `TBD`.
- Confirm the voltage/horsepower discrepancy between the package title and DBM motor basis is carried as a human ruling item.
- Confirm cross-document terminology preserves the source package name spelling.

## Documentation

The Scope of Work package shall produce or preserve:

- package scope of work;
- tagged equipment and package identity list, with tag values marked `TBD` when unavailable;
- package function and integration narrative;
- responsibility assignment record;
- interface basis for Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports;
- list of source limitations, TBDs, assumptions, and human ruling items.
