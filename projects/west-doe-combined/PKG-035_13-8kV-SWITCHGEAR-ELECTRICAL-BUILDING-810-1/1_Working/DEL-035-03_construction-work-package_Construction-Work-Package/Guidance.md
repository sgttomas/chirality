# Guidance: DEL-035-03_construction-work-package

## Purpose

This guidance supports the EPC Integrator's Construction Work Package for `PKG-035` (13.8kV SWITCHGEAR ELECTRICAL BUILDING (810-1)). Building 810-1 houses the 13.8 kV main switchgear that anchors the plant's main power distribution. The Construction Work Package is the EPC Integrator's plan for how the vendor-supplied modular building and switchgear are received, set, tied in, inspected, energized, and turned over so that the rest of the facility electrical distribution can be brought online.

Building 810-1 is the gating electrical asset for facility energization. Construction sequence, tie-in readiness, and turnover quality at PKG-035 govern when downstream electrical buildings (6.9 kV, 4.16 kV, 600 V buildings) can be energized (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, radial distribution paragraph).

## Principles

1. **Respect the Package Vendor / EPC Integrator split.** Package Vendor owns engineering, design, fabrication, vendor documentation, and the physical switchgear and modular building. The EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. Construction Work Package activities must not silently expand into vendor engineering or design (`PACKAGE_REGISTER.csv` row `PKG-035`).
2. **Treat 810-1 as a gating asset.** The 13.8 kV bus is the plant main power distribution center sized for the full facility scope. Tie-in readiness for incoming utility supply and outgoing radial feeders shapes the overall energization sequence (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, facility electrical system and radial distribution paragraphs).
3. **Plan installation around bottom entry and pile elevation.** The building is elevated on piles to allow bottom-entry of incoming and outgoing power cables; cable routing, tray installation, and pull plans must be designed to that geometry (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings paragraphs).
4. **Maintain interface discipline across all twelve PKG-035 interface types.** Each interface type in `INTERFACE_REGISTER.csv` for `PKG-035` is in scope of construction coordination and turnover, even where the package-specific tie-in details remain TBD.
5. **Build in maintenance from day one.** Equipment doors/transoms sized for largest-equipment removal, GFI receptacles, ground wells, and cable routing clear of access lanes are construction-time decisions that cannot be added cheaply later (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings paragraphs).

## Considerations

- **Pre-energization checks dominate the schedule.** Grounding two-point verification, cable acceptance tests, protection settings (from vendor), and HVAC commissioning all gate energization.
- **Coordinate with civil/structural.** Piles, grading, drainage, and spill containment around 810-1 are construction interfaces; verify civil readiness before setting the building (`INTERFACE_REGISTER.csv` `IFC-A5DBFBF436`, `IFC-589CAC7BC6`).
- **Coordinate with the utility supply construction.** The 25 kV / 13.8 kV utility transformer and its connections are upstream of the 810-1 switchgear; energization of 810-1 cannot precede readiness of the utility step-down (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, facility electrical system paragraph).
- **Standby power basis has shifted.** The current basis is TOU standby generators at the LV MCC level with transfer switches, not a centralized 13.8 kV emergency-generator concept. Construction Work Package activities at 810-1 should not assume a 13.8 kV standby generator tie-in (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, line 2080, line 2943).
- **HVAC failure must not stop construction commissioning.** N+1 sizing is required; commissioning records should demonstrate the redundancy explicitly.

## Trade-offs

- **Pre-installation of cable tray vs. field routing.** DBM prefers shop pre-installation of main tray runs and limits field-run tray to field-constructed portions; the trade-off is fewer field hours vs. less in-field flexibility. Construction Work Package should follow the DBM preference and reserve field routing for interconnecting trays between racks, skids, and electrical buildings.
- **Energization sequencing.** Earlier energization of 810-1 enables downstream commissioning but raises construction-area safety controls (live MV). Sequence should be optimized against downstream readiness and live-work permitting, not just earliest possible date.
- **Witness points vs. schedule.** Package Vendor witness points (FAT/SAT, settings verification, energization) add schedule friction but provide acceptance evidence; bypassing them is not consistent with the Package Vendor / EPC Integrator split.

## Examples

- The DBM building list explicitly identifies "810-1 13.8kV Switchgear Electrical Building" as Shop-fabricated. The Construction Work Package treats receipt, transport, and setting as a single workface package rather than field assembly.
- DBM specifies 13.8 kV cables as three-conductor TECK rated 15 kV with 133 percent insulation, shielded. This is a fixed construction parameter; substitutions are not within the EPC Integrator's authority.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CFL-035-03-001 | DBM "Distance between fired heater and control room or electrical buildings = 25 m (82 ft)" cites OGAOM Sec. 9.6.15, but OGAOM clause text is not locally accessible. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 298 | OGAOM Sec. 9.6.15 (text not locally accessible) | Specification Standards; Datasheet Construction (installation location) | PROPOSAL: treat 25 m as design constraint citing DBM; mark OGAOM clause location TBD. | TBD |
| CFL-035-03-002 | DBM states a "13.8 kV tie-in eliminated" for standby power and that standby is now LV MCC-level with transfer switches (lines 2080, 2943). Package-level documentation that might still imply a 13.8 kV standby tie-in at 810-1 must not be carried into the Construction Work Package. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2080 | Workbook row 37 (does not contradict, but does not state) | Specification REQ-035-03-04/05; Guidance principles | PROPOSAL: explicitly exclude a 13.8 kV standby generator tie-in from PKG-035 construction scope. | TBD |

## Needs Human Ruling

- HRR-035-03-001: Specific pile foundation criteria, anchorage, and exact site location for Building 810-1 are not present in the accessible source slice. Proposed handling: keep foundation/pile specifics `TBD` until civil/structural source slice is provided.
- HRR-035-03-002: Detailed package-specific F&G tie-in, communications/network tie-in, utility piping, and drain/containment scope at 810-1 are not present in the accessible source slice. Proposed handling: keep these interface tie-ins coordinated but with detailed scope `TBD` until package-specific source content is available.
