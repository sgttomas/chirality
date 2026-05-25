# Datasheet: DEL-020-06_epc-vendor-package-review-and-acceptance

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-020-06_epc-vendor-package-review-and-acceptance` | `_CONTEXT.md` |
| Deliverable name | EPC Vendor Package Review and Acceptance | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-020` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | 13.8kV SWITCHGEAR EQUIPMENT | Workbook Packages row 22; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 20 / row 22 | Workbook Packages row 22; `PACKAGE_REGISTER.csv` |
| WBS | 01 | Workbook Packages row 22; `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-01-30-011 | Workbook Packages row 22; `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | Workbook Packages row 22; `_CONTEXT.md` |
| Deliverable type | EPC Vendor Package Acceptance | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | EPC Integrator (lead) with Package Vendor input | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-020` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Deliverable role | EPC-integrator review and acceptance evidence for the PKG-020 vendor package against the EPC Scope of Work, Package Datasheet, and Construction Work Package. | `DELIVERABLE_REGISTER.csv` row `DEL-020-06...`; `_CONTEXT.md` |
| Anticipated artifacts | Vendor document review log; package acceptance checklist; test/inspection evidence; turnover evidence. | `DELIVERABLE_REGISTER.csv`; `_CONTEXT.md` |
| Subject package function | 13.8 kV switchgear, designed, purchased, and installed as the plant main power distribution center; bus sized for the full facility scope; distributes power radially through step-down transformers to 6.9 kV, 4.16 kV, 600 V, and general-area electrical buildings. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-12 Power System paragraphs |
| Subject voltage / service basis | 13.8 kV, 3-phase, 3-wire, 60 Hz, low-resistance grounded medium-voltage service used both for BC Hydro utility distribution and facility backbone distribution. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, System Voltages table |
| Governing equipment specification | ELC-QAS-000007-001 "Medium Voltage Switchgear" (Rev 1) governs the equipment basis; ELC-QAS-000003-001 "Electrical Requirements for Packaged Equipment" (Rev 2) governs vendor packaged-equipment requirements. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Table 12-1 |
| Housing | DBM contemplates housing the 13.8 kV main switchgear within prefabricated, modular electrical buildings (e.g., "810-1 13.8kV Switchgear Electrical Building"). Final building assignment confirmed by detailed design. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings and module list |
| Vendor scope to review | Package engineering, package design, vendor documentation, and the physical equipment package as supplied by the Package Vendor for PKG-020. | `PACKAGE_REGISTER.csv` row `PKG-020`; `DELIVERABLE_REGISTER.csv` rows `DEL-020-04`, `DEL-020-05` |
| EPC-integrator review scope | Integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-020` |

## Conditions

| Interface / condition | Acceptance-review consideration | Source |
|---|---|---|
| Electrical Power | Verify vendor package electrical input/output ratings, interrupting capacity, bus rating, and feeder arrangement against EPC Package Datasheet and electrical studies. | Workbook Packages row 22; `INTERFACE_REGISTER.csv` `IFC-611474D99C`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-12 |
| Grounding / Bonding | Verify vendor package ground-grid connections, copper ground conductor sizing per CEC, and two-point ground attachments for major electrical equipment. | Workbook Packages row 22; `INTERFACE_REGISTER.csv` `IFC-F3098CE7CD`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding and bonding paragraphs |
| I&C / Control Cabling | Verify control and protection wiring, terminal-block arrangement, and interface points for plant control and protective relaying. | Workbook Packages row 22; `INTERFACE_REGISTER.csv` `IFC-8BF7209227` |
| Communications / Network | Verify communications interfaces (e.g., relay/SCADA networking) against facility network architecture; specific protocol and media TBD pending detailed design. | Workbook Packages row 22; `INTERFACE_REGISTER.csv` `IFC-340091634A` |
| Maintenance Access | Verify maintenance access envelopes, cable-tray and conduit routing, and rack-out/withdrawal clearances. | Workbook Packages row 22; `INTERFACE_REGISTER.csv` `IFC-2FB786FC10`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable-tray paragraphs |
| Structural / Foundations / Supports | Verify support/foundation interface with the electrical-building structure and any pad, anchor, or seismic restraint required. | Workbook Packages row 22; `INTERFACE_REGISTER.csv` `IFC-08E563D004` |
| Required electrical studies (preconditions) | Hazardous-area-classification, load, short-circuit, relay-coordination/arc-flash, and load-flow studies shall be completed before finalizing equipment ratings and suitability; acceptance shall not be granted until study outputs are reflected in the accepted vendor package. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-12 electrical-studies paragraph |
| Certification basis | Equipment supplied shall be new, of current design, and third-party certified by CSA, ULc, FM, ETL, or another Nationally Recognized Testing Laboratory acceptable for the application. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-12 codes/standards paragraph |

## Construction

| Topic | Basis | Source / status |
|---|---|---|
| Vendor package production | Package Vendor produces engineering, design, vendor documentation, and the physical equipment package (DEL-020-04, DEL-020-05). | `DELIVERABLE_REGISTER.csv` rows `DEL-020-04`, `DEL-020-05`; `PACKAGE_REGISTER.csv` row `PKG-020` |
| Review log | Vendor document review log: numbered list of vendor submittals with reviewer, review status (e.g., A/B/C/Rev), comments, and disposition. Specific review-status taxonomy and EPC document-control numbering TBD pending project document-control procedure. | `_CONTEXT.md`, anticipated artifacts |
| Acceptance checklist | Package acceptance checklist covering scope conformance, interface conformance, code/standard conformance, study-outcome incorporation, and turnover prerequisites. | `_CONTEXT.md`, anticipated artifacts |
| Test/inspection evidence | Factory acceptance test (FAT) records, site acceptance test (SAT) records, and inspection reports. Specific FAT/SAT scope TBD pending governing equipment specification (ELC-QAS-000007-001) review and project test plan. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Table 12-1; `_CONTEXT.md` |
| Turnover evidence | Vendor turnover records associated with DEL-020-05 vendor document turnover package; final mechanical-completion and EPC-acceptance sign-offs against facility turnover procedure. | `DELIVERABLE_REGISTER.csv` row `DEL-020-05` |
| Tie-ins and constructability | EPC Integrator constructability and facility tie-in review per DEL-020-03 Construction Work Package. | `DELIVERABLE_REGISTER.csv` row `DEL-020-03` |

## References

- `_CONTEXT.md`, deliverable identity and scope.
- `_REFERENCES.md`, Gate 7 source pointers.
- `_DEPENDENCIES.md`, declared upstream/downstream lists.
- `DELIVERABLE_REGISTER.csv`, row `DEL-020-06_epc-vendor-package-review-and-acceptance` (and sibling rows `DEL-020-01..05`).
- `PACKAGE_REGISTER.csv`, row `PKG-020`.
- `INTERFACE_REGISTER.csv`, rows for `PKG-020`.
- `OBJECTIVE_DELIVERABLE_MAP.csv`, rows for `DEL-020-06...`.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-12 Electrical Basis (Power System; System Voltages; codes/standards; electrical buildings; equipment list).
- `_Sources/26020-Package_Requirements.docx` — referenced by package convention; specific PKG-020 package slice not extracted in this run (`location TBD`).
