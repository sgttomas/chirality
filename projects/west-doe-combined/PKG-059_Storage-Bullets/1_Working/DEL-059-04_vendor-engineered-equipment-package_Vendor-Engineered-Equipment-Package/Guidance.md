# Guidance — DEL-059-04 Vendor Engineered Equipment Package

> Directional guidance for the Package Vendor and the EPC Integrator's reviewer. This document does not impose new requirements; it explains intent, principles, considerations, and trade-offs grounded in accessible sources.

## Purpose

The Vendor Engineered Equipment Package exists to convert the EPC-issued Scope of Work and Package Datasheet for PKG-059 NGL storage bullets into a vendor-engineered, fabricated, and supplied physical equipment package. The upstream basis explicitly identifies the detailed bullet design parameters as a required design-development item, so the vendor's engineering work is on the project's critical-design path, not a routine commodity purchase. [Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 1629, 1814.]

## Principles

1. **Source fidelity over convention.** Vendor design decisions shall be traceable to the EPC SOW, Package Datasheet, and the project DBM. Where the DBM defers a parameter to design development (e.g., bullet pressure, temperature, materials), the vendor's value is a proposal that requires EPC Integrator acceptance — not a vendor convention asserted as fact. [Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 1629.]

2. **API 2510 governs pressurized bullet spacing.** All cluster-internal geometry, cluster-to-cluster separation, and bullet-to-adjacent-equipment offsets shall be consistent with API 2510 spacing rules quoted in the DBM minimum spacing tables. Deviations require explicit EPC ruling. [Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §2.5 lines 245-259, line 284, line 299.]

3. **Spill containment is a co-designed interface.** Grading and containment beneath the bullets is owned by site civil but is shaped by the bullet layout. The vendor shall provide drainage/containment interface points consistent with sloped grading that redirects NGL away from the pipe rack and process areas to reduce pool-fire exposure. [Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2722.]

4. **Clear scope boundaries.** Package deliverables shall preserve clear boundaries among process vendors, electrical/controls systems, field construction, and cross-facility utility interfaces. Ambiguous boundary content is the leading cause of late-stage commercial rework. [Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 617.]

5. **Document register is a first-class deliverable.** A complete vendor document register (datasheets, C&E, utility loads, relief/load data, field tie-ins, envelopes, sparing, materials/coatings, maintenance access, shipped-loose items) is the package's "product" alongside the hardware. [Source: same line 617.]

## Considerations

- **No truck or rail distribution at 04-25.** Vendor design need not include truck/rail loading provisions for NGL from this facility. [Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 446.]
- **C3+ NGL product service, not C3/C4 split.** The current basis replaces the retired C3/C4 storage concept (which would have driven butane/propane segregation per the API 2510 butane-to-propane spacing rule). Vendor proposals built on a C3/C4 split assumption should be challenged. [Source: lines 1627-1629; spacing rule line 251.]
- **Property-line spacing dominates plot.** 38.1 m (125 ft) to property line is the largest single bullet-area spacing requirement and frequently controls overall plot layout. Vendor cluster proposals should highlight property-line implications early. [Source: line 259.]
- **Pump suction interface is tight.** 3.05 m (10 ft) bullet-to-pump-skid spacing means the package's external nozzle layout interacts directly with pump-skid placement. [Source: line 252.]
- **Pressure-vessel code is not stated in source.** Available DBM excerpts do not name the governing pressure-vessel code (e.g., ASME Section VIII). Vendor and EPC should confirm jurisdictional code at kick-off rather than assume from convention.
- **Workbook/`.docx` source slice not rendered.** The decomposition cites `26020-Package_Requirements.docx` package heading 14 as the package source row. That binary file is present in `_Sources/` but is not locally rendered to markdown; substantive content from it is `TBD` until extracted.

## Trade-offs

| Trade-off | Tension | Disposition |
|---|---|---|
| Cluster size vs. plot footprint | Larger clusters (up to 6 bullets) reduce inter-cluster spacing demand but concentrate fire risk and complicate isolation. | API 2510 caps cluster at <=6; final cluster sizing is a vendor proposal subject to EPC acceptance. [Source: line 249.] |
| Vendor convention vs. project DBM | Vendor catalog defaults may not match project DBM intent (e.g., insulation, materials). | DBM and EPC SOW govern; vendor catalog defaults are starting points, not facts. (ASSUMPTION pending EPC ruling on each parameter.) |
| Containment beneath bullets vs. drainage routing | Sloped grading away from pipe rack favors fire safety; routing toward containment basins favors operability/cleanup. | DBM identifies the safety priority (away from pipe rack/process areas); vendor and civil shall co-design tie-in geometry. [Source: line 2722.] |
| Package self-sufficiency vs. facility utility supply | Skid-internal utility systems shorten field work; facility-supplied utilities reduce duplication. | Project-wide basis favors clear cross-facility utility interfaces with package boundaries. [Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 617.] |

## Examples

- Spacing-table application: A 16-bullet inventory at <=6/cluster requires at least three clusters (e.g., 6+6+4) with >=15.24 m (50 ft) between clusters. Vendor layouts proposing fewer clusters are non-compliant with API 2510 as quoted in the DBM. [Source: line 249, line 250.]
- Pump-skid interface: If the pump skid taking suction from the bullets is placed against the cluster, the minimum 3.05 m (10 ft) bullet-to-pump-skid offset sets the skid's near-bullet edge. [Source: line 252.]

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-1 | Governing pressure-vessel code for NGL bullets is not named in any accessible source slice. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §"NGL Storage Bullets" (silent) | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 617 (silent on code) | Specification R-4.2; Datasheet "Materials of construction" | PROPOSAL: ASME Section VIII (Div 1 or 2) per common jurisdictional practice | TBD |
| C-2 | LPG terminology in spacing criteria vs. NGL process-scope basis. DBM notes "LPG terminology... is retained as a spacing-code descriptor for API 2510 application. It does not change the current process-scope basis for NGL treating and product handling." | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 274 | Implicit NGL scope at lines 1627-1629 | Specification R-2.x labeling | PROPOSAL: retain "pressurized bullet" terminology consistently; apply LPG-spacing rules to NGL service per source note | TBD |
| C-3 | `26020-Package_Requirements.docx` package heading 14 (cited in `_REFERENCES.md` and `_CONTEXT.md`) has not been rendered to a markdown source slice. | `_CONTEXT.md` "Source Reference" | `_REFERENCES.md` "Source Materials Referenced By Decomposition Row" | All four documents (gaps in detailed package-requirements content) | PROPOSAL: extract heading 14 to a markdown slice and re-run Pass 2/3 | TBD |
| C-4 | `_CONTEXT.md` lists OBJ-001/003-010 as "Supports Objectives" via package heuristic; objective-to-deliverable mapping at deliverable-ID level is not confirmed. | `_CONTEXT.md` Supports Objectives | `OBJECTIVE_DELIVERABLE_MAP.csv` (Gate-7 snapshot) | Datasheet Identification; project traceability | PROPOSAL: human confirmation of objective association at deliverable-ID resolution | TBD |
