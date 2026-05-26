# Datasheet — DEL-082-02 Package Datasheet (Flare KO Drum, Low Pressure, 3-25)

## Identification

| Field | Value |
|---|---|
| DeliverableID | DEL-082-02_package-datasheet |
| DeliverableName | Package Datasheet |
| ParentPackageID | PKG-082 |
| PackageName | Flare KO Drum (Low Pressure) 3-25 |
| Discipline | Mechanical |
| Type | EPC Package Datasheet |
| ResponsibleParty | EPC Integrator |
| PrimaryEquipmentTag | V-3900-2 (LP flare KO drum) |
| AssociatedPumpTag | P-3900-2 (LP KO drum transfer pump, 1 x 100 percent) |
| Facility | 03-25 (Compression and Liquids) |

Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC headings "Flare and Blowdown" (lines 495-501) and the equipment count summary table (line 584).

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Service | LP flare relief knock-out — receives TEG regeneration, VRU, and compressor seal-pot services | DBM SEC "Flare and Blowdown" |
| Equipment count | 1 x 100 percent KO drum with 1 x 100 percent transfer pump | DBM equipment summary (line 583-584) |
| Liquid disposition | Transfer pump P-3900-2 routes recovered liquids to slop | DBM SEC "Flare and Blowdown" |
| Upstream relief header (LP) nominal size | 508 mm (20 inch) carried in source basis | DBM SEC "Flare and Blowdown" |
| Flare stack arrangement | Discharges to shared HP/Cryo and LP dual flare stack (3-25/4-25 shared) | DBM SEC "Flare and Blowdown" |
| LP flare stack OD | TBD | DBM SEC "Flare and Blowdown" (explicit TBD) |
| Vessel orientation | TBD | Not specified in accessible source |
| Vessel design pressure | TBD | Not specified in accessible source |
| Vessel design temperature | TBD | Not specified in accessible source |
| Vessel internal diameter | TBD | Not specified in accessible source |
| Vessel tan-tan length | TBD | Not specified in accessible source |
| Internals (demister, vortex breaker, baffle) | TBD | Not specified in accessible source |
| Material of construction (shell, internals) | TBD | Not specified in accessible source |
| Corrosion allowance | TBD | Not specified in accessible source |
| Insulation / heat tracing | TBD | Not specified in accessible source |
| Pump P-3900-2 type / driver / rating | TBD | Not specified in accessible source |
| Instrumentation (LT, LIC, LSHH, LSLL, PT, TT) | TBD | Not specified in accessible source |
| Noise / area classification | TBD | Not specified in accessible source |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Inlet streams | TEG regeneration vent, VRU vent, compressor seal-pot vent | DBM SEC "Flare and Blowdown" |
| Service category | Low-pressure flare relief, hydrocarbon (potentially sour — see ASSUMPTION) | DBM whole-document context |
| Blowdown sequencing | Staggered blowdown required to limit maximum relief; sequencing per W242510-PRC-REP-000003-001 (not in workspace) | DBM SEC "Flare and Blowdown" |
| LP relief load / sizing case | TBD — final flare studies pending | DBM "Required Closeout" note |
| Operating temperature range | TBD | Not specified in accessible source |
| Operating pressure range | TBD | Not specified in accessible source |
| Liquid composition (hydrocarbon, water, TEG, glycol carry-over) | TBD | Not specified in accessible source |
| H2S / sour service exposure | ASSUMPTION: sour-service applicable per general project context (sour hydrocarbon service referenced elsewhere in DBM); confirmation TBD | DBM general isolation philosophy paragraph (line 607) |

## Construction

| Item | Value | Source |
|---|---|---|
| Vessel code | TBD (project pressure-vessel code basis not in accessible source slice) | TBD |
| Inspection / NDE basis | TBD | TBD |
| Pump configuration | 1 x 100 percent transfer pump P-3900-2, slop destination | DBM equipment summary line 584; DBM SEC "Flare and Blowdown" |
| Skid / mounting | TBD | TBD |
| Foundation requirements | Per project geotechnical and equipment-load basis (general project rule) | DBM SEC "Foundations" general paragraph |
| Interface tie-ins | LP relief header (20 inch / 508 mm); slop transfer line; instrument air and electrical from shared utility scope | DBM SEC "Flare and Blowdown"; DBM SEC "Utilities" |

## References

- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` — accessible authoritative DBM (3-25 Compression and Liquids).
- `_Sources/26020-Package_Requirements.docx`, package heading 35 — referenced as source basis row for this deliverable but not accessible in workspace as parsed text. Content dependent on this source remains TBD.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx` — Workbook Packages row 56 — referenced but not accessible as parsed text. Interface matrix details remain TBD.
- W242510-PRC-REP-000003-001 (Plant Shutdown and Blowdown Philosophy) — referenced by DBM; not in workspace.
- Gate 7 PROJECT_DECOMP snapshot — `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24`.
