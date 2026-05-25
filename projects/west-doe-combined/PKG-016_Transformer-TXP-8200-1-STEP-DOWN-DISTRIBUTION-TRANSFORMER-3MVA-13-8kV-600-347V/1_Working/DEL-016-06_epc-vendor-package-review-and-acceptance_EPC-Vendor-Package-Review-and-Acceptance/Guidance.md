# Guidance: DEL-016-06_epc-vendor-package-review-and-acceptance

## Purpose

This deliverable is the EPC Integrator's evidence that the PKG-016 vendor package (the 13.8 kV / 600 V, 3 MVA distribution transformer TXP-8200-1) has been reviewed against the EPC reference set (Scope of Work, Package Datasheet, Construction Work Package), is integration-ready, and is ready for handoff into facility-level commissioning. It does not author the design and it does not certify the package; it records and dispositions what the vendor produced.

## Principles

- **Authority hierarchy.** Source materials in `_Sources/` (especially `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`) and the Gate 7 decomposition registers are authoritative. The EPC Scope of Work (DEL-016-01), Package Datasheet (DEL-016-02), and Construction Work Package (DEL-016-03) define what the vendor was asked to do. The vendor's submittals (DEL-016-04, DEL-016-05) define what they delivered. This deliverable records the comparison.
- **Acceptance, not approval.** Per K-AUTH-1, only humans author binding approval records. Acceptance artifacts here are evidence and disposition records; they do not constitute approval, certification, or release for reliance.
- **Source-grounded dispositions.** Each disposition (accept, accept-with-comment, reject-and-resubmit) should cite the EPC reference clause or source it was compared against. Where a clause cannot be located, mark `location TBD` rather than asserting compliance.
- **Interface coverage is mandatory.** Every interface type declared in `INTERFACE_REGISTER.csv` for `PKG-016` should produce at least one disposition line item.
- **Conservative assumptions.** Where the vendor scope, the package title, and the DBM tables interpret differently (see Conflict Table below), surface the conflict rather than picking one silently.

## Considerations

- **Primary feeder and grounding regime.** The 13.8 kV primary is a 3-wire, 60 Hz, LRG system fed from 04-25; the 600 V secondary side is the LV MCC service which is 3-wire HRG with a 5 A continuous resistor. Acceptance of the transformer secondary therefore needs to confirm vendor neutral arrangement matches the HRG basis on the LV side and does not introduce an unintended solidly grounded neutral.
- **Title says "600/347 V"; DBM table says 600 V 3-wire only.** The "347 V" component implies a 4-wire (line-to-neutral 347 V from a 600 V system) secondary that is not explicitly carried in the DBM system-voltage table. The acceptance record must resolve this interpretation explicitly. See Conflict Table CT-016-06-01.
- **Standards anchors are not enumerated.** Accessible sources do not name the specific transformer design and test standard (e.g., CSA C88, IEEE C57.12.00/.90/.91 family). Acceptance dispositions on factory test reports should remain partial until DEL-016-02 or vendor data names the governing standard.
- **Hazardous area context.** The transformer's specific area classification is governed by detailed classification drawings, not the general Zone 2 statement; ensure the vendor was given the correct classification and that any vendor-supplied apparatus is suitable.
- **Cold-weather basis.** -40 deg C minimum ambient is the governing site condition unless a vendor condition is more severe; this affects bushing selection, oil (if oil-filled), gasketing, and any cabinet heaters.
- **Maintenance access and raceways.** Cable tray and conduit routing shall not interfere with maintenance access; for a 3 MVA distribution transformer this typically includes radiator access, bushing access, and any oil-handling clearance.
- **EPC role is integrator.** Acceptance evidence should focus on integration fitness (interfaces, foundation/anchorage, raceways, control termination map) rather than re-doing vendor design.

## Trade-offs

- **Depth vs. timeliness.** Deeper inspection (e.g., independent re-checking vendor calculations) improves confidence but slows handoff; the acceptance checklist should make the chosen depth explicit per line item.
- **Documenting absent items vs. waiting.** When a vendor item is missing, recording the gap on the review log with a "reject-and-resubmit" disposition is preferable to leaving the line blank, even if it delays acceptance.
- **Assumption labelling vs. silent reconciliation.** Where the package title (600/347 V) and the DBM table (600 V 3W only) disagree, recording the interpretation as ASSUMPTION and routing it through the Conflict Table is preferable to silently choosing one interpretation.
- **Standards naming.** When the governing transformer standard is unnamed, requiring the vendor to nominate the standard they tested to (and accepting it as ASSUMPTION pending DEL-016-02 confirmation) is preferable to a blanket "tested to applicable standards" acceptance.

## Examples

- *Disposition example — accept.* "Vendor factory routine test report shows induced and applied voltage tests per the governing transformer standard; nameplate matches DEL-016-02 specified primary/secondary voltages and capacity; no exceptions. Disposition: ACCEPT."
- *Disposition example — accept-with-comment.* "Vendor cold-weather declaration states -40 deg C ambient capability; gasket material catalogued for -45 deg C minimum — no impact, exceeds requirement. Disposition: ACCEPT-WITH-COMMENT (gasket variant confirmed)."
- *Disposition example — reject-and-resubmit.* "Vendor grounding drawing depicts solidly grounded LV neutral; project LV basis is HRG with 5 A continuous resistor (DBM "System Voltages"). Disposition: REJECT-AND-RESUBMIT (LV neutral arrangement to be revised or formally exempted)."

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CT-016-06-01 | Package title carries "600/347 V" implying a 4-wire LV secondary, but the DBM "System Voltages" table describes 600 V LV service as 3-phase, 3-wire HRG only. | Workbook Packages row 18 (package title, via `PACKAGE_REGISTER.csv` row `PKG-016`) | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, "System Voltages" | Datasheet "Acceptance secondary nominal (347 V)"; Specification REQ-016-06-07 | Treat "600/347 V" as title/identity; require the EPC Package Datasheet (DEL-016-02) to define whether the package delivers a 4-wire secondary (and the basis for the 347 V neutral) or whether 347 V is provided by a downstream dry-type transformer; reflect the resolution in the acceptance record. | TBD |
| CT-016-06-02 | Governing transformer standard for design and routine/type/special tests is not enumerated in accessible sources. | `_REFERENCES.md` (no specific transformer standard listed) | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (no transformer standard enumeration) | Specification REQ-016-06-12, REQ-016-06-13; Standards table | Require DEL-016-02 EPC Package Datasheet or DEL-016-04 Vendor Engineered Equipment Package to cite the governing transformer standard set (likely CSA C88 / IEEE C57 family) and record it in the acceptance Standards table. | TBD |
| CT-016-06-03 | Acceptance disposition vocabulary (Accept / Accept-with-comment / Reject-and-resubmit) is proposed; no project-level disposition vocabulary is found in accessible sources. | This deliverable's drafted content | None in `_Sources/` or registers | Datasheet "Disposition states"; Specification REQ-016-06-15 | Adopt the proposed three-state vocabulary unless project document control specifies otherwise. | TBD |

## Decomposition note

Objective association (OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010) is carried from `OBJECTIVE_DELIVERABLE_MAP.csv` rows that map by deliverable ID within the PKG-016 group. The rows in the snapshot identify this deliverable explicitly, so the objective association here is direct, not heuristic.
