# Specification: DEL-099-05 — Vendor Document Turnover Package

## Scope

This deliverable specifies the **Vendor Document Turnover Package** for `PKG-099 Truck Product Loading Unit 3-25`. It defines the document register, submittal expectations, source-required vendor documentation, and turnover records that the Package Vendor shall produce and that the EPC Integrator shall review for interface/integration acceptance.

**In scope:**
- Vendor document register (index of all required vendor documents for the truck loading package)
- Vendor document submittals (drawings, datasheets, calculations, manuals, certificates)
- Source-required vendor documentation per project specifications
- Turnover records (handover dossier evidencing mechanical completion and acceptance)

**Out of scope:**
- Physical fabrication, installation, or commissioning of the truck loading equipment itself (covered by other PKG-099 deliverables)
- LACT custody-transfer equipment documentation (third-party NRM scope per DBM SEC-06, line 417; FACT)
- Documentation for other PKG-099 deliverables (e.g., separate mechanical, piping, electrical, controls deliverables) except where vendor turnover spans those interfaces

Source: `_CONTEXT.md`; DBM SEC-06.

## Requirements

### R1 — Vendor document register exists

The vendor shall produce a vendor document register listing every required vendor document with document number, title, revision, planned and actual issue date, and turnover status.

- Source: DBM SEC-09 "Mechanical Package Structure" (line 617) explicitly enumerates "vendor document registers" as part of required package deliverable content. (FACT)

### R2 — Required vendor document classes

Vendor submittals shall, at minimum, address the deliverable content enumerated for mechanical packages in the DBM:

- datasheets
- cause-and-effect inputs
- utility load summaries
- relief/load data
- field tie-in lists
- operating and design envelopes
- sparing philosophy
- materials and coating basis
- maintenance access
- shipped-loose item lists
- vendor document registers (the register itself)

Source: DBM SEC-09 (line 617) (FACT).

### R3 — Detailed submittal list aligned to project specifications

The full submittal list, document numbering convention, revision/approval workflow, and any class-specific contents (e.g., GA drawings, P&IDs, electrical schematics, IOM manuals, QA/QC dossiers, MTRs, FAT/SAT records, spare-parts lists, training material, warranties) shall be aligned to the project specification index referenced in DBM SEC-12 (line 888).

- Source: DBM SEC-12 (line 888) (FACT, scope only).
- Detailed list of required classes: **TBD — location `26020-Package_Requirements.docx` heading 51 not locally parseable.** (location TBD)

### R4 — Source-required vendor documents preserved

Where the project package requirements specification (`26020-Package_Requirements.docx` heading 51) names specific vendor documents, those documents shall be obtained from the vendor and recorded in the register.

- Source: `_CONTEXT.md` Source Reference; `_REFERENCES.md`. Specific list: **TBD (location TBD).**

### R5 — Turnover records assembled

A turnover dossier shall be assembled covering at least:
- as-built drawings (ASSUMPTION — typical industry practice; not confirmed from accessible sources)
- FAT and SAT signed reports (ASSUMPTION)
- calibration / certification records (ASSUMPTION)
- punch list with disposition (ASSUMPTION)
- system handover certificate (ASSUMPTION)

Full prescribed turnover contents: **TBD (location TBD)**, pending access to the project package requirements specification.

### R6 — EPC Integrator interface/integration review

The EPC Integrator shall review vendor submittals for interface and integration consistency against the parent DBM, P&IDs, and adjacent packages prior to acceptance.

- Source: `_CONTEXT.md` ResponsibleParty (FACT).

### R7 — Revision and configuration control

Each register entry shall track revision history and current status (Issued For Review, Issued For Construction, As-Built, Accepted-For-Turnover). Workflow specifics: **TBD (location TBD).**

### R8 — Low-ambient and service consistency

Documentation shall reflect the -40 deg C site ambient basis (DBM SEC-02 / SEC-09, line 145) and the product condensate truck loading service basis (DBM SEC-06, lines 22, 34, 413-416). (FACT)

## Standards

| Standard / Reference | Role | Status |
|---|---|---|
| `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-06, SEC-09, SEC-12 | Governing design basis for unit 3-25 mechanical packages | Locally accessible (FACT) |
| `26020-Package_Requirements.docx` heading 51 | Package-specific document requirements | Cited; **location TBD (not locally parseable)** |
| `26020-Packages_Interfaces_4_export.xlsx` row 98 | Package interface register row | Cited; **location TBD (not locally parseable)** |
| Project specification index (DBM SEC-12 line 888) | Defines applicable specifications, codes, regulations | Referenced in DBM (FACT); index content TBD |

## Verification

| Req | Verification Method | Evidence Record |
|---|---|---|
| R1 | Inspect register file presence and completeness against R2 classes | Vendor document register file accepted by EPC Integrator |
| R2 | Cross-check vendor submittals against the SEC-09 class list | Submittal log / register columns |
| R3 | Review against project specification index | Specification compliance checklist (TBD) |
| R4 | Cross-check register entries against `26020-Package_Requirements.docx` heading 51 list | Source-required vendor doc traceability matrix (TBD) |
| R5 | Verify presence and signature of turnover dossier items | Signed turnover dossier |
| R6 | Confirm EPC Integrator review record exists for each submittal | Review/comment log |
| R7 | Inspect revision metadata in register | Register revision history |
| R8 | Review datasheets/manuals for ambient and service consistency | Spot-check against DBM |

## Documentation

Anticipated artifacts (from `_CONTEXT.md`):

- Vendor document register
- Vendor document submittals (per R2 classes)
- Source vendor document table rows as artifacts where available
- Turnover records
