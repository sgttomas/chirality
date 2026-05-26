# Specification — DEL-072-06 EPC Vendor Package Review and Acceptance

## Scope

This specification governs the EPC Integrator's review and acceptance of the PKG-072 vendor package (workbook package name "Truck Product Loading Unit 4-25"; tagged equipment per DEL-072-01: skid, LP fuel-gas heater, LP fuel-gas scrubber serving the 04-25 West Doe Deep Cut Facility low-pressure fuel-gas system). The deliverable produces vendor document review records, an acceptance checklist, test/inspection evidence summaries, and turnover evidence sufficient for integration handoff to commissioning (source: _CONTEXT.md; DEL-072-01 Specification.md; 4-25_Deepcut_DBM.md sec. 2.2 Site Data Basis; sec. Fuel Gas Basis).

**Covers.** Acceptance of vendor scope items SOW-0245, SOW-0246, SOW-0247, SOW-0248 as listed in _CONTEXT.md; review against EPC SOW (DEL-072-01), Package Datasheet (DEL-072-02), and Construction Work Package (DEL-072-03); coordination with Vendor Engineered Equipment Package (DEL-072-04) and Vendor Document Turnover Package (DEL-072-05).

**Excludes.** Vendor engineering, fabrication, or supply (delivered under DEL-072-04). Vendor document production (delivered under DEL-072-05). Downstream commissioning and start-up operations. Modifications to upstream sales-gas, expander-compressor, or instrument-air scopes, except to confirm interface compliance at the package boundary.

## Requirements

| Req ID | Requirement | Source / Basis |
|---|---|---|
| REQ-1 | The acceptance set SHALL evidence vendor conformance with each accepted requirement carried in DEL-072-01 (EPC Scope of Work). | DELIVERABLE_REGISTER.csv row 558 (acceptance basis); DEL-072-01 Specification.md R-072-01-01 through R-072-01-11 |
| REQ-2 | The acceptance set SHALL evidence vendor conformance with the Package Datasheet (DEL-072-02), including tagged equipment list, design conditions, and interface requirements matrix. | DELIVERABLE_REGISTER.csv row 559 |
| REQ-3 | The acceptance set SHALL evidence construction, tie-in, inspection, and turnover steps consistent with DEL-072-03 (Construction Work Package). | DELIVERABLE_REGISTER.csv row 560 |
| REQ-4 | The acceptance set SHALL reconcile vendor document submittals against the Vendor Document Turnover Package (DEL-072-05) register; missing or non-conforming documents SHALL be itemized in the review log. | DELIVERABLE_REGISTER.csv row 562 |
| REQ-5 | Acceptance evidence SHALL confirm the package boundary operating/design envelope carried in SOW-0248 (Design Flow > 8.4 MMSCFD; Operating Pressure 150 psig; Design Pressure 150 psig; Design Temperature -40 C to 35 C; Ambient -19 C to 22.2 C). Final Flow and MAWP remain TBD per SOW-0248. | DEL-072-01 Specification.md R-072-01-05; SCOPE_LEDGER.csv SOW-0248 |
| REQ-6 | Acceptance evidence SHALL confirm the LP fuel-gas service envelope: normal source from plant fuel gas upstream of the expander-compressor, with documented water content (< 0.1 ppmv H2O normal; <= 4 lb H2O/MMSCF upset), H2S (< 6 mg/m3), and supply-pressure envelope (J-T mode expected < 2561 kPag, high 2895 kPag). | 4-25_Deepcut_DBM.md sec. Fuel Gas Design Values |
| REQ-7 | Acceptance evidence SHALL confirm package design for the site ambient envelope -40 deg C to +35 deg C, plant elevation 673 m AMSL, snow load Ss 2.5 kPa / Sr 0.2 kPa, and hourly wind pressure q(1/50) 0.40 kPa unless a stricter package-specific basis is invoked by DEL-072-02. | 4-25_Deepcut_DBM.md sec. 2.2 Site Data Basis |
| REQ-8 | Acceptance evidence SHALL confirm the regulator sparing philosophy: minimum 2 x 100% regulators per service, individual isolation, outlet test connections, pilot isolation on pilot-type regulators, and quick-acting internally-sensing start-gas regulators (not pilot-type). | 4-25_Deepcut_DBM.md sec. Fuel Gas Equipment and Controls |
| REQ-9 | Acceptance evidence SHALL confirm the emergency-generator fuel-gas supply: < 66 psig at supply for general-purpose classification, design flow 0.468 MMSCFD, and start-gas flow 3.6 MMSCFD for 30 s (TBC), with piping and vessels accommodating simultaneous start-gas plus design operating case. | 4-25_Deepcut_DBM.md sec. Fuel Gas Equipment and Controls |
| REQ-10 | Acceptance evidence SHALL confirm the LP fuel-gas scrubber sizing at max K = 0.35 Imperial with operating-pressure derating, hydrocarbon liquid routing (DBM basis to TK-9130-1), and the electric resistance heater controls (SCR control; skin-temperature thermocouple override; gas outlet temperature control). Heater duty value remains TBD pending DE. | 4-25_Deepcut_DBM.md sec. Fuel Gas Equipment and Controls |
| REQ-11 | Acceptance evidence SHALL include FAT, SAT (where applicable), pressure-test, NDE, and functional-test records for the skid scope. Specific test plan content is TBD pending DEL-072-02 and vendor ITP. | _CONTEXT.md (Anticipated Artifacts); location TBD |
| REQ-12 | Acceptance evidence SHALL include turnover records: mechanical completion certificate, punchlist (open/cleared), system handover sign-off. | _CONTEXT.md (Anticipated Artifacts) |
| REQ-13 | Acceptance SHALL confirm that the sweet-gas purge / methyl-mercaptan hazard review has been conducted, or carry the gap as an open item. Fuel gas SHALL NOT be assumed safe across all operating modes for purge service without supporting review. | 4-25_Deepcut_DBM.md sec. Emergency Buyback and Purge |
| REQ-14 | Open items requiring human ruling (e.g., package taxonomy reconciliation per CONFLICT-0; shared 03-25/04-25 fuel-gas demand split per CONFLICT-1; acid-gas dilution sizing inclusion per CONFLICT-2; sibling-deliverable maturity per CONFLICT-3) SHALL NOT be silently closed during acceptance; unresolved items SHALL be carried as TBD on the acceptance checklist. | 4-25_Deepcut_DBM.md sec. Fuel Gas Basis; sec. Emergency Buyback and Purge; _CONTEXT.md |
| REQ-15 | The acceptance package SHALL cite source slices for every accepted requirement to preserve audit traceability. | K-PROV-1 (governance) — ASSUMPTION as a deliverable-level invariant |

