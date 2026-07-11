# Deliverable–Implementation Reconciliation Plan

**Date:** 2026-07-10
**Project:** Chirality App Dev
**Status:** DESIGN PROPOSAL — historical/non-governing method record; never a work-selection surface
**Revised:** 2026-07-10 after the owner-adopted deliverable-driven loop consolidation
**Prepared for:** owner-authorized reconciliation executed through the current standing loop after active development reaches a stable handoff
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

This file lives under `plans/` as method and provenance only. It cannot activate
itself and must never be treated as a queue. Execution requires an explicit owner
direction or ruling, followed by bounded reconciliation work recorded in the
affected deliverables' `_STATUS.md` `## Remaining` sections. The newest
`loop/WORKPLAN_*.md` governs execution; this proposal supplies only the
reconciliation method.

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
   acceptance criteria become draft packets for the existing human decision
   register; they do not form a parallel queue.
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
   routed unchanged to `AGENT_WORKFLOW_OBSERVATIONS.md` for later owner-led analysis.
   Product runtime behavior that loads, packages, invokes, or presents agents
   remains in scope, provided the repair does not alter the underlying workflow
   contract.
9. **Single work surface.** This proposal, its evidence bundles, and its findings
   never select work. Owner decisions remain in the existing decision register;
   executable residuals and authorized repairs live only in the owning
   deliverable's `_STATUS.md` `## Remaining`. Existing `(gated: ...)` and
   `(stage-gated: ...)` suffixes are preserved unless their owning authority
   changes them.

## 4. Start gate and baseline

Do not begin the full sweep until the human owner identifies the remedial session
as stable enough to inspect. Before any dispatch:

1. confirm an explicit owner direction or ruling authorizes the reconciliation
   scope and creation of its immutable evidence run;
2. confirm the selected reconciliation work is recorded in the affected
   deliverables' `_STATUS.md` `## Remaining` sections; if not, stop for the
   owner-authorized bootstrap update rather than selecting work from this plan;
3. resolve `REPO_ROOT` and `WORKING_ROOT` from the active checkout;
4. record a source-state identifier for the reviewed tree;
5. enumerate live packages, deliverables, lifecycle states, and all present or
   absent `## Remaining` sections directly from `execution/`;
6. identify files actively changing in another session and defer their affected
   claims rather than racing them; and
7. create the specifically authorized immutable run folder:
   `execution/_Reconciliation/DeliverableConcordance/<RunID>/`.

If the implementation or authority corpus changes materially during the sweep,
affected claims must be marked `STALE_INPUT` and rerun against the new baseline.

## 5. Authority map

Before evaluating requirements, publish a run-local authority map. At minimum it
must identify:

- current human rulings under `execution/_Coordination/_DECISIONS/`;
- the newest `loop/WORKPLAN_*.md`, `loop/LOOP_INIT.md`, and loop receipts as
  execution protocol and handoff context, not product-scope authority;
- current project contracts, PRD, specification, and decomposition;
- each deliverable's `_CONTEXT.md`, `Specification.md`, `Datasheet.md`,
  `Procedure.md`, `Guidance.md`, and `_STATUS.md`;
- live application and runtime source under `frontend/`;
- tests and validation wrappers;
- existing `Assessment_INSP-03_*.md`, `Evidence_*.md`, and run records; and
- superseded, archival, or explanatory-only material.

Agent instructions, matrices, skill contracts, and agent-workflow guidance are
classified as `FROZEN_PROCESS_INPUT` for this run. They may constrain execution
or substantiate what the current app does, but this plan does not judge whether
their roles or workflows should be retained, merged, ported, or retired. If an
older workflow guide conflicts with the newest loop workplan, record the stale
process-document fact for the separate owner-led program; do not repair it here.

The authority map must distinguish these functions:

| Function | Meaning |
|---|---|
| Normative scope | Defines what the product or deliverable is required to do |
| Accepted decision | Changes or interprets normative scope through human authority |
| Declared current state | Says what is presently implemented or unresolved |
| Recorded remaining work | `_STATUS.md` `## Remaining`; the sole current work-discovery surface, including its source and gate suffixes |
| Implementation evidence | Shows live behavior or structure |
| Verification evidence | Demonstrates behavior at a named source state |
| Lifecycle evidence | Records workflow state; does not by itself prove completeness |
| Execution protocol | Constrains how selected work runs; does not create product scope or select work |
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
| `RecordedRemaining` | Exact current `_STATUS.md` residual text or `NONE_RECORDED` |
| `RemainingSource` | Source named by the residual or `NONE_RECORDED` |
| `RemainingGate` | Exact gate/stage suffix or `UNGATED`/`NONE_RECORDED` |
| `SelectableUnderCurrentLoop` | `YES`, `NO`, or `UNKNOWN`, derived from current lifecycle, gate, and dependency evidence |
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
- `REMAINING_STATE_MISMATCH` — a landed or ruled-shut item remains recorded, an
  evidence-backed residual is omitted, or ownership/source/gate metadata no
  longer agrees with current authority and implementation.
- `DEFERRED_AGENT_WORKFLOW` — resolution depends on understanding or changing an
  agent instruction, skill contract, authority allocation, or workflow that is
  reserved for the separate owner-led program.
