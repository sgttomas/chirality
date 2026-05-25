# Guidance: DEL-001-03_construction-work-package — Construction Work Package

## Purpose

This Construction Work Package exists to turn the accepted PKG-001 Earthworks for foundations basis into a construction-facing package for installation, tie-in, inspection, turnover, and interface control. Gate 7 identifies it as a mandatory EPC Integrator deliverable; the 04-25 DBM identifies field construction activities, including grading, piling, and foundation work, as Tourmaline field construction scope.

## Principles

- Keep source authority visible. Workbook row 2 and Gate 7 define package identity and interfaces; DBM-Deepcut SEC-11 defines the civil basis values currently available for construction planning.
- Separate document ownership from field execution. Gate 7 assigns this deliverable to the EPC Integrator; the DBM assigns field construction activities to Tourmaline Oil Corporation.
- Do not close geotechnical or topographical values from placeholders. The DBM explicitly keeps multiple geotechnical and survey inputs TBD pending completion and review.
- Treat interface facts as construction controls. PKG-001 carries Grading / Site Drainage / Spill Containment and Structural / Foundations / Supports interfaces, so the workface plan and turnover checklist should include these controls.
- Preserve unresolved items in the work package rather than converting them into construction criteria.

## Considerations

The available sources support construction planning at a basis level, not a final issued-for-construction package level. The DBM provides civil design principles such as pad slope, grade slope, ditch/culvert slopes, retention-pond intent, and default foundation basis. It does not provide PKG-001-specific quantities, coordinates, approved inspection forms, construction schedule, or final work packs.

Construction content should therefore be organized as a controlled package with explicit placeholders for final inputs:

- geotechnical assessment report;
- topographical survey and grade surface file;
- plot plan and retention pond coordination;
- detailed engineering drainage design;
- approved foundation drawings and pile parameters;
- inspection and turnover form templates.

## Trade-offs

| Topic | Conservative treatment |
|---|---|
| DBM values vs final construction data | Use DBM values as planning basis only; require accepted detailed engineering or geotechnical/topographical inputs before final construction criteria are closed. |
| Construction responsibility | Show both the EPC Integrator deliverable owner and Tourmaline field construction basis to avoid assigning field execution solely from the deliverable register. |
| Interface checklist detail | Include known interface categories now; leave detailed checklist line items TBD until approved drawings/forms are available. |
| Foundation basis | Carry driven steel piles as the default DBM basis while allowing detailed engineering to confirm different support requirements. |

## Examples

- A grading workface plan entry may cite the DBM pad slope basis and then reference the approved grading drawing as `TBD` until issued.
- A foundation turnover checklist may include pile installation records and as-built checks, but final form IDs remain `TBD` unless project forms are available.
- An interface checklist item may require confirmation that grading/site drainage/spill containment and structural/foundations/supports interfaces have been reviewed against the latest plot plan and civil drawings.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CWP-CON-001 | Deliverable owner is EPC Integrator, while field construction responsibility is assigned to Tourmaline Oil Corporation. | DELIVERABLE_REGISTER.csv row DEL-001-03 | DBM-Deepcut/4-25_Deepcut_DBM.md, Construction Responsibility | Datasheet Construction; Specification CWP-011; Procedure Prerequisites/Steps | Treat EPC Integrator as document owner and Tourmaline as field execution responsibility unless project RACI states otherwise. | TBD |
