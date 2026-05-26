# Specification: DEL-094-05 — Vendor Document Turnover Package

## Scope

This specification governs the Vendor Document Turnover Package for PKG-094 "Tanks, Caustic (API 650) 3-25". The deliverable comprises:

- the vendor document register (master index of all vendor documentation produced for the package),
- vendor document submittals (the controlled documents themselves),
- source-required vendor documentation (i.e., the rows of the source vendor document table in `_Sources/26020-Package_Requirements.docx` package heading 46), preserved as artifacts/evidence rather than separate deliverables,
- turnover records (certifications, manuals, spares, test/inspection evidence, nameplate / code records as applicable).

**Excluded from this deliverable:**

- Vendor engineering/design/datasheet content itself — that is produced under DEL-094-04 and is *indexed* and *turned over* here but not authored here.
- EPC integration acceptance — performed in DEL-094-06.
- Construction installation records — DEL-094-03.
- Foundations, on-site mounting, electrical/instrumentation, platforms, staircases — by others per SOW-0196.

## Requirements

### R1 — Master Vendor Document Register

R1.1 The Package Vendor shall produce a master vendor document register that lists every controlled document required by the source vendor document table in `_Sources/26020-Package_Requirements.docx` package heading 46 (`location TBD` — clause-level rows not extracted in this run). [Source: `_CONTEXT.md`; DELIVERABLE_REGISTER row DEL-094-05]

R1.2 The register shall include, at minimum (ASSUMPTION: industry-standard vendor document register columns; source row-level columns `location TBD`): document number, title, document class/category, revision, status, planned submittal date, actual submittal date, EPC review status, and turnover status. [ASSUMPTION]

R1.3 The register shall be the single point of truth for vendor documentation completeness; every row in the source vendor document table shall appear in the register. [Source: `_CONTEXT.md` Notes — source rows preserved as artifacts]

### R2 — Submittals

R2.1 The Package Vendor shall submit each document listed on the register to the EPC Integrator for interface/integration review. [Source: `_CONTEXT.md` ResponsibleParty]

R2.2 Submittals shall preserve revision identity (rev letter/number, date, approval state). [ASSUMPTION: standard submittal practice]

R2.3 Submittals shall include any source-required vendor documentation (per source vendor document table) — see R1.1. [Source: `_CONTEXT.md`]

### R3 — Source Vendor Documentation Coverage

R3.1 Each row of the source vendor document table (`_Sources/26020-Package_Requirements.docx` package heading 46, `location TBD`) shall be carried into this deliverable as an artifact/evidence row, not as a separate deliverable. [Source: `_CONTEXT.md` Notes; DELIVERABLE_REGISTER row Notes]

R3.2 The standard mechanical-package deliverable types listed in DBM 3-25 line 617 shall be included unless the source vendor document table explicitly omits them: datasheets, cause-and-effect inputs, utility load summaries, relief/load data, field tie-in lists, operating and design envelopes, sparing philosophy, materials and coating basis, maintenance access, shipped-loose item lists, and vendor document registers. [Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 617]

### R4 — Turnover Records

R4.1 The Package Vendor shall produce turnover records sufficient for EPC acceptance under DEL-094-06. [Source: DELIVERABLE_REGISTER row DEL-094-06]

R4.2 Turnover records shall include, at minimum (ASSUMPTION: typical API 650 tank turnover; source-row driven detail `location TBD`): equipment nameplate records, material test reports (MTRs), inspection/NDE/hydrotest records, painting/coating records, operating & maintenance manuals, commissioning spares list, and any code-required certifications. [ASSUMPTION]

### R5 — EPC Integrator Interface

R5.1 Vendor documents shall be reviewed by EPC Integrator for interface and integration consistency with DEL-094-01 (Scope of Work), DEL-094-02 (Package Datasheet), and DEL-094-03 (Construction Work Package). [Source: `_CONTEXT.md`; DELIVERABLE_REGISTER row DEL-094-06]

R5.2 Disposition codes (e.g., approved / approved with comments / rejected) shall be recorded against each register row. [ASSUMPTION: typical EPC vendor-document review practice]

### R6 — Code, Standard, and Certification Coverage

R6.1 Vendor documentation shall reflect the API 650 family code basis stated in SOW-0195 (modified API 650 atmospheric tanks). [Source: SOW-0195]

R6.2 Where the DBM 3-25 identifies HOLD/TBC items affecting the package (caustic material selection, coating, drain temperature limit, heater design, etc.), the vendor document set shall include either the resolving submittal or a hold-item closure record. [Source: DBM 3-25 caustic / drain sections]

## Standards

- API 650 (Welded Tanks for Oil Storage) — modified per SOW-0195; specific edition/appendices `location TBD`.
- 26020 Package Requirements document — package heading 46 source vendor document table, `location TBD`.
- DBM 3-25 (`_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`) — caustic, drain, and mechanical package basis (line 617).
- Site-basis standards (electrical area classification, fire/gas, regulatory) — to the extent any vendor-supplied document is affected; specific applicability `TBD`.

## Verification

| Req | Verification approach |
|---|---|
| R1 | Inspection of master register against the source vendor document table (when the table is extracted); register completeness review by EPC Integrator (DEL-094-06). |
| R2 | EPC Integrator review log per submittal; revision audit. |
| R3 | Cross-check register rows ↔ source table rows. |
| R4 | Turnover checklist signed by EPC Integrator under DEL-094-06; evidence files present. |
| R5 | EPC interface/integration review record per row of the register. |
| R6 | Code/standard compliance shown by submitted certifications, code stamps, or hold-item closure records. |

## Documentation

Required artifacts (per `_CONTEXT.md`):

- Vendor document register
- Vendor document submittals
- Source vendor document table rows preserved as artifacts/evidence
- Turnover records

Companion deliverables consumed/produced alongside this one:

- DEL-094-01 Scope of Work, DEL-094-02 Package Datasheet, DEL-094-03 Construction Work Package, DEL-094-04 Vendor Engineered Equipment Package (input/upstream).
- DEL-094-06 EPC Vendor Package Review and Acceptance (downstream consumer of the review log and turnover records).
