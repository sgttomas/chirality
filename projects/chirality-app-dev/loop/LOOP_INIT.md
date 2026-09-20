# Work Loop — session init and generic loop

You are resuming, as the next bounded operator, the work loop that lives in
this file's directory. This file carries the protocol, the fences, the
checks, and the pointer index. It carries **no status, no history, and no
work**. Current work lives in the owning run and its session work graph,
with traceable links to the accepted phase DAG and relevant deliverables.
Priorities and phase transitions come from the owner. Revalidate state against
the live tree; do not restart historical work by default.
This text is orientation, **not authority**: owner rulings and directions
authorize work; sources govern on any disagreement.

## 1. Bootstrap

- Resolve `REPO_ROOT` with `git rev-parse --show-toplevel`; work from there.
  `WORKING_ROOT` is `projects/chirality-app-dev`.
- Handoff context (chat-only owner directions, gate outcomes, stale-map
  deltas) lives in `LOOP_RECEIPTS.md` beside this file; its local rules
  govern what a receipt may contain.

## 2. Where live work is re-derived (pointer index; never a status surface)

- **Session discovery:** the owner-named run, its work graph, handoff and
  recorded directions; otherwise discover applicable run pointers through
  `execution/_Coordination/_LATEST.md` and validated `LOOP_RECEIPTS.md`.
  Inspect named branches and worktrees, including unmerged and parked work.
- **Deliverable basis:** `execution/PKG-*/1_Working/DEL-*/` — `_STATUS.md`
  (lifecycle + `## Remaining`), `MEMORY.md`, `ScopeOfWork.md` or legacy
  four-document kits, `Dependencies.csv` / `_DEPENDENCIES.md`,
  `_run_records/**`.
- **Ruled records:** decision register
  `execution/_Coordination/_DECISIONS/_REGISTER.md` (packets and ruling
  records beside it; open rows are the owner-gated surface) ·
  `execution/_Coordination/_COORDINATION.md` · discovery pointer
  `execution/_Coordination/_LATEST.md` · v3 owner rulings and steers under
  repo-root `plans/steers/` (transcription sources, not authority).
- **Delegation instrument:** D-APP-60 as refined by D-APP-64 §5
  (`execution/_Coordination/_DECISIONS/D-APP-60_PACKET_FROZEN_BLOCK_INSTRUMENT_2026-07-17.md`,
  `D-APP-64_PACKET_REASONED_SELECTION_OVERLAY_2026-07-18.md` beside it).
- **Dependency evidence:** the accepted snapshot named by
  `execution/_Reconciliation/DepClosure/_LATEST.md` · SCC work follows
  repo-root `docs/CYCLE_DRIVEN_RESOLUTION.md`.
- **What must be built and why:**
  `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` ·
  scope amendments `execution/_ScopeChange/_LATEST.md` · product yardstick
  `docs/PRD.md` · strategy `docs/PLAN.md` (non-governing) · authority
  documents `docs/DIRECTIVE.md`, `docs/CONTRACT.md`, `docs/SPEC.md`,
  `docs/TYPES.md`.
- **Cross-loop handoffs:** routed Root notices `execution/_Coordination/NOTICE_*`
  · APP-HOLD-1 register `execution/_Coordination/APP_HOLD_REGISTER.csv` ·
  Task Management register `execution/_Coordination/_TaskManagement/REGISTER.csv`
  · `_DomainEngines/bridge/LOOP_RECEIPTS.md` (scope dedup only).
- **Validation gates:** `docs/VALIDATION_STRATEGY.md` ·
  `docs/RELEASE_QUALITY_GATES.md` (§13 is validation evidence only) ·
  `docs/BUILD_AND_RELEASE.md`.
- **Agent posture:** `AGENTS.md` beside this project (dispatch contract,
  delegation posture, independent-review path, host-capability rule,
  closeout and git discipline, concurrent-loop write-scope rule).
- **Frontend contract surfaces:** `frontend/packages/harness-contract/**`
  (pull contract pinned at
  `execution/_Coordination/_DECISIONS/D-APP-48_FLOW_A_PULL_CONTRACT_*.json`).
