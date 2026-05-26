# Guidance — DEL-044-04 EPC / Instrumentation Discipline Production Package

> Pass 1/2 draft. Guidance is intentionally directional rather than prescriptive because the deliverable is source-limited (`_CONTEXT.md` Notes; DELIVERABLE_REGISTER DEL-044-04 Notes). Where rationale cannot be drawn from an accessible source it is marked TBD or ASSUMPTION.

## Purpose

This deliverable carries the **discipline-side production work** that does not naturally land in the three EPC-anchor deliverables (Scope of Work, Package Datasheet, Construction Work Package) for `PKG-044`. Its existence is required by the Gate 5 deliverable model so that the non-vendor instrumentation scope has an explicit owner and a place where source-limited items can be tracked toward Gate 5 disposition (DELIVERABLE_REGISTER DEL-044-04 Notes).

## Principles

1. **Conservative carry.** The deliverable's existence at this gate is deliberately conservative; do not invent engineering requirements where source slices are not yet accessible (DELIVERABLE_REGISTER DEL-044-04 Notes). ASSUMPTION: this principle applies generally to PKG-044..045 discipline production units, which share identical decomposition language.
2. **EPC-anchor primacy.** The discipline production unit consumes the package's Scope of Work and Package Datasheet rather than re-authoring them. The Construction Work Package owns installation/turnover. ASSUMPTION: derived from the four-deliverable structure observed for PKG-043..045 in DELIVERABLE_REGISTER.
3. **Plug-n-play interface posture.** Instrumentation field supports, power, and communications are included in each package scope as appropriate under the plug-n-play package philosophy (Gate 6 disposition language in ARTIFACT_REGISTER ART-05F89F3B5C / ART-7114CBB6AD / ART-C0C9C4ADC7).
4. **Source-limited transparency.** Items without an accessible source slice must remain TBD with a closure path identified, rather than being silently inferred (`_CONTEXT.md` Notes).

## Considerations

- **Responsibility ambiguity.** Ownership (EPC Integrator vs. discipline subcontractor) is source-dependent (PACKAGE_REGISTER PKG-044 ResponsibilityNote). Until ruled, the discipline production unit should be authored in a way that does not assume either role's internal procedures.
- **Discipline boundary with mechanical packages.** Package name explicitly excludes instrumentation embedded in mechanical packages; do not import requirements from mechanical-package vendor scopes into this deliverable.
- **Objective lineage is heuristic.** Objective associations `OBJ-002; OBJ-003; OBJ-005; OBJ-006; OBJ-007; OBJ-010` are by package-grouping heuristic (ASSUMPTION) per the `four-documents` skill default and `_CONTEXT.md`.
- **Interface coverage.** Address each of the five applicable interface types from PACKAGE_REGISTER PKG-044 (Process Piping; Utility Piping; Electrical Power; I&C/Control Cabling; Communications/Network) at the production-unit level, even when sub-scope is TBD.

## Trade-offs

| Trade-off | Conservative posture | Aggressive posture | Recommendation |
|---|---|---|---|
| Issue TBD-heavy production basis now vs. defer until source access | Issue with TBD markers and a closure register | Wait for full source access | Issue now (the deliverable explicitly anticipates a "source-limited requirements closure record") — ASSUMPTION based on decomposition Notes |
| Adopt a default ownership model | Author in role-neutral terms | Pick EPC Integrator or subcontractor and pre-load procedures | Stay role-neutral until Gate 5 disposition |
| Inherit project instrumentation standards by default | Mark as ASSUMPTION; do not derive clauses | Cite specific clauses | Mark as ASSUMPTION; defer clause-level derivation (Step 2 of `four-documents`) |

## Examples

- TBD; no source-supported example available within the locally accessible reference set.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| CONF-044-04-01 | Responsibility assignment | `_CONTEXT.md` ResponsibleParty: "TBD; EPC Integrator or discipline subcontractor as assigned" | PACKAGE_REGISTER PKG-044 ResponsibilityNote: source-dependent, no vendor-package ownership inferred | Datasheet Identification; Specification R-044-04-09 | Carry as TBD until Gate 5 disposition rules | TBD |
| CONF-044-04-02 | Standards applicability | `_REFERENCES.md` Missing/Deferred References (no source slices) | Specification "Standards" row (project instrumentation standards likely applicable) | Specification Standards; Verification | Mark all standards as ASSUMPTION until source access established | TBD |
