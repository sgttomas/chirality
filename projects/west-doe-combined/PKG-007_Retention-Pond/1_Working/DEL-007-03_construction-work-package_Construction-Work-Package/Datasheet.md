# Datasheet: DEL-007-03 Construction Work Package

## Identification

| Field | Value |
|---|---|
| Deliverable ID | DEL-007-03_construction-work-package |
| Deliverable name | Construction Work Package |
| Parent package | PKG-007 - Retention Pond |
| Workbook basis | Workbook Packages row 8 |
| WBS | 02 |
| CoA tracking number | 26020-02-42-007 |
| Discipline | Civil |
| Type | EPC Construction Work Package |
| Responsible party | EPC Integrator |
| Scope item | SOW-0007 |
| Accepted decomposition snapshot | `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package function | Civil package for the Retention Pond under WBS 02 with recorded physical interfaces. | `PACKAGE_REGISTER.csv`, PKG-007 |
| Scope statement | Carry the workbook-defined Civil package "Retention Pond" as a distinct flat project package for WBS 02. | `SCOPE_LEDGER.csv`, SOW-0007 |
| Construction work package purpose | Describe physical installation, construction, tie-in, inspection, and turnover into larger systems. | `PROJECT_DECOMP.md` lines 118-127; `ARTIFACT_REGISTER.csv`, ART-2320994953 |
| Anticipated artifacts | Construction work package; installation and tie-in workface plan; construction interface and turnover checklist. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv`, DEL-007-03 |
| Declared package interfaces | Drain / Containment; Grading / Site Drainage / Spill Containment. | `INTERFACE_REGISTER.csv`, IFC-AB14FD2A67 and IFC-1B8CFB3D40 |
| Objective context | OBJ-002, OBJ-007, OBJ-008, OBJ-009, OBJ-010 are mapped to this deliverable; use as directional context, not clause-level construction requirements. | `OBJECTIVE_DELIVERABLE_MAP.csv`, DEL-007-03 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Facility context | 03-25 West Doe Compressor Station and Liquids Hub at LSD 03-25-80-15W6, north of Dawson Creek, British Columbia. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Facility Overview |
| Surface-water basis | Current rainfall basis uses NBCC 2020 Dawson Creek intensity-duration-frequency data as a proxy pending site-specific update. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-02/meteorological basis |
| Retention pond uncertainty | Civil drainage, retention pond sizing, and surface-water management carry uncertainty until final hydrology inputs are confirmed. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-02 |
| Civil design basis | Civil design covers grading, drainage, roads, surface-water management, retention pond, piling/foundations, module supports, tank foundations, pipe rack supports, truck-loading slabs, building foundations, fencing, and security. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-11 |
| Final geotechnical dependency | Final geotechnical report is required before foundation design closure. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-11 |
| Stormwater/regulatory basis | Project water use, watercourse interaction, diversion, discharge, produced-water handling, stormwater management, and related activities must comply with applicable BC water legislation and regulator requirements; detailed regulatory review remains required. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-15 |

## Construction

| Construction element | Required treatment in this CWP | Source |
|---|---|---|
| Workface planning | Include a workface plan for installing/building the package and connecting it to adjacent process, utility, electrical, controls, civil, structural, and safety systems as applicable. | `ARTIFACT_REGISTER.csv`, ART-D5E162ED55 |
| Interface and turnover checklist | Include construction-facing interface, tie-in, inspection, and turnover evidence for the approved package. | `ARTIFACT_REGISTER.csv`, ART-0FDA9BD0DD |
| Drain / containment interface | Address package tie-ins to drain and containment interfaces. Specific routing, tie-in points, and acceptance criteria are TBD. | `INTERFACE_REGISTER.csv`, IFC-AB14FD2A67 |
| Grading / site drainage / spill containment interface | Address grading, site drainage, and spill-containment interfaces. Specific grades, slopes, elevations, and discharge/pump-out criteria are TBD. | `INTERFACE_REGISTER.csv`, IFC-1B8CFB3D40 |
| Surface-water management | Prevent uncontrolled offsite discharge, protect process areas, and support construction and operations access. Process-contaminated drainage must route to appropriate drain or containment systems rather than surface-water discharge. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-11 |
| Construction values | Pond location, pond capacity, final hydrology inputs, detailed drainage design, survey/grade surface file, and detailed geotechnical inputs are TBD. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-02 and SEC-11 |

## References

- `_CONTEXT.md` for deliverable identity, scope, artifacts, and local context.
- `_REFERENCES.md` for accepted decomposition and source pointers.
- `DELIVERABLE_REGISTER.csv`, `PACKAGE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, `SCOPE_LEDGER.csv`, and `OBJECTIVE_DELIVERABLE_MAP.csv` in the Gate 7 snapshot.
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, especially Facility Overview, SEC-02 meteorological basis, SEC-11 civil/layout basis, and SEC-15 regulatory basis.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` was checked for similar civil retention-pond basis but is not treated as the controlling source for this WBS 02 package.
