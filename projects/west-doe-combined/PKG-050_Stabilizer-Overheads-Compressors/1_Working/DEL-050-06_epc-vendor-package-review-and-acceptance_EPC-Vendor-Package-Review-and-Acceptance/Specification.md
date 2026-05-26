# Specification — DEL-050-06 EPC Vendor Package Review and Acceptance

## Scope

This specification governs the EPC Integrator's review and acceptance of the Stabilizer Overheads Compressor (SOC) vendor package (PKG-050; tag `26020-01-PT-12-005`). It covers vendor document review, package acceptance against the EPC Scope of Work (DEL-050-01), EPC Package Datasheet (DEL-050-02), and Construction Work Package (DEL-050-03), and compilation of integration handoff readiness evidence (test, inspection, and turnover).

**In scope**
- Review of vendor-submitted documentation registered in DEL-050-05.
- Verification that the vendor-engineered equipment package (DEL-050-04) conforms to EPC-defined scope, datasheet, and construction interfaces.
- Compilation of acceptance, test/inspection, and turnover evidence per `_CONTEXT.md` Anticipated Artifacts.

**Out of scope**
- EPC Scope of Work authoring (DEL-050-01).
- Package Datasheet authoring (DEL-050-02).
- Construction Work Package authoring (DEL-050-03).
- Vendor engineering, design, fabrication, or supply (DEL-050-04 vendor responsibility).
- Vendor document register production (DEL-050-05 vendor responsibility).
- Facility-level integration design beyond the package boundary (other PKG-* deliverables).

## Requirements

Each requirement is the EPC Integrator's acceptance obligation for this deliverable. SourceRef cites the originating source slice.

| ID | Requirement | SourceRef |
|---|---|---|
| R-01 | Confirm that two (2) 100% Ariel KBC/6 four-stage separable reciprocating compressor packages are supplied as the vendor equipment under DEL-050-04. | DBM-Deepcut/4-25_Deepcut_DBM.md §SOC Basis; SCOPE_LEDGER SOW-0174, SOW-0175 |
| R-02 | Verify driver basis: 4000 V, 3-phase, 60 Hz, 2,700 hp / 2,013 kW, 8-pole ~891 rpm, 3:1 inverter turndown, NEMA MG 1, Class F insulation with Class B rise, non-sparking bidirectional cooling fans; confirm "No Toshiba motors" exclusion enforced. | DBM-Deepcut/4-25_Deepcut_DBM.md §SOC Basis and §Controls/Protection; SCOPE_LEDGER SOW-0175, SOW-0176 |
| R-03 | Verify SOC design pressures: stage 1 suction 345 kPag (50 psig); stage 4 discharge 7,585 kPag (1,100 psig); inter-stage suction/discharge values per source table. | DBM-Deepcut/4-25_Deepcut_DBM.md §SOC stage pressure table; SCOPE_LEDGER SOW-0174, SOW-0176 |
| R-04 | Verify stage design capacities: Stage 1 = 2.5 MMSCFD; Stage 2 = 5 MMSCFD; Stage 3 = 17 MMSCFD; Stage 4 = 17 MMSCFD. | DBM-Deepcut/4-25_Deepcut_DBM.md §SOC capacity table; SCOPE_LEDGER SOW-0176 |
| R-05 | Verify MAWP basis: stage 1 suction ≥1,723 kPag at 149 °C; stage 4 discharge ≥9,101 kPag at 177 °C; require vendor to close out other-stage MAWPs (TBC per source). | DBM-Deepcut/4-25_Deepcut_DBM.md §SOC MAWP table; SCOPE_LEDGER SOW-0176 |
| R-06 | Verify aerial intercooler outlet temperatures (Stage 1: 65.56 °C; Stage 2: 87.78 °C; Stage 3: 65.56 °C; Stage 4: 77.35 °C) remain above hydrocarbon dewpoint; require explicit reviewer disposition on the narrow stage-2 cooler-to-dewpoint margin. | DBM-Deepcut/4-25_Deepcut_DBM.md §SOC cooler table |
| R-07 | Verify suction-scrubber configuration: 1st stage two-phase cyclonic element; 2nd/3rd/4th stage two-phase with mist pads (not mesh/vane); max imperial K factor 0.25 with pressure deration. | DBM-Deepcut/4-25_Deepcut_DBM.md §Controls/Protection; SCOPE_LEDGER SOW-0175 |
| R-08 | Verify recycle and start-up provisions: single 100% recycle valve sized for 40% speed and low discharge pressure; recycle fail-position TBC (require vendor disposition); start-up bypass quarter-turn full-port automated ball valve; equalized-versus-normal start mode evaluated. | DBM-Deepcut/4-25_Deepcut_DBM.md §Controls/Protection |
| R-09 | Verify blowdown architecture: SOC package blowdown controlled by compressor unit control panel; suction-header blowdowns upstream of side-stream PCVs wired to balance-of-plant control system; valve locations recorded for review during detailed engineering. | DBM-Deepcut/4-25_Deepcut_DBM.md §Controls/Protection |
| R-10 | Verify auxiliary scope is included: packing vent/drain seal pot (DP 101 kPag); vacuum pump; seal-pot waste-oil transfer pump; sweet-gas purge connection at stage-1 suction downstream of inlet PCV; circulating lube-oil heater; warm-air recirculation plus plenum heater on coolers; automated louver control. | DBM-Deepcut/4-25_Deepcut_DBM.md §Controls/Protection; SCOPE_LEDGER SOW-0175 |
| R-11 | Verify modularization and shipping basis: shop assembly, disassembly into three pieces for shipment, self-framing buildings erected on site; record vendor position on single-assembly shipment. | DBM-Deepcut/4-25_Deepcut_DBM.md §SOC Basis |
| R-12 | Verify facility-side "by others" interfaces are excluded from vendor scope: package shipping, installation on piles, tie-in piping, electrical connections, mounting platform, and stairs. | SCOPE_LEDGER SOW-0176 |
| R-13 | Verify package interfaces are addressed across the 13 interface types listed in PACKAGE_REGISTER row 81 (Process Piping; Utility Piping; Relief/Flare/Vent; Drain/Containment; Electrical Power; EHT; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Building HVAC/Services; Fire & Gas/Safety Systems; Maintenance Access; Structural/Foundations/Supports). | PACKAGE_REGISTER.csv row 81 |
| R-14 | Verify SOC-side process interfaces are reflected in vendor design: stabilizer flash/feed overheads, stabilizer tower overheads, MPFF overheads, 04-25 and 03-25 VRUs, amine flash gas, TEG glycol flash, pressurized caustic drain drum vapours, downstream amine inlet filter/coalescers, HP flare/blowdown, VRU suction header for packing vent recovery, electrical power, heat tracing/winterization, H2O/HCL drain headers. | DBM-Deepcut/4-25_Deepcut_DBM.md §Interfaces |
| R-15 | Produce and retain the four anticipated artifacts: vendor document review log, package acceptance checklist, test/inspection evidence, and turnover evidence. | `_CONTEXT.md` Anticipated Artifacts |
| R-16 | Do not certify, approve, or issue for reliance any vendor deliverable on the EPC Integrator's behalf where the underlying source slice is `TBC`/`TBD`; record the disposition as conditional and route to human ruling. | ASSUMPTION (governance default per repository convention); `_CONTEXT.md` ResponsibleParty framing |