- **Historical archive (never selection surfaces):** `plans/**`
  (`plans/PLAN_COMPLETION_LOG.md` holds landed narrative) ·
  `execution/_Coordination/NEXT_INSTANCE_PROMPT.md` · every retired
  workplan under `plans/workplans/`. D-APP-114 retired the committed overlay;
  the owner-authorised session work graph now replaces the session workplan.

## 3. Standing constraints — hard fences (all iterations; always stop for a human ruling)

- **F-APP-1 (provider/network):** Codex remains the sole current MVP engine.
  Apply the current Runtime-owned network, tool and credential contracts as
  amended by D-GOV-43/A2 and D-APP-127. Retired hosted admission, per-root
  consent and supplier containment are not current proof prerequisites. Codex
  owns login/logout and its credentials in the App's effective Codex home;
  the App must not read, copy or relay those credentials or affect other
  clients' credentials. This loop grants no provider expansion, remote MCP,
  plugin or broad tool-search enablement beyond separately accepted scope.
- **F-APP-2 (release/distribution):** no signing, notarization, publication,
  external distribution, or release-readiness / professional / certification
  claims.
- **F-APP-3 (domain-engine boundary):** domain-engine work happens only
  inside what the tier-0 bridge loop's ruled decisions grant (the `D-APP-4x`
  F-series rows); this loop never writes `_DomainEngines/**` or piping
  surfaces, and never advances integration level, live binding, or
  apply-class tool exposure on its own authority.
- **F-APP-4 (issuance):** no `CHECKING -> ISSUED` lifecycle issuance.
- **F-APP-5 (truth and planning surfaces):** authoritative deliverable scope,
  lifecycle and dependencies remain in their governed sources; owner decisions
  remain in the decision register and applicable owner-direction records.
  The session work graph is the executable plan, not a replacement for those
  sources. It neither issues deliverables nor silently changes the phase DAG.
  Historical plans remain readable; do not select new work from them.
- **Fresh-ruling stops** (carried from the pre-consolidation coordination
  record): provider execution outside the current Codex MVP direction and
  its current accepted Runtime/network/credential scope; write/edit/bash/
  tool-execution exposure beyond the current approved item; changes to the
  project-truth model for sessions, transcripts, chats, runtime logs, or
  completion logs; professional-boundary or release-readiness posture.

Changing a fence requires owner authority. This loop grants no new release
act; later specific owner rulings retain their effects and historical releases
are not undone by F-APP-2. Do not infer another release from a prior one.

## 4. Phase DAG, session work graph and strategy

The project DAG describes project-wide deliverables and dependencies. It is
expected to remain relatively stable within each project phase and to be rebuilt
or reconciled when the owner directs the next phase. Agents do not infer or
initiate a phase transition from apparent progress. Use the accepted dependency
snapshot and decomposition in §2; no DAG rebuild is required at session entry.

Maintain the undertaking's work graph under
`execution/_Coordination/AgentRuns/<RUN_ID>/`. Choose a useful structure: each
slice's state, dependencies, blockers, named semantic changes, departures from
specification, deferred work and its retirement condition, and evidence pointers.
Link to the current phase's accepted DAG and relevant deliverables, marking
uncertain mappings provisional. Record discoveries for the next owner-directed
reconciliation rather than silently amending the DAG or guessing an evidence
home. Keep one canonical copy of run evidence and derive handoffs from the graph.

The graph replaces the session workplan. There is no dated workplan selector,
compulsory separate issue plan, or requirement to recreate a standing queue.
Existing plans, receipts and ruled snapshots retain their historical meaning.

Discover enough to propose the delegation and model strategy before substantial
implementation or launching agents. Explain Agent 0's work, delegated
responsibilities, model/effort choices, parallel work, write scopes and
integration/review ownership. Use previous experience where useful; cost
estimates are not required. Obtain the owner's agreement, then proceed within
it and revisit material changes. An already approved applicable strategy
satisfies this requirement. Read-only discovery and preparation of the strategy
and bounded decision packages may proceed beforehand.

## 5. The loop protocol (every iteration)

### Step 0 — Discover

Run from `REPO_ROOT`:

