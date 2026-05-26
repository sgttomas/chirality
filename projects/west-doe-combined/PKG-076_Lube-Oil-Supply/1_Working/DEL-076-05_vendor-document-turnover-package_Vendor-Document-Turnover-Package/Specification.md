# Specification: DEL-076-05 — Vendor Document Turnover Package

> Normative requirements for vendor document turnover for the Lube Oil Supply package (PKG-076). Requirements derived only from accessible sources; inferences labeled `ASSUMPTION`; unknowns marked `TBD`.

## Scope

This specification governs the Package Vendor's preparation, control, submission, and turnover of vendor documentation for the Lube Oil Supply package (PKG-076), including the vendor document register, vendor document submittals, source-required vendor document table rows carried as artifacts, and turnover records. The EPC Integrator is responsible for interface/integration review and acceptance.

**Included**
- Vendor document register and revision control through turnover.
- Submittal of vendor documents required by the EPC Scope of Work (DEL-076-01) and Package Datasheet (DEL-076-02).
- Mechanical package documentation classes enumerated by the project DBM mechanical package structure (datasheets, cause-and-effect inputs, utility load summaries, relief/load data, field tie-in lists, operating and design envelopes, sparing philosophy, materials and coating basis, maintenance access, shipped-loose item lists, vendor document registers) — Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 617.
- Turnover records: acceptance log, certification, custody-transfer and as-built confirmation.

**Excluded**
- Engineering, design, and physical fabrication of equipment (covered by DEL-076-04 Vendor Engineered Equipment Package).
- EPC integration acceptance decisions (covered by DEL-076-06 EPC Vendor Package Review and Acceptance).
- Cross-facility utility scope assignment between 03-25 and 04-25 (governed by DBM utility section).

## Requirements

| ID | Requirement | Source | Verification (see § Verification) |
|---|---|---|---|
| R-076-05-01 | Package Vendor shall maintain a vendor document register listing every document required by the EPC Scope of Work, Package Datasheet, and applicable source-required document rows, with at minimum: document number, title, type, revision, status, planned issue date, actual issue date. | DBM 3-25 line 617; _CONTEXT.md Anticipated Artifacts | V-01 |
| R-076-05-02 | Vendor document submittals shall include the document classes enumerated for mechanical packages: datasheets, cause-and-effect inputs, utility load summaries, relief/load data, field tie-in lists, operating and design envelopes, sparing philosophy, materials and coating basis, maintenance access, shipped-loose item lists, and vendor document registers. | DBM 3-25 line 617 | V-02 |
| R-076-05-03 | Vendor documentation for lube-oil storage and pumping equipment shall reflect the package basis: cylinder lube-oil 400 bbl heated tank, cylinder lube-oil pump P-9240-1, and crank-case lube-oil basis, with values consistent with the project Lube Oil Storage and Pump Basis. | DBM 4-25 lines 2059-2068 | V-03 |
| R-076-05-04 | Where vendor lube-oil documents reference hazardous-material classification, they shall reference the project hazardous-material list. (Project hazardous-material list location: `TBD` — not in workspace.) | DBM 3-25 line 507; location TBD | V-04 |
| R-076-05-05 | The Package Vendor shall produce turnover records covering: acceptance log, certification of compliance, custody-transfer/handover acknowledgement, and as-built confirmation for the equipment package. | _CONTEXT.md Anticipated Artifacts | V-05 |
| R-076-05-06 | Source-required vendor document table rows (where the source specifies named vendor documents) shall be tracked as register entries; the source rows are evidence/artifacts and shall not be reframed as separate deliverables. | _CONTEXT.md Notes | V-01 |
| R-076-05-07 | EPC Integrator shall perform interface/integration review of all vendor documents; review status shall be recorded in the register before turnover acceptance. | _CONTEXT.md ResponsibleParty | V-06 |
| R-076-05-08 | Document numbering, revision control codes, transmittal format, and EDMS interface shall conform to the project document control basis. (Project document control basis: `TBD` — not in workspace.) | location TBD; ASSUMPTION | V-07 |
| R-076-05-09 | Vendor documentation shall be sufficient to support the package's coverage of SOW-0135, SOW-0136, SOW-0137, SOW-0138 as recorded in the GATE-07 deliverable register. | DELIVERABLE_REGISTER.csv (GATE-07) | V-08 |

## Standards

| Standard / Reference | Applicability | Location |
|---|---|---|
| `26020-Package_Requirements.docx` heading 30 | Governing package requirements set for vendor documentation | location TBD (DOCX not converted) |
| Project DBM (03-25 Comp & Liquids; 04-25 Deepcut) | Authoritative basis for mechanical package documentation classes and lube-oil basis | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |
| Project Document Control / EDMS procedure | Document numbering, revision codes, transmittal | TBD |
| Project hazardous-material list | Lube-oil storage classification | TBD |
| Applicable industry standards for compressor lube-oil systems (e.g., API equivalents) | Equipment-level vendor documents | TBD — not enumerated in accessible source |

## Verification

| Verification ID | Method | Maps Requirements |
|---|---|---|
| V-01 | Register review against deliverable register and source-required document rows | R-076-05-01, R-076-05-06 |
| V-02 | Submittal completeness check against the mechanical-package document-class list | R-076-05-02 |
| V-03 | Cross-check of vendor lube-oil documents against DBM Lube Oil Storage and Pump Basis values | R-076-05-03 |
| V-04 | Confirmation that vendor docs cite project hazardous-material list (where applicable) | R-076-05-04 |
| V-05 | Turnover record set audit (acceptance log, certification, handover, as-built) | R-076-05-05 |
| V-06 | EPC Integrator review status entries present for every register row before acceptance | R-076-05-07 |
| V-07 | Document control conformance audit | R-076-05-08 |
| V-08 | Coverage check: SOW-0135..0138 each mapped to at least one vendor document set | R-076-05-09 |

## Documentation (Required Artifacts)

- Vendor document register (controlled spreadsheet/database export)
- Vendor document submittals (as listed in the register)
- Source-required vendor document table rows (carried as artifacts where available)
- Turnover records: acceptance log, certification, handover acknowledgement, as-built confirmation
- EPC Integrator review log entries against each register row
- Final issued vendor document index at turnover
