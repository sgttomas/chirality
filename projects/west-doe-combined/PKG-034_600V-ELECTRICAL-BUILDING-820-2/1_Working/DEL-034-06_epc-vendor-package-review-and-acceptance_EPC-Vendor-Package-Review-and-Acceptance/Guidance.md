# Guidance: DEL-034-06_epc-vendor-package-review-and-acceptance

## Purpose

The EPC Vendor Package Review and Acceptance deliverable converts the Gate 7 package basis for `PKG-034` into auditable EPC-integrator review and acceptance evidence for the 600V ELECTRICAL BUILDING (820-2) vendor package. It documents how the EPC Integrator reviewed the vendor documentation, accepted the vendor package against the EPC Scope of Work, Package Datasheet, and Construction Work Package, and confirmed handoff readiness for construction integration.

## Principles

- Preserve source spelling and identity. The package name is carried as "600V ELECTRICAL BUILDING (820-2)" because that is the workbook and Gate 7 register spelling.
- Treat vendor-owned package engineering, design, and documentation as inputs to be reviewed, not as items the EPC Integrator authors.
- Keep EPC-owned facility integration and interfaces distinct from vendor-owned package design.
- Anchor acceptance to upstream EPC deliverables (`DEL-034-01`, `DEL-034-02`, `DEL-034-03`); do not certify against ad-hoc criteria.
- Use `TBD` for building-specific equipment counts, MCC/switchgear lineups, transformer ratings, generator sizing, transfer-switch configuration, and "820-2" physical location until source-supported values exist.
- Treat the workbook interface `X` facts as evidence to be checked against the vendor package, not as separate deliverables.

## Considerations

The DBM Comp and Liquids source supports a 600 V, 3 phase, 3 wire, 60 Hz HRG low-voltage service used for motors 3/4 hp through 250 hp, lighting transformers, building heaters, and UPS larger than 10 kVA. Electrical buildings shall house MCCs, switchgear, distribution equipment, and associated HVAC/ventilation systems. Standby power is supplied at the 600V MCC level via LV standby natural-gas generators with transfer switch; generator sizing, transfer-switch type, emergency bus configuration, and load-shedding/critical-load list remain `TBD` at the DBM level. Acceptance review should confirm vendor alignment to these bases but should not introduce values not present in the source set.

The DBM Deepcut electrical-buildings inventory lists 600V buildings as "840-1 600V Acid Gas Compressor Electrical Building," "850-1 600V Inlet / Sales Compressor Electrical Building," and "860-1 600V General Area / Tank Farm Electrical Building." The workbook label for this package is "600V ELECTRICAL BUILDING (820-2)." No accessible source slice maps "820-2" to any of these DBM-listed buildings. The reconciliation is recorded as an open item and as a human-ruling row in the Conflict Table.

Foundations, area classification, building HVAC, fire & gas, grounding/bonding, cable tray and conduit routing, communications/network, and maintenance access are all live interface facts on `PKG-034`. Acceptance review should confirm that vendor design addresses each interface against the DBM basis without claiming clause-level conformance the source set does not establish.

Standby power and emergency generator details are particularly source-thin; the DBM explicitly leaves transfer switch type, emergency bus configuration, generator count, rating, and load-shedding/critical-load list as `TBD`. The acceptance deliverable must preserve those gaps rather than close them on vendor narrative alone.

The package-specific Word requirements source (`26020-Package_Requirements.docx`) did not produce a confirmed `PKG-034` match during this run; package-specific acceptance criteria from that source remain unresolved.

## Trade-offs

| Topic | Conservative position | Reason |
|---|---|---|
| Acceptance language | Frame as "EPC review and integration acceptance," not as certification or fitness-for-purpose endorsement. | Acceptance is an integrator activity; certification rests outside this deliverable. |
| "820-2" building mapping | Treat "820-2" as the workbook-given identity; do not map it to 840-1, 850-1, or 860-1 without source. | DBM building inventory does not contain "820-2." A silent mapping would invent decomposition truth. |
| Generator/standby details | Carry generator sizing, transfer-switch type, emergency-bus configuration, and load-shedding list as `TBD`. | DBM explicitly leaves these `TBD`. |
| Factory/shop test acceptance | Accept only what test/inspection evidence supports; mark gaps `TBD`. | Detailed package-specific test specifications were not found in accessible sources. |
| Vendor documentation completeness | Use the vendor document register from `DEL-034-05` as the checklist baseline. | `DEL-034-05` registers carry a "TBD vendor document register" artifact (`ART-D602A4F8C4`), and acceptance review should reflect that gap. |
| Standards | List CEC, area classification, and project electrical specifications with locations TBD. | DBM references these but specification documents are not locally accessible. |

## Examples

- Acceptable acceptance entry: "Electrical interface review confirms vendor package 600V service basis is consistent with DBM low-voltage service basis (`_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, low-voltage service row). Source: vendor electrical interface drawing under review."
- Acceptable source-gap entry: "Building '820-2' physical location: TBD. The DBM Deepcut building inventory enumerates 840-1, 850-1, and 860-1; no accessible source slice maps '820-2' to any of these. Recorded as `HRR-034-06-001`."
- Acceptable acceptance entry for standby power: "Standby power interface accepted at the 600V MCC level; generator sizing, transfer switch type, and load-shedding list remain `TBD` pending detailed engineering."
- Not acceptable without new source: "Building 820-2 is the inlet/sales 600V building (formerly 850-1)." The accessible source set does not establish this mapping.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-034-06-001 | Workbook names the package "600V ELECTRICAL BUILDING (820-2)" but the DBM Deepcut building inventory enumerates 600V buildings as 840-1, 850-1, and 860-1 with no "820-2" entry. | Workbook Packages row 36; `PACKAGE_REGISTER.csv` row `PKG-034` | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings inventory table | Datasheet Identification/Attributes; Specification Requirements; Procedure Steps | Carry "820-2" as workbook identity only; do not map to a DBM-listed 600V building until source confirms. | TBD |
| HRR-034-06-002 | Standby power generator sizing, transfer switch type, emergency bus configuration, and load-shedding/critical-load list are explicitly `TBD` in DBM, but vendor acceptance may pressure resolution. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, standby power paragraph | Vendor acceptance checklist scope (`ART-8E586DD59F`) | Specification REQ-034-06-008; Datasheet Attributes (standby power interface) | Preserve `TBD` until the EPC Package Datasheet, EPC Scope of Work, or detailed engineering closes the gap; do not accept vendor narrative as final basis. | TBD |
| HRR-034-06-003 | The Vendor Document Turnover Package register (`DEL-034-05`) currently carries a "TBD vendor document register" artifact (`ART-D602A4F8C4`); acceptance against an undefined vendor document baseline is at risk. | `DELIVERABLE_REGISTER.csv` row `DEL-034-05`; `ARTIFACT_REGISTER.csv` `ART-D602A4F8C4` | `ARTIFACT_REGISTER.csv` `ART-F631454830` (vendor document review and comment log) | Specification REQ-034-06-003; Procedure Steps; Verification (vendor input completeness) | Treat the vendor document register as required input; defer review-log closure for any document category that is undefined in the register. | TBD |
