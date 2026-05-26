# Specification: DEL-091-06 — EPC Vendor Package Review and Acceptance

## Scope

This deliverable specifies the EPC Integrator review and acceptance of the Tank Farm Pump Building 3-25 vendor package (DEL-091-04) and its turnover documentation set (DEL-091-05) against the EPC anchor documents for PKG-091:

- Inclusions: vendor document review log; package acceptance checklist; vendor test/inspection evidence reconciliation; turnover record acceptance; integration verification against the EPC Scope of Work (DEL-091-01), Package Datasheet (DEL-091-02), and Construction Work Package (DEL-091-03).
- Exclusions: vendor-internal engineering execution (covered by DEL-091-04); origination of vendor documents (covered by DEL-091-05); LACT scope (third-party NRM; `3-25_Comp_and_Liquids_DBM.md` line 54); construction execution acts (procedure for installation is in DEL-091-03).

## Requirements

| ID | Requirement | Source / Status |
|---|---|---|
| R-01 | The vendor package shall be reviewed against DEL-091-01 (EPC Scope of Work), DEL-091-02 (Package Datasheet), and DEL-091-03 (Construction Work Package) prior to acceptance. | `_CONTEXT.md` Scope; ASSUMPTION |
| R-02 | A vendor document review log shall be maintained with one row per vendor document covering at least: document ID, revision, review status, review comments, disposition, and disposition date. | ASSUMPTION (industry-standard review log shape); detailed columns TBD pending `26020-Package_Requirements.docx` heading 44 |
| R-03 | The acceptance checklist shall reconcile each in-scope SOW item (SOW-0185, SOW-0186, SOW-0187, SOW-0188) to objective evidence prior to acceptance. | `_CONTEXT.md` Covers Scope Items; ASSUMPTION on checklist structure |
| R-04 | Test and inspection evidence supplied by the Package Vendor shall be reviewed for completeness against the vendor's document register (DEL-091-05). | `DELIVERABLE_REGISTER.csv` (DEL-091-05); ASSUMPTION |
| R-05 | Pump performance evidence shall demonstrate conformance to the Package Datasheet performance values, including condensate booster pump duty 165 m3/h at 35 m TDH per pump. | `3-25_Comp_and_Liquids_DBM.md` line 413 |
| R-06 | Pump building scope shall be reviewed for consistency with the active 03-25 Liquids Hub equipment basis (2 x 100% condensate booster pumps; three condensate loading pumps; 2 x 100% produced-water transfer pumps). | `3-25_Comp_and_Liquids_DBM.md` lines 40, 412-414, 429, 575-583 |
| R-07 | Interfaces to LACT (third-party NRM scope) shall be reviewed for facility-side tie-in only; LACT equipment shall not be carried inside the vendor package acceptance scope. | `3-25_Comp_and_Liquids_DBM.md` lines 54, 417 |
| R-08 | A turnover evidence package shall be assembled covering completed inspections, signed-off punch items, and required vendor documentation prior to handoff to construction (DEL-091-03) and commissioning. | ASSUMPTION (turnover convention); detail TBD |
| R-09 | Sour-service applicability for in-scope equipment shall be verified consistent with the 03-25 sour-service basis. | `3-25_Comp_and_Liquids_DBM.md` scope sections; ASSUMPTION on per-equipment classification |
| R-10 | Non-conformances identified during review shall be tracked to disposition (accept / accept-with-comment / reject / rework) with traceability to source clauses. | ASSUMPTION |

## Standards

| Standard | Applicability | Source |
|---|---|---|
| `26020-Package_Requirements.docx` package heading 44 | Package-level requirements binding on the vendor scope | `_REFERENCES.md`; location TBD (document not locally accessible as text) |
| Site code/jurisdiction requirements (BC, Canada) | Applicable by site location | `3-25_Comp_and_Liquids_DBM.md` line 85; specific code citations TBD |
| Industry pump and pressure-equipment standards (e.g., API 610, ASME B31.3) | TBD — likely applicable to in-scope pump and piping equipment | ASSUMPTION; clause-level requirements not derived without source access |

## Verification

| Requirement | Verification Approach |
|---|---|
| R-01 | Documented cross-walk between vendor package and DEL-091-01 / DEL-091-02 / DEL-091-03 sections, signed by EPC Integrator |
| R-02 | Sample review of vendor document review log against vendor register (DEL-091-05) |
| R-03 | Checklist row coverage audit against SOW-0185..0188 (location TBD in source) |
| R-04 | Documentation review and witness records reconciliation |
| R-05 | Witness or review of pump performance test (FAT) reports against datasheet values |
| R-06 | Equipment list reconciliation against the 03-25 DBM Liquids Hub equipment count basis |
| R-07 | Interface drawing/P&ID review at the LACT tie-in boundary |
| R-08 | Turnover package completeness review prior to handoff |
| R-09 | Material/service class verification on equipment datasheets and welder/inspection records |
| R-10 | Non-conformance log review at acceptance gate |

## Documentation

Required acceptance artifacts (per `_CONTEXT.md` Anticipated Artifacts):

- Vendor document review log
- Package acceptance checklist
- Test/inspection evidence (FAT, hydrostatic test, NDE, instrumentation calibration — exact set TBD)
- Turnover evidence (turnover index, redlines, signed checklists, punch list disposition)

Cross-references:

- DEL-091-01 EPC Scope of Work
- DEL-091-02 EPC Package Datasheet
- DEL-091-03 Construction Work Package
- DEL-091-04 Vendor Engineered Equipment Package
- DEL-091-05 Vendor Document Turnover Package
