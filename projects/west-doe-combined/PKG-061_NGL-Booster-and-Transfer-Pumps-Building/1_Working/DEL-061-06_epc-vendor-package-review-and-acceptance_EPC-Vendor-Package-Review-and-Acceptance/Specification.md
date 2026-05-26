# Specification — DEL-061-06 EPC Vendor Package Review and Acceptance

## Scope

### In scope
This deliverable specifies the EPC Integrator's review-and-acceptance work product for the NGL Booster and Transfer Pumps Building package (`PKG-061`). It defines the evidence the EPC Integrator must produce to demonstrate that the Package Vendor's `DEL-061-04` Vendor Engineered Equipment Package and `DEL-061-05` Vendor Document Turnover Package satisfy the EPC Scope of Work (`DEL-061-01`), Package Datasheet (`DEL-061-02`), and Construction Work Package (`DEL-061-03`).

Sources: `26020-Package_Requirements.docx` Heading 17 (location TBD — source slice not locally accessible in markdown during this run); `DELIVERABLE_REGISTER.csv` row `DEL-061-06`.

### Out of scope
- Authoring or modifying the vendor-side engineering deliverables themselves; those are `DEL-061-04` / `DEL-061-05` outputs.
- Other facility pump packages or NGL transfer scope outside `PKG-061` (e.g., separate compressor or process packages).
- Building/civil works not bundled into this package's scope (location TBD until Heading 17 is locally accessible).

## Requirements

| Req ID | Requirement | Source / Basis |
|---|---|---|
| `R-061-06-01` | The acceptance evidence MUST cover all SOW items mapped to this deliverable: `SOW-0149`, `SOW-0150`, `SOW-0151`, `SOW-0152`. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| `R-061-06-02` | The vendor document review log MUST enumerate every "Vendor Engineering Deliverable" listed for the NGL Booster and Transfer Pumps Building scope in Heading 17 and record disposition (accepted / rejected / open). Specific document list TBD until Heading 17 is locally accessible. | `26020-Package_Requirements.docx` Heading 17 "Vendor Engineering Deliverables" (location TBD) |
| `R-061-06-03` | The package acceptance checklist MUST verify scope inclusions enumerated in Heading 17 "Basic Scope" / "Major Included Equipment" for the NGL booster and transfer pumps and their housing building. Specific scope items TBD until Heading 17 is locally accessible. | `26020-Package_Requirements.docx` Heading 17 "Basic Scope" / "Major Included Equipment" (location TBD) |
| `R-061-06-04` | The acceptance evidence MUST confirm that all "Scope Notes / Open Items" stated in Heading 17 are addressed (closed or carried with disposition). Specific notes TBD until source slice is locally accessible. | `26020-Package_Requirements.docx` Heading 17 "Scope Notes / Open Items" (location TBD) |
| `R-061-06-05` | The acceptance evidence MUST cover each physical interface marked `Yes` in the Heading 17 Physical Interface Summary, cross-referenced with the package row in `26020-Packages_Interfaces_4_export.xlsx` (row 75). Specific interface set TBD until Heading 17 and the interface workbook columns are locally resolved. | `26020-Package_Requirements.docx` Heading 17 "Physical Interface Summary" (location TBD); `26020-Packages_Interfaces_4_export.xlsx` row 75 |
| `R-061-06-06` | Rotating-equipment acceptance MUST include pump data sheets (`MEC-007`), NPSH calcs (`PRO-013`), mechanical seal / lube oil specification (`MEC-019`), motor starting study (`ELE-011`), and Equipment FAT / Performance Test Report (`MEC-022`) for each booster and transfer pump in the package. | ASSUMPTION — typical rotating-equipment acceptance set; final code list TBD until Heading 17 "Vendor Engineering Deliverables" — Rotating equipment / pumps is locally accessible |
| `R-061-06-07` | Building / enclosure acceptance MUST include applicable architectural, structural, HVAC, electrical, and fire/gas detection submittals for the pumps building. Specific artifact codes and applicability TBD until Heading 17 is locally accessible. (ASSUMPTION — building-scope artifacts are implied by package name.) | `26020-Package_Requirements.docx` Heading 17 (location TBD); ASSUMPTION |
| `R-061-06-08` | Area-classification and electrical acceptance MUST cover the hazardous-area zoning of the pumps building, motor specifications, EHT (if any), grounding/bonding, lighting, and I&C cabling for the package. Specific artifact codes TBD until Heading 17 is locally accessible. | `26020-Package_Requirements.docx` Heading 17 "Vendor Engineering Deliverables" — Electrical block (location TBD); ASSUMPTION |
| `R-061-06-09` | Quality records MUST be assembled: Supplier Quality Plan (`QLT-006`), ITP execution evidence (`QLT-003`), Material Test Reports / Certificates (`QLT-013`), Inspection Release Certificate (`QLT-020`), and Manufacturing Record Book / Vendor Data Book (`QLT-021` / `MEC-023` / `PRQ-016`). | ASSUMPTION — standard EPC quality-records bundle; final list TBD until source slice is accessible |
| `R-061-06-10` | Turnover MUST include the SPIR (`PRQ-015`), Logistics / Shipping Plan (`PRQ-013`), and Mechanical Equipment IOM Manual (`MEC-025`). | ASSUMPTION — standard EPC turnover bundle; final list TBD until source slice is accessible |
| `R-061-06-11` | Numeric design/operating values used in acceptance (pump head, flow, NPSHr, power, design pressure/temperature, building HVAC and area-classification parameters) MUST be traceable to specific Package Vendor submittals. Specific values are TBD until those vendor submittals are accepted; the acceptance pack MUST NOT assert numeric values not present in vendor docs or in Heading 17 source slice. | `26020-Package_Requirements.docx` Heading 17 (location TBD); ASSUMPTION |
| `R-061-06-12` | Open items called out in the Heading 17 source slice MUST be closed or carried with explicit disposition in the acceptance record. | `26020-Package_Requirements.docx` Heading 17 "Scope Notes / Open Items" (location TBD) |

