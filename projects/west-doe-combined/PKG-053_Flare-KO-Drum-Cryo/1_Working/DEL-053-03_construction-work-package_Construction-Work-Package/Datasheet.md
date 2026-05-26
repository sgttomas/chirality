# Datasheet — DEL-053-03 Construction Work Package (Flare KO Drum, Cryo)

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-053-03_construction-work-package` |
| DeliverableName | Construction Work Package |
| ParentPackageID | `PKG-053` |
| PackageName | Flare KO Drum (Cryo) |
| Workbook Row | 53 |
| Facility | 04-25 (Deepcut) — `DBM-Deepcut/4-25_Deepcut_DBM.md` §SEC-09 Flare / §Modularization |
| Discipline | Mechanical (EPC Construction Work Package) |
| Type | EPC Construction Work Package |
| ResponsibleParty | EPC Integrator |
| Decomposition Snapshot | `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` |

## Attributes (Package Equipment in Construction Scope)

Source: `DBM-Deepcut/4-25_Deepcut_DBM.md` §Equipment List rows 11-12 and §SEC-09 Flare Equipment and Routing.

| Tag | Service | Quantity | Source SectionRef |
|---|---|---:|---|
| `V-4110-1` | Cryo Flare K.O. Drum | 1 | DBM-Deepcut row 12 (Equipment List) |
| `H-4112-1` | Cryo Flare K.O. Drum Immersion Heater | 1 | DBM-Deepcut row 11 (Equipment List); SEC-09 routing table |

Module designation: `410-1 HP / Cryo Flare KO Drum Module` — Shop-built (DBM-Deepcut §Modularization List).

ASSUMPTION: the package "Flare KO Drum (Cryo)" maps to V-4110-1 and the H-4112-1 immersion heater per equipment-list rows 11-12; the HP element V-4100-1 is carried in PKG-054 and is co-located on the same shop module 410-1 (DBM-Deepcut §Modularization). Construction-interface implications of this co-mounting are noted in Section "Conditions" below and TBD pending package-split confirmation.

## Conditions (Site and Installation Basis)

| Parameter | Value | Source SectionRef |
|---|---|---|
| Plot location | 04-25 Deepcut facility; cryogenic flare KO drum located adjacent to cryogenic process modules | DBM-Deepcut §SEC-09 Flare Equipment and Routing |
| Common flare stack location | 03-25 facility (HP/Cryo stack physically at 03-25, shared 03-25/04-25) | DBM-Deepcut §SEC-09 Flare Equipment and Routing |
| Cryogenic relief header size | 610 mm (24 in), 304SS, ~140 m long with 5 m tie-in slack basis | DBM-Deepcut §Flare Header and Backpressure Basis |
| Combined HP/cryo header (downstream of KO drums) | 762 mm (30 in), 304SS, ~90 m tie-in basis | DBM-Deepcut §Flare Header and Backpressure Basis |
| Built-up backpressure (peak) | 695 kPag (100 psig) at peak blowdown / fire-zone load | DBM-Deepcut §Flare Header and Backpressure Basis |
| Header heat trace | Cryogenic flare headers NOT heat traced (water not expected) | DBM-Deepcut §SEC-09 Flare narrative |
| Spacing — flare/KO tanks to vegetation or fire hazards | ≥10 m (32 ft) | DBM-Deepcut §SEC-04 Flare and Incinerator Spacing (OGAOM 9.6.15) |
| Spacing — flare to public road / property line | ≥80 m (262.5 ft) | DBM-Deepcut §SEC-04 (OGAOM 9.6.15) |
| Vessel design temperature (cold side) | TBD — relief case scenarios for sub -45.5 deg C cryogenic service govern; vendor datasheet to confirm | DBM-Deepcut §SEC-09 cryogenic flare scope statement |
| Vessel design pressure | TBD — vendor datasheet pending; bounded by HP/cryo PSV set pressures | TBD |
| Foundation criteria | Per final geotechnical report, equipment loads, snow/wind/seismic, frost, vibration, settlement, maintenance access; flare/stack elements and tall vessels require equipment-specific anchorage checks | DBM-Deepcut §SEC-04 Foundations |

## Construction (Construction Work Package Composition)

The Construction Work Package itself is the deliverable; the entries below describe its expected work-product composition for installation, build, inspection, and turnover of `V-4110-1` and `H-4112-1` and module 410-1.

| Work-Package Element | Content | Source / Basis |
|---|---|---|
| Installation Workface Plan | Set, level, grout, anchor module 410-1 on its foundation; lift plan for KO drum vessel and immersion heater | ASSUMPTION (industry-standard CWP composition; not enumerated in source) |
| Tie-In List | Cryogenic relief header tie-ins (610 mm, 24 in, 304SS); combined HP/cryo outlet (762 mm, 30 in, 304SS); immersion heater electrical, instrument, drain, vent, and instrument-air interfaces | DBM-Deepcut §Flare Header and Backpressure Basis; ASSUMPTION on full interface list TBD until P&ID issue |
| Welding & NDE Plan | WPS/PQR per pressure piping code; 100% RT of cryogenic service welds (TBD — code clause `location TBD`) | TBD — governing piping code clause not in accessible source slice |
| Pre-Commissioning Plan | Hydrotest of vessel and relief piping per code; cleaning of cryogenic service to dryness; purge and lock-out | TBD — vendor procedures pending |
| Inspection & Test Plan (ITP) | Vessel receipt inspection, dimensional, NDE review, pressure test, immersion-heater electrical commissioning, control loop checkout | ASSUMPTION (industry-standard ITP scope) |
| Turnover Checklist | Mechanical Completion → Ready for Commissioning → Ready for Start-up gates with punchlist closeout | ASSUMPTION (industry-standard EPC turnover gates) |
| Construction Interface Register | Tie-ins to PKG-054 (HP Flare KO Drum, co-mounted on module 410-1); interfaces to 03-25 common HP/cryo stack; civil/structural; electrical heat-trace exclusion zone documentation | DBM-Deepcut §Modularization; §SEC-09 Flare |

## References

- `DBM-Deepcut/4-25_Deepcut_DBM.md` — SEC-04 Site, Layout, and Spacing; SEC-09 Flare; Equipment List; Modularization List
- `26020-Package_Requirements.docx` — package heading 8 (binary `.docx`; relevant text not directly readable in this run — content marked **location TBD**)
- `26020-Packages_Interfaces_4_export.xlsx` — package row 53 (binary `.xlsx`; **location TBD** as above)
- Decomposition: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` — row `DEL-053-03_construction-work-package`
