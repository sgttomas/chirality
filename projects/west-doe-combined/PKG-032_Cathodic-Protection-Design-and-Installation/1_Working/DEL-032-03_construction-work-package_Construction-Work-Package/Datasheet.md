# Datasheet: DEL-032-03_construction-work-package

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-032-03_construction-work-package` | `_CONTEXT.md` |
| Deliverable name | Construction Work Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-032` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | Cathodic Protection Design and Installation | Workbook Packages row 34; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 32 / row 34 | Workbook Packages row 34; `PACKAGE_REGISTER.csv` |
| WBS | 03 | `PACKAGE_REGISTER.csv` row `PKG-032` |
| CoA tracking number | 26020-03-30-023 | `PACKAGE_REGISTER.csv` row `PKG-032` |
| Discipline | Electrical | `PACKAGE_REGISTER.csv`; `_CONTEXT.md` |
| Deliverable type | EPC Construction Work Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | EPC Integrator | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. EPC Integrator owns integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-032` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Package class | Vendor-owned Electrical package; EPC Integrator owns construction/integration into the facility | `PACKAGE_REGISTER.csv` row `PKG-032` |
| Package function | Cathodic protection design and installation for buried/submerged metallic assets within the 03-25 Comp and Liquids facility scope; cathodic protection is identified as part of the electrical design scope. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Electrical Design Scope section (line 770: "Lighting, receptacles, electric heat tracing, building heaters, and cathodic protection are part of the electrical design scope") |
| Protected assets list | `TBD`. The DBM identifies cathodic protection as in-scope at the facility level but does not enumerate the specific protected assets (tanks, buried piping, vessels, casings, structural piles) attributable to PKG-032. Asset list shall be confirmed during detailed design from plot plan, piping, and tankage drawings. | Source gap; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` does not enumerate CP-protected items |
| CP system type (impressed-current vs. galvanic) | `TBD`. Not specified in accessible source slices for PKG-032. | Source gap |
| Test station / rectifier configuration | `TBD`. Not specified in accessible source slices. Vendor package outputs (`DEL-032-04`) will establish rectifier count, test station layout, and reference electrode placements. | Source gap; vendor engineered package not yet produced |
| Coating / corrosion coordination | Materials/coatings basis falls under project painting, insulation, coating, corrosion, and sour-service requirements; package-specific coordination with CP is `TBD`. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Standards and References table (line 897) |
| Installation location (CP equipment / rectifier shelter) | `TBD`. Not assigned in accessible source slices. | Source gap |
| Module/skid lift, set, and shipping basis | `TBD`. Vendor package lift plan, shipping configuration, and rigging are vendor-package outputs not yet available. | Source gap; `DEL-032-04` not yet produced |
| Turnover and handover basis | `TBD`. Construction interface and turnover checklist artifact required (`ART-9C1116778C`); detailed turnover acceptance criteria depend on vendor package documents and facility electrical commissioning plan. | `ARTIFACT_REGISTER.csv` row `ART-9C1116778C`; source gap on vendor turnover content |

## Conditions