## Standards

| Standard / Code | Applicability | Location |
|---|---|---|
| API STD 610 (Centrifugal pumps for petroleum, petrochemical and natural gas industries) | Likely governing for NGL booster / transfer pump mechanical design and FAT. | location TBD — not yet confirmed against `26020-Package_Requirements.docx` Heading 17; ASSUMPTION based on service type |
| Provincial / national hazardous-area electrical code (CEC / NEC Article 500 series as applicable to the project jurisdiction) | Governs area classification, motor selection, building lighting and instrumentation in a hazardous area. | location TBD — not stated in source slice during this run; ASSUMPTION |
| National Building Code / structural code applicable to the project jurisdiction | Governs pumps-building enclosure structural and life-safety design. | location TBD — not stated in source slice; ASSUMPTION |
| Fire / gas detection standard applicable to the project jurisdiction | Governs F&G coverage for an indoor NGL pump enclosure. | location TBD — not stated in source slice; ASSUMPTION |

## Verification

| Req ID | Verification Approach |
|---|---|
| `R-061-06-01` | Traceability matrix mapping each SOW item to acceptance-checklist rows and to evidence artifacts. |
| `R-061-06-02` | Document-by-document review log inspection; every Heading 17 vendor deliverable has a tracked disposition. |
| `R-061-06-03` | Walk-down and as-built/IFC drawing review against the Heading 17 Basic Scope and Major Included Equipment list. |
| `R-061-06-04` | Open-items log inspection; each Heading 17 "Scope Notes / Open Items" entry mapped to closure or carry-forward record. |
| `R-061-06-05` | Interface-by-interface checklist against the Heading 17 Physical Interface Summary and `26020-Packages_Interfaces_4_export.xlsx` row 75. |
| `R-061-06-06` | FAT witness records (`MEC-022`); NPSH calc review (`PRO-013`); motor starting study (`ELE-011`) accepted; data sheets (`MEC-007`) reconciled against `DEL-061-02`. |
| `R-061-06-07` | Building submittal review (architectural / structural / HVAC) reconciled with `DEL-061-02` and `DEL-061-03`. |
| `R-061-06-08` | Area-classification drawings, motor data sheets, EHT and grounding packages reviewed and energization records confirmed. |
| `R-061-06-09` | Quality records audit; Inspection Release Certificate (`QLT-020`) issued; MRB (`QLT-021`) compiled and accepted. |
| `R-061-06-10` | Receipt inspection records; SPIR provided and accepted; IOM in turnover bundle. |
| `R-061-06-11` | Reconciliation table between EPC Package Datasheet (`DEL-061-02`) values and vendor-submitted values; TBD entries flagged. |
| `R-061-06-12` | Open-items log carried into commissioning; explicit closure or carryover noted. |

## Documentation

Acceptance deliverable artifacts (per `_CONTEXT.md`):

- Vendor document review log.
- Package acceptance checklist (SOW-, interface-, and artifact-indexed).
- Test / inspection evidence bundle (FAT, ITP execution, MTRs, IRC).
- Turnover evidence bundle (MRB / VDB, hydrotest packages where applicable, SPIR, IOM, building-handover records).
- Open-items disposition log.

Standards-related and numeric design values that depend on vendor submittals or on the Heading 17 source slice carry `TBD` placeholders until those become locally accessible / accepted.