```bash
git status --short && git log --oneline -20
python3 tools/validation/validate_app_dev_loop_receipts.py --repo-root .
head -51 projects/chirality-app-dev/loop/LOOP_RECEIPTS.md && tail -60 projects/chirality-app-dev/loop/LOOP_RECEIPTS.md
rg -n "^\| D-APP-[0-9]+ \|([^|]*\|){2} (AWAITING_RULING|NOT_PREPARED)" projects/chirality-app-dev/execution/_Coordination/_DECISIONS/_REGISTER.md
ls projects/chirality-app-dev/execution/_Coordination/NOTICE_* 2>/dev/null
cd projects/chirality-app-dev && PYTHONDONTWRITEBYTECODE=1 python3 execution/_Reconciliation/References/reconcile_authority_corpus.py status; cd -
rg -l '^## Remaining' projects/chirality-app-dev/execution/PKG-*/1_Working/DEL-*/_STATUS.md
PYTHONDONTWRITEBYTECODE=1 python3 tools/practitioner_harness/harness.py status --project chirality-app-dev
PYTHONDONTWRITEBYTECODE=1 python3 tools/practitioner_harness/harness.py self-check
```

Rules the output does not show you:

- A receipt-validator failure blocks use of the ledger until it is repaired
  through its governed path.
- Check applicable owner steering, newer rulings and routed notices. This
  loop does not itself grant writes to Root surfaces.
- Verify before relying: plans, receipts, dated assessments, and your own
  tasking are maps with citations. Open the cited source; on disagreement
  repository evidence establishes what exists; it does not overrule owner
  direction. Preserve dated records and point to corrections in the owning run.
- If a relied-on brief or `Remaining` item pins a reference by hash, recompute it
  and stop on a mismatch.
- A `_STATUS.md` without a `## Remaining` section has no recorded open scope.
- For frontend, configuration and packaging work, identify checks whose
  earlier evidence the change invalidates. D-APP-127 replaces A1 re-staging
  with the affected-check rule; applicable S-8 production-path native evidence
  and packaging requirements remain in their owning records.
- Material conflicts in authority, scope or candidate identity block the
  affected action. Report minor documentary drift and correct it within scope
  while independent work proceeds. Do not reproduce work already in a lane.

### Step 1 — Select within the owner-directed undertaking

Use the owner's scope and priorities, the verified work graph, and relevant
accepted deliverable obligations. An open Remaining item is evidence of work,
not permission to restart a phase or expand the undertaking. Never revive a
ruled-shut item without the required owner act. Apply CONTRACT **K-ENGINE-6**:
standalone-harness or feature-parity work is off-strategy.

Preserve named `(gated: ...)`, `(stage-gated: ...)` and `NOT_SELECTABLE_UNTIL:`
conditions. Verify the required act at its specified source; a condition that
requires a merged ruling still requires it. Record current in-session owner
direction verbatim without pretending it was already merged. A predecessor
commit, its checks and its run record may establish a dependent step on the
same branch unless the specific gate requires a merge.

For deliverable dependency selection, re-derive blockedness from the item's
`Depends` line, `Dependencies.csv` / `_DEPENDENCIES.md` and the accepted
DepClosure snapshot, not a hand-maintained summary. A row blocks only when it
is `ACTIVE`, type `PREREQUISITE`, has `SatisfactionStatus` `TBD`, `PENDING` or
`IN_PROGRESS`, and the item's `Depends` names its target. `INTERFACE`,
`HANDOVER`, `CONSTRAINT` and `ENABLES` rows order work; `SATISFIED`, `WAIVED`
and `NOT_APPLICABLE` do not block. A provisional graph mapping cannot bypass
an applicable dependency or APP-HOLD-1 check.

Judgment-shaped forks are triaged under the D-APP-64 §5 contract (fast-reject
boundary first, then the selection method and attribution schema); D-APP-60
is the underlying instrument.

### Step 2 — Brief or slate

Material or hard-to-reverse forks (a fence question, a K-ENGINE-6 strategy
fork, a costly public-contract or data-migration change, an item marked as
needing its own packet) get a `PROPOSAL` packet in the decision register.
Ordinary forks inside the fences are decided by the agent and recorded per
D-APP-64 §5.3. Seal delegated briefs before launch: objective, parent, role, context and
hashes, tools, write scope, constraints, outputs and checks. Retain child
returns verbatim with hashes, actual model/effort, substitutions and disposition.
Record enforcement limits truthfully; harness-specific transcript scripts,
launch mechanics and commit trailers do not transfer automatically. A parent
launches and supervises its children and validates their returns. Type 2
instances do not delegate. A manager is useful for coupled repair cycles;
a bounded specialist may report directly to Agent 0. Neither role type nor
reasoning effort is a proxy for task complexity.

