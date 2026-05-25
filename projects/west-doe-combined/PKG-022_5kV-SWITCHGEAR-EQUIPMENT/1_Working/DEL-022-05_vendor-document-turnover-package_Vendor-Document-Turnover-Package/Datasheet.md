# Datasheet: DEL-022-05_vendor-document-turnover-package

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-022-05_vendor-document-turnover-package` | `_CONTEXT.md` |
| Deliverable name | Vendor Document Turnover Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-022` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | 5kV SWITCHGEAR EQUIPMENT | Workbook Packages row 24; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 22 / row 24 | Workbook Packages row 24; `PACKAGE_REGISTER.csv` |
| WBS | 01 | `PACKAGE_REGISTER.csv` row `PKG-022` |
| CoA tracking number | 26020-01-30-013 | `PACKAGE_REGISTER.csv` row `PKG-022` |
| Discipline | Electrical | Workbook Packages row 24; `_CONTEXT.md` |
| Deliverable type | Vendor Document Turnover | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | Package Vendor (vendor documentation) with EPC Integrator interface/integration review | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-022` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Deliverable function | Single Package Vendor deliverable assembling the vendor document register, submittals, source-required vendor documentation, and turnover records for the PKG-022 5kV switchgear equipment package, with EPC Integrator review. | `DELIVERABLE_REGISTER.csv` row `DEL-022-05`; `_CONTEXT.md` |
| Anticipated artifacts | Vendor document register; vendor document submittals; source vendor document table rows as artifacts where available; turnover records. | `DELIVERABLE_REGISTER.csv` row `DEL-022-05`; `_CONTEXT.md` |
| Artifact register (current) | One register row: `ART-E34A2C824B` — "TBD vendor document register" — flagged as Vendor Documentation Gap Evidence; detailed vendor-document requirements are not present in current source material for this package. | `ARTIFACT_REGISTER.csv` row `ART-E34A2C824B` |
| Source vendor document table rows | TBD. `_Sources/26020-Package_Requirements.docx` contains package-by-package sections for many packages but no section keyed to PKG-022 / 5kV SWITCHGEAR EQUIPMENT. No source vendor-document table rows for this package are locally accessible. | `_Sources/26020-Package_Requirements.docx` table of contents; `_REFERENCES.md` |
| Required vendor document set | TBD. No package-specific vendor-document requirements are stated for PKG-022 in accessible source materials. ASSUMPTION: the vendor document set will follow the project's standard EPC vendor data requirements (e.g., quality plan, datasheets, drawings, manuals, test certificates, spare parts list, FAT report) once those are confirmed by EPC vendor data requirements documentation. | Source gap; `_Sources/26020-Package_Requirements.docx` |
| Package equipment scope (context) | The package supplies "5kV SWITCHGEAR EQUIPMENT" for the West Doe Combined facility, WBS 01, Electrical discipline. The DBM Deepcut design basis identifies medium-voltage cabling rated 5 kV with 100% insulation for 4.160 kV services but does not contain a 5kV-rated switchgear assembly description. The technical content, voltage class, and configuration of the PKG-022 equipment as physically deployed are TBD pending confirmation against project source materials. | Workbook Packages row 24; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, medium-voltage cable and switchgear paragraphs |
| Coordination mode | DECLARED. No upstream or downstream dependencies were declared during PREPARATION. | `_DEPENDENCIES.md` |

## Conditions

| Interface / condition | Datasheet requirement basis | Source |
|---|---|---|
| Electrical Power | Interface fact applies to PKG-022; vendor turnover documentation must include drawings, schedules, schematics, and test records supporting this interface. | Workbook Packages row 24; `INTERFACE_REGISTER.csv` `IFC-FAD0C5C924` |
| Grounding / Bonding | Interface fact applies to PKG-022; vendor turnover documentation must include grounding/bonding details and ground-grid connection drawings supporting this interface. | Workbook Packages row 24; `INTERFACE_REGISTER.csv` `IFC-291807A33B` |
| I&C / Control Cabling | Interface fact applies to PKG-022; vendor turnover documentation must include control schematics, wiring diagrams, and termination details supporting this interface. | Workbook Packages row 24; `INTERFACE_REGISTER.csv` `IFC-FFD6E87354` |
| Communications / Network | Interface fact applies to PKG-022; vendor turnover documentation must include communications/protocol descriptions and network drawings supporting this interface. | Workbook Packages row 24; `INTERFACE_REGISTER.csv` `IFC-652BE03197` |
| Maintenance Access | Interface fact applies to PKG-022; vendor turnover documentation must include maintenance access envelopes and clearance drawings supporting this interface. | Workbook Packages row 24; `INTERFACE_REGISTER.csv` `IFC-53BEFBC3CA` |
| Structural / Foundations / Supports | Interface fact applies to PKG-022; vendor turnover documentation must include loading data and anchorage/foundation drawings supporting this interface. | Workbook Packages row 24; `INTERFACE_REGISTER.csv` `IFC-ED54C3FD1A` |
| Package-specific exclusions | TBD; no package-specific exclusions are stated in source materials. | `PACKAGE_REGISTER.csv` row `PKG-022` |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Vendor documentation responsibility | Package Vendor produces and owns the vendor document register, submittals, source-required vendor documentation, and turnover records for PKG-022. | `DELIVERABLE_REGISTER.csv` row `DEL-022-05`; `PACKAGE_REGISTER.csv` row `PKG-022` |
| Integrator review responsibility | EPC Integrator performs interface and integration review of the vendor document turnover set. | `DELIVERABLE_REGISTER.csv` row `DEL-022-05` |
| Source vendor-document basis | TBD. No PKG-022 / 5kV switchgear vendor-document basis is present in accessible source materials (`26020-Package_Requirements.docx`, DBM Deepcut). | `_Sources/26020-Package_Requirements.docx`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |
| Detailed vendor-document gap | The artifact register records the current state explicitly as a Vendor Documentation Gap. | `ARTIFACT_REGISTER.csv` row `ART-E34A2C824B` |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `_DEPENDENCIES.md`, DECLARED coordination state.
- `DELIVERABLE_REGISTER.csv`, row `DEL-022-05_vendor-document-turnover-package`.
- `PACKAGE_REGISTER.csv`, row `PKG-022`.
- `ARTIFACT_REGISTER.csv`, row `ART-E34A2C824B`.
- `INTERFACE_REGISTER.csv`, rows `IFC-FAD0C5C924`, `IFC-291807A33B`, `IFC-FFD6E87354`, `IFC-652BE03197`, `IFC-53BEFBC3CA`, `IFC-ED54C3FD1A`.
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-022-05_vendor-document-turnover-package`.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 24.
- `_Sources/26020-Package_Requirements.docx`, searched for PKG-022 / 5kV switchgear section; no package match found.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, medium-voltage and switchgear paragraphs (context only; no 5kV switchgear assembly description).
