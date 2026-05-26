# Specification — DEL-103-03 Construction Work Package (PKG-103 Pipe Rack Modules)

> Normative requirements for the Construction Work Package artifact (the document) and the construction execution it governs. Requirements are source-grounded where evidence exists; inferred requirements are labeled **ASSUMPTION**; values not present in accessible sources are marked `TBD`.

## Scope

### In scope

- Authoring, content, and structure of the EPC Construction Work Package for PKG-103 Pipe Rack Modules.
- Field installation, mechanical hookup, inspection, testing, turnover, and facility tie-ins for the pipe rack modules covered by `SOW-0259`.
- All declared physical interfaces of PKG-103: Process Piping; Utility Piping; Relief/Flare/Vent; Electrical Power; EHT; I&C/Control Cabling; Communications/Network; Grading/Site Drainage/Spill Containment; Structural/Foundations/Supports. (`PACKAGE_REGISTER.csv`; `INTERFACE_REGISTER.csv`)

### Out of scope

- Vendor package selection and design for non-pipe-rack equipment hosted on the rack. Pipe racks and pipe rack modules themselves are designed exclusively by the EPC Integrator (Gate 6 disposition; `INTERFACE_REGISTER.csv`).
- Process design and equipment design contained in other PKG-103 deliverables (`DEL-103-01`, `DEL-103-02`, `DEL-103-04`).
- Other facility packages and their internal construction work packages.

## Requirements

### REQ-CWP-1 — Artifact composition

The Construction Work Package shall consist of: (a) the construction work package document, (b) an installation and tie-in workface plan, and (c) a construction interface and turnover checklist. (`_CONTEXT.md` anticipated artifacts; `DELIVERABLE_REGISTER.csv`)

### REQ-CWP-2 — Installation and setting

The package shall specify off-loading and setting of pipe rack modules on foundations consistent with the Tourmaline field construction scope for "setting modules, pipe racks, and equipment on foundations." (`DBM-Deepcut/4-25_Deepcut_DBM.md` line 113)

### REQ-CWP-3 — Mechanical hookup

The package shall specify mechanical hookup of modules, equipment, and interconnecting piping at the rack, consistent with the construction scope statement. (`DBM-Deepcut/4-25_Deepcut_DBM.md` line 114)

### REQ-CWP-4 — Skid-edge isolation

The package shall locate skid-edge isolation in the interconnect piping between the pipe rack and the module, processing unit, or building. (`DBM-Deepcut/4-25_Deepcut_DBM.md` line 2454)

### REQ-CWP-5 — Foundations and supports

The package shall execute pipe rack foundations and supports per a design grounded in the final geotechnical report and addressing equipment loads, snow/wind/seismic design criteria, frost protection, vibration, settlement, and maintenance access. (`DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 688, 700)

### REQ-CWP-6 — Cold-climate construction

The package shall plan and execute work consistent with the site -40 deg C minimum ambient and the project's winter-operation accommodation for module delivery, road access, drainage, and foundation work. (`DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 145, 696)

### REQ-CWP-7 — Area classification compliance

Construction shall preserve the area-classification basis that outdoor pipe racks are general-purpose non-hazardous areas unless detailed classification drawings identify otherwise. Where detailed classification drawings impose hazardous-area requirements on rack locations, the construction work package shall reflect them. (`DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 722)

### REQ-CWP-8 — Interface coverage

The construction interface and turnover checklist shall cover every declared physical interface for PKG-103: Process Piping, Utility Piping, Relief/Flare/Vent, Electrical Power, EHT, I&C/Control Cabling, Communications/Network, Grading/Site Drainage/Spill Containment, and Structural/Foundations/Supports. (`INTERFACE_REGISTER.csv` IFC-1B5D83EC66, IFC-AECC45897E, IFC-933A9B9DC3, IFC-3268483707, IFC-489CEA5AA8, IFC-FC76A7E07D, IFC-38D5605A15, IFC-E2FEA8FA23, IFC-BC9813EE49)

### REQ-CWP-9 — Rack-supported commodity verification

Rack-supported commodities shall be confirmed against the plot plan and 3D model prior to construction release. (`PACKAGE_REGISTER.csv` and `INTERFACE_REGISTER.csv` rows: "Rack-supported commodities should be confirmed against plot plan/model.")

### REQ-CWP-10 — EHT (electrical heat tracing) provisioning

Where rack-supported lines require winterization, the package shall include EHT installation, terminations, and commissioning consistent with the winterization drivers identified in the design basis. (`DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 145; interface IFC-489CEA5AA8) — **ASSUMPTION**: the specific lines requiring EHT are detailed-design output and are `TBD` at this stage.

### REQ-CWP-11 — Inspection, testing, turnover (ITT)

The package shall define inspection, testing, and turnover steps for structural erection, piping completion, electrical/EHT/I&C continuity, and grading/drainage tie-ins. Specific ITT acceptance criteria are `TBD` (not present in accessible sources). — **ASSUMPTION** content-shape; values `TBD`.

### REQ-CWP-12 — Responsibility

The Construction Work Package is authored and executed under the EPC Integrator. (`_CONTEXT.md`; Gate 6 disposition recorded in `INTERFACE_REGISTER.csv`)

## Standards

| Standard | Applicability | Location |
|---|---|---|
| API RP 505 | Cited basis for treating process modules/buildings as Zone 2 hazardous areas using fugitive-emission studies; outdoor racks default to general-purpose non-hazardous | `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 722 |
| Site geotechnical report (final) | Required input for foundation design closure | `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 688; **location TBD** (report not in accessible source set) |
| Structural / piping / electrical jurisdictional codes | Applicable to construction execution | **location TBD** — not enumerated in accessible source set; **ASSUMPTION** likely applicable |
| Project welding, NDE, hydrotest, and torque specifications | Applicable to mechanical hookup ITT | **location TBD** — not enumerated in accessible source set; **ASSUMPTION** likely applicable |

## Verification

| Requirement | Verification approach |
|---|---|
| REQ-CWP-1 | Document completeness audit — three sub-artifacts present |
| REQ-CWP-2 | Construction execution records; module-setting reports vs. foundation set tolerances (tolerances `TBD`) |
| REQ-CWP-3 | Hookup completion records, line walk-down sign-offs |
| REQ-CWP-4 | Walk-down confirming skid-edge isolation valves in interconnect piping between rack and each module/unit/building |
| REQ-CWP-5 | Foundation QC records traceable to geotechnical report and design loads |
| REQ-CWP-6 | Winter-construction execution records; cold-weather work permits |
| REQ-CWP-7 | Cross-check against issued area-classification drawings; field marking inspection |
| REQ-CWP-8 | Turnover checklist completeness audit covering all nine interface types |
| REQ-CWP-9 | Pre-release sign-off against plot plan and 3D model |
| REQ-CWP-10 | EHT continuity / megger tests; commissioning records (criteria `TBD`) |
| REQ-CWP-11 | ITT records signed off by EPC Integrator construction QA (acceptance criteria `TBD`) |
| REQ-CWP-12 | EPC Integrator approval block on the package |

## Documentation

The deliverable shall produce (per `_CONTEXT.md` anticipated artifacts):

1. Construction work package (root document).
2. Installation and tie-in workface plan.
3. Construction interface and turnover checklist.

Supporting evidence retained: weld maps, NDE reports, hydrotest packs, torque records, electrical continuity records, EHT commissioning records, structural QC records, foundation QC records, area-classification walkdown reports — specific record forms are **`TBD`** (not in accessible sources).
