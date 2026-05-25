# Datasheet: DEL-016-06_epc-vendor-package-review-and-acceptance

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-016-06_epc-vendor-package-review-and-acceptance` | `_CONTEXT.md` |
| Deliverable name | EPC Vendor Package Review and Acceptance | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent package | `PKG-016` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Package name | Transformer TXP-8200-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 3MVA 13.8kV/600/347V | Workbook Packages row 18; `PACKAGE_REGISTER.csv` |
| Workbook ID / row | 16 / row 18 | Workbook Packages row 18; `PACKAGE_REGISTER.csv` |
| WBS | 02 | Workbook Packages row 18; `PACKAGE_REGISTER.csv` |
| CoA tracking number | 26020-02-30-007 | Workbook Packages row 18; `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | Workbook Packages row 18; `_CONTEXT.md` |
| Deliverable type | EPC Vendor Package Acceptance | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | EPC Integrator (lead) with Package Vendor input | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Covers SOW item | `SOW-0017` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Supports objectives | OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010 | `OBJECTIVE_DELIVERABLE_MAP.csv` (package-grouped, ASSUMPTION) |
| Package responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and physical equipment package; EPC Integrator owns facility-level integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-016` |

## Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Acceptance subject | Vendor-delivered 13.8 kV / 600 V step-down distribution transformer package TXP-8200-1, rated 3 MVA, secondary nominal 600/347 V. | Workbook Packages row 18; `PACKAGE_REGISTER.csv`; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` "Incoming Power and Transformers" |
| Service designation | 13.8 kV to 600 V, 3 MVA transformer feeding the 600 V MCC for LV loads at 03-25. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, "Incoming Power and Transformers" table |
| Upstream feed | Sub-fed from the 04-25 13.8 kV Main Switchgear Electrical Building via 03-25 primary feeders. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, "Incoming Power and Transformers" |
| Downstream load served | 600 V MCC for LV loads — motors 3/4 hp through 250 hp DOL, lighting transformers, building heaters, UPS larger than 10 kVA. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, "System Voltages" and "600V MCC and Standby Power" |
| LV system grounding basis | 600 V, 3 phase, 3 wire, 60 Hz, HRG with 5 A continuous resistor. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, "System Voltages" |
| MV system grounding basis | 13.8 kV incoming, 3 phase, 3 wire, 60 Hz LRG. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, "System Voltages" |
| Site ambient basis | -40 deg C minimum ambient governs exposed equipment, package buildings, control panels, instrumentation, and field devices unless a more severe process or vendor condition applies. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, site basis paragraph |
| Hazardous area context | General facility classification basis: Class I Zone 2, Gas Groups IIA and IIB; transformer location classification confirmation by detailed design. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, "Area Classification" |
| Acceptance evidence anchors (EPC reference set) | (a) DEL-016-01 EPC Scope of Work; (b) DEL-016-02 EPC Package Datasheet; (c) DEL-016-03 EPC Construction Work Package. | `DELIVERABLE_REGISTER.csv` rows for `PKG-016`; `_CONTEXT.md` Scope |
| Vendor-side input anchors | DEL-016-04 Vendor Engineered Equipment Package; DEL-016-05 Vendor Document Turnover Package. | `DELIVERABLE_REGISTER.csv` rows for `PKG-016` |
| Acceptance secondary nominal (347 V) | Package title includes "600/347 V" indicating a 600 V, 3-phase, 4-wire secondary supporting 347 V line-to-neutral; explicit acceptance criteria for the 347 V neutral are not detailed in accessible DBM sources. | Workbook Packages row 18 (title); DBM table lists 600 V 3W only — ASSUMPTION (title interpretation); see Guidance Conflict Table |

## Conditions

