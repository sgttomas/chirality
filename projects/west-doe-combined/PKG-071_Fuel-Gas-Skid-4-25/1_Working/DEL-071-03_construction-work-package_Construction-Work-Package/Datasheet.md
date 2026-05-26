# Datasheet — DEL-071-03 Construction Work Package (Fuel Gas Skid 4-25)

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | DEL-071-03_construction-work-package | `_CONTEXT.md` |
| Deliverable Name | Construction Work Package | `_CONTEXT.md` |
| Parent Package | PKG-071 — Fuel Gas Skid 4-25 | `_CONTEXT.md` |
| Workbook Row | 61 | `_CONTEXT.md`; `_Decomposition/.../DELIVERABLE_REGISTER.csv` |
| Source Heading | `26020-Package_Requirements.docx` — `26020-01-PT-23-001 - Fuel Gas Skid` (4-25 West Doe Deepcut) | `_Sources/26020-Package_Requirements.docx`, Heading 1 (4-25 instance) |
| Discipline | Mechanical (EPC construction integration) | `_CONTEXT.md` |
| Type | EPC Construction Work Package | `_CONTEXT.md` |
| Responsible Party | EPC Integrator | `_CONTEXT.md` |
| Facility | West Doe Deep Cut Facility, 4-25 train | `26020-Package_Requirements.docx`, Location/Status line for 26020-01-PT-23-001 |

## Attributes (Package the CWP Will Install)

| Attribute | Value | Source |
|---|---|---|
| Package Identity | 26020-01-PT-23-001 — Fuel Gas Skid | `26020-Package_Requirements.docx`, Heading 1 (4-25 instance) |
| Process Function | Serves the low-pressure fuel gas system for the West Doe Deep Cut Facility | `26020-Package_Requirements.docx`, Basic Scope |
| Skid Count | 1 skid-mounted Low Pressure Fuel Gas Package | `26020-Package_Requirements.docx`, Basic Scope |
| Primary Equipment | 1 low-pressure fuel gas heater; 1 low-pressure fuel gas scrubber; supporting skid structure | `26020-Package_Requirements.docx`, Major Included Equipment |
| Heater Driver | SCR (600 V) electric heater with skin-temperature thermocouple override | `26020-Package_Requirements.docx`, Major Included Equipment |
| Design Flow | > 8.4 MMSCFD (237.5 e3m3/day); final flow TBD | `26020-Package_Requirements.docx`, Scope Notes / Open Items |
| Gas Outlet Temperature | 95 °F (35 °C) | `26020-Package_Requirements.docx`, Scope Notes / Open Items |
| Heater Capacity | TBD | `26020-Package_Requirements.docx`, Major Included Equipment |
| Scrubber Sizing Basis | k-factor sizing method (value TBD in source extract) | `26020-Package_Requirements.docx`, Major Included Equipment |
| By Others (excluded from vendor scope; required from EPC CWP) | Shipping to site; installation; tie-in piping; electrical tie-in | `26020-Package_Requirements.docx`, Scope Notes / Open Items |

## Conditions (Site/Service Conditions Relevant to Construction)

| Condition | Value | Source |
|---|---|---|
| Site | West Doe Deep Cut Facility, 4-25 train | `26020-Package_Requirements.docx`, Location/Status |
| Service | Low-pressure fuel gas conditioning (heat + scrubbing) | `26020-Package_Requirements.docx`, Basic Scope |
| Hazardous Area Classification | TBD (not extracted from source slice) | TBD |
| Climatic / Wind / Seismic Design Basis | TBD — refer to facility civil/structural design basis | TBD |
| Foundation Loading Inputs | From vendor STR-013 Anchor Bolt / Embedment Drawings and STR-005 Foundation Design Calculations | `26020-Package_Requirements.docx`, Vendor Engineering Deliverables (Structural) |

## Construction Scope Elements (Carried by This Deliverable)

