# Datasheet — DEL-060-06 EPC Vendor Package Review and Acceptance

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | DEL-060-06_epc-vendor-package-review-and-acceptance | `_CONTEXT.md` |
| Name | EPC Vendor Package Review and Acceptance | `_CONTEXT.md` |
| ParentPackageID | PKG-060 | `_CONTEXT.md` |
| PackageName | Tank Farm Pump Building 4-25 | `_CONTEXT.md` |
| Workbook row | Packages row 85 | `_CONTEXT.md` Source Reference |
| Package heading | 26020-Package_Requirements.docx heading 15 (binary) | `_CONTEXT.md` Source Reference |
| Discipline | Mechanical | `_CONTEXT.md` |
| Type | EPC Vendor Package Acceptance | `_CONTEXT.md` |
| ResponsibleParty | EPC Integrator (lead) with Package Vendor input | `_CONTEXT.md` |
| Covers Scope Items | SOW-0189, SOW-0190, SOW-0191, SOW-0192 | `_CONTEXT.md` |
| Supports Objectives (ASSUMPTION: PACKAGE_HEURISTIC) | OBJ-001, OBJ-003 through OBJ-010 | `_CONTEXT.md`; package-heuristic mapping |

ASSUMPTION: The package "Tank Farm Pump Building 4-25" (workbook Packages row 85) corresponds in the locally accessible DBM (`4-25_Deepcut_DBM.md`) to "Tank Farm Pump Building 2" at facility 04-25 (Deepcut), which houses condensate transfer, water transfer, sour-water treatment, process water transfer, and fresh caustic transfer pumps (DBM lines 2555, 2618-2622). The definitive package equipment list and clause-level acceptance requirements are `TBD — location TBD` pending readable extraction of `26020-Package_Requirements.docx` package heading 15.

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Review subject | EPC integrator acceptance of vendor-engineered package supplied for PKG-060 (Tank Farm Pump Building, 4-25 Deepcut facility) | `_CONTEXT.md` Scope |
| Package equipment scope (per DBM line 2555) | Condensate Transfer Pumps (x2); Water Transfer Pumps (x4); Sour Water Treatment Pumps (x2); Process Water Transfer Pumps (x2); Fresh Caustic Transfer Pumps (x2) | DBM 4-25_Deepcut_DBM.md line 2555 |
| Representative equipment tags | P-9210-1, P-9220-1 (condensate transfer); P-9290-1, P-9293-1 (water transfer); P-9231-1, P-9232-1 (sour water treatment); P-5317-1, P-5318-1 (process water transfer); P-6760-1, P-6765-1 (fresh caustic) | DBM lines 2618-2622 |
| Vendor package upstream inputs (declared) | DEL-060-04 Vendor Engineered Equipment Package; DEL-060-05 Vendor Document Turnover Package | Inferred from PKG-060 sibling deliverable folders |
| Vendor package upstream inputs (formal declaration) | None declared in `_DEPENDENCIES.md` | `_DEPENDENCIES.md` |
| Acceptance basis documents | EPC Scope of Work (DEL-060-01); Package Datasheet (DEL-060-02); Construction Work Package (DEL-060-03) | `_CONTEXT.md` Scope |
| Anticipated artifacts | Vendor document review log; package acceptance checklist; test/inspection evidence; turnover evidence | `_CONTEXT.md` Anticipated Artifacts |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Facility | 04-25 West Doe Deepcut expansion (300 MMSCFD deep cut sour gas plant) | DBM SEC-01 (lines 5-7); SEC-02 (line 16) |
| Site location | LSD 04-25-80-15W6, ~22.2 km north of Dawson Creek, BC | DBM SEC-01 (line 7); SEC-02 (line 17) |
| Plant elevation | 673 m AMSL | DBM SEC-02 (line 195) |
| Design ambient temperature | -40 deg C minimum; +35 deg C maximum | DBM SEC-02 (line 198) |
| Extreme ambient temperature | -49.2 deg C minimum; 38.9 deg C maximum | DBM SEC-02 (line 197) |
| -40 deg C governance | Governs exposed equipment, package buildings, control panels, instrumentation, field devices unless a more severe process or vendor condition applies | DBM SEC-02 (per project basis) |
| Wind pressure 1-in-50 yr | 0.40 kPa | DBM SEC-02 (line 202) |
| Maximum wind speed | 138 km/h (to be confirmed) | DBM SEC-02 (line 200) |
| Facility service class | Sour gas processing facility; combined-feed H2S 1 mol% (design) | DBM SEC-01 (line 5); SEC-05 (line 396) |
| Sour-service classification (pumps in package) | ASSUMPTION: sour-service compliance required for any wetted, pressure-containing components exposed to H2S-bearing process streams (condensate, sour water); `location TBD` for clause-level basis | DBM SEC-05 (sour-gas basis); 26020-Package_Requirements.docx heading 15 location TBD |
| Tank-farm separation basis | Distance between pressurized bullets and pump skid taking suction from bullets: 3.05 m (10 ft) per API 2510 | DBM SEC-02 (line 252) |

## Construction

| Item | Value | Source |
|---|---|---|
| Package deliverable content (general) | Datasheets, cause-and-effect inputs, utility load summaries, relief/load data, field tie-in lists, operating and design envelopes, sparing philosophy, materials and coating basis, maintenance access, shipped-loose item lists, vendor document registers | DBM SEC-09 (line 617) |
| Modularization basis | Tank Farm Pump Module shop-built (per facility modularization list) | DBM line 2817 ("920-1 Tank Farm Pump Module — Shop") |
| Pump package functional duties (representative) | Product recycle pump 1 x 100% manual start, tank farm pump module, ~20 m3/h at 80 m TDH (TBC); condensate skim pump 1 x 100% automatic on PW tank interface, ~20 m3/h at 80 m TDH (TBC) | DBM lines 1667-1672 |
| Building/electrical context | 860-1 600V General Area / Tank Farm Electrical Building (shop-built); 4.16 kV / 600 V General Area/Tank Farm/Process Electrical Building | DBM lines 2816, 2925 |
| Control system interface | Package values and general alarms replicated to BPCS; final data maps, permissive logic, trip interfaces, alarm priorities resolved during vendor integration | DBM SEC-12 (line 810) precedent applied |
| Cable tray basis | Tank farm includes field-run cable tray between main pipe racks, process skids, and electrical buildings | DBM line 2999 |
| Acceptance test/inspection requirements (specific) | TBD — `26020-Package_Requirements.docx` heading 15 slice not locally accessible as readable text |
| Turnover document content (specific) | TBD — `26020-Package_Requirements.docx` heading 15 slice not locally accessible as readable text |

## References

- `_CONTEXT.md` — deliverable identity and scope
- `_REFERENCES.md` — authoritative basis pointers
- `_DEPENDENCIES.md` — declared upstream/downstream (currently none)
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — locally accessible DBM source slices (SEC-01, SEC-02, SEC-05, SEC-09, SEC-12; equipment list lines 2555, 2618-2622; pump module lines 1667-1672)
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/26020-Package_Requirements.docx` — referenced authoritative source (binary; package heading 15 slice `location TBD`)
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/26020-Packages_Interfaces_4_export.xlsx` — workbook Packages row 85 (binary; readable slice `location TBD`)
- Gate 7 Final Published PROJECT_DECOMP snapshot — `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24`
