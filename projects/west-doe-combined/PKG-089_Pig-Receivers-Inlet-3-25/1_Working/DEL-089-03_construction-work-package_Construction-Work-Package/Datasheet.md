# Datasheet: DEL-089-03 — Construction Work Package

> **Document role:** Descriptive — identifies the deliverable artifact and the entities, attributes, and conditions that the Construction Work Package (CWP) describes for PKG-089 *Pig Receivers (Inlet) 3-25*.

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-089-03_construction-work-package` |
| Deliverable name | Construction Work Package |
| Parent package | `PKG-089` — Pig Receivers (Inlet) 3-25 |
| Workbook row | 77 |
| Discipline | Mechanical |
| Type | EPC Construction Work Package |
| Responsible party | EPC Integrator |
| Decomposition basis | GATE-07_Final_Published_2026-05-24 PROJECT_DECOMP snapshot |
| Covers SOW | `SOW-0157`, `SOW-0158`, `SOW-0159`, `SOW-0160` |
| Supports objectives | `OBJ-002`, `OBJ-003`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package process function | Plant inlet pipeline gas enters the facility through the pig receivers and moves on into the inlet separators. | `_Decomposition/.../PACKAGE_REGISTER.csv` row PKG-089 (Process function) |
| Package configuration (per package register) | Two (2) identical 610 mm (24") OD pig receivers with ESDV on dedicated structural-steel non-enclosed skids. | `_Decomposition/.../PACKAGE_REGISTER.csv` row PKG-089 (Process function) |
| Package configuration (per DBM source) | Single combined three-phase pig receiver on structural-steel non-enclosed skid; sweet-gas purge and HP flare vent provisions; full-port piggable inlet ESDV with position transmitters. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` §"Inlet Pipeline Interface and Pigging" (lines 226–240) |
| Receiver size | 610 mm (24") OD per package register; DBM records receiver size as TBD. | PACKAGE_REGISTER.csv row PKG-089; DBM line 230 |
| Inlet ESDV | Full-port, piggable, position transmitters. | DBM lines 230, 239 |
| Inlet separator ESDV shutdown pressure | 635 psig (current basis). | DBM line 230 |
| Applicable interface types | Process Piping; Relief/Flare/Vent; Drain/Containment; Electrical Power; EHT; I&C/Control Cabling; Maintenance Access; Grading/Site Drainage/Spill Containment; Structural/Foundations/Supports; Pipeline/Pigging. | PACKAGE_REGISTER.csv row PKG-089 (Interface types) |
| Plant inlet boundary | First aboveground flange within lease boundary; Doe field pipeline contractor transfers scope to facility fabricator/construction contractor at this flange. | DBM line 228 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Service | Sour natural gas inlet pipeline; pig receipt and isolation. | DBM §SEC-04, line 244 |
| Pressure class | TBD at pig receiver level in accessible sources (inlet separators 600# per DBM line 253). | DBM line 253; pig receiver class — location TBD |
| Design pressure | TBD for pig receivers in accessible sources (inlet separator design pressure 4,963 kPag). | DBM line 254; pig receiver design pressure — location TBD |
| Purge / vent provisions | Sweet-gas purge and HP flare vent. | DBM line 238 |
| Slug / pigging management | No explicit pigging slug volume in source beyond separator slug handling (~38 m³). Operator manages pigging/flowback to avoid overrunning downstream capacity. | DBM lines 255, 270 |
| Delivery-point ESDV shutdown pressure | TBC (DBM). | DBM line 230 |

## Construction

The artifact this deliverable produces — the Construction Work Package itself — describes the means and methods by which the physical package will be installed, built, inspected, turned over, and tied into the larger facility. The CWP artifact set consists of:

| Sub-artifact | Description | Source basis |
|---|---|---|
| Construction work package | The bound CWP document defining means, methods, sequencing, and acceptance for field installation of the PKG-089 skid(s) and tie-ins. | DELIVERABLE_REGISTER.csv row DEL-089-03 ("Anticipated Artifacts") |
| Installation and tie-in workface plan | Workface-level execution plan addressing skid setting, piping tie-ins to the inlet pipeline and to the inlet separators, electrical/EHT/I&C tie-ins, relief/flare/vent tie-ins, drain/containment tie-ins, and structural/foundation interfaces. | DELIVERABLE_REGISTER.csv row DEL-089-03; PACKAGE_REGISTER.csv interface list |
| Construction interface and turnover checklist | Interface-by-interface acceptance and turnover checklist covering each applicable interface type and the EPC-Integrator-to-operations handoff. | DELIVERABLE_REGISTER.csv row DEL-089-03; PACKAGE_REGISTER.csv interface list |

## References

- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` — row `DEL-089-03_construction-work-package`.
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv` — row `PKG-089`.
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/OBJECTIVE_SCOPE_MAP.csv` — entries for SOW-0157..0160 / PKG-089.
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` — §"Inlet Pipeline Interface and Pigging" (lines 226–240); §"Inlet Separation" (lines 242–260); §"Slug and Flowback Basis" (lines 268–270).
- `_Sources/26020-Package_Requirements.docx` — package heading 42. **location TBD** (binary source not locally readable as text in this run).
- `_Sources/26020-Packages_Interfaces_4_export.xlsx` — Workbook Packages row 77. **location TBD** (binary source not locally readable as text in this run).
- `_Sources/Bid Docs/26020-02-PT-RFQ-35-001-Pig_Recv_1.docx` — referenced by PACKAGE_REGISTER.csv (Word Source Basis). **location TBD** (binary source not locally readable as text in this run).
