# Datasheet — DEL-052-04 Vendor Engineered Equipment Package (Inlet / TEG Dehy Cross Exchanger)

## Identification

| Field | Value |
|---|---|
| DeliverableID | DEL-052-04_vendor-engineered-equipment-package |
| Name | Vendor Engineered Equipment Package |
| ParentPackageID | PKG-052 |
| PackageName | Inlet / TEG Dehy Cross Exchanger |
| Discipline | Mechanical |
| Type | Vendor Package Production Unit |
| ResponsibleParty | Package Vendor (engineering/design/equipment) with EPC Integrator integration review |
| Primary Tagged Equipment | E-5718-1 (Inlet / TEG Dehy Cross Exchanger) [Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2586] |
| Covers Scope Items | SOW-0103; SOW-0104; SOW-0105; SOW-0106 |
| Supports Objectives | OBJ-001; OBJ-003; OBJ-004; OBJ-005; OBJ-006; OBJ-007; OBJ-008; OBJ-009; OBJ-010 |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Equipment class | Heat Exchangers (Shell and Tube) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2537 |
| Equipment subtype | Shell-and-tube; BEM type as described in DBM source | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` § "Inlet / TEG Dehy Cross Exchanger" (line 595) |
| Quantity | 1 | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 601 |
| Service | Heats inlet separator overhead gas; cools a downstream warm process gas stream upstream of process-gas molecular-sieve inlet filter/coalescers | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 606 |
| Facility unit | 4-25 (Deepcut) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2586 |

## Conditions

| Parameter | Value | Source |
|---|---|---|
| Design pressure | 9,756 kPag (1,415 psig) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 603 |
| Design temperature | 66 deg C | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 604 |
| Cold-side fluid | Inlet separator overhead gas | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 606 |
| Warm-side fluid | UNRESOLVED — current project information states both dehydrated overhead gas from the TEG contactor and warm sweet gas leaving the amine sweetening unit (CONFLICT — see Guidance.md Conflict Table) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 606 |
| Operating flows, temperatures, pressures (each side) | TBD — not stated in accessible source slice | location TBD |
| Heat duty | TBD | location TBD |
| Fouling allowance | TBD | location TBD |
| MDMT | TBD | location TBD |
| Corrosion allowance | TBD | location TBD |

## Construction

| Attribute | Value | Source |
|---|---|---|
| Configuration | Shell-and-tube, BEM (TEMA type per DBM source) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 602 |
| Materials of construction | TBD — not in accessible source slice; vendor to confirm against sour-gas service and design conditions | location TBD |
| Code of construction | ASME BPVC Section VIII Division 1 — ASSUMPTION (typical for pressure design pressure 9,756 kPag in this jurisdiction; not explicitly cited in source slice) | location TBD |
| Nozzle schedule and orientation | TBD | location TBD |
| Insulation / heat tracing | TBD | location TBD |
| Supports / mounting | TBD | location TBD |
| Shop vs field fabrication | TBD | location TBD |

## References

- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` § Inlet / TEG Dehy Cross Exchanger (lines 595-606), Equipment list rows (lines 2537, 2586)
- DEL-052-01 Scope of Work (sibling) — `PKG-052_Inlet-TEG-Dehy-Cross-Exchanger/1_Working/DEL-052-01_scope-of-work_Scope-of-Work/` — referenced for EPC scope basis (currently undrafted; treat as TBD).
- DEL-052-02 Package Datasheet (sibling) — referenced as the EPC technical handoff basis (currently undrafted; treat as TBD).
- 26020-Package_Requirements.docx, heading 7 — cited by decomposition row; full clause text not extracted into accessible markdown (location TBD).
