# Guidance — DEL-041-06 EPC Vendor Package Review and Acceptance

## Purpose

This deliverable exists so the EPC Integrator can demonstrate, with evidence, that the vendor-supplied standby-generator package (PKG-041) is fit for integration into the West Doe facility against the EPC Scope of Work (`DEL-041-01`), the EPC Package Datasheet (`DEL-041-02`), and the EPC Construction Work Package (`DEL-041-03`). It is the integration-acceptance and handoff-readiness boundary between the Package Vendor's owned scope and the EPC Integrator's owned scope, as defined in GATE-07 `PACKAGE_REGISTER.csv` row `PKG-041`.

## Principles

- **Acceptance is a human act.** Agents may organize, draft, and propose dispositions; only humans may issue binding acceptance or approval-for-reliance (`K-AUTH-1`).
- **Acceptance is evidence-bound.** Every accepted line in the review log or checklist must cite the underlying vendor document or test record. Where evidence is missing, the line is `TBD`, not an asserted pass (`K-PROV-1`).
- **The EPC artifacts are the acceptance ruler.** The Scope of Work, Package Datasheet, and Construction Work Package set what the vendor package must satisfy. The vendor's own design basis is acceptance input, not acceptance criterion.
- **Interfaces drive integration acceptance.** Each applicable PKG-041 interface type from GATE-07 `INTERFACE_REGISTER.csv` (twelve types listed in `Datasheet.md`) must be explicitly covered.
- **Source-grounded conservatism.** When source material is not locally accessible (for example, the workbook DOCX or specific engine/generator standards), record `TBD` rather than infer detailed acceptance criteria.

## Considerations

- **Workbook title vs. current DBM basis.** The package row title ("13.8kV, 3.0MW STANDBY GENERATOR BUILDING (490-1)") reflects an earlier emergency-generator concept. Both DBMs in the accessible source set explicitly supersede it with an LV (low-voltage) standby-generator architecture on the LV MCC with transfer switch (DBM-Comp_and_Liquids line 505; DBM-Deepcut line 175). Acceptance must not silently choose one description over the other; the discrepancy is surfaced in `CONF-041-06-001` for human ruling.
- **Responsibility split.** Per `PACKAGE_REGISTER.csv` row `PKG-041`, the Package Vendor owns package engineering, design, vendor documentation, and the physical equipment package; the EPC Integrator owns facility integration. Acceptance commentary on vendor-internal design should be limited to integration consequences, not redesign demands.
- **Upstream maturity.** Acceptance is meaningful only when upstream EPC deliverables (`DEL-041-01`, `-02`, `-03`) are stable enough to serve as a ruler. The PREPARATION dependency view records `DECLARED` mode with no edges yet; if acceptance is started before upstream maturity is declared, surface the gap rather than asserting acceptance.
- **Facility utility context.** DBM-Deepcut establishes the emergency-generator fuel-gas interface (less than 66 psig normal, 0.468 MMSCFD design, 3.6 MMSCFD 30-s start gas, local particulate filter) and packaged-enclosure expectations (outdoor weather-protective enclosure, 1 m walkway, MLE-confirmed overhead lift provisions). Reviewers should anchor utility-interface acceptance to these facts.
- **Open vendor parameters.** Generator make/model/rating, switchgear assignment, transfer switch configuration, fuel selection, battery/charger sizing, diesel storage (if any), and generator count are listed as open in the DBM. Acceptance must register each as a punch-list item until vendor data closes it.
- **Documentation gap upstream.** PKG-041's vendor document register (in `DEL-041-05`) is not yet baselined; vendor document review entries here will inherit `TBD` items until that register stabilizes.

## Trade-offs

- **Breadth vs. depth in the review log.** A broad pass-by-document review is cheap but weak evidence; a clause-by-clause review is expensive but auditable. Prefer clause-by-clause review for safety-relevant (Fire & Gas), area-classification, and interface-relevant clauses; document-level review elsewhere.
- **Early acceptance vs. waiting for full vendor turnover.** Provisional acceptance with a punch list accelerates construction but creates downstream rework risk if interfaces shift. Provisional acceptance should be explicit and time-bounded, not implicit.
- **Strict source grounding vs. operational pragmatism.** When acceptance criteria require standards that are not locally available, the strict choice is `TBD` rather than asserting compliance from convention. Choose `TBD` and add a Conflict Table entry rather than overstating.
- **Honoring workbook title vs. honoring DBM supersession.** Carrying the package under its workbook title preserves traceability; accepting under the DBM-superseded architecture preserves facility coherence. Acceptance criteria must be conditioned on the human ruling, not silently aligned to one source.

## Examples

- Example acceptance line (illustrative; not asserted as compliant):
  - "Interface: Fuel Gas (Utility Piping). Evidence: vendor fuel-gas-train P&ID rev 01 dated YYYY-MM-DD; design pressure 60 psig, start-gas peak 3.6 MMSCFD; matches DBM-Deepcut line 1870. Disposition: PROPOSAL — accept; human ruling pending."
- Example `TBD` line:
  - "Interface: Electrical Power. Evidence: vendor generator rating not yet submitted; architecture (LV per DBM vs. 13.8 kV per workbook title) unresolved. Disposition: TBD; blocked by `CONF-041-06-001`."

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONF-041-06-001 | Workbook package title describes a 13.8 kV / 3 MW standby generator; both DBMs explicitly supersede that concept with an LV standby-generator architecture on the LV MCC with transfer switch. | GATE-07 `PACKAGE_REGISTER.csv` row `PKG-041` (Workbook Packages row 43) | DBM-Comp_and_Liquids `3-25_Comp_and_Liquids_DBM.md` line 505; DBM-Deepcut `4-25_Deepcut_DBM.md` line 175 | Datasheet.Conditions; Specification.Requirements (REQ-041-06-05); Procedure.Prerequisites and Steps | Treat the DBM (LV standby on LV MCC with transfer switch) as the integration-acceptance basis; carry the workbook title for traceability but do not derive 13.8 kV / 3 MW acceptance criteria from it. | TBD |
| CONF-041-06-002 | Acceptance criteria depth requires engine/generator/packaged-enclosure standards whose clause text is not locally accessible. | Specification REQ-041-06-11 (ASSUMPTION) | `_REFERENCES.md` Missing/Deferred section | Specification.Requirements; Procedure.Steps; Datasheet.Conditions | Treat standards as nominally applicable; defer clause-level acceptance criteria until locally accessible. | TBD |
| CONF-041-06-003 | PKG-041 vendor document register (from `DEL-041-05`) is not yet baselined; PKG-041 has no formal vendor document register to review against. | GATE-07 `ARTIFACT_REGISTER.csv` rows for `DEL-041-05` | Specification REQ-041-06-01 | Specification.Requirements; Procedure.Prerequisites | Use vendor submittal index as interim baseline; flag every reviewed document with `register-baseline=TBD`. | TBD |
| CONF-041-06-004 | `_DEPENDENCIES.md` declares no upstream edges, but acceptance is logically dependent on `DEL-041-01`..`DEL-041-05`. | `_DEPENDENCIES.md` (Declared: none) | GATE-07 `SCOPE_LEDGER.csv` row `SOW-0042` (lists sibling deliverables) | Procedure.Prerequisites; Guidance.Considerations | Treat sibling deliverables as required upstream context; explicit edge declaration recommended via `dependency-extract` skill. | TBD |
