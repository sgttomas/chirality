# Specification: DEL-054-04 Vendor Engineered Equipment Package

## Scope

This specification governs the Package Vendor production unit for the High-Pressure Flare Knock-Out Drum package (PKG-054, facility 04-25 Deepcut). It covers vendor engineering, design, fabrication/supply, and the physical equipment package developed from the EPC package Scope of Work (DEL-054-01) and EPC Package Datasheet (DEL-054-02). [Source: `_CONTEXT.md` Scope]

In-scope:
- Vendor engineered physical equipment package centered on H.P. FLARE K.O. DRUM (V-4100-1) and HP FLARE K.O. DRUM TRANSFER PUMP (P-4100-1). [Source: `4-25_Deepcut_DBM.md` lines 2028, 2360, 2534]
- Vendor package design basis and datasheet set. [Source: `_CONTEXT.md` Anticipated Artifacts]
- Vendor engineering, design, and fabrication/supply activities required to deliver the equipment package complete. [Source: `_CONTEXT.md` Scope]

Out-of-scope (carried by other DEL-054-* deliverables):
- EPC Scope of Work content (DEL-054-01). [Source: `DELIVERABLE_REGISTER.csv`]
- EPC Package Datasheet content (DEL-054-02). [Source: `DELIVERABLE_REGISTER.csv`]
- Construction Work Package (DEL-054-03). [Source: `DELIVERABLE_REGISTER.csv`]
- Vendor Document Turnover Package (DEL-054-05). [Source: `DELIVERABLE_REGISTER.csv`]
- EPC Vendor Package Review and Acceptance (DEL-054-06). [Source: `DELIVERABLE_REGISTER.csv`]

## Requirements

| ID | Requirement | Type | Source |
|---|---|---|---|
| REQ-054-04-01 | The vendor shall engineer and design the package using the EPC Scope of Work (DEL-054-01) and EPC Package Datasheet (DEL-054-02) as the controlling input set. | Input control | `_CONTEXT.md` Scope; `DELIVERABLE_REGISTER.csv` |
| REQ-054-04-02 | The vendor-engineered package shall deliver the H.P. FLARE K.O. DRUM (V-4100-1) and HP FLARE K.O. DRUM TRANSFER PUMP (P-4100-1) as the anchoring tags of the production unit. | Equipment scope | `4-25_Deepcut_DBM.md` lines 2028, 2360, 2534 |
| REQ-054-04-03 | The HP flare KO drum and associated header shall accept the 508 mm (20 in) HP flare relief header and shall combine with the cryogenic flare downstream of both KO drums before the common HP/cryo stack. | Process interface | `4-25_Deepcut_DBM.md` line 2028 |
| REQ-054-04-04 | The package shall include a truck-out provision served by P-4100-1. | Liquids handling | `4-25_Deepcut_DBM.md` line 2028 |
| REQ-054-04-05 | HP flare headers outside heated buildings shall be electrically heat traced and insulated for freeze protection, except PSV outlets that free-drain into the flare header. | Freeze protection | `4-25_Deepcut_DBM.md` line 2033 |
| REQ-054-04-06 | Layout submittals shall respect minimum spacing between flare tanks (including KO drums) and vegetation or other fire hazards of 10 m (32 ft). | Spacing | `4-25_Deepcut_DBM.md` line 287 (OGAOM Sec. 9.6.15) |
| REQ-054-04-07 | The vendor shall produce a vendor package design basis and a datasheet set as deliverables of the production unit. | Documentation output | `_CONTEXT.md` Anticipated Artifacts |
| REQ-054-04-08 | The completed vendor-engineered equipment package shall be presented to the EPC Integrator for integration review. | Integration | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| REQ-054-04-09 | Final relief volume basis, header backpressure, and shared 03-25/04-25 allocation shall be confirmed during detailed engineering. | Open-item closure | `4-25_Deepcut_DBM.md` lines 1834, 2021 |
| REQ-054-04-10 | ASSUMPTION - Vendor pressure-containing components for HP flare service should be specified to be consistent with the SA-333 material reference used for HP flare stack/header. Confirm during detailed engineering. | Materials | `4-25_Deepcut_DBM.md` line 2039 (ASSUMPTION - extends stack/header MOC to package per package consistency) |

