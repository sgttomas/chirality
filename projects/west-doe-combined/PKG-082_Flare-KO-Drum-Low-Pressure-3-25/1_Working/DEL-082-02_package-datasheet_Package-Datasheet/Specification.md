# Specification — DEL-082-02 Package Datasheet (Flare KO Drum, Low Pressure, 3-25)

## Scope

### In scope
- Technical datasheet content for the LP flare knock-out drum package PKG-082, vessel tag V-3900-2, and its associated transfer pump P-3900-2, sized as one 100 percent unit.
- Capture of LP-flare service definition (receives TEG regeneration, VRU, and compressor seal-pot services per the 3-25 DBM Flare and Blowdown section).
- Capture of declared interfaces: LP relief header (20 inch / 508 mm), discharge to shared LP/HP-Cryo dual flare stack, slop transfer destination, utility tie-ins from shared 03-25/04-25 utility scope.
- Identification of design data items required for third-party vendor or discipline-package engineering, including items currently `TBD` pending source resolution.

### Out of scope
- HP flare KO drums V-4100-2 and V-4150-2 (separate package scope per DBM equipment summary).
- Shared flare stack mechanical and structural design (governed by shared 03-25/04-25 flare studies).
- Plant shutdown and blowdown sequencing philosophy (governed by W242510-PRC-REP-000003-001, not in workspace).
- Final emissions tables (per DBM "Required Closeout" — pending final flare studies).

## Requirements

| Req ID | Requirement | Basis / Source | Label |
|---|---|---|---|
| R-01 | The package shall comprise one LP flare knock-out drum, tag V-3900-2, with one 100 percent transfer pump, tag P-3900-2. | DBM "Flare and Blowdown" (lines 495-499); DBM equipment summary (line 584) | FACT |
| R-02 | V-3900-2 shall be capable of receiving and separating liquid from the combined LP relief streams from TEG regeneration, VRU, and compressor seal-pot services. | DBM "Flare and Blowdown" (line 499) | FACT |
| R-03 | P-3900-2 shall transfer recovered liquids from V-3900-2 to the slop system. | DBM "Flare and Blowdown" (line 499) | FACT |
| R-04 | The LP relief header tie-in shall be 508 mm (20 inch) nominal in the current source basis. | DBM "Flare and Blowdown" (line 499) | FACT |
| R-05 | Outlet vapor shall route to the shared LP flare stack of the HP/Cryo and LP dual flare stack. LP stack OD is `TBD`. | DBM "Flare and Blowdown" (line 499) | FACT (with TBD on stack OD) |
| R-06 | The package design shall be compatible with staggered blowdown to limit maximum relief load. Final blowdown sequencing per W242510-PRC-REP-000003-001 — `location TBD` (document not in workspace). | DBM "Flare and Blowdown" (line 501) | FACT (with TBD on referenced doc) |
| R-07 | The vessel shall be designed to a pressure-vessel code applicable to the project (specific code edition `TBD` — not present in accessible source slice). | TBD | TBD |
| R-08 | Vessel design pressure, design temperature, dimensions, internals, materials of construction, and corrosion allowance shall be defined to support the relief case from final flare studies. Specific values `TBD`. | DBM "Required Closeout" (line 555) | TBD |
| R-09 | The pump P-3900-2 type, driver, capacity, head, NPSH, materials, seal arrangement, and area classification shall be defined consistent with sour hydrocarbon service if confirmed. Specific values `TBD`. | TBD | TBD |
| R-10 | Sour-service materials and isolation safeguards shall be specified consistent with the project sour-service basis. (DBM general isolation paragraph, line 607.) | DBM general isolation philosophy | ASSUMPTION (sour-service applicability to LP KO drum specifically requires confirmation) |
| R-11 | Drain and vent connections shall route to the correct flare, drain, or closed system per pressure, sour-service, and contamination classification. | DBM general isolation philosophy (line 607) | FACT |
| R-12 | Foundations and anchorage shall meet project geotechnical, seismic, wind, snow, frost, vibration, and access requirements for tall vessels and flare-system equipment. | DBM "Foundations" (line 700) | FACT |
| R-13 | Instrumentation (level, pressure, temperature, high/low level shutdowns, alarms, control) shall be defined consistent with project safeguarding and SIS requirements. Specific tag and set-point list `TBD`. | TBD | TBD |

## Standards

| Standard / Reference | Coverage | Location |
|---|---|---|
| Project pressure-vessel code basis | Vessel design and fabrication | `location TBD` (not in accessible source slice) |
| Project piping code basis | Tie-in piping (LP relief header, pump suction/discharge, drain/vent) | `location TBD` |
| W242510-PRC-REP-000003-001 (Plant Shutdown and Blowdown Philosophy) | Staggered blowdown sequencing affecting LP relief load | Not in workspace — `location TBD` |
| Project Hazardous Area Classification basis | Pump motor and instrument area classification | `location TBD` |
| Project sour-service / NACE basis | Materials selection if sour confirmed | `location TBD` |
| 26020-Package_Requirements.docx, package heading 35 | Project-wide package datasheet content and format requirements | Not accessible as parsed text — `location TBD` |
| 26020-Packages_Interfaces_4_export.xlsx, Workbook Packages row 56 | Interface matrix for PKG-082 | Not accessible as parsed text — `location TBD` |

## Verification

| Req ID | Verification Approach |
|---|---|
| R-01 | Equipment list and datasheet review against DBM equipment summary. |
| R-02 | Process flow and heat-and-material-balance review against LP relief stream definition. |
| R-03 | P&ID and equipment-list review confirming P-3900-2 discharge to slop. |
| R-04 | Piping line list and isometric review confirming 508 mm / 20 inch LP relief tie-in. |
| R-05 | Flare system layout and stack datasheet review (separate scope). LP stack OD verification deferred until shared flare study issued. |
| R-06 | Cross-discipline review against W242510-PRC-REP-000003-001 when available. |
| R-07-R-09 | Vendor / discipline-package engineering review with finalized inputs. |
| R-10 | Materials review against confirmed sour-service basis. |
| R-11 | P&ID review of vents and drains. |
| R-12 | Foundation and anchorage calculation package review. |
| R-13 | SIS / safeguarding review and C&E matrix sign-off. |

## Documentation

Anticipated artifacts (from `_CONTEXT.md`):

- Package technical datasheet (this deliverable).
- Vendor engineering handoff basis.
- Package interface requirements matrix.
- Source-supported equipment and design criteria summary.

Additional documentation expected from downstream vendor engineering:

- Vessel mechanical datasheet (V-3900-2).
- Pump datasheet (P-3900-2).
- Instrumentation index and SIS C&E.
- Piping line list and tie-in schedule for LP relief header, slop transfer, and utility tie-ins.
- Final relief and blowdown load reconciliation against flare studies.
