# Datasheet — DEL-087-01 Scope of Work (PKG-087 Incinerator)

> Pass: P1_P2 (Pass 1 + Pass 2 cross-check). Source-grounded; unsupported values marked `TBD`.

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-087-01_scope-of-work` | `_CONTEXT.md` |
| Name | Scope of Work | `_CONTEXT.md` |
| ParentPackageID | `PKG-087` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row 64 |
| Package Name | Incinerator | `PACKAGE_REGISTER.csv` row 64 |
| Discipline | Mechanical | `PACKAGE_REGISTER.csv` row 64 |
| WBS | 02 | `PACKAGE_REGISTER.csv` row 64 |
| Source RFQ Tag | `26020-02-PT-25-003 - Incinerator` | `PACKAGE_REGISTER.csv` row 64 |
| ResponsibleParty (this deliverable) | EPC Integrator | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row 348 |
| Type | EPC Scope of Work | `_CONTEXT.md` |

## Attributes — Tagged Equipment in the Package

Source: DBM-Deepcut `4-25_Deepcut_DBM.md` (Equipment Identification table, row "Incinerator", and Tag Detail row 32). Authoritative count and tag list:

| Tag | Description | Source ref |
|---|---|---|
| `B-6920-1` | Incinerator (blower / burner assembly — DBM tag listing) | `DBM-Deepcut/4-25_Deepcut_DBM.md` Tag-Detail row 32; mapping of tag to function is `ASSUMPTION` (DBM lists tags without per-tag descriptors) |
| `FL-6920-1` | Incinerator (flare/incinerator stack element) | same; per-tag function `ASSUMPTION` |
| `P-6900-1` | Incinerator knockout drum transfer pump | `PACKAGE_REGISTER.csv` row 64 names "incinerator knockout drum transfer pump"; tag-to-function mapping `ASSUMPTION` |
| `V-6900-1` | Incinerator knockout drum | `PACKAGE_REGISTER.csv` row 64 names "incinerator knockout drum"; tag-to-function mapping `ASSUMPTION` |

Workbook (`PACKAGE_REGISTER.csv` row 64) names four supplied items, in this order:

1. Qty 1 incinerator knockout drum
2. Qty 1 incinerator knockout drum transfer pump
3. Qty 1 incinerator – low pressure flare stack
4. Qty 1 incinerator blower

The DBM-Deepcut row tag list also reports a count of 4 tags for the Incinerator entry, consistent with four supplied items.

Associated shop module: `691-1 Incinerator KO Drum Module` (DBM-Deepcut). Verifies the knockout drum is a shop-fabricated module.

## Conditions

| Attribute | Value | Source |
|---|---|---|
| Service / vapour source | Vapours from the spent caustic storage tank and DSO off-gas route to the incinerator | `DBM-Deepcut` line 1570 |
| Upstream knockout | Knock-out drum upstream of the incinerator separates free liquids before the stack | `DBM-Deepcut` line 1570 |
| Backflash protection on contributing tanks | Spent caustic and DSO storage tanks vent through flame arrestors to the incinerator header | `DBM-Comp_and_Liquids` line 402; `DBM-Deepcut` lines 1562, 1564 |
| Pilot / supplemental / purge fuel basis | `TBD` — `DBM-Deepcut` line 1572 records supplemental fuel gas rate, incinerator flow basis, and 03-25/04-25 operational responsibility as `TBD` |
| Dilution / enrichment gas | `TBC` — `DBM-Deepcut` line 1890 ("Incinerator dilution/enrichment gas — TBC") |
| Emissions basis (current non-regenerative caustic) | `TBD` — `DBM-Deepcut` lines 2244-2246, 2294-2295 |
| Spacing to nearest plant equipment | 25 m (82 ft) minimum (OGAOM Sec. 9.6.15) | `DBM-Deepcut` line 280 |
| Spacing between fired heater and incinerator | 25 m (82 ft) (OGAOM Sec. 9.6.15) | `DBM-Deepcut` line 296 |

## Construction (package-supplied scope items)

1. Incinerator knockout drum (`V-6900-1`) — `PACKAGE_REGISTER.csv` row 64; `DBM-Deepcut` Tag-Detail row 32.
2. Incinerator knockout drum transfer pump (`P-6900-1`) — same.
3. Incinerator low-pressure flare stack — `PACKAGE_REGISTER.csv` row 64. Tag mapping to `FL-6920-1`: `ASSUMPTION`.
4. Incinerator blower — `PACKAGE_REGISTER.csv` row 64. Tag mapping to `B-6920-1`: `ASSUMPTION`.

Materials, sizing, design pressures/temperatures, MOC, and code stamps: `TBD` (not stated in locally accessible source slices; the `26020-Package_Requirements.docx` package heading 40 listed in `_REFERENCES.md` is not locally accessible in markdown form).

## References

- `_CONTEXT.md` — deliverable identity, scope, anticipated artifacts.
- `_REFERENCES.md` — authoritative basis pointers.
- `_Decomposition/.../GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` row 348.
- `_Decomposition/.../GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv` row 64.
- `_Decomposition/.../GATE-07_Final_Published_2026-05-24/OBJECTIVE_SCOPE_MAP.csv` (rows mapping OBJ-002/004/005/006/007/008 to SOW-0111..SOW-0114 / PKG-087).
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — lines 182, 276-296, 1562-1572, 1568 (Incinerator Interface), 1890, 2244-2246, 2294-2295, 2538, 2587, 2803.
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` — lines 56, 400-402, 547-555.
- `_Sources/26020-Package_Requirements.docx` package heading 40 — `location TBD` (not locally accessible in this run; cited but not opened).
