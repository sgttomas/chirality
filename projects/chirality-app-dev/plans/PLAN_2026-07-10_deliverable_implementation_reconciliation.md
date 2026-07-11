# Deliverable–Implementation Reconciliation Plan

**Date:** 2026-07-10
**Project:** Chirality App Dev
**Status:** PROPOSED — non-governing until selected by the human owner
**Prepared for:** a future autonomous reconciliation loop after the current remedial development session reaches a stable handoff
**Write boundary:** `projects/chirality-app-dev/**` only

## 1. Purpose

Re-establish the current deliverable corpus as a reliable statement of:

1. accepted scope;
2. implemented behavior;
3. verification evidence;
4. unresolved work; and
5. lifecycle state.

The program reconciles the 53 deliverables currently represented under
`execution/PKG-00` through `execution/PKG-10` against the live application,
tests, current authority documents, and recorded human decisions. The count and
status distribution are an observed planning baseline, not an invariant; the
execution loop must re-enumerate them from the live tree.

This is not an issuance program and not a pretext for expanding product scope.
Implementation is evidence of current behavior, not automatic proof of accepted
scope. Existing inspection assessments are evidence records, not current truth.

Agent instruction files and the workflows they encode are deliberately outside
this program's change scope. They require a separate, owner-intensive effort to
identify workflows that must be preserved or ported before any simplification or
consolidation is attempted. This program may read those surfaces as frozen
context where a product deliverable packages, loads, routes, or displays them;
it may not redesign them or authorize changes to them.

## 2. Why this pass is needed

The prior inspection program produced 53 deliverable assessments and moved the
corpus into `CHECKING`. Subsequent implementation and document corrections mean
that some assessments now describe an older specification or implementation
state. In the pilot sample, `DEL-02-01` had a current specification and live
implementation aligned to the loop-first shell, while its inspection assessment
still reported parts of that same pivot as specification drift.

The resulting problem is broader than “specification versus code.” At least six
surfaces can disagree:

- current normative scope;
- deliverable `Specification.md` and related four-document content;
- live implementation;
- tests and recorded review evidence;
- `_STATUS.md` lifecycle state; and
- later human rulings or accepted product pivots.

## 3. Governing boundaries

1. **No automatic scope adoption.** Undocumented implementation is classified;
   it is not silently incorporated into a deliverable.
2. **No implementation work in discovery.** The inventory and concordance phases
   are read-only except for reconciliation artifacts under the reconciliation
   run root.
3. **No lifecycle transitions.** `CHECKING`, `ISSUED`, approval SHAs, and human
   acceptance remain human-owned. This program may recommend a lifecycle action
   but must not apply one without separate authority.
4. **No silent conflict resolution.** Conflicting decisions, specifications, or
   acceptance criteria enter the human decision queue.
5. **No historical-plan authority.** `plans/` and archived material may explain
   provenance but do not establish current scope unless a live authority surface
   explicitly incorporates them.
6. **No cross-project edits.** Root governance and all other project workspaces
   are outside the write scope.
7. **No self-approval.** Agents may report and propose; they may not represent a
   reconciliation disposition as a human ruling.
8. **Separate agent-workflow program.** Do not modify root or project-local
   `AGENTS.md`, `agents/AGENT_*.md`, agent matrices, agent authority contracts,
   or skill contracts as part of this plan. Do not recommend persona
   consolidation or workflow removal from repository shape alone. A finding
   whose resolution requires an agent-instruction or agent-workflow change is
   routed unchanged to `AGENT_WORKFLOW_HANDOFF.md` for later owner-led analysis.
   Product runtime behavior that loads, packages, invokes, or presents agents
   remains in scope, provided the repair does not alter the underlying workflow
   contract.

## 4. Start gate and baseline

Do not begin the full sweep until the human owner identifies the remedial session
as stable enough to inspect. At run start:

1. resolve `REPO_ROOT` and `WORKING_ROOT` from the active checkout;
2. record a source-state identifier for the reviewed tree;
3. enumerate live packages and deliverables directly from `execution/`;
4. record the lifecycle distribution without changing it;
5. identify files actively changing in another session and defer their affected
   claims rather than racing them; and
