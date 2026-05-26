# Datasheet — DEL-085-03 Construction Work Package (Flare Stack, High Pressure)

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-085-03_construction-work-package` |
| Name | Construction Work Package |
| ParentPackageID | `PKG-085` |
| PackageName | Flare Stack (High Pressure) |
| PackageTag | `26020-02-PT-25-001 - Flare Stack (High Pressure)` (SourcePath: `_Decomposition/.../PACKAGE_REGISTER.csv`, SectionRef: PKG-085 row) |
| Discipline | Mechanical |
| Type | EPC Construction Work Package |
| ResponsibleParty | EPC Integrator |
| WBS | 02 (SourcePath: PACKAGE_REGISTER.csv, SectionRef: PKG-085 row) |

## Attributes (Physical Package Being Installed)

| Attribute | Value | Source |
|---|---|---|
| Service | HP/Cryo and LP dual flare stack, shared 03-25/04-25 | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 56, 497, 548 |
| Stack configuration | Self-supported dual flare stack | `_Sources/.../PACKAGE_REGISTER.csv` PKG-085 (Bid Docs/Budgetary/24292-02-PT-ENR-25-201_Self Supported Dual Flare Stack_R1.pdf) |
| HP/Cryo stack outside diameter | 660 mm OD | `3-25_Comp_and_Liquids_DBM.md` line 499 |
| HP/Cryo stack height | 60,957 mm | `3-25_Comp_and_Liquids_DBM.md` line 499 |
| HP/Cryo tip type | Sonic | `3-25_Comp_and_Liquids_DBM.md` line 499 |
| LP stack outside diameter | TBD | `3-25_Comp_and_Liquids_DBM.md` line 499 (explicit TBD in source) |
| HP relief header connecting size | DN 500 / 20 in | `3-25_Comp_and_Liquids_DBM.md` line 499 |
| LP relief header connecting size | DN 500 / 20 in | `3-25_Comp_and_Liquids_DBM.md` line 499 |
| Upstream HP KO drums | V-4100-2 (compressor area), V-4150-2 (tank farm) | `3-25_Comp_and_Liquids_DBM.md` line 497 |
| Upstream LP KO drum | V-3900-2 | `3-25_Comp_and_Liquids_DBM.md` line 499 |
| Service split (HP vs LP, 03-25 vs 04-25 ownership) | TBD — `CONFLICT`: source records this as an open shared-interface item | `3-25_Comp_and_Liquids_DBM.md` lines 56, 548 |

## Conditions (Installation/Construction Conditions)

| Condition | Value | Source |
|---|---|---|
| Site / facility | 03-25 Comp and Liquids facility (shared with 04-25 gas plant) | `3-25_Comp_and_Liquids_DBM.md` line 56 |
| Geotechnical basis | Final geotechnical report TBD; flare/stack foundations require equipment-specific design | `3-25_Comp_and_Liquids_DBM.md` line 700 |
| Environmental loads (snow/wind/seismic) | TBD pending final civil/structural basis | `3-25_Comp_and_Liquids_DBM.md` line 700 (ASSUMPTION: applies to flare stack as listed tall element) |
| Construction season constraints | TBD |
| Hot-work / energized-tie-in constraints | TBD (HAZOP-driven; see Procedure §Verification) |

## Construction (Installation, Tie-in, and Turnover Scope)

| Item | Value | Source |
|---|---|---|
| Foundation and anchorage | Equipment-specific foundation and anchorage check required for flare/stack element | `3-25_Comp_and_Liquids_DBM.md` line 700 |
| Mechanical interfaces (EPC integration scope) | Utility Piping; Relief/Flare/Vent; Drain/Containment; Electrical Power; Grounding/Bonding; I&C/Control Cabling; Fire & Gas/Safety Systems; Structural/Foundations/Supports | `PACKAGE_REGISTER.csv` PKG-085 "Applicable interface types" |
| Tie-in points (HP) | HP relief headers from V-4100-2 and V-4150-2 manifold to HP flare | `3-25_Comp_and_Liquids_DBM.md` line 497 |
| Tie-in points (LP) | LP relief header from V-3900-2 to LP flare | `3-25_Comp_and_Liquids_DBM.md` line 499 |
| KO drum pump tie-ins | P-4100-2, P-4150-2 (HP); P-3900-2 (LP) — truck-out / slop transfer | `3-25_Comp_and_Liquids_DBM.md` lines 497, 499, 583-584 |
| Detection/Fire & Gas installation | LEL, H2S, methyl mercaptan, fire detection at flare/vent interfaces — quantity, placement, set points TBD | `3-25_Comp_and_Liquids_DBM.md` line 838 |
| Turnover artifacts | Construction work package; installation and tie-in workface plan; construction interface and turnover checklist | `DELIVERABLE_REGISTER.csv` DEL-085-03 "Anticipated Artifacts" |
| Vendor-supplied equipment package boundary | Vendor scope (DEL-085-04) ends at package skid limits; EPC owns facility integration and interfaces | `PACKAGE_REGISTER.csv` PKG-085 "Discipline Responsibility Note"; `DELIVERABLE_REGISTER.csv` DEL-085-04 |

## SOW and Objective Linkage

- Covers Scope Items: `SOW-0087`, `SOW-0088`, `SOW-0089`, `SOW-0090` (Source: `_CONTEXT.md`)
- Supports Objectives: `OBJ-002`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` (ASSUMPTION: package-heuristic association per skill default; `_CONTEXT.md`)

## References

- `_REFERENCES.md` (this deliverable)
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (HP/LP flare basis, lines 56, 497, 499, 548, 583-584, 700, 838)
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` (DEL-085-03 row)
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv` (PKG-085 row)
- Workbook Packages row 58; 26020-Package_Requirements.docx package heading 38 (location TBD — source slice not locally accessible)
- Bid Docs/Budgetary/24292-02-PT-ENR-25-201_Self Supported Dual Flare Stack_R1.pdf (budgetary go-by only; location TBD — slice not locally accessible)
