# Datasheet — DEL-093-06 EPC Vendor Package Review and Acceptance

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-093-06_epc-vendor-package-review-and-acceptance` | `_CONTEXT.md` |
| Name | EPC Vendor Package Review and Acceptance | `_CONTEXT.md` |
| ParentPackageID | `PKG-093` | `_CONTEXT.md` |
| PackageName | Tanks, Water (API 650) 3-25 | `_CONTEXT.md` |
| Discipline | Mechanical | `_CONTEXT.md` |
| Type | EPC Vendor Package Acceptance | `_CONTEXT.md` |
| ResponsibleParty | EPC Integrator (lead) with Package Vendor input | `_CONTEXT.md` |
| Source Reference | Workbook Packages row 95; `26020-Package_Requirements.docx` package heading 45 | `_CONTEXT.md` (location TBD in source slice) |

## Attributes

The deliverable is an EPC-Integrator-led acceptance record set for the produced-water (API 650) tank package supplied by the Package Vendor for facility 03-25. It collects vendor document review outcomes, integration acceptance findings, test/inspection evidence, and turnover readiness evidence against the EPC Scope of Work (`DEL-093-01`), Package Datasheet (`DEL-093-02`), and Construction Work Package (`DEL-093-03`).

| Attribute | Value | Source |
|---|---|---|
| Acceptance target package | Tanks, Water (API 650) 3-25 — produced-water storage tankage | DBM `3-25_Comp_and_Liquids_DBM.md` SEC-06 "Produced-Water Storage, Treatment, and Transfer" (lines 419-432) |
| Subject equipment count | Seven (7) × 3,800 bbl produced-water tanks (5 sour + 2 sweet) | DBM SEC-06 line 421, 425 |
| Tank construction basis | API-650 Modified atmospheric tanks, externally insulated and heated, Devchem 253 internal coating | DBM SEC-06 line 421 |
| Design specific gravity (tank) | 1.25 (TBC in source) | DBM SEC-06 line 421 |
| Pump fluid SG basis (related) | 1.18 (discrepancy with tank SG 1.25 to be closed in detailed design) | DBM SEC-06 line 421 |
| Auxiliary in-scope storage | One 400 bbl H2O2 storage tank | DBM SEC-06 line 428 |
| Vapour interface | VRU collects vapours from produced-water tank systems (2 × 100% VRU compressors) | DBM SEC-06 line 436 (cross-package) |
| Vacuum truck connection assumption | 2.75 m3/min per tank assumed | DBM SEC-06 line 430 |
| Minimum ambient design driver | -40 °C minimum ambient governs exposed equipment, packages, panels, instrumentation | DBM Site Basis line 145 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Service | Sour and sweet produced water; H2O2 treated stream auxiliary | DBM SEC-06 (lines 419-432) |
| Produced-water contaminants identified | Lube oils, hydrocarbons, TEG, H2S, caustic, mercaptans; list not comprehensive | DBM SEC-04 line 194 |
| Facility produced-water design flow (context) | 3,600 m3/d (22,644 bbl/d) total | DBM SEC-04 line 161 |
| Disposition routes | Pipeline or truck-out; downstream pipeline by others past facility tie-in | DBM SEC-06 line 432; SEC-04 line 214 |
| Ambient minimum | -40 °C | DBM Site Basis line 145 |
| Vendor responsibility split | Vendor engineers/designs/supplies; EPC reviews/accepts/integrates | OBJ-004; `DEL-093-04` register row |

## Construction (Acceptance Evidence Items)

These are the categories of evidence the acceptance record captures. Specific tank construction values reside in `DEL-093-02 Package Datasheet`; this deliverable verifies them, it does not redefine them.

| Evidence Item | Description | Source/Driver |
|---|---|---|
| Vendor document review log | Review status per item against Vendor Document Turnover Package (`DEL-093-05`) | OBJ-010; `DEL-093-05` register row |
| Package acceptance checklist | EPC verification that vendor scope conforms to SOW, Datasheet, and CWP | OBJ-004; `_CONTEXT.md` Anticipated Artifacts |
| Test and inspection evidence | API 650 hydrotest, NDE, coating verification (Devchem 253), insulation/heating function check | DBM SEC-06 line 421 (ASSUMPTION on specific test catalog — clause-level API 650 acceptance tests not extracted from local source slice; clause-level details `location TBD`) |
| Turnover evidence | Mechanical completion, punch lists, commissioning records, custody handoff to facility operations | OBJ-010 |
| Integration interface acceptance | Tie-ins to produced-water transfer pumps (2 × 100%), VRU header, vacuum truck connection, H2O2 system, EHT/heating, fire/gas, and shutdown signals | DBM SEC-06 lines 419-436; OBJ-006; OBJ-009 |
| Non-conformance and open-item closure | Documented dispositions for vendor NCRs and EPC-identified gaps | OBJ-010 |

## References

- `_CONTEXT.md`
- `_REFERENCES.md`
- DBM `3-25_Comp_and_Liquids_DBM.md` sections SEC-04, SEC-06, Site Basis, SEC-15
- Decomposition snapshot `GATE-07_Final_Published_2026-05-24`:
  - `DELIVERABLE_REGISTER.csv` rows `DEL-093-01` … `DEL-093-06`
  - `OBJECTIVE_REGISTER.csv` rows `OBJ-002` through `OBJ-010`
- Workbook Packages row 95; `26020-Package_Requirements.docx` package heading 45 (binary; not directly read — clause-level content `location TBD`)

## TBD / ASSUMPTION Inventory

- `TBD`: API 650 clause-level test/inspection acceptance criteria — not extracted from accessible source slices; reside in `26020-Package_Requirements.docx` heading 45 (binary, not read).
- `ASSUMPTION`: Specific vendor document categories captured by the review log mirror those listed in `DEL-093-05` register row (vendor document register; submittals; source-required documentation; turnover records).
- `TBD`: Final produced-water contaminant list (DBM SEC-04 line 194 explicitly states list is not comprehensive).
- `TBD`: Resolution of design SG 1.25 vs pump SG 1.18 discrepancy — to be closed during detailed design per DBM SEC-06 line 421.
- `ASSUMPTION` (PACKAGE_HEURISTIC): Objectives `OBJ-002`…`OBJ-010` apply via the package-grouping mapping; not deliverable-ID-explicit.