For a small read-only assignment, a launch message retained verbatim before
dispatch may itself be the sealed brief. Keep the same necessary purpose,
context identity, parent/role, tools and read-only boundary, expected return and
checks; no separate elaborate brief file is required. Preserve its hash and
return in the owning run. Scale the detail to the assignment, not its role type.

Disclose departures from specification, rationale and reversal method. An
explicit owner decision cannot be contradicted by an agent's preference.
Bring consequential decisions as packages with evidence and a recommendation.

An explicit ruling, a specifically adopted choice or a protected criterion
cannot be reversed by an agent. Other implementation departures may be decided
within delegated discretion and disclosed with their rationale and reversal
method. An approved specification is not automatically optional: read its terms
and the owner's direction to distinguish fixed requirements from implementation
discretion. Bring a conflict with a fixed requirement to the owner before acting.

### Step 3 — Gate

STOP at the hard fences (§3) and at owner acts: adoption, ruling, and
direction are the owner's (K-AUTH-1; D-GOV-04). Ambiguity about whether a
fast-reject boundary is touched is itself owner-class. In-session directions
are recorded verbatim in their governed artifact; chat-only directions with
no governed home go in the receipt, labeled evidence rather than ruling.
Record every gate outcome, including no-ops and their reason.

### Step 4 — Execute and check

Use scoped branches and worktrees appropriate to the undertaking. Preserve
unmerged work and record basis and candidate identities. Parallelise disjoint
writes with explicit dependencies; serialize shared-file integration and native
or browser resources when concurrent use would invalidate evidence. If repeated
repair attempts yield no new evidence, change the diagnosis rather than repeat
them indefinitely. Execute only within authorised scope.

Exercise changed user workflows as soon as they are operable using native
computer use, real pointer/keyboard input or suitable automation alongside code
tests. Extend connected scenarios as functionality permits: project and chat
creation, role/method selection, turns, tool review, interruption, retry,
attachments, save/reopen and recovery, including keyboard and window-size
behaviour where touched. Scale the scenarios to the change. Record expected and
observed outcomes, candidate/environment and evidence; fix defects and rerun
affected scenarios. Behavioural checks do not establish owner or usability
acceptance. Reconciliation work does not itself authorise product repairs.

When changed behaviour depends on native-host integration, verify it in the
native application; browser evidence alone does not establish that behaviour.
Identify the affected native scenarios in the slice's verification brief and
report any unavailable witness explicitly. This does not require a full native
sweep for every unrelated change.

Run §8 checks and satisfy §9 for evidence claims. Never weaken a protected
check to obtain a pass. Apply independent review and APP-HOLD-1 as required by
`AGENTS.md`. Product checks run on a clean candidate before merge; required CI
and review must cover the actual merging revision. Later edits need additional
review coverage and checks whose applicability changed.

Here a slice means a proposed mergeable change, including instructions and
owner-direction records; a read-only dispatch is not itself a slice. Scale review
depth to what the change can break. Small changes can have small independent
reviews; backcheck the affected correction and its consequences rather than
repeating the whole investigation without cause. This does not permit skipping
required review, leaving a finding unchecked or treating later bytes as reviewed.

During long work, keep the graph current and create useful recoverable Git
checkpoints at meaningful boundaries. Label incomplete work and unverified
checks explicitly; do not weaken a check to make a checkpoint green. After an
involuntary stop, inspect the branch, index and working tree before resuming:
a checkpoint or handoff may not include the last edits. This is not a requirement
to commit after every edit or to discard work that has not yet passed checks.

### Step 5 — Closeout or pause

Update the owning work graph, retain canonical evidence and a concise handoff
with remaining work, blockers and rerun requirements. Update deliverable scope,
status or the phase DAG only within an authorised reconciliation or deliverable
assignment; a merge does not discharge those commitments automatically. Preserve
lifecycle gates and `Checking Approval SHA` discipline. Use traceable pointers
rather than copying evidence into guessed deliverable locations.

