# Specification: DEL-061-03 — Construction Work Package (NGL Booster and Transfer Pumps Building)

## Scope

This specification governs the EPC Integrator Construction Work Package (CWP) for PKG-061 (NGL Booster and Transfer Pumps Building). It defines what the CWP must contain to direct physical installation, construction inspection, mechanical completion, turnover, and integration tie-in for the LPG booster pump package P-9570-1 / P-9580-1 (two parallel vertical multistage can-type pumps, API 610, 575 V / 3 ph / 60 Hz) supplied as a vendor module with package piping, instrumentation, electrical, HVAC/enclosure, and CRN/TSBC certification as applicable. (Source: SCOPE_LEDGER.csv SOW-0149/0150/0151/0152.)

The package vendor delivers the engineered equipment package (DEL-061-04). The EPC Integrator is responsible for facility-level integration: site preparation, foundations, electrical supply to MCC, DCS integration, tie-ins, and turnover (SCOPE_LEDGER.csv SOW-0152; PACKAGE_REGISTER.csv row for PKG-061).

**Excluded from this deliverable:** Vendor package design, fabrication, and factory acceptance (covered by DEL-061-04); vendor document turnover (DEL-061-05); EPC vendor review/acceptance (DEL-061-06). No package-specific construction exclusions are stated in source materials; package-level exclusions remain TBD per PACKAGE_REGISTER.csv row for PKG-061.

## Requirements

| ID | Requirement | Source |
|---|---|---|
| R1 | The CWP shall identify the package by ID (PKG-061), name (NGL Booster and Transfer Pumps Building), and equipment tags P-9570-1 / P-9580-1. | DBM-Deepcut/4-25_Deepcut_DBM.md row 2609 |
| R2 | The CWP shall cover SOW-0149, SOW-0150, SOW-0151, and SOW-0152 as the construction-relevant scope items. | DELIVERABLE_REGISTER.csv row for DEL-061-03 |
| R3 | The CWP shall include the construction work package, the installation and tie-in workface plan, and the construction interface and turnover checklist as anticipated artifacts. | DELIVERABLE_REGISTER.csv row for DEL-061-03; `_CONTEXT.md` |
| R4 | The CWP shall address each applicable physical interface listed in the package register for PKG-061: Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports. | PACKAGE_REGISTER.csv row for PKG-061 |
| R5 | The CWP shall identify foundations, electrical supply to MCC, and DCS integration as EPC-side scope (vendor-out) and ensure the workface plan reflects these as integration responsibilities. | SCOPE_LEDGER.csv SOW-0152 |
| R6 | The CWP shall preserve API 610 receipt-condition requirements for the LPG booster pump skids, including seal plan 13/52 verification at FAT and prior to commissioning. | SCOPE_LEDGER.csv SOW-0151; ASSUMPTION: API 610 receipt and seal plan verification protocols apply consistent with API 610 practice; clause-level confirmation TBD pending extraction of 26020-Package_Requirements.docx heading 17 |
| R7 | The CWP shall coordinate the rigging, lift, set, and grout sequence consistent with the "950-1 LPG Booster and Transfer Pump Module" shop-assembled module envelope. | DBM-Deepcut/4-25_Deepcut_DBM.md row 2818 |
| R8 | The CWP shall require commissioning support from the package vendor as part of construction completion. | SCOPE_LEDGER.csv SOW-0151 |
| R9 | The CWP shall ensure CRN/TSBC certification (as applicable) is documented and field-verified prior to mechanical completion. | SCOPE_LEDGER.csv SOW-0151 |
| R10 | The CWP shall record per-pump operating basis (145 m3/h at 150% capacity; booster differential 25 psid / 172 kPad) so installed system tie-in conditions can be verified against design intent. | SCOPE_LEDGER.csv SOW-0152 |
| R11 | The CWP shall flag TDH and any sour/LPG materials requirements as TBD inputs to be resolved by DEL-061-02 (Package Datasheet) and the vendor package (DEL-061-04) prior to construction execution. | SCOPE_LEDGER.csv SOW-0152 (TBD TDH); materials specification not located in accessible PKG-061 source slices |
| R12 | The CWP shall align downstream tie-in to the LACT unit boundary with the package datasheet (DEL-061-02). | SCOPE_LEDGER.csv SOW-0150 |

## Standards

| Standard / Code | Applicability | Source |
|---|---|---|
| API 610 (centrifugal pumps for petroleum industries) | Pump design/receipt basis for P-9570-1/P-9580-1 | SCOPE_LEDGER.csv SOW-0151 (clause-level text `location TBD`) |
| API 610 seal plan 13/52 | Mechanical seal arrangement for the LPG booster pumps | SCOPE_LEDGER.csv SOW-0151 |
| CRN / TSBC | Pressure equipment registration (where applicable) for the package | SCOPE_LEDGER.csv SOW-0151 |
| Hazardous area / electrical classification standard | Applicable for LPG service; specific code/clause TBD | ASSUMPTION based on LPG service per SCOPE_LEDGER.csv SOW-0150; `location TBD` (26020-Package_Requirements.docx heading 17) |
| Project-specific construction, inspection, and turnover standards | location TBD | Workbook Packages row 75; 26020-Package_Requirements.docx package heading 17 |

## Verification

| Requirement | Verification Approach |
|---|---|
| R1, R2, R3 | Document review: confirm CWP cover sheet, scope inclusions, and anticipated artifacts. |
| R4 | Interface checklist review against PACKAGE_REGISTER.csv interface list for PKG-061. |
| R5 | Workface-plan review: verify EPC scope items (foundation, MCC supply, DCS integration) are listed with responsible parties. |
| R6, R9 | FAT report and field verification record review (seal plan, CRN/TSBC tags). |
| R7 | Lift plan / rigging study review for compatibility with vendor module envelope and weight. |
| R8 | Commissioning plan inclusion of vendor support hours and scope. |
| R10 | Tie-in test record: compare installed system performance markers to design intent (TDH TBD pending DEL-061-02). |
| R11 | Open-item register sign-off prior to construction execution. |
| R12 | Tie-in package review against DEL-061-02 LACT boundary definition. |

## Documentation

The CWP, when complete, shall include:

- A construction work package document keyed to PKG-061.
- An installation and tie-in workface plan covering each applicable interface in R4.
- A construction interface and turnover checklist that maps each interface to its acceptance criterion and turnover record.
- Cross-references to DEL-061-01 (Scope of Work), DEL-061-02 (Package Datasheet), DEL-061-04 (Vendor Engineered Equipment Package), DEL-061-05 (Vendor Document Turnover Package), and DEL-061-06 (EPC Vendor Package Review and Acceptance).
- Identification of TBD inputs (TDH; materials specification; hazardous area classification clause-level text; field environment values) with their resolution path.

(Source: DELIVERABLE_REGISTER.csv anticipated artifacts for DEL-061-03; PACKAGE_REGISTER.csv PKG-061; sibling deliverable registrations.)
