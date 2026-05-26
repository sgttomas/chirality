# Datasheet: DEL-051-06 — EPC Vendor Package Review and Acceptance

> Descriptive datasheet capturing the identity, scope-of-acceptance attributes, conditions of acceptance, constructional/operational evidence categories, and authoritative references for the EPC Integrator's review-and-acceptance of the PKG-051 Process Heat Medium Unit vendor package.

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | DEL-051-06_epc-vendor-package-review-and-acceptance | `_CONTEXT.md` Identity |
| Name | EPC Vendor Package Review and Acceptance | `_CONTEXT.md` Identity |
| Parent Package ID | PKG-051 | `_CONTEXT.md` Identity |
| Workbook Row | 79 (Workbook Packages) | `_CONTEXT.md` Source Reference |
| Package Name | Process Heat Medium Unit | `_CONTEXT.md` Identity |
| Discipline | Mechanical | `_CONTEXT.md` Identity |
| Deliverable Type | EPC Vendor Package Acceptance | `_CONTEXT.md` Identity |
| Responsible Party | EPC Integrator (lead) with Package Vendor input | `_CONTEXT.md` Identity |
| Covers Scope Items | SOW-0165; SOW-0166; SOW-0167; SOW-0168 | `_CONTEXT.md` |
| Supports Objectives | OBJ-001; OBJ-004; OBJ-005; OBJ-006; OBJ-007; OBJ-008; OBJ-009; OBJ-010 (ASSUMPTION: package-grouped objective mapping) | `_CONTEXT.md`; PACKAGE_HEURISTIC |
| Source Reference | Workbook Packages row 79; 26020-Package_Requirements.docx package heading 6 | `_CONTEXT.md` |

## Attributes

| Attribute | Value | Source / Notes |
|---|---|---|
| Acceptance subject | PKG-051 Process Heat Medium Unit vendor package (single unified loop, 220 deg C heat-medium service) | DBM-Deepcut sec "Heat Medium Basis" (location: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, lines ~1945-2003) |
| Vendor scope under review | Heat Medium Heater Package (510-1) and integrated heat-medium loop equipment (heater H-5170-1, pump module, expansion tank, pop tank) | DBM-Deepcut sec "Heat Medium Pressure and Equipment" |
| Acceptance authority | EPC Integrator (lead) with Package Vendor input | `_CONTEXT.md` |
| Acceptance basis documents | EPC Scope of Work (DEL-051-01); EPC Package Datasheet (DEL-051-02); EPC Construction Work Package (DEL-051-03); Vendor Engineered Equipment Package (DEL-051-04); Vendor Document Turnover Package (DEL-051-05) | DELIVERABLE_REGISTER.csv rows 438-442 |
| Acceptance output categories | Vendor document review log; package acceptance checklist; test/inspection evidence; turnover evidence | `_CONTEXT.md` Anticipated Artifacts |
| Governing facility-level codes | API-560 (heat medium heater); API STD 527 (relief valve seat tightness — acceptance basis); BCER Oil and Gas Processing Facility Regulation (flare radiation) | DBM-Deepcut |
| Vendor-confirmation items the acceptance must close | Fluid rating to maximum bulk temperature; heater minimum-flow 85% basis; circulation rates; pump sparing basis; pop-tank sour rupture review | DBM-Deepcut sec "Heat Medium Basis" |

## Conditions

Operating and design conditions that bound vendor-package acceptance:

| Condition | Value | Source |
|---|---|---|
| Heat medium fluid | Brenntag Petrotherm | DBM-Deepcut line 1951 |
| Maximum normal operating temperature | 428 deg F / 220 deg C | DBM-Deepcut Heat Medium Temperature Parameter table |
| Maximum bulk fluid temperature | 599 deg F / 315 deg C | DBM-Deepcut Heat Medium Temperature Parameter table |
| Pour point | TBC (vendor to confirm) | DBM-Deepcut Heat Medium Temperature Parameter table |
| Maximum tubeskin/film temperature | TBC (vendor to confirm) | DBM-Deepcut |
| Assumed start-up temperature | 68 deg F / 20 deg C | DBM-Deepcut |
| Heater minimum-flow assumption | 85% of design flow (vendor to confirm) | DBM-Deepcut line 2000 |
| Heater pressure drop assumption | 25 psid / 172 kPad | DBM-Deepcut line 2000 |
| Heater design duty | 1.25 x winter steady-state design duty | DBM-Deepcut line 1998 |
| Heater sparing basis | 1 x 125% (pending review of 2 x 62.5% or 3 x 41.7%) | DBM-Deepcut line 1998 |
| Heater area classification | General Purpose | DBM-Deepcut line 2000 |
| Total required heat medium duty | ~21,913 kW / ~74.8 MM BTU/h (winter design) | DBM-Deepcut Heat Medium Users table |
| Minimum design pressure (HM-containing components) | 350 psig / 2413 kPag | DBM-Deepcut line 1983 |
| Estimated pump-discharge pressure | 100 psig / 695 kPag (75 psid pump differential, TBC) | DBM-Deepcut line 1983 |
| Pop tank size | ~600 bbl, normally empty, SG 1.00 (TBC) | DBM-Deepcut line 2002 |
| Site/winter design ambient | TBD | not in accessible sources |

## Construction

Evidence categories the acceptance package must compile:

| Evidence Class | Required Items |
|---|---|
| Vendor document register & submittals | Vendor document register; submittal log; transmittal records; comment-resolution log (linked to DEL-051-05). |
| Design verification | Heater datasheet; pump datasheet; pop-tank datasheet; expansion-tank datasheet; PSV sizing/seat-tightness records (API STD 527 basis); fluid suitability confirmation at 220 deg C bulk temperature. |
| Fabrication / shop-test evidence | Material test reports (MTRs); welder qualification records; NDE reports; hydrotest records; performance/string test records for heater and pump module. |
| Site/field installation evidence | Receipt inspection; installation check sheets against DEL-051-03 (Construction Work Package); tie-in punchlist; insulation/heat-trace verification per DBM Heat Medium Basis. |
| Commissioning / start-up evidence | Loop integrity (cleanliness, flushing, fluid fill, sampling); functional test of heater burner management and 4:1 turndown; pump module start under cold-start (15 deg C) condition; PSV pop test; pop-tank level-switch test. |
| Turnover evidence | Final vendor document package; spare-parts list; warranty letter; calibration records; acceptance-checklist sign-off; outstanding-items (punchlist) log; handover certificate. |

## References

- `_CONTEXT.md` (identity, scope, anticipated artifacts).
- `_REFERENCES.md` (authoritative decomposition basis pointers).
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` (rows 438-443).
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — Heat Medium Basis (lines ~1945-2003) — primary accessible source slice.
- `_Sources/26020-Package_Requirements.docx` — package heading 6 — **location TBD** (binary, not locally readable as text).
- `_Sources/26020-Packages_Interfaces_4_export.xlsx` — Package 51 interface rows — **location TBD** (binary, not locally readable as text).
- Sibling EPC deliverables (acceptance basis): DEL-051-01 (Scope of Work), DEL-051-02 (Package Datasheet), DEL-051-03 (Construction Work Package), DEL-051-04 (Vendor Engineered Equipment Package), DEL-051-05 (Vendor Document Turnover Package).
