# Specification — DEL-084-05 Vendor Document Turnover Package (PKG-084)

## Scope

This specification governs the Vendor Document Turnover Package for PKG-084 Fuel Gas Skid 3-25. It covers the assembly, management, submission, and turnover of all vendor-originated documentation for the package, including the vendor document register, submittals, source-required vendor documents (carried as artifacts), and turnover records. The deliverable is produced by the Package Vendor (vendor documentation function); EPC Integrator review/acceptance is handled under DEL-084-06.

Excluded: vendor engineering/design/equipment supply (DEL-084-04); EPC Scope of Work (DEL-084-01); EPC Package Datasheet (DEL-084-02); EPC Construction Work Package (DEL-084-03); EPC review and acceptance activity (DEL-084-06).

Sources: `_CONTEXT.md` Scope; DELIVERABLE_REGISTER.csv rows DEL-084-01 through DEL-084-06.

## Requirements

| ID | Requirement | Source |
|---|---|---|
| R-1 | The deliverable SHALL include a Vendor Document Register listing every vendor-produced document required for PKG-084. | `_CONTEXT.md` Anticipated Artifacts; DBM-Comp_and_Liquids line 617 |
| R-2 | The deliverable SHALL include the vendor document submittals themselves, tracked against the register. | `_CONTEXT.md` Anticipated Artifacts |
| R-3 | Where individual source-required vendor document rows exist, they SHALL be carried as artifacts/evidence under this deliverable and not as separate deliverables. | `_CONTEXT.md` Notes; DELIVERABLE_REGISTER.csv row DEL-084-05 Notes |
| R-4 | The deliverable SHALL include turnover records sufficient to support EPC Integrator acceptance under DEL-084-06. | `_CONTEXT.md` Anticipated Artifacts; DELIVERABLE_REGISTER.csv row DEL-084-06 |
| R-5 | The vendor document register and submittals SHALL address the package-level documentation expectations enumerated in the DBM (datasheets, cause-and-effect inputs, utility load summaries, relief/load data, field tie-in lists, operating and design envelopes, sparing philosophy, materials and coating basis, maintenance access, shipped-loose item lists, and vendor document register itself) to the extent applicable to a fuel gas skid. | DBM-Comp_and_Liquids line 617 (ASSUMPTION: applicability of each item to a fuel gas skid is TBD until vendor scope and `26020-Package_Requirements.docx` heading 37 are resolved) |
| R-6 | Document numbering, revision codes, status codes, and transmittal conventions SHALL conform to the project document control specification. | TBD — specification reference and clause `location TBD` (`26020-Package_Requirements.docx` heading 37 not locally accessible) |
| R-7 | Required vendor document types, hold points, and acceptance criteria SHALL be those enumerated in `26020-Package_Requirements.docx` heading 37 and Workbook Packages row 60. | TBD — `location TBD` (sources not locally text-accessible) |
| R-8 | Submittals SHALL be transmitted, reviewed, and re-issued through the EPC Integrator review process associated with DEL-084-06 prior to package turnover. | DELIVERABLE_REGISTER.csv rows DEL-084-05, DEL-084-06 |

## Standards

| Standard / Reference | Applicability | Source |
|---|---|---|
| Project document control specification | Document numbering, revisions, status codes, transmittals | TBD — `location TBD` |
| `26020-Package_Requirements.docx` heading 37 | Package-specific vendor document requirements | `_REFERENCES.md`; `location TBD` (binary, not opened) |
| Workbook Packages row 60 | Package definition row for PKG-084 | `_REFERENCES.md`; `location TBD` |
| DBM-Comp_and_Liquids §617 (package deliverables enumeration) | Categories of package-level documentation expected | DBM-Comp_and_Liquids `3-25_Comp_and_Liquids_DBM.md` line 617 |

## Verification

| Req ID | Verification Approach | Source |
|---|---|---|
| R-1 | Review of vendor document register completeness against `26020-Package_Requirements.docx` heading 37 and package equipment list | DELIVERABLE_REGISTER.csv row DEL-084-06 (artifacts: vendor document review log) |
| R-2 | Receipt log reconciliation: every register row has a transmitted submittal at the required revision and status | DELIVERABLE_REGISTER.csv row DEL-084-06 |
| R-3 | Cross-check that source-required vendor document rows appear as artifacts under DEL-084-05, not as standalone deliverables | `_CONTEXT.md` Notes |
| R-4 | Turnover record review against EPC acceptance checklist (DEL-084-06) | DELIVERABLE_REGISTER.csv row DEL-084-06 (artifacts: package acceptance checklist; turnover evidence) |
| R-5 | Spot-check of applicable DBM line 617 categories present in register | DBM-Comp_and_Liquids line 617 |
| R-6 | Document control audit | TBD (`location TBD`) |
| R-7 | Compliance verification once heading 37 / Workbook row 60 contents are resolved | TBD |
| R-8 | EPC Integrator acceptance per DEL-084-06 | DELIVERABLE_REGISTER.csv row DEL-084-06 |

## Documentation

Artifacts produced under this deliverable (per `_CONTEXT.md` Anticipated Artifacts):

- Vendor Document Register (controlled, revisioned)
- Vendor document submittals (each transmitted submittal)
- Source vendor document table rows carried as artifacts where available
- Turnover records (transmittals, acceptance evidence, handoff documentation)

Specific document templates, register column conventions, and turnover record formats: TBD pending `26020-Package_Requirements.docx` heading 37 access.
