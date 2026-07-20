# Orchestration Plan v1 — CQ-F1 Post-D-APP-68 Concordance

- **RunID:** `APPDEV_LOOP_2026-07-19_CQF1_CONCORDANCE`
- **Plan version:** 1
- **Selection authority:** `AGENT_0`
- **Descriptive posture:** `MIXED`
- **Branch:** `codex/app-dev-cqf1-concordance-20260719`
- **Accepted basis:** `be4be0dfcc18a34995db61429a2342c2758a5d00`
- **Parent receipt:** Receipt-75
- **Lifecycle transition:** prohibited
- **Frontend/runtime writes:** prohibited
- **Hard-fence crossing:** prohibited

This plan freezes HELP_HUMAN's cross-manager work graph. It is a control
record, not authority, decomposition truth, a decision slate, or a work queue.
The five live `_STATUS.md ## Remaining` entries remain the executable work
surface. Derivative findings cannot create ownership or close those entries.

## Accepted activation and method basis

1. Committed standing workplan:
   `projects/chirality-app-dev/loop/WORKPLAN_2026-07-18b_app_dev_loop.md`.
2. Valid Receipt-75 and its executed D-APP-68 pointers.
3. D-APP-65 disposition 7: a scoped post-merge concordance pass using the
   D-APP-55 ratified method revisions.
4. D-APP-68 ruled and merged; its ownership mappings and explicit no-ops are
   current inputs, never editable evidence.
5. Prior derivative handoff:
   `projects/chirality-app-dev/execution/_Reconciliation/DeliverableConcordance/SCOPED_D65_CONCORDANCE_2026-07-19/HANDOFF.md`.
6. D-APP-56 R4-P48: all 22 CQ-F1 paths were deferred with affinity only,
   expressly without ownership or mapping, for revisit at the next
   concordance pass.
7. D-APP-60 method binding as refined by D-APP-64's reasoned-selection
   overlay. Fast-reject limits remain owner-class; a disposition-class result
   applies existing authority, creates none, is bounded/reversible, records
   rationale and rejected alternatives, and receives calibrated independent
   verification.

R1 must confirm at activation preflight that the committed D-APP-65 ruling,
the D-APP-55 MR-1..MR-11 plus R2 addendum method, and this exact RunID satisfy
its actual RECONCILIATION instruction package. Any unresolved activation or
authority conflict is a terminal `BLOCKED_INPUT`, not an inferred waiver.

## Frozen scope

`CQF1_SCOPE.csv` is the exact scope manifest: 22 unique existing paths in five
live Remaining containers. Ordered path-list SHA-256 (one repo-relative path
per line, manifest order, trailing LF):
`2e314f3f601350736032ace2730492c2afa6ab5b21fe26465d799470a195fc36`.

| Remaining container | Paths |
|---|---:|
| DEL-02-01 | 14 |
| DEL-03-03 | 1 |
| DEL-06-02 | 1 |
| DEL-09-04 | 4 |
| DEL-10-04 | 2 |
| **Total** | **22** |

R1 may inspect only evidence needed to assess these paths, their five live
Remaining entries, accepted authority, current deliverable affinities, and
candidate mapping. A cited supporting file is read context, not added scope.

## Frozen work graph

| Node | Owner | State | Depends on | Return / fan-in gate |
|---|---|---|---|---|
| R1 | RECONCILIATION | READY_RELEASED | accepted basis | New derivative concordance package plus `instances/R1/RETURN.md`; HELP_HUMAN validates schema, scope, provenance, child fan-in, and containment before V1 |
| V1 | EVALUATION | PENDING | R1 terminal return accepted for audit | Independent read-only-subject evaluation package plus `instances/V1/RETURN.md`; HELP_HUMAN accepts or blocks the evidence/mapping/classification claims |
| D1 | HELP_HUMAN | PENDING | V1 ACCEPT accepted | Cross-manager classification and route: disposition-class, owner-class slate, no-repair closure, or rerun |
| H1 | HUMAN | CONDITIONAL | D1 owner-class route | Owner ruling on a near-miss candidate slate; no inferred approval |
| W1 | WORKING_ITEMS | BLOCKED | D1 disposition-class route under existing authorization **or** H1 explicit ruling | Package-bounded repair returns under a later versioned brief; no scope is granted by this reservation |
| V2 | EVALUATION | CONDITIONAL | accepted W1 returns | Fresh read-only-subject repair/backcheck evaluation before closure |
| C1 | ORCHESTRATOR | PENDING | D1 accepted no-repair closure **or** V2 ACCEPT | Serialized closeout/handoff proposal; shared receipt/completion-log writes require a later explicit brief |
| G1 | CHANGE | PENDING | C1 accepted and required checks pass | Git closeout only; no content repair; owner merge remains terminal |
| H2 | HUMAN | PENDING | G1 complete | Review and merge |

## R1 execution and optional subagent use