| Interface / condition | Construction-package basis | Source |
|---|---|---|
| Electrical Power | Construction work package shall plan and execute power feed(s) to CP rectifier(s) or impressed-current equipment per facility electrical distribution basis; CP is part of the electrical design scope. Voltage class, feeder size, breaker source, and MCC bucket assignment are `TBD` pending detailed design. | `INTERFACE_REGISTER.csv` `IFC-C2719906C1`; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Electrical Design Scope (line 718, 770) |
| Grounding / Bonding | Construction shall coordinate CP system with the facility grounding/bonding scheme so cathodic protection performance is not compromised by direct bonding of protected assets to the ground grid; cable tray, conduit, grounding, and bonding shall comply with project electrical specifications and detailed design. Decoupling/isolation device requirements are `TBD`. | `INTERFACE_REGISTER.csv` `IFC-F1FE9DF9DD`; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Cable, Tray, and Bonding paragraph (line 768) |
| I&C / Control Cabling | Construction work package shall include installation and termination of CP monitoring/control cabling (rectifier status, test-station leads, remote-monitoring telemetry) routed in plant cable tray/conduit, with power/signal segregation per the DBM. Cable schedules, termination details, and signal types are `TBD` pending vendor data. | `INTERFACE_REGISTER.csv` `IFC-4D092EC70F`; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, cable/segregation paragraph (line 768) |
| Communications / Network | Construction work package shall include any network/communications cabling required for CP remote monitoring or integration with the plant control/monitoring network. Protocol (Modbus TCP/IP, hardwired, protocol converter via Kepware/Redlion DA30D) is `TBD` pending vendor data. | `INTERFACE_REGISTER.csv` `IFC-8594557BD3`; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Package and Third-Party Interfaces paragraph (line 812) |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Construction execution party | Facility construction scope includes construction management, grading, piling, foundations, roads, field buildings, offloading and setting of modules, mechanical hookups, installation of shipped-loose instruments and valves, pipe supports, ISBL/OSBL interconnecting piping, home-run cabling, terminations, area lighting, fencing, security systems, and demolition/removal where required for project tie-ins. CP installation falls under this construction scope as an electrical sub-scope. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Construction Scope Summary (line 75) |
| EPC Integrator scope | Facility integration, tie-ins, constructability, procurement/construction coordination, and facility-level integration for the package. | `PACKAGE_REGISTER.csv` row `PKG-032` |
| Package Vendor scope | Package engineering, package design, vendor documentation, and the physical equipment package — not facility construction. | `PACKAGE_REGISTER.csv` row `PKG-032` |
| Workface planning artifact | Installation and tie-in workface plan covering electrical power, grounding/bonding, I&C/control cabling, communications/network, civil (rectifier shelter / anode bed / test station foundations), and safety provisions for a cathodic protection package. | `ARTIFACT_REGISTER.csv` row `ART-7FA44ED0D3` |
| Construction interface and turnover artifact | Construction-facing interface, tie-in, inspection, and turnover checklist evidence for the approved CP package. | `ARTIFACT_REGISTER.csv` row `ART-9C1116778C` |
| Tie-in coordination basis | Construction work package register shall be aligned to the plot plan and equipment list before issue for construction; cross-facility interface corridors and tie-in handoffs apply to 04-25, NRM, and pipeline scopes. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Miscellaneous Facilities (line 661); General Site Layout (line 681) |
| Anode bed / groundbed civil basis | `TBD`. Foundation type, trenching depth, backfill (coke breeze / native soil), groundbed geometry (deep-well vs. surface horizontal), and area requirements are not specified in accessible source slices and require vendor CP design output. | Source gap; vendor engineered package (`DEL-032-04`) not yet produced |
| Pre-commissioning / energization | `TBD`. Native potential survey, system commissioning potentials, interference testing with adjacent buried metallic systems, rectifier energization, and acceptance criteria are typical for a CP system but are not specified by an accessible source slice for PKG-032. Steps and acceptance values shall be established during detailed engineering and vendor coordination. | Source gap; not derived from decomposition prose |
| Winterization / site conditions | Site design ambient -40 deg C to +35 deg C; rectifier shelter, anode bed installation method, and trenching schedule shall account for winter operation. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Design Implications (line 145); Roads and Access (line 696) |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-032-03_construction-work-package`.
- `PACKAGE_REGISTER.csv`, row `PKG-032`.
- `ARTIFACT_REGISTER.csv`, rows for `DEL-032-03_construction-work-package` (`ART-655045CC72`, `ART-7FA44ED0D3`, `ART-9C1116778C`).
- `INTERFACE_REGISTER.csv`, rows for `PKG-032` (`IFC-C2719906C1`, `IFC-F1FE9DF9DD`, `IFC-4D092EC70F`, `IFC-8594557BD3`).
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-032-03_construction-work-package` (OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010).
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 34.
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Construction Scope Summary, Electrical Design Scope, Cable/Tray/Bonding, Package and Third-Party Interfaces, Miscellaneous Facilities, General Site Layout, Design Implications source slices.
- `_Sources/26020-Package_Requirements.docx`, searched for package-specific cathodic-protection construction content; no source slice locally extracted for PKG-032 CP construction execution detail (recorded as `TBD`/`location TBD`).