## Standards

| Standard | Applicability | Source |
|---|---|---|
| OGAOM Sec. 9.6.15 | Flare and incinerator spacing including KO drum proximity to vegetation/fire hazards | `4-25_Deepcut_DBM.md` line 287 |
| OGPFR Appendix 1, Schedule 1, Sec. 2 | Allowable thermal radiation flux at flare boundaries (DBM notes verification against governing regulation during detailed design) | `4-25_Deepcut_DBM.md` lines 285-286, 289 |
| API 2510 | Spacing reference (flare-to-pressurized-bullets context within the broader flare/spacing basis) | `4-25_Deepcut_DBM.md` line 284 |
| Vessel design code (e.g., ASME BPVC Sec. VIII) | Pressure vessel design of the HP KO drum | TBD - location TBD; not stated at clause level in the available Gate 7 snapshot or DBM excerpts |
| Pump design code (e.g., API 610 / API 685) | HP KO drum transfer pump design | TBD - location TBD; not stated at clause level in the available Gate 7 snapshot or DBM excerpts |
| 26020-Package_Requirements.docx package heading 9 | Package-level requirements per workbook | ASSUMPTION - referenced in `_CONTEXT.md` and `_REFERENCES.md`; document not locally text-extracted, clause-level requirements TBD |

## Verification

| Requirement | Verification Approach | Source |
|---|---|---|
| REQ-054-04-01 | Document review confirms DEL-054-01 and DEL-054-02 cited as controlling inputs in vendor design basis. | `DELIVERABLE_REGISTER.csv` |
| REQ-054-04-02 | Equipment list and tag register cross-check against V-4100-1 and P-4100-1 in vendor datasheets. | `4-25_Deepcut_DBM.md` line 2534 |
| REQ-054-04-03 | P&ID review and dimensional check of relief header tie-in size and downstream merge point. | `4-25_Deepcut_DBM.md` line 2028 |
| REQ-054-04-04 | Vendor design basis includes truck-out provision via P-4100-1; visible in equipment GA and P&ID. | `4-25_Deepcut_DBM.md` line 2028 |
| REQ-054-04-05 | Heat-tracing and insulation drawings demonstrate compliance for outside, non-heated-building portions. | `4-25_Deepcut_DBM.md` line 2033 |
| REQ-054-04-06 | Layout drawing dimensional check against site plot plan. | `4-25_Deepcut_DBM.md` line 287 |
| REQ-054-04-07 | Vendor design basis document and datasheet set delivered, registered in DEL-054-05 turnover. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| REQ-054-04-08 | EPC Integrator review log entry per DEL-054-06. | `DELIVERABLE_REGISTER.csv` row `DEL-054-06_epc-vendor-package-review-and-acceptance` |
| REQ-054-04-09 | Closure evidence captured in detailed engineering memos / flare stack vendor confirmation. | `4-25_Deepcut_DBM.md` line 2021 |
| REQ-054-04-10 | Material test reports (MTRs) and vendor material spec consistency check. | TBD pending DEL-054-02 |

## Documentation

The deliverable shall produce, at minimum, the following artifacts. Specific document numbering follows the vendor document register issued under DEL-054-05.

- Vendor engineered physical equipment package (the equipment itself, identified per V-4100-1 / P-4100-1). [Source: `_CONTEXT.md` Anticipated Artifacts]
- Vendor package design basis. [Source: `_CONTEXT.md` Anticipated Artifacts]
- Vendor datasheet set (vessel, pump, ancillary instruments/components). [Source: `_CONTEXT.md` Anticipated Artifacts]
- Drawings (equipment GA, P&ID extensions, layout) - TBD specific list pending DEL-054-02 issue. [ASSUMPTION based on standard vendor package production unit content]
- Inspection, test, and turnover records flowing to DEL-054-05 / DEL-054-06. [`DELIVERABLE_REGISTER.csv` rows `DEL-054-05`, `DEL-054-06`]
