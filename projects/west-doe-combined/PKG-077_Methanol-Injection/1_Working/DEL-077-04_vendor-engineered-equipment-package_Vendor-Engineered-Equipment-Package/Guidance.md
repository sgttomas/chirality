# Guidance — DEL-077-04 Vendor Engineered Equipment Package

## Purpose

This deliverable exists because PKG-077 (Methanol Injection) is a **vendor-owned Mechanical package**: the Package Vendor — not the EPC Integrator — performs the package engineering, design, and equipment supply. The decomposition frames this as a "Vendor Package Production Unit" anchored by, and developed from, the EPC Integrator's Scope of Work (DEL-077-01) and Package Datasheet (DEL-077-02). It exists alongside, but distinctly from, the EPC-owned anchor deliverables and the EPC review/acceptance deliverable (DEL-077-06). [Source: `DELIVERABLE_REGISTER.csv` rows 396, 397, 399, 401; `PACKAGE_REGISTER.csv` row 72]

## Principles

1. **Two-party authorship boundary.** Package engineering/design/equipment belongs to the Package Vendor; facility-level integration belongs to the EPC Integrator. Treat this split as the primary structuring principle for every section of every vendor document. [Source: `PACKAGE_REGISTER.csv` row 72]
2. **EPC anchors are authoritative inputs.** The EPC Scope of Work (DEL-077-01) and Package Datasheet (DEL-077-02) are the authoritative inputs to vendor engineering. Vendor work is derivative of these anchors and must trace to them. [Source: `DELIVERABLE_REGISTER.csv` row 399 Notes]
3. **Interface evidence flows through the EPC Package Datasheet.** Workbook interface facts are carried in DEL-077-02 (and its artifact rows) as datasheet evidence, not as standalone vendor inputs. The vendor consumes them via the datasheet. [Source: `ARTIFACT_REGISTER.csv` row 4273; `DELIVERABLE_REGISTER.csv` row 397 Notes]
4. **Documentation is split.** Design basis and datasheet set live in DEL-077-04; transmittal/register/turnover records live in DEL-077-05. Do not duplicate. [Source: `DELIVERABLE_REGISTER.csv` rows 399, 400]
5. **Acceptance is external.** Vendor work is reviewed and accepted under DEL-077-06; the vendor does not self-certify integration acceptance. [Source: `DELIVERABLE_REGISTER.csv` row 401]

## Considerations

- **Source-slice gap.** As of this draft, no deliverable-specific source slices have been copied locally (`_REFERENCES.md` "Missing / Deferred References"). Process-, equipment-, and standard-specific content remains `TBD` until source slices from the workbook, package requirements document, or DBM are extracted. Vendor drafting should not invent technical specifics in advance of source extraction.
- **Objective association.** `OBJ-001, OBJ-004..OBJ-010` are associated under the package-grouping heuristic (ASSUMPTION). Treat them as directional context, not as hard requirements for vendor work, unless a human ruling promotes specific objectives.
- **Gate 6 scope disposition.** The PACKAGE_REGISTER notes that "Methanol Injection scope is included with the Cryogenic Unit package scope" (Gate 6). Vendor planning should clarify whether DEL-077-04 is delivered as a discrete vendor package or as a sub-element of a larger Cryogenic Unit vendor package. This is currently `TBD` and surfaced in the Conflict Table.
- **Interface breadth.** PKG-077 carries 13 declared interface types. Vendor design must anticipate accommodation for all 13 even if only a subset are physically wired/piped in the final installation. [Source: `PACKAGE_REGISTER.csv` row 72; `INTERFACE_REGISTER.csv` rows 574-586]

## Trade-offs

- **Pre-engineered vs. custom-engineered.** Methanol injection packages are commonly available as pre-engineered skids; full custom engineering increases schedule and cost. Pre-engineered options may not satisfy all 13 declared interface types or the project DBM. TBD: source-based trade-off basis. (ASSUMPTION — industry convention only.)
- **Single-vendor responsibility vs. EPC-managed sub-supply.** A single vendor for engineering, design, and equipment simplifies the responsibility boundary but concentrates risk. The decomposition assigns a single Package Vendor role; this trade-off has therefore been resolved at the decomposition level. [Source: `DELIVERABLE_REGISTER.csv` row 399]
- **Documentation density.** Sufficient design-basis detail to enable EPC acceptance (DEL-077-06) without bloating the design-basis set with material that belongs in the turnover package (DEL-077-05). The split is defined by the deliverable boundary, not by document-volume preference.

## Examples

No source-grounded examples are available in the deliverable-local reference set. Omitted to avoid invention.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-077-04-001 | Whether DEL-077-04 is a discrete vendor package or a sub-element of a Cryogenic Unit vendor package. | `DELIVERABLE_REGISTER.csv` row 399 (treats DEL-077-04 as a standalone PKG-077 production unit) | `PACKAGE_REGISTER.csv` row 72 Notes: "Gate 6 disposition: Methanol Injection scope is included with the Cryogenic Unit package scope." | Datasheet (Identification, Construction); Specification (R4, R9); Procedure (Prerequisites, Steps) | Treat DEL-077-04 as the vendor production unit of record for PKG-077 scope while flagging the Gate 6 disposition as a scope-integration question for the EPC Integrator. | TBD |
| C-077-04-002 | Whether OBJ-001 / OBJ-004..OBJ-010 are normative for vendor work or only package-grouping context. | `_CONTEXT.md` Supports Objectives | `DELIVERABLE_REGISTER.csv` row 399; skill heuristic `PACKAGE_HEURISTIC` (ASSUMPTION) | Datasheet (Identification — Supports Objectives); Specification (Verification) | Treat as directional context only until an explicit objective-to-deliverable map confirms vendor-scope normativity. | TBD |