## Standards

| Standard | Applicability | Location |
|---|---|---|
| Project EPC SOW (DEL-072-01) | Primary contractual basis for vendor acceptance | DEL-072-01 Specification.md (drafted; full deliverable maturity TBD) |
| Project Package Datasheet (DEL-072-02) | Technical basis for acceptance | location TBD (DEL-072-02 not yet drafted at run time) |
| Project Construction Work Package (DEL-072-03) | Construction/turnover basis for acceptance | location TBD (DEL-072-03 not yet drafted at run time) |
| 26020-Package_Requirements.docx package heading 26 | Source-of-truth package requirement statements | location TBD (binary source not parsed in this run) |
| National Building Code of Canada 2020 (Dawson Creek IDF data) | Site environmental loading basis for package buildings and structures | 4-25_Deepcut_DBM.md sec. 2.2 Site Data Basis (climate-data basis) |
| BC Building Code 2018 | Building code basis (nearest site Dawson Creek, BC) | 4-25_Deepcut_DBM.md sec. 2.2 Site Data Basis |
| Applicable Canadian provincial mechanical, pressure equipment, and electrical codes for British Columbia | Acceptance validation of regulatory compliance | location TBD (no clause-level text in accessible source slices) |

## Verification

| Req | Verification Method |
|---|---|
| REQ-1, REQ-2, REQ-3 | Document review against DEL-072-01/02/03; conformance log entries |
| REQ-4 | Cross-check of vendor submittals against DEL-072-05 register |
| REQ-5 | Inspection of vendor data sheets/calculations confirming the SOW-0248 envelope; TBD items carried |
| REQ-6 | Inspection of vendor design records (datasheets, calculations) confirming fuel-gas inlet envelope |
| REQ-7 | Inspection of vendor structural/environmental design records confirming ambient, snow, wind, and elevation basis |
| REQ-8 | Review of regulator arrangement drawings, isolation provisions, and start-gas regulator type certification |
| REQ-9 | Review of emergency-generator supply piping, vessel sizing, and pressure-classification compliance |
| REQ-10 | Review of scrubber sizing calculation, heater datasheet, and control narrative |
| REQ-11 | Witnessed/reviewed FAT/SAT/test reports; NDE certificates; pressure-test packets |
| REQ-12 | Mechanical completion certificate; punchlist register; signed turnover transmittal |
| REQ-13 | Evidence that the sweet-gas purge / methyl-mercaptan hazard review has been executed (or recorded as open item) |
| REQ-14 | Acceptance checklist entries marked TBD or NEEDS_HUMAN_RULING with traceable references |
| REQ-15 | Audit of acceptance package for source citations |

## Documentation

The acceptance deliverable comprises:

- Vendor document review log (per REQ-4)
- Package acceptance checklist (covering REQ-1 through REQ-14)
- Test/inspection evidence dossier (per REQ-11)
- Turnover evidence dossier (per REQ-12)
- Hazard-review confirmation record (per REQ-13)
- Open-items register (per REQ-14)