| Interface / condition | Acceptance basis | Source |
|---|---|---|
| Electrical Power | Acceptance must include evidence the vendor package satisfies the primary 13.8 kV incoming and 600 V outgoing interface as defined in the EPC Package Datasheet. | `INTERFACE_REGISTER.csv` `IFC-0C63CABBEC`; Workbook Packages row 18 |
| Grounding / Bonding | Acceptance must include vendor evidence of grounding/bonding arrangement consistent with project HRG / LRG bases and CEC grounding practice. | `INTERFACE_REGISTER.csv` `IFC-C4343B4BCA`; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, "Electrical Buildings, Raceways..." |
| Area / Exterior Lighting | Acceptance must record whether vendor package includes integral or interface area lighting, and that EPC integration scope is unambiguous. | `INTERFACE_REGISTER.csv` `IFC-C649F648C5` |
| I&C / Control Cabling | Acceptance must include vendor identification of all control terminations, alarm contacts, and protective relay interfaces required to integrate with the plant control architecture. | `INTERFACE_REGISTER.csv` `IFC-AC26461656`; DBM "Control System Basis" pointer |
| Communications / Network | Acceptance must capture vendor communications/network interfaces (if any), or formally record "none". | `INTERFACE_REGISTER.csv` `IFC-D3B7348DC6` |
| Maintenance Access | Acceptance must include evidence that maintenance access for the transformer (and oil-handling/de-energization equipment as applicable) is consistent with the EPC layout and CWP. | `INTERFACE_REGISTER.csv` `IFC-4A94795733`; DBM raceway/cable-tray paragraph |
| Structural / Foundations / Supports | Acceptance must include vendor anchorage loads, foundation interface drawings, and confirmation of compatibility with EPC structural/foundation design. | `INTERFACE_REGISTER.csv` `IFC-E3BE98E89B` |
| Cable / conduit routing | Cable tray and conduit routing shall not interfere with maintenance access; EPC acceptance must confirm vendor routing data is compatible. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, raceways paragraph |
| Circuit separation | 13.8 kV, 4,160 V, and 600 V power circuits shall be separated from control and instrument circuits by distance, shielding, or routing. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, raceways paragraph |
| Winterization | Vendor package must meet -40 deg C minimum ambient design unless a vendor condition is more severe. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, site basis |

## Construction

| Element | Value / status | Source |
|---|---|---|
| Acceptance artifact set produced | Vendor document review log; package acceptance checklist; test/inspection evidence; turnover evidence. | `DELIVERABLE_REGISTER.csv` row `DEL-016-06`; `_CONTEXT.md` Anticipated Artifacts |
| Review framework | EPC Integrator-led review against (a) DEL-016-01 EPC Scope of Work, (b) DEL-016-02 EPC Package Datasheet, (c) DEL-016-03 EPC Construction Work Package. | `_CONTEXT.md` Scope; `DELIVERABLE_REGISTER.csv` rows `DEL-016-01..03` |
| Vendor-side inputs to review | DEL-016-04 Vendor Engineered Equipment Package and DEL-016-05 Vendor Document Turnover Package supply the engineering, documentation, and physical package material being accepted. | `DELIVERABLE_REGISTER.csv` rows `DEL-016-04`, `DEL-016-05` |
| Acceptance organization | EPC Integrator leads; Package Vendor provides input and clarifications. | `DELIVERABLE_REGISTER.csv` row `DEL-016-06` |
| Disposition states | Accept / Accept-with-comment / Reject-and-resubmit (PROPOSAL — disposition vocabulary not defined in accessible sources). | ASSUMPTION |
| Acceptance test/inspection categories (placeholder) | Factory test reports, site inspection records, energization checks, and turnover evidence — specific tests TBD pending vendor scope freeze. | TBD; see Specification Verification |
| Turnover evidence | EPC-accepted record set is the input to facility-level commissioning and to PKG-016 closure. | `_CONTEXT.md` Scope; `DELIVERABLE_REGISTER.csv` row `DEL-016-06` |

## References

- `_CONTEXT.md` (this deliverable folder)
- `_REFERENCES.md` (this deliverable folder)
- `_DEPENDENCIES.md` (this deliverable folder)
- Gate 7 snapshot: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
  - `DELIVERABLE_REGISTER.csv` rows `DEL-016-01` through `DEL-016-06`
  - `PACKAGE_REGISTER.csv` row `PKG-016`
  - `INTERFACE_REGISTER.csv` rows `IFC-0C63CABBEC`, `IFC-C4343B4BCA`, `IFC-C649F648C5`, `IFC-AC26461656`, `IFC-D3B7348DC6`, `IFC-4A94795733`, `IFC-E3BE98E89B`
  - `OBJECTIVE_DELIVERABLE_MAP.csv` rows for `PKG-016` (objectives OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010)
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` — sections "Area Classification", "System Voltages", "Incoming Power and Transformers", "600V MCC and Standby Power", "Electrical Buildings, Raceways, Lighting, and Heat Tracing"
- Workbook Packages row 18
