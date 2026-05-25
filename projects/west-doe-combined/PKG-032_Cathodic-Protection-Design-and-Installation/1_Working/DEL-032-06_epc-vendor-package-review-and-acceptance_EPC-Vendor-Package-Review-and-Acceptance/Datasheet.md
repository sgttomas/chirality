# Datasheet: DEL-032-06_epc-vendor-package-review-and-acceptance

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-032-06_epc-vendor-package-review-and-acceptance` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Deliverable name | EPC Vendor Package Review and Acceptance | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-032` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | Cathodic Protection Design and Installation | Workbook Packages row 34; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 32 / row 34 | Workbook Packages row 34; `PACKAGE_REGISTER.csv` |
| WBS | 03 | Workbook Packages row 34; `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-03-30-023 | Workbook Packages row 34; `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | Workbook Packages row 34; `_CONTEXT.md` |
| Deliverable type | EPC Vendor Package Acceptance | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | EPC Integrator (lead) with Package Vendor input | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-032` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Deliverable role | EPC Integrator review and acceptance evidence for the vendor cathodic-protection package, against the EPC Scope of Work, Package Datasheet, and Construction Work Package. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-032-06` |
| Facility design boundary | Cathodic protection engineering and supply are excluded from the facility design scope; the facility design supports owner cathodic-protection interfaces as required. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, section "Cathodic Protection" |
| Owner coordination model | Propak shall work with the owner to facilitate cathodic-protection interface requirements; engineering and supply are excluded from facility design and remain owner-coordinated. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, sections "Cathodic Protection" and electrical heat tracing/CP summary table |
| Electrical scope context | Electrical design shall support cathodic protection interface power where defined, alongside facility utility, lighting, heat tracing, and building heater loads. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, electrical design scope paragraphs |
| Acceptance package contents (anticipated) | Vendor document review log; package acceptance checklist; test/inspection evidence; turnover evidence. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-032-06`; `ARTIFACT_REGISTER.csv` rows `ART-581D762C15`, `ART-43C50697CD`, `ART-B84E5EEC19` |
| Vendor scope under review | Vendor-owned engineering, design, fabrication/supply, and physical equipment package; vendor design basis and datasheet set; vendor documentation/turnover. | `ARTIFACT_REGISTER.csv` rows `ART-771B99C440`, `ART-E96FBE31DB` for `DEL-032-04`; vendor turnover artifacts for `DEL-032-05` |
| Vendor documentation availability | TBD. Source material does not provide a detailed vendor-document register for this package. | `ARTIFACT_REGISTER.csv` row `ART-A82FC3C3ED` ("TBD vendor document register") |
| Detailed CP design parameters | TBD. Anode type, anode bed location, rectifier rating, test station design, reference electrodes, current-density basis, and coating coordination are owner/vendor-defined and not present in accessible facility sources. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, section "Cathodic Protection"; `26020-Package_Requirements.docx` searched, no `PKG-032` package match accessible |

## Conditions

| Interface / condition | Acceptance basis | Source |
|---|---|---|
| Electrical Power | Vendor package shall identify required facility electrical power feeds (e.g., rectifier supply) and conform to the EPC interface fact registered for `PKG-032`. | Workbook Packages row 34; `INTERFACE_REGISTER.csv` `IFC-C2719906C1` |
| Grounding / Bonding | Vendor package shall coordinate grounding and bonding with facility electrical design without creating stray-current paths that defeat cathodic protection of buried/immersed steel. | Workbook Packages row 34; `INTERFACE_REGISTER.csv` `IFC-F1FE9DF9DD`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding and bonding paragraphs |
| I&C / Control Cabling | Vendor package shall define control/monitoring cabling, signal points, and test-station I&C interfaces required by the owner CP solution and the facility I&C system. | Workbook Packages row 34; `INTERFACE_REGISTER.csv` `IFC-4D092EC70F` |
| Communications / Network | Vendor package shall define any remote-monitoring or network interface for rectifier or test-station data required by the owner CP system. | Workbook Packages row 34; `INTERFACE_REGISTER.csv` `IFC-8594557BD3` |
| Facility design exclusion | Acceptance shall confirm that vendor-supplied engineering does not implicitly transfer cathodic-protection engineering or supply into the facility design scope. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, section "Cathodic Protection" |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Vendor package engineering and physical equipment | Package Vendor responsibility under EPC Integrator integration review. | `PACKAGE_REGISTER.csv` row `PKG-032`; `DELIVERABLE_REGISTER.csv` row `DEL-032-04` |
| Facility integration, interfaces, tie-ins, constructability | EPC Integrator responsibility under review and acceptance evidence. | `PACKAGE_REGISTER.csv` row `PKG-032`; `DELIVERABLE_REGISTER.csv` row `DEL-032-06` |
| Installation location | TBD. Source does not assign physical locations for rectifier(s), anode bed(s), or test stations under PKG-032. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, section "Cathodic Protection" |
| Test and inspection evidence | Factory/shop test and inspection evidence shall be carried as acceptance artifacts; detailed test list is vendor-defined and TBD. | `ARTIFACT_REGISTER.csv` row `ART-B84E5EEC19` |
| Turnover evidence | Vendor package acceptance and turnover checklist shall be produced and reviewed by EPC Integrator. | `ARTIFACT_REGISTER.csv` row `ART-43C50697CD` |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers and shared source root.
- `DELIVERABLE_REGISTER.csv`, row `DEL-032-06_epc-vendor-package-review-and-acceptance` (and sibling DEL-032-01..05 for context).
- `PACKAGE_REGISTER.csv`, row `PKG-032`.
- `ARTIFACT_REGISTER.csv`, rows for `DEL-032-06` and supporting sibling deliverables.
- `INTERFACE_REGISTER.csv`, rows for `PKG-032` (`IFC-C2719906C1`, `IFC-F1FE9DF9DD`, `IFC-4D092EC70F`, `IFC-8594557BD3`).
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-032-06`.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 34.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, section "Cathodic Protection" and electrical design basis introduction; grounding and bonding paragraphs.
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, electrical design scope and cathodic-protection scope paragraphs.
- `_Sources/26020-Package_Requirements.docx`, searched for package-specific cathodic-protection content; no PKG-032 package match found.
