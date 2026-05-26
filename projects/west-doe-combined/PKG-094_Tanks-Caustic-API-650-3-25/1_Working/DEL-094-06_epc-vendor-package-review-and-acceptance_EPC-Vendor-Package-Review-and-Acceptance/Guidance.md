# Guidance — DEL-094-06 EPC Vendor Package Review and Acceptance

## Purpose

This deliverable exists because the Package Vendor owns engineering, design, supply, and vendor documentation for the Tanks, Caustic (API 650) 3-25 package, while the EPC Integrator is responsible for integrating the package into the 03-25 facility and accepting it on behalf of the project. Without a controlled EPC-led review and acceptance step, vendor work cannot be safely confirmed as ready for installation, commissioning, and turnover — particularly for a caustic-service package with multiple TBC source items (material/coating, SG, drain temperature) and notable safety controls (vapour blanket, flame arrestor, aluminum exclusion).

Source rationale: the decomposition explicitly separates Package Vendor responsibility from EPC Integrator responsibility (OBJ-004), and the Gate 5 decomposition adds this deliverable specifically to capture EPC review/acceptance evidence (`DELIVERABLE_REGISTER.csv` `DEL-094-06` row "Additional Gate 5 deliverable framed as EPC-integrator review and acceptance evidence").

## Principles

1. **EPC reviews; vendor designs.** The EPC does not re-engineer the vendor's package; it verifies conformance against the SOW, Package Datasheet, and Construction Work Package. (Source: OBJ-004.)
2. **Source-anchored acceptance.** Every accept/reject decision SHOULD reference a specific clause of the EPC anchor deliverables or a clause of `26020-Package_Requirements.docx` heading 46 (clause-level text `location TBD` in source slice).
3. **Multi-discipline sign-off.** Mechanical, electrical, controls/I&C, and civil/structural disciplines each verify their respective interfaces before acceptance (OBJ-005, OBJ-006, OBJ-008).
4. **Open items are explicit.** No item is silently closed; open items at acceptance carry explicit human-approved carry-over (OBJ-010).
5. **Caustic-service awareness is non-optional.** Materials, coating, embrittlement review, and aluminum exclusion are first-order acceptance items, not nice-to-haves (DBM lines 402, 493; OBJ-009).
6. **Cold-temperature awareness.** -40 °C governs exposed components; heat tracing, insulation, and instrumentation must be checked for cold-service applicability (DBM Site Basis line 145).
7. **Vapour-handling discipline.** Spent-caustic vapour routes through a flame arrestor to the incinerator header; fresh-caustic is explicitly NOT on the VRU. Vapour-path conformance is a safety-relevant acceptance item (DBM line 402).

## Considerations

- **Source-text gaps.** Detailed package requirements live in `26020-Package_Requirements.docx` heading 46, which is not directly readable from the current source set. Clause-level acceptance criteria are `location TBD`. Reviewers should escalate to retrieve and trace those clauses before final acceptance.
- **DBM TBC items propagating into acceptance.** The DBM itself carries TBC items relevant to this package: caustic solution SG 1.75 (line 402), caustic tank material/coating (line 402), caustic drain max temperature 121 °C / 250 °F (line 493), heat-tracing redundancy (line 493). Acceptance cannot resolve these unilaterally; it depends on detailed-design closure.
- **Cross-package interfaces.** Caustic tanks interface with: the C5+ non-regenerative caustic mercaptan treating package (contactor/pre-heater/water wash/filter — DBM line 400), the incinerator (via spent-caustic vent flame arrestor — line 402), the LP fuel-gas blanket system (line 402), the caustic drain header (line 493), and the H2O2 treatment package (line 216). Each interface's owning package readiness should be checked before declaring acceptance complete.
- **Turnover boundary.** Pipeline tie-out is by others past the facility riser; the EPC is accountable only up to the defined interface (DBM SEC-04 line 216).
- **Caustic regeneration is excluded.** DBM line 389 explicitly states caustic regeneration is not part of the 03-25 basis. Reviewers must not accept vendor scope expansions that imply regeneration capability without a controlled change.
- **Acceptance evidence vs construction evidence.** Construction Work Package (`DEL-094-03`) captures *how* the package is installed; this deliverable captures *whether the vendor's package itself* is acceptable. Avoid conflating the two evidence sets.

