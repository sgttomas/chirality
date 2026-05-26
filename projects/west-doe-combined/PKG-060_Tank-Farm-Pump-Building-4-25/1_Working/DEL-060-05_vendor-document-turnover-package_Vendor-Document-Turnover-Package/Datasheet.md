# Datasheet: DEL-060-05_vendor-document-turnover-package

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-060-05_vendor-document-turnover-package` | `_CONTEXT.md` |
| Deliverable name | Vendor Document Turnover Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-060` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | Tank Farm Pump Building 4-25 | Workbook Packages row 85; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 60 / row 85 | Workbook Packages row 85; `PACKAGE_REGISTER.csv` |
| WBS | 01 | `PACKAGE_REGISTER.csv` row `PKG-060` |
| CoA tracking number | 26020-01-18-001 | `PACKAGE_REGISTER.csv` row `PKG-060` |
| Discipline | Mechanical | Workbook Packages row 85; `_CONTEXT.md` |
| Deliverable type | Vendor Document Turnover | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | Package Vendor (vendor documentation) with EPC Integrator interface/integration review | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; EPC Integrator owns integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-060` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Package class | Vendor-owned Mechanical pump-building package | `PACKAGE_REGISTER.csv` row `PKG-060` |
| Package function | Tank Farm Pump Building 4-25 housing two water transfer pumps/motors, two condensate transfer pumps/motors, one condensate recycle pump/motor with strainer, and two process water transfer pumps/motors. | `PACKAGE_REGISTER.csv` row `PKG-060` (DeliverableContent column); `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §"Pumps and Pump Buildings" lines 2555, 2618-2622 (Tank Farm Pump Building 2 pump list) |
| Process duties | Water Transfer Pumps (2x): pull water from produced water tanks and push it to the 3-25 compressor station. Condensate Transfer Pumps (2x): transfer condensate product to downstream liquids hub; designed for 350 kPad (50 psid) differential to reach the hub. Condensate Recycle Pump (1x): recycles condensate from the produced water tank condensate skim. | `PACKAGE_REGISTER.csv` row `PKG-060` (DeliverableContent column) |
| Turnover content basis | Vendor document register, vendor document submittals, source vendor document table rows as artifacts where available, and turnover records, as defined by the artifact register for this deliverable. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-060-05`; `ARTIFACT_REGISTER.csv` rows for `DEL-060-05` |
| Covered Scope of Work items | `SOW-0189`, `SOW-0190`, `SOW-0191`, `SOW-0192` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Supported objectives | `OBJ-001`, `OBJ-003`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` (ASSUMPTION: package-grouping heuristic; PACKAGE_HEURISTIC mode) |
| Vendor document register basis | The register enumerates the vendor document categories and items recorded in `ARTIFACT_REGISTER.csv` for `DEL-060-05`. | `ARTIFACT_REGISTER.csv` rows for `DEL-060-05` (110+ artifact rows across vendor-documentation categories) |
| Detailed numbering scheme | `TBD` — no package-specific vendor document numbering convention is present in accessible source slices. | Source gap; `26020-Package_Requirements.docx package heading 15` text not extracted to markdown |
| Turnover record format | `TBD` — no package-specific turnover record format is defined in accessible source slices. | Source gap |

## Conditions

