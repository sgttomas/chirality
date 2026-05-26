# Guidance — DEL-065-06 EPC Vendor Package Review and Acceptance

EpistemicStatus: DRAFT (Pass 1/Pass 2)

## Purpose

This deliverable closes the EPC-integrator review loop for the Caustic Tanks package (PKG-065). It establishes that the vendor's engineered equipment package and turnover documentation, taken together, satisfy the EPC Scope of Work, Package Datasheet, and Construction Work Package, and that the package is ready for handoff to construction, commissioning, and operations. (DELIVERABLE_REGISTER.csv row 491; `_CONTEXT.md` Scope.)

## Principles

- **Acceptance is evidence-based.** Acceptance positions rest on traceable artifacts (review log entries, checklist sign-offs, ITRs, turnover records), not opinion. (Authority hierarchy.)
- **EPC anchors govern.** The EPC SOW (DEL-065-01), Package Datasheet (DEL-065-02), and Construction Work Package (DEL-065-03) are the acceptance basis. Vendor work is measured against them, not against itself. (DELIVERABLE_REGISTER.csv rows 486–488.)
- **Code conformance is non-negotiable.** API 650 is the governing tank standard for this package. Code stamps, nameplates, and inspection records must be present before acceptance. (Package name; clause locations TBD.)
- **Caustic service drives constraints.** Material selection, indoor installation, freezing protection, safety showers, and fuel-gas blanketing are caustic-service-driven. They are not optional. (DBM-Deepcut lines 1552, 1562, 1566.)

## Considerations

- **Reference accessibility.** API 650 is not in the local source set; clause-level acceptance criteria must be obtained before final acceptance can be signed off. `26020-Package_Requirements.docx` is locally present but its slice for package heading 20 has not been extracted (binary file). Both should be opened during review.
- **Specific-gravity basis is TBC.** Fresh caustic tank design SG = 1.75 is marked TBC in the DBM. Acceptance should record vendor-confirmed value and any deviation. (DBM-Deepcut line 1562.)
- **Safety-shower coverage is open.** Shower quantity and location remain TBD per DBM; acceptance must not silently close this. (DBM-Deepcut line 1552.)
- **Material substitution risk.** "Polymer or other caustic-compatible materials" is the DBM phrase. Vendor-selected material must be reviewed for compatibility at 50 wt% NaOH service temperature, freezing protection, and venting. (DBM-Deepcut line 1566.)
- **Off-gas routing crosses package boundaries.** Spent caustic tank vapours route to an incinerator physically located at 3-25 facility. Acceptance must include the cross-facility interface evidence (KO drum, flame arrestor, supplemental fuel-gas basis). (DBM-Deepcut lines 1570–1572.)

## Trade-offs

- **Strict checklist vs. risk-weighted review.** A strict line-by-line checklist gives auditability but can mask integration risks (e.g., cross-facility incinerator interface). A risk-weighted review surfaces integration risk but is harder to evidence. The acceptance package should do both — checklist for code/datasheet conformance, risk register for integration items. (No source citation — guidance pattern.)
- **Acceptance with open TBDs.** Several DBM items (SG TBC, shower locations, materials, incinerator supplemental fuel-gas) are explicitly TBD. Holding acceptance until all are closed risks blocking turnover; accepting with open TBDs requires explicit, tracked carry-forward. The acceptance checklist should list each open item with owner and target close date (TBD).

## Examples

No worked acceptance examples are available in the local source set. (Omit; mark TBD when worked examples become available.)

## Conflict Table (for human ruling)

No source-vs-source conflicts identified in Pass 1/Pass 2 drafting. The recurrent pattern is **missing source slices**, not source conflict:

| Conflict ID | Conflict (short) | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| (none) | — | — | — | — | — | TBD |

Open items needing human ruling are listed under Considerations and as TBDs in the Specification.
