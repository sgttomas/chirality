# Specification — PKG-104 Package Datasheet (Structural Steel — Outside of Modules)

> Normative requirements for the package-datasheet artifact and for the structural-steel scope it describes. Requirements are derived only from accessible source slices. Inferred requirements are labeled **ASSUMPTION**; values not in the accessible source set are marked **TBD** and not invented.

## Scope

**In scope.** The DEL-104-02 Package Datasheet shall present the technical data set required for a third-party structural-steel vendor or discipline subcontractor to begin engineering the PKG-104 scope: structural steel installed outside of process and utility modules at the West Doe expansion facility. Typical in-scope items (ASSUMPTION, per the package title and the DBM module inventory): field-erected pipe racks, equipment support structures, tank-farm support steel, transformer support steel, cable-tray support modules on pipe racks, miscellaneous platforms and access steel, and field-erected structural steel supporting truck-loading and similar facilities.

**Out of scope.** Structural steel that is internal to shop-fabricated process or utility modules listed in the DBM module table (`DBM-Deepcut` lines ~2766-2818) is not part of PKG-104 and is excluded from this datasheet (ASSUMPTION based on package title "outside of modules"). Foundation design (piles, pile caps, concrete) is governed by the Civil/Foundations package; PKG-104's steel scope is to be designed to interface with that foundation basis. Process equipment, piping, electrical, and controls are out of scope except where structural support interfaces are required.

## Requirements

### R-1 — Codes and Standards (Mandatory)
Structural steel design, fabrication, and erection for this package shall comply with:
- National Building Code of Canada (current edition) — building code basis. Source: `DBM-Deepcut` line ~2672.
- CAN/CSA-S16 — Design of Steel Structures (current edition; CSA S16:19 cited in `DBM-Deepcut` line ~3412). Source: `DBM-Deepcut` line ~2673.
- CSA G40.20/G40.21 — rolled or welded structural quality steel; CSA G40.20-13/G40.21-13 cited. Source: `DBM-Deepcut` lines ~2676, ~3411.
- CSA W59-18 — Welded steel construction. Source: `DBM-Deepcut` line ~3413.

### R-2 — Material Grades (Mandatory)
- W-flange and HSS sections shall be CSA G40.20/G40.21 **350W**.
- Channels, plates, and angles shall be CSA G40.20/G40.21 **300W**.
- Source: `DBM-Deepcut` line ~2676.

### R-3 — Environmental Design Conditions (Mandatory)
- Minimum design ambient temperature: **-40 deg C**. Metallurgy of exposed steel shall be compatible with this minimum where affected by low temperature. Source: `DBM-Comp_and_Liquids` line ~145.
- Snow, rain, wind, and seismic loading: per the National Building Code of Canada for the project site. Source: `DBM-Deepcut` §"Buildings and Miscellaneous Facilities" (line ~2753); `DBM-Comp_and_Liquids` §"Foundations and Structural Supports" (line ~700).

### R-4 — Foundation Interface (Mandatory)
The structural-steel package shall interface with driven-steel-pile foundations, which are the default support basis for buildings, equipment, towers, tanks, modules, pipe racks, and similar structures. Pile-cap elevations and connection geometry shall be coordinated with the Civil/Foundations package. Final pile-design parameters are TBD pending the geotechnical report. Source: `DBM-Deepcut` lines ~2740, ~2749.

### R-5 — Pipe-Rack Grading Coordination (Mandatory)
Pipe-rack steel design shall accept top-of-pile-cap elevations consistent with the site grading basis: high equal-elevation ridges along main pipe racks, pad slopes 1.5% to each side (reducible to 1.0% where required to maintain reasonable top-of-pile-cap elevations). Source: `DBM-Deepcut` lines ~2708-2710.

### R-6 — Cable-Tray Support Modules (Mandatory where applicable)
Where the package includes pipe-rack-top cable-tray support modules, those modules shall:
- be located on the uppermost sections of pipe racks;
- include a construction walkway and tray support brackets on each side of the walkway where practical;
- provide tray covers where mechanical protection is required against falling materials;
- be sized with at least **30%** future tray growth capacity.
- Source: `DBM-Deepcut` line ~3023.

### R-7 — Hazardous-Area Compatibility (Informational / Mandatory if applicable)
Outdoor pipe racks are general-purpose non-hazardous areas unless detailed area-classification drawings identify otherwise; steel design does not need to satisfy hazardous-area equipment ratings, but coordination with detailed classification drawings is required. Source: `DBM-Comp_and_Liquids` line ~722.

### R-8 — Datasheet Completeness (Mandatory)
The Package Datasheet artifact shall contain at minimum: package identity; boundary statement; governing codes and standards; material grades; environmental design conditions; foundation/grading interface; tag/equipment list of supported equipment (TBD until accessible source slice — see Documentation); package interface requirements matrix (TBD until accessible source slice from `26020-Packages_Interfaces_4_export.xlsx`); list of accepted source materials. ASSUMPTION derived from `_CONTEXT.md` "Anticipated Artifacts".

## Standards

| Standard | Title | Applicability | Source |
|---|---|---|---|
| National Building Code of Canada | Building code | Loading, egress, building basis | `DBM-Deepcut` line ~2672 |
| CAN/CSA-S16 (S16:19) | Design of Steel Structures | Primary design code | `DBM-Deepcut` lines ~2673, ~3412 |
| CSA G40.20-13/G40.21-13 | Rolled/welded structural quality steel | Material basis | `DBM-Deepcut` lines ~2676, ~3411 |
| CSA W59-18 | Welded steel construction | Welding | `DBM-Deepcut` line ~3413 |
| Canadian Foundation Engineering Manual | Foundation engineering | Foundation interface (Civil package) | `DBM-Deepcut` line ~2675 |

## Verification

| Requirement | Verification Approach |
|---|---|
| R-1 Codes | Review of vendor/discipline design submittal package; check stamped drawings cite NBCC, CSA S16, G40.20/21, W59. |
| R-2 Materials | Review of bill of materials and mill test reports against grade requirements (350W / 300W). |
| R-3 Environmental | Review of design-load report against project site loads and -40 deg C minimum. |
| R-4 Foundations | Review of anchorage details against Civil package pile-cap basis; interface signoff. |
| R-5 Grading | Cross-check of top-of-pile-cap elevations against Civil grading drawings. |
| R-6 Cable-tray modules | Walkway/tray-bracket arrangement check; confirmation of ≥30% growth allowance in tray cross-section sizing. |
| R-7 Hazardous areas | Cross-check against issued area-classification drawings (TBD; classification drawings outside accessible source set). |
| R-8 Datasheet completeness | Editorial review of issued datasheet against required content list. |

## Documentation

The Package Datasheet shall be accompanied by, or reference, the following supporting documents (anticipated artifacts per `_CONTEXT.md`):

- Package technical datasheet (this deliverable).
- Vendor engineering handoff basis (companion narrative; ASSUMPTION — actual artifact location TBD).
- Package interface requirements matrix (to be populated from `26020-Packages_Interfaces_4_export.xlsx` — location TBD; binary source not parsed in this run).
- Source-supported equipment and design-criteria list (TBD — supported-equipment list for outside-of-module steel is not in accessible source slices and must be assembled during detailed engineering or sourced from Workbook Packages row 105 in `26020-Package_Requirements.docx`).
