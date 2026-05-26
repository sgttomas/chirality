# Guidance — DEL-097-06 EPC Vendor Package Review and Acceptance

## Purpose

This deliverable exists because the Package Vendor owns engineering, design, supply, and vendor documentation for the Tanks, Condensate (API 650) 3-25 package, while the EPC Integrator is responsible for integrating the package into the 03-25 facility and accepting it on behalf of the project. Without a controlled EPC-led review and acceptance step, vendor work cannot be safely confirmed as ready for installation, commissioning, and turnover.

Source rationale: the decomposition explicitly separates Package Vendor responsibility from EPC Integrator responsibility (OBJ-004), and the Gate 5 decomposition adds this deliverable specifically to capture EPC review/acceptance evidence (`DELIVERABLE_REGISTER.csv` `DEL-097-06` row "Additional Gate 5 deliverable framed as EPC-integrator review and acceptance evidence").

## Principles

1. **EPC reviews; vendor designs.** The EPC does not re-engineer the vendor's package; it verifies conformance against the SOW, Package Datasheet, and Construction Work Package. (Source: OBJ-004.)
2. **Source-anchored acceptance.** Every accept/reject decision SHOULD reference a specific clause of the EPC anchor deliverables or a clause of `26020-Package_Requirements.docx` heading 49. The source slice provides Basic Scope, Major Included Equipment, Scope Notes, Physical Interface Summary, and Vendor Engineering Deliverables — these are the anchor texts for review decisions.
3. **Interface-applicability discipline.** Heading 49 explicitly lists each physical interface as Yes or No. Acceptance shall not silently expand to interfaces marked **No** in source, and shall actively verify each interface marked **Yes**.
4. **Multi-discipline sign-off.** Mechanical, electrical, controls/I&C, and civil/structural disciplines each verify their respective in-scope interfaces before acceptance (OBJ-005, OBJ-006, OBJ-008).
5. **Open items are explicit.** No item is silently closed; open items at acceptance carry explicit human-approved carry-over (OBJ-010). The source-level "Interface Coordination Notes: TBD" must be explicitly closed or carried over.
6. **Cold-temperature awareness.** -40 °C minimum ambient (DBM Site Basis) and -40 °C minimum design (heading 49 Scope Notes) govern relief devices, instrumentation, valves, and blanket-gas controls.
7. **Vendor scope boundary respect.** "By others" items (foundations, mounting, electrical/instrumentation install, platforms, staircases — heading 49 Scope Notes) are NOT vendor scope; the EPC shall not accept their presence or absence in the vendor package as a conformance issue against this deliverable.

## Considerations

- **Standards not in local source set.** API 650 and API 2000 clause-level acceptance criteria are not in the local source set. Clause-level acceptance criteria are `location TBD`. Reviewers should retrieve the relevant standards before final acceptance and capture the specific clauses applied.
- **Preliminary design conditions.** Capacity/operating/design values at heading 49 are explicitly labelled "Preliminary Design conditions." Acceptance must verify the as-built values against the final (not preliminary) design conditions; if final conditions differ from preliminary, a documented change record is required.
- **Winter recycle is conditional.** Heading 49 says a recycle "may be required to maintain a certain temperature during winter." Whether it is required, and what form, is a vendor design output; acceptance must confirm the disposition (required vs not required, with rationale).
- **VRU and blanket gas cross-package interface.** Tank vapour handling depends on the VRU package (different package), which under SCA-002 reroutes discharge to the 04-25 SOC (DBM line 442). Blanket gas supply also originates outside this package. Cross-package readiness should be checked before declaring acceptance complete.
- **Hub context.** This package supplies four of the eleven 3,800 bbl condensate tanks in the Liquids Hub; the other seven are in sour, sour-inlet, and slop service in separate packages (DBM line 406). Conformance reviews should not implicitly absorb obligations belonging to those sibling packages.
- **LACT boundary.** Sales condensate LACT equipment is third-party NRM scope; the facility provides only the tie-in (DBM line 417). Acceptance covers the facility side of the interface only.
- **Acceptance evidence vs construction evidence.** Construction Work Package (`DEL-097-03`) captures *how* the package is installed; this deliverable captures *whether the vendor's package itself* is acceptable. Avoid conflating the two evidence sets.