| Element | Description | Source |
|---|---|---|
| Skid Receipt and Set | Receive, off-load, and set the vendor-supplied skid on foundations (vendor delivers FOB; site activities are EPC scope) | `26020-Package_Requirements.docx`, Scope Notes / Open Items ("By others: Shipping packages to site, installation, tie-in piping, electrical tie-in etc.") |
| Foundation Construction | Foundation construction per vendor STR-005/STR-006/STR-013 outputs | `26020-Package_Requirements.docx`, Vendor Engineering Deliverables (Structural section) |
| Tie-In Piping Construction | Process piping tie-ins (applicable = Yes); utility piping tie-ins (Yes); relief/flare/vent (Yes); drain/containment (Yes) | `26020-Package_Requirements.docx`, Physical Interface Summary |
| Electrical Tie-Ins | Electrical Power applicability per source = No at skid boundary; however SCR-driven heater requires 600 V supply terminated at skid — TBD reconciliation between table row "Electrical Power: No" and Major Included Equipment "SCR (600V)" (see Guidance Conflict Table) | `26020-Package_Requirements.docx`, Physical Interface Summary and Major Included Equipment |
| I&C / Control Cabling | Applicable = Yes; install and terminate per vendor INS-009/INS-010/INS-011 | `26020-Package_Requirements.docx`, Physical Interface Summary; Vendor Engineering Deliverables (Instrumentation) |
| Fire & Gas / Safety Systems | Applicable = Yes; integrate detectors and signals per vendor TSF-003/TSF-004 | `26020-Package_Requirements.docx`, Physical Interface Summary; Vendor Engineering Deliverables (Fire and gas) |
| Grounding / Bonding | Applicable = Yes; install per vendor ELE-019 Earthing/Bonding Layout | `26020-Package_Requirements.docx`, Physical Interface Summary; Vendor Engineering Deliverables (Electrical) |
| Area / Exterior Lighting | Applicable = Yes (per source row referencing interfaces file column M, row 99 — the corresponding interface file row is recorded in source but not opened here; ASSUMPTION: same row applies) | `26020-Package_Requirements.docx`, Physical Interface Summary |
| Maintenance Access | Applicable = Yes; provide platforms/ladders integrating vendor STR-011 | `26020-Package_Requirements.docx`, Physical Interface Summary |
| Structural Supports | Applicable = Yes; install per vendor STR-002 / STR-012 | `26020-Package_Requirements.docx`, Physical Interface Summary; Vendor Engineering Deliverables (Structural) |
| Not Applicable at Boundary | EHT (No); Cathodic Protection (No); Communications/Network (No); Building HVAC (No); Grading/Site Drainage (No); Product Loading (No); Pipeline/Pigging (No) | `26020-Package_Requirements.docx`, Physical Interface Summary |

## Construction Documentation Set (Anticipated Artifacts)

| Artifact | Source |
|---|---|
| Construction Work Package (this deliverable) | `_CONTEXT.md` Anticipated Artifacts |
| Installation and Tie-In Workface Plan | `_CONTEXT.md` Anticipated Artifacts |
| Construction Interface and Turnover Checklist | `_CONTEXT.md` Anticipated Artifacts |

## Scope and Objective Linkage

- Covers scope items: SOW-0099, SOW-0100, SOW-0101, SOW-0102 (source: `_CONTEXT.md`; `OBJECTIVE_SCOPE_MAP.csv`).
- Supports objectives (ASSUMPTION — package-grouping heuristic, not deliverable-explicit map): OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 (source: `_CONTEXT.md`).

## References

- `_CONTEXT.md` — deliverable identity, scope, anticipated artifacts.
- `_REFERENCES.md` — decomposition snapshot pointers; source roots.
- `_Sources/26020-Package_Requirements.docx` — Heading 1 `26020-01-PT-23-001 - Fuel Gas Skid` (4-25 West Doe Deepcut instance), subsections Basic Scope, Major Included Equipment, Physical Interface Summary, Vendor Engineering Deliverables.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx` — interface file referenced by source (rows 61 / 99 for lighting); not opened in this run — location TBD.
- Decomposition snapshot: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv`.
