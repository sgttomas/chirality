# Guidance — DEL-073-06 EPC Vendor Package Review and Acceptance (PKG-073 Amine Treating Unit)

## Purpose

DEL-073-06 captures the EPC Integrator's review and acceptance evidence for the PKG-073 Amine Treating Unit vendor package. It is the integrator-side counterpart to the vendor-owned engineered equipment package (DEL-073-04) and vendor document turnover package (DEL-073-05). Its purpose is to make the responsibility split (PKG-073 `PACKAGE_REGISTER.csv` row; OBJ-004) auditable at handoff: vendor produces, EPC reviews and accepts for integration into the facility.

This deliverable does not engineer the package and does not approve it on its own authority — final acceptance is a human-authored decision (root governance K-AUTH-1).

## Principles

- **Vendor/EPC split is preserved.** Reviewers do not re-author vendor scope; they document conformance, non-conformance, and dispositions (source: `PACKAGE_REGISTER.csv` row PKG-073 responsibility text; OBJ-004).
- **Acceptance is integration-focused.** Acceptance asks whether the package, as delivered, can be integrated into the facility (interfaces, tie-ins, constructability, commissioning) — not whether it is optimal in isolation.
- **Evidence over assertion.** Each acceptance line is backed by a reviewed vendor document, an inspection record, or a test result. Assertions without traceable evidence are open items.
- **Open items are tracked, not hidden.** Items not closeable at acceptance are dispositioned (deferred, conditional, escalated) per OBJ-010 closure-evidence requirement.
- **Authority hierarchy.** Source materials (when accessible) outrank decomposition narrative and prior draft wording. Where source clause text is unavailable, claims are marked `TBD` rather than fabricated.

## Considerations

- **Source-text accessibility.** Clause-level requirements from `26020-Package_Requirements.docx` (heading 27) are not locally accessible as markdown. The decomposition snapshot (GATE-07) captures package-level summaries but not the full clause text required to derive every acceptance criterion. This deliverable defers detailed criteria to `TBD` where source clauses would be needed.
- **Interface breadth.** PKG-073 carries 13 declared interface types (`INTERFACE_REGISTER.csv`). Acceptance evidence must cover each; absence of per-interface specifications at this gate forces conservative review (presence-check rather than spec-match) until interface specifications are produced.
- **Objective coverage.** Nine objectives (OBJ-001, OBJ-003..OBJ-010) attach to this deliverable via the package-grouping heuristic (`OBJECTIVE_ASSOCIATION_MODE: PACKAGE_HEURISTIC`). These are directional context, not hard requirements — confirm with the human before treating any as a hard acceptance gate.
- **Dependency mode.** `_DEPENDENCIES.md` is in DECLARED mode with no edges declared. Practically, this deliverable consumes DEL-073-01..05 as inputs; that relationship should be declared upstream when dependency hygiene is run.
- **Acceptance authority.** No agent may issue acceptance. The artifacts produced here are evidence packs supporting a human-authored acceptance decision.

## Trade-offs

| Decision | Option A | Option B | Notes |
|---|---|---|---|
| Acceptance granularity | Per-document acceptance (item-by-item) | Package-level acceptance (whole vendor scope) | Item-by-item gives stronger traceability but heavier process; package-level is faster but loses per-item disposition. PROPOSAL: hybrid — per-document review log feeding package-level acceptance checklist. |
| Open-item handling at acceptance | Block acceptance on any open item | Accept with conditions and a closure plan | Hard-block protects facility integration but stalls schedule; conditional acceptance preserves schedule but requires disciplined closure tracking. PROPOSAL: condition-based acceptance with explicit closure owners and dates (ASSUMPTION pending project convention). |
| Test/inspection scope | Witness all factory tests | Witness critical tests only, accept vendor reports for the rest | Witnessing all is expensive; selective witnessing relies on vendor QA credibility. TBD — confirm against project quality plan. |
| Interface acceptance | Acceptance at vendor scope boundary | Acceptance after EPC tie-in installation | This deliverable scopes to vendor-package acceptance (boundary). Post-tie-in commissioning is a different deliverable. |

## Examples

Examples of acceptance-evidence patterns (drawn from the artifact register and objective set; specific text examples deferred to vendor-supplied material):

- **Vendor document review log entry pattern (ASSUMPTION):** `Doc ID | Doc Title | Revision | Reviewer | Review date | Status | Comments | Vendor response | Disposition | Closure date`.
- **Acceptance checklist section pattern (ASSUMPTION):** sections for Documentation Completeness, Physical Package Completeness, Interface Coverage (per `INTERFACE_REGISTER.csv` PKG-073 rows), Test/Inspection Coverage, Open Item Disposition, Objective Trace.
- **Test/inspection evidence pattern:** Factory Acceptance Test reports, hydrostatic test certificates, NDE records, performance test results, materials certifications — actual required set is `TBD` pending source-clause extraction.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted Sections | Proposed Authority (PROPOSAL) | Human Ruling (TBD) |
|---|---|---|---|---|---|---|
| C-073-06-01 | Detailed vendor document list and per-document acceptance criteria are not locally accessible — source is the binary `26020-Package_Requirements.docx` package heading 27. | `_Sources/26020-Package_Requirements.docx` package heading 27 (binary; `location TBD`) | GATE-07 decomposition snapshot (summary level only) | Specification REQ-073-06-02, REQ-073-06-03; Datasheet Anticipated Artifacts; Guidance Examples | Promote source clauses to the authority once extracted; until then decomposition summary stands as the only accessible reference and acceptance criteria remain `TBD` | TBD |
| C-073-06-02 | Specific factory/shop test and inspection requirements (which tests, who witnesses, acceptance thresholds) are not locally accessible. | `_Sources/26020-Package_Requirements.docx` package heading 27 (binary; `location TBD`) and bid document `26020-01-PT-RFQ-27-001_Amine_Treat_Unit_R0.docx` (not in `_Sources/`) | GATE-07 decomposition snapshot (artifact-level only) | Specification REQ-073-06-04; Procedure test/inspection steps; Datasheet Conditions | Promote source clauses and bid Appendix A once accessible | TBD |
| C-073-06-03 | Objective association uses the PACKAGE_HEURISTIC mode (OBJ-001, OBJ-003..OBJ-010 attached at package level, not deliverable level). Treating these as hard acceptance gates is ASSUMPTION. | `OBJECTIVE_REGISTER.csv` (package-grouped) | `_CONTEXT.md` "Supports Objectives" list (deliverable-level echo) | Specification REQ-073-06-09; Guidance Considerations | Use objective list as directional context only; require human confirmation before any objective becomes a hard acceptance gate | TBD |
| C-073-06-04 | `_DEPENDENCIES.md` declares no upstream edges, but this deliverable functionally depends on DEL-073-01..05. | `_DEPENDENCIES.md` (DECLARED; no edges) | `_CONTEXT.md` and `DELIVERABLE_REGISTER.csv` (functional dependency on SOW, Datasheet, CWP, vendor equipment, vendor docs) | Procedure Prerequisites; Specification REQ-073-06-01 | Declare upstream edges to DEL-073-01, DEL-073-02, DEL-073-03, DEL-073-04, DEL-073-05 when dependency-extract is run | TBD |
