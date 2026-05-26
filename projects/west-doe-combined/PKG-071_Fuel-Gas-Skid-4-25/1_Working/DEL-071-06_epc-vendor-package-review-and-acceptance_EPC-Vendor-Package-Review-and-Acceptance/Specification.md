# Specification — DEL-071-06 EPC Vendor Package Review and Acceptance

## Scope

This specification governs the EPC Integrator's review and acceptance of the Fuel Gas Skid 4-25 vendor package (PKG-071). The deliverable produces vendor document review records, an acceptance checklist, test/inspection evidence summaries, and turnover evidence sufficient for integration handoff to commissioning at the 04-25 West Doe Deepcut Gas Plant (source: _CONTEXT.md; 4-25_Deepcut_DBM.md sec. 2.2 Site Data Basis; sec. Fuel Gas Basis).

**Covers.** Acceptance of vendor scope items SOW-0099, SOW-0100, SOW-0101, SOW-0102 as listed in _CONTEXT.md; review against EPC SOW (DEL-071-01), Package Datasheet (DEL-071-02), and Construction Work Package (DEL-071-03); coordination with Vendor Engineered Equipment Package (DEL-071-04) and Vendor Document Turnover Package (DEL-071-05).

**Excludes.** Vendor engineering, fabrication, or supply (delivered under DEL-071-04). Vendor document production (delivered under DEL-071-05). Downstream commissioning and start-up operations. Modifications to upstream sales-gas, expander-compressor, or instrument-air scopes, except to confirm interface compliance at the fuel-gas skid boundary.

## Requirements

| Req ID | Requirement | Source / Basis |
|---|---|---|
| REQ-1 | The acceptance set SHALL evidence vendor conformance with each accepted requirement carried in DEL-071-01 (EPC Scope of Work). | DELIVERABLE_REGISTER.csv row 330 (acceptance basis) |
| REQ-2 | The acceptance set SHALL evidence vendor conformance with the Package Datasheet (DEL-071-02), including tagged equipment list, design conditions, and interface requirements matrix. | DELIVERABLE_REGISTER.csv row 331 |
| REQ-3 | The acceptance set SHALL evidence construction, tie-in, inspection, and turnover steps consistent with DEL-071-03 (Construction Work Package). | DELIVERABLE_REGISTER.csv row 332 |
| REQ-4 | The acceptance set SHALL reconcile vendor document submittals against the Vendor Document Turnover Package (DEL-071-05) register; missing or non-conforming documents SHALL be itemized in the review log. | DELIVERABLE_REGISTER.csv row 334 |
| REQ-5 | Acceptance evidence SHALL confirm the LP fuel-gas service envelope: normal source from plant fuel gas upstream of the expander-compressor, with documented water content (< 0.1 ppmv H2O normal; <= 4 lb H2O/MMSCF upset), H2S (< 6 mg/m3), and supply-pressure envelope (J-T mode expected < 2561 kPag, high 2895 kPag; expander mode expected 2217 kPag, high 2895 kPag). | 4-25_Deepcut_DBM.md sec. Fuel Gas Design Values |
| REQ-6 | Acceptance evidence SHALL confirm package design for the site ambient envelope -40 deg C to +35 deg C, plant elevation 673 m AMSL, snow load Ss 2.5 kPa / Sr 0.2 kPa, and hourly wind pressure q(1/50) 0.40 kPa unless a stricter package-specific basis is invoked by DEL-071-02. | 4-25_Deepcut_DBM.md sec. 2.2 Site Data Basis |
| REQ-7 | Acceptance evidence SHALL confirm the regulator sparing philosophy: minimum 2 x 100% regulators per service, individual isolation, outlet test connections, pilot isolation on pilot-type regulators, and quick-acting internally-sensing start-gas regulators (not pilot-type). | 4-25_Deepcut_DBM.md sec. Fuel Gas Equipment and Controls |
| REQ-8 | Acceptance evidence SHALL confirm the emergency-generator fuel-gas supply: < 66 psig at supply for general-purpose classification, design flow 0.468 MMSCFD, and start-gas flow 3.6 MMSCFD for 30 s (TBC), with piping and vessels accommodating simultaneous start-gas plus design operating case. | 4-25_Deepcut_DBM.md sec. Fuel Gas Equipment and Controls |
| REQ-9 | Acceptance evidence SHALL confirm the LP fuel-gas scrubber (V-3210-1) sizing at max K = 0.35 Imperial with operating-pressure derating, hydrocarbon liquid routing to TK-9130-1, and the electric resistance heater controls (SCR control; skin-temperature thermocouple override; gas outlet temperature control). Heater duty value remains TBD pending DE. | 4-25_Deepcut_DBM.md sec. Fuel Gas Equipment and Controls |
| REQ-10 | Acceptance evidence SHALL include FAT, SAT (where applicable), pressure-test, NDE, and functional-test records for the skid scope. Specific test plan content is TBD pending DEL-071-02 and vendor ITP. | _CONTEXT.md (Anticipated Artifacts); location TBD |
| REQ-11 | Acceptance evidence SHALL include turnover records: mechanical completion certificate, punchlist (open/cleared), system handover sign-off. | _CONTEXT.md (Anticipated Artifacts) |
| REQ-12 | Acceptance SHALL confirm that the sweet-gas purge / methyl-mercaptan hazard review has been conducted, or carry the gap as an open item. Fuel gas SHALL NOT be assumed safe across all operating modes for purge service without supporting review. | 4-25_Deepcut_DBM.md sec. Emergency Buyback and Purge |
| REQ-13 | Open items requiring human ruling (e.g., shared 03-25/04-25 fuel-gas demand split and boundary isolation philosophy per CONFLICT-1; acid-gas dilution sizing inclusion per CONFLICT-2) SHALL NOT be silently closed during acceptance; unresolved items SHALL be carried as TBD on the acceptance checklist. | 4-25_Deepcut_DBM.md sec. Fuel Gas Basis; sec. Emergency Buyback and Purge |
| REQ-14 | The acceptance package SHALL cite source slices for every accepted requirement to preserve audit traceability. | K-PROV-1 (governance) — ASSUMPTION as a deliverable-level invariant |

