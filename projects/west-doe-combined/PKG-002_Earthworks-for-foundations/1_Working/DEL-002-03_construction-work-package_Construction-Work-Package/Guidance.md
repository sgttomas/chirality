# Guidance: DEL-002-03 Construction Work Package

## Purpose

This guidance explains how to use the initial construction work package for `PKG-002 - Earthworks for foundations` without overstating the currently available source basis.

The deliverable exists because Gate 5 makes `Construction Work Package` a mandatory EPC Integrator anchor deliverable for every approved package. For this package, it must describe physical installation, construction, tie-in, inspection, and turnover into larger systems. Source: `PROJECT_DECOMP.md`, Gate 5 Accepted Basis; `DELIVERABLE_REGISTER.csv`, row `DEL-002-03_construction-work-package`.

## Principles

- Treat the accepted Gate 7 snapshot as the authoritative decomposition truth for identity, package membership, objectives, deliverable purpose, artifacts, and interface facts.
- Treat workbook row 3 and the Gate 7 registers as authoritative for package identity and interface flags.
- Treat the 03-25 DBM civil/construction slices as the accessible source basis for civil scope, drainage, access, foundations, geotechnical dependency, and construction scope context.
- Keep construction means, quantities, tolerances, workface sequence, ITP hold points, and turnover signoffs as `TBD` unless a local source defines them.
- Do not treat the decomposition narrative as a substitute for final geotechnical, IFC drawing, construction specification, or discipline execution criteria.

## Considerations

| Topic | Guidance |
|---|---|
| Foundation closure | The DBM explicitly requires the final geotechnical report before foundation design closure. Avoid closing foundation type, pile details, settlement criteria, frost protection detail, or acceptance criteria in this CWP until the geotechnical basis and civil design are available. |
| Drainage and containment | The package has confirmed interface flags for grading/site drainage/spill containment. The CWP should surface drainage/containment tie-ins, but routing and tie-in points are `TBD` unless defined by IFC civil drawings or drainage design. |
| Structural/foundation/support interfaces | The package has a confirmed structural/foundations/supports interface. The CWP should coordinate with equipment loads, snow/wind/seismic criteria, frost protection, vibration, settlement, and maintenance access, but package-specific values remain `TBD`. |
| Winter construction/access | The 03-25 DBM gives a -40 deg C to +35 deg C ambient basis and identifies road access, drainage, foundations, and module layout impacts. Use this as a planning constraint, not as a complete winter construction procedure. |
| Responsibility | The package register says responsibility is EPC Integrator or discipline subcontractor source-dependent. Assign coordination to the EPC Integrator and keep subcontractor assignment `TBD` unless separately confirmed. |

## Trade-offs

- Early CWP drafting improves package coordination, but premature closure of geotechnical-dependent values would create false precision.
- Carrying broad DBM civil/construction scope helps preserve interfaces, but the CWP should distinguish relevant PKG-002 work from adjacent civil packages such as site grading, containment berms, retention pond, pipe racks, buildings, and roads.
- Using `TBD` for execution details creates open items, but it preserves source fidelity until IFC-level civil/foundation documents are available.

## Examples

- Source-supported: "Address Grading / Site Drainage / Spill Containment and Structural / Foundations / Supports interfaces" because workbook row 3 and `INTERFACE_REGISTER.csv` identify these interface types.
- Source-supported: "Do not close foundation design until the final geotechnical report is available" because the 03-25 DBM states this dependency.
- Not source-supported yet: exact excavation limits, compaction requirements, pile sizes, hold points, workface sequence, or turnover signoff names.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| None | No source conflict identified during P1/P2 drafting. Unsupported detail is marked `TBD` rather than treated as conflict. | N/A | N/A | N/A | N/A | N/A |
