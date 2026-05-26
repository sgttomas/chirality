# Datasheet — DEL-050-06 EPC Vendor Package Review and Acceptance

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-050-06_epc-vendor-package-review-and-acceptance` | `_CONTEXT.md` |
| Name | EPC Vendor Package Review and Acceptance | `_CONTEXT.md` |
| Parent Package | `PKG-050` Stabilizer Overheads Compressors | `_CONTEXT.md`; PACKAGE_REGISTER.csv row 81 |
| Workbook Row | 81 (WBS 01) | PACKAGE_REGISTER.csv row 81 |
| Tag (package) | `26020-01-PT-12-005` Stabilizer Overheads Compressors | PACKAGE_REGISTER.csv row 81 |
| Discipline | Mechanical | `_CONTEXT.md` |
| Type | EPC Vendor Package Acceptance | `_CONTEXT.md` |
| Responsible Party | EPC Integrator (lead) with Package Vendor input | `_CONTEXT.md`; DELIVERABLE_REGISTER.csv row 455 |
| Covers Scope Items | SOW-0173; SOW-0174; SOW-0175; SOW-0176 | `_CONTEXT.md`; SCOPE_LEDGER.csv rows 174-177 |
| Supports Objectives | OBJ-001; OBJ-003; OBJ-004; OBJ-005; OBJ-006; OBJ-007; OBJ-008; OBJ-009; OBJ-010 (ASSUMPTION: PACKAGE_HEURISTIC, package-grouped objectives) | `_CONTEXT.md`; OBJECTIVE_DELIVERABLE_MAP.csv |

## Attributes (Subject Package Under Review)

The artifact produced by this deliverable is review and acceptance evidence for the Stabilizer Overheads Compressor (SOC) vendor package. The package under review has the following source-supported attributes:

| Attribute | Value | Source |
|---|---|---|
| Function | Compresses flashed and stabilizer overhead streams; final discharge routed to amine inlet filter/coalescers or recycled to first-stage suction | DBM-Deepcut/4-25_Deepcut_DBM.md §SEC-04 "Stabilizer Overheads Compressor Basis" |
| Quantity / Sparing | 2 x 100%, operating plus standby | DBM-Deepcut/4-25_Deepcut_DBM.md §SOC Basis table |
| Compressor model | Ariel KBC/6 four-stage reciprocating | DBM-Deepcut/4-25_Deepcut_DBM.md §SOC Basis; SCOPE_LEDGER SOW-0175 |
| Stages | 4 | DBM-Deepcut/4-25_Deepcut_DBM.md §SOC Basis |
| Driver | 4000 V, 3-phase, 60 Hz electric induction motor, 2,700 hp / 2,013 kW, 8-pole ~891 rpm, 3:1 inverter turndown; NEMA MG 1; non-sparking bidirectional cooling fans; Class F insulation with Class B rise; no Toshiba motors | DBM-Deepcut/4-25_Deepcut_DBM.md §SOC Basis and §Controls/Protection; SCOPE_LEDGER SOW-0175, SOW-0176 |
| Suction pressure (design, stage 1) | 345 kPag (50 psig) | DBM-Deepcut/4-25_Deepcut_DBM.md §SOC Basis; SCOPE_LEDGER SOW-0174 |
| Discharge pressure (design, stage 4) | 7,585 kPag (1,100 psig) | DBM-Deepcut/4-25_Deepcut_DBM.md §SOC Basis; SCOPE_LEDGER SOW-0174 |
| Inter-stage suction/discharge | Stage 1: 305.67 / 799.09 kPag; Stage 2: 723.48 / 1696.74 kPag; Stage 3: 1594.72 / 3600.16 kPag; Stage 4: 3423.59 / 8353.83 kPag | DBM-Deepcut/4-25_Deepcut_DBM.md §SOC stage pressure table |
| Stage design capacity | Stage 1: 2.5 MMSCFD; Stage 2: 5 MMSCFD; Stage 3: 17 MMSCFD; Stage 4: 17 MMSCFD | DBM-Deepcut/4-25_Deepcut_DBM.md §SOC capacity table; SCOPE_LEDGER SOW-0176 |
| Stage design temperature | 149 °C at each stage suction; 177 °C at each stage discharge | DBM-Deepcut/4-25_Deepcut_DBM.md §SOC MAWP table; SCOPE_LEDGER SOW-0176 |
| Stage MAWP | Stage 1 suction: 1,723 kPag; Stage 4 discharge: 9,101 kPag minimum; other stage MAWPs: TBC | DBM-Deepcut/4-25_Deepcut_DBM.md §SOC MAWP table; SCOPE_LEDGER SOW-0176 |
| Cooler discharge temperatures | Stage 1: 65.56 °C; Stage 2: 87.78 °C; Stage 3: 65.56 °C; Stage 4: 77.35 °C | DBM-Deepcut/4-25_Deepcut_DBM.md §SOC cooler table |
| Suction scrubbers | 1st stage two-phase with cyclonic element; 2nd/3rd/4th stage two-phase with demister/mist pad; max imperial K factor 0.25 plus pressure deration | DBM-Deepcut/4-25_Deepcut_DBM.md §Controls/Protection; SCOPE_LEDGER SOW-0175 |
| Auxiliaries (vendor scope) | Aerial intercoolers with warm-air recirculation and plenum heater; packing vent/drain seal pot; vacuum pump; seal-pot waste-oil transfer pump; sweet-gas purge connection; circulating lube-oil heater | DBM-Deepcut/4-25_Deepcut_DBM.md §Controls/Protection; SCOPE_LEDGER SOW-0175 |

## Conditions (Acceptance Conditions for This Deliverable)

| Condition | Value | Source |
|---|---|---|
| EPC anchor inputs to verify against | EPC Scope of Work (DEL-050-01); EPC Package Datasheet (DEL-050-02); Construction Work Package (DEL-050-03) | `_CONTEXT.md` Scope; DELIVERABLE_REGISTER.csv rows 450-452 |
| Vendor inputs accepted | Vendor Engineered Equipment Package (DEL-050-04); Vendor Document Turnover Package (DEL-050-05) | DELIVERABLE_REGISTER.csv rows 453-454 |
| Modularization | Shop-assembled, disassembled into three pieces for shipping; self-framing buildings erected in field; single-assembly shipment to be reviewed | DBM-Deepcut/4-25_Deepcut_DBM.md §SOC Basis |
| By-others interfaces (not vendor scope) | Shipping packages to site; installation on piles; tie-in piping; electrical connections; mounting platform and stairs | SCOPE_LEDGER SOW-0176 |
| Applicable interface types | Process Piping; Utility Piping; Relief/Flare/Vent; Drain/Containment; Electrical Power; EHT; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Building HVAC/Services; Fire & Gas/Safety Systems; Maintenance Access; Structural/Foundations/Supports | PACKAGE_REGISTER.csv row 81 |

## Construction (Acceptance Artifact Construction)

The deliverable assembles the following artifacts (per `_CONTEXT.md` Anticipated Artifacts):

| Artifact | Description | Status |
|---|---|---|
| Vendor document review log | Itemized record of vendor documents reviewed (from DEL-050-05 register/submittals), with reviewer disposition, comments, and close-out reference | TBD (populated during execution) |
| Package acceptance checklist | Verification matrix mapping EPC requirements (DEL-050-01/02/03) and source SOW items (SOW-0173 through SOW-0176) to vendor evidence and pass/fail/conditional disposition | TBD (populated during execution) |
| Test and inspection evidence | Compiled records (FAT/SAT, NDE, hydrotest, motor tests, control function tests) referenced from the vendor turnover set | TBD (populated during execution) |
| Turnover evidence | Compiled turnover records (mechanical completion, OEM data books, calibration records, lube-oil samples, spares lists, training records) referenced from the vendor turnover set | TBD (populated during execution) |

## References

- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` (deliverable-local)
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — §SEC-04 "Inlet, Separation, Stabilization, and Stabilizer Overheads Basis" (Stabilizer Overheads Compressor Basis subsection)
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` — context for compressor package construction conventions at the West Doe complex
- PACKAGE_REGISTER.csv row 81 (GATE-07_Final_Published_2026-05-24)
- DELIVERABLE_REGISTER.csv row 455 (GATE-07_Final_Published_2026-05-24)
- SCOPE_LEDGER.csv rows 174-177 (SOW-0173..0176)
- OBJECTIVE_DELIVERABLE_MAP.csv (PKG-050 entries)
- Authoritative bid/RFQ source not locally accessible (location TBD): `26020-01-PT-RFQ-12-005_Stabilizer_OH_Comp.docx`
- Authoritative package requirements source not locally accessible (location TBD): `26020-Package_Requirements.docx` package heading 5
