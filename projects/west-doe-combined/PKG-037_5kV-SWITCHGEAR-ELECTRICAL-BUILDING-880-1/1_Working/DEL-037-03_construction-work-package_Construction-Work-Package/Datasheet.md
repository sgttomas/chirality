# Datasheet: DEL-037-03_construction-work-package

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-037-03_construction-work-package` | `_CONTEXT.md` |
| Deliverable name | Construction Work Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-037` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | 5kV SWITCHGEAR ELECTRICAL BUILDING (880-1) | Workbook Packages row 39; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 37 / row 39 | Workbook Packages row 39; `PACKAGE_REGISTER.csv` |
| WBS | 01 | Workbook Packages row 39; `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-01-30-028 | Workbook Packages row 39; `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | Workbook Packages row 39; `_CONTEXT.md` |
| Deliverable type | EPC Construction Work Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | EPC Integrator | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-037` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Package class | Vendor-owned Electrical package; EPC-integrated installation | `PACKAGE_REGISTER.csv` row `PKG-037` |
| Package function | 5kV switchgear electrical building (Building 880-1) housing medium-voltage switchgear and supporting electrical-building services | Workbook Packages row 39; `PACKAGE_REGISTER.csv` |
| Building configuration basis | Electrical buildings shall be prefabricated, modular buildings located in general purpose areas, climate-controlled with n+1 HVAC, and designed for bottom entry of incoming and outgoing power cables. Buildings shall be elevated and installed on piles to provide space beneath the building for incoming cables in trays. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, "Electrical Buildings" section |
| Cabling basis | Electrical buildings shall be wired with TECK and ACIC cables. EMT conduit shall be used for equipment located adjacent to each other (e.g., control panels to contactor panels). An outdoor GFI receptacle shall be provided for exterior maintenance. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, "Electrical Buildings" section |
| Access provisions | Equipment doors shall be sized for, or include removable transom sections to allow, removal of the largest equipment housed in the building. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, "Electrical Buildings" section |
| Switchgear voltage class | 5 kV class medium-voltage switchgear, package identity confirmed by workbook row. Specific bus rating, interrupting capacity, lineup, and feeder schedule remain `TBD` pending vendor engineered package data. | Workbook Packages row 39; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical design basis |
| Grounding basis | All major electrical equipment shall be directly connected to the ground grid at two points. Ground wells at power transformers or electrical buildings shall be provided for maintenance and operational testing, with bolted ground connections at test points in the ground wells. Above-grade grounding conductors shall be green insulated ground wires run in PVC conduit where mechanical protection is required; ground connections shall be compression type. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding and bonding section |
| Installation location | `TBD`. Source material confirms general-purpose-area siting for electrical buildings but does not assign a confirmed plot coordinate or arrangement for Building 880-1. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, area classification and electrical buildings sections |

## Conditions

| Interface / condition | Construction implication | Source |
|---|---|---|
| Utility Piping | Coordinate routing through or adjacent to the electrical building footprint; avoid conflict with electrical-building services. | Workbook Packages row 39; `INTERFACE_REGISTER.csv` `IFC-524BC4670F` |
| Drain / Containment | Provide site drainage and any required containment around the electrical building. | Workbook Packages row 39; `INTERFACE_REGISTER.csv` `IFC-A8DC0D3056` |
| Electrical Power | Tie-in of incoming and outgoing power cables via bottom entry; coordinate with facility power distribution. | Workbook Packages row 39; `INTERFACE_REGISTER.csv` `IFC-35A170DE7F`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings section |
| Grounding / Bonding | Two-point connection of major electrical equipment to facility ground grid; ground wells at the electrical building. | Workbook Packages row 39; `INTERFACE_REGISTER.csv` `IFC-E26DA604FB`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding section |
| Area / Exterior Lighting | Coordinate exterior lighting around the building for maintenance and egress; specific fixtures/levels `TBD`. | Workbook Packages row 39; `INTERFACE_REGISTER.csv` `IFC-8F0D1E29F1` |
| I&C / Control Cabling | Coordinate routing of control cabling between building equipment and field; TECK/ACIC basis applies. | Workbook Packages row 39; `INTERFACE_REGISTER.csv` `IFC-F5B78B59CE`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings section |
| Communications / Network | Coordinate communications/network cabling and rack interfaces inside the electrical building. | Workbook Packages row 39; `INTERFACE_REGISTER.csv` `IFC-1ECBDB6397` |
| Building HVAC / Services | Provide n+1 HVAC system sized to tolerate failure or maintenance of one unit without affecting heating/cooling. | Workbook Packages row 39; `INTERFACE_REGISTER.csv` `IFC-D6D4CB07AF`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings section |
| Fire & Gas / Safety Systems | Coordinate fire/gas detection and safety interfaces with the electrical building services. | Workbook Packages row 39; `INTERFACE_REGISTER.csv` `IFC-4D8A22B2CA` |
| Maintenance Access | Equipment doors and clearances sized for removal of the largest housed equipment; preserve access during installation. | Workbook Packages row 39; `INTERFACE_REGISTER.csv` `IFC-CE2AC83D1D`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings section |
| Grading / Site Drainage / Spill Containment | Provide grading and drainage around the elevated, pile-supported building; spill containment per site requirements. | Workbook Packages row 39; `INTERFACE_REGISTER.csv` `IFC-65DF6F2E88` |
| Structural / Foundations / Supports | Pile-supported, elevated foundation to allow bottom cable entry; coordinate with civil/structural packages. | Workbook Packages row 39; `INTERFACE_REGISTER.csv` `IFC-8012069CE2`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings section |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Building delivery | Prefabricated, modular electrical building delivered as a vendor-engineered package; field set on piles. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings section; `PACKAGE_REGISTER.csv` row `PKG-037` |
| Installation responsibility | EPC Integrator owns site installation, tie-ins, constructability, procurement/construction coordination, and facility-level integration. Package Vendor owns the engineered building and its physical equipment. | `PACKAGE_REGISTER.csv` row `PKG-037` |
| Tie-ins | Bottom-entry incoming and outgoing power cables; control, communications, grounding, HVAC, drainage, and safety system tie-ins per the interface list. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings section; `INTERFACE_REGISTER.csv` rows for `PKG-037` |
| Inspection | EPC Integrator-led construction inspections cover foundations/piles, building set, bottom cable entry provisions, grounding-grid connections, HVAC commissioning, and door/access provisions. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings and grounding sections |
| Turnover | Construction turnover to commissioning includes verified tie-ins, grounding test records, HVAC functional checks, and confirmation that maintenance access has been preserved. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings section |
| Foundations / supports | Pile-supported, elevated foundation; cable tray access maintained beneath the building. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings section |
| Detailed construction schedule | `TBD` pending vendor delivery dates, site readiness, and facility-level integrated schedule. | Source gap |
| Workforce/equipment plan | `TBD` pending EPC Integrator construction execution planning. | Source gap |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-037-03_construction-work-package`.
- `PACKAGE_REGISTER.csv`, row `PKG-037`.
- `ARTIFACT_REGISTER.csv`, rows for `DEL-037-03_construction-work-package`.
- `INTERFACE_REGISTER.csv`, rows for `PKG-037`.
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-037-03_construction-work-package`.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 39.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings, electrical design basis, and grounding/bonding source slices.
