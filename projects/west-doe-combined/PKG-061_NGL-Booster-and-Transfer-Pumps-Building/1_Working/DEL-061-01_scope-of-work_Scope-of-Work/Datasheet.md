# Datasheet — DEL-061-01_scope-of-work (Scope of Work, PKG-061 NGL Booster and Transfer Pumps Building)

## Identification

| Field | Value |
|---|---|
| DeliverableID | DEL-061-01_scope-of-work |
| Name | Scope of Work |
| ParentPackageID | PKG-061 |
| PackageName | NGL Booster and Transfer Pumps Building |
| ParentWorkbookID | 61 |
| Discipline | Mechanical |
| Type | EPC Scope of Work |
| ResponsibleParty | EPC Integrator |
| Covers Scope Items | SOW-0149; SOW-0150; SOW-0151; SOW-0152 |
| Supports Objectives | OBJ-001; OBJ-003; OBJ-004; OBJ-005; OBJ-006; OBJ-007; OBJ-008; OBJ-009; OBJ-010 |
| Decomposition Source | Workbook Packages row 75; 26020-Package_Requirements.docx package heading 17 |
| Decomposition Snapshot | GATE-07_Final_Published_2026-05-24 |

## Attributes — Package Identity

| Attribute | Value | Source |
|---|---|---|
| Package function | Transfer NGL/LPG product from storage to LACT where booster pressure may be required | SOW-0150 (heading 17, Basic scope) |
| Plant area | 4-25 (Deepcut) | DBM-Deepcut equipment table (line 2548, 2609) |
| Tagged units in building | 2 | DBM-Deepcut equipment table (line 2609) |
| Equipment type | Pumps, API 610, multi-stage can | DBM-Deepcut equipment table (line 2609) |

## Attributes — Tagged Equipment

| Tag | Service | Configuration | Source |
|---|---|---|---|
| P-9570-1 | LPG/NGL booster pump | Vertical multistage can-type, API 610 seal plan 13/52 | SOW-0151 (heading 17, Major included equipment) |
| P-9580-1 | LPG/NGL booster pump | Vertical multistage can-type, API 610 seal plan 13/52 | SOW-0151 (heading 17, Major included equipment) |

## Conditions — Process Duty

| Parameter | Value | Source |
|---|---|---|
| Service | LPG/NGL product transfer from storage to LACT | SOW-0150 |
| Arrangement | Two booster pumps in parallel | SOW-0150 |
| Per-pump flow (sizing) | 145 m3/h at 150% capacity | SOW-0152 |
| Per-pump TDH | TBD | SOW-0152 |
| Booster pump design differential | 25 psid / 172 kPad | SOW-0152 |
| Motor electrical | 575 V, 3-phase, 60 Hz | SOW-0151 |
| Driver type | Electric motor (voltage per SOW-0151) | SOW-0151 |
| Upstream connection | NGL storage bullets (16 x 120,000 USG at 4-25; production basis 15,400 bbl/d, 2.5 days storage) | DBM-Deepcut line 448 |
| Downstream connection | NRM NEBC Connector via LACT (NGL C3+ product) | DBM-Deepcut lines 57, 446 |
| LACT inclusion / responsibility | TBD (current DBM contains both inclusion and exclusion language) | DBM-Deepcut lines 62, 82 |

## Conditions — Building / Package Boundary

| Parameter | Value | Source |
|---|---|---|
| Building / enclosure | HVAC/enclosure within vendor package | SOW-0151 |
| Skid | Structural skid (vendor-supplied) | SOW-0151 |
| Foundations | By others (excluded from vendor package) | SOW-0152 |
| Electrical supply to MCC | By others (excluded from vendor package) | SOW-0152 |
| DCS integration | By others (excluded from vendor package) | SOW-0152 |
| CRN/TSBC compliance | As applicable | SOW-0151 |

## Construction — Package Scope Items Included

- Two LPG/NGL booster pumps P-9570-1 and P-9580-1 (vertical multistage can-type) — SOW-0151
- API 610 seal plan 13/52 — SOW-0151
- Pump drivers: 575 V / 3-phase / 60 Hz electric motors — SOW-0151
- Structural skid — SOW-0151
- Package piping — SOW-0151
- Package instrumentation — SOW-0151
- Package electrical — SOW-0151
- HVAC / enclosure — SOW-0151
- CRN / TSBC documentation as applicable — SOW-0151
- Commissioning support — SOW-0151

## Construction — Excluded From Vendor Package (by EPC Integrator or others)

- DCS integration — SOW-0152
- Foundations — SOW-0152
- Electrical supply to MCC — SOW-0152

## References

- 26020-Package_Requirements.docx package heading 17 (NGL Booster and Transfer Pumps Building; Basic scope, Major included equipment, Scope notes and open items)
- Workbook Packages row 75 (PKG-061 identity)
- GATE-07 PROJECT_DECOMP snapshot: SCOPE_LEDGER.csv rows SOW-0149..SOW-0152; DELIVERABLE_REGISTER.csv DEL-061-01
- DBM-Deepcut/4-25_Deepcut_DBM.md (NGL product disposition lines 57, 446–448; equipment table lines 2548, 2609; LACT scope notes lines 62, 82)

## TBD / Open Items

- Per-pump TDH (rated) — TBD (SOW-0152)
- LACT unit inclusion, ownership, and design responsibility — TBD (DBM-Deepcut line 62)
- NPSHA at suction flange under all storage cases — TBD (no source value)
- Suction/discharge design pressures and design temperature — TBD (no source value in heading 17 extract)
- Process fluid composition at pump suction (treated NGL C3+) — TBD as part of pump selection (composition basis available in DBM-Deepcut SEC-07 but not specifically allocated to P-9570/P-9580 in heading 17)
