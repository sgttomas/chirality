# Guidance — DEL-044-03 Construction Work Package

## Purpose

This guidance explains why the Construction Work Package exists for PKG-044 and how the EPC Integrator should approach its preparation. The Construction Work Package is one of four mandatory Gate 5 EPC anchor deliverables for the package (PACKAGE_REGISTER.csv row 46; DELIVERABLE_REGISTER.csv row 246). Its purpose is to translate the approved package scope (DEL-044-01) and package datasheet (DEL-044-02) into an executable construction plan that yields a built, inspected, and turned-over instrumentation package integrated with adjacent facility systems.

## Principles

1. **Source authority for design values.** Construction methodology that depends on equipment counts, dimensions, weights, or design conditions must cite Workbook Packages row 46 or the relevant DBM section. Where the source is not yet locally accessible in the deliverable folder, mark `TBD (location TBD)`. (Authority: PACKAGE_REGISTER.csv row 46.)
2. **Plug-n-play package philosophy.** Instrumentation field supports, power, and communications are included in each package scope as appropriate under the plug-n-play package philosophy (Gate 6 disposition). The construction plan must treat these as in-scope, not as carve-outs to other packages. (Source: INTERFACE_REGISTER.csv rows 302-306.)
3. **Interface-first workface planning.** All five declared package interface types (Process Piping, Utility Piping, Electrical Power, I&C / Control Cabling, Communications / Network) must be addressed in the installation and tie-in workface plan. Missing interface treatment is a construction risk and should be surfaced as an open item, not silently omitted. (Source: PACKAGE_REGISTER.csv row 46; INTERFACE_REGISTER.csv rows 302-306.)
4. **Conservative responsibility assignment.** Source materials state that EPC Integrator or discipline subcontractor responsibility is source-dependent; no separate vendor-package ownership model is inferred. Construction responsibility tables should mirror this stance and avoid asserting ownership that the workbook does not support. (Source: PACKAGE_REGISTER.csv row 46.)
5. **Traceability to SOW and objectives.** Each construction section should be traceable to SOW-0045 and to the supported objectives (OBJ-002, OBJ-003, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-010). (Source: DELIVERABLE_REGISTER.csv row 246; SCOPE_LEDGER.csv row 46.)
6. **Handoff evidence for turnover.** OBJ-010 explicitly identifies the Construction Work Package as evidence supporting operability, maintainability, isolation, winterization, vendor-documentation, commissioning, and turnover. The turnover checklist should be designed to satisfy this evidence role. (Source: OBJECTIVE_REGISTER.csv row for OBJ-010.)

## Considerations

- **Source-limited detail.** `_REFERENCES.md` records that no deliverable-specific source slices were copied during PREPARATION. Detailed construction methodology (lift plans, sequencing, manhour estimates) will require source slices to be brought into the folder before they can be drafted source-grounded.
- **Discipline scoping caveat.** PKG-044 is specifically "Instrumentation (outside of Mechanical Packages only)" — installations inside mechanical packages remain with those packages. The workface plan must clearly delineate this boundary to avoid duplication or omission.
- **OBJ-008 inclusion.** This deliverable is one of the few in PKG-044 that supports OBJ-008 (civil/structural/site/construction-support scope). Field supports, foundations, and access platforms for instrumentation should be addressed even when they cross civil/structural discipline boundaries.
- **Vendor document interaction.** The package datasheet (DEL-044-02) holds the vendor-handoff evidence and interface requirements matrix. The construction work package should consume that evidence rather than re-derive it.

## Trade-offs

- **Detail vs. source fidelity.** Prefer `TBD (location TBD)` over fabricated specificity. Construction work packages traditionally include detailed scopes, but for this Gate 5 anchor deliverable the priority is grounded traceability over apparent completeness.
- **Interface coverage vs. scope creep.** Address all five declared interface types, but resist expanding into scope that is properly owned by adjacent packages (e.g., upstream Electrical bulk power scope, upstream Process Piping prime contractor scope).
- **Construction sequencing vs. tie-in readiness.** Workface planning must balance discipline-specific construction productivity with availability of tie-in points; do not assume tie-in readiness that the project schedule has not confirmed (mark schedule dependencies as `TBD` until project schedule is referenced).

## Examples

Examples drawn from source: none directly available. The decomposition registers describe the *kind* of construction-package content (workface planning, tie-in, inspection, turnover) but do not contain example construction-package text. Concrete examples are TBD pending source slice extraction.

## Conflict Table (for human ruling)

No cross-document or source-to-decomposition conflicts identified in this initial draft. Table left present for downstream passes.

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| (none) | — | — | — | — | — | — |