HELP_HUMAN dispatches exactly one RECONCILIATION manager. R1 is the sole
integration owner for the derivative package and may delegate bounded,
read-only package/path analysis through the Agent 2 forms permitted by its
actual instruction package. The useful terminal fan-out is at most five
independent analysis slices matching the five Remaining containers above.

- Shared reads are allowed.
- Children do not edit frontend/runtime, deliverables, decisions, receipts,
  prior reconciliation packages, or Git state.
- Each child return has a disjoint target under
  `instances/R1/children/<child-id>/`; children do not write the derivative
  package directly.
- R1 validates all returns, preserves conflicts, and serially authors the new
  derivative package. Invalid or partial returns are not accepted at fan-in.
- A live finding relevant to another slice travels through R1; no hidden
  sibling coordination or overlapping writes are allowed.

R1's derivative write root is frozen as:
`projects/chirality-app-dev/execution/_Reconciliation/DeliverableConcordance/SCOPED_CQF1_POST_DAPP68_CONCORDANCE_2026-07-19/`.
Its other write targets are only its instance return/control records under
this run root.

Minimum R1 package outputs:

- `RUN_BASIS.md`
- `CQF1_PATH_LEDGER.csv`
- `AFFINITY_AND_MAPPING_ANALYSIS.md`
- `PROPOSED_MAPPING.csv`
- `DECISION_CLASSIFICATION.md`
- `CANDIDATE_OWNER_SLATE.md` (only if owner-class; clearly `PROPOSAL`)
- `QA.md`
- `HANDOFF.md`

Every one of the 22 rows must record current path existence/source binding,
current evidence and citation state, preserved prior affinity, candidate
deliverable mapping, competing candidates, rejected alternatives, authority
anchors, and D-APP-60/D-APP-64 classification. No row may treat
implementation as authority or prior affinity as ownership.

## V1 independent audit

V1 is a fresh EVALUATION manager with no R1 authorship. The evaluated subject
is read-only. V1 independently reopens the 22 paths, five live Remaining
entries, D-APP-56/60/64/65/68, Receipt-75, the workplan, and accepted prior
handoffs. It must attempt to refute:

1. exact 22/22 coverage and source-state binding;
2. evidence and citation claims;
3. affinity preservation without ownership smuggling;
4. each proposed mapping and competing alternative;
5. every disposition-class or owner-class classification;
6. hard-fence, lifecycle, runtime-write, and derivative-status compliance;
7. the completeness and truthful attribution of any candidate owner slate.

V1 writes only under
`projects/chirality-app-dev/execution/_Evaluation/CQF1_POST_DAPP68_CONCORDANCE_2026-07-19/`
and its instance return/control records. No candidate slate or closure verdict
is accepted until HELP_HUMAN validates V1's terminal return.

## Decision and repair gates

D1 applies fast-reject ordering after V1:

- **Disposition-class route:** W1 may be released only when R1 proves, V1
  independently sustains, and HELP_HUMAN accepts that the exact action applies
  existing authority, creates no scope/ownership/normative criterion, stays
  bounded and reversible, and satisfies D-APP-60/D-APP-64 attribution and
  verification. Plural surviving alternatives alone is not an owner gate.
- **Owner-class route:** any ownership creation/transfer, new accepted mapping,
  scope adoption, normative/acceptance criterion, lifecycle/stage/release act,
  hard-fence contact, stale evidence, authority conflict, or ambiguity about a
  fast-reject boundary holds W1 and routes a near-miss slate to H1.
- **No-repair route:** evidence may show the live entries are already
  concordant or deliberately remain open. D1 may accept a derivative closure
  only after V1, without editing the five Remaining entries.
- **Block/rerun route:** incomplete coverage, changed source basis, invalid
  return, or V1 `BLOCK` returns to R1 under a versioned amendment.

W1 has no current write authorization. A later release must freeze exact
package ownership, disjoint write targets, accepted upstream snapshots,
validation, and handoff requirements. Runtime/frontend source remains
excluded in every route.

## Fan-in, closure, and safety

- HELP_HUMAN owns every cross-manager fan-in and consequential amendment.
- Concurrent writes must be disjoint; R1 is serialized integration owner for
  the concordance package, V1 for the evaluation package, and any later W1
  briefs must identify one integration owner per overlapping package.
- Failed nodes block only declared dependants. Independent read-only analysis
  may continue.
- Prior reconciliation/evaluation packages are immutable derivative evidence.
- New R1/V1/V2 packages are derivative and must cite accepted upstreams; they
  never substitute for decisions, decomposition, deliverable, lifecycle, or
  runtime truth.
- No waiver is pre-authorized.
- Any basis change, any of the 22 source paths changing, a five-entry Remaining
  change, a governing decision change, or a contradictory verifier return
  invalidates affected returns and requires rerun from the earliest stale
  node.

## Current release posture

R1 is the only released execution node. V1, D1, H1, W1, V2, C1, G1, and H2
remain dependency-gated. There is no current owner decision request: whether
one is needed is itself an evidence/classification output that cannot be
accepted before V1.
