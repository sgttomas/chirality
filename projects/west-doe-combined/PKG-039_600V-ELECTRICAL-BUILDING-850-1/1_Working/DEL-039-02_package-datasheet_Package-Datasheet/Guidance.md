# Guidance: DEL-039-02_package-datasheet

## Purpose

The Package Datasheet exists to convert the accepted Gate 7 package basis for `PKG-039` into a source-supported technical handoff document for the 600V ELECTRICAL BUILDING (850-1). It should let the Package Vendor understand the EPC integration basis for the prefabricated modular electrical building serving the 600 V Inlet / Sales Compressor area while keeping EPC-owned facility interfaces distinct from vendor-owned package design.

## Principles

- Preserve source spelling and identity. The package name is carried as "600V ELECTRICAL BUILDING (850-1)" because that is the workbook and Gate 7 register spelling.
- Treat workbook interface `X` facts as evidence under the Package Datasheet, not as separate deliverables. All twelve applicable interfaces are reflected.
- Keep vendor-owned design work (building fabrication, internal MCC/UPS/transformer/panelboard lineup, HVAC sizing) with the Package Vendor and facility-level integration (feeder from 13.8 kV switchgear, grounding tie-in, standby power transfer, plot-plan siting) with the EPC Integrator.
- Use `TBD` for 600 V MCC bus rating, UPS quantity/sizing, distribution-transformer kVA, panelboard schedules, building footprint, HVAC capacity, foundation/pile design, fire-and-gas population, and exact siting until a source-supported package-specific basis is available.
- Use the DBM electrical basis at the level it supports: building type, voltage and service classes, UPS service basis, standby power interface, grounding/bonding, cable/raceway methodology, HVAC n + 1 sizing rule, lighting, and receptacle conventions.

## Considerations

The DBM electrical design basis explicitly lists building 850-1 in the building-allocation table as the "600V Inlet / Sales Compressor Electrical Building," confirming both the building name and its served compressor area. The 13.8 kV switchgear paragraph confirms that the 600 V electrical buildings are radially fed via step-down transformers from the plant main switchgear. The voltage table confirms 600 V, 3-phase, 3-wire, 60 Hz, high-resistance grounded with 5 A continuous resistor as the LV service class for motors up to 250 hp, lighting/utility transformers, building heaters, and UPS larger than 10 kVA.

The Electrical Buildings section enumerates the equipment that "may" be housed in electrical buildings as required by detailed design. This is a permissive list, not a confirmed lineup for 850-1; vendor-facing datasheet content reflects this by carrying the list as anticipated population while marking the specific lineup as `TBD`. The standby-power basis is preserved as a TOU LV-MCC-level generator/transfer-switch interface with sizing and configuration `TBD`, consistent with the DBM Standby Power paragraph.

Grounding and bonding are applicable interface topics. The DBM provides facility grounding basis (driven-pile electrodes, main #2/0 conductor, two-point connection for major equipment, ground wells at electrical buildings, separate copper conductor for distribution transformers, panelboards, and >100 hp three-phase motors per CEC). The datasheet should require coordination with this basis without inventing package-specific conductor sizing.

Maintenance access is both an explicit workbook interface fact and a DBM constraint for cable tray and conduit routing as well as for equipment-door sizing in electrical buildings. The datasheet should require routing and physical placement to preserve maintenance access while leaving detailed clearances to detailed design.

## Trade-offs

| Topic | Conservative position | Reason |
|---|---|---|
| Internal equipment lineup | Mark `TBD` pending package-specific source confirmation; list anticipated population per DBM. | DBM lists what electrical buildings *may* house; specific 850-1 lineup is not in the accessible source set. |
| 600 V MCC bus rating / UPS sizing | Carry as `TBD`. | Sizing depends on connected Inlet/Sales Compressor loads not enumerated in the available source slices. |
| Building footprint and foundation | Identify pile-elevated, bottom-entry basis only; mark footprint and pile schedule `TBD`. | DBM gives the elevation/bottom-entry convention but not building-specific dimensions. |
| Standby generator | Carry TOU LV-MCC interface only; sizing, transfer scheme, and load-shedding `TBD`. | DBM explicitly leaves these open. |
| Standards | List CEC, NEMA VE2, area classification, project electrical specs, and building code as governing bases with locations `TBD`. | DBM references these bases but detailed clauses and project specs are not available in the deliverable folder. |

## Examples

- Acceptable datasheet entry: "Low-voltage service: 600 V, 3 ph, 3 W, 60 Hz, high-resistance grounded with 5 A continuous resistor. Source: DBM voltage and service table."
- Acceptable source-gap entry: "Building footprint and pile schedule: TBD. No package-specific source slice available."
- Not acceptable without new source: "600 V MCC bus rated 2000 A with 65 kA short-circuit; building footprint 12 m x 6 m." The accessible source set does not establish these values for 850-1.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-039-02-001 | DBM Electrical Buildings paragraph lists multiple equipment types that "may" be housed in an electrical building, but the specific internal lineup for 850-1 (count and rating of MCC, UPS, distribution transformers, panelboards, and PLC/network racks) is not stated in any accessible source slice. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings paragraph | Workbook Packages row 41; `PACKAGE_REGISTER.csv` row `PKG-039` | Datasheet Attributes/Construction; Specification Requirements; Procedure Steps | Treat the DBM list as anticipated population only and keep the 850-1 specific lineup `TBD` until vendor package data or detailed electrical engineering is accepted. | TBD |
| HRR-039-02-002 | The package-specific Word requirements source (`26020-Package_Requirements.docx`) was searched but did not return a confirmed PKG-039 / building-850-1 match during this run, so no package-specific requirements supersede the DBM general electrical-building basis. | `_Sources/26020-Package_Requirements.docx` | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` | Datasheet Attributes/Construction; Specification Requirements | Vendor-facing datasheet content should remain conservative until a package-specific source slice is identified or vendor data resolves the gaps. | TBD |