6. create an immutable run folder:
   `execution/_Reconciliation/DeliverableConcordance/<RunID>/`.

If the implementation or authority corpus changes materially during the sweep,
affected claims must be marked `STALE_INPUT` and rerun against the new baseline.

## 5. Authority map

Before evaluating requirements, publish a run-local authority map. At minimum it
must identify:

- current human rulings under `execution/_Coordination/_DECISIONS/`;
- current project contracts, PRD, specification, and decomposition;
- each deliverable's `_CONTEXT.md`, `Specification.md`, `Datasheet.md`,
  `Procedure.md`, `Guidance.md`, and `_STATUS.md`;
- live application and runtime source under `frontend/`;
- tests and validation wrappers;
- existing `Assessment_INSP-03_*.md`, `Evidence_*.md`, and run records; and
- superseded, archival, or explanatory-only material.

Agent instructions, matrices, and skill contracts are classified as
`FROZEN_EXTERNAL_INPUT` for this run. They may substantiate what the current app
does, but this plan does not judge whether their roles or workflows should be
retained, merged, ported, or retired.

The authority map must distinguish these functions:

| Function | Meaning |
|---|---|
| Normative scope | Defines what the product or deliverable is required to do |
| Accepted decision | Changes or interprets normative scope through human authority |
| Declared current state | Says what is presently implemented or unresolved |
| Implementation evidence | Shows live behavior or structure |
| Verification evidence | Demonstrates behavior at a named source state |
| Lifecycle evidence | Records workflow state; does not by itself prove completeness |
| Historical context | Explains provenance but cannot override a live authority |

If two live normative surfaces conflict and precedence is not explicit, do not
choose one. Record `AUTHORITY_CONFLICT` for human disposition.

## 6. Claim-level concordance

The atomic audit unit is a requirement or stable scope claim, not a whole
deliverable. Generate one row for every current requirement plus any material
implemented behavior that lacks a requirement mapping.

Required columns:

| Column | Contract |
|---|---|
| `ClaimID` | Stable requirement ID, or run-local `UNMAPPED-*` ID |
| `PackageID` / `DeliverableID` | Owning execution scope |
| `ClaimType` | `REQUIREMENT`, `ACCEPTANCE`, `EXCLUSION`, `IMPLEMENTED_UNMAPPED`, `REMAINING_WORK` |
| `NormativeSource` | Current authority and exact location |
| `LatestDecision` | Applicable human ruling or `NONE_FOUND` |
| `DeclaredState` | What current deliverable documents say |
| `ImplementationEvidence` | Exact source locations or `NONE_FOUND` |
| `VerificationEvidence` | Exact tests/reviews and reviewed source state |
| `LifecycleState` | Copied from `_STATUS.md`; never used as a completeness proxy |
| `AssessmentEvidence` | Existing inspection conclusion, date/source state, and whether still current |
| `Disposition` | One controlled value from §7 |
| `Confidence` | `HIGH`, `MEDIUM`, `LOW` |
| `RemainingWork` | Evidence-based residual, `NONE_OBSERVED`, or `UNKNOWN` |
| `HumanDecisionNeeded` | Decision ID or `NO` |

Every `PASS`-equivalent conclusion requires both implementation and verification
evidence where the claim is behavioral. Document-only or governance claims must
name their appropriate verification basis instead of inventing a code test.

## 7. Controlled dispositions

Use only these reconciliation dispositions:

- `ALIGNED` — current scope, declaration, implementation, and evidence agree.
- `IMPLEMENTED_UNDOCUMENTED` — live behavior exists without an accepted mapping.
- `DOCUMENTED_UNIMPLEMENTED` — current requirement has no adequate implementation.
- `PARTIALLY_IMPLEMENTED` — only a bounded portion is supported.
- `IMPLEMENTED_DIFFERENTLY` — behavior differs materially from current wording.
- `STALE_SPECIFICATION` — setup or superseded wording no longer describes the
  accepted current state.
