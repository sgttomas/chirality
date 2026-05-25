# Datasheet: DEL-034-06_epc-vendor-package-review-and-acceptance

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-034-06_epc-vendor-package-review-and-acceptance` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Deliverable name | EPC Vendor Package Review and Acceptance | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-034` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | 600V ELECTRICAL BUILDING (820-2) | Workbook Packages row 36; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 34 / row 36 | Workbook Packages row 36; `PACKAGE_REGISTER.csv` |
| WBS | 02 | Workbook Packages row 36; `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-02-30-025 | Workbook Packages row 36; `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | Workbook Packages row 36; `_CONTEXT.md` |
| Deliverable type | EPC Vendor Package Acceptance | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | EPC Integrator (lead) with Package Vendor input | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Acceptance basis | Review and integration acceptance of the vendor package against the EPC Scope of Work (`DEL-034-01`), Package Datasheet (`DEL-034-02`), and Construction Work Package (`DEL-034-03`). | `DELIVERABLE_REGISTER.csv` row `DEL-034-06`; deliverable description |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; EPC Integrator owns facility-level integration, interfaces, tie-ins, constructability, procurement/construction coordination. | `PACKAGE_REGISTER.csv` row `PKG-034` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Acceptance scope | EPC Integrator review, integration acceptance, and handoff-readiness evidence for the `PKG-034` 600V electrical building vendor package. | `DELIVERABLE_REGISTER.csv` row `DEL-034-06` |
| Upstream EPC anchors | EPC Scope of Work (`DEL-034-01`); Package Datasheet (`DEL-034-02`); Construction Work Package (`DEL-034-03`). | `DELIVERABLE_REGISTER.csv` rows `DEL-034-01`, `DEL-034-02`, `DEL-034-03` |
| Vendor inputs reviewed | Vendor Engineered Equipment Package (`DEL-034-04`); Vendor Document Turnover Package (`DEL-034-05`). | `DELIVERABLE_REGISTER.csv` rows `DEL-034-04`, `DEL-034-05` |
| Building service basis | 600 V, 3 phase, 3 wire, 60 Hz HRG (5 A continuous resistor) low-voltage service supporting motors, lighting transformers, building heaters, and UPS larger than 10 kVA. Application to building "820-2" shall be confirmed against detailed design. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, low-voltage service row |
| Housed equipment basis | Electrical buildings shall house MCCs, switchgear, distribution equipment, and associated HVAC/ventilation systems; 600V MCCs use electronic motor overload relays with local control stations and may include 600V VFDs in the lineup. Package-specific equipment list is TBD pending vendor data. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, electrical buildings paragraph; `600V MCC and Standby Power` |
| Standby power interface | Emergency power is supplied at the 600V MCC level via LV standby natural-gas generators with transfer switch; transfer switch type, emergency bus configuration, generator count, rating, and load-shedding/critical-load list remain TBD. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, standby power paragraph |
| Building naming reconciliation | TBD. Workbook row 36 names the package "600V ELECTRICAL BUILDING (820-2)"; the DBM Deepcut building inventory enumerates 600V buildings as 840-1, 850-1, and 860-1, with no explicit "820-2" entry. Mapping of "820-2" to a DBM-listed 600V building is not source-confirmed. | Workbook Packages row 36; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings inventory table |

## Conditions

