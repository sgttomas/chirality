# Specification — DEL-078-02 Package Datasheet (Pig Receivers (Inlet) 4-25)

Normative requirements for the contents and use of the PKG-078 Package Datasheet, derived from accessible decomposition sources (SCOPE_LEDGER `SOW-0161` to `SOW-0164`, PACKAGE_REGISTER row 78, INTERFACE_REGISTER PKG-078 rows) and the DBM-Deepcut basis document.

## Scope

### In scope

- Documenting source-supported equipment, design, and operating data needed for third-party Package Vendor or downstream discipline engineering of the (3x) 610 mm (24 in) inlet pig receivers with HIPPS at the 04-25 facility.
- Capturing the package interface requirements matrix at the EPC/Vendor boundary for the ten interface types declared in INTERFACE_REGISTER for PKG-078.
- Recording sour-service classification, operating envelope, design envelope, and ambient envelope for the receiver skids.
- Recording explicit `By Others` allocations declared in `SOW-0164` (interconnecting piping, DCS integration, foundations, electrical supply to MCC).

### Out of scope

- Vendor package engineering and design (owned by Package Vendor; produced under DEL-078-04 Vendor Engineered Equipment Package).
- Construction work packaging and installation (DEL-078-03 Construction Work Package).
- Vendor document register and turnover records (DEL-078-05 Vendor Document Turnover Package).
- Final review and acceptance of vendor package against this datasheet (DEL-078-06 EPC Vendor Package Review and Acceptance).
- Pipeline scope upstream of the pig-receiver inlet flange beyond what is required to define the tie-in interface (per DBM-Deepcut SEC-04 framing).
- Resolution of `By Others` work items themselves (only their allocation is recorded here).

## Requirements

| Req ID | Requirement | Source |
|---|---|---|
| REQ-DS-001 | The datasheet shall identify three (3) identical 610 mm (24 in) OD pig receivers on dedicated structural-steel non-enclosed skids. | `SOW-0162`, `SOW-0163` |
| REQ-DS-002 | The datasheet shall record receiver tag basis `PR-1010 / PR-1020 / PR-1030-1`. | `SOW-0163` |
| REQ-DS-003 | The datasheet shall specify a HIPPS package on each skid with ESDV(s) upstream of the receiver. | `SOW-0163` |
| REQ-DS-004 | The HIPPS package shall include a pressure control valve and outlet pressure transmitter under PID control to maintain inlet separator vessel operating pressure below the applicable setpoint. | `SOW-0163` |
| REQ-DS-005 | The HIPPS package shall include a shutdown valve with pneumatic hi-low shutoff and an additional redundant shutdown valve with pneumatic hi-low to close the high-pressure inlet. | `SOW-0163` |
| REQ-DS-006 | A sweet-gas purge connection shall be provided downstream of a manual isolation valve, sized for sour-gas purge of the receiver barrel prior to opening for pig retrieval. | `SOW-0163` |
| REQ-DS-007 | A vent line from each receiver shall be routed to the HP flare system. | `SOW-0163` |
| REQ-DS-008 | The datasheet shall classify the service as sour with design H2S of 1.0 mol%. | `SOW-0163`; DBM SEC-04 |
| REQ-DS-009 | The datasheet shall record design throughput of 225 MMSCFD (total for the package). Normal flowrate per receiver shall be carried as `TBC`. | `SOW-0164` |
| REQ-DS-010 | The datasheet shall record normal operating pressure 653-725 psig, MAOP 1300 psig, design pressure low 653 psig / normal high 725 psig, and MAWP 1440 psig. | `SOW-0164` |
| REQ-DS-011 | The datasheet shall record historical ambient temperature -19 deg C min / 22.2 deg C max, and ambient design temperature -40 deg C min / +35 deg C max. | `SOW-0164` |
| REQ-DS-012 | The datasheet shall record explicit `By Others` allocations: interconnecting piping, DCS integration, foundations, and electrical supply to MCC. | `SOW-0164` |
| REQ-DS-013 | The datasheet shall include a Package Interface Requirements Matrix covering all ten PKG-078 interfaces in INTERFACE_REGISTER (Process Piping; Relief/Flare/Vent; Drain/Containment; Electrical Power; EHT; I&C/Control Cabling; Maintenance Access; Grading/Site Drainage/Spill Containment; Structural/Foundations/Supports; Pipeline/Pigging). | INTERFACE_REGISTER rows 647-656; PACKAGE_REGISTER row 78 |
| REQ-DS-014 | The datasheet shall cite source provenance (file + section/row) for each non-trivial value. Items not derivable from accessible sources shall be marked `TBD`. Inferences shall be labelled `ASSUMPTION`. | `four-documents` skill QA; project epistemic policy |
| REQ-DS-015 | Materials of construction (MOC) for sour service shall be specified by the Package Vendor consistent with the stated 1.0 mol% H2S design and applicable industry sour-service standards. | `SOW-0163`; specific standard reference TBD (not stated in available sources) |
| REQ-DS-016 | Relief device sizing and vent-line sizing supporting the HP flare tie-in shall be specified by the Package Vendor consistent with the receiver design conditions. Sizing basis not stated in available sources (TBD). | `SOW-0163`; sizing basis location TBD |
| REQ-DS-017 | Hydrate management at the receivers shall use methanol injection points consistent with the DBM facility basis; no continuous hydrate suppression is provided in raw inlet gas piping. | DBM-Deepcut SEC-04 |

