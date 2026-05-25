# Guidance: DEL-037-06 — EPC Vendor Package Review and Acceptance

## Purpose

This deliverable is the EPC Integrator's formal acceptance record for the `PKG-037` 5 kV switchgear electrical building vendor package. It exists so that vendor-furnished engineering, documentation, equipment, and turnover materials are demonstrably reviewed against the EPC Scope of Work, Package Datasheet, and Construction Work Package before the package is handed over to operations.

Source: `DELIVERABLE_REGISTER.csv` row 209; `PACKAGE_REGISTER.csv` row 39.

## Principles

- **Acceptance, not re-authorship.** The EPC Integrator reviews, comments, accepts, or rejects vendor outputs. The EPC does not rewrite vendor engineering or vendor documentation. (Source: `PACKAGE_REGISTER.csv` row 39 ownership split.)
- **Traceability to EPC anchors.** Each acceptance item traces to a clause in `DEL-037-01` (SOW), `DEL-037-02` (Package Datasheet), or `DEL-037-03` (Construction Work Package). Acceptance items lacking an EPC anchor are flagged as scope drift.
- **Interface readiness is first-class.** Each interface type listed in `PACKAGE_REGISTER.csv` row 39 receives an acceptance row, because facility integration is the EPC Integrator's primary risk surface for this package.
- **No silent TBDs.** Missing vendor evidence remains `TBD`/`Pending` until evidence arrives; it is never quietly cleared to "Accepted."

## Considerations

- **Building-electrical applicability.** The DBM "Electrical Buildings" provisions (n+1 HVAC, bottom-entry/elevated building, prefab modular construction) apply when EPC SOW/Datasheet incorporate them; verify that the SOW/Datasheet explicitly invokes them before scoring the vendor against them. (Source: DBM-Deepcut "Electrical Buildings".)
- **5 kV voltage class.** The package title is "5kV SWITCHGEAR." The DBM enumerates 13.8 kV, 6.9 kV, 4.16 kV, and 600 V building variants but does not contain a 5 kV building narrative. Accept 5 kV switchgear against vendor-cited standards and the EPC Datasheet rather than DBM building-class clauses. (Source: DBM "Electrical Buildings".)
- **Grounding compatibility.** The DBM specifies driven-pile grounding interconnected by a main #2/0 conductor, with two-point connection for major equipment; building/equipment acceptance should confirm the vendor solution is compatible. (Source: DBM "Grounding and Bonding".)
- **Cable conventions.** Where vendor scope includes incoming/outgoing cable conventions, confirm alignment with DBM cable types (TECK 90, ACWU, ACIC). (Source: DBM "Cable, Wire, and Raceways".)
- **Dependency view.** `_DEPENDENCIES.md` lists no declared upstream/downstream edges; downstream construction and operations consumers should be added when known.

## Trade-offs

- **Strict checklist vs. risk-based sampling.** A line-by-line checklist gives maximum traceability but is laborious. Risk-based sampling is faster but requires explicit rationale for any unsampled requirement. Choose strict checklist for safety-critical and interface-bearing items; sampling is acceptable only for low-risk repeating elements with explicit rationale captured.
- **Acceptance staging.** Stage-gated acceptance (per submittal) reduces end-of-project risk but consumes EPC review bandwidth earlier. Single-package end-of-project acceptance concentrates risk and is discouraged for complex electrical buildings.
- **Vendor comment closure rigor.** Tracking every comment to written closure is heavier but defensible; closing comments verbally accelerates schedule but weakens the audit trail. Default to written closure.

## Examples

No worked examples are available in accessible source materials. `TBD` — examples should be added when historical comparable acceptance packages become available.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONF-037-06-001 | Package title denotes "5 kV SWITCHGEAR," but the DBM "Electrical Buildings" section enumerates 13.8 kV, 6.9 kV, 4.16 kV, and 600 V buildings only — no 5 kV building basis is provided in accessible sources. | `PACKAGE_REGISTER.csv` row 39 (title) | DBM-Deepcut/4-25_Deepcut_DBM.md "Electrical Buildings" | Datasheet Conditions; Specification Standards | Treat package title as identity; assess vendor 5 kV equipment against vendor-cited 5 kV class standards and the EPC Datasheet rather than against DBM building-class clauses. | TBD |
| CONF-037-06-002 | `_DEPENDENCIES.md` declares no upstream dependencies, yet acceptance is logically downstream of `DEL-037-01` (SOW), `DEL-037-02` (Datasheet), `DEL-037-03` (CWP), `DEL-037-04` (Vendor Equipment), `DEL-037-05` (Vendor Document Turnover). | `_DEPENDENCIES.md` Declared Upstream | `DELIVERABLE_REGISTER.csv` row 209 narrative | Specification R-2/R-3/R-4; Procedure Prerequisites | Add these five deliverables as declared upstream when `Dependencies.csv` is next generated. | TBD |
| CONF-037-06-003 | No deliverable-specific source slices were copied during PREPARATION (`_REFERENCES.md` Missing/Deferred). Acceptance criteria depend on slices not yet placed locally (e.g., 5 kV switchgear standards). | `_REFERENCES.md` Missing/Deferred | Specification Standards row "5 kV class equipment standards" | Specification Standards; many R-9 verifications | Resolve and copy package-specific source slices before formal acceptance. | TBD |
