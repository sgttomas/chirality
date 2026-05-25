# Specification: DEL-035-06_epc-vendor-package-review-and-acceptance

## Scope

### In scope

- EPC Integrator review of vendor-submitted documentation, factory test/inspection evidence, and acceptance/turnover artifacts for the `PKG-035` 13.8 kV switchgear electrical building package (Building 810-1).
- EPC Integrator acceptance decision evidencing readiness of the vendor package for facility integration and handoff against the EPC Scope of Work (DEL-035-01), Package Datasheet (DEL-035-02), and Construction Work Package (DEL-035-03).
- Production of the four anticipated artifacts: vendor document review log, package acceptance/turnover checklist, factory/shop test and inspection evidence, and turnover evidence.

Source: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv`; `SCOPE_LEDGER.csv` `SOW-0036`; `ARTIFACT_REGISTER.csv`.

### Out of scope

- Vendor-side package engineering, package design, vendor documentation authorship, and physical equipment manufacture. These are owned by the Package Vendor under the `PKG-035` responsibility model. Source: `PACKAGE_REGISTER.csv` row `PKG-035`.
- Re-statement of the EPC Scope of Work, Package Datasheet, or Construction Work Package content. This deliverable consumes those upstream deliverables; it does not replace them.
- Field construction, mechanical completion, and commissioning of the building once placed at site. ASSUMPTION: those activities sit downstream of acceptance/turnover; field-construction ownership is defined in DEL-035-03 (Construction Work Package).

## Requirements

| Req ID | Statement | Source |
|---|---|---|
| REQ-035-06-001 | The deliverable shall produce a vendor document review and comment log (`ART-AA841F7CA1`) recording each vendor document submission, EPC reviewer, comment disposition, and revision-closure status. | `ARTIFACT_REGISTER.csv` `ART-AA841F7CA1` |
| REQ-035-06-002 | The deliverable shall produce a vendor package acceptance and turnover checklist (`ART-72A172E45B`) evidencing satisfaction of EPC Scope of Work (DEL-035-01), Package Datasheet (DEL-035-02), and Construction Work Package (DEL-035-03) items for PKG-035, signed by the EPC Integrator with Package Vendor input. | `ARTIFACT_REGISTER.csv` `ART-72A172E45B`; `DELIVERABLE_REGISTER.csv` |
| REQ-035-06-003 | The deliverable shall capture vendor factory/shop test and inspection evidence (`ART-7F4CFC552C`) for the shop-built Building 810-1 and its 13.8 kV switchgear, consistent with the vendor specification and the EPC Package Datasheet acceptance basis. Detailed witness/hold-point criteria — `location TBD` pending `_Sources/26020-Package_Requirements.docx` slice. | `ARTIFACT_REGISTER.csv` `ART-7F4CFC552C`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Building Strategy table (Shop) |
| REQ-035-06-004 | Acceptance shall evidence closure of each of the twelve `PKG-035` interface facts (`IFC-C8A7133D59`, `IFC-231DB0CBFA`, `IFC-A5EF521315`, `IFC-C11BBF56CD`, `IFC-EB2FA7BDE6`, `IFC-9214AEAF28`, `IFC-00317770B3`, `IFC-73CF283A27`, `IFC-C00E60F032`, `IFC-A3B2DADC44`, `IFC-589CAC7BC6`, `IFC-A5DBFBF436`) against the EPC Interface Requirements Evidence carried in DEL-035-02. | `INTERFACE_REGISTER.csv` rows for `PKG-035` |
| REQ-035-06-005 | The 13.8 kV switchgear shall be sized for the full facility scope and shall serve as the plant main power distribution centre supplying downstream electrical buildings; acceptance shall evidence vendor compliance with this distribution role. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Electrical Basis (13.8 kV switchgear paragraph) |
| REQ-035-06-006 | The 810-1 electrical building shall be a prefabricated, modular, shop-built building located in a general purpose area; acceptance shall evidence shop-build origin and area classification. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Building Strategy table; Area Classification paragraph; Electrical Buildings section |
| REQ-035-06-007 | The building shall be elevated and installed on piles to provide space beneath the building for cable trays; incoming and outgoing power cables shall be bottom entry; acceptance shall evidence both. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Electrical Buildings |
| REQ-035-06-008 | HVAC for the electrical building shall be sized as n+1 such that cooling can tolerate failure or maintenance of one unit without affecting heating and cooling; acceptance shall evidence n+1 sizing and operation. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Electrical Buildings (n+1 HVAC) |
| REQ-035-06-009 | Equipment doors shall be sized for, or include removable transom sections to allow, removal of the largest equipment; acceptance shall evidence door/transom configuration. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Electrical Buildings |
| REQ-035-06-010 | Major electrical equipment shall be directly connected to the ground grid at two points; ground wells at the electrical building shall be provided for maintenance/operational testing with bolted ground connections at test points; acceptance shall evidence grounding configuration and test points. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Grounding and Bonding |
| REQ-035-06-011 | Vendor design, fabrication, installation, testing, and inspection shall conform to CSA C22.1-21 Canadian Electrical Code and applicable BC provincial/local electrical codes and the requirements of the designated electrical inspection authority; applicable standards include CSA, API, IEEE, ISA, NEMA, WorkSafeBC, Technical Safety BC, and BCER. Acceptance shall include a vendor statement of conformance. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Electrical Basis (standards paragraph) |
| REQ-035-06-012 | The deliverable shall record vendor-side open items at acceptance time and the agreed closure path, supporting controlled open-item closure for procurement and downstream facility handoff (OBJ-010). | `OBJECTIVE_REGISTER.csv` OBJ-010 |
| REQ-035-06-013 | The acceptance record shall preserve the package responsibility split: Package Vendor owns package engineering/design/documentation/equipment; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration (OBJ-004). | `PACKAGE_REGISTER.csv` row `PKG-035`; `OBJECTIVE_REGISTER.csv` OBJ-004 |

## Standards

| Standard / authority | Applicability | Source |
|---|---|---|
| CSA C22.1-21 Canadian Electrical Code | Governs electrical design, fabrication, installation, testing, and inspection for the package. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Electrical Basis |
| BC provincial and local electrical codes and regulations | Apply alongside CSA C22.1-21 per the designated electrical inspection authority. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Electrical Basis |
| CSA, API, IEEE, ISA, NEMA standards | Apply to electrical materials and equipment; latest applicable revisions. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Electrical Basis |
| WorkSafeBC, Technical Safety BC, BCER | Apply as governing regulatory bodies. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Electrical Basis |
| `_Sources/26020-Package_Requirements.docx` vendor-document tables | Define the vendor documentation set the review log must cover. Specific table content `location TBD` — source is binary and was not slice-extracted in this pass. | `OBJECTIVE_REGISTER.csv` OBJ-004 narrative; `OBJECTIVE_REGISTER.csv` OBJ-010 narrative |

## Verification

| Req ID | Verification approach | Evidence |
|---|---|---|
| REQ-035-06-001 | Document audit: confirm every vendor submission referenced by the package is logged with reviewer, comments, and resolution status. | Vendor document review log (`ART-AA841F7CA1`). |
| REQ-035-06-002 | Checklist review: confirm each EPC Scope of Work, Package Datasheet, and Construction Work Package item for PKG-035 has a signed disposition. | Acceptance and turnover checklist (`ART-72A172E45B`). |
| REQ-035-06-003 | Inspection record review: confirm FAT and shop inspection reports cover the building and switchgear; witness/hold-point items closed or carried as open items. | Factory/shop test and inspection evidence (`ART-7F4CFC552C`). |
| REQ-035-06-004 | Interface walkdown of the twelve PKG-035 interface facts against DEL-035-02 evidence. | Interface closure entries in the acceptance checklist. |
| REQ-035-06-005..010 | Design/installation verification against DBM electrical-basis statements (distribution role, shop build, elevation/bottom entry, HVAC n+1, equipment door/transom, grounding two-point + ground wells). | Vendor design records, FAT/shop inspection, EPC walkdown notes. |
| REQ-035-06-011 | Code/standards verification: vendor statement of conformance reviewed by EPC and electrical inspection authority engagement evidence. | Vendor conformance statement; inspection authority correspondence. |
| REQ-035-06-012 | Open-items audit: confirm every TBD/open item is captured with owner and closure plan. | Open-items log within the acceptance package. |
| REQ-035-06-013 | Responsibility-split review: confirm acceptance record does not assign vendor engineering/design to the EPC and does not assign integration work to the vendor. | Acceptance checklist signature pages; responsibility assignment record. |

## Documentation

The deliverable shall produce and retain:

- Vendor document review and comment log (`ART-AA841F7CA1`).
- Vendor package acceptance and turnover checklist (`ART-72A172E45B`).
- Factory/shop test and inspection evidence package (`ART-7F4CFC552C`).
- Turnover evidence file (collated record of handoff from Package Vendor to EPC Integrator and from EPC Integrator to facility operations/commissioning).
- Open-items closure log (supporting OBJ-010).

Source: `_CONTEXT.md` anticipated artifacts; `ARTIFACT_REGISTER.csv`; `OBJECTIVE_REGISTER.csv` OBJ-010.