## Standards

Standards explicitly named in accessible sources: none stated at clause level. Probable applicable standards (recorded as ASSUMPTION pending confirmation by the Package Vendor under REQ-DS-015):

- ASME B31.3 / ASME B31.8 — process and pipeline piping (location TBD; ASSUMPTION).
- ASME BPVC Section VIII Div. 1 or 2 — pressure vessel design for the receiver barrel (location TBD; ASSUMPTION).
- NACE MR0175 / ISO 15156 — sour-service materials (location TBD; ASSUMPTION, consistent with stated sour service).
- IEC 61511 / IEC 61508 — HIPPS functional safety lifecycle (location TBD; ASSUMPTION, consistent with `SOW-0163` HIPPS redundancy).
- Provincial pipeline / pressure equipment regulation applicable to the British Columbia facility location (location TBD; ASSUMPTION).

Standards not derivable from `_REFERENCES.md` or accessible sources at clause level: location TBD.

## Verification

| Verification Target | Approach | Evidence |
|---|---|---|
| REQ-DS-001 through REQ-DS-007 | Cross-check Datasheet entries against `SCOPE_LEDGER.csv` rows `SOW-0162`, `SOW-0163`. | Datasheet "Attributes" and "Construction" tables. |
| REQ-DS-008 through REQ-DS-011 | Cross-check Datasheet entries against `SCOPE_LEDGER.csv` row `SOW-0164` and DBM-Deepcut SEC-04 inlet basis. | Datasheet "Conditions" table. |
| REQ-DS-012 | Confirm `By Others` allocations are explicit in Datasheet. | Datasheet "Interfaces — By Others" subsection. |
| REQ-DS-013 | Confirm 10/10 PKG-078 interface rows from `INTERFACE_REGISTER.csv` are present in Datasheet matrix. | Datasheet "Interfaces" table. |
| REQ-DS-014 | Walk the Datasheet; every non-trivial value carries a `Source` column or is marked `TBD`/`ASSUMPTION`. | Datasheet tables. |
| REQ-DS-015 / REQ-DS-016 | Package Vendor submittal review against DEL-078-06 EPC Vendor Package Review and Acceptance. | Vendor calculation packages (downstream evidence). |
| REQ-DS-017 | Confirm Datasheet notes hydrate management approach consistent with DBM SEC-04. | Datasheet "Conditions" row "Hydrate suppression". |

## Documentation

Anticipated artifacts produced or referenced by this deliverable (per `_CONTEXT.md`):

- Package technical datasheet (this document set).
- Vendor engineering handoff basis (this Specification + Datasheet).
- Package interface requirements matrix (Datasheet "Interfaces" table).
- Source-supported equipment and design criteria (Datasheet "Attributes", "Conditions", "Construction").

Downstream consumers (per `DELIVERABLE_REGISTER.csv` PKG-078):

- DEL-078-04 Vendor Engineered Equipment Package.
- DEL-078-03 Construction Work Package.
- DEL-078-05 Vendor Document Turnover Package.
- DEL-078-06 EPC Vendor Package Review and Acceptance.
