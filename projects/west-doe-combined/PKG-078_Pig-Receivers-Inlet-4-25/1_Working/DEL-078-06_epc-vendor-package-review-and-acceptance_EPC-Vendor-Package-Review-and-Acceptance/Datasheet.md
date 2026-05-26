# Datasheet — DEL-078-06: EPC Vendor Package Review and Acceptance

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-078-06_epc-vendor-package-review-and-acceptance` |
| Name | EPC Vendor Package Review and Acceptance |
| ParentPackageID | `PKG-078` |
| PackageName | Pig Receivers (Inlet) 4-25 |
| Discipline | Mechanical |
| Type | EPC Vendor Package Acceptance |
| ResponsibleParty | EPC Integrator (lead) with Package Vendor input |
| Facility | West Doe Deepcut (04-25) [SourcePath: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`; SectionRef: Facility Identification table] |
| Package roster line item | `61 — Pig Receivers (Inlet) 2 — Inlet Pig Receivers 2 — 4-25 (Deepcut) — equipment count 3` [SourcePath: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`; SectionRef: Package Line-Item Requirements row 61] |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Deliverable role | Review and acceptance evidence package, EPC integrator produced, vendor input received | `_CONTEXT.md` Scope; `DELIVERABLE_REGISTER.csv` row DEL-078-06 |
| Acceptance basis (upstream artifacts referenced) | EPC Scope of Work (DEL-078-01), Package Datasheet (DEL-078-02), Construction Work Package (DEL-078-03) | `_CONTEXT.md` Scope |
| Vendor inputs referenced | Vendor Engineered Equipment Package (DEL-078-04), Vendor Document Turnover Package (DEL-078-05) | `DELIVERABLE_REGISTER.csv` rows DEL-078-04/05 |
| Equipment population (per roster) | 3 inlet pig receiver units, tags `PR-1010-1`, `PR-1020-1`, `PR-1030-1` | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Package Line-Item Requirements row 61 |
| DBM-body design quantity | 1 x 610 mm OD (24 in.) pig receiver on a dedicated structural steel non-enclosed skid | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Inlet Pig Receiving narrative |
| Quantity reconciliation | CONFLICT — see Conflict Table in `Guidance.md` | both sources above |

## Conditions

| Item | Value | Source |
|---|---|---|
| Service | Sour natural gas, plant inlet pipeline gas | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Inlet Pipeline / Inlet Pig Receiving narrative |
| Inlet pipeline OD | 610 mm OD (24 in.) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Inlet Pig Receiving |
| Upstream isolation | Full-port skid-mounted isolation valves or ESDVs (full port for pigging) | same |
| Pig migration control | Barred tees shall prevent pigs from entering facility piping | same |
| Pre-opening purge | Low-pressure fuel gas purge downstream of manual isolation valve for sweet-gas purge before opening | same |
| Vent | Pig receiver vents to HP flare system | same |
| ESDV at inlet | Full-port piggable ESDV with position transmitters on the pig receiver inlet skid | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Inlet Separator/ESDV narrative |
| Inlet separator shut ESDV pressure shutdown basis | 1,360 psig | same |
| Delivery point ESDV pressure shutdown | TBC (per source) | same |
| HIPPS requirement | TBD — possibly required if inlet pipeline MAOP exceeds facility inlet design pressure | same |
| Design pressure (plant gate up to inlet separator inlet PCV downstream isolation) | MAWP equal to upstream inlet pipeline; downstream of PCV 1,360 psig (600# flanges at 200 °F) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Inlet Pipeline Pressure and Flow |
| Inlet Gathering MAOP (assumed) | 1,440 psig (TBC) | same |
| Maximum inlet operating pressure | 1,300 psig (90% of assumed upstream MAOP) | same |
| Facility inlet design flow | 300 MMSCFD summer; 308 MMSCFD winter | same |
| Facility inlet maximum flow | 300 MMSCFD summer; ~325 MMSCFD winter | same |
| Inlet condensate (winter slug, normal operating during pigging) | 572 Am3/d facility total | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Inlet Separator Design Parameters |
| Two-phase pigging hazards | Methanol injection may be required upstream of inlet separators and in MPFF feed for hydrate suppression | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Inlet Pipeline Pressure and Flow |

## Construction

| Item | Value | Source |
|---|---|---|
| Skid | Dedicated structural steel non-enclosed skid | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Inlet Pig Receiving |
| Coatings | Not stated for pig receiver in DBM body; TBD | source silent |
| Materials | Not stated explicitly in accessible DBM slice; TBD (vendor package basis) | source silent in accessible slice |
| Tie-in references | Plant inlet pipeline; downstream barred-tee transition into facility piping; HP flare for vent; LP fuel-gas connection for purge | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Inlet Pig Receiving |
| Future scope hooks | "Inlet pipeline final configuration, detailed tie-ins, and any second inlet pipeline pig receiver/isolation requirements are TBD" | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line ~846 |

## Anticipated Acceptance Evidence Artifacts (this deliverable produces)

- Vendor document review log (status per submittal, comment-disposition record)
- Package acceptance checklist (against SOW, Package Datasheet, CWP)
- Test/inspection evidence (FAT, pressure test, NDE, weld traceability, PMI as applicable) — TBD which apply
- Turnover evidence (mechanical completion certificate, ITR/QITP records, redline drawings, vendor data book index)

Source: `_CONTEXT.md` Anticipated Artifacts; `DELIVERABLE_REGISTER.csv` row DEL-078-06.

## Covers Scope Items / Supports Objectives

- Scope items: `SOW-0161`, `SOW-0162`, `SOW-0163`, `SOW-0164` [Source: `_CONTEXT.md`]
- Objectives (PACKAGE_HEURISTIC, ASSUMPTION best-effort mapping): `OBJ-001`, `OBJ-003`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` [Source: `_CONTEXT.md`; OBJECTIVE_DELIVERABLE_MAP.csv]

## References

- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (accessible) — Inlet Pig Receiving narrative; Package Line-Item Requirements row 61; Inlet Separator Design Parameters; Inlet Pipeline Pressure and Flow.
- `_Sources/26020-Package_Requirements.docx` package heading 31 (not locally accessible as text; location TBD).
- `_Sources/26020-Packages_Interfaces_4_export.xlsx` Packages row 78 (not locally accessible as text; location TBD).
- Gate 7 PROJECT_DECOMP snapshot: `DELIVERABLE_REGISTER.csv` row DEL-078-06; `PACKAGE_REGISTER.csv` PKG-078.
