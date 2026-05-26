# Datasheet — DEL-103-03 Construction Work Package (PKG-103 Pipe Rack Modules)

> Descriptive register of the constructed asset and the construction-work-package artifact attributes. Values are source-grounded where evidence exists; otherwise marked `TBD` or labeled **ASSUMPTION**.

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-103-03_construction-work-package` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Deliverable Name | Construction Work Package | `_CONTEXT.md` |
| Parent Package | `PKG-103` Pipe Rack Modules | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Workbook ID | 103 (Workbook Packages row 104) | `PACKAGE_REGISTER.csv` |
| CoA Tracking Number | `26020-03-36-003` | `PACKAGE_REGISTER.csv` |
| WBS | 03 | `PACKAGE_REGISTER.csv` |
| Discipline | Structural | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Type | EPC Construction Work Package | `_CONTEXT.md` |
| Responsible Party | EPC Integrator | `_CONTEXT.md`; Gate 6 disposition (interface register) |
| Covers Scope Items | `SOW-0259` | `_CONTEXT.md` |
| Supports Objectives | OBJ-002; OBJ-005; OBJ-006; OBJ-007; OBJ-008; OBJ-009; OBJ-010 | `_CONTEXT.md`; `OBJECTIVE_DELIVERABLE_MAP.csv` (PACKAGE_HEURISTIC, **ASSUMPTION** at deliverable-row granularity) |

## Attributes (Constructed Asset — Pipe Rack Modules)

| Attribute | Value | Source |
|---|---|---|
| Asset class | Outdoor structural pipe rack modules supporting interconnecting commodities between process modules, processing units, and buildings | `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 75, 688 |
| Module delivery mode | Modular: modules are shipped to site, off-loaded, and set on foundations | `DBM-Deepcut/4-25_Deepcut_DBM.md` lines 111-113 |
| Setting responsibility | Tourmaline field construction scope (setting modules, pipe racks, and equipment on foundations) | `DBM-Deepcut/4-25_Deepcut_DBM.md` line 113 |
| Mechanical hookup | Mechanical hookup of modules, equipment, and interconnecting piping is field construction scope | `DBM-Deepcut/4-25_Deepcut_DBM.md` line 114 |
| Foundation basis | Pipe rack supports are part of civil/foundation design driven by final geotechnical report, equipment loads, snow/wind/seismic, frost protection, vibration, settlement, maintenance access | `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 688, 700 |
| Area classification | Outdoor pipe racks are general purpose non-hazardous areas unless detailed classification drawings identify otherwise | `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 722 |
| Skid-edge isolation | Isolation located in interconnect piping between the pipe rack and the module/processing unit/building | `DBM-Deepcut/4-25_Deepcut_DBM.md` line 2454 |
| Design ownership | Pipe racks and pipe rack modules are designed exclusively by the EPC Integrator (Gate 6 disposition) | `INTERFACE_REGISTER.csv` (IFC-1B5D83EC66, IFC-AECC45897E, IFC-933A9B9DC3, IFC-3268483707, IFC-489CEA5AA8, IFC-FC76A7E07D, IFC-38D5605A15, IFC-E2FEA8FA23, IFC-BC9813EE49) |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Site ambient (minimum design) | -40 deg C governs exposed equipment, package buildings, control panels, instrumentation, and field devices unless more severe applies | `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 145 |
| Winterization drivers | Electrical heat tracing, building heating, road access, drainage, foundations, structural steel design, module layout | `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 145 |
| Seasonality | Road, foundation, and module setting work must account for winter operation | `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 696 |
| Geotechnical | Final geotechnical report required before foundation design closure | `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 688 |
| Spill/drainage interface | Rack area drainage and grading interface present | `INTERFACE_REGISTER.csv` (IFC-E2FEA8FA23) |

## Construction (Work-Package Artifact Composition)

| Component | Description | Source |
|---|---|---|
| Construction work package (root artifact) | The bound EPC document describing how the package will be physically installed, built, inspected, turned over, and tied into the larger facility systems | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Installation and tie-in workface plan | Workface-level plan covering installation sequencing and tie-ins to upstream/downstream systems | `_CONTEXT.md` (anticipated artifacts) |
| Construction interface and turnover checklist | Interface-by-interface and turnover-readiness checklist for the package | `_CONTEXT.md` (anticipated artifacts) |
| Interface coverage | Process Piping; Utility Piping; Relief/Flare/Vent; Electrical Power; EHT; I&C/Control Cabling; Communications/Network; Grading/Site Drainage/Spill Containment; Structural/Foundations/Supports | `PACKAGE_REGISTER.csv`; `INTERFACE_REGISTER.csv` |

## References

- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` (deliverable-local)
- Gate 7 snapshot registers: `DELIVERABLE_REGISTER.csv`, `PACKAGE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, `OBJECTIVE_DELIVERABLE_MAP.csv`
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`
- `_Sources/26020-Package_Requirements.docx` — **location TBD** (binary `.docx` not extracted in this run)
- `_Sources/26020-Packages_Interfaces_4_export.xlsx` — **location TBD** (binary `.xlsx` not extracted in this run)
