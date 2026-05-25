# Guidance: DEL-032-01_scope-of-work — Scope of Work

Directional guidance for authors and reviewers of the EPC Integrator Scope of Work covering PKG-032 Cathodic Protection Design and Installation.

## Purpose

This deliverable exists to make the EPC Integrator's accountability for PKG-032 explicit at the facility level. The cathodic protection system is unusual within the package set: the DBM places CP engineering and supply outside facility design scope, while still requiring the facility to provide interface support. The SOW must therefore clearly distinguish the Package Vendor's engineering and supply scope from the EPC Integrator's integration scope, and from the owner-driven CP basis itself.

## Principles

- **Identity first.** Anchor the SOW to the package tag `26020-03-30-023`, WBS 03, and Electrical discipline before describing scope content (PACKAGE_REGISTER row PKG-032).
- **Source over convention.** Defer to DBM source language for what is excluded from facility design and what facility design must support (DBM-Deepcut SEC-12 §Cathodic Protection, line 3073-3075). Do not invent CP engineering content from generic convention.
- **Boundary symmetry.** Every interface listed (Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network) should have a stated facility-side responsibility AND a stated package-side responsibility, or be marked TBD.
- **Owner-coordination is mandatory.** Per DBM Assumptions/TBDs table (line 3092), owner interface requirements remain to be coordinated; the SOW must call this out explicitly rather than absorbing the owner's role silently.

## Considerations

- The two DBM source documents are partially in tension on whether facility electrical scope includes "cathodic protection." DBM-Comp_and_Liquids lists CP within electrical-design support (line 718, 770); DBM-Deepcut excludes CP engineering and supply from facility design (line 3075). Treat the Deepcut exclusion as the more specific, governing statement for the CP package itself, while the Comp_and_Liquids statements describe facility-side support obligations.
- The Anticipated Artifacts in `_CONTEXT.md` include a "tagged equipment and package identity list." The accessible sources do not enumerate the CP package equipment list. The SOW should hold this open as TBD pending vendor data, rather than fabricating tag identifiers.
- Objectives `OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-009, OBJ-010` are associated to this deliverable via the package-grouping heuristic and should be treated as directionally relevant context, not as derived requirements, until human ruling.

## Trade-offs

- **Breadth vs. precision.** A broad SOW that paraphrases DBM material risks restating obligations the facility design explicitly excludes. A narrow SOW risks losing the integration narrative the EPC Integrator owns. Prefer narrow precision plus explicit pointers to the owner CP basis.
- **Tagged equipment now vs. later.** Filling tagged equipment with placeholders inflates apparent maturity; keeping them TBD preserves epistemic honesty and aligns with the source state.

## Examples

- TBD: no example SOW excerpts available within the accessible source set.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted Sections | Proposed Authority (PROPOSAL) | Human Ruling |
|---|---|---|---|---|---|---|
| CFL-032-01-001 | DBM-Comp_and_Liquids lists "cathodic protection" within electrical-design support scope; DBM-Deepcut explicitly excludes CP engineering and supply from facility design. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 718, 770 | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 3075, 3092 | Specification §Scope, §Requirements R-SOW-032-05; Guidance §Considerations | Treat the DBM-Deepcut exclusion as governing for CP package engineering/supply; treat DBM-Comp_and_Liquids language as describing facility-side interface support obligations only. | TBD |
| CFL-032-01-002 | Objective associations to `DEL-032-01_scope-of-work` are derived from the package-grouping heuristic rather than from an explicit deliverable-ID-level mapping. | `_CONTEXT.md` Supports Objectives | DELIVERABLE_REGISTER row `DEL-032-01_scope-of-work` (heuristic basis) | Datasheet §Identification; Specification §Requirements R-SOW-032-09 | Carry the objective list as ASSUMPTION until objective-deliverable map is consulted directly or human confirms. | TBD |