| Interface / condition | Datasheet requirement basis | Source |
|---|---|---|
| Utility Piping | Interface fact applies to `PKG-034` and shall be confirmed by EPC review of the vendor package interface register. | Workbook Packages row 36; `INTERFACE_REGISTER.csv` `IFC-FC0F34096E` |
| Drain / Containment | Interface fact applies to `PKG-034` and shall be confirmed by EPC review. | Workbook Packages row 36; `INTERFACE_REGISTER.csv` `IFC-E270A479B8` |
| Electrical Power | Interface fact applies to `PKG-034` and shall be confirmed by EPC review of feeder/tie-in arrangement. | Workbook Packages row 36; `INTERFACE_REGISTER.csv` `IFC-0E87B7BCE6` |
| Grounding / Bonding | Interface fact applies to `PKG-034` and shall be confirmed by EPC review of vendor grounding interfaces against the facility grounding basis. | Workbook Packages row 36; `INTERFACE_REGISTER.csv` `IFC-46D2497CB7` |
| Area / Exterior Lighting | Interface fact applies to `PKG-034` and shall be confirmed by EPC review. | Workbook Packages row 36; `INTERFACE_REGISTER.csv` `IFC-63A70A25C3` |
| I&C / Control Cabling | Interface fact applies to `PKG-034` and shall be confirmed by EPC review of cable separation and routing. | Workbook Packages row 36; `INTERFACE_REGISTER.csv` `IFC-5EA9F4B39F` |
| Communications / Network | Interface fact applies to `PKG-034` and shall be confirmed by EPC review. | Workbook Packages row 36; `INTERFACE_REGISTER.csv` `IFC-1333B6962E` |
| Building HVAC / Services | Interface fact applies to `PKG-034`; electrical-building HVAC basis applies and shall be confirmed by EPC review. | Workbook Packages row 36; `INTERFACE_REGISTER.csv` `IFC-DA391B1AF1`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, building heater/HVAC paragraph |
| Fire & Gas / Safety Systems | Interface fact applies to `PKG-034` and shall be confirmed by EPC review. | Workbook Packages row 36; `INTERFACE_REGISTER.csv` `IFC-94BF4E7C7C` |
| Maintenance Access | Interface fact applies to `PKG-034`; cable tray and conduit routing shall not interfere with maintenance access and this shall be verified during EPC review. | Workbook Packages row 36; `INTERFACE_REGISTER.csv` `IFC-CAE509DDFA`; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, cable tray and conduit paragraphs |
| Grading / Site Drainage / Spill Containment | Interface fact applies to `PKG-034` and shall be confirmed by EPC review. | Workbook Packages row 36; `INTERFACE_REGISTER.csv` `IFC-7BD20E62E6` |
| Structural / Foundations / Supports | Interface fact applies to `PKG-034`; electrical-building foundations and anchorage require equipment-specific checks against geotechnical, snow/wind/seismic, frost, vibration, and maintenance basis. | Workbook Packages row 36; `INTERFACE_REGISTER.csv` `IFC-EC6DF8B5D4`; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, foundations paragraph |
| Area classification | Electrical buildings shall be located in general purpose areas for convenient power distribution; remote distribution centres in unclassified locations where practical. Building "820-2" specific area classification shall be confirmed by EPC review. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, area classification and electrical buildings paragraphs |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Vendor scope under review | Package Vendor engineering, package design, vendor documentation, and the physical equipment package. | `PACKAGE_REGISTER.csv` row `PKG-034`; `DELIVERABLE_REGISTER.csv` rows `DEL-034-04`, `DEL-034-05` |
| EPC scope of acceptance | Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-034` |
| Required review artifacts | Vendor document review and comment log (`ART-F631454830`); vendor package acceptance and turnover checklist (`ART-8E586DD59F`); factory/shop test and inspection evidence (`ART-853E05D6CB`). | `ARTIFACT_REGISTER.csv` rows for `DEL-034-06` |
| Acceptance verification basis | Acceptance is evaluated against the EPC Scope of Work, EPC Package Datasheet, and EPC Construction Work Package. | `DELIVERABLE_REGISTER.csv` row `DEL-034-06` description |
| Factory/shop test scope | Expected package test/inspection evidence; detailed requirements are source-specific where available and are TBD without vendor or detailed-design test specifications. | `ARTIFACT_REGISTER.csv` `ART-853E05D6CB`; no package-specific test specification found in accessible sources |
| Turnover evidence basis | Construction-facing interface, tie-in, inspection, and turnover evidence for the approved package; detailed turnover content for `PKG-034` is TBD until the Construction Work Package and vendor turnover register are issued. | `ARTIFACT_REGISTER.csv` `ART-EEB94D0E0D` (cross-reference to `DEL-034-03`); `ART-8E586DD59F` |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, rows `DEL-034-01` through `DEL-034-06`.
- `PACKAGE_REGISTER.csv`, row `PKG-034`.
- `ARTIFACT_REGISTER.csv`, rows for `DEL-034-06` (and cross-references for `DEL-034-02`, `DEL-034-03`).
- `INTERFACE_REGISTER.csv`, rows for `PKG-034` (12 interface facts).
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows mapping `OBJ-002`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` to `DEL-034-06`.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 36.
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, low-voltage service, 600V MCC and standby power, electrical buildings, foundations, and cable tray/conduit source slices.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical building inventory, area classification, and electrical design basis source slices.
- `_Sources/26020-Package_Requirements.docx`, searched for package-specific 600V electrical building review/acceptance content; no PKG-034 match found.
