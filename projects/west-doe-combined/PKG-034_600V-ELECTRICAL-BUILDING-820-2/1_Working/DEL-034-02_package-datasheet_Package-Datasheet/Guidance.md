# Guidance: DEL-034-02_package-datasheet

## Purpose

The Package Datasheet exists to convert the accepted Gate 7 package basis for `PKG-034` into a source-supported technical handoff document. It should let the Package Vendor understand the EPC integration basis for the 600V ELECTRICAL BUILDING (820-2) while keeping EPC-owned facility interfaces distinct from vendor-owned package design.

## Principles

- Preserve source spelling and identity. The package name is carried as "600V ELECTRICAL BUILDING (820-2)" because that is the workbook and Gate 7 register spelling.
- Treat workbook interface `X` facts as evidence under the Package Datasheet, not as separate deliverables; all twelve PKG-034 interfaces are in scope.
- Keep vendor-owned package design and equipment selection with the Package Vendor, and facility-level integration with the EPC Integrator.
- Use the DBM electrical-building basis only at the level it supports: prefabricated modular construction, general-purpose-area siting, n+1 HVAC, bottom cable entry, pile-elevated foundations, internal wiring conventions (TECK/ACIC, EMT), and possible housed equipment classes (600 V MCC, distribution transformers, 208/120 V panels, UPS systems, PLC panels, network racks).
- Use `TBD` for the PKG-034 internal equipment list, ratings, quantities, single-line, transformer feeder source, plot location, area classification, and HVAC unit sizing until a source-supported package-specific basis is available.

## Considerations

The DBM identifies several named 600 V electrical buildings (e.g., 840-1, 850-1, 860-1) but does not separately enumerate an "820-2" instance. The workbook is the authority for package identity and assigns tag 820-2 to PKG-034. Datasheet content should describe the building class per DBM and avoid inferring detailed scope by analogy to a different specific building.

The Comp_and_Liquids DBM establishes that emergency power is supplied at the 600 V MCC level via low-voltage standby natural-gas generators with transfer switch, replacing the prior 13.8 kV / 3 MW emergency generator concept. Transfer-switch type, emergency bus configuration, generator count and rating, and the critical-load/load-shedding list remain TBD and are appropriate to flag as vendor-coordination and detailed-electrical-study items.

Grounding and bonding are applicable interface topics. The DBM source contains facility grounding basis including two-point grounding for major equipment, ground wells at electrical buildings, and above-grade conductor practice. The datasheet should require coordination with this basis while avoiding unsupported package-specific conductor sizing.

Maintenance access and building HVAC are both explicit workbook interface facts and DBM constraints. The datasheet should require routing and door sizing to preserve maintenance access and require HVAC sized n+1, while leaving unit sizing and equipment-specific clearance numbers to detailed design.

## Trade-offs

| Topic | Conservative position | Reason |
|---|---|---|
| 820-2 building scope | Treat as workbook-assigned identity; do not import scope from 840-1/850-1/860-1. | Accessible DBM source slices do not enumerate an 820-2 building; workbook is the authority for identity but not for internal equipment list. |
| Internal equipment list | Describe as "may include" per DBM building class; mark specific inclusion/quantity as `TBD`. | DBM lists possible housed equipment classes; PKG-034 specific inclusion is not confirmed in accessible sources. |
| Incoming feeder source | Describe facility radial-distribution basis; mark transformer rating and source bus for PKG-034 as `TBD`. | DBM describes distribution through step-down transformers from 13.8 kV but does not assign a specific feeder to the 820-2 building. |
| Standby power | Identify 600 V MCC-level LV gen + transfer switch; mark sizing/configuration as `TBD`. | Comp_and_Liquids DBM explicitly leaves transfer-switch type, generator count/rating, and load-shedding list as TBD. |
| Standards | List CEC, area classification, and project electrical specifications as governing bases with locations `TBD`. | DBM references these bases but detailed clauses/specification documents are not in the deliverable folder. |

## Examples

- Acceptable datasheet entry: "Applicable interfaces (12): Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports. Source: Workbook Packages row 36 and `INTERFACE_REGISTER.csv`."
- Acceptable source-gap entry: "PKG-034 internal equipment list and ratings: TBD. DBM lists possible housed equipment classes but no PKG-034-specific equipment schedule is available."
- Not acceptable without new source: "PKG-034 houses two 600 V MCCs, one 600/208-120 V transformer rated X kVA, and one 125 V DC UPS at Y A." The accessible source set does not establish these values.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-034-02-001 | Workbook assigns building tag "820-2" to PKG-034, but accessible DBM source slices enumerate 810-1, 820-1, 830-1, 840-1, 850-1, and 860-1 only; no "820-2" appears. | Workbook Packages row 36; `PACKAGE_REGISTER.csv` row `PKG-034` | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical-building enumeration | Datasheet Identification/Attributes; Specification Requirements (REQ-034-02-011); Procedure Steps | Treat "820-2" as workbook-assigned identity only; describe the building class per DBM and do not import scope by analogy. | TBD |
| HRR-034-02-002 | PKG-034 internal equipment list, ratings, quantities, transformer feeder source, plot location, and area classification are not established by accessible sources. | Workbook Packages row 36; Gate 7 `PACKAGE_REGISTER.csv` | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, 600V MCC and Standby Power | Datasheet Attributes/Construction; Specification Requirements (REQ-034-02-010); Procedure Steps | Hold internal equipment scope and location-specific values as `TBD` until vendor data or a 820-2-specific design source is accepted. | TBD |
