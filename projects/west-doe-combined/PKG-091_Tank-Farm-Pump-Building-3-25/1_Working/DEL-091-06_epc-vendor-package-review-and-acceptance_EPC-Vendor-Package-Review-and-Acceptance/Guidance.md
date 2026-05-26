# Guidance: DEL-091-06 — EPC Vendor Package Review and Acceptance

## Purpose

This deliverable exists to provide EPC-Integrator-side evidence that the Tank Farm Pump Building 3-25 vendor package (DEL-091-04) and its turnover documentation (DEL-091-05) have been reviewed against the EPC anchor artifacts (DEL-091-01 EPC SOW; DEL-091-02 EPC Package Datasheet; DEL-091-03 Construction Work Package) and are acceptable for handoff to construction and downstream commissioning (`_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row 473).

## Principles

- **EPC Integrator owns acceptance.** Vendor authoring (DEL-091-04, DEL-091-05) and EPC acceptance (DEL-091-06) are deliberately separated; acceptance evidence here must not relitigate vendor design choices but must verify conformance to the EPC anchor set (`_CONTEXT.md` ResponsibleParty).
- **Anchor docs are authoritative.** EPC Scope of Work, Package Datasheet, and Construction Work Package set the binding acceptance basis. The Liquids Hub equipment basis in `3-25_Comp_and_Liquids_DBM.md` (lines 40, 412-414, 526, 575-583) frames what equipment is in scope.
- **Source-grounded over convention.** Where vendor turnover content disagrees with the 3-25 DBM equipment basis or the package requirements document (`26020-Package_Requirements.docx` heading 44, location TBD), treat the EPC anchors and the project source as authoritative and capture the disagreement in the Conflict Table for human ruling.
- **Defer LACT scope.** LACT is third-party NRM scope (`3-25_Comp_and_Liquids_DBM.md` lines 54, 417) and is reviewed at the tie-in boundary only.

## Considerations

- **Source access constraint.** `26020-Package_Requirements.docx` heading 44 and `26020-Packages_Interfaces_4_export.xlsx` Packages row 84 are referenced but not locally accessible as text (`_REFERENCES.md`, Missing / Deferred References). Clause-level acceptance criteria from those documents cannot be enumerated until the source slice is resolved; treat checklist row structure as ASSUMPTION until then.
- **Driver type for non-loading pumps.** The DBM explicitly identifies electric drivers for loading pumps and VRU drivers; other pump-building pump drivers are assumed electric pending vendor confirmation (`Datasheet.md`, Attributes; `3-25_Comp_and_Liquids_DBM.md` line 526).
- **Sour service applicability.** The 03-25 site has sour gas and sour produced water present in adjacent systems; per-equipment sour-service classification within the pump building is to be confirmed at acceptance from vendor datasheets, not inferred (`Specification.md` R-09).
- **Objectives association heuristic.** The OBJ-002..OBJ-010 association in `_CONTEXT.md` reflects PACKAGE_HEURISTIC; treat these as directionally relevant context, not as binding acceptance criteria (RuntimeOverride `OBJECTIVE_ASSOCIATION_MODE=PACKAGE_HEURISTIC`).
- **Modularization assumption.** Building/skid modularization is consistent with the project modularization convention (`3-25_Comp_and_Liquids_DBM.md` line 294) but the package-level enclosure details are TBD pending the package requirements document.

## Trade-offs

- **Checklist depth vs. schedule.** A clause-by-clause checklist mapped to `26020-Package_Requirements.docx` heading 44 maximizes acceptance traceability but requires source access; an interim, structure-only checklist preserves schedule but defers traceability and increases risk of missed clauses. Recommendation: start with structure-only and convert to clause-mapped once source access is resolved.
- **Witness vs. document review.** Witnessed FAT/inspection coverage provides higher acceptance confidence than document review alone but adds cost and scheduling risk. Apply witness coverage selectively to performance-critical equipment (e.g., condensate booster pumps per Datasheet duty 165 m3/h at 35 m TDH).
- **Punch list strictness.** A tight "no punch items at handoff" gate increases the chance of rejecting otherwise acceptable packages over minor items; a graded disposition (accept / accept-with-comment / reject / rework, per `Specification.md` R-10) preserves momentum while retaining traceability.

## Examples

- Pump performance acceptance: condensate booster pumps verified at 2 x 100% with duty 165 m3/h at 35 m TDH per pump against FAT report and Package Datasheet (`3-25_Comp_and_Liquids_DBM.md` lines 412-413).
- Loading pump count acceptance: three condensate loading pumps mapped one-per-truck-loading-station against the construction work package layout (`3-25_Comp_and_Liquids_DBM.md` lines 414, 526, 654).
- LACT boundary acceptance: P&ID review confirms tie-in only at the facility-side flange; LACT internals are NRM scope and excluded from this acceptance (`3-25_Comp_and_Liquids_DBM.md` lines 54, 417).

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority | Human ruling |
|---|---|---|---|---|---|---|
| C-01 | Driver type for non-loading pumps in pump building is not explicitly enumerated; DBM names electric drivers for loading pumps and VRU drivers only. | `3-25_Comp_and_Liquids_DBM.md` line 526 (loading pumps + VRU electric) | `26020-Package_Requirements.docx` heading 44 (not locally accessible) | Datasheet "Driver type"; Specification R-09 | PROPOSAL: confirm electric drivers via vendor datasheets (DEL-091-04/05); fall back to PROPOSAL pending source slice access | TBD |
| C-02 | Pump building enclosure / modularization details not explicitly documented at package level. | `3-25_Comp_and_Liquids_DBM.md` line 294 (modularization convention) | `26020-Package_Requirements.docx` heading 44 (location TBD) | Datasheet "Construction"; Specification Standards row 1 | PROPOSAL: treat modularization as ASSUMPTION; resolve when source slice is accessible | TBD |
| C-03 | Clause-level acceptance criteria cannot be enumerated without `26020-Package_Requirements.docx` heading 44 access. | `_REFERENCES.md` (Missing / Deferred References) | n/a | Specification R-02, R-03, R-08, Standards row 1; Procedure Step 3 | PROPOSAL: maintain structural checklist; mark clause-mapping TBD until source slice access. | TBD |
| C-04 | Industry pump/pressure standards (API 610, ASME B31.3) are likely applicable but not explicitly named in accessible sources. | `3-25_Comp_and_Liquids_DBM.md` (no explicit citation) | `26020-Package_Requirements.docx` heading 44 (location TBD) | Specification Standards row 3, R-05, R-09 | PROPOSAL: confirm applicability via package requirements doc and vendor datasheets before adopting as acceptance basis. | TBD |

No items flagged HRR (High-Risk-Ruling) by upstream `_SEMANTIC_LENSING.md` — that file does not yet exist for this deliverable (Pass 3 deferred). Conflicts above are surfaced for routine human ruling, not as HRR items.
