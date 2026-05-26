# Datasheet — DEL-046-06 EPC Vendor Package Review and Acceptance

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | DEL-046-06_epc-vendor-package-review-and-acceptance | `_CONTEXT.md` |
| Name | EPC Vendor Package Review and Acceptance | `_CONTEXT.md` |
| ParentPackageID | PKG-046 | `_CONTEXT.md` |
| PackageName | Acid Gas Compressors | `_CONTEXT.md` |
| Workbook row | Packages row 48 | `_CONTEXT.md` Source Reference |
| Discipline | Mechanical | `_CONTEXT.md` |
| Type | EPC Vendor Package Acceptance | `_CONTEXT.md` |
| ResponsibleParty | EPC Integrator (lead) with Package Vendor input | `_CONTEXT.md` |
| Covers Scope Items | SOW-0047, SOW-0048, SOW-0049, SOW-0050 | `_CONTEXT.md` |
| Supports Objectives (ASSUMPTION: PACKAGE_HEURISTIC) | OBJ-001, OBJ-003 through OBJ-010 | `_CONTEXT.md`; package-heuristic mapping |

ASSUMPTION: The package title "Acid Gas Compressors" appears at workbook row 48; the locally accessible DBM (3-25_Comp_and_Liquids_DBM.md) treats acid gas as routed to the NRM disposal well (line 51, 208) and identifies reciprocating *sour-gas* inlet compressor packages (SEC-04, SEC-05) rather than dedicated acid-gas compressor packages. A definitive equipment-tag list for "Acid Gas Compressors" is `TBD — location TBD` pending the actual `26020-Package_Requirements.docx` package heading 1 slice (referenced in `_CONTEXT.md` but only available in binary `.docx` form locally).

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Review subject | EPC integrator acceptance of vendor-engineered package supplied for PKG-046 | `_CONTEXT.md` scope |
| Vendor package upstream inputs (declared) | DEL-046-04 Vendor Engineered Equipment Package; DEL-046-05 Vendor Document Turnover Package | Inferred from PKG-046 sibling deliverable folders |
| Vendor package upstream inputs (formal declaration) | None declared in `_DEPENDENCIES.md` | `_DEPENDENCIES.md` |
| Acceptance basis documents | EPC Scope of Work (DEL-046-01); Package Datasheet (DEL-046-02); Construction Work Package (DEL-046-03) | `_CONTEXT.md` scope |
| Anticipated artifacts | Vendor document review log; package acceptance checklist; test/inspection evidence; turnover evidence | `_CONTEXT.md` Anticipated Artifacts |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Facility | 03-25 West Doe Compressor Station and Liquids Hub | DBM SEC-01 / SEC-02 |
| Site location | LSD 03-25-80-15 W6M, north of Dawson Creek, BC | DBM SEC-02 |
| Site elevation | 673 m AMSL | DBM SEC-02 |
| Design ambient temperature range | -40 deg C to +35 deg C | DBM SEC-02 |
| -40 deg C governance | Governs exposed equipment, package buildings, control panels, instrumentation, field devices unless a more severe process or vendor condition applies | DBM SEC-02 |
| Wind pressure 1-in-50 yr | 0.40 kPa | DBM SEC-02 |
| Maximum wind speed | 138 km/h (TBC) | DBM SEC-02 |
| H2S in inlet compressor composition | ~0.296 mol% (sour service) | DBM SEC-05 |
| Acceptance equipment H2S service class | Sour service per DBM compressor composition basis | DBM SEC-05 (ASSUMPTION extended to PKG-046 acid-gas service: location TBD) |

## Construction

| Item | Value | Source |
|---|---|---|
| Package deliverable content (general) | Datasheets, cause-and-effect inputs, utility load summaries, relief/load data, field tie-in lists, operating and design envelopes, sparing philosophy, materials and coating basis, maintenance access, shipped-loose item lists, vendor document registers | DBM SEC-09 (line 617) |
| Modularization basis (related package precedent) | Inlet compressor packages modularized for shop assembly; disassembled into three pieces for transport; field-installed in self-framing buildings | DBM SEC-05 (line 294) |
| Control system interface | Compression unit controls are standalone Unit Control Systems; values and general alarms replicated to BPCS; final data maps, permissive logic, trip interfaces, alarm priorities resolved during vendor integration | DBM SEC-12 (line 810) |
| Acceptance test/inspection requirements (specific) | TBD — `26020-Package_Requirements.docx` heading 1 slice not locally accessible as readable text |
| Turnover document content (specific) | TBD — `26020-Package_Requirements.docx` heading 1 slice not locally accessible as readable text |

## References

- `_CONTEXT.md` — deliverable identity and scope
- `_REFERENCES.md` — authoritative basis pointers
- `_DEPENDENCIES.md` — declared upstream/downstream (currently none)
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` — locally accessible DBM source slices (SEC-01, SEC-02, SEC-04, SEC-05, SEC-09, SEC-12)
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/26020-Package_Requirements.docx` — referenced authoritative source (binary; package heading 1 slice `location TBD`)
- Gate 7 Final Published PROJECT_DECOMP snapshot — `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24`
