# Guidance: DEL-030-06_epc-vendor-package-review-and-acceptance

## Purpose

This guidance directs how the EPC Integrator should conduct review and acceptance of the Package Vendor's engineered equipment package (DEL-030-04) and vendor document turnover package (DEL-030-05) for `PKG-030`, the Transformer TXP-8200-1 step-down distribution transformer (2.5 MVA, 13.8 kV / 600/347 V). Its purpose is to produce traceable acceptance evidence that the vendor package integrates with the facility per the EPC Scope of Work (DEL-030-01), Package Datasheet (DEL-030-02), and Construction Work Package (DEL-030-03), without substituting EPC opinion for vendor design or for accepted decomposition truth.

## Principles

- **Source-grounded acceptance.** Acceptance decisions cite the accepted source slice (Gate 7 register row, DBM paragraph, vendor data sheet) being relied on. If no source supports the criterion, mark `TBD` rather than asserting acceptability.
- **Interface-first review.** Review is organized around the seven accepted interface facts for `PKG-030` (Electrical Power, Grounding / Bonding, Area / Exterior Lighting, I&C / Control Cabling, Communications / Network, Maintenance Access, Structural / Foundations / Supports) and against the acceptance basis deliverables, not around free-form opinions.
- **Vendor responsibility preserved.** EPC review does not redesign the vendor's package. Comments are framed as integration constraints or evidence requests, not as substitute engineering.
- **Human approval authority.** The acceptance checklist requires a human EPC Integrator approver signature. This skill, this deliverable, and any agent produce evidence and proposals only (K-AUTH-1).
- **Open items are visible.** Unresolved items at handoff are listed with owner, due date, and risk note, not hidden inside narrative.

## Considerations

- The DBM expects 13.8 kV plant switchgear feeding step-down transformers radially to 600 V services. PKG-030's TXP-8200-1 fits this pattern; the acceptance basis should confirm primary/secondary tie-in points and the 600 V high-resistance grounding scheme (5 A continuous resistor) at the transformer secondary.
- Large oil-filled transformers per the DBM are spaced per CEC and generally installed on structural steel transformer bases; secondary containment requirements shall be reviewed. The vendor's selection (oil-filled vs. dry-type) drives spacing, containment, and foundation review and must be confirmed in vendor submittals before acceptance.
- The DBM requires distribution transformers to have a separate copper ground conductor connected directly to ground, sized per CEC, in addition to grounding conductors run with power wiring. EPC acceptance should evidence this connection on installation.
- The 347 V leg implied by the package name (600/347 V) is typical of a wye secondary used for lighting/utility services; explicit lighting/load assignments to this transformer's 347 V secondary are TBD pending vendor and detailed design.
- Workbook row 32 confirms WBS 01 and CoA 26020-01-30-021. Differences between TXP-8200-1 (PKG-030, WBS 01) and the similar TXP-8600-1 (PKG-029, WBS 01) and PKG-016 (3 MVA, WBS 02) should not be conflated in the review log.

## Trade-offs

- **Comment depth vs. timeline.** Deep EPC comments improve integration confidence but can lengthen vendor cycles. Bias depth toward interface-fact and grounding/foundation items where DBM provides clear acceptance basis.
- **Test scope expansion vs. source support.** Adding tests beyond vendor standard scope must be tied to a source-supported requirement; otherwise carry as `TBD` rather than imposing.
- **Acceptance with deviation vs. rework.** When a vendor deviation does not violate an accepted source requirement, an accepted-with-deviation disposition with reference is preferred over rework; otherwise an open punch item with owner.

## Examples

- A vendor submittal shows a single-point grounding bond to the transformer tank. The DBM states major electrical equipment shall be connected to the ground grid at two points. EPC disposition: comment requesting two-point connection with field evidence at acceptance, citing the DBM grounding paragraph.
- A vendor proposes routing secondary cable tray across the transformer maintenance pull area. The DBM states cable tray/conduit shall not interfere with maintenance access. EPC disposition: comment to reroute, citing the cable tray/conduit paragraph and the Maintenance Access interface fact (IFC-345609CB34).

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONF-030-06-001 | DBM Transformers paragraph references oil-filled transformers as the spacing basis, but vendor selection for TXP-8200-1 (oil-filled vs. dry-type) is not fixed by accepted source. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Transformers paragraph | `PACKAGE_REGISTER.csv` row `PKG-030` (no oil/dry designation) | Datasheet Construction; Specification REQ-030-06-006; Guidance Considerations | PROPOSAL: keep acceptance basis conditional on vendor selection; do not assert oil-filled in EPC documents. | TBD |
| CONF-030-06-002 | Test-standard family for routine/type tests (IEEE C57 vs. IEC 60076 vs. CSA) is not fixed by accepted source slices. | DBM electrical section (no test-standard call-out for this transformer class) | `26020-Package_Requirements.docx` (not opened for PKG-030) | Specification REQ-030-06-004, Standards | PROPOSAL: list candidate standards as ASSUMPTION; require vendor to declare the governing standard, then EPC accepts/comments. | TBD |

## Human-Ruling Required Items

- HRR-030-06-001: Confirm the governing transformer test standard family (IEEE C57 / IEC 60076 / CSA) for acceptance evidence scope; current pass carries this as ASSUMPTION with multiple candidates.
- HRR-030-06-002: Confirm whether TXP-8200-1 is procured as oil-filled or dry-type; this affects CEC spacing, secondary containment, and foundation acceptance criteria.
- HRR-030-06-003: Confirm package-specific objective-deliverable association (currently package-heuristic ASSUMPTION).
