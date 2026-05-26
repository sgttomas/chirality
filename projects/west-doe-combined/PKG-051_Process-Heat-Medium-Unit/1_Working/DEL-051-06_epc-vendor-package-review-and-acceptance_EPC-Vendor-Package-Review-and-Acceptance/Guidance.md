# Guidance: DEL-051-06 — EPC Vendor Package Review and Acceptance

> Directional guidance for performing the EPC Integrator's review-and-acceptance of the PKG-051 vendor package. This document explains why the work is shaped the way it is, what to weigh when judgement is required, and where common trade-offs land.

## Purpose

The EPC Integrator owns final integration of the Process Heat Medium Unit into the facility, but the package itself is engineered, fabricated, and largely supplied by the Package Vendor (DEL-051-04). DEL-051-06 exists so that the EPC has an explicit, auditable record that:

1. The vendor's package meets the EPC's scope-of-work, datasheet, and construction-work-package requirements (DEL-051-01/02/03).
2. The vendor's documentation set is complete and is properly captured in the turnover package (DEL-051-05).
3. The package is physically ready to be operated and handed over to operations.

This is the deliverable that converts "vendor work delivered" into "vendor work accepted" for governance purposes.

## Principles

- **Acceptance is an EPC Integrator decision, not a vendor decision.** The vendor demonstrates; the EPC accepts (or accepts with conditions, or rejects). Per K-AUTH-1, no agent (including this skill) may issue the acceptance.
- **Source-grounded conformance.** Every "accepted" item should point back to a specific EPC requirement (DEL-051-01/02/03) and a specific vendor evidence artifact (datasheet, test report, etc.). Reviewer opinion alone is not acceptance evidence.
- **Acceptance is a portfolio of dispositions, not a single sign-off.** Document review, design conformance, fabrication evidence, installation evidence, commissioning evidence, and turnover evidence are independently dispositioned; the package-level acceptance memo summarises them.
- **Defer to source when in doubt.** Where the source DBM, scope of work, or datasheet conflicts with vendor narrative, the EPC documents (and ultimately the DBM) govern.
- **Punchlist over re-work.** When acceptance items remain open at handover, prefer a tracked outstanding-items list with named owners and dates over either (a) accepting silently with hidden risk, or (b) refusing handover when residual items are operationally tolerable.

## Considerations

- **Single-loop heat medium basis is recent.** The DBM's single unified loop at 220 deg C supersedes prior hot/cold segregation and retires the depropanizer reboiler from the heat medium loop. Acceptance should explicitly check that the vendor package reflects the single-loop basis and not legacy two-loop assumptions. *(Source: DBM-Deepcut "Heat Medium Basis".)*
- **Several DBM parameters are TBC/TBD.** Pour point, maximum tubeskin/film temperature, heater available duty for H-5170-1, circulation rates, lateral header pressure drops, and pump sparing basis are all flagged in the DBM. The acceptance review is the appropriate moment to close most of these via vendor confirmation letters. Closing them is a precondition for clean acceptance.
- **Heater minimum-flow protection.** The DBM assumes 85% of design flow as the heater minimum-flow basis pending vendor confirmation. Review must confirm that user bypasses and heater minimum-flow control valves are present in the vendor scope so the single-loop system can hold minimum flow as users turn down.
- **Pop-tank sour-rupture exposure.** The DBM flags sour tube-rupture venting to the pop tank as requiring detailed-engineering review including dispersion modeling if needed. Acceptance should not silently close this; it is either (a) demonstrated unnecessary by the vendor analysis, or (b) carried as a tracked conditional acceptance item.
- **Vendor document interlock with DEL-051-05.** DEL-051-06's document review log is naturally a view onto DEL-051-05's vendor document register. Avoid creating a duplicate register; cite the turnover-package register.
- **Inaccessible primary sources.** The vendor package requirements text (`26020-Package_Requirements.docx` heading 6) and interface workbook (`26020-Packages_Interfaces_4_export.xlsx`) are not locally readable as text. Acceptance criteria that depend on those documents remain TBD until either (a) text extracts are produced, or (b) the EPC reviewer interprets them directly during the run.

## Trade-offs

| Trade-off | Toward stricter acceptance | Toward more permissive acceptance |
|---|---|---|
| Vendor letter vs. shop test for fluid suitability | Demand shop test at maximum bulk temperature | Accept vendor written confirmation with manufacturer data |
| Heater sparing (1 x 125% vs. N x small) | Multiple-unit sparing improves reliability and turndown | Single-unit sparing reduces capex/footprint; matches current DBM basis |
| Pop-tank sour-rupture mitigation | Require dispersion modeling and possibly secondary mitigation | Accept low-likelihood disposition with operating procedure controls |
| Turnover at substantial completion vs. mechanical completion | Accept only at mechanical completion with full punchlist clearance | Accept at substantial completion with tracked carry-over items |
| Document closure threshold | Hold acceptance until 100% vendor docs received | Accept with documented exception list for low-criticality items |

These trade-offs are project-policy calls and ultimately human rulings.

## Examples

- *Example A — fluid-rating confirmation.* The DBM names Brenntag Petrotherm as the heat medium fluid and 599 deg F / 315 deg C as the maximum bulk fluid temperature. A typical acceptance closure here is a vendor letter referencing the manufacturer's product data confirming bulk-fluid suitability at the stated maximum, attached to the acceptance checklist row for REQ-051-06-011.
- *Example B — heater minimum-flow.* The DBM's 85% minimum-flow basis is preliminary. Acceptance closure for REQ-051-06-014 is the heater vendor's written minimum-flow capability statement plus a P&ID/PFD showing user bypasses and minimum-flow control loops sized accordingly.
- *Example C — PSV seat tightness.* For REQ-051-06-021, acceptance evidence is a PSV test certificate per API STD 527, filed by tag in the acceptance package, with traceability to the vendor PSV datasheet.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| CONF-001 | Heater sparing basis | DBM-Deepcut Heat Medium Basis (1 x 125%, pending review) | Potential alternative (2 x 62.5% or 3 x 41.7%) noted in same DBM section | Datasheet "Conditions"; Specification REQ-051-06-013/019; Procedure step "Accept design package" | PROPOSAL: defer to vendor recommendation supported by reliability analysis | TBD |
| CONF-002 | Vendor-package detailed acceptance criteria | DBM-Deepcut (heat-medium technical) | `26020-Package_Requirements.docx` package heading 6 (binary; not text-accessible) | Specification REQ-051-06-030/031/040/041/050; Procedure inspection/turnover steps | PROPOSAL: extract `26020-Package_Requirements.docx` heading 6 to markdown before final acceptance to ground SOW-rooted criteria | TBD |
| CONF-003 | Interface boundary detail for PKG-051 | DBM-Deepcut (process narrative) | `26020-Packages_Interfaces_4_export.xlsx` Package 51 rows (binary; not text-accessible) | Datasheet "Attributes"; Specification REQ-051-06-050 | PROPOSAL: extract interface workbook rows for PKG-051 to markdown to support traceability matrix | TBD |
