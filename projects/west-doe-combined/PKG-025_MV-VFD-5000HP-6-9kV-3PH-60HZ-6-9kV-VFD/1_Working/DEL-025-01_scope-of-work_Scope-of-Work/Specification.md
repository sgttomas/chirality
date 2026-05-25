# Specification: DEL-025-01 Scope of Work

## Scope

This deliverable defines the EPC Integrator scope of work for PKG-025, the workbook-defined Electrical package named `MV VFD - 5000HP, 6.9kV, 3PH, 60HZ - 6.9kV VFD`, WBS 01, tracking number `26020-01-30-016`.

The Scope of Work shall cover:

- package identity, source basis, and workbook row traceability;
- package function and whole-facility integration narrative as a 6.9 kV medium-voltage variable frequency drive serving a 5,000 hp, 3-phase, 60 Hz process motor (driven equipment identity TBD);
- tagged equipment where source-supported;
- responsibility split between Package Vendor and EPC Integrator;
- applicable package interfaces: Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports;
- scope boundaries, assumptions, TBDs, and open items required for downstream package datasheet, construction work package, vendor package production, vendor document turnover, and EPC acceptance.

The Scope of Work shall not assign package engineering, package design, vendor documentation production, or physical equipment package supply to the EPC Integrator. Gate 7 assigns those responsibilities to the Package Vendor and assigns facility-level integration/interface responsibilities to the EPC Integrator.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| SOW-025-01 | The Scope of Work shall identify PKG-025, workbook ID 25, workbook row 27, WBS 01, tracking number `26020-01-30-016`, package name `MV VFD - 5000HP, 6.9kV, 3PH, 60HZ - 6.9kV VFD`, and discipline Electrical. | Compare against workbook Packages row 27 and Gate 7 `PACKAGE_REGISTER.csv` row PKG-025. |
| SOW-025-02 | The Scope of Work shall state that the package is vendor-owned for package engineering, package design, vendor documentation, and physical equipment package supply. | Compare against Gate 7 `PACKAGE_REGISTER.csv` row PKG-025. |
| SOW-025-03 | The Scope of Work shall state that the EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | Compare against Gate 7 `PACKAGE_REGISTER.csv` row PKG-025. |
| SOW-025-04 | The Scope of Work shall include the six source-supported interface categories for PKG-025: Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports. | Compare against workbook Packages row 27 and Gate 7 `INTERFACE_REGISTER.csv` PKG-025 rows. |
| SOW-025-05 | The Scope of Work shall identify the facility MV bus context as 6.9 kV, 3 phase, 3 wire, 60 Hz, low-resistance grounded with a 100 A, 10 s neutral grounding resistor, and shall identify 6.9 kV MV cabling as three-conductor copper TECK rated 8 kV with 100 percent insulation. These are facility-level service basis items, not package design assertions. | Compare against DBM Deepcut electrical power distribution table (line 2935), grounding section (line 2985), and MV cable section (line 3008). |
| SOW-025-06 | The Scope of Work shall identify facility MV starting context — i.e., that MV starting devices (Starting VFDs) for at least the inlet/sales gas compressor motors KM-2150/2250 are part of the 6.9 kV facility basis — without assuming PKG-025 serves those specific motors. | Compare against DBM Deepcut MV MCC section (line 2955) and inlet/sales compressor driver section (line 893). |
| SOW-025-07 | The Scope of Work shall mark unsupported package-specific design values as `TBD`, including driven-equipment identity, VFD topology, output filter / harmonic mitigation, input/isolation transformer arrangement, bypass arrangement, enclosure rating, cooling method, environmental rating, weights, dimensions, and support loads. | Review against accessible sources and confirm no unsupported values are introduced. |
| SOW-025-08 | The Scope of Work shall preserve anticipated artifacts: package scope of work, tagged equipment and package identity list, package function and integration narrative, and responsibility assignment record. | Compare against `_CONTEXT.md` Anticipated Artifacts. |
| SOW-025-09 | The Scope of Work shall identify no declared critical upstream or downstream dependencies unless `_DEPENDENCIES.md` is later updated. | Compare against `_DEPENDENCIES.md` declared lists. |
| SOW-025-10 | The Scope of Work shall record the apparent rating discrepancy between this package title (5,000 hp at 6.9 kV) and the inlet/sales compressor driver rating (6,700 hp at 6.9 kV) so that downstream documents do not silently equate them. | Cross-reference DBM line 893 and workbook Packages row 27; capture in Guidance Conflict Table. |

## Standards

| Standard / basis | Status |
|---|---|
| Gate 7 PROJECT_DECOMP snapshot | Authoritative accepted decomposition basis for package, deliverable, objective, artifact, scope, and interface registers. |
| Workbook Packages row 27 | Authoritative source row for package identity and interface flags. |
| DBM Deepcut electrical basis | Accessible facility-level source for 6.9 kV MV service context, grounding, cabling, MV motor starting basis, and electrical building basis. |
| Package-specific MV VFD standards (e.g., IEEE 519, IEC 61800 series, NEMA ICS 7-series, NFPA 70 / CSA C22.1 articles applicable to MV drives) | TBD; not present in accessible source slices for this deliverable. |
| Vendor MV VFD specifications and datasheets | TBD; not present in accessible source slices for this deliverable. |

## Verification

- Verify identity fields against workbook Packages row 27 and Gate 7 `PACKAGE_REGISTER.csv`.
- Verify deliverable role against Gate 7 `PROJECT_DECOMP.md` mandatory EPC anchor deliverable basis.
- Verify responsibility split against Gate 7 `PACKAGE_REGISTER.csv` row PKG-025.
- Verify interface list against workbook row 27 and Gate 7 `INTERFACE_REGISTER.csv` rows for PKG-025.
- Verify facility MV service context against DBM Deepcut electrical power distribution table, grounding section, MV cable section, MV MCC section, and electrical building section.
- Confirm each package-specific technical value is source-supported or marked `TBD`.
- Confirm cross-document terminology uses `MV VFD - 5000HP, 6.9kV, 3PH, 60HZ - 6.9kV VFD` as the source spelling.

## Documentation

The Scope of Work package shall produce or preserve:

- package scope of work;
- tagged equipment and package identity list, with tag values marked `TBD` when unavailable;
- package function and integration narrative;
- responsibility assignment record;
- interface basis for Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports;
- list of source limitations, TBDs, assumptions, and human ruling items.
