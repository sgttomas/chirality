# Datasheet: DEL-032-04_vendor-engineered-equipment-package

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-032-04_vendor-engineered-equipment-package` | `_CONTEXT.md` |
| Deliverable name | Vendor Engineered Equipment Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-032` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | Cathodic Protection Design and Installation | Workbook Packages row 34; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 32 / row 34 | Workbook Packages row 34; `PACKAGE_REGISTER.csv` |
| WBS | 03 | `PACKAGE_REGISTER.csv` row `PKG-032` |
| CoA tracking number | 26020-03-30-023 | `PACKAGE_REGISTER.csv` row `PKG-032` |
| Discipline | Electrical | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Deliverable type | Vendor Package Production Unit | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | Package Vendor (engineering/design/equipment) with EPC Integrator integration review | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; EPC Integrator owns integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-032` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Production unit class | Vendor-owned Electrical package — engineering, design, fabrication/supply, vendor documentation, and physical equipment package for cathodic protection. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-032-04` |
| Package function | Cathodic protection design and installation package for the facility. | Workbook Packages row 34; `PACKAGE_REGISTER.csv` row `PKG-032` |
| Facility-design positioning | The Deepcut (4-25) DBM states that cathodic protection engineering and supply is excluded from facility design scope; the facility design shall support owner cathodic-protection interfaces. PKG-032 is the owner/vendor-side production unit that fulfills cathodic protection design and installation outside the facility electrical design scope. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Cathodic Protection section |
| Electrical scope acknowledgment | The Comp_and_Liquids (3-25) DBM lists cathodic protection as part of the electrical design scope (lighting, receptacles, EHT, building heaters, cathodic protection). | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, electrical design scope paragraph |
| CONFLICT: scope inclusion | 4-25 DBM excludes cathodic protection from facility electrical design (owner scope); 3-25 DBM lists cathodic protection within electrical design scope. See `Guidance.md` Conflict Table. | `_Sources/DBM-Deepcut/...`; `_Sources/DBM-Comp_and_Liquids/...` |
| Vendor engineering inputs | EPC Scope of Work (`DEL-032-01`) and Package Datasheet (`DEL-032-02`) form the vendor engineering basis. | `_CONTEXT.md`, Scope; `DELIVERABLE_REGISTER.csv` rows `DEL-032-01`, `DEL-032-02` |
| Vendor engineering outputs | Vendor engineered physical equipment package; vendor package design basis and datasheet set. | `_CONTEXT.md`, Anticipated Artifacts; `DELIVERABLE_REGISTER.csv` row `DEL-032-04` |
| Cathodic protection method / type | TBD. Sources do not specify impressed-current vs. sacrificial-anode, anode type, transformer-rectifier ratings, junction box configuration, or test station design for this package. | No package-specific source slice accessible |
| Protected assets / coverage | TBD. Sources do not enumerate which buried/submerged metallic assets (tanks, piping, vessels, grounding grid coordination) are within PKG-032 coverage. | Source gap |
| Quantities / counts | TBD. No package-specific quantity data is present in accessible sources. | `26020-Package_Requirements.docx` not parsed for PKG-032 specifically; no PKG-032 row link in `PACKAGE_REGISTER.csv` `WordSourceBasis` column |

## Conditions

| Interface / condition | Vendor package basis | Source |
|---|---|---|
| Electrical Power | Vendor package shall be engineered to the EPC-defined Electrical Power interface. | `INTERFACE_REGISTER.csv` `IFC-C2719906C1`; Workbook Packages row 34 |
| Grounding / Bonding | Vendor package shall be engineered to the EPC-defined Grounding / Bonding interface; coordination with facility grounding grid is required where cathodic protection and grounding interact. | `INTERFACE_REGISTER.csv` `IFC-F1FE9DF9DD`; Workbook Packages row 34 |
| I&C / Control Cabling | Vendor package shall be engineered to the EPC-defined I&C / Control Cabling interface for any monitoring, rectifier control, or alarm signaling. | `INTERFACE_REGISTER.csv` `IFC-4D092EC70F`; Workbook Packages row 34 |
| Communications / Network | Vendor package shall be engineered to the EPC-defined Communications / Network interface for remote monitoring of cathodic protection systems where applicable. | `INTERFACE_REGISTER.csv` `IFC-8594557BD3`; Workbook Packages row 34 |
| Owner / facility coordination | Per 4-25 DBM, Propak shall work with the owner to facilitate cathodic-protection interface requirements; the vendor package shall preserve this owner-coordinated interface posture. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Cathodic Protection section |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Package engineering and physical equipment | Package Vendor responsibility — engineering, design, fabrication/supply, vendor documentation, and the physical equipment package. | `PACKAGE_REGISTER.csv` row `PKG-032`; `DELIVERABLE_REGISTER.csv` row `DEL-032-04` |
| Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination | EPC Integrator responsibility (subject to integration review of the vendor package). | `PACKAGE_REGISTER.csv` row `PKG-032` |
| Installation location | TBD. Accessible sources do not assign PKG-032 cathodic protection equipment (transformer-rectifier units, anode beds, junction boxes, test stations) to specific facility locations. | Source gap |
| Foundations / supports | TBD. Structural / Foundations / Supports interface is not listed in the four PKG-032 interface rows; physical support of any transformer-rectifier cabinet or junction-box pedestal is `TBD`. | `INTERFACE_REGISTER.csv` PKG-032 rows |
| Vendor documentation set | Captured separately by `DEL-032-05_vendor-document-turnover-package`; this deliverable supplies the engineering, design basis, datasheet set, and physical equipment. | `DELIVERABLE_REGISTER.csv` (sibling deliverables under PKG-032) |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-032-04_vendor-engineered-equipment-package`.
- `PACKAGE_REGISTER.csv`, row `PKG-032`.
- `ARTIFACT_REGISTER.csv`, rows for `PKG-032`.
- `INTERFACE_REGISTER.csv`, rows `IFC-C2719906C1`, `IFC-F1FE9DF9DD`, `IFC-4D092EC70F`, `IFC-8594557BD3`.
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-032-04_vendor-engineered-equipment-package`.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Cathodic Protection section (facility design exclusion; owner interface).
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, electrical design scope paragraph naming cathodic protection.
- `_Sources/26020-Package_Requirements.docx`, package-specific cathodic protection content not retrieved for PKG-032 in this run.
- Sibling deliverables: `DEL-032-01_scope-of-work`, `DEL-032-02_package-datasheet` (vendor engineering inputs); `DEL-032-05_vendor-document-turnover-package`, `DEL-032-06_epc-vendor-package-review-and-acceptance` (downstream integration; if present in this package).
