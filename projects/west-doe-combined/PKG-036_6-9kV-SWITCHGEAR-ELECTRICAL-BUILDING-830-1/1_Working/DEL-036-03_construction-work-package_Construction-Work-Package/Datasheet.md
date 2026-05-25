# Datasheet: DEL-036-03_construction-work-package

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-036-03_construction-work-package` | `_CONTEXT.md` |
| Deliverable name | Construction Work Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-036` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | 6.9kV SWITCHGEAR ELECTRICAL BUILDING (830-1) | `PACKAGE_REGISTER.csv` row `PKG-036`; Workbook Packages row 38 |
| Workbook ID / row | 36 / row 38 | `PACKAGE_REGISTER.csv`; Workbook Packages row 38 |
| WBS | 01 | `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-01-30-027 | `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Deliverable type | EPC Construction Work Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | EPC Integrator | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Covers scope item | `SOW-0037` | `DELIVERABLE_REGISTER.csv` |
| Supports objectives | OBJ-001; OBJ-004; OBJ-005; OBJ-006; OBJ-007; OBJ-008; OBJ-009; OBJ-010 | `OBJECTIVE_DELIVERABLE_MAP.csv` (PACKAGE_HEURISTIC: ASSUMPTION) |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Package class | Vendor-owned Electrical package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-036` |
| Construction work package artifact | Integrator-authored construction work package for physical installation, construction, and tie-in to larger systems. | `ARTIFACT_REGISTER.csv` `ART-5AF99634D9` |
| Installation and tie-in workface plan artifact | Workface planning evidence for installing/building the package and connecting it to adjacent process, utility, electrical, controls, civil, structural, and safety systems as applicable. | `ARTIFACT_REGISTER.csv` `ART-0CFB00EEF8` |
| Construction interface and turnover checklist artifact | Construction-facing interface, tie-in, inspection, and turnover evidence for the approved package. | `ARTIFACT_REGISTER.csv` `ART-A5CFBCEAB9` |
| Electrical building construction basis | Electrical buildings shall be prefabricated, modular buildings located in general purpose areas. Switchgear-class electrical buildings are listed as "Shop" prefab type. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings paragraph; electrical building type table |
| Cable-entry construction basis | Electrical buildings shall be designed for bottom entry of incoming and outgoing power cables; buildings shall be elevated and installed on piles to provide space beneath the building for incoming cable trays. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings paragraph |
| Climate-control construction basis | Electrical buildings shall be climate controlled with HVAC sized as n+1. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings paragraph |
| Internal wiring construction basis | Electrical buildings shall be wired with TECK and ACIC cables; EMT conduit shall be used for equipment located adjacent to each other; an outdoor GFI receptacle shall be provided for exterior maintenance; equipment doors sized or transom-equipped for removal of the largest equipment. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings paragraph |
| Grounding construction basis | All major electrical equipment shall be directly connected to the ground grid at two points; ground wells at electrical buildings shall be provided for maintenance and operational testing, with bolted ground connections at test points; above-grade grounding conductors shall be green insulated ground wires run in PVC conduit where mechanical protection is required; ground connections shall be compression type. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Grounding paragraph |

## Conditions

| Interface / condition | Construction-package requirement basis | Source |
|---|---|---|
| Utility Piping | Tie-in plan and construction sequencing required where utility piping crosses the building battery limit. | `INTERFACE_REGISTER.csv` `IFC-9188C9FD26` |
| Drain / Containment | Tie-in to facility drain/containment system required; field routing and slope to be coordinated with civil. | `INTERFACE_REGISTER.csv` `IFC-628EF275F0` |
| Electrical Power | Incoming and outgoing power-cable tie-ins to/from the 13.8 kV switchgear feed and downstream 6.9 kV distribution must be planned for bottom-entry installation. | `INTERFACE_REGISTER.csv` `IFC-3B6012818E`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings and Plant Power Distribution paragraphs |
| Grounding / Bonding | Building shall be tied to facility ground grid at two points per equipment with ground wells provided. | `INTERFACE_REGISTER.csv` `IFC-B6F77BBE8A`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Grounding paragraph |
| Area / Exterior Lighting | Field installation of exterior area lighting tied to the building's lighting service to be coordinated. | `INTERFACE_REGISTER.csv` `IFC-D49FB38D6F` |
| I&C / Control Cabling | I&C and control cable tray/conduit tie-ins to adjacent skids and plant PLC racks to be planned in workface plan. | `INTERFACE_REGISTER.csv` `IFC-972B08F285` |
| Communications / Network | Network cabling tie-in to the building's network rack and facility backbone to be planned. | `INTERFACE_REGISTER.csv` `IFC-349D2200D1` |
| Building HVAC / Services | HVAC commissioning of the n+1 building system required during turnover. | `INTERFACE_REGISTER.csv` `IFC-C81A342112`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings paragraph |
| Fire & Gas / Safety Systems | Tie-in of building F&G detection and alarms to facility systems required during construction. | `INTERFACE_REGISTER.csv` `IFC-2C313DA749` |
| Maintenance Access | Construction layout and door sizing must preserve removal-path access for the largest equipment. | `INTERFACE_REGISTER.csv` `IFC-21B90D3691`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings paragraph |
| Grading / Site Drainage / Spill Containment | Pad grading and surface drainage at the building location to be coordinated with civil. | `INTERFACE_REGISTER.csv` `IFC-DC7DB17C89` |
| Structural / Foundations / Supports | Piled foundation supporting elevated, bottom-entry building installation; structural tie-in to be coordinated with structural design. | `INTERFACE_REGISTER.csv` `IFC-BDE626F7DD`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings paragraph |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Package engineering and physical equipment delivery | Package Vendor responsibility. | `PACKAGE_REGISTER.csv` row `PKG-036` |
| Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination | EPC Integrator responsibility. | `PACKAGE_REGISTER.csv` row `PKG-036` |
| Building prefabrication / shop assembly | The package is a shop-prefabricated modular electrical building. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical-building-type table |
| Site receipt, set, and anchor | Set on piled, elevated foundation supporting bottom-entry cabling. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings paragraph |
| Cable pulls and terminations | TECK/ACIC cables run through cable tray; EMT used for adjacent-equipment connections; bottom entry to MCC/switchgear sections. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings paragraph |
| Grounding installation | Two-point connection to facility ground grid per equipment; ground wells at building; compression-type ground connections. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Grounding paragraph |
| Inspection and test in field | Field acceptance tests, megger / continuity / functional tests of electrical equipment in accordance with detailed design. | TBD — detailed test list not present in accessible source slices |
| Turnover and tie-in checklist | Construction interface and turnover checklist artifact (`ART-A5CFBCEAB9`) governs handoff to commissioning. | `ARTIFACT_REGISTER.csv` `ART-A5CFBCEAB9` |
| Schedule / sequencing | TBD — no project schedule reference is available in source slices. | Source gap |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-036-03_construction-work-package`.
- `PACKAGE_REGISTER.csv`, row `PKG-036`.
- `ARTIFACT_REGISTER.csv`, rows `ART-5AF99634D9`, `ART-0CFB00EEF8`, `ART-A5CFBCEAB9`.
- `INTERFACE_REGISTER.csv`, rows for `PKG-036` (12 declared interface types).
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-036-03_construction-work-package`.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 38.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical-building, plant power distribution, grounding, cable tray and conduit slices.
- `_Sources/26020-Package_Requirements.docx`, searched for package-specific construction content; no `PKG-036` package-specific slice accessible.
