# Specification — Vendor Document Turnover Package (DEL-090-05)

## Scope

This specification governs the vendor document turnover package produced by the Package Vendor for PKG-090 Vapour Recovery Unit 3-25, with EPC Integrator interface/integration review.

In scope:
- The vendor document register for PKG-090.
- Vendor document submittals (engineering, fabrication, inspection/test, manuals, certifications).
- Source-required vendor documentation listed against the package requirement source (`26020-Package_Requirements.docx` heading 43 — exact list `location TBD`).
- Turnover records evidencing acceptance of the vendor package documentation set.

Out of scope:
- Physical equipment design, fabrication, supply (DEL-090-04).
- Scope of work narrative and package datasheet (DEL-090-01, DEL-090-02).
- EPC review/acceptance decisions and the EPC acceptance record (DEL-090-06).
- Individual source vendor document rows; these remain artifacts/evidence, not separate deliverables (`_CONTEXT.md` Notes).

## Requirements

### R-1 Document register
The vendor shall maintain a vendor document register that indexes every submittal required for PKG-090, with at minimum: document number, title, revision, status, submittal stage, transmittal reference, and EPC review disposition. (ASSUMPTION on column set — standard practice; authoritative column list `location TBD` per `26020-Package_Requirements.docx` heading 43.)

### R-2 Required document classes
The vendor shall submit, at minimum, the document classes required by `26020-Package_Requirements.docx` heading 43. Exact list `location TBD`. ASSUMPTION (standard vendor turnover): drawings (GA, P&ID, datasheets), engineering calculations, equipment datasheets, materials and welding documentation, electrical/instrumentation schedules, ITPs and test records, certifications (PED/ASME/CRN as applicable), operations and maintenance manuals, spare-parts lists, as-built marked-up drawings.

### R-3 Submittal stages
Each governed document shall be submitted at the required project stages (e.g., IFR / IFA / IFC / As-Built). Stage map `TBD` until extracted from `26020-Package_Requirements.docx` heading 43.

### R-4 Review cycle
Each submittal shall be reviewed by the EPC Integrator. Maximum review duration and number of review cycles before escalation `TBD`.

### R-5 Source-required vendor documentation
The vendor shall provide the source-required vendor documents called out by the package requirement source. Individual source rows are carried as artifacts/evidence under this deliverable, not as separate deliverables (`_CONTEXT.md` Notes).

### R-6 Turnover record completeness
At turnover, the vendor shall provide a closed turnover record set that demonstrates: register closeout (every entry at acceptance disposition or documented deviation), completed ITP records, certifications, as-built revisions, and a turnover acceptance statement.

### R-7 Interface with DEL-090-06
The turnover record set shall be in a form consumable by DEL-090-06 (EPC Vendor Package Review and Acceptance). The acceptance authority resides with the EPC Integrator under DEL-090-06; this deliverable produces the evidence base.

### R-8 Document control discipline
Document numbering, revision control, and transmittal conventions shall conform to project standards. Project numbering convention `TBD` (location: `26020-Package_Requirements.docx` heading 43).

### R-9 Objective alignment (ASSUMPTION — package-heuristic)
The deliverable supports OBJ-002 through OBJ-010 as listed against PKG-090 in the GATE-07 deliverable register. Mapping is package-grouped; direct deliverable-to-objective evidence remains in the decomposition Objective-Deliverable Map.

## Standards

| Standard / Source | Applicability | Location |
|---|---|---|
| `26020-Package_Requirements.docx` heading 43 | Package vendor documentation requirements (governing) | location TBD (binary source not locally accessible) |
| `26020-Packages_Interfaces_4_export.xlsx` Packages row 100 | Package row entry for PKG-090 | location TBD (binary source not locally accessible) |
| `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-06 Vapour Recovery | Subject-equipment basis context | line 434 ff |
| Project document control / EDMS conventions | Numbering, transmittal, revisioning | TBD |
| Pressure equipment / mechanical certification standards (ASME/CRN/PED where applicable) | Certifications required for VRU compressor packages | ASSUMPTION; exact applicability TBD pending source extraction |

## Verification

| Requirement | Verification approach |
|---|---|
| R-1 | Inspect register; confirm column completeness and currency at each milestone gate |
| R-2 | Compare submitted classes against required class list (once `26020` heading 43 is extracted) |
| R-3 | Stage-completeness check at each gate (IFR / IFA / IFC / As-Built) |
| R-4 | Track review cycles per document; report exceedance |
| R-5 | Cross-check submittals against source-document table for PKG-090 |
| R-6 | Turnover checklist: register at 100 percent disposition, ITP/certifications complete, as-builts logged |
| R-7 | DEL-090-06 sign-off referencing this turnover evidence |
| R-8 | Spot audit of document control attributes (numbering, revision, transmittal) |
| R-9 | Trace acceptance evidence back to OBJ-002 .. OBJ-010 via PKG-090 grouping |

## Documentation

Artifacts required at completion of this deliverable:

- Vendor document register (controlled, current).
- Complete submittal set across required document classes and stages.
- Source-required vendor document rows as artifacts/evidence.
- Turnover record set: register closeout, ITP/certification records, as-builts, vendor turnover acceptance statement.
- Transmittal log linking each submittal to its EPC review disposition.

Anticipated artifacts (from `_CONTEXT.md`): vendor document register; vendor document submittals; source vendor document table rows as artifacts where available; turnover records.
