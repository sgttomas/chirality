# Guidance — DEL-093-06 EPC Vendor Package Review and Acceptance

## Purpose

This deliverable exists because the Package Vendor owns engineering, design, supply, and vendor documentation for the Tanks, Water (API 650) 3-25 package, while the EPC Integrator is responsible for integrating the package into the 03-25 facility and accepting it on behalf of the project. Without a controlled EPC-led review and acceptance step, vendor work cannot be safely confirmed as ready for installation, commissioning, and turnover.

Source rationale: the decomposition explicitly separates Package Vendor responsibility from EPC Integrator responsibility (OBJ-004), and the Gate 5 decomposition adds this deliverable specifically to capture EPC review/acceptance evidence (`DELIVERABLE_REGISTER.csv` `DEL-093-06` row "Additional Gate 5 deliverable framed as EPC-integrator review and acceptance evidence").

## Principles

1. **EPC reviews; vendor designs.** The EPC does not re-engineer the vendor's package; it verifies conformance against the SOW, Package Datasheet, and Construction Work Package. (Source: OBJ-004.)
2. **Source-anchored acceptance.** Every accept/reject decision SHOULD reference a specific clause of the EPC anchor deliverables or a clause of `26020-Package_Requirements.docx` heading 45 (clause-level text `location TBD` in source slice).
3. **Multi-discipline sign-off.** Mechanical, electrical, controls/I&C, and civil/structural disciplines each verify their respective interfaces before acceptance (OBJ-005, OBJ-006, OBJ-008).
4. **Open items are explicit.** No item is silently closed; open items at acceptance carry explicit human-approved carry-over (OBJ-010).
5. **Sour-service awareness.** The package handles sour produced water; materials, MTRs, and corrosion allowances are not optional review items (OBJ-009; DBM SEC-15).
6. **Cold-temperature awareness.** -40 °C governs exposed components; heat tracing, insulation, and instrumentation must be checked for cold-service applicability (DBM Site Basis line 145).

## Considerations

- **Source-text gaps.** Detailed package requirements live in `26020-Package_Requirements.docx` heading 45, which is not directly readable from the current source set. Clause-level acceptance criteria are `location TBD`. Reviewers should escalate to retrieve and trace those clauses before final acceptance.
- **DBM TBC items propagating into acceptance.** The DBM itself carries TBC items relevant to this package: tank SG 1.25, pump SG 1.18 discrepancy, produced-water contaminant list, caustic tank material details (cross-package). Acceptance cannot resolve these unilaterally; it depends on detailed-design closure (DBM SEC-06 line 421; SEC-04 line 194).
- **Cross-package interfaces.** Tank vapour handling depends on the VRU (different package) which itself depends on SCA-002 routing to 04-25 SOC (DBM SEC-06 line 436). VRU readiness and SCA status should be checked before declaring acceptance complete.
- **Turnover boundary.** Pipeline tie-out is by others past the facility riser; the EPC is accountable only up to the defined interface (DBM SEC-04 line 216, SEC-06 line 432).
- **Acceptance evidence vs construction evidence.** Construction Work Package (`DEL-093-03`) captures *how* the package is installed; this deliverable captures *whether the vendor's package itself* is acceptable. Avoid conflating the two evidence sets.

## Trade-offs

- **Speed vs traceability.** Closing acceptance quickly with informal sign-offs reduces traceability and weakens later turnover and warranty positions. The decomposition (OBJ-010) prioritises traceability and explicit closure evidence.
- **Strict-conformance vs change accommodation.** Vendor as-built differences from the Package Datasheet may be benign or material. Acceptance practice should require a documented change record (RFI/DCN equivalent) rather than informally accepting deviations.
- **EPC scope creep risk.** Excessive EPC review can drift into vendor engineering territory, violating OBJ-004. Keep EPC review focused on conformance, integration, and turnover readiness — not on redesign.

## Examples

- Example (acceptance with carry-over): Vendor delivers seven 3,800 bbl tanks per Datasheet, hydrotest pass, coating reports complete, but two punch-list items (instrument tagging mismatch) remain open. Acceptance recorded as **Conditional Accept** with the two punch items tracked to closure by a documented date; turnover gated on closure. (Illustrative — convention `TBD`.)
- Example (rejection): Vendor delivers tanks with internal coating differing from Devchem 253 without an approved deviation. Per R-2.2 and the DBM-stated coating basis, the package is **Rejected** until a deviation is approved or coating is corrected. (Source for coating basis: DBM SEC-06 line 421.)

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short) | Source A | Source B | Impacted Sections | Proposed Authority (PROPOSAL) | Human Ruling (TBD) |
|---|---|---|---|---|---|---|
| CONF-01 | Tank design SG 1.25 (TBC) vs pump fluid SG 1.18 | DBM SEC-06 line 421 (tank SG 1.25 TBC) | DBM SEC-06 line 421 (pump fluid SG 1.18) | Datasheet Attributes; Specification R-2.4 | Resolve in detailed design; carry as TBC until vendor confirms | TBD |
| CONF-02 | Clause-level API 650 / package requirements acceptance criteria not in accessible source set | DBM SEC-06 line 421 (references API-650 Modified) | `26020-Package_Requirements.docx` heading 45 (binary; not readable from local source) | Specification R-3.1, R-3.2; Standards table | Retrieve and extract clause-level slices from `26020-Package_Requirements.docx` heading 45 before final acceptance | TBD |
| CONF-03 | Vendor document review status convention not declared in accessible source | None in local DBM/registers | `26020-Package_Requirements.docx` vendor document tables (not directly read) | Specification R-1.2 | Adopt project document control convention once retrieved; default to Approved / Approved with Comments / Revise and Resubmit / Rejected | TBD |