- `AUTHORITY_CONFLICT` — live normative sources disagree.
- `UNKNOWN` — evidence is insufficient; name the smallest next check.

Do not compress multiple different dispositions into one deliverable-level
verdict. A deliverable summary is derived from its claim rows.

## 8. Execution phases

### R0 — Method calibration

After activation is recorded on the live work surface, run the full method on
the owner-authorized calibration deliverable(s). `DEL-02-01` remains the
recommended first sample because the pilot already exposed stale-assessment
risk there, but this plan does not make it selectable. A human or designated reviewer
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
6. assessment/evidence recency index;
7. present/absent `## Remaining` inventory with source and gate parsing; and
8. unmapped implementation candidate list.

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

Each wave produces claim rows, a package summary, conflicts, unknowns, and
non-operative decision/repair findings. It does not edit deliverable documents.
`DEFERRED_AGENT_WORKFLOW` rows go only to the evidence-only agent-workflow
observations artifact and never enter this program's repair recommendations.

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

Present bounded findings and draft decision packets grouped by decision type:

1. scope adoption or retirement;
2. product-behavior ruling;
3. acceptance-criteria ruling;
4. deliverable ownership/mapping;
5. residual work acceptance or deferral; and
6. lifecycle recommendation.

Agent-workflow questions are not decision packets under this method. They are
collected without a recommendation to merge, retire, or port a workflow, so the
owner-led program can examine them with the missing operational context.

Every decision packet must include options, evidence, affected claims and
deliverables, downstream consequences, and a recommended minimal-change option.
Unruled items remain explicit; they do not block unrelated repairs.

### R5 — Authorized repair tranches

After dispositions are ruled or directed and the work is recorded in the
owning deliverable's `## Remaining`, execute separate bounded change tranches:

- refresh stale specifications and datasheets;
- supersede or annotate stale assessments without erasing historical evidence;
- correct current-state and remaining-work declarations;
- repair evidence pointers and verification records;
- update dependency mappings where separately authorized; and
- record surviving implementation or validation residuals only in the owning
  deliverable's `## Remaining`, preserving applicable source and gate metadata.

R5 must not edit agent instructions, agent indexes or matrices, skill contracts,
or the authority/workflow semantics they encode. If an otherwise authorized
deliverable repair depends on one of those changes, split the tranche: apply the
independent product/document portion and leave the agent-workflow portion in the
separate evidence-only observations artifact.

Do not mix product implementation with document repair unless the selected
tranche explicitly includes both and has independent acceptance criteria.
Every completed repair follows the standing loop closeout contract: update the
owning `_STATUS.md` `## Remaining`, `MEMORY.md`, and `_run_records/**`; append the
minimal loop receipt and completion narrative required by current guidance; run
applicable validation; hand off to CHANGE; open a PR; and never self-merge.

### R6 — Backcheck and closeout

Re-extract every changed claim and verify:

- normative wording, declared state, implementation, and verification agree;
- every residual is assigned or explicitly deferred;
- no stale assessment is still presented as current truth;
- every accepted residual is reflected on the owning deliverable's sole
  `## Remaining` work surface and every landed item is removed there;
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
- `AGENT_WORKFLOW_OBSERVATIONS.md`
- `PROPOSED_DECISION_FINDINGS.md`
- `PROPOSED_DELIVERABLE_UPDATES.csv`
- `COVERAGE_AND_QA.md`
- `RUN_SUMMARY.md`

These are immutable evidence artifacts, not queues or selection surfaces.
`AGENT_WORKFLOW_OBSERVATIONS.md` contains only affected product claims, exact
citations, and why reconciliation cannot resolve them; it makes no workflow
recommendation. Do not create a new `_LATEST.md`, standing pointer, register, or
status surface unless separately ruled. Continuing state is recorded in the
affected deliverables and existing decision register.

## 10. QA and acceptance criteria

The discovery program is complete only when:

- 100% of live deliverables and current requirement IDs are indexed;
- every claim has a normative source or is explicitly `IMPLEMENTED_UNMAPPED`;
- every behavioral `ALIGNED` claim has exact implementation and verification
  evidence tied to the reviewed source state;
- every existing inspection assessment is classified as current, stale, or
  non-applicable at claim level;
- every material implementation surface is mapped or listed as unmapped;
- every live deliverable's present or absent `## Remaining` section is checked
  against current implementation, decisions, and residual evidence;
- every agent-file or agent-workflow implication is classified
  `DEFERRED_AGENT_WORKFLOW`, recorded without a redesign recommendation, and
  excluded from proposed deliverable updates;
- every conflict and unknown has an owner and smallest next action;
- package summaries are reproducible from the claim ledger; and
- a reviewer spot-checks all high-risk claims plus a representative sample of
  other dispositions.

The repair program is complete only when ruled repairs are applied, backchecked,
and the surviving work surface is correctly represented in current deliverable
`## Remaining` sections without consulting obsolete plans.

## 11. Autonomous-loop rules

An autonomous loop iteration selects an eligible deliverable-local
`## Remaining` item under the newest standing workplan, never a package wave or
repair finding from this proposal. The reconciliation method governs execution
only after that selection. Each iteration re-derives its inputs, performs the
bounded work, validates the artifact contract, and records deliverable-local
closeout before selection restarts. It must stop or defer when:

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
