# Datasheet — DEL-056-01 Scope of Work (PKG-056 Inlet Separators 4-25)

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-056-01_scope-of-work` | `_CONTEXT.md` |
| Name | Scope of Work | `_CONTEXT.md` |
| ParentPackageID | `PKG-056` | `_CONTEXT.md` |
| ParentWorkbookID | 56 | `_CONTEXT.md` |
| Package Name | Inlet Separators 4-25 | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row 68 |
| Facility | West Doe Deepcut expansion (04-25) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §Facility identifiers |
| Discipline | Mechanical | `_CONTEXT.md` |
| Deliverable Type | EPC Scope of Work | `_CONTEXT.md` |
| Responsible Party | EPC Integrator | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row 372 |
| Source Basis | Workbook Packages row 68; `26020-Package_Requirements.docx` package heading 11 | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row 372 |
| Word Source Basis (RFQ / DBM) | `Bid Docs/Budgetary/26020-01-PT-RFQ-17-004_Inlet Separators 2_R1.docx`; `DBM-Deepcut/4-25_Deepcut_DBM.md` | `PACKAGE_REGISTER.csv` row 68 |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package function | Receive raw inlet gas and separate into three phases: sour natural gas (vapour), sour raw condensate (light liquid), sour water (heavy liquid) | `PACKAGE_REGISTER.csv` row 68; `4-25_Deepcut_DBM.md` §Inlet separator system |
| Package equipment basis | Two (2) horizontal three-phase HP inlet separators (each 9 ft ID x 40 ft S/S) with plot space reserved for a third (CONFLICT: legacy project references describe four inlet separator packages) | `4-25_Deepcut_DBM.md` §Inlet separator system |
| Equipment tag identity (current authority) | `V-1600-1` (Inlet Separators 2 — Unit 1); `V-1700-1` (Inlet Separators 2 — Unit 2) | `4-25_Deepcut_DBM.md` row 2540, 2596–2597 |
| Vendor authority on package | Package engineering, package design, vendor documentation, physical equipment package | `PACKAGE_REGISTER.csv` row 68 |
| EPC Integrator authority | Integration into the functional process facility — interfaces, tie-ins, constructability, procurement/construction coordination, facility-level integration | `PACKAGE_REGISTER.csv` row 68 |
| Per-separator slug capacity | UNRESOLVED between 31.8 m3 and 33.9 m3 | `4-25_Deepcut_DBM.md` §Inlet separator system |
| Upstream pipeline holdup volume | 67 m3 (estimated) | `4-25_Deepcut_DBM.md` §Inlet separator system |
| Inlet shut-ESDV pressure shutdown basis | 1360 psig (delivery-point ESDV pressure shutdown TBC) | `4-25_Deepcut_DBM.md` line ~809 |

## Conditions (Service / Operating Context)

| Item | Value | Source |
|---|---|---|
| Service | Sour gas / sour raw condensate / sour water three-phase separation upstream of MPFF and stabilizer | `4-25_Deepcut_DBM.md` §Front-end process basis |
| Facility design throughput basis | 8,490 e3m3/d ≈ 300 MMSCFD nominal sour gas | `4-25_Deepcut_DBM.md` §Facility identifiers |
| Inlet separator gas outlet meter (design point) | 300 MMSCFD vapour | `4-25_Deepcut_DBM.md` line ~372 |
| Drive-gas source | Sales gas immediately upstream of sales gas splitter (alternate: inlet compressor discharge); separately metered per package | `4-25_Deepcut_DBM.md` line ~811 |
| Upstream HIPPS requirement | Possible if inlet pipeline MAOP exceeds facility inlet design pressure — TBC at detailed engineering | `4-25_Deepcut_DBM.md` line ~809 |

## Construction (Integration / Build Context)

| Item | Value | Source |
|---|---|---|
| Construction model | Package Vendor delivers engineered equipment package; EPC Integrator installs and integrates into the facility | `PACKAGE_REGISTER.csv` row 68 |
| Applicable interface types | Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports | `PACKAGE_REGISTER.csv` row 68 |
| Unit-level isolation basis | Multiple parallel packages isolated on a unit basis so a unit can be removed from service while others continue to operate | `4-25_Deepcut_DBM.md` line ~2408 |
| Methanol injection touchpoints | Upstream of PCV; upstream of HCL and water dump valves (per package) | `4-25_Deepcut_DBM.md` line ~1328 |
| Downstream interfaces | MPFF (via heated hydrocarbon liquid outlet lines); gas processing train (overhead gas) | `4-25_Deepcut_DBM.md` line ~834 |

## Anticipated Artifacts (this deliverable)

- Package scope of work
- Tagged equipment and package identity list
- Package function and integration narrative
- Responsibility assignment record

Source: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row 372.

## References

- `_CONTEXT.md`
- `_REFERENCES.md`
- `DELIVERABLE_REGISTER.csv` (row 372) — Gate-7 snapshot
- `PACKAGE_REGISTER.csv` (row 68) — Gate-7 snapshot
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`
- `_Sources/26020-Package_Requirements.docx` (binary; location TBD — package heading 11)
- `Bid Docs/Budgetary/26020-01-PT-RFQ-17-004_Inlet Separators 2_R1.docx` (location TBD — not opened in this run)

## Open Items (TBD)

- TBD: Final installed quantity of inlet separators (current authority: two installed + future provision; legacy references: four). See Conflict Table in `Guidance.md`.
- TBD: Per-separator slug capacity (between 31.8 m3 and 33.9 m3).
- TBD: Inlet separator peak produced water, water retention time, condensate retention time.
- TBD: Inlet separator liquid outlet heater outlet temperature target, duty, heating medium.
- TBD: HIPPS requirement and configuration.
- TBD: Delivery-point ESDV pressure-shutdown setpoint.
