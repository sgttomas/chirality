# Guidance — DEL-062-01 Scope of Work (PKG-062 NGL Loading Pumps Building)

## Purpose

DEL-062-01 is the **Gate 5 EPC anchor** Scope of Work for PKG-062. It exists to bind the workbook-defined vendor-responsible Mechanical package "NGL Loading Pumps Building" to a single, source-anchored statement of what is being engineered, supplied, and integrated, who is responsible, and what the package boundary is (source: SCOPE_LEDGER SOW-0153; `_CONTEXT.md` Notes). Downstream EPC and Vendor deliverables in PKG-062 (DEL-062-02 through DEL-062-06) consume this SOW as their normative scope reference.

## Principles

1. **Workbook row authority.** The workbook package row (row 76) is authoritative for the package boundary; duplicate tracking numbers are not merged (source: SCOPE_LEDGER SOW-0153 note).
2. **Vendor-engineered, EPC-integrated.** The Package Vendor owns engineering/design/equipment supply; the EPC Integrator owns the facility integration (source: SCOPE_LEDGER SOW-0153).
3. **Source-anchored content only.** All numeric values, equipment counts, and By-Others exclusions are stated in the source materials; do not invent. Where source says "TBC", carry TBC forward — do not silently resolve.
4. **Boundary clarity over completeness.** The SOW exists to clarify the boundary, not to substitute for the Package Datasheet (DEL-062-02). Detailed vendor handoff data belongs to the Datasheet.
5. **Facility integration is non-trivial.** PKG-062 is part of the 04-25 Deepcut NGL system (storage bullets → loading pumps → truck-loading). Position the SOW within this chain (source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 73).

## Considerations

- **Building scope.** The self-framing building is explicitly inside the package (SCOPE_LEDGER SOW-0155). Foundations are excluded (SOW-0156). The handoff line between building and foundation must be unambiguous in the SOW narrative.
- **Electrical demarcation.** Motors are 575 V / 3 Ph / 60 Hz, fed from a 600 V MCC; the supply line to the MCC is By Others (SOW-0156). The demarcation point is at the MCC supply, not at the motor terminals.
- **DCS integration By Others.** Local control via H-O-A or On-Off switch is in scope; DCS integration is out (SOW-0156). The SOW should state which signals (if any) are wired to the local panel versus those exposed to DCS by others.
- **Cold start-up basis.** Motor sizing is driven by -40 C inlet stabilizer composition density (SOW-0156). The SOW must preserve this design driver so the vendor sizes for the cold case.
- **TBC fields.** Operating conditions, design conditions, and TDH are all "TBC" in source (SOW-0155, SOW-0156). The SOW should expose these as open items rather than supply default values.

## Trade-offs

- **Single SOW vs. per-artifact documents.** `_CONTEXT.md` lists four anticipated artifacts (scope narrative, equipment list, function narrative, responsibility record). They may be combined for readability; do not lose artifact identity in the combination.
- **Verbose narrative vs. tabular boundary.** The boundary statements (in scope / By Others / handoff points) benefit from tabular form; the integration narrative benefits from prose. Mix accordingly.
- **Citing 4-25 Deepcut DBM extensively vs. tightly.** The DBM is the upstream basis but is not the EPC-facing source. Cite it for the facility-integration narrative only; do not import DBM design values into the SOW where the package source disagrees.

## Examples

The package row narrative (SCOPE_LEDGER SOW-0154) is itself a concise example of an in-scope statement:

> "Basic scope: Supply 4 Identical Blackmer Model LGL4B Rotary Vane Pumps set up in parallel. Process function: Pumps to move LPG product from storage to LPG Truck Loading."

A by-others statement directly from source (SCOPE_LEDGER SOW-0156):

> "By others: DCS integration, foundations, electrical supply to MCC."

These two excerpts together form the spine of the SOW boundary statement.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority | Human ruling |
|---|---|---|---|---|---|---|
| C-001 | Objective associations come from package-grouping heuristic, not deliverable-level mapping | `_CONTEXT.md` Supports Objectives list (OBJ-001, OBJ-003..OBJ-010) | `OBJECTIVE_SCOPE_MAP.csv` rows linking objectives to SOW items at PKG-062 level | Datasheet "Coverage", Specification R-SOW-11 | PROPOSAL: treat as ASSUMPTION pending explicit deliverable-level mapping | TBD |
| C-002 | Source slice from `26020-Package_Requirements.docx` package heading 16 not locally extracted; SCOPE_LEDGER fragments are the only accessible portion | `_REFERENCES.md` Missing/Deferred section | SCOPE_LEDGER SOW-0153..SOW-0156 | All four documents | PROPOSAL: SCOPE_LEDGER fragments authoritative for cited values; remaining details TBD | TBD |
| C-003 | Operating, design, and TDH conditions all marked TBC in source | SCOPE_LEDGER SOW-0155 | SCOPE_LEDGER SOW-0156 | Datasheet Conditions; Specification R-SOW-04 | PROPOSAL: carry TBC forward and surface as open items for the Package Datasheet | TBD |
