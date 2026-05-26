# Datasheet — DEL-077-02 Package Datasheet (PKG-077 Methanol Injection)

> Descriptive document. Source-grounded; missing values are marked `TBD`; inferences are labeled `ASSUMPTION`.

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-077-02_package-datasheet` | `_CONTEXT.md` |
| Name | Package Datasheet | `_CONTEXT.md` |
| ParentPackageID | `PKG-077` | `_CONTEXT.md` |
| ParentWorkbookID | 77 | `_CONTEXT.md` |
| PackageName | Methanol Injection | `_CONTEXT.md`; PACKAGE_REGISTER.csv (row PKG-077) |
| Discipline | Mechanical | `_CONTEXT.md`; PACKAGE_REGISTER.csv |
| WBS | 01 | PACKAGE_REGISTER.csv (row PKG-077) |
| Type | EPC Package Datasheet | `_CONTEXT.md` |
| ResponsibleParty | EPC Integrator | `_CONTEXT.md` |
| Workbook Row | Workbook Packages row 72 | `_CONTEXT.md`; PACKAGE_REGISTER.csv |
| Vendor Document Code | 26020-01-29-002 | PACKAGE_REGISTER.csv (row PKG-077) |
| Authoritative Decomp Snapshot | `GATE-07_Final_Published_2026-05-24` | `_REFERENCES.md` |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package function | Temporary/transient hydrate suppression via methanol injection at designated points across the 4-25 Deepcut facility. | DBM-Deepcut `4-25_Deepcut_DBM.md` L428, L1328 |
| Injection mode | System designed to inject into one point at a time. | DBM-Deepcut L1328 |
| Storage | Atmospheric double-walled methanol tank adjacent to expander building. | DBM-Deepcut L1329 |
| Pump | Triplex reciprocating injection pump. | DBM-Deepcut L1329, L2379 |
| Tank design specific gravity | 1.00 (pure methanol; **TBC** in source) | DBM-Deepcut L1329, L1351, L1392 |
| Service medium | Pure methanol. | DBM-Deepcut L1329 |
| Continuous hydrate suppression in raw inlet gas piping | Not provided; methanol injection points are for temporary transient management only. | DBM-Deepcut L428 |

## Conditions (Operating / Design)

| Parameter | Value | Source |
|---|---|---|
| Winter hydrate temperature (reference) | -2.8 degC | DBM-Deepcut L920 |
| Hydrate margin (cryogenic area design intent) | Maintain normal inlet ~6 degC above expected hydrate temperature; no methanol injection provisions in that area. | DBM-Deepcut L1153 |
| Injection-point design capacities | TBC (TBD in source) | DBM-Deepcut L1328, L1351, L1392 |
| Injection-rate values | TBD | DBM-Deepcut L1351 |
| BAHX design temperature limit (downstream of injection) | Max design temperature 150 degF (66 degC) | DBM-Deepcut L1324 |
| Acid-gas-compressor methanol-injection provisions | TBD | DBM-Deepcut L1371, L1351 |

## Construction (Equipment List and Tag Numbers)

| Tag | Description | Qty | Source |
|---|---|---|---|
| TK-6395-1 | METHANOL STORAGE TANK | 1 | DBM-Deepcut L2605 (Equipment row 54) |
| P-6396-1 | METHANOL PUMP | 1 | DBM-Deepcut L2606 (Equipment row 55) |

Sparing per source: Methanol Pump — 1 / 100% installed / 100% operating. (DBM-Deepcut L2379)

## Injection Points (Interface Inventory)

The methanol-injection system feeds the following interface points within the larger facility. Capacities and required points are **TBC** in source (DBM-Deepcut L1328, L1351, L1392).

| Injection Point | Service Location | Source |
|---|---|---|
| BAHX pass-inlet headers (each pass) | Upstream of tee strainers on each BAHX pass | DBM-Deepcut L1324, L1328 |
| J-T valve inlet | UltraTEF cryogenic J-T path | DBM-Deepcut L1328, L1363 |
| Inlet separators — upstream of PCV | Inlet separation area | DBM-Deepcut L1328 |
| Inlet separators — upstream of HCL and water dump valves | Inlet separation area | DBM-Deepcut L1328 |
| Acid gas compressor package | Acid-gas compression train | DBM-Deepcut L1328, L1371 (provisions TBD) |
| MPFF feed system (transient/line-pack start-up) | Upstream of MPFF inlet LCV/PCV | DBM-Deepcut L630, L674 |

## Interfaces (Package-Level)

PACKAGE_REGISTER lists the applicable interface types for PKG-077 (source: Workbook Packages row 72):

- Process Piping
- Utility Piping
- Relief / Flare / Vent
- Drain / Containment
- Electrical Power
- EHT (Electric Heat Trace)
- Grounding / Bonding
- Area / Exterior Lighting
- I&C / Control Cabling
- Building HVAC / Services
- Fire & Gas / Safety Systems
- Maintenance Access
- Structural / Foundations / Supports

Source: `PACKAGE_REGISTER.csv` row PKG-077.

## References

- `_REFERENCES.md`
- `_CONTEXT.md`
- PROJECT_DECOMP snapshot `GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` (row `DEL-077-02_package-datasheet`)
- PROJECT_DECOMP snapshot `GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv` (row PKG-077)
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — relevant slices: L428, L606-L674, L834-L838, L920, L1107, L1135, L1153, L1278-L1329, L1351, L1363-L1392, L2379, L2545, L2605-L2606
- `_Sources/26020-Packages_Interfaces_4_export.xlsx` — Workbook Packages row 72 (binary; **location TBD** for direct citation)
- `_Sources/26020-Package_Requirements.docx` — package-level requirements (binary; **location TBD**)
