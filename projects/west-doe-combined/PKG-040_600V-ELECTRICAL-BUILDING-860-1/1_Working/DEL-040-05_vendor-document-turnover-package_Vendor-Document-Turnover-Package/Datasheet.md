# Datasheet: DEL-040-05_vendor-document-turnover-package

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-040-05_vendor-document-turnover-package` | `_CONTEXT.md` |
| Deliverable name | Vendor Document Turnover Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-040` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | 600V ELECTRICAL BUILDING (860-1) | Workbook Packages row 42; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 40 / row 42 | Workbook Packages row 42; `PACKAGE_REGISTER.csv` |
| WBS | 01 | Workbook Packages row 42; `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-01-30-031 | Workbook Packages row 42; `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | Workbook Packages row 42; `_CONTEXT.md` |
| Deliverable type | Vendor Document Turnover | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | Package Vendor (vendor documentation) with EPC Integrator interface/integration review | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; EPC Integrator owns integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-040` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Package class | Vendor-owned Electrical package | `PACKAGE_REGISTER.csv` row `PKG-040` |
| Package function | 600V Electrical Building (860-1), identified in DBM as the "600V General Area / Tank Farm Electrical Building" housing 600V general-area/tank-farm electrical distribution and associated services. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2816 (building list) and line 2925 (4.16 kV/600 V General Area/Tank Farm/Process Electrical Building feed) |
| Turnover content basis | Electrical package deliverables shall include datasheets, equipment ratings, load and short-circuit/coordination/arc-flash study inputs, area-classification basis, grounding/bonding details, cable and raceway design, lighting/receptacle and heat-tracing details, building HVAC coordination, maintenance access, shipped-loose item lists, and the vendor document register, derived from the SEC-12 Electrical Basis scope and the project electrical specifications table. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-12 §"Discipline Scope" (line 2860); §"Governing Codes, Standards, Specifications, and Studies" (Table 12-1, lines 2872–2892); electrical studies table (lines 2895–2901) |
| Covered Scope of Work item | `SOW-0041` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Supported objectives | `OBJ-001`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv`; `OBJECTIVE_DELIVERABLE_MAP.csv` (ASSUMPTION: package-grouping heuristic; `OBJECTIVE_ASSOCIATION_MODE=PACKAGE_HEURISTIC`) |
| Detailed vendor document list | `TBD`. Detailed vendor-document requirements (per-document numbering, content, submittal format) are not present in the accessible source material for this package. | `ARTIFACT_REGISTER.csv` row `ART-EF224E6F34` ("TBD vendor document register", Vendor Documentation Gap Evidence) |
| Turnover record format | `TBD`. No package-specific turnover record format is defined in accessible source slices; no PKG-040 match was found in `_Sources/26020-Package_Requirements.docx` accessible to this run. | Source gap; `_REFERENCES.md`; `ARTIFACT_REGISTER.csv` row `ART-EF224E6F34` |

## Conditions