| Interface / condition | Datasheet requirement basis | Source |
|---|---|---|
| Process Piping | Interface fact applies to PKG-060; vendor documents shall include P&IDs, piping line list, isometrics, tie-in list, MTOs, and as-builts. | Workbook Packages row 85; `INTERFACE_REGISTER.csv` `IFC-40CB9DE2A3`; `ARTIFACT_REGISTER.csv` Process piping interfaces category |
| Utility Piping | Interface fact applies to PKG-060; vendor documents shall include the utility summary / utility consumption report. | Workbook Packages row 85; `INTERFACE_REGISTER.csv` `IFC-69B1E2DF22`; `ARTIFACT_REGISTER.csv` Utility piping interfaces category |
| Relief / Flare / Vent | Interface fact applies to PKG-060; vendor documents shall include relief and flare design basis, PSV sizing calculations, relief valve data sheets, flare load summary, and blowdown study. | Workbook Packages row 85; `INTERFACE_REGISTER.csv` `IFC-89861F9A53`; `ARTIFACT_REGISTER.csv` Relief / flare / vent design category |
| Drain / Containment | Interface fact applies to PKG-060; vendor documents shall include process sewer/closed drain design basis and bund/dike/secondary containment drawings. | Workbook Packages row 85; `INTERFACE_REGISTER.csv` `IFC-1F5DAD08E7`; `ARTIFACT_REGISTER.csv` Drainage / containment interfaces category |
| Electrical Power | Interface fact applies to PKG-060; vendor documents shall include electrical load list, SLDs, cable schedules, layouts, equipment data sheets, and energization records. | Workbook Packages row 85; `INTERFACE_REGISTER.csv` `IFC-E2ACDBC3AC`; `ARTIFACT_REGISTER.csv` Electrical/grounding category |
| EHT (Electrical Heat Tracing) | Interface fact applies to PKG-060; vendor documents shall include the EHT design package and piping insulation/heat tracing schedule. | Workbook Packages row 85; `INTERFACE_REGISTER.csv` `IFC-10732C110E`; `ARTIFACT_REGISTER.csv` Electrical heat tracing artifacts |
| Grounding / Bonding | Interface fact applies to PKG-060; vendor documents shall include grounding/earthing study and bonding layout drawings. | Workbook Packages row 85; `INTERFACE_REGISTER.csv` `IFC-897D5300B9`; `ARTIFACT_REGISTER.csv` Electrical/grounding category |
| Area / Exterior Lighting | Interface fact applies to PKG-060; vendor documents shall include lighting layout drawings. | Workbook Packages row 85; `INTERFACE_REGISTER.csv` `IFC-30393FE7EE`; `ARTIFACT_REGISTER.csv` `ART-0A3ED3C045` |
| Cathodic Protection | Interface fact applies to PKG-060; vendor documents shall preserve cathodic protection design basis for buried/wetted package components. | Workbook Packages row 85; `INTERFACE_REGISTER.csv` `IFC-E715EB5D71`; specific CP artifact not enumerated in `ARTIFACT_REGISTER.csv` (location TBD) |
| I&C / Control Cabling | Interface fact applies to PKG-060; vendor documents shall include instrument index, data sheets, loop diagrams, hook-up drawings, cable schedules, I/O list, cause-and-effect matrix, control narrative, and Package Vendor Interface Specification. | Workbook Packages row 85; `INTERFACE_REGISTER.csv` `IFC-222CE41830`; `ARTIFACT_REGISTER.csv` Instrumentation and controls interfaces category |
| Building HVAC / Services | Interface fact applies to PKG-060; vendor documents shall include ventilation / process safety equipment inputs and building siting / occupied building risk assessment. | Workbook Packages row 85; `INTERFACE_REGISTER.csv` `IFC-AE5871A3F7`; `ARTIFACT_REGISTER.csv` Building / HVAC / code interfaces category |
| Fire & Gas / Safety Systems | Interface fact applies to PKG-060; vendor documents shall include fire and gas philosophy, mapping study, detector layouts, SIL determination, SRS, supplier SIL documentation, and emergency response plan inputs. | Workbook Packages row 85; `INTERFACE_REGISTER.csv` `IFC-0A19AB343B`; `ARTIFACT_REGISTER.csv` Fire and gas / technical safety interfaces category |
| Maintenance Access | Interface fact applies to PKG-060; vendor documents shall preserve maintenance access provisions (lifting/handling studies, platform/access drawings). | Workbook Packages row 85; `INTERFACE_REGISTER.csv` `IFC-0296CFA39E`; `ARTIFACT_REGISTER.csv` rows `ART-88C54F4EBB`, `ART-57485C85B5` |
| Structural / Foundations / Supports | Interface fact applies to PKG-060; vendor documents shall include structural design basis, calculation package, foundation calculations and drawings, anchor bolt drawings, and structural MTO. | Workbook Packages row 85; `INTERFACE_REGISTER.csv` `IFC-CAC59EDFA2`; `ARTIFACT_REGISTER.csv` Structural / access category |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Vendor document authorship | Package Vendor authors and submits all vendor documents and the turnover package for the Tank Farm Pump Building 4-25. | `PACKAGE_REGISTER.csv` row `PKG-060`; `_CONTEXT.md` |
| EPC interface/integration review | EPC Integrator reviews vendor documents for facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row `PKG-060`; `DELIVERABLE_REGISTER.csv` row `DEL-060-06` |
| Anticipated artifact set | Vendor document register; vendor document submittals; source vendor document table rows as artifacts where available; turnover records. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-060-05` |
| Vendor document categories | Vendor documentation register; core vendor documents; core package engineering; rotating equipment / pumps; relief / flare / vent design; process piping interfaces; utility piping interfaces; drainage / containment interfaces; electrical and grounding; instrumentation and controls interfaces; building / HVAC / code interfaces; fire and gas / technical safety interfaces; structural / access. | `ARTIFACT_REGISTER.csv` rows for `DEL-060-05` (category headers) |
| Source documents searched for package-specific requirements | `26020-Package_Requirements.docx` package heading 15 (not extracted to markdown for this run); `26020-Packages_Interfaces_4_export.xlsx` Packages sheet row 85 (used via Gate 7 registers); `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` for pump-building scope. | `_REFERENCES.md`; `_Sources/` listing |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers and Shared Source Root.
- `DELIVERABLE_REGISTER.csv`, row `DEL-060-05_vendor-document-turnover-package`.
- `PACKAGE_REGISTER.csv`, row `PKG-060`.
- `ARTIFACT_REGISTER.csv`, rows tied to `DEL-060-05_vendor-document-turnover-package`.
- `INTERFACE_REGISTER.csv`, rows for `PKG-060` (fourteen interface facts).
- `OBJECTIVE_DELIVERABLE_MAP.csv` (package-grouping heuristic; ASSUMPTION).
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 85.
- `_Sources/26020-Package_Requirements.docx`, package heading 15 (text not extracted to markdown for this run; cited as source of detailed vendor document requirements).
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Tank Farm Pump Building 2 entries (lines 2555, 2618-2622) and surrounding pump-building scope.
