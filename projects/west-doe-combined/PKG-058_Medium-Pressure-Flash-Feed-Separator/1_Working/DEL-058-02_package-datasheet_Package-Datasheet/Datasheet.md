# Datasheet — DEL-058-02 Package Datasheet (PKG-058 Medium Pressure Flash Feed Separator)

> Descriptive datasheet for the EPC Package Datasheet deliverable for PKG-058. Values cite the locally accessible 04-25 Deepcut Design Basis Memorandum (DBM) source slices. Where the source itself records `TBD/TBC`, this datasheet preserves those markers.

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-058-02_package-datasheet` | `_CONTEXT.md` |
| Deliverable Name | Package Datasheet | `_CONTEXT.md` |
| Parent Package | `PKG-058` Medium Pressure Flash Feed Separator | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Discipline | Mechanical | `_CONTEXT.md` |
| Deliverable Type | EPC Package Datasheet | `_CONTEXT.md` |
| Responsible Party | EPC Integrator | `_CONTEXT.md` |
| Equipment Tags (4-25 Deepcut) | V-7110-1, V-7310-1 (separators, x2); E-7120-1, E-7320-1 (HCL heater bundles, x2) | DBM-Deepcut `4-25_Deepcut_DBM.md` §"MPFF Operating and Capacity Basis"; equipment register rows 52-53; heat medium duty table |
| Modules | 710-1 Medium Pressure Flash Feed Module; 730-1 Medium Pressure Flash Feed Module (shop-assembled) | DBM-Deepcut `4-25_Deepcut_DBM.md` module table |
| Sparing Basis | 2 x 100% normal operation (no sparing for off-design line-pack maximum) | DBM-Deepcut §"MPFF and Stabilizer Train Relationship" |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Function | Medium-pressure flash separation of high-pressure hydrocarbon liquid from inlet separators; overhead vapour routed to SOC third-stage suction; liquid bottoms feed downstream stabilizer flash/feed | DBM-Deepcut §"MPFF Operating and Capacity Basis" |
| Vessel internals | Mistex demister; no internal coating specified | DBM-Deepcut §"MPFF Operating and Capacity Basis" |
| Liquid residence time | ≥10 minutes between weir height and NLL-interface | DBM-Deepcut §"MPFF Operating and Capacity Basis" |
| Blowdown | Automated blowdown valve required; routes to HP flare (ASSUMPTION: consistent with adjacent flash/feed routing in source) | DBM-Deepcut §"MPFF Operating and Capacity Basis"; §"Relief and Blowdown" |
| Purge / drive gas | LP fuel gas downstream of fuel-gas scrubber, regulated to maintain MPFF pressure above downstream stabilizer flash/feed separator; available for sour-gas sweep during maintenance | DBM-Deepcut §"MPFF Operating and Capacity Basis" |
| Hydrate suppression | Methanol injection upstream of MPFF inlet level/pressure control valve (safeguard) | DBM-Deepcut §"MPFF Operating and Capacity Basis" |
| Package enclosure | Self-framing building enclosing instrumentation and one end of vessel; configured similarly to inlet separator package | DBM-Deepcut §"MPFF Operating and Capacity Basis" |
| Train coupling | One MPFF assigned to one stabilizer; MPFF out of service if its stabilizer is out of service | DBM-Deepcut §"MPFF and Stabilizer Train Relationship" |

## Operating Conditions (per MPFF separator unless noted)

| Parameter | Low | Expected Normal | Expected High | Design | Source |
|---|---:|---:|---:|---:|---|
| Operating pressure, kPag | TBD | 1724 | TBD | 1724 | DBM-Deepcut §"MPFF Operating and Capacity Basis" |
| Operating temperature, deg C | — | 40 (ASSUMPTION pending detailed engineering) | — | 40 (ASSUMPTION) | DBM-Deepcut §"MPFF Operating and Capacity Basis" |
| Total two-phase inlet, summer, MMSCFD | 0 | 0 | Minimal | Minimal | DBM-Deepcut §"MPFF Operating and Capacity Basis" |
| Total two-phase inlet, winter, MMSCFD | 0 | 6.681 | 12.91 | 12.91 | DBM-Deepcut §"MPFF Operating and Capacity Basis" |
| Liquid inlet, summer, m3/h | 0 | 0 | Minimal | Minimal | DBM-Deepcut §"MPFF Operating and Capacity Basis" |
| Liquid inlet, winter, m3/h | 0 | <15.3 | 19.58 | 19.58 | DBM-Deepcut §"MPFF Operating and Capacity Basis" |
| Vapour inlet, winter, MMSCFD | 0 | <1.151 | 4.143 | 4.143 | DBM-Deepcut §"MPFF Operating and Capacity Basis" |
| Overhead routing | Pressure-regulated to SOC third-stage suction | — | — | — | DBM-Deepcut §"MPFF Operating and Capacity Basis"; SOC source capacity table (V-7110-1/V-7310-1 → SOC stage 3) |
| MPFF inlet temperature (post-HEX) | TBD/TBC | TBD/TBC | TBD/TBC | TBD/TBC | DBM-Deepcut §"MPFF Operating and Capacity Basis" |

## Construction

| Attribute | Value | Source |
|---|---|---|
| Vessel quantity | 2 (V-7110-1, V-7310-1) | DBM-Deepcut equipment register rows 52-53 |
| Heater bundle (if retained) | U-bundle / BKU-type, heat medium tube side; original sizing 140 deg F MPFF outlet, 87 deg F at 50 psig downstream LP flash feed; 10% excess surface area for line-pack scenario | DBM-Deepcut §"MPFF Operating and Capacity Basis" |
| Heater bundle disposition | TBD — retention, de-rate, or removal pending thermal re-simulation; tube-sheet seal-weld requirements TBC; vessel nozzle provisions preserved until disposition confirmed | DBM-Deepcut §"MPFF Operating and Capacity Basis" |
| Heater bundle heat-medium duty (each) | 762 kW (2.6 MM BTU/h); supply 118 deg C / 245 deg F; return 80 deg C / 175 deg F | DBM-Deepcut §"Heat Medium Users and Duties" (E-7120-1, E-7320-1) |
| Heater bundle heat-medium supply (original basis) | 350 deg F supply — TBC after thermal re-simulation | DBM-Deepcut §"MPFF Operating and Capacity Basis" |
| Materials of construction | TBD (not stated at MPFF level in accessible source) | TBD |
| Design pressure / temperature (vessel) | TBD (not specified in accessible source slices) | TBD |
| Relief / blowdown destination | HP flare (ASSUMPTION; consistent with adjacent equipment) | DBM-Deepcut §"Relief and Blowdown" |
| Modular packaging | Shop-assembled; self-framing building erected in field (consistent with PKG approach) | DBM-Deepcut module table; §"MPFF Operating and Capacity Basis" |

## Interfaces (carried here as evidence per `_CONTEXT.md` Notes)

| Interface | Counterparty | Source |
|---|---|---|
| Liquid feed inlet | Inlet separator liquid outlet header, pre-heated by inlet-separator liquid outlet heater | DBM-Deepcut §"MPFF Operating and Capacity Basis"; §"Inlet Separator Interfaces" |
| Overhead vapour outlet | SOC third-stage suction (V-7110-1 / V-7310-1 → SOC stage 3) | DBM-Deepcut SOC source capacity table |
| Liquid bottoms outlet | Downstream stabilizer flash/feed separator | DBM-Deepcut §"Stabilizer Design and Operating Basis" |
| Heat-medium service (if bundle retained) | Heat-medium loop (E-7120-1, E-7320-1) | DBM-Deepcut §"Heat Medium Users and Duties" |
| LP fuel gas | Downstream of fuel-gas scrubber (purge / drive gas) | DBM-Deepcut §"MPFF Operating and Capacity Basis" |
| Methanol injection | Methanol distribution system, upstream of MPFF inlet LCV | DBM-Deepcut §"MPFF Operating and Capacity Basis" |
| Relief / blowdown | HP flare (ASSUMPTION) | DBM-Deepcut §"Relief and Blowdown" |
| Balance-of-plant controls | Package instrumentation enclosure; BOP controls (TBD detail) | DBM-Deepcut §"MPFF Operating and Capacity Basis" |

## Open / Unresolved Items (carried from source TBD/TBC)

- MPFF low and expected-high operating pressure values: TBD (DBM-Deepcut §"MPFF and SOC TBDs").
- MPFF post-upstream-HEX inlet temperatures: TBD/TBC pending thermal reassessment.
- Internal heater bundle retention, sizing, and heat-medium conditions: TBD pending re-simulation.
- 03-25 condensate routing to MPFF versus direct stabilizer feed: unresolved.
- Vessel design pressure/temperature and materials of construction: TBD (not present in accessible source).
- Inlet separator quantity legacy "4 vessels" annotation: unresolved upstream conflict tied to MPFF source table.

## References

- DBM-Deepcut `4-25_Deepcut_DBM.md` — §"MPFF and Stabilizer Train Relationship"; §"MPFF Operating and Capacity Basis"; §"Heat Medium Users and Duties"; §"Relief and Blowdown"; §"MPFF and SOC TBDs"; equipment register rows 52-53; module table.
- `_CONTEXT.md` (deliverable identity, package association, anticipated artifacts).
- `_REFERENCES.md` (decomposition registers, source root).
- GATE-07 PROJECT_DECOMP snapshot `OBJECTIVE_DELIVERABLE_MAP.csv` (explicit objective mapping OBJ-001/004/005/006/007/008/009/010 for DEL-058-02).
- 26020-Package_Requirements.docx package heading 13 — referenced by decomposition; **location TBD** (no markdown extract locally accessible).
- 26020-Packages_Interfaces_4_export.xlsx Packages row 71 — referenced by decomposition; **location TBD** (no markdown extract locally accessible).
