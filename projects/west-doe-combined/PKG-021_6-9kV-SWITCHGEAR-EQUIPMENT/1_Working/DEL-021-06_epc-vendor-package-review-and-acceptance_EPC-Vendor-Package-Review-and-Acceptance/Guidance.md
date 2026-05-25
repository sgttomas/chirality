# Guidance — DEL-021-06 EPC Vendor Package Review and Acceptance

## Purpose

This deliverable exists so the EPC Integrator can demonstrate, with evidence, that the vendor-supplied 6.9 kV switchgear package (PKG-021) is fit for integration into the West Doe facility against the EPC Scope of Work (`DEL-021-01`), the EPC Package Datasheet (`DEL-021-02`), and the EPC Construction Work Package (`DEL-021-03`). It is the integration-acceptance and handoff-readiness boundary between the Package Vendor's owned scope and the EPC Integrator's owned scope, as defined in GATE-07 `PACKAGE_REGISTER.csv` row `PKG-021`.

## Principles

- **Acceptance is a human act.** Agents may organize, draft, and propose dispositions; only humans may issue binding acceptance or approval-for-reliance (`K-AUTH-1`).
- **Acceptance is evidence-bound.** Every accepted line in the review log or checklist must cite the underlying vendor document or test record. Where evidence is missing, the line is `TBD`, not an asserted pass (`K-PROV-1`).
- **The EPC artifacts are the acceptance ruler.** The Scope of Work, Package Datasheet, and Construction Work Package set what the vendor package must satisfy. The vendor's own design basis is acceptance input, not acceptance criterion.
- **Interfaces drive integration acceptance.** Each applicable PKG-021 interface type from GATE-07 `INTERFACE_REGISTER.csv` (Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports) must be explicitly covered.
- **Source-grounded conservatism.** When source material is not locally accessible (for example, the workbook DOCX or specific standards), record `TBD` rather than infer detailed acceptance criteria.

## Considerations

- **Responsibility split.** Per `PACKAGE_REGISTER.csv` row `PKG-021`, the Package Vendor owns package engineering, design, vendor documentation, and the physical equipment package; the EPC Integrator owns facility integration. Acceptance commentary on vendor-internal design should be limited to integration consequences, not redesign demands.
- **Upstream maturity.** Acceptance is meaningful only when upstream EPC deliverables (`DEL-021-01`, `-02`, `-03`) are stable enough to serve as a ruler. The PREPARATION dependency view records `DECLARED` mode with no edges yet; if acceptance is started before upstream maturity is declared, surface the gap rather than asserting acceptance.
- **Facility electrical context.** DBM-Deepcut establishes the medium-voltage system as 6.9 kV, 3-phase, 3-wire, 60 Hz, low-resistance grounded with 100 A, 10 s neutral grounding (lines 2935, 2985) and modular electrical buildings as the housing envelope (line 2973). Reviewers should anchor electrical-integration acceptance to these facts.
- **Documentation gap upstream.** `ART-FA39AD509D` (`DEL-021-05`) is recorded as a `TBD vendor document register`; until that register stabilizes, the vendor document review log here will inherit `TBD` items.

## Trade-offs

- **Breadth vs. depth in the review log.** A broad pass-by-document review is cheap but weak evidence; a clause-by-clause review is expensive but auditable. Prefer clause-by-clause review for safety-relevant and interface-relevant clauses; document-level review elsewhere.
- **Early acceptance vs. waiting for full vendor turnover.** Provisional acceptance with a punch list accelerates construction but creates downstream rework risk if interfaces shift. Provisional acceptance should be explicit and time-bounded, not implicit.
- **Strict source grounding vs. operational pragmatism.** When acceptance criteria require standards that are not locally available, the strict choice is `TBD` rather than asserting compliance from convention. Choose `TBD` and add a Conflict Table entry rather than overstating.

## Examples

- Example acceptance line (illustrative; not asserted as compliant):
  - "Interface: Electrical Power. Evidence: vendor certified single-line diagram rev 02 dated YYYY-MM-DD; matches EPC Package Datasheet interface fact `ART-AF731BD7FC`. Disposition: PROPOSAL — accept; human ruling pending."
- Example `TBD` line:
  - "Interface: Grounding / Bonding. Evidence: vendor grounding scheme not yet submitted. Disposition: TBD; required for closeout. Reference: DBM-Deepcut line 2985."

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONF-021-06-001 | Acceptance criteria depth requires standards (e.g., IEEE C37, CSA, IEC) whose clause text is not locally accessible. | Specification REQ-021-06-10 (ASSUMPTION) | `_REFERENCES.md` Missing/Deferred section | Specification.Requirements; Procedure.Steps; Datasheet.Conditions | Treat standards as nominally applicable; defer clause-level acceptance criteria until locally accessible. | TBD |
| CONF-021-06-002 | `ART-FA39AD509D` (DEL-021-05) is `TBD vendor document register`; PKG-021 has no formal vendor document register to review against. | GATE-07 `ARTIFACT_REGISTER.csv` row `ART-FA39AD509D` | Specification REQ-021-06-01 | Specification.Requirements; Procedure.Prerequisites | Use vendor submittal index as interim baseline; flag every reviewed document with `register-baseline=TBD`. | TBD |
| CONF-021-06-003 | `_DEPENDENCIES.md` declares no upstream edges, but acceptance is logically dependent on `DEL-021-01`..`DEL-021-05`. | `_DEPENDENCIES.md` (Declared: none) | GATE-07 `SCOPE_LEDGER.csv` row `SOW-0022` (lists sibling deliverables) | Procedure.Prerequisites; Guidance.Considerations | Treat sibling deliverables as required upstream context; explicit edge declaration recommended via `dependency-extract` skill. | TBD |