## Trade-offs

- **Speed vs traceability.** Closing acceptance quickly with informal sign-offs reduces traceability and weakens later turnover and warranty positions. The decomposition (OBJ-010) prioritises traceability and explicit closure evidence.
- **Strict-conformance vs change accommodation.** Vendor as-built differences from the Package Datasheet may be benign or material. Acceptance practice should require a documented change record (RFI/DCN equivalent) rather than informally accepting deviations.
- **EPC scope creep risk.** Excessive EPC review can drift into vendor engineering territory, violating OBJ-004. Keep EPC review focused on conformance, integration, and turnover readiness — not on redesign.
- **Coordination-note carry-over.** The source's open "Interface Coordination Notes: TBD" can either be closed now (higher up-front cost, lower late-phase risk) or carried over (lower up-front cost, higher risk that an uncoordinated interface causes installation rework). Prefer closure before final acceptance.

## Examples

- Example (acceptance with carry-over): Vendor delivers four 3,800 bbl tanks per Datasheet, hydrotest pass, coating reports complete, PVRV/EPRV function tests complete, but two punch-list items (instrument tagging mismatch) and the source-level Interface Coordination Notes item remain open. Acceptance recorded as **Conditional Accept** with the open items tracked to closure by a documented date; turnover gated on closure. (Illustrative — convention `TBD`.)
- Example (rejection): Vendor delivers tanks with internal coating differing from Devchem 253 without an approved deviation. Per R-2.2 and the heading-49-stated coating basis, the package is **Rejected** until a deviation is approved or coating is corrected. (Source for coating basis: heading 49 Major Included Equipment.)
- Example (non-applicable interface confirmation): Heading 49 marks Electrical Power as **No** for this package. Acceptance record explicitly notes "Electrical Power: not in vendor scope per heading 49 Physical Interface Summary" rather than leaving the interface unaddressed.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short) | Source A | Source B | Impacted Sections | Proposed Authority (PROPOSAL) | Human Ruling (TBD) |
|---|---|---|---|---|---|---|
| CONF-01 | Clause-level API 650 / API 2000 acceptance criteria not in accessible source set | `26020-Package_Requirements.docx` heading 49 (references modified API 650 and API 2000 blanket gas) | API 650 / API 2000 standards (not in local source set) | Specification R-3.1, R-5.2; Standards table | Retrieve and extract clause-level slices from API 650 and API 2000 before final acceptance; record specific clauses applied | TBD |
| CONF-02 | "Interface Coordination Notes" marked **TBD** in source slice | `26020-Package_Requirements.docx` heading 49 Interface Coordination Notes ("TBD.") | No alternative source | Datasheet Construction; Specification R-4.3 | Resolve coordination notes content before final acceptance, or capture explicit human-approved carry-over | TBD |
| CONF-03 | Vendor document review status convention not declared in accessible source | None in local DBM/registers | `26020-Package_Requirements.docx` heading 49 Vendor Engineering Deliverables (list given, status convention not given) | Specification R-1.2 | Adopt project document control convention once retrieved; default to Approved / Approved with Comments / Revise and Resubmit / Rejected | TBD |
| CONF-04 | Capacity/throughput values labelled "Preliminary Design conditions" in source | `26020-Package_Requirements.docx` heading 49 Scope Notes (94,940 kg/h; 3,187 Am3/d preliminary) | Final design conditions (not in local source set) | Datasheet Attributes; Specification R-2.4 | Verify against final (not preliminary) design conditions before acceptance; require documented change record if final differs from preliminary | TBD |
| CONF-05 | Service classification — sweet (product) vs sour | `26020-Package_Requirements.docx` heading 49 Basic Scope ("Condensate Product Storage Tanks") | DBM line 406 (differentiates sour inlet, sour, product, slop tanks) | Datasheet Conditions; Specification R-5.1 | Treat this package as sweet C5+ product service per heading 49; carry residual H2S exposure awareness via DBM | TBD |
