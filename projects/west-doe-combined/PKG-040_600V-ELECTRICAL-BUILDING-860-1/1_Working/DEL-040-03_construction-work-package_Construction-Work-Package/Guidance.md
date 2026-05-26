# Guidance: DEL-040-03_construction-work-package — Construction Work Package

## Purpose

This Construction Work Package exists to turn the accepted PKG-040 600V Electrical Building (860-1) basis into a construction-facing package for installation, tie-in, inspection, turnover, and interface control. Gate 7 identifies it as a mandatory EPC Integrator deliverable; the 04-25 DBM identifies the relevant field construction activities (off-loading, setting on foundations, mechanical hookup, home-run cabling, electrical terminations, area lighting) as Tourmaline field construction scope, and the package register identifies Package Vendor scope for package engineering/design/equipment.

## Principles

- Keep source authority visible. Workbook row 42 and Gate 7 define package identity and the twelve interface categories; DBM-Deepcut SEC-11 and SEC-12 define the civil/building and electrical basis values currently available for construction planning.
- Separate document ownership from field execution. Gate 7 assigns this deliverable to the EPC Integrator; PACKAGE_REGISTER splits Package Vendor scope (engineering/design/equipment) from EPC Integrator scope (facility integration); DBM assigns field construction activities to Tourmaline Oil Corporation.
- Do not close geotechnical, topographical, plot-plan, or electrical-study values from placeholders. The DBM explicitly keeps multiple geotechnical, survey, layout, and electrical-study inputs TBD pending completion and review.
- Treat all twelve interface facts as construction controls. PKG-040 carries the full SEC-12 / vendor-package interface set, so the workface plan and turnover checklist should cover utility piping, drains, electrical power, grounding/bonding, area/exterior lighting, I&C cabling, communications/network, building HVAC/services, fire & gas/safety systems, maintenance access, grading/drainage/spill containment, and structural/foundation/supports.
- Preserve unresolved items in the work package rather than converting them into construction criteria.

## Considerations

The available sources support construction planning at a basis level, not a final issued-for-construction package level. The DBM provides electrical building principles (modular shop-built, general-purpose area, n+1 HVAC, bottom-entry cabling, elevated on piles, equipment-removal door provisions, grounding, cable specification, lighting and receptacles) and civil basis values (pad slope, grade slope, ditch/culvert slopes, retention-pond intent, foundation basis). It does not provide PKG-040-specific quantities, coordinates, approved inspection forms, vendor IFC drawings, completed electrical studies, or final construction schedules.

Construction content should therefore be organized as a controlled package with explicit placeholders for final inputs:

- geotechnical assessment report;
- topographical survey and grade surface file;
- plot plan CIV-235633-5002 and 860-1 building coordinates;
- completed electrical studies (HAC, load analysis, short-circuit, relay coordination/arc-flash, load-flow);
- vendor IFC drawings and equipment lists for the 860-1 building;
- standby generator sizing, connection-point count, transfer-switch ratings, and sequencing;
- approved inspection and turnover form templates.

## Trade-offs

| Topic | Conservative treatment |
|---|---|
| DBM values vs final construction data | Use DBM SEC-11/SEC-12 values as planning basis only; require accepted detailed engineering, electrical studies, or geotechnical/topographical inputs before final construction criteria are closed. |
| Construction responsibility | Show Package Vendor (engineering/design/equipment), EPC Integrator (deliverable owner / facility integration), and Tourmaline (field construction execution) to avoid assigning field execution solely from the deliverable register. |
| Interface checklist detail | Include all twelve PKG-040 interface categories now; leave detailed checklist line items TBD until approved drawings/forms are available. |
| Foundation basis | Carry driven steel piles as the default DBM basis while allowing detailed engineering to confirm building-specific support requirements. |
| Plot plan dependency | Carry building coordinates and tie-in locations as TBD until CIV-235633-5002 is available and reviewed. |
| Standby/emergency power | Show the SEC-12 TOU-standby-generators-at-600V-MCC basis as the current direction, with sizing and transfer-switch ratings explicitly TBD. |
| Cathodic protection | Treat CP engineering/supply as out of facility design scope; document only the interface points the owner CP scope will use. |

## Examples

- A 860-1 building installation workface plan entry may cite the DBM SEC-12 bottom-entry-on-piles basis and then reference the approved vendor IFC drawing as `TBD` until issued.
- A grounding turnover checklist may include the #2/0 main loop installation, two-point connection of major equipment, and ground-well test records, but final form IDs remain `TBD` unless project forms are available.
- A HVAC turnover entry may require evidence that the cooling system continues to provide building heating and cooling during shutdown of one HVAC unit (n+1 basis), even where final commissioning form IDs are TBD.
- An interface checklist item may require confirmation that all twelve interface categories have been reviewed against the latest plot plan and approved electrical/civil drawings.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CWP-040-CON-001 | Deliverable owner is EPC Integrator, while field construction responsibility for activities including field-erected buildings, off-loading/setting on foundations, mechanical hookup, home-run cables, electrical terminations, and area lighting is assigned to Tourmaline Oil Corporation. | DELIVERABLE_REGISTER.csv row DEL-040-03 | DBM-Deepcut/4-25_Deepcut_DBM.md, Construction Responsibility | Datasheet Construction; Specification CWP-040-017; Procedure Prerequisites/Steps | Treat EPC Integrator as document owner, Package Vendor as package engineering/design/equipment owner, and Tourmaline as field execution responsibility unless project RACI states otherwise. | TBD |
| CWP-040-CON-002 | DBM SEC-12 Power System lists "600 V Sales/Overheads Compressor Electrical Building" among 600 V destinations but the 860-1 building is described in SEC-11 as the "600V General Area / Tank Farm Electrical Building"; PACKAGE_REGISTER labels PKG-040 as "600V ELECTRICAL BUILDING (860-1)". | DBM-Deepcut SEC-12 Power System (radial distribution list) | DBM-Deepcut SEC-11 (Buildings table, row 860-1); PACKAGE_REGISTER.csv PKG-040 | Datasheet Identification/Construction; Specification CWP-040-005 | Treat 860-1 as the General Area / Tank Farm Electrical Building per SEC-11 and PACKAGE_REGISTER; SEC-12 narrative naming variations require human ruling for any radial-feed scope statement. | TBD |
