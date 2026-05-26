# Guidance — DEL-062-04 Vendor Engineered Equipment Package (NGL Loading Pumps Building)

> Directional guidance for executing the vendor-engineered equipment package for PKG-062. This document gives rationale and considerations; binding requirements live in `Specification.md`.

## Purpose

DEL-062-04 carries the Package Vendor's production unit — engineering, package design, fabrication/supply, and the physical equipment package — for the NGL Loading Pumps Building. The package exists because the workbook (row 76) and `26020-Package_Requirements.docx` package heading 16 define a vendor-owned mechanical scope that must move LPG product from storage to truck loading using four parallel Blackmer LGL4B rotary vane pumps housed in a self-framing site building. [SOW-0153; SOW-0154; SOW-0155; SOW-0156]

The deliverable exists in support of the EPC package set (DEL-062-01 Scope of Work, DEL-062-02 Package Datasheet, DEL-062-03 Construction Work Package, DEL-062-05 Vendor Document Turnover, DEL-062-06 EPC Vendor Package Review and Acceptance). [DELIVERABLE_REGISTER row]

## Principles

1. **Vendor owns the package; EPC owns integration.** Package engineering, design, fabrication, equipment, and documentation are the Package Vendor's. Facility integration and interface review are the EPC Integrator's. Do not migrate vendor design work into EPC scope. [OBJ-004]
2. **Source-anchored design.** The workbook row and the heading-16 source set the binding scope envelope (pump count, model, capacity, drivers, building type, exclusions). Treat these values as authoritative until updated by a controlled change. [SOW-0153..SOW-0156]
3. **Cold-start design rules motor sizing.** Motors are sized on inlet stabilizer composition density at the −40 °C start-up condition — not on warm-running conditions. Do not relax this. [SOW-0156; R4.2]
4. **Local control with DCS as a separate boundary.** Local H-O-A / On-Off control is in scope; DCS integration is by others. The vendor's job is to expose clean control and I/O interfaces, not to perform the DCS integration. [SOW-0156; R5; OBJ-006]
5. **Boundary discipline at "by others" items.** Foundations, MCC power feed, and DCS integration are explicit exclusions. Confirm them at every boundary review. [SOW-0156; R8.1]

## Considerations

- **LPG service.** LPG is flammable and pressure-volatile. The vendor should select seals, materials, and area classification to match LPG truck-loading service even though the available source slice does not state these details. Treat any sour-service applicability question as `TBD` until resolved against OBJ-009. [OBJ-009; ASSUMPTION]
- **Parallel operation.** Four identical pumps in parallel are likely to require staged starting, surge/cavitation protection on the suction header, and balanced discharge piping. The vendor's hydraulic design should consider the storage-to-truck-loading hydraulic profile end-to-end. [SOW-0154; R2.2 TBC]
- **Self-framing building.** Building deliverables typically include HVAC, lighting, area classification, and life-safety provisions even when the source slice is silent. The vendor should engineer to LPG-service norms; the EPC should confirm against the facility electrical, HVAC, and fire/gas philosophies (OBJ-005, OBJ-006, OBJ-007). [SOW-0155]
- **Cold weather operability.** A −40 °C start-up requirement implies winterization, heat tracing, lubricant selection, and likely building heating choices that are not stated in the available source slice. Treat as `TBD` and engineer conservatively. [SOW-0156]
- **Site erection.** The self-framing building "to be erected at site" implies vendor responsibility for delivery and erection logistics — but foundations are "by others." Coordinate erection sequence with the EPC's foundation schedule (DEL-062-03). [SOW-0155; SOW-0156]
- **Document turnover.** Turnover scope/format is the subject of DEL-062-05. Aim the vendor document program at that deliverable rather than improvising. [OBJ-010; ASSUMPTION]

## Trade-offs

- **Vendor-engineered building vs. EPC-engineered building.** Source places the building inside the vendor package (self-framing, site-erected). Keeping it in vendor scope simplifies vendor responsibility for area classification and HVAC inside the building envelope but increases the vendor's exposure to site-specific civil and electrical interfaces. Do not unilaterally reassign the building to EPC scope. [SOW-0155; OBJ-004]
- **Local-only vs. DCS-tied control.** Source mandates local H-O-A / On-Off control and excludes DCS integration. A "DCS-only" control approach would violate the boundary; a "local-only with no DCS interface points" approach would fail integration. The right trade is a clean, documented interface that the EPC can integrate. [SOW-0156; OBJ-006]
- **Motor sizing margin.** Sizing strictly on cold-start density is required (R4.2). Adding margin is acceptable; reducing the basis is not. [SOW-0156]
- **TDH "TBC" vs. fixed value.** Source records 50 psid as the rated differential but flags TDH as "TBC." Locking TDH prematurely risks under-sized hydraulics if the storage-to-truck profile is more demanding than 50 psid; leaving it open too long delays motor and electrical sizing. Aim for early vendor confirmation against the actual hydraulic profile. [SOW-0155; SOW-0156]

## Examples

- *Interface drawing scope (example, ASSUMPTION).* A typical vendor package interface drawing set covers process tie-ins (suction, discharge, vents/drains), electrical tie-ins (MCC feed, grounding), controls tie-ins (DCS I/O list, local control panel), HVAC penetrations, and building anchor points to foundation. The source slice does not enumerate these; the vendor should adopt a standard set appropriate to LPG-service rotary vane pump packages. [ASSUMPTION]
- *Cold-start verification (example, ASSUMPTION).* Demonstrating R4.2 typically combines a vendor sizing calculation (composition density curve at −40 °C → required brake power → motor selection) with either a FAT cold-condition test or a site low-temperature start. The source slice does not prescribe the method. [ASSUMPTION]

## Conflict Table (for human ruling)

No source-vs-source conflicts identified in the available slice. (Internal SOW notes are mutually consistent and the workbook row aligns with `26020-Package_Requirements.docx` heading 16 as cited.)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| — | none open | — | — | — | — | — |
