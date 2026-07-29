# HZN-GOV-01 — Governance Concordance Report

## Basis and method

- **Frozen basis:** `85ea0628fa4e57dd6aae53b06139b2b8734a9612`
- **Method:** read-only `git show`, `git grep`, `git ls-tree`, and history inspection.
- **Writes/delegation/network:** none.
- **Successor search:** no D-8 successor proposal, candidate, decision, or effective instrument is present or reachable from the frozen basis. The decision series ends at D-GOV-28; exact-phrase searches find only the current D-8 and its derived/restated surfaces.

## Governing inventory

| Surface | Requirement |
|---|---|
| `85ea0628…:docs/PRD_ROOT.md:454` | D-8: CHANGE-managed, human-gated PRs, never self-merge. |
| `85ea0628…:docs/CONTRACT.md:71-73` | Only humans author binding approvals; approval binds to a specific Git SHA and is voided by content change. |
| `85ea0628…:docs/CONTRACT.md:111-115` | Main merge requires branch HEAD to equal the approved SHA. |
| `85ea0628…:agents/AGENT_CHANGE.md:40-47,59-76` | CHANGE may execute merges, but only after human approval of the exact merge action; merge is non-routine. |
| `85ea0628…:agents/AGENT_CHANGE.md:87,94-101` | Immediately before merge, CHANGE must verify checks and that source HEAD still equals the approved SHA. |
| `85ea0628…:execution/_Coordination/LOOP_INIT.md:55-65,115-129` | Human acts are not inferred; commits/PRs do not create semantic acceptance; Root closeout never self-merges; a run steer cannot override ratified governance. |
| `85ea0628…:execution/PKG-04_Developmental_Machinery_and_Change_Control/1_Working/DEL-04-06_Change_Management_and_Human_Gated_Closeout/ScopeOfWork.md:62-82` | The accepted operationalization requires human-gated closeout and defines self-merge evidence by distinguishing the merge actor from the authoring actor. |
| `85ea0628…:docs/governance_harness/_DECISIONS/D-GOV-26_owner_gated_closeout.md:20-25` | Owner adoption of recommendations and delegation of exact prose is a valid vehicle, but this precedent bound the result at a later human-gated merge. |
| `85ea0628…:docs/governance_harness/_DECISIONS/D-GOV-25_root_decomposition_acceptance.md:25-34` | Approval vehicles may vary, provided the exact vehicle and scope are stated and SHA binding is preserved. |
| `85ea0628…:docs/PRD_ROOT.md:459,477,521-527,793-840` | PRD amendment requires a superseding SHA-bound instrument and M2 closeout; semantic approval, publication, and effective identity remain distinct. |
| `85ea0628…:execution/_Coordination/CHIRALITY_PROGRAM_ARCH_REMEDIATION_CLOSEOUT_2026-07-28.md:18-25` | The July 28 umbrella direction is transcribed and treated as substantive owner approval of recommendations. It does not itself demonstrate pre-merge approval of each exact source HEAD. |

## Findings

### HZN-GOV-001 — `NECESSARY_BEFORE_NEXT_WORK`

No successor exists. Current D-8, LOOP_INIT, SOW-042, and DEL-04-06 remain in force. A future Root closeout cannot rely on a changed self-merge rule until an exact successor is adopted and propagated.

Named affected claim: “a Root PR authored and merged by the same actor complies with current D-8.”

### HZN-GOV-002 — `NECESSARY_BEFORE_NEXT_WORK`

The candidate must distinguish two materially different arrangements:

1. **Delegated merge execution:** a distinct CHANGE actor merges an author’s branch after exact human approval. Existing CHANGE doctrine already permits this, and DEL-04-06’s present operational definition can treat it as not self-merge.
2. **Same-actor author-and-merge:** the actor that authored the tranche also executes its merge. This is a substantive exception to current D-8 and DEL-04-06, not merely clarification that the owner may delegate execution.

The future proposal must state which arrangement it intends and define `authoring actor`, `merge executor`, and `self-merge`.

