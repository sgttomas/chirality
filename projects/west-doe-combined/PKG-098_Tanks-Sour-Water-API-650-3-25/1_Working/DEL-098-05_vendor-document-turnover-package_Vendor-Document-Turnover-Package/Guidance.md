# Guidance — DEL-098-05 Vendor Document Turnover Package

## Purpose

This deliverable exists because the PKG-098 sour-water tank package is procured from a Package Vendor while the EPC Integrator owns facility integration. The Package Vendor's design, fabrication, and quality evidence must be captured in a structured document set that (a) demonstrates compliance with the package requirements, (b) supports EPC integration design (interfaces, tie-ins, foundations by others, electrical/instrumentation by others), and (c) provides the legal/operational turnover record that the facility owner relies on for operate-and-maintain. Source: `_CONTEXT.md` Scope; PACKAGE_REGISTER PKG-098 responsibility text; SCOPE_LEDGER SOW-0221.

## Principles

1. Source primacy. The vendor document set is defined by `26020-Package_Requirements.docx` package heading 50, Vendor Engineering Deliverables table, as enumerated in ARTIFACT_REGISTER for DEL-098-05. The vendor does not unilaterally substitute its in-house list for the project list.
2. Interface alignment. Because foundations, on-site mounting, electrical, instrumentation, platforms and staircases are "by others" (SOW-0224), the vendor's interface-side documents (anchor bolt drawings, foundation calcs, instrument I/O list, junction-box drawings, structural GA) carry disproportionate weight: they are the contract surface against which "by-others" scope executes.
3. Sour-service rigor. Service is sour produced water; site basis is -40 deg C minimum ambient (3-25_Comp_and_Liquids_DBM.md). Material certificates (QLT-013), coating evidence (Devchem 253), and insulation/heat-tracing documents are first-class turnover items, not optional addenda.
4. Turnover, not transmittal. The deliverable is judged on a complete final state (Vendor Data Book / Final Supplier Documentation, PRQ-016), not on the cumulative count of transmittals.
5. Decomposition is routing, not authority. The Gate 7 snapshot defines what to produce; clause-level requirements come from the package requirements document and API 650, not from decomposition prose.

## Considerations

- Capacity / design throughput points to "Appendix A" in source (SOW-0224); the vendor data book must include the resolved Appendix A values when available, not the TBD.
- The package heading 50 quote lists the same tanks under "Major included equipment" three times by item; the vendor index must show the resolved count (3+2+2 = 7 tanks per SOW-0223) consistently across data sheets, MTRs, and the SPIR.
- Item No. 2 operating temperature is TBD in source (SOW-0224); coating and skim-system suitability under that operating range is a turnover-record concern, not just a design-phase concern.
- Modified API 650 (vs. baseline API 650) implies a deviation register; the vendor's Storage Tank Data Sheets and Static Equipment Specifications should make modifications explicit and traceable.
- Interfaces enumerated in INTERFACE_REGISTER for PKG-098 are all "YES" (active). Missing any interface-document category from the turnover package will materially block EPC integration.

## Trade-offs

- Granularity of the document index. A document-per-tank index is more traceable for MTRs and Inspection Release Certificates but inflates the index; a category-rolled index is leaner but harder to audit per-tag. The chosen position should be recorded in the Vendor Document Control Procedure (DOC-008).
- Native-format vs. PDF turnover. Native CAD/calc files support downstream reuse; PDF supports archival integrity. Source does not specify; ASSUMPTION: both are typically required and the EPC Integrator's document control standard governs.
- Inclusion of "by others" interface drawings (foundation, anchor bolts). The vendor must produce these as bases for "by others" execution; whether they are stamped by the vendor's or the EPC's engineer-of-record is project-specific and TBD in source.

## Examples

Source-supported example: The "Core vendor documents" category includes both an inspection-release artifact (QLT-020) and a manufacturing record book (QLT-021). The intent is that each tank ships with a release certificate referenced from the consolidated MRB so that the field receiving party can verify shipment against the final book.

Source-supported example: For the relief / flare / vent interface, the vendor produces the Relief and Flare Design Basis, PSV / Pressure Relief Sizing Calculations, Relief Valve Data Sheets, Flare Load Summary / Flare System Study, and a Blowdown / Depressurization Study (ARTIFACT_REGISTER). The flare-side system itself is not in the vendor's physical scope, but the loads the tank package contributes are, and those loads are the input the EPC Integrator's facility-level flare study consumes.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CT-01 | Modified API 650 vs. unmodified API 650 — the standard is named "modified" in SOW-0223 but the nature/list of modifications is not in the locally accessible source slice. | SCOPE_LEDGER SOW-0223 | API 650 itself (clause text not locally accessible) | Specification REQ-09, Datasheet "Design / fabrication code", IOM acceptance | PROPOSAL: vendor shall maintain a deviation register against base API 650 and include it in the Vendor Data Book. | TBD |
| CT-02 | Item count consistency — `SOW-0223` lists tank items by Item No. 1, 2, 3 (3 + 2 + 2 = 7 tanks) but `SOW-0222` references only "Item No. 1: Three (3) ... Sour Produced Water Storage Tanks" under "Basic scope". | SCOPE_LEDGER SOW-0222 (Basic scope) | SCOPE_LEDGER SOW-0223 (Major included equipment) | Datasheet "Package equipment scope"; Specification REQ-09; Vendor Document Index | PROPOSAL: treat SOW-0223 (Major included equipment) as the authoritative tank list (7 tanks) and treat SOW-0222 Basic scope as the headline subset. | TBD |
| CT-03 | Item No. 2 operating temperature listed as TBD in SOW-0224 while design-temperature window is fully specified. | SCOPE_LEDGER SOW-0224 | (no second source locally available) | Datasheet "Operating temperature"; Specification REQ-13; coating and insulation justification | PROPOSAL: vendor proposes Item No. 2 operating temperature in the Mechanical Design Basis (MEC-001) for EPC ruling at first MEC-001 submittal. | TBD |
| CT-04 | Driver listed as TBD in SOW-0224, but storage-tank packages frequently have pump-driver or mixer-driver implications. | SCOPE_LEDGER SOW-0224 | (no second source locally available) | Datasheet "Driver"; Mechanical Equipment List (MEC-002) | PROPOSAL: vendor confirms in MEC-002 that the tank package contains no rotating equipment requiring a driver, or proposes the driver if applicable. | TBD |
| CT-05 | Capacity / design throughput is referenced to "Appendix A" which is not in the locally accessible source slice. | SCOPE_LEDGER SOW-0224 | Appendix A of package requirements (not extracted) | Datasheet "Capacity / design throughput"; Mechanical Calculation Package | PROPOSAL: vendor requests Appendix A from EPC Integrator at kickoff and includes resolved values in MEC-001 and Storage Tank Data Sheets. | TBD |
| CT-06 | Objective association heuristic — `_CONTEXT.md` lists OBJ-002..OBJ-010 by package heuristic, not by deliverable-ID confirmation. | `_CONTEXT.md` Supports Objectives | OBJECTIVE_DELIVERABLE_MAP.csv (no DEL-098-05 explicit row sampled) | Datasheet Notes; Guidance Purpose | PROPOSAL: keep as ASSUMPTION; human ruling sets the binding objective list. | TBD |
