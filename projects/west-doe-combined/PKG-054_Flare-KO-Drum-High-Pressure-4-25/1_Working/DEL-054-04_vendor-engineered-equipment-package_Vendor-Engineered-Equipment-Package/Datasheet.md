# Datasheet: DEL-054-04 Vendor Engineered Equipment Package

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | DEL-054-04_vendor-engineered-equipment-package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-054-04_vendor-engineered-equipment-package` |
| Deliverable name | Vendor Engineered Equipment Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-054-04_vendor-engineered-equipment-package` |
| Parent package | PKG-054 - Flare KO Drum (High Pressure) 4-25 | `_CONTEXT.md` |
| Workbook ID / row | 54 / Workbook Packages row 55 | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Discipline | Mechanical | `_CONTEXT.md` |
| Deliverable type | Vendor Package Production Unit | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible party | Package Vendor (engineering/design/equipment) with EPC Integrator integration review | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Covered scope items | SOW-0075, SOW-0076, SOW-0077, SOW-0078 | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Supported objectives | OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 | `_CONTEXT.md` (ASSUMPTION - package-grouping heuristic per OBJECTIVE_ASSOCIATION_MODE=PACKAGE_HEURISTIC) |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package subject | High-Pressure Flare Knock-Out Drum production unit for facility 04-25 (Deepcut) | `_CONTEXT.md`; `4-25_Deepcut_DBM.md` Sec. flare system |
| Anchoring tag - vessel | H.P. FLARE K.O. DRUM (V-4100-1) | `4-25_Deepcut_DBM.md` line 2028, 2534 |
| Anchoring tag - pump | HP FLARE K.O. DRUM TRANSFER PUMP (P-4100-1) | `4-25_Deepcut_DBM.md` line 2028, 2360, 2534 |
| Vendor-supplied equipment scope | Vendor engineered physical equipment package and associated vendor design basis and datasheet set | `_CONTEXT.md` Anticipated Artifacts |
| Engineering input basis | EPC package Scope of Work (DEL-054-01) and Package Datasheet (DEL-054-02) | `_CONTEXT.md` Scope; `DELIVERABLE_REGISTER.csv` rows for DEL-054-01, DEL-054-02 |
| Integration review responsibility | EPC Integrator | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Service | High-pressure flare relief and blowdown collection, balance of plant outside the cryogenic unit and excluding LP equipment | `4-25_Deepcut_DBM.md` line 2028 |
| Relief header tie | 508 mm (20 in) HP flare relief header | `4-25_Deepcut_DBM.md` line 2028 |
| Downstream tie | HP flare combines with cryogenic flare downstream of both KO drums before the common HP/cryo stack | `4-25_Deepcut_DBM.md` line 2028 |
| Pump and truck-out provision | HP KO drum pump P-4100-1 with truck-out provided | `4-25_Deepcut_DBM.md` line 2028 |
| Heat tracing requirement | HP flare headers outside heated buildings shall be electrically heat traced and insulated for freeze protection, except PSV outlets that free-drain into the flare header | `4-25_Deepcut_DBM.md` line 2033 |
| Spacing - vegetation/fire hazards | Distance between flare tanks (including KO drums) and vegetation or other fire hazards >=10 m (32 ft) | `4-25_Deepcut_DBM.md` line 287 (OGAOM Sec. 9.6.15) |
| Declared upstream dependencies | None declared during PREPARATION | `_DEPENDENCIES.md` |
| Declared downstream dependencies | None declared during PREPARATION | `_DEPENDENCIES.md` |
| Relief volumes / final sizing basis | TBD - relief volumes remain to be determined during detailed design; preliminary Aspen Flare System Analyzer models support current header sizing | `4-25_Deepcut_DBM.md` line 2021 |
| Backpressure / shared 03-25/04-25 allocation | TBD - open items per DBM | `4-25_Deepcut_DBM.md` line 1834 |

## Construction

| Item | Value | Source |
|---|---|---|
| Construction-facing companion deliverable | DEL-054-03 Construction Work Package | `DELIVERABLE_REGISTER.csv` row `DEL-054-03_construction-work-package` |
| Document-turnover companion deliverable | DEL-054-05 Vendor Document Turnover Package | `DELIVERABLE_REGISTER.csv` row `DEL-054-05_vendor-document-turnover-package` |
| Acceptance / review companion deliverable | DEL-054-06 EPC Vendor Package Review and Acceptance | `DELIVERABLE_REGISTER.csv` row `DEL-054-06_epc-vendor-package-review-and-acceptance` |
| Material of construction - flare piping | SA-333 (HP flare stack/header MOC reference) | `4-25_Deepcut_DBM.md` line 2039 |
| Vendor engineering deliverables expected | Vendor package design basis, datasheets, equipment GA, P&ID extensions, instrumentation list, weld map, pressure test plan | ASSUMPTION - standard vendor package production unit content; specific list TBD pending Package Datasheet (DEL-054-02) issue |
| Detail-design verification items | Final vessel sizing, pump sizing, relief header tie-in elevations, freeze-protection extent, instrument and ESD interfaces | TBD - detailed values not available in the accepted Gate 7 snapshot; depends on DEL-054-02 issue |

## References

- `_CONTEXT.md` (deliverable context)
- `_REFERENCES.md` (authoritative decomposition basis and shared source root)
- `_DEPENDENCIES.md` (declared dependency view)
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv`
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (DBM source slices: flare system Sec. 2021-2039; spacing Sec. 287; equipment register lines 2360, 2533-2535)
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/26020-Package_Requirements.docx` (package heading 9; not locally text-extracted - location TBD at clause level)
