# Datasheet: DEL-035-06_epc-vendor-package-review-and-acceptance

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-035-06_epc-vendor-package-review-and-acceptance` | `_CONTEXT.md` |
| Deliverable name | EPC Vendor Package Review and Acceptance | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-035` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | 13.8kV SWITCHGEAR ELECTRICAL BUILDING (810-1) | Workbook Packages row 37; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 35 / row 37 | `PACKAGE_REGISTER.csv` |
| WBS | 01 | `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-01-30-026 | `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | `PACKAGE_REGISTER.csv`; `_CONTEXT.md` |
| Deliverable type | EPC Vendor Package Acceptance | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | EPC Integrator (lead) with Package Vendor input | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. EPC Integrator owns integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-035` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Acceptance subject | The vendor-delivered 13.8 kV switchgear electrical building package (Building 810-1) and its vendor documentation, factory testing, and inspection evidence. | `PACKAGE_REGISTER.csv` row `PKG-035`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Electrical Buildings section |
| Acceptance purpose | Establish EPC Integrator evidence that the vendor-engineered switchgear/electrical building package satisfies the EPC Scope of Work, Package Datasheet, and Construction Work Package, and is ready for integration and turnover. | `DELIVERABLE_REGISTER.csv` description; `SCOPE_LEDGER.csv` `SOW-0036` |
| Acceptance scope items | `SOW-0036` (carry the vendor-responsible Electrical package '13.8kV SWITCHGEAR ELECTRICAL BUILDING (810-1)' for WBS 01 with vendor engineering/design/equipment and EPC facility integration). | `SCOPE_LEDGER.csv` `SOW-0036`; `_CONTEXT.md` |
| Anticipated artifacts | Vendor document review log; package acceptance checklist; test/inspection evidence; turnover evidence. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Vendor review artifact | `ART-AA841F7CA1` — vendor document review and comment log (EPC Vendor Review Evidence). | `ARTIFACT_REGISTER.csv` |
| Acceptance/turnover artifact | `ART-72A172E45B` — vendor package acceptance and turnover checklist (EPC Acceptance Evidence). | `ARTIFACT_REGISTER.csv` |
| Test/inspection artifact | `ART-7F4CFC552C` — factory/shop test and inspection evidence (Vendor Test Evidence). | `ARTIFACT_REGISTER.csv` |
| Package function (integration basis) | 13.8 kV main switchgear distributes plant power radially through step-down transformers to downstream medium- and low-voltage electrical buildings; the 13.8 kV bus shall be sized for the full facility scope. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Electrical Basis (`13.8 kV switchgear shall be designed, purchased, and installed as the plant main power distribution center`) |
| Building type basis | Building 810-1 is a shop-fabricated, prefabricated, modular electrical building housing the 13.8 kV main switchgear and supporting equipment as required by detailed design. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Building Strategy table (`810-1 13.8kV Switchgear Electrical Building`, Shop); Electrical Buildings section |
| Supports facility objectives | OBJ-001 (04-25 facility scope), OBJ-004 (vendor/EPC responsibility split), OBJ-005 (electrical infrastructure), OBJ-006 (controls/instrumentation/F&G interfaces), OBJ-007 (utilities/HVAC/building services), OBJ-008 (civil/structural/foundation), OBJ-009 (safety/fire-gas), OBJ-010 (operability/turnover/vendor documentation). | `OBJECTIVE_DELIVERABLE_MAP.csv`; `OBJECTIVE_REGISTER.csv` |

## Conditions

| Interface / condition | Acceptance basis | Source |
|---|---|---|
| Utility Piping | Interface fact `IFC-C8A7133D59` applies to PKG-035; vendor package shall demonstrate interface boundary closure for utility piping connections to the building. | `INTERFACE_REGISTER.csv` `IFC-C8A7133D59` |
| Drain / Containment | Interface fact `IFC-231DB0CBFA` applies to PKG-035; building floor drains and containment provisions shall be verified at acceptance. | `INTERFACE_REGISTER.csv` `IFC-231DB0CBFA` |
| Electrical Power | Interface fact `IFC-A5EF521315` applies to PKG-035; the package shall provide the 13.8 kV bus and feeders to downstream electrical buildings per facility distribution basis. | `INTERFACE_REGISTER.csv` `IFC-A5EF521315`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Electrical Basis (radial distribution from 13.8 kV switchgear) |
| Grounding / Bonding | Interface fact `IFC-C11BBF56CD` applies to PKG-035; major electrical equipment shall be directly connected to the ground grid at two points; ground wells at the electrical building shall be provided for maintenance/testing. | `INTERFACE_REGISTER.csv` `IFC-C11BBF56CD`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Grounding and Bonding |
| Area / Exterior Lighting | Interface fact `IFC-EB2FA7BDE6` applies to PKG-035; exterior lighting interface shall be verified at acceptance. | `INTERFACE_REGISTER.csv` `IFC-EB2FA7BDE6` |
| I&C / Control Cabling | Interface fact `IFC-9214AEAF28` applies to PKG-035; control cabling boundary, terminations, and segregation shall be evidenced. | `INTERFACE_REGISTER.csv` `IFC-9214AEAF28` |
| Communications / Network | Interface fact `IFC-00317770B3` applies to PKG-035; network rack provisions and communications boundary shall be evidenced. | `INTERFACE_REGISTER.csv` `IFC-00317770B3`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Electrical Buildings (network racks) |
| Building HVAC / Services | Interface fact `IFC-73CF283A27` applies to PKG-035; HVAC shall be n+1 sized so cooling tolerates failure or maintenance of one unit without affecting heating/cooling. | `INTERFACE_REGISTER.csv` `IFC-73CF283A27`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Electrical Buildings (n+1 HVAC) |
| Fire & Gas / Safety Systems | Interface fact `IFC-C00E60F032` applies to PKG-035; F&G detection/alarm interfaces to the building shall be evidenced. | `INTERFACE_REGISTER.csv` `IFC-C00E60F032` |
| Maintenance Access | Interface fact `IFC-A3B2DADC44` applies to PKG-035; equipment doors shall be sized for, or include removable transom sections to allow, removal of the largest equipment; cable tray/conduit routing shall not interfere with maintenance access. | `INTERFACE_REGISTER.csv` `IFC-A3B2DADC44`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Electrical Buildings; cable tray paragraphs |
| Grading / Site Drainage / Spill Containment | Interface fact `IFC-589CAC7BC6` applies to PKG-035; site grading/drainage at the building footprint shall be evidenced. | `INTERFACE_REGISTER.csv` `IFC-589CAC7BC6` |
| Structural / Foundations / Supports | Interface fact `IFC-A5DBFBF436` applies to PKG-035; building shall be elevated and installed on piles per electrical-building basis. | `INTERFACE_REGISTER.csv` `IFC-A5DBFBF436`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Electrical Buildings (elevated on piles, bottom entry) |
| Area classification | Electrical buildings shall be located in general purpose areas for convenient power distribution. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Area Classification paragraph |
| Cable entry | Buildings shall be designed for bottom entry of incoming and outgoing power cables. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Electrical Buildings |

## Construction

| Acceptance package element | Vendor evidence required | Source / status |
|---|---|---|
| Vendor document review log (`ART-AA841F7CA1`) | EPC review record listing each vendor document submission, EPC reviewer, comment disposition, and revision closure status. | `ARTIFACT_REGISTER.csv`; `OBJECTIVE_REGISTER.csv` OBJ-010 (vendor documentation register) |
| Package acceptance/turnover checklist (`ART-72A172E45B`) | EPC-authored checklist evidencing satisfaction of EPC Scope of Work, Package Datasheet, and Construction Work Package items for PKG-035, with sign-off lines for the EPC Integrator and Package Vendor. | `ARTIFACT_REGISTER.csv`; `SCOPE_LEDGER.csv` `SOW-0036` |
| Factory/shop test and inspection evidence (`ART-7F4CFC552C`) | Vendor FAT records, shop inspection reports, and witness/hold-point evidence for the shop-built 810-1 building and its 13.8 kV switchgear. Detailed test scope and acceptance criteria are vendor-specification driven; location TBD pending `26020-Package_Requirements.docx` slice. | `ARTIFACT_REGISTER.csv`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Building Strategy table (Shop) |
| Interface closure evidence | Per-interface closure record covering each of the twelve PKG-035 interface facts above, citing the EPC Interface Requirements Evidence carried in DEL-035-02. | `INTERFACE_REGISTER.csv` rows for PKG-035 |
| Standards conformance evidence | Vendor statement of conformance to the electrical design basis: CSA C22.1-21 Canadian Electrical Code; applicable BC provincial/local codes; CSA, API, IEEE, ISA, NEMA, WorkSafeBC, Technical Safety BC, and BCER as applicable. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Electrical Basis (standards paragraph) |
| Outstanding/open-item closure log | Record of vendor-side TBD/open items at acceptance time and the agreed closure path, supporting OBJ-010 controlled open-item closure. | `OBJECTIVE_REGISTER.csv` OBJ-010 |

## References

- `PACKAGE_REGISTER.csv` row `PKG-035` (Gate 7 snapshot).
- `DELIVERABLE_REGISTER.csv` row `DEL-035-06_epc-vendor-package-review-and-acceptance` (Gate 7 snapshot).
- `ARTIFACT_REGISTER.csv` rows `ART-AA841F7CA1`, `ART-72A172E45B`, `ART-7F4CFC552C` (Gate 7 snapshot).
- `INTERFACE_REGISTER.csv` rows for `PKG-035` (twelve interface facts; Gate 7 snapshot).
- `OBJECTIVE_DELIVERABLE_MAP.csv` rows for `DEL-035-06` (Gate 7 snapshot).
- `OBJECTIVE_REGISTER.csv` rows `OBJ-001`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` (Gate 7 snapshot).
- `SCOPE_LEDGER.csv` row `SOW-0036` (Gate 7 snapshot).
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — SEC-12 Electrical Basis (13.8 kV switchgear, electrical buildings, grounding, cable systems); Building Strategy table (`810-1 13.8kV Switchgear Electrical Building`, Shop).
- `_Sources/26020-Package_Requirements.docx` — vendor documentation tables (binary; specific clause text not extracted; cited as location TBD).
