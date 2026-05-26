# Datasheet: DEL-046-01 — Scope of Work (PKG-046 Acid Gas Compressors)

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-046-01_scope-of-work` | `_CONTEXT.md` |
| DeliverableName | Scope of Work | `_CONTEXT.md` |
| ParentPackageID | `PKG-046` | `_CONTEXT.md` |
| WorkbookRow | 48 | `PACKAGE_REGISTER.csv` |
| WBS | 01 | `PACKAGE_REGISTER.csv` |
| PackageNumber | `26020-01-12-001` | `PACKAGE_REGISTER.csv` |
| PackageName | Acid Gas Compressors | `_CONTEXT.md` |
| EquipmentTag | `26020-01-PT-12-001 - Acid Gas Compressor` | `PACKAGE_REGISTER.csv` (Equipment Tag column) |
| Discipline | Mechanical | `_CONTEXT.md` |
| DeliverableType | EPC Scope of Work | `_CONTEXT.md` |
| ResponsibleParty | EPC Integrator | `_CONTEXT.md` |
| Vendor (package supplier) | Package Vendor (engineering, design, vendor docs, equipment) | `PACKAGE_REGISTER.csv` (Responsibility column) |
| Facility | West Doe 04-25 Deepcut Gas Plant Expansion | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §line 5 |

## Tagged Equipment and Package Identity

| Item | Value | Source |
|---|---|---|
| Package tag | `26020-01-PT-12-001` (Acid Gas Compressor) | `PACKAGE_REGISTER.csv` Equipment Tag |
| Package count | Two (2x) identical acid gas compressor packages, each 100% capacity; one spare compressor included | `4-25_Deepcut_DBM.md` §Compression Configuration (line 878); §Acid Gas Compressor Design Conditions (line 994) |
| Alternative configuration | Three (3x) 50% arrangement remains TBD; not confirmed basis | `4-25_Deepcut_DBM.md` line 878, 885, 994 |
| Compressor type | Separable reciprocating, induction-motor-driven, electric-drive | `4-25_Deepcut_DBM.md` §Compression Configuration; PACKAGE_REGISTER scope text |
| Compressor model reference | Ariel KBT/6, five-stage (conflicting KBK/6 reference TBD) | `4-25_Deepcut_DBM.md` line 995 |
| Driver | 969 kW (1,300 hp) induction motor, ~10% excess power; 8-pole, 900 rpm on VFD; min 3:1 speed turndown | `4-25_Deepcut_DBM.md` lines 1003-1004 |

## Process Function (Package Identity)

Acid gases (H2S and CO2) recovered from the amine treating unit are compressed and routed to an injection/disposal well for sequestration. The package compresses the amine acid gas stream and delivers it to the acid gas injection pipeline interface for disposal at the existing acid gas disposal well/reservoir shared with the 02-25 facility.

Source: `PACKAGE_REGISTER.csv` Scope and Notes columns; `4-25_Deepcut_DBM.md` §Acid Gas Injection Compression Basis (lines 868, 885, 971-973, 1037-1059).

## Design Capacity Snapshot (informational; full datasheet values carried in DEL-046-02)

| Parameter | Value | Source |
|---|---|---|
| Design total flow | 4.209 MMSCFD | `4-25_Deepcut_DBM.md` line 996 |
| Design unit flow | 4.5 MMSCFD (preliminary) | `4-25_Deepcut_DBM.md` line 997 |
| Start-up total flow | 0.603 MMSCFD | `4-25_Deepcut_DBM.md` line 998 |
| 1st stage suction pressure | 3.8 psig low; 7 psig normal | `4-25_Deepcut_DBM.md` line 1001 |
| 5th stage discharge pressure | 1,200 psig normal; 1,500 psig design reference unresolved | `4-25_Deepcut_DBM.md` line 1002 |

## Whole-Facility Integration (summary)

The package interfaces with the 04-25 amine regeneration system (suction-side acid gas), facility utilities and electrical, and the acid gas injection pipeline + disposal well (discharge-side). The disposal well is shared with the existing 02-25 facility; incremental volume from 04-25 may require 02-25 modifications (scope TBD).

Source: `4-25_Deepcut_DBM.md` lines 84, 93, 1037-1061; `PACKAGE_REGISTER.csv` Applicable Interfaces.

## Applicable Interface Types (carried from PACKAGE_REGISTER)

Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports.

Source: `PACKAGE_REGISTER.csv` Applicable Interfaces column.

## Responsibility Assignment Record (RAR)

| Scope area | Responsible | Source |
|---|---|---|
| Package engineering, package design, vendor documentation, physical equipment package | Package Vendor | `PACKAGE_REGISTER.csv` Responsibility |
| Integration into the functional process facility (interfaces, tie-ins, constructability, procurement/construction coordination, facility-level integration) | EPC Integrator | `PACKAGE_REGISTER.csv` Responsibility |
| Acid gas disposal pipeline and well design | Excluded from this package; existing shared interface (Tourmaline / third party for well data) | `4-25_Deepcut_DBM.md` lines 84, 1049, 1053 |
| Disposal well pressure characteristics (MAWP, min, max) | Provided by Tourmaline | `4-25_Deepcut_DBM.md` lines 1051-1055 |

## Covered Scope Items (from PROJECT_DECOMP)

- `SOW-0047`, `SOW-0048`, `SOW-0049`, `SOW-0050` — Source: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row DEL-046-01.

## Supported Objectives (from PROJECT_DECOMP, PACKAGE_HEURISTIC association)

- `OBJ-001`, `OBJ-003`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` — ASSUMPTION (best-effort, package-grouped). Source: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv`.

## References

- `_CONTEXT.md`
- `_REFERENCES.md`
- PROJECT_DECOMP GATE-07 snapshot: `DELIVERABLE_REGISTER.csv`, `PACKAGE_REGISTER.csv`
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (Compression and Acid Gas Handling sections, lines 867-1061)
- `_Sources/26020-Package_Requirements.docx` package heading 1 — location TBD (binary not locally readable in this run)
- `_Sources/26020-Packages_Interfaces_4_export.xlsx` Workbook Packages row 48 — location TBD (binary not locally readable in this run)
