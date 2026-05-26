# Datasheet — DEL-103-02 Package Datasheet (PKG-103 Pipe Rack Modules)

> Descriptive document. Values are **source-grounded**; unknowns are marked **TBD**; inferences are labeled **ASSUMPTION**. Decomposition is the routing surface; authoritative content comes from the DBM source slices cited below.

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-103-02_package-datasheet` |
| DeliverableName | Package Datasheet |
| ParentPackageID | `PKG-103` |
| PackageName | Pipe Rack Modules |
| ParentWorkbookID | 103 |
| Discipline | Structural |
| Type | EPC Package Datasheet |
| ResponsibleParty | EPC Integrator |
| CoversScope | `SOW-0259` |
| SupportsObjectives | `OBJ-002`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` (ASSUMPTION — package-grouping heuristic via decomposition row 585) |
| DecompRow | DELIVERABLE_REGISTER.csv row 585 (GATE-07 Final Published 2026-05-24) |
| Status | OPEN at task start; INITIALIZED upon completion of this pass |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package scope identity | Pipe Rack Modules — shop-fabricated modular pipe-rack assemblies carrying primary plant interconnect piping, cable trays, electric heat tracing, and supporting steel | DBM-Deepcut §General — `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` L2999, L3023, L3047; DBM-Comp_and_Liquids — `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` L38 |
| Primary structural function | Elevated, equal-elevation ridge structures supporting interconnecting piping between process modules, electrical buildings, and tank/loading areas | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` L2708–L2709 |
| Cable tray integration | Main cable tray runs pre-installed in shop on dedicated structural modules at the uppermost section of the pipe rack; future-growth capacity (cable tray) at least 30% | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` L2999, L3023 |
| Heat-tracing integration | Most electric heat tracing installed by Propak on pipe-rack modules; combined heat-traced lines between adjacent racks where possible; wired to pipe-rack junction boxes in conduit | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` L3047 |
| Heat-tracing electrical | Self-regulating 208 V 1Ø 60 Hz primary; 120 V 1Ø 60 Hz for short lines / instrument tubing; fed from local transformers and heat-tracing distribution panels located along the pipe rack | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` L3059 |
| Alarm beacon / horn provisions | Visual beacons and audible horns installed at strategic outdoor locations on piperacks | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` L3262, L3264, L3293, L3296 |
| Skid-edge interface convention | Isolation located in the interconnect piping between the pipe rack and the module / processing unit / building | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` L2454–L2457 |
| Module sizing / weight envelope | TBD — not specified in locally accessible source slices |
| Tonnage / steel quantities | TBD — not specified in locally accessible source slices |
| Module count | TBD — not specified in locally accessible source slices |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Hazardous area classification (outdoor pipe rack) | General purpose / non-hazardous unless detailed classification drawings identify otherwise | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` L722; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` L2911 |
| Climatic / seismic / snow / wind loading | Per project-wide structural basis; specific values TBD — values not in locally accessible source slices | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` L700 (foundation design basis enumerated); detailed magnitudes location TBD |
| Vibration / settlement / frost / maintenance-access design factors | Required for equipment-specific anchorage including pipe racks | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` L700 |
| Site grading interaction | Facility pad slopes down from pipe racks at 1.5% to each side; main pipe rack grading uses high equal-elevation ridges | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` L2708–L2709 |
| Containment interaction (NGL area) | NGL storage area grading sloped to redirect spill AWAY from pipe rack and process areas | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` L2722 |
| Permanent lighting on cable-tray walkway | Not installed; walkway is construction / future-additions only | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` L3023 |
| Maintenance-access clearance | Cable tray routing shall not interfere with exchanger bundle removal, cranes / hoists, pumps, or valves | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` L3023 |

## Construction

| Item | Value | Source |
|---|---|---|
| Fabrication mode | Shop-fabricated modular assemblies, including pre-installed main cable tray runs | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` L2999 |
| Field-installation activities | Setting modules on foundations; field-run cable tray limited to field-constructed plant portions (tank farm, interconnect trays between main racks, process skids, electrical buildings); home-run heat-tracing cables run in field as required | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` L113, L2999, L3047 |
| Default foundation basis | Driven steel piles unless a more specific basis applies; final pile design parameters TBD pending geotechnical report | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` L2740, L2749 |
| Grounding / bonding | Pipe racks welded to piles; additional bonding conductors from cable tray down to piles not required; main grounding conductor #2/0 green insulated in highest-voltage-carrying tray | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` L2987 |
| Trace heating distribution | Local transformers and heat-tracing distribution panels located along the pipe rack; transformers fed from motorized/trip MCC feeder breakers to allow staged energization | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` L3059 |
| Construction interface party | Module setting on foundations is Tourmaline field construction scope (precedent from Deepcut DBM) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` L113 — ASSUMPTION: applies to PKG-103 unless EPC contract terms supersede |

## References

- `_REFERENCES.md`
- `_CONTEXT.md`
- Decomposition entry: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` row 585
- Package register: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv`
- Authoritative DBM source slices read for this pass:
  - `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` L38, L688, L700, L722
  - `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` L113, L2454–L2457, L2502, L2656, L2708–L2709, L2722, L2740, L2749, L2911, L2987, L2999, L3023, L3047, L3059, L3262, L3264, L3293, L3296
- Source materials referenced by decomposition row but **not locally accessible as text** (location TBD):
  - `_Sources/26020-Package_Requirements.docx` (binary; not converted to markdown)
  - `_Sources/26020-Packages_Interfaces_4_export.xlsx` (binary; not converted to markdown)

## Notes

- Mandatory Gate 5 EPC anchor deliverable; interface facts are intentionally carried here as evidence rather than as standalone deliverables (per `_CONTEXT.md`).
- Package-level quantitative data (module count, tonnage, dimensional envelope, weight) is **TBD** because the two workbook-form source artifacts (`26020-Package_Requirements.docx`, `26020-Packages_Interfaces_4_export.xlsx`) are not locally accessible as text.