### HZN-GOV-003 — `NECESSARY_BEFORE_NEXT_WORK`

Valid owner delegation does not remove K-AUTH-2 or K-MERGE-1. A standing or umbrella direction can authorize a class of work, but it does not by itself prove that each eventual branch HEAD was the specific approved SHA.

For every delegated merge, the procedure must retain:

- semantic approval and its subject;
- the exact approved source HEAD;
- explicit merge authorization, target, and strategy;
- proof that source HEAD remained unchanged at execution;
- the resulting merge/effective SHA.

One owner message may perform several of these acts, but the record must not collapse their identities.

### HZN-GOV-004 — `NECESSARY_BEFORE_NEXT_WORK`

A successor must not claim retroactive cure. The July 28 umbrella direction is strong evidence of owner intent and substantive delegation, but later prose cannot make an earlier procedure compliant with a rule then in force.

The candidate must choose and state one treatment for an exact closed set of July 28 acts:

- record them as disclosed procedural exceptions while preserving their substantive rulings; or
- separately ratify the resulting current state at an exact SHA.

Either treatment is prospective evidence about current reliance. Neither rewrites the historical procedure.

### HZN-GOV-005 — `NECESSARY_BEFORE_NEXT_WORK`

A D-8 change cannot be completed by editing LOOP_INIT alone. D-8 is an adopted Root product requirement and is decomposed as SOW-042/DEL-04-06. Required ordering is:

1. exact Root PRD successor candidate and owner adoption;
2. human-merged M2 application under the still-current D-8;
3. Root SCOPE_CHANGE for SOW-042/DEL-04-06 and their evidence criteria;
4. concordant LOOP_INIT and other approved procedural propagation.

The successor may not consume its own not-yet-effective merge exception.

### HZN-GOV-006 — `OUTSIDE_PROGRAM_OBJECTIVE`

Project-local App, PEC, and Piping merge rules are not automatically amended by a Root D-8 successor. If shared `AGENT_CHANGE.md` is changed, the candidate must explicitly state the cross-project effect and route notices; otherwise the change should remain Root-specific.

### HZN-GOV-007 — `UNKNOWN`

The exact future D-8 candidate, its intended scope and expiry, and the closed inventory of July 28 acts are `PENDING_INPUT / UNKNOWN`. No judgment on their exact adequacy is possible yet.

## Candidate feedback checklist

The future candidate should contain:

- an exact current/new D-8 diff and provenance label;
- a definition of self-merge based on actor identity;
- an explicit choice between distinct CHANGE execution and same-actor execution;
- Root-only versus shared scope;
- per-PR, session-bounded, tranche-class, or standing duration and expiry;
- exact exclusions: no semantic auto-approval by an agent, no content mutation after approval, no force/rebase/conflict resolution, and no lifecycle authority;
- a four-identity record: approved subject SHA, merge authorization, source HEAD verified at execution, effective merge SHA;
- a closed July 28 act inventory with PR/source/merge identities and one non-retroactive disposition per act;
- PRD → decomposition → ScopeOfWork → LOOP_INIT propagation;
- a human merge for the successor’s own adoption/application PR.

Required deterministic checks:

- candidate manifest and exact-postimage hashes;
- source-HEAD-equals-approved-SHA immediately before merge;
- CI/check verdict present and green;
- branch/target/strategy equal the authorization;
- no head movement or content mutation after approval;
- expiry and scope still active at execution;
- exact current-surface scan for stale `never self-merge` requirements after propagation, excluding labeled historical records;
- SOW-042/DEL-04-06 traceability and stable-ID preservation;
- explicit inability to infer GitHub merge actor solely from Git commit metadata; actor evidence must come from a recorded PR/action source.

## Limitations and rerun

This audit does not determine who executed every July 28 merge, exhaustively inventory those acts, or assess a candidate that does not yet exist. No global product block is assigned.

**Rerun requirement:** re-execute this lane against the exact committed D-8 candidate before adoption, then recheck the exact final bytes and resulting SHAs after landing.