| Interface / condition | Datasheet requirement basis | Source |
|---|---|---|
| Utility Piping | Interface fact applies to PKG-040; vendor documents shall include applicable utility tie-in records. | Workbook Packages row 42; `INTERFACE_REGISTER.csv` `IFC-C7A10165E0` |
| Drain / Containment | Interface fact applies to PKG-040; vendor documents shall include drain/containment design and tie-in records. | Workbook Packages row 42; `INTERFACE_REGISTER.csv` `IFC-84254E4D74` |
| Electrical Power | Interface fact applies to PKG-040; vendor documents shall include feeder, distribution, and protective device data. | Workbook Packages row 42; `INTERFACE_REGISTER.csv` `IFC-01418C7B46` |
| Grounding / Bonding | Interface fact applies to PKG-040; vendor documents shall include grounding/bonding details supporting building tie-in to plant ground grid. | Workbook Packages row 42; `INTERFACE_REGISTER.csv` `IFC-1AFD94C7C5` |
| Area / Exterior Lighting | Interface fact applies to PKG-040. | Workbook Packages row 42; `INTERFACE_REGISTER.csv` `IFC-31FBC53269` |
| I&C / Control Cabling | Interface fact applies to PKG-040; vendor documents shall include control cable schedules and termination details. | Workbook Packages row 42; `INTERFACE_REGISTER.csv` `IFC-4924815E92` |
| Communications / Network | Interface fact applies to PKG-040. | Workbook Packages row 42; `INTERFACE_REGISTER.csv` `IFC-07F9E1739B` |
| Building HVAC / Services | Interface fact applies to PKG-040; vendor documents shall include HVAC/ventilation design coordinated with electrical heat load. | Workbook Packages row 42; `INTERFACE_REGISTER.csv` `IFC-E5C808A2AF` |
| Fire & Gas / Safety Systems | Interface fact applies to PKG-040. | Workbook Packages row 42; `INTERFACE_REGISTER.csv` `IFC-AB1228ED22` |
| Maintenance Access | Interface fact applies to PKG-040; vendor documents shall preserve maintenance access requirements. | Workbook Packages row 42; `INTERFACE_REGISTER.csv` `IFC-DD57C5C1B0` |
| Grading / Site Drainage / Spill Containment | Interface fact applies to PKG-040. | Workbook Packages row 42; `INTERFACE_REGISTER.csv` `IFC-CB9A638F41` |
| Structural / Foundations / Supports | Interface fact applies to PKG-040; vendor documents shall include building structural and foundation design coordination. | Workbook Packages row 42; `INTERFACE_REGISTER.csv` `IFC-327D21980E` |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Vendor document authorship | Package Vendor authors and submits vendor documents and the turnover package. | `PACKAGE_REGISTER.csv` row `PKG-040`; `_CONTEXT.md` |
| EPC interface/integration review | EPC Integrator reviews vendor documents for facility integration, interfaces, tie-ins, and constructability. | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row `PKG-040` |
| Anticipated artifact set | Vendor document register; vendor document submittals; source vendor document table rows as artifacts where available; turnover records. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-040-05` |
| Governing electrical specifications | The project electrical and instrumentation specifications listed in DBM Table 12-1 (ELC-QAS-000001-001 through ELC-QAS-000018-001) govern electrical distribution design and electrical equipment procurement basis; ELC-QAS-000003-001 ("Electrical Requirements for Packaged Equipment") is directly applicable to vendor-packaged scope. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Table 12-1 (lines 2872–2892) |
| Source documentation gap | Detailed vendor-document requirements (numbering, workflow, format, acceptance criteria) are not present in current source material for this package; an artifact gap is recorded. | `ARTIFACT_REGISTER.csv` row `ART-EF224E6F34` |
| Source documents searched for package-specific requirements | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (SEC-12 Electrical Basis), `_Sources/26020-Packages_Interfaces_4_export.xlsx` (Packages sheet row 42), and `_Sources/26020-Package_Requirements.docx`; no PKG-040 vendor-document-detail slice was accessible to this run. | `_REFERENCES.md`; source file listing |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `DELIVERABLE_REGISTER.csv`, row `DEL-040-05_vendor-document-turnover-package`.
- `PACKAGE_REGISTER.csv`, row `PKG-040`.
- `ARTIFACT_REGISTER.csv`, rows for `DEL-040-05_vendor-document-turnover-package` (including `ART-EF224E6F34`).
- `INTERFACE_REGISTER.csv`, rows for `PKG-040` (twelve interface facts).
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-040-05_vendor-document-turnover-package`.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 42.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-12 Electrical Basis (Discipline Scope line 2860; governing codes and Table 12-1 lines 2864–2892; electrical studies lines 2895–2901; building list line 2816; power distribution line 2925).
- `_Sources/26020-Package_Requirements.docx`, searched for package-specific vendor document content; no PKG-040 match accessible.