- `STALE_ASSESSMENT` — an assessment conclusion has been overtaken by later
  documents, decisions, implementation, or tests.
- `STALE_VERIFICATION` — cited evidence does not bind the reviewed source state
  or no longer exercises the current behavior.
- `ACCEPTED_DIVERGENCE` — a human decision deliberately permits a bounded
  difference, deferral, or transitional state.
- `LIFECYCLE_ONLY_MISMATCH` — lifecycle wording or history conflicts with the
  evidence while scope and implementation do not.
- `DEFERRED_AGENT_WORKFLOW` — resolution depends on understanding or changing an
  agent instruction, skill contract, authority allocation, or workflow that is
  reserved for the separate owner-led program.
- `AUTHORITY_CONFLICT` — live normative sources disagree.
- `UNKNOWN` — evidence is insufficient; name the smallest next check.

Do not compress multiple different dispositions into one deliverable-level
verdict. A deliverable summary is derived from its claim rows.

## 8. Execution phases

### R0 — Method calibration

Run the full method on `PKG-02`, beginning with `DEL-02-01`, because the pilot
already exposed stale-assessment risk there. A human or designated reviewer
checks the first concordance packet for:

- correct authority precedence;
- adequate evidence granularity;
- false-positive rate;
- distinction between scope and current behavior; and
- usefulness of the proposed remaining-work statements.

Revise the run-local method before scaling. Do not rewrite deliverables in R0.

### R1 — Read-only inventory

Build:

1. package and deliverable inventory;
2. specification requirement index;
3. implementation surface index;
4. test and validation index;
5. decision-to-deliverable index;
6. assessment/evidence recency index; and
7. unmapped implementation candidate list.

Generated files and caches (`node_modules`, `.next`, `dist`, packaged apps, and
runtime sessions) are evidence only when specifically needed and must not be
treated as source truth.

### R2 — Package concordance waves

Process bounded package waves with disjoint artifact write scopes. Derive the
final ordering from the live dependency graph; the default grouping is:

1. `PKG-02` shell and operator state;
2. `PKG-03` through `PKG-06` runtime, provider, session, and permission spine;
3. `PKG-07` and the product-runtime portions of `PKG-08` filesystem and
   agent/pipeline integration, with underlying agent files and workflow design
   frozen and deferred;
4. `PKG-09` validation, packaging, and security;
5. `PKG-01` governance and reliance boundaries;
6. `PKG-10` future domain-engine boundary; and
7. `PKG-00` control-plane closure after downstream truth is known.

Each wave produces claim rows, a package summary, conflicts, unknowns, and a
proposed decision/repair queue. It does not edit deliverable documents.
`DEFERRED_AGENT_WORKFLOW` rows go only to the separate handoff and never enter
this program's repair queue.

### R3 — Cross-package synthesis

Detect:

- the same implementation surface claimed by incompatible deliverables;
- requirements with no implementation owner;
- implementation with no deliverable owner;
- inconsistent terminology or identifiers;
- test evidence cited by multiple claims with incompatible meanings;
- stale cross-deliverable dependencies; and
- remaining-work statements contradicted by another package.

Produce a complete coverage report: all deliverables, all requirements, all
material implementation surfaces, and every unresolved row accounted for.

### R4 — Human decision gate

Present a bounded queue grouped by decision type:

1. scope adoption or retirement;
2. product-behavior ruling;
3. acceptance-criteria ruling;
4. deliverable ownership/mapping;
5. residual work acceptance or deferral; and
6. lifecycle recommendation.

Agent-workflow questions are not decision packets under this plan. They are
collected without a recommendation to merge, retire, or port a workflow, so the
owner-led program can examine them with the missing operational context.

Every decision packet must include options, evidence, affected claims and
deliverables, downstream consequences, and a recommended minimal-change option.
Unruled items remain explicit; they do not block unrelated repairs.

### R5 — Authorized repair tranches

After dispositions are ruled, execute separate, bounded change tranches:

- refresh stale specifications and datasheets;
- supersede or annotate stale assessments without erasing historical evidence;
- correct current-state and remaining-work declarations;
- repair evidence pointers and verification records;
- update dependency mappings where separately authorized; and
- create implementation work items only for residuals that survive
  reconciliation.

R5 must not edit agent instructions, agent indexes or matrices, skill contracts,
or the authority/workflow semantics they encode. If an otherwise authorized
deliverable repair depends on one of those changes, split the tranche: apply the
independent product/document portion and leave the agent-workflow portion in the
separate handoff.

Do not mix product implementation with document repair unless the selected
tranche explicitly includes both and has independent acceptance criteria.

### R6 — Backcheck and closeout

Re-extract every changed claim and verify:

- normative wording, declared state, implementation, and verification agree;
- every residual is assigned or explicitly deferred;
- no stale assessment is still presented as current truth;
- no human decision is attributed to an agent;
- lifecycle states were unchanged unless separately authorized; and
- the final summary distinguishes deliverable readiness from release,
  professional approval, or issuance.

## 9. Run artifacts

Each immutable run folder must contain:

- `RUN_BASIS.md`
- `AUTHORITY_MAP.md`
- `DELIVERABLE_INVENTORY.csv`
- `IMPLEMENTATION_SURFACES.csv`
- `VERIFICATION_INDEX.csv`
- `CLAIM_CONCORDANCE.csv`
- `PACKAGE_SUMMARIES/PKG-XX.md`
- `UNMAPPED_IMPLEMENTATION.csv`
- `CONFLICTS_AND_UNKNOWNS.csv`
- `AGENT_WORKFLOW_HANDOFF.md`
- `HUMAN_DECISION_QUEUE.md`
- `AUTHORIZED_REPAIR_QUEUE.csv`
- `COVERAGE_AND_QA.md`
- `RUN_SUMMARY.md`

`execution/_Reconciliation/DeliverableConcordance/_LATEST.md` may point to the
latest completed run but must not replace immutable run artifacts.

## 10. QA and acceptance criteria

The discovery program is complete only when:

- 100% of live deliverables and current requirement IDs are indexed;
- every claim has a normative source or is explicitly `IMPLEMENTED_UNMAPPED`;
- every behavioral `ALIGNED` claim has exact implementation and verification
  evidence tied to the reviewed source state;
- every existing inspection assessment is classified as current, stale, or
  non-applicable at claim level;
- every material implementation surface is mapped or listed as unmapped;
- every agent-file or agent-workflow implication is classified
  `DEFERRED_AGENT_WORKFLOW`, recorded without a redesign recommendation, and
  excluded from the authorized repair queue;
- every conflict and unknown has an owner and smallest next action;
- package summaries are reproducible from the claim ledger; and
- a reviewer spot-checks all high-risk claims plus a representative sample of
  other dispositions.

The repair program is complete only when ruled repairs are applied, backchecked,
and the surviving remaining-work queue can be regenerated from current
deliverables without consulting obsolete plans.

## 11. Autonomous-loop rules

An autonomous loop iteration selects one bounded package wave or repair tranche,
re-derives its inputs, performs the work, validates the artifact contract, and
records closeout before selecting another item. It must stop or defer when:

- a human scope or acceptance decision is required;
- another session is modifying an affected source;
- authority precedence is unclear;
- validation evidence cannot be reproduced;
- a proposed change crosses the project write boundary; or
- the claim requires agent-instruction, skill-contract, agent-authority, or
  workflow-porting analysis reserved for the separate owner-led program; or
- the work would imply issuance, approval, or a product strategy decision.

The loop may continue around a blocked claim by processing independent claims.
It must never convert uncertainty into inferred scope merely to keep moving.

## 12. Completion state

Success means the live deliverable corpus can answer, without relying on old
plans or chat history:

- what is required;
- what is implemented;
- how that implementation was verified;
- what remains;
- what has been deliberately deferred; and
- which decisions or lifecycle actions remain human-owned.

Completion of this plan is not issuance, release readiness, professional
approval, certification, sealing, or authentication.
