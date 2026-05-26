# Guidance: DEL-094-03_construction-work-package — Construction Work Package

## Purpose

This Construction Work Package exists to turn the accepted PKG-094 Tanks, Caustic (API 650) 3-25 basis into a construction-facing package for installation, tie-in, inspection, turnover, and interface control of one (1) fresh caustic tank and one (1) spent caustic tank serving the 03-25 Liquids Hub non-regenerative caustic mercaptan treating unit. Gate 7 identifies it as a mandatory EPC Integrator deliverable.

## Principles

- Keep source authority visible. Workbook Packages row 86 and Gate 7 registers define package identity and interfaces; DBM-Comp_and_Liquids 3-25 defines the caustic-service, caustic-drain, and site basis values currently available for construction planning.
- Separate document ownership from field execution. Gate 7 assigns this deliverable to the EPC Integrator; the PACKAGE_REGISTER row further assigns package engineering and the physical equipment package to the package vendor.
- Respect caustic-service safety constraints in construction planning: no aluminum in the caustic building; spent-caustic flame arrestor to incinerator header; fuel-gas blanketing, heating, and insulation on both tanks.
- Treat interface facts as construction controls. PKG-094 carries nine interfaces; each must appear in the construction interface and turnover checklist.
- Preserve unresolved items (tank material/coating, caustic drain temperature, heat tracing, foundation/plot data, API 650 clause-level provisions) as TBD rather than converting them into construction criteria.

## Considerations

The available sources support construction planning at a basis level, not a final issued-for-construction package level. The DBM provides caustic-service design principles such as tank type and size, fuel-gas blanketing, heating/insulation, venting through flame arrestor to incinerator header, truck-out support, drain rating, and material exclusions. It does not provide PKG-094-specific quantities, coordinates, approved inspection forms, construction schedule, foundation drawings, or material/coating selections. API 650 is named in the package title but its clause text is not locally accessible.

Construction content should be organized as a controlled package with explicit placeholders for final inputs:

- API 650 clause-level construction and inspection requirements;
- approved tank material and coating selections (currently TBC);
- caustic drain maximum temperature (currently TBC) and heat-tracing decision;
- foundation drawings and equipment coordinates;
- plot plan and tie-in coordinates for the nine PKG-094 interfaces;
- inspection and turnover form templates;
- PKG-094 field construction execution responsibility assignment.

## Trade-offs

| Topic | Conservative treatment |
|---|---|
| DBM values vs final construction data | Use DBM caustic-service and drain values as planning basis only; require accepted detailed engineering or vendor data before final construction criteria are closed. |
| Tank material/coating | Carry the DBM exclusion (no aluminum in caustic building) as a binding rule; leave positive material/coating selections TBD/TBC until detailed engineering and vendor data resolve them. |
| API 650 clause use | Name API 650 as governing standard; do not transcribe specific clause numbers/values without the source slice. |
| Responsibility split | Show both the EPC Integrator deliverable owner and the package vendor's engineering/equipment scope; flag PKG-094 field construction execution responsibility as TBD. |
| Interface checklist detail | Include all nine known interface categories now; leave detailed checklist line items TBD until approved drawings/forms are available. |

## Examples

- A spent-caustic vent workface entry may cite the DBM "flame arrestor to incinerator header" basis and then reference the approved P&ID/ISO as `TBD` until issued.
- A caustic drain tie-in entry may cite the 300# ANSI minimum and 300# flange termination, with the drain maximum-temperature limit recorded as `TBC` per DBM.
- An interface checklist item may require confirmation that grounding/bonding and cathodic protection interfaces have been reviewed against the latest electrical and CP drawings.

## Conflict Table (for human ruling)

This table records the High-Risk-Resolution (HRR) items where source materials disagree, where decomposition narrative may overstate source content, or where construction-significant inputs remain unresolved.

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CWP-094-CON-001 | Field construction execution responsibility for PKG-094 is not explicitly assigned in accessible 03-25 source slices, while Gate 7 assigns the deliverable to the EPC Integrator. | DELIVERABLE_REGISTER.csv row DEL-094-03 (EPC Integrator deliverable owner) | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md (no PKG-094-specific construction responsibility section located) | Datasheet Construction; Specification CWP-011; Procedure Prerequisites/Steps | Treat EPC Integrator as document owner; record PKG-094 field execution responsibility as TBD pending project RACI or human ruling. | TBD |
| CWP-094-CON-002 | API 650 is named in the package title but no API 650 source slice is locally accessible to drive clause-level construction or inspection content. | PACKAGE_REGISTER.csv row PKG-094 (title "Tanks, Caustic (API 650) 3-25") | _REFERENCES.md (no API 650 source slice referenced); local `_Sources/` (API 650 text not present) | Specification CWP-009 and Standards table; Procedure Steps and Verification | Name API 650 as governing standard; keep clause-level construction/inspection provisions as `location TBD` until API 650 source slices are added. | TBD |
| CWP-094-CON-003 | Caustic tank material/coating, caustic drain maximum temperature, and SG value are all marked TBC in the DBM, but downstream construction must select definite materials and operating conditions. | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md, Caustic Mercaptan Treating Basis ("material/coating details remain TBC"; "SG 1.75 TBC") | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md, Drain Systems ("maximum temperature 121 deg C / 250 deg F TBC"; heat tracing "under consideration") | Datasheet Attributes/Conditions; Specification CWP-004, CWP-005, CWP-007 | Carry DBM exclusions (no aluminum in caustic building) as binding; leave positive material/coating, drain temperature, and heat-tracing decisions TBD pending detailed engineering. | TBD |
| CWP-094-CON-004 | Package responsibility split per PACKAGE_REGISTER assigns package engineering, design, vendor documentation, and physical equipment to the package vendor, while the Construction Work Package is an EPC Integrator deliverable; boundary at the vendor/EPC interface is not explicitly enumerated for construction handoff. | PACKAGE_REGISTER.csv row PKG-094, ResponsibilityNarrative | DELIVERABLE_REGISTER.csv row DEL-094-03 | Specification CWP-012; Procedure Steps; Guidance Trade-offs | Use the PACKAGE_REGISTER responsibility narrative as the working split; record the precise vendor-to-EPC construction handoff list as TBD pending detailed engineering or human ruling. | TBD |
| CWP-094-CON-005 | The 26020-Package_Requirements.docx package heading 46 is named as a source for PKG-094 deliverables but is not extracted to locally readable markdown, so any explicit construction provisions it contains are not available. | _REFERENCES.md (Workbook Packages row 86; 26020-Package_Requirements.docx package heading 46) | Local `_Sources/26020-Package_Requirements.docx` (binary; no extracted slice) | Specification Standards; Datasheet References; Procedure Prerequisites | Cite the Word source with `location TBD` until the heading-46 slice is extracted; do not invent provisions from decomposition narrative. | TBD |