## Standards

| Standard / Code Reference | Applicability | Source slice |
|---|---|---|
| NEMA MG 1 | SOC compressor motors (R-02) | DBM-Deepcut/4-25_Deepcut_DBM.md §Controls/Protection |
| Workbook Packages row 81; `26020-Package_Requirements.docx` package heading 5 | Authoritative SOC package requirements | location TBD (source not locally accessible); cited per `_REFERENCES.md` |
| `26020-01-PT-RFQ-12-005_Stabilizer_OH_Comp.docx` (bid/RFQ source) | SOC vendor scope/requirements | location TBD (not locally accessible) |
| API 618, API 11P, API 670, API 614, etc. | Applicable industry standards typically governing reciprocating compressor packages | TBD — not confirmed in accessible sources; ASSUMPTION pending vendor datasheet review |

## Verification

| Requirement | Verification Approach |
|---|---|
| R-01..R-05 | Cross-check vendor datasheets and nameplate data against source tables. Record evidence in package acceptance checklist. |
| R-06 | Review vendor thermal/HX calculations; confirm dewpoint margin documented. Flag stage 2 explicitly. |
| R-07 | Review scrubber datasheets and sizing calculations. |
| R-08 | Witness control-narrative review and FAT recycle-valve stroke/timing tests; confirm recycle valve fail-position disposition is recorded. |
| R-09 | Review blowdown valve schedule and control narrative; verify with I&C functional test. |
| R-10 | Verify auxiliary equipment inclusion via vendor bill of materials, P&IDs, and FAT walkdown. |
| R-11 | Confirm shipping/assembly plan in vendor execution documents. |
| R-12 | Confirm scope split in vendor Scope-of-Supply versus EPC Construction Work Package. |
| R-13 | Cross-reference vendor interface documents against PKG-050 interface list. |
| R-14 | Cross-reference vendor P&IDs and tie-in schedule against §Interfaces source slice. |
| R-15 | Confirm all four anticipated artifacts are produced and filed in the deliverable folder before status advances beyond INITIALIZED. |
| R-16 | Status checkpoint at each phase boundary; any unresolved `TBC`/`TBD` is logged in the acceptance checklist with a NEEDS_HUMAN_RULING note. |

## Documentation

The following documents shall be produced and retained in this deliverable folder:

- Vendor document review log
- Package acceptance checklist (verification matrix)
- Test and inspection evidence index (with pointers into DEL-050-05 turnover set)
- Turnover evidence index (mechanical completion, OEM data, calibration, lube-oil, spares, training)
- Conflict log entries (when source basis disagreements arise) — see `Guidance.md`