## Trade-offs

- **Speed vs traceability.** Closing acceptance quickly with informal sign-offs reduces traceability and weakens later turnover and warranty positions. The decomposition (OBJ-010) prioritises traceability and explicit closure evidence.
- **Strict-conformance vs change accommodation.** Vendor as-built differences from the Package Datasheet may be benign or material. For caustic service, deviations in material/coating or vent-path arrangement are presumptively material and SHALL be processed via a documented change record (RFI/DCN equivalent).
- **EPC scope creep risk.** Excessive EPC review can drift into vendor engineering territory, violating OBJ-004. Keep EPC review focused on conformance, integration, and turnover readiness — not on redesign.

## Examples

- Example (acceptance with carry-over): Vendor delivers the caustic tank set per Datasheet, hydrotest pass, flame arrestor function check pass, but caustic tank coating selection remains TBC pending detailed-design closure of DBM line 402. Acceptance recorded as **Conditional Accept** with the coating-selection item tracked to closure by a documented date; turnover gated on closure. (Illustrative — convention `TBD`.)
- Example (rejection): Vendor delivers tanks with aluminum gratings or platforms in the caustic building. Per R-5.2 and DBM line 402, the package is **Rejected** until non-aluminum materials are substituted or an explicit deviation is approved by the owner.

## Conflict Table (for human ruling)

HRR items (caustic-package-specific) are surfaced explicitly below. All `TBD` rulings require human authority to close.

| Conflict ID | Conflict (short) | Source A | Source B | Impacted Sections | Proposed Authority (PROPOSAL) | Human Ruling (TBD) |
|---|---|---|---|---|---|---|
| CONF-01 | Caustic solution SG 1.75 carried as TBC | DBM line 402 (states "TBC") | Vendor as-designed values (not yet available) | Datasheet Attributes; Specification R-2.4 | Resolve in detailed design; carry as TBC until vendor confirms; acceptance gated by resolution record | TBD |
| CONF-02 | Caustic tank material and internal coating "remain TBC" | DBM line 402 (explicit TBC) | Vendor material/coating selection (not yet declared) | Datasheet Attributes; Specification R-2.5, R-5.1 | Vendor declares material/coating; EPC verifies against project specs and embrittlement review (line 493); deviation requires change record | TBD |
| CONF-03 | Caustic drain max temperature 121 °C / 250 °F TBC; heat-tracing redundancy "under consideration" | DBM line 493 (TBC and "under consideration") | Vendor drain design (not yet declared) | Datasheet Conditions; Specification R-3.4 | Close in detailed design; verify against vendor drain design; record in interface acceptance form | TBD |
| CONF-04 | Clause-level API 650 / package-requirements acceptance criteria not in accessible source set | DBM line 402 (references API 650 framing) | `26020-Package_Requirements.docx` heading 46 (binary; not readable from local source) | Specification R-3.1, R-3.2; Standards table | Retrieve and extract clause-level slices from `26020-Package_Requirements.docx` heading 46 before final acceptance | TBD |
| CONF-05 | Vendor document review status convention not declared in accessible source | None in local DBM/registers | `26020-Package_Requirements.docx` vendor document tables (not directly read) | Specification R-1.2 | Adopt project document control convention once retrieved; default to Approved / Approved with Comments / Revise and Resubmit / Rejected | TBD |
| CONF-06 | Unit count per caustic tank service not explicit in DBM | DBM line 40 (enumerates the tank set: process-water, fresh-caustic, spent-caustic, H2O2) | DBM line 400 (lists tank functions but not counts) | Datasheet Attributes; Specification R-2.2 | Assume one tank per service at 400 bbl pending Package Datasheet (`DEL-094-02`) confirmation | TBD |
| CONF-07 | Aluminum exclusion scope across ancillary items | DBM line 402 (states aluminum not used in caustic building) | Vendor BOM (not yet available) | Specification R-5.2 | Apply exclusion to fasteners, gratings, ladders, platforms, and ancillary items; vendor must declare in materials list | TBD |
