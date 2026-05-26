# Specification — DEL-088-04 Vendor Engineered Equipment Package

## Scope

This Specification governs the Package Vendor production unit for engineering, design, fabrication/supply, and delivery of the physical Caustic Treating (Condensate Mercaptan Removal) equipment package for PKG-088, developed from the EPC package Scope of Work (DEL-088-01) and Package Datasheet (DEL-088-02). (Source: `_CONTEXT.md`; DELIVERABLE_REGISTER row 267.)

**Included:** non-regenerable caustic treating package for C5+ condensate mercaptan removal at 20,000 BPD; caustic contactor/treating equipment, pumps, indoor caustic-area equipment, instrumentation, piping, controls, and related package systems; DSO, spent-caustic, fresh-caustic, fresh-water tanks as package scope. (Source: SOW-0056; SOW-0057; DBM-Comp_and_Liquids §Condensate Mercaptan Treating.)

**Excluded:** caustic regeneration (not included in current basis, per DBM-Comp_and_Liquids §Condensate Mercaptan Treating); facility-side integration scope owned by EPC Integrator (per SOW-0055); off-package incinerator/dilution/enrichment-gas systems beyond defined interface flanges.

## Requirements

| Req ID | Requirement | Source |
|---|---|---|
| REQ-088-04-01 | The package SHALL be a non-regenerable caustic treating package for C5+ condensate mercaptan removal. | SOW-0056 |
| REQ-088-04-02 | The package SHALL treat 20,000 BPD of C5+ condensate. | SOW-0057; DBM-Comp_and_Liquids §Condensate Mercaptan Treating |
| REQ-088-04-03 | Major equipment SHALL include caustic contactor/treating equipment, pumps, indoor caustic-area equipment, instrumentation, piping, controls, and related package systems sized for 20,000 BPD service. | SOW-0057 |
| REQ-088-04-04 | Treated product SHALL meet C1-C3 RSH below 175 ppmw S. | SOW-0058 |
| REQ-088-04-05 | Treated product SHALL meet total sulphur below 0.5 wt%. | SOW-0058 |
| REQ-088-04-06 | A possible volatile mercaptan waiver applies and SHALL be confirmed by human ruling before final design issue. | SOW-0058 |
| REQ-088-04-07 | All caustic treating equipment SHALL be located indoors (caustic building). | SOW-0058 |
| REQ-088-04-08 | Aluminum SHALL NOT be used in the caustic building. | SOW-0058; DBM-Comp_and_Liquids §Condensate Mercaptan Treating |
| REQ-088-04-09 | Package internals SHALL include a caustic C5+ contactor, pre-heater, caustic outlet filter, and water wash. | DBM-Comp_and_Liquids §Condensate Mercaptan Treating |
| REQ-088-04-10 | DSO, spent-caustic, fresh-caustic, and fresh-water tankage SHALL be supplied with the package. | DBM-Comp_and_Liquids §Condensate Mercaptan Treating |
| REQ-088-04-11 | Fresh and spent caustic tanks SHALL be atmospheric 32 oz tanks with LP fuel-gas blanket, heating, and insulation. | DBM-Comp_and_Liquids §Condensate Mercaptan Treating |
| REQ-088-04-12 | The spent caustic tank SHALL vent through a flame arrestor to the incinerator header and SHALL support truck-out. | DBM-Comp_and_Liquids §Condensate Mercaptan Treating |
| REQ-088-04-13 | Fresh caustic SHALL NOT be connected to the VRU. | DBM-Comp_and_Liquids §Condensate Mercaptan Treating |
| REQ-088-04-14 | The caustic solution basis SHALL be 50 wt% NaOH/H2O (SG 1.75 TBC by vendor). | DBM-Comp_and_Liquids §Condensate Mercaptan Treating |
| REQ-088-04-15 | DSO entrainment design target SHALL be 50 ppmw S (TBC by vendor); expected DSO entrainment is 30 ppmw S. | DBM-Comp_and_Liquids §Condensate Mercaptan Treating |
| REQ-088-04-16 | Defined external interfaces SHALL be provided for incinerator overhead, dilution gas, and enrichment gas. | DBM-Comp_and_Liquids §Condensate Mercaptan Treating |
| REQ-088-04-17 | Caustic regeneration SHALL NOT be included in the package scope. | DBM-Comp_and_Liquids §Condensate Mercaptan Treating |
| REQ-088-04-18 | The package SHALL be designed for extractable compounds including H2S, CO2, and methyl/ethyl/propyl/butyl mercaptans. | DBM-Comp_and_Liquids §Condensate Mercaptan Treating |
| REQ-088-04-19 | Caustic tank material/coating selections SHALL be confirmed (TBC); aluminum is prohibited. | DBM-Comp_and_Liquids §Condensate Mercaptan Treating |
| REQ-088-04-20 | The vendor package SHALL be developed from and consistent with the EPC Scope of Work (DEL-088-01) and Package Datasheet (DEL-088-02). | DELIVERABLE_REGISTER row 267 |

## Standards

| Standard | Applicability | Location |
|---|---|---|
| Source Authority — 26020-Package_Requirements.docx, package heading 41 | Authoritative requirements text for PKG-088 | location TBD (binary .docx not accessible as text) |
| Workbook Packages row 50 | Vendor responsibility allocation for PKG-088 | location TBD (binary .xlsx) |
| West Doe DBM-Comp_and_Liquids 3-25 §"Condensate Mercaptan Treating" | Design basis for non-regenerative caustic mercaptan treating at 03-25 | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 387–402 |
| Applicable Canadian provincial and CSA standards for caustic service / pressure equipment | ASSUMPTION: customary jurisdiction; specific codes TBD | TBD |

## Verification

| Req ID | Verification Method |
|---|---|
| REQ-088-04-01, -02, -03, -09, -10, -16, -17 | Design review against vendor package design basis and P&IDs; equipment list audit. |
| REQ-088-04-04, -05, -06 | Performance test or vendor performance guarantee against C1-C3 RSH and total sulphur targets; waiver disposition recorded. |
| REQ-088-04-07, -08, -19 | Layout/general arrangement review; material certifications audit (no aluminum in caustic building). |
| REQ-088-04-11, -12, -13 | Tank datasheet review; mechanical inspection; flame arrestor witness test; venting tie-in verification. |
| REQ-088-04-14, -15 | Vendor TBC closure: confirm SG and DSO entrainment design with vendor data sheets/test results. |
| REQ-088-04-18 | Process simulation / vendor sizing record review for the extractable compound slate. |
| REQ-088-04-20 | EPC Integrator integration review against DEL-088-01 and DEL-088-02 (per DEL-088-06 acceptance gate). |

## Documentation

The vendor SHALL produce, as anticipated artifacts for this deliverable (source: `_CONTEXT.md`; DELIVERABLE_REGISTER row 267):

- Vendor engineered physical equipment package (the supplied equipment itself).
- Vendor package design basis.
- Vendor package datasheet set.

Vendor document register, submittals, and turnover records are tracked under sibling deliverable DEL-088-05 (Vendor Document Turnover Package). EPC integration review and acceptance is tracked under DEL-088-06.
