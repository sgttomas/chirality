# Guidance — DEL-050-01_scope-of-work (PKG-050 Stabilizer Overheads Compressors)

## Purpose

This Scope of Work is the EPC Integrator's anchor deliverable for PKG-050 Stabilizer Overheads Compressors. It exists to (a) carry the workbook-defined vendor-responsible Mechanical package as a distinct flat project package for WBS 01, and (b) state the responsibility split under which the Package Vendor owns engineering, design, vendor documentation, and the physical equipment package, while the EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. Source: SCOPE_LEDGER.csv SOW-0173; PACKAGE_REGISTER.csv PKG-050 responsibility narrative.

`_CONTEXT.md` Notes flag this as the "Mandatory Gate 5 EPC anchor deliverable defined by user instruction"; this Guidance treats that as a directive, not as a derived requirement.

## Principles

- **Decomposition routes; sources determine content.** The SCOPE_LEDGER and PACKAGE_REGISTER rows for PKG-050 (with the Word package heading 5 and Workbook row 81) are the authoritative source set for what the Scope of Work must say. Decomposition narrative scopes the deliverable but does not supply unsourced design values.
- **Faithfulness over fluency.** Where source values are partial (e.g., truncated 3rd-stage cooler discharge temperature in SOW-0176), they are carried as `TBD` rather than completed by inference.
- **Boundary discipline.** The Scope of Work is package-level. Tag-level datasheet content, construction work packaging, vendor turnover, and acceptance work belong to sibling deliverables DEL-050-02 through DEL-050-06 and shall not be duplicated here.
- **Responsibility legibility.** The Vendor/Integrator boundary is reproduced verbatim from PACKAGE_REGISTER.csv so downstream readers cannot misallocate scope.
- **Interface enumeration is not interface engineering.** Listing the 13 workbook-declared interface types satisfies the Scope of Work; engineering each interface belongs to DEL-050-02 (Interface Fact Evidence rows in ARTIFACT_REGISTER.csv).

## Considerations

- **Source granularity.** The package requirements document text reaches the Scope of Work via the SCOPE_LEDGER extracts (SOW-0173..SOW-0176). The raw `.docx` is present at `_Sources/26020-Package_Requirements.docx` but is not parsed within this run; deeper rereads (e.g., to recover the truncated SOW-0176 fields) require a tool pass and should be requested before any value currently marked `TBD` is filled.
- **Standards citation.** NEMA MG 1 is named in SOW-0176 for motor testing/labelling; no clause is cited. Treat NEMA MG 1 as applicable but with `location TBD` until a vendor proposal or full source pass establishes the clause.
- **Ariel KBC/6.** The compressor frame is named in source (SOW-0175). Detailed frame selection, throw geometry, and rod-load envelopes are vendor-design content and are not Scope-of-Work data.
- **Objective association.** `_CONTEXT.md` lists nine supported objectives (OBJ-001, OBJ-003..OBJ-010). Per `OBJECTIVE_ASSOCIATION_MODE = PACKAGE_HEURISTIC`, this association is treated as ASSUMPTION (best-effort mapping) unless a deliverable-ID-level mapping from OBJECTIVE_DELIVERABLE_MAP.csv confirms otherwise.
- **Bid document.** The Word Source Basis `26020-01-PT-RFQ-12-005_Stabilizer_OH_Comp.docx` is the formal bid scope companion; it is not locally extracted in this run. Any Scope of Work statement that depends on bid-doc text alone must be marked `TBD` until parsed.
- **Exclusions.** Source records no package-specific exclusions ("TBD; no package-specific exclusions stated in source materials"). Do not invent exclusions; surface a Conflict-Table entry if downstream needs prompt an exclusion.

## Trade-offs

- **Verbatim vs. paraphrase.** Verbatim source fragments are preferred for the basic-scope, equipment, and operating-condition sections because the source text is itself the scope. Paraphrase is reserved for connective narrative.
- **Stage 3 / Stage 4 cooler discharge temperatures.** The source extract is truncated. Options: (a) carry as `TBD` (chosen here); (b) re-extract from the `.docx` (a separate tool pass). Option (b) is preferred before Gate 5 review.
- **Interface list vs. interface engineering.** The Scope of Work enumerates interface types only. Detailed per-interface engineering is a deliverable-level tradeoff handled in DEL-050-02; mixing the two here would obscure the package/interface boundary.

## Examples

- **Identity statement (compliant).** "PKG-050 Stabilizer Overheads Compressors; workbook row 81; CoA tracking 26020-01-12-005; WBS 01; Mechanical." Source: PACKAGE_REGISTER.csv PKG-050.
- **Basic-scope statement (compliant).** "Supply Stabilizer Overhead Compressor Packages consisting of two (2) identical induction-motor-driven separable reciprocating compressor packages, each designed for 100% capacity." Source: SCOPE_LEDGER.csv SOW-0174.
- **Responsibility statement (compliant).** Reproduce the PACKAGE_REGISTER.csv PKG-050 responsibility narrative verbatim.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| CONF-01 | SOW-0176 cooler discharge temperatures: 1st (65.56 °C), 2nd (87.78 °C), 3rd ("3rd." — truncated). Source extract is incomplete for stages 3 and 4. | SCOPE_LEDGER.csv SOW-0176 (extract) | `_Sources/26020-Package_Requirements.docx` package heading 5 (not extracted) | Datasheet Conditions (Operating); Specification REQ-07 | Re-extract from `.docx`; values currently `TBD`. | TBD |
| CONF-02 | SOW-0176 records "Other MAWP is TBC" alongside specific 1st-stage suction and final-stage discharge MAWP values. | SCOPE_LEDGER.csv SOW-0176 | `_Sources/26020-Package_Requirements.docx` package heading 5 (not extracted) | Datasheet Conditions (Design); Specification REQ-08 | Carry "TBC" verbatim; do not infer interstage MAWP. | TBD |
| CONF-03 | `_CONTEXT.md` Supports Objectives lists nine objectives; mapping is package-heuristic. | `_CONTEXT.md` Supports Objectives | OBJECTIVE_DELIVERABLE_MAP.csv | Specification REQ-13 | Treat as ASSUMPTION (best-effort) until deliverable-ID-level mapping is confirmed. | TBD |
| CONF-04 | Word Source Basis bid document `26020-01-PT-RFQ-12-005_Stabilizer_OH_Comp.docx` is named in PACKAGE_REGISTER.csv but not locally extracted. | PACKAGE_REGISTER.csv PKG-050 | `_Sources/` (file not located in this run) | Specification REQ-11; References | Cite file path; mark `location TBD` until the bid doc is parsed. | TBD |
