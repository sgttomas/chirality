# Datasheet — DEL-062-03 Construction Work Package (NGL Loading Pumps Building)

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | DEL-062-03_construction-work-package | `_CONTEXT.md` |
| Name | Construction Work Package | `_CONTEXT.md` |
| ParentPackageID | PKG-062 | `_CONTEXT.md` |
| PackageName | NGL Loading Pumps Building | `_CONTEXT.md` |
| Discipline | Mechanical | `_CONTEXT.md` |
| Type | EPC Construction Work Package | `_CONTEXT.md` |
| ResponsibleParty | EPC Integrator | `_CONTEXT.md` |
| Decomposition Snapshot | GATE-07_Final_Published_2026-05-24 | `_REFERENCES.md` |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Covers Scope Items | SOW-0153, SOW-0154, SOW-0155, SOW-0156 | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row 422 |
| Supports Objectives | OBJ-001, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 | `_CONTEXT.md`; `OBJECTIVE_SCOPE_MAP.csv` (PKG-062 rows) |
| Gate Anchor | Gate 5 EPC anchor deliverable (mandatory) | `_CONTEXT.md` Notes |
| Artifacts | Construction work package; installation and tie-in workface plan; construction interface and turnover checklist | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row 422 |

## Conditions (Package Scope Being Installed)

| Attribute | Value | Source |
|---|---|---|
| Package Function | Truck/loading NGL loading service via four rotary-vane pumps housed in a dedicated building | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2549, line 2610 |
| Pump Tags | P-9510-1, P-9520-1, P-9530-1, P-9540-1 | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2610 |
| Pump Count | 4 | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2549, line 2610 |
| Pump Type | Rotary vane | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2610 |
| Facility Area (LSD) | 4-25 (Deepcut) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2610 |
| Building Type | Dedicated equipment building for NGL loading pumps | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2549 (package name "NGL Loading Pumps Building") |
| Service Stream | NGL (mercaptan-treated, dehydrated NGL product) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 73 (ASSUMPTION on connecting service path) |

## Construction (Work Package Scope Indicators)

| Attribute | Value | Source |
|---|---|---|
| Civil/Structural scope | Building foundation, slab, structural steel, building enclosure for housing four pumps | TBD — specific civil/structural scope and dimensions not in locally accessible sources |
| Mechanical scope | Setting and alignment of P-9510-1 through P-9540-1; suction/discharge piping; vent/drain; relief; pump skids | ASSUMPTION based on pump tag list (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2610) |
| Piping tie-ins | NGL feed from NGL Booster and Transfer Pumps Building; discharge to truck/loading interfaces | ASSUMPTION based on package adjacency (Package 58 NGL Booster and Transfer Pumps Building; line 2548, 2609); confirm in DEL-062-02 Package Datasheet |
| Electrical scope | Motor power feeds for four pumps; building lighting, small power, grounding | TBD — specific drivers/voltages not in locally accessible sources |
| Instrumentation scope | Pump local instrumentation, control interface to host DCS; flow, pressure, temperature, vibration as required | TBD — instrument index for this package not in locally accessible sources |
| HVAC scope | Building ventilation classified for NGL service | TBD — classification and air change rate not in locally accessible sources |
| Grounding | Facility main ground grid connection for building and equipment | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2993 (truck-loading grounding context; ASSUMPTION extending principle to NGL loading building) |

## References

- `_REFERENCES.md` (deliverable-local)
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (Deepcut Design Basis Memorandum)
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` row 422
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/OBJECTIVE_SCOPE_MAP.csv` (PKG-062 rows)
- `_Sources/26020-Package_Requirements.docx` package heading 16 — location TBD (not locally accessible as text)
- `_Sources/26020-Packages_Interfaces_4_export.xlsx` row 76 — location TBD (not locally accessible as text)
