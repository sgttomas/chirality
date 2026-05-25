# Guidance: DEL-038-02_package-datasheet

## Purpose

The Package Datasheet exists to convert the accepted Gate 7 package basis for `PKG-038` into a source-supported technical handoff document. It should let the Package Vendor understand the EPC integration basis for the 600V ELECTRICAL BUILDING (820-1) package while keeping EPC-owned facility interfaces distinct from vendor-owned package design.

## Principles

- Preserve source spelling and identity. The package name is carried as "600V ELECTRICAL BUILDING (820-1)" because that is the workbook and Gate 7 register spelling.
- Treat workbook interface `X` facts as evidence under the Package Datasheet, not as separate deliverables.
- Keep vendor-owned design work with the Package Vendor and facility-level integration with the EPC Integrator.
- Use `TBD` for package-specific equipment counts, ratings, layout dimensions, UPS battery autonomy, HVAC unit sizing, and detailed MCC line-up content until source-supported package-specific data is available.
- Use the DBM electrical basis at the level it actually supports: low-voltage service basis, 600 V MCC and SCR control basis, the Electrical Buildings paragraph (construction, HVAC, cable entry, internal wiring), grounding and bonding rules, cable tray / conduit routing rules, and building-heater rating.

## Considerations

The DBM Electrical Buildings paragraph states that electrical buildings are prefabricated, modular buildings located in general purpose areas, climate controlled with HVAC sized as an n + 1 system, elevated on piles with bottom cable entry, and internally wired with TECK and ACIC cable with EMT conduit between adjacent equipment. These are facility-wide rules that bind any electrical building package; they should be carried into the datasheet as requirements rather than as design proposals.

The DBM low-voltage service basis (600 V, 3-phase 3-wire 60 Hz, high-resistance grounded with 5 A continuous resistor) and the 600 V MCC basis (traditional MCCs with electronic overload relays; 600 V VFDs supplied within the MCC lineup; 600 V SCR heater-control panels supplied by feeder breakers in the 600 V MCC) anchor the electrical performance of the package and should be reflected in the datasheet's attributes and the specification's requirements.

The DBM Grounding and Bonding section supports specific package-relevant requirements: 600 V transformer grounding via 5 A continuous high-resistance resistor; 600 V MCCs with power metering and ground/resistor fault detection; alarm-only ground-fault protection on 600 V systems; two-point ground connections for major electrical equipment; and ground wells at electrical buildings. Detailed conductor sizing should follow CEC and detailed design rather than being asserted in this datasheet.

Cable tray and conduit must not interfere with maintenance access, which is also one of the workbook interface facts for this package. The datasheet should require electrical routing and physical placement to preserve maintenance access while leaving specific clearances to detailed design.

The package-specific Word requirements source (`26020-Package_Requirements.docx`) was referenced in `_REFERENCES.md` but no PKG-038 source slice was extracted in this run, so package-specific quantities, ratings, and layout values remain `TBD`.

## Trade-offs

| Topic | Conservative position | Reason |
|---|---|---|
| Equipment count / ratings | Mark `TBD` pending PKG-038-specific source confirmation. | Workbook and DBM identify equipment classes (MCC, UPS, transformers, panels), not PKG-038 quantities or ratings. |
| Building 820-1 identity | Carry workbook name verbatim and flag the conflict for ruling. | DBM lists building 820-1 as a 6.9 kV building; workbook names PKG-038 as a 600 V building at 820-1. |
| HVAC sizing | Require n + 1 redundancy at the architectural level; mark unit count and capacity `TBD`. | DBM establishes n + 1 basis but not absolute unit count for this building. |
| Standards | List CEC, building code, area classification, project electrical specifications, and NEMA VE2 with clause locations `TBD` where specifications are not available locally. | DBM references these bases without exposing all clause-level text. |
| UPS systems housed in building | Identify 120 V AC and 125 V DC UPS as possible housed equipment per DBM; require explicit confirmation by detailed design. | DBM says "as required by detailed design"; package-specific UPS allocation is not stated. |

## Examples

- Acceptable datasheet entry: "Applicable interfaces: Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports. Source: Workbook Packages row 40 and `INTERFACE_REGISTER.csv`."
- Acceptable source-gap entry: "Number of 600 V MCC sections, total connected load, HVAC unit capacity: TBD. No PKG-038-specific source slice available."
- Not acceptable without new source: "Building 820-1 shall house two 600 V MCCs, one 120 V AC UPS, one 125 V DC UPS, and N HVAC units of M kW each." The accessible source set does not establish these PKG-038-specific values.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-038-02-001 | Building identifier 820-1 is named "600V ELECTRICAL BUILDING (820-1)" by the workbook but is identified as "6.9 kV Inlet / Sales Compressor Electrical Building" in the DBM electrical-buildings list; DBM identifies 600 V buildings as 840-1, 850-1, and 860-1. | Workbook Packages row 40; `PACKAGE_REGISTER.csv` row `PKG-038` | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings list (lines 2811-2816) and electrical buildings paragraph | Datasheet Identification/Attributes; Specification REQ-038-02-001 and REQ-038-02-011; Procedure Steps | Carry the workbook name as the package identity (Gate 7 register authority) and surface the DBM mapping discrepancy as an open ruling; do not silently rename the package or reassign the building identifier. | TBD |
| HRR-038-02-002 | PKG-038-specific quantities, ratings, and layout values are not extracted from `26020-Package_Requirements.docx` in this run; DBM provides facility-level basis only. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings and Motor Control sections | `_Sources/26020-Package_Requirements.docx` (not processed for PKG-038 in this run) | Datasheet Attributes/Construction; Specification Requirements; Procedure Steps | Keep PKG-038-specific equipment counts, ratings, and layout as `TBD` until a PKG-038 slice of `26020-Package_Requirements.docx` is processed and accepted. | TBD |