At a meaningful pause or closure, append a short receipt pointing to the owning
run and continuation work under `LOOP_RECEIPTS.md`'s rules; rerun its validator.
Use scoped PRs at meaningful integration boundaries; no fixed one-commit-per-
iteration or whole-backlog exhaustion requirement applies. Standing Git authority
permits merge after actual-candidate CI and independent review pass, subject to
explicit holds. `chirality-change` and project `AGENTS.md` govern safe closeout.
Do not reinterpret old verdicts or claim a merged slice is an accepted deliverable.

## 6. First return from discovery

Give a concise live orientation: Git state, applicable run and receipt, owner
directions and gates, significant discrepancies, next bounded work and proposed
strategy. Distinguish owner direction, agent decisions and historical advice.
If parked pending owner direction, report that condition without manufacturing
implementation work. Continue under an applicable approved strategy and existing
authority; do not ask again for routine choices already covered.

## 7. Default posture

Complete the authorised undertaking, not every discoverable project obligation.
Maintain the graph while implementing, testing, repairing and integrating.
Bring unresolved consequential choices to the owner with a recommendation;
do not keep busy around an owner gate. Phase transitions remain owner-directed.

Pressure never weakens a gate, evidence bar, fence, ownership boundary or write
scope. Attribute agent judgments as such; never write a ruling or `RULED` row
for an owner act that did not occur. Specific steering and state pointers belong
in run records and discovery surfaces, not these recurrent instructions.

## 8. Checks by work type

| Work type | Required before push | Notes |
|---|---|---|
| Any tranche | repo-wide `self-check` exit 0; practitioner-harness pytest at closeout; receipt validator pass before and after appending | Cosmetic whitespace is not a commit or merge gate. |
| Product source (`frontend/src/**` outside `__tests__/**`, `frontend/electron/**`, `frontend/packages/**`, `frontend/scripts/**`, build/packaging config) | typecheck + vitest + build/premerge gates (`docs/VALIDATION_STRATEGY.md`, `docs/RELEASE_QUALITY_GATES.md`, `docs/BUILD_AND_RELEASE.md`); independent review per `AGENTS.md`; affected-check assessment under D-APP-127 | Stop the dev server before build/package/premerge commands; use available host permissions for build, premerge and render-bar runs; record unavailable required evidence. |
| UI work | the above plus the D-APP-36 render bar (`docs/ISSUE_READINESS_PROFILES.md` §4) | Evidence per `docs/ui/UI_POLISH_EXECUTION_PLAN.md`. |
| Authority docs (`docs/DIRECTIVE.md`, `CONTRACT.md`, `SPEC.md`, `TYPES.md`) | D-APP-38 corpus reconciliation (`execution/_Reconciliation/References/reconcile_authority_corpus.py`) | Drift is repair-first. |
| Governance / control-plane only | record that frontend gates were skipped because no runtime source changed | |
| Deliverable reliance, dispatch, CHECKING promotion or accepted-dependency consumption | APP-HOLD-1 preflight (`AGENTS.md`) | Every applicable act, regardless of entry path. Do not invent a deliverable target for instruction-only work. |
| Host-only surfaces | supported host approval mechanism where required, per `AGENTS.md` | Unavailable or declined execution remains `HOST_RERUN_REQUIRED`, not a pass. |

## 9. Evidence contract for empirical, fixture, conformance, and gate-evidence items (A12; Root R17 N3)

Acceptance and return require enough durable non-secret bytes for an
independent verifier to recompute the claim: input identities and cited-byte
inventory; fixture, evaluator, and validator bytes; command, arguments, cwd,
effective environment, versions, and exit status; canonical stdout/stderr
and machine-readable results; sorted manifests with independent hash
recomputation; and a bounded rerun method. Never preserve credentials,
tokens, or forbidden binaries. When the bytes cannot be preserved or
recomputed, the claim stays unavailable; a prose summary is not evidence.

## 10. Per-run steer

If the owner appended a steer for this run (the launcher's `Steer` line,
their message, or the owning run's direction record), apply it to priorities,
scope and phase. Keep run-specific steering out of this recurrent file. Owner
direction can amend procedure explicitly; it does not silently erase protected
checks or holds. Historical procedural habits are not new approval gates.
Historical receipts cite the section numbers of the revision current when
they were written: "LOOP_INIT §7 defaults" is the former session-conventions
section quoted verbatim in D-APP-61; §1 to §10 of receipts before D-APP-112
refer to the D-APP-105 text in git history.
