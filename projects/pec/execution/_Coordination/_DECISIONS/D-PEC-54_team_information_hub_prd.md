# D-PEC-54 — RULED: author the team information-hub PRD

**Status:** RULED 2026-07-09 — owner-directed authoring; PRD adoption remains open
**Decision ID:** D-PEC-54
**Structure precedent:** `D-PEC-53_live_agent_activity_stream.md` (direct owner
instruction, ruled behavior, exact fence, verification/rollback, and bounded ruling)

## Owner direction

Owner direction of record (Ryan Tufts, in-session, 2026-07-09) includes:

> “its potential is to be the hub for critical information flow to inform
> project leadership, helping them maintain a sufficiently relevant and detailed
> project state that others can rely upon without requiring NxN coordination
> events.”

> “Because those decisions have consequences, it's about triaging and assigning
> change to the right place, and that place should be a form of documentation
> that others rely upon (like a scope of work, or the DBM, etc.).”

> “I ask the same thing from each discipline each week: has anything changed that
> would impact on other disciplines? Or is there a risk of change to the budget,
> scope or schedule? Do you have any needs for information, resources, decisions,
> approval, or clarification? Have you or will you soon be issuing internal or
> external deliverables, or requesting a squad check? Then I ask for current
> development state (in-progress, complete, on hold, etc.) and a percent complete
> based on rules-of-credit.”

> “With this in mind, write the PRD for `PEC` to actually become such an
> application, useable by a team.”

The owner also clarified that the gap is where decisions occur, that this
foreground belongs on the Planning page, and that the workflow must not be
over-designed from assumptions.

## Ruled authoring behavior

1. Replace the old task-management-centred PRD with a candidate team product
   definition centred on the recurring discipline information contract.
2. Make the maintained shared project state—not report generation—the product's
   core value.
3. Make decision gaps, explicit consequences, and placement of consequential
   change into relied-upon documentation the Planning foreground.
4. Preserve factual-or-absent, source/coverage visibility, human authority, and
   bounded-agent principles from the Chirality basis.
5. Define team roles, multi-user collaboration, permissions, information model,
   functional requirements, UX principles, non-functional requirements, metrics,
   release sequence, acceptance scenarios, risks, and open product decisions.
6. Label the PRD a candidate. Authoring does not adopt the exact requirement set,
   authorize implementation, or claim that the current prototype conforms.
7. Label the current SPEC, traceability, and status account as historical
   prototype-baseline documentation until an adopted rebaseline replaces them.
8. Replace the completed sponsor-demo standing plan with a product-reorientation
   standing plan whose next gate is owner review/adoption of the candidate PRD.

## Exact fence

- `projects/pec/docs/PRD.md`
- introductory basis/status notes only in:
  - `projects/pec/docs/SPEC.md`
  - `projects/pec/docs/TRACEABILITY.md`
  - `projects/pec/docs/STATUS.md`
- `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-54_team_information_hub_prd.md`
- `projects/pec/execution/_Coordination/_DECISIONS/_REGISTER.md`
- `_DomainEngines/pec/WORKPLAN_2026-07-09_pec_team_information_hub.md`
- `_DomainEngines/pec/LOOP_RECEIPTS.md`

No runtime source, dependency, database, demo input, report, or external system
change is authorized by this row.

## Verification and rollback

- Verify the PRD directly contains the five owner questions and the
  decision-consequence-to-document distinction.
- Check relative links and the historical v0.4 Git object.
- Review requirement-ID uniqueness and Markdown structure.
- Run self-check, coordination check, and `git diff --check`.
- Roll back by reverting the documentation/coordination commit; no data rollback
  exists.

## Human ruling

**RULED for authoring only:** the quoted direct owner instruction authorizes this
candidate PRD and the documentation/standing-plan alignment inside the fence above.
Adoption of PRD v1.0 and runtime implementation remain owner acts.
