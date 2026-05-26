# Guidance: Vendor Engineered Equipment Package

## Purpose

This guidance supports production of the Package Vendor production unit for PKG-074 Caustic Treating (NGL Mercaptan Removal). The package exists to turn accepted Gate 7 package/interface truth and the available 4-25 Deepcut DBM source slices into a vendor-engineered design basis and physical equipment package without inventing missing detailed mechanical specifications from the binary source that is not locally readable in this run.

## Principles

- Treat Gate 7 registers as accepted upstream truth for package identity, deliverable identity, interfaces, objectives, and artifacts.
- Treat the 4-25 Deepcut DBM source slices ("Current-Scope NGL Mercaptan Treating" and "Disulphide Oil, Spent Caustic, and Waste Amine") as the governing source for process basis, design parameters, equipment scope, and materials/installation constraints.
- Treat the third-party proprietary process provider's detailed engineering package as the eventual authority for stage count, vapour pressure cases, and detailed sizing; do not pre-empt those values.
- Treat the EPC Scope of Work (DEL-074-01) and EPC Package Datasheet (DEL-074-02) as the authoritative EPC handoff once formally accepted. Until then, mark the link as ASSUMPTION (package-grouping heuristic).
- Keep unsupported detailed requirements as `TBD` rather than inferring values from package name or workbook descriptors alone.
- Preserve the vendor-vs-EPC responsibility split recorded in PACKAGE_REGISTER.csv: vendor owns package engineering, package design, vendor documentation, and the physical equipment package; EPC Integrator owns facility-level integration, tie-ins, and constructability.

## Considerations

- The principal mechanical specification text for PKG-074 lives in 26020-Package_Requirements.docx package heading 28, which is a binary source not locally readable in this run. Requirements depending on that text are carried as TBD or as ASSUMPTION pending binary extraction.
- The 4-25 Deepcut DBM provides a usable process and design-parameter basis (rate, pressures, temperatures, caustic chemistry, equipment list, materials, indoor installation, incinerator interface) that can ground most of the vendor package envelope.
- Several design values are TBC at source: low/high pressure cases, circulating caustic concentration, fresh/DSO tank design SGs, contactor-stage count, winter vapour pressure values, high-ethane case, shower quantity/location, building floor and tank materials. These remain TBC in the four documents, not invented.
- The package is classified as common equipment (single train), so the vendor's maintenance access, isolation, and turnaround strategy is material to facility operability.
- Tagged equipment list is taken from the DBM common-equipment row (E-6720-1, H-6710-1, MX-6727-1, MX-6728-1, P-6720-1, P-6725-1, P-6730-1, P-6735-1, P-6726-1, P-6710-1, P-6711-1, V-6720-1). Vendor refinements may revise tags during detailed engineering.

## Trade-offs

| Topic | Trade-off | Current treatment |
|---|---|---|
| Vendor proprietary process vs. EPC-defined basis | Vendor selects/owns the detailed proprietary process design, but it must align with the EPC SOW, Package Datasheet, and DBM-defined performance and interfaces. | Cite DBM/EPC basis as authority; treat proprietary detailing as vendor scope. |
| Indoor caustic installation vs. layout/cost | Indoor installation is mandatory due to caustic freezing/crystallization risk, which constrains layout and increases building scope. | Carry indoor installation as a non-negotiable requirement. |
| Single-train common equipment vs. operational availability | Common equipment must be taken out of service for maintenance; sparing is at the component level (e.g., 2 x 100% filters and recycle pumps), not unit level. | Carry component-level sparing per DBM; flag unit-level outage in operability discussion. |
| Locally readable DBM vs. binary package requirements doc | DBM grounds process basis; binary doc holds detailed mechanical specification text. | Use DBM as primary source; mark binary-only content as TBD with explicit reference. |
| Workbook objective grouping vs. explicit objective mapping | OBJECTIVE_DELIVERABLE_MAP.csv lists OBJ-001/003/004/005/006/007/008/009/010 against DEL-074-04 as part of the package-grouping mapping. | Carry as ASSUMPTION (package-grouping heuristic) until human confirms a stricter mapping. |

## Examples

- Supported statement: "Design rate is 2,385 m3/d / 15,000 bbl/d." Source: 4-25_Deepcut_DBM.md, NGL Mercaptan Treating Design Parameters.
- Supported statement: "All caustic treating equipment is installed indoors due to caustic freezing/crystallization risk." Source: 4-25_Deepcut_DBM.md, NGL Mercaptan Treating Equipment and Utilities.
- Supported statement: "DSO and spent caustic vapours route to the 3-25 incinerator through a knock-out drum." Source: 4-25_Deepcut_DBM.md, Incinerator Interface.
- Unsupported statement unless binary source is read: "[Specific vendor documentation list rows from package heading 28]." Current treatment: TBD.
- Unsupported statement unless detailed engineering is complete: "[Final stage count for the caustic contactor]." Current treatment: TBD.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| HRR-074-04-001 | Detailed mechanical specification text for PKG-074 lives in a binary source not locally readable in this run. | _REFERENCES.md, Missing / Deferred References | ARTIFACT_REGISTER.csv, ART-EDAC8A3AB7 (Major included equipment evidence cites 26020-Package_Requirements.docx package heading 28) | Datasheet Construction; Specification Requirements; Specification Standards | Convert 26020-Package_Requirements.docx to a locally accessible source slice and re-run drafting; until then mark binary-only content as TBD. | TBD |
| HRR-074-04-002 | Objective-deliverable mapping (OBJ-001/003/004/005/006/007/008/009/010 to DEL-074-04) is package-grouped, not deliverable-specific. | _CONTEXT.md, Supports Objectives | OBJECTIVE_DELIVERABLE_MAP.csv, PKG-074 rows | Datasheet Identification | Treat objective association as ASSUMPTION (package-grouping heuristic) until human confirms. | TBD |
| HRR-074-04-003 | Several DBM design values are TBC and not yet closed (low/high pressure cases, circulating caustic concentration, fresh/DSO tank SG, shower quantity/location, building floor and tank materials, contactor stages, winter vapour pressure values, high-ethane case). | 4-25_Deepcut_DBM.md, NGL Mercaptan Treating Design Parameters | 4-25_Deepcut_DBM.md, NGL Mercaptan Treating Equipment and Utilities | Datasheet Conditions; Specification Requirements; Procedure Verification | Keep TBC items as TBD until detailed engineering or vendor proprietary process provider closes them. | TBD |
| HRR-074-04-004 | EPC-handoff basis (DEL-074-01 SOW and DEL-074-02 Package Datasheet) has not yet been produced or accepted; vendor package was drafted on the package-grouping basis. | DELIVERABLE_REGISTER.csv, DEL-074-01, DEL-074-02 | _DEPENDENCIES.md, Declared Upstream Dependencies (none declared) | Specification Scope; Procedure Prerequisites | Re-anchor the vendor package basis on accepted DEL-074-01 and DEL-074-02 once they exist; record dependency edges in _DEPENDENCIES.md. | TBD |