## Standards

| Standard | Applicability | Location |
|---|---|---|
| Project EPC SOW (DEL-071-01) | Primary contractual basis for vendor acceptance | location TBD (DEL-071-01 not yet drafted at run time) |
| Project Package Datasheet (DEL-071-02) | Technical basis for acceptance | location TBD (DEL-071-02 not yet drafted) |
| 26020-Package_Requirements.docx package heading 25 | Source-of-truth package requirement statements | location TBD (binary source not parsed) |
| National Building Code of Canada 2020 (Dawson Creek IDF data) | Site environmental loading basis for package buildings and structures | 4-25_Deepcut_DBM.md sec. 2.2 Site Data Basis (climate-data basis) |
| BC Building Code 2018 | Building code basis (nearest site Dawson Creek, BC) | 4-25_Deepcut_DBM.md sec. 2.2 Site Data Basis |
| Applicable Canadian provincial mechanical, pressure equipment, and electrical codes for British Columbia | Acceptance validation of regulatory compliance | location TBD (no clause-level text in accessible source slices) |

## Verification

| Req | Verification Method |
|---|---|
| REQ-1, REQ-2, REQ-3 | Document review against DEL-071-01/02/03; conformance log entries |
| REQ-4 | Cross-check of vendor submittals against DEL-071-05 register |
| REQ-5 | Inspection of vendor design records (datasheets, calculations) confirming fuel-gas inlet envelope |
| REQ-6 | Inspection of vendor structural/environmental design records confirming ambient, snow, wind, and elevation basis |
| REQ-7 | Review of regulator arrangement drawings, isolation provisions, and start-gas regulator type certification |
| REQ-8 | Review of emergency-generator supply piping, vessel sizing, and pressure-classification compliance |
| REQ-9 | Review of scrubber sizing calculation, heater datasheet, and control narrative |
| REQ-10 | Witnessed/reviewed FAT/SAT/test reports; NDE certificates; pressure-test packets |
| REQ-11 | Mechanical completion certificate; punchlist register; signed turnover transmittal |
| REQ-12 | Evidence that the sweet-gas purge / methyl-mercaptan hazard review has been executed (or recorded as open item) |
| REQ-13 | Acceptance checklist entries marked TBD or NEEDS_HUMAN_RULING with traceable references |
| REQ-14 | Audit of acceptance package for source citations |

## Documentation

The acceptance deliverable comprises:

- Vendor document review log (per REQ-4)
- Package acceptance checklist (covering REQ-1 through REQ-13)
- Test/inspection evidence dossier (per REQ-10)
- Turnover evidence dossier (per REQ-11)
- Hazard-review confirmation record (per REQ-12)
- Open-items register (per REQ-13)
