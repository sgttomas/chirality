# Datasheet: DEL-060-02 — Package Datasheet (Tank Farm Pump Building 4-25)

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-060-02_package-datasheet` | `_CONTEXT.md` |
| Name | Package Datasheet | `_CONTEXT.md` |
| ParentPackageID | `PKG-060` | `_CONTEXT.md` |
| Package Name | Tank Farm Pump Building 4-25 | `_CONTEXT.md`; PACKAGE_REGISTER row 85 |
| Workbook Row | 85 | `_REFERENCES.md`; PACKAGE_REGISTER |
| Package RFQ Tag | `26020-01-PT-18-002 — Tank Pumps` | PACKAGE_REGISTER (Gate 7) |
| Discipline | Mechanical | `_CONTEXT.md`; PACKAGE_REGISTER |
| Type | EPC Package Datasheet | `_CONTEXT.md` |
| Responsible Party | EPC Integrator | `_CONTEXT.md` |
| Facility | West Doe Deepcut 04-25 (Tank Farm) | DBM-Deepcut §SEC-11 / §Product Pumps |
| LSD | 04-25-80-15 W6M | DBM §Site Basis (line 193) |

## Attributes (Scope of Supply)

Authoritative source: PACKAGE_REGISTER row 85 (Gate 7 snapshot); DBM-Deepcut §Product Pumps (lines 1667-1679); DBM Package Roster (line 2555) and Line-Item table (lines 2618-2622).

| Component | Quantity / Configuration | Service | Source |
|---|---|---|---|
| Condensate Transfer Pumps | 2 x 150% (P-9210-1, P-9220-1); multi-stage horizontal | Transfer stabilized condensate from condensate storage tanks to 03-25 Liquids Hub | DBM lines 1673, 2618; PACKAGE_REGISTER row 85 |
| Water Transfer Pumps | 2 (P-9290-1, P-9293-1); radial centrifugal | Transfer produced water from produced-water tanks to 03-25 Compressor Station | DBM line 2619; PACKAGE_REGISTER row 85 |
| Sour Water Treatment Pumps | 2 (P-9231-1, P-9232-1); radial centrifugal | Sour-water treatment service | DBM line 2620 |
| Process Water Transfer Pumps | 2 (P-5317-1, P-5318-1); radial centrifugal | Process water transfer | DBM line 2621 |
| Fresh Caustic Transfer Pumps | 2 (P-6760-1, P-6765-1); radial centrifugal | Fresh caustic transfer | DBM line 2622 |
| Condensate Recycle Pump | 1 x 100% (TBD tag) | Recycles condensate from produced-water tank skim system to stabilizer flash-feed separator | DBM line 1672; PACKAGE_REGISTER row 85 |
| Total package equipment items | 10 | — | DBM line 2555 |

Notes:
- The PACKAGE_REGISTER row 85 narrative also references "(1x) Condensate recycle pump" and pump motors as part of the package vendor scope. The Condensate Recycle Pump tag is `TBD` against the line-item table.
- The "Product recycle pump" listed at DBM line 1671 (20 m3/h at 80 m TDH, TBC) appears to be the same unit as the Condensate Recycle Pump in the package narrative. **CONFLICT:** see Conflict Table in Guidance.md.

## Design Conditions

| Parameter | Value | Source |
|---|---|---|
| Condensate transfer pump differential | 350 kPad (50 psid) to liquids hub | DBM line 1673; PACKAGE_REGISTER row 85 |
| Condensate transfer sparing | 2 x 150% of facility design flow of combined condensate product; both pumps capable of simultaneous operation | DBM line 1675 |
| Condensate transfer NPSHR (design flow) | ≤ 0.75 m | DBM line 1677 |
| Motor sizing basis (condensate transfer) | Inlet stabilizer composition density at -40 deg C startup, including potential initial JT-mode startup | DBM line 1679 |
| Minimum-flow control valve | Required for continuous pumping to downstream liquids hub | DBM line 1679 |
| Recycle / skim pump capacity (TBC) | 20 m3/h at 80 m TDH | DBM lines 1671-1672 |
| Site ambient envelope | Per DBM SEC-02 site basis | DBM §Site Basis (location TBD specific extreme values) |
| Sour service requirements | TBD — sour-service isolation requirements unresolved at DBM-level | DBM line 2639 |

## Construction / Module Basis

| Parameter | Value | Source |
|---|---|---|
| Module designator | Tank farm pump module (Mod 920-1) | DBM line 2817 |
| Construction status | Shop module | DBM line 2817 |
| Building services | Building HVAC / Services; Area / Exterior Lighting; EHT; Fire & Gas / Safety Systems | PACKAGE_REGISTER row 85 |
| Electrical area | Served from 4.16 kV / 600 V General Area / Tank Farm / Process Electrical Building | DBM line 2925 |
| Cable tray | Field-run cable tray permitted at tank farm and interconnecting trays | DBM line 2999 |

## Interface Types (Required Per Package Register Row 85)

- Process Piping
- Utility Piping
- Relief / Flare / Vent
- Drain / Containment
- Electrical Power
- EHT (Electric Heat Trace)
- Grounding / Bonding
- Area / Exterior Lighting
- Cathodic Protection
- I&C / Control Cabling
- Building HVAC / Services
- Fire & Gas / Safety Systems
- Maintenance Access
- Structural / Foundations / Supports

Source: PACKAGE_REGISTER row 85 ("Applicable interface types").

## References

- `_REFERENCES.md` (deliverable-local)
- DBM-Deepcut: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (§Product Pumps lines 1667-1679; Package Roster line 2555; Package Line-Item table lines 2618-2622; SEC-11 Civil/Modules; §Electrical SEC areas)
- PACKAGE_REGISTER (Gate 7 snapshot) row 85
- DELIVERABLE_REGISTER (Gate 7 snapshot) row for `DEL-060-02_package-datasheet`
- Workbook Packages row 85 (location TBD — not locally accessible as parsed text)
- 26020-Package_Requirements.docx package heading 15 (location TBD — .docx not parsed locally)
- 26020-01-PT-RFQ-18-002-Tank_Farm_Pump.docx (Bid Docs / Budgetary; location TBD — not parsed locally)
