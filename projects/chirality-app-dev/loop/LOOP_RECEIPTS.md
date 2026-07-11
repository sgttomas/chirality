# App-Dev Loop Receipts

> **Epistemic status: derivative handoff ledger — not authority.** Append-only.
> Current state is always re-derived from the live tree, the decision register,
> the owner-adopted queue plans, git history, and the deterministic checks; on
> any disagreement those sources govern (K-AUTH-1). A receipt records only what
> tools cannot re-derive: owner directions given outside governed artifacts,
> gate outcomes and their rationale, deltas found in dated maps (which are never
> edited), and pointers to the authoritative artifacts created elsewhere.

## Rules (fixed — part of the loop protocol)

1. **Pointer, not narrative.** Prefer paths, PR numbers, commit SHAs, decision
   IDs, and queue-item IDs. Work history lives in commits, PRs, decision
   records, plan rows, and project-local files — never here.
2. **Owner directions verbatim.** Any owner direction not otherwise captured in
   a governed artifact is quoted word-for-word with its date. This is the one
   place chat-only directions become durable.
3. **Measurements as check summaries only.** `self-check pass; harness pytest
   pass; typecheck/vitest/build gates pass` is the maximum — counts and tables
   belong in plan rows and evidence artifacts.
4. **Stale-map deltas as one-line pointers.** Dated assessments and plan files
   are never edited to match reality; a receipt line says what disagreed and
   where to verify.
5. **Gate outcomes with reason.** stopped / executed / awaiting owner — and
   why, especially no-op outcomes ("all remaining work is owner-shaped"), so
   the next loop neither rediscovers the stop nor invents work around it.
6. **Capped.** Roughly 6–12 lines per receipt. If it wants more, the detail
   belongs in a decision packet, PR description, or project-local record.

## Receipts

- **2026-07-04 — Receipt 0** (loop creation).
  - Start: local `main` synced with origin at the PR #54 merge; loop artifacts
    authored on branch `claude/pec-init-prompt` (PR #55).
  - Owner direction of record (2026-07-04, in-session, Ryan Tufts): "I want the
    new init-prompt to be the current leaner convention, not this older one.
    All projects should have the current development loop structure and
    workflow, and therefore same type of init prompt." — with "Dedicated loops
    per project" selected over pointing at the shared bridge loop.
  - Artifacts created: `projects/chirality-app-dev/loop/{LOOP_INIT.md
    (byte-identical copy of the generic loop init), this WORKPLAN, this
    ledger}`; `projects/chirality-app-dev/init/init-prompt.md` rewritten to the
    lean launcher pointing here.
  - Deltas (live tree wins): the legacy entry
    `execution/_Coordination/NEXT_INSTANCE_PROMPT.md` remains in place as a
    dated historical map — status claims inside it (active queue, operating
    mode) are not refreshed by this loop's creation; the live queue state is
    re-derived from the register and plan rows at Step 0.
  - Gate outcome: structure-only tranche; no app-dev queue item selected, no
    register change. First working iteration starts at the next launch's
    Step 0.
  - Parked lanes: owner rulings on the app-dev register's open rows (re-derive
    from `execution/_Coordination/_DECISIONS/_REGISTER.md` at Step 0).

- **2026-07-10 — Receipt 1** (inspection-orphan remediation resumed).
  - Start: clean detached `199c6d545` = `main` = `origin/main`; branch
    `codex/app-dev-orn-remediation`; newest prior receipt Receipt 0.
  - Owner steer (2026-07-10, in-session, Ryan Tufts): "Fan out and fan in with
    subagents where warranted."
  - Live gates: D-APP-01..52 all RULED; D-APP-51/52 already consumed; no open
    app-dev register row. Active queue remains
    `plans/PLAN_2026-06-21_inspection_orphan_remediation.md`.
  - Executed: ORN-02 `71fff1277`; ORN-03 `ed54bbf94`; ORN-04 `658802bd5`;
    ORN-05 `40afda52c`; ORN-07 `2eef3d09c`; ORN-08 `dc9c50ca6`; ORN-09
    `24f40d5d8`; ORN-06 dropped as already closed.
  - Gate outcome: ORN-01 BLOCKED — live CI is repo-root
    `.github/workflows/harness-premerge.yml`, outside D-APP-39 app-dev-only
    staging authority and under newer owner-directed manual-only posture
    `48f622c93`; explicit root-workflow direction required.
  - Deltas: `_LATEST.md` still says D-APP-45 AWAITING_RULING; live register says
    D-APP-45..52 RULED. Standing workplan F-APP-1 wording predates D-APP-44;
    live ruling/active queue govern.
  - Checks: self-check pass; full practitioner-harness pytest pass; frontend
    focused/full Vitest pass; typecheck pass; authority corpus status pass; git
    diff check pass.
  - Parked/next: PEC P4 requires owner-at-screen; ORN-10..13 remain VERIFIED /
    READY; issuance/release/apply/live-binding hard fences unchanged.

- **2026-07-10 — Receipt 2** (`ORN-01` root-workflow authority granted and consumed).
  - Accepted owner direction (2026-07-10, in-session, Ryan Tufts): "For ORN-01
    you are permitted to modify repo-root as specified."
  - Upstream: Receipt 1 and active
    `plans/PLAN_2026-06-21_inspection_orphan_remediation.md`; derivative-package
    status unchanged and no authority-corpus document changed.
  - Executed: repo-root `.github/workflows/harness-premerge.yml` now runs on
    relevant pull requests with the stub provider and no paid secret or Claude
    CLI; it enforces typecheck, full Vitest, instruction-root integrity, and the
    release-quality wrapper.
  - Boundary: CI uses a temporary project root outside the immutable
    instruction-root fixture; the workflow-contract regression pins this
    containment requirement and the four enforced gates.
  - Gate outcome: ORN-01 DONE. Section 8 premerge, release-quality, and
    instruction-root-integrity summaries are verified separately; this is CI
    plumbing and not a release-readiness claim.
  - Checks: local release-quality wrapper pass with premerge not skipped;
    Section 8 and Section 9 pass; workflow contract and typecheck pass; CI
    fixture integrity pass.
  - Handoff: ORN-10..13 remain VERIFIED / READY; PEC P4 still requires
    owner-at-screen; issuance/release/apply/live-binding hard fences unchanged.

- **2026-07-10 — Receipt 3** (inspection-orphan queue exhausted).
  - Owner steer (2026-07-10, in-session, Ryan Tufts): "Fan out and fan in
    with subagents where warranted."
  - Start/upstream: clean synchronized `b001bd247`; Receipt 2; no open or
    newer D-APP register row; active queue recomputed from the live plan.
  - Executed: ORN-13 `6e3f4b5b4`; ORN-10 `da5a8f803`; ORN-11
    `9f8f5aae4`; ORN-12 `d2f1cb7ff`; all were independently verified before
    disjoint implementation and CHANGE closeout.
  - Gate outcome: queue CLOSED — ORN-01..05 and ORN-07..13 DONE; ORN-06
    DROPPED as already closed; no eligible row remains and no successor queue
    is inferred.
  - Checks: full frontend Vitest/typecheck pass; 16-ID Section 9 and unskipped
    release-quality pass; secret scan pass; self-check and full practitioner
    pytest pass; git diff check pass.
  - Delta: `_LATEST.md` still labels the now-exhausted remediation plan ACTIVE;
    live plan rows/status and this receipt govern discovery.
  - Parked: PEC P4 requires owner-at-screen; issuance, release/distribution,
    provider expansion, and live/apply integration retain their owner gates.

- **2026-07-10 — Receipt 4** (post-closure discovery; coordination repair; D-APP-53 slate).
  - Start: clean `61d70bdb0` = `main` = `origin/main`; worktree branch
    `claude/app-dev-loop-post-orn-2026-07-10`; newest prior receipt Receipt 3.
  - Owner steer (2026-07-10, in-session, Ryan Tufts): "Fan out and fan in with
    subagents where warranted. Use only `fable` models, contrary to your loop
    instructions. Create a new worktree before you set off and start a branch
    for your work."
  - Live gates: D-APP-01..52 all RULED, no open row; ORN queue CLOSED; fan-out
    discovery confirmed every ruled tranche landed (two D-APP-50 residuals stay
    descriptor-only per their own ruling, pending piping transport soundness).
  - Executed (branch-first + PR #155; no self-merge): guidance-surface repair
    per the `_COORDINATION.md` correction rule (`_LATEST.md` lean rewrite;
    `_COORDINATION.md` queue/ceiling/intake lines; ADQ plan header aligned to
    its own §9); D-APP-53 successor-queue PROPOSAL packet + AWAITING_RULING row.
  - Gate outcome: all remaining development work is owner-shaped — slate is
    D-APP-53 (Options A–E, non-binding rec. A); D-APP-52 live-LLM demo and PEC
    P4 stay owner-gated; hard fences unchanged. Loop parks pending ruling.
  - Checks: worktree self-check exit 0; practitioner pytest 263 passed/1
    skipped; corpus v5 no drift; frontend gates green on main (typecheck pass;
    Vitest 667/4 skipped); frontend untouched by this tranche.
  - Delta (external state): uncommitted main-tree deletions of
    `projects/chirality-governance/**` trip the live-baseline WARN pin (6→7)
    when pytest runs there; clean-tree runs pass — not repaired by this loop.

- **2026-07-10 — Receipt 5** (loop-instruction consolidation, owner-adopted;
  deliverables become the work-discovery surface).
  - Start: `origin/main` at the PR #158 merge (`7f0571b19`); branch
    `claude/chirality-app-dev-loop-consolidation`; newest prior receipt Receipt 4.
  - Owner directions of record (2026-07-10, in-session, Ryan Tufts): the piping
    consolidation adoption — "I really want the deliverables themselves to be the
    means of discovering work going forward, with the loop mechanics included as the
    development loop instructions. ... We need to simplify these instructions and
    avoid creating unnecessary registers or plans."; "Adopted." — then, for this
    project: "Now do the same for chirality-app-dev/  you have my permission to
    include that project in your write scope. Use subagents (fable model) when
    warranted."
  - Artifacts: `WORKPLAN_2026-07-10_app_dev_loop.md` (supersedes the 2026-07-04 plan;
    adds fence F-APP-5, single-surface rule); `_COORDINATION.md` rewritten as a
    ruled-record stub (queue-of-record retired; correction rule, state rules, and
    authoritative-state enumeration preserved); `## Remaining` sections in 15
    deliverable `_STATUS.md` files (19 items rehomed from the D-APP-53 candidate
    enumeration, each gated); D-APP-53 packet §7 addendum (no successor queue plan;
    the ruling now names live lanes — row stays AWAITING_RULING); `_LATEST.md`
    work-discovery lines; `NEXT_INSTANCE_PROMPT.md` internal historical banner;
    `LOOP_INIT.md` §7 synced to the 2026-07-05 owner revision; docs entry pointers
    aligned; `plans/PLAN_COMPLETION_LOG.md` consolidation entry. Scope note: one
    repo-root edit outside `projects/chirality-app-dev/**` —
    `tools/practitioner_harness/test_live_baseline.py` conscious pin update
    (REVIEW 28→27; GEN8 25→24 files) because relativizing docs/README.md's
    entry-list path cleared its pinned abs-path finding, per that file's
    same-PR pin-update rule. PR from this branch, awaiting owner merge.
  - Gate outcome: coordination/control consolidation executed at owner direction; no
    lifecycle transition; no register-row state change (D-APP-53 remains the open
    owner gate — its ruling now names which rehomed lanes are live); hard fences
    F-APP-1..4 unchanged; D-APP-52 demo and PEC P4 stay owner-gated.
  - Checks: self-check exit 0; practitioner pytest pass; frontend gates skipped —
    governance/docs-only tranche, no runtime source changed; no authority-doc edit,
    so no D-APP-38 corpus bump.

- **2026-07-10 — Receipt 6** (D-APP-53 ruled Option A; dependency-reconciliation lane executed; merged with the Receipt-5 consolidation).
  - Start: `f5a4c3946` = `main` = `origin/main` (PR #155 merge); branch
    `claude/app-dev-d53a-dep-reconciliation-2026-07-10`; prior receipt 4.
  - Owner steer (2026-07-10, in-session, Ryan Tufts): "Fan out and fan in with
    subagents where warranted. Use only `fable` models, contrary to your loop
    instructions. Create a new worktree before you set off and start a branch
    for your work. Your first order of business is to present the decision
    slate to me D-APP-53." — worktree instruction rescinded in-session
    ("sorry ignore the worktree instruction and continue in the current one").
  - Owner ruling (2026-07-10, in-session slate selection): D-APP-53 =
    "Option A (Recommended)", no riders — recorded in
    `execution/_Coordination/_DECISIONS/D-APP-53_RULING_2026-07-10.md`;
    register row RULED.
  - Executed: queue `plans/PLAN_2026-07-10_pre_issuance_dependency_reconciliation.md`
    authored and run to CLOSED — DRQ-01..11 DONE; 89/100 rows SATISFIED on
    re-verified evidence, 11 left open with recorded gates; ten
    `Evidence_D53A_Dependency_Reconciliation_2026-07-10.md` records; accepted
    snapshot `CLOSURE_D53A_DEP_RECONCILIATION_2026-07-11_0224Z`;
    `DepClosure/_LATEST.md` + `_Reconciliation/_LATEST.md` updated. Three-way
    discovery + four-way execution subagent fan-out, all fable per steer.
  - Gate outcome: owner-gated residuals surfaced, not decided — DEP-10-03-004
    / DEP-10-04-004 (accepted-amendment judgment), DEP-10-04-006
    (ResponsibleParty), DEP-04-01-007 (D-APP-52 live-LLM gate); evidence-gated
    DEP-04-01-010..013, DEP-10-02-005, DEP-10-04-007/-008. No fence crossed;
    no `_STATUS.md` transition. Branch-first + PR; no self-merge.
  - Checks: v3.1 linter 0/0 on all ten registers; snapshot acyclic with
    `schema_invalid = 0`; self-check pass; corpus status pass; git diff check
    pass.
  - Sequencing/reconciliation (recorded at the PR #159 merge with `main`):
    the Option A ruling and this tranche's execution preceded the Receipt-5
    consolidation's adoption the same evening; the consolidation's packet §7
    addendum ("row stays AWAITING_RULING; no successor queue plan") was
    written without knowledge of the already-received ruling. The ruling
    stands (truthful attribution — the act occurred); the queue plan was
    authored and CLOSED under the packet's then-live §6 mechanism and is now
    historical archive per F-APP-5. Reconciled in this PR: register row RULED
    with sequencing note; packet §8 sequencing note; ruling record sequencing
    note; the ten Option A deliverables' `## Remaining` items updated to
    executed state with residual gates; coordination pointers refreshed;
    live-baseline pins re-verified post-merge.


- **2026-07-11 — Receipt 7** (concordance plans revised; lifecycle model settled; DRAFT kernel authored).
  - Start: clean branch `claude/concordance-method-2026-07-11` off `703deb9b7`
    (= `main` at the PR #159 merge); newest prior receipt Receipt 6.
  - Owner directions (2026-07-11, in-session, Ryan Tufts), verbatim: "present
    any rulings I'm expected to make for incorporation into these plans. I
    will decide on them. And then you may proceed as intended, with my
    athorization for the expanded write scope in this instance." — and, on
    the shared method: "I do indeed intend this to be part of Chirality
    itself, and you may proceed as you recommend." Piping suspension
    direction quoted in the piping plan's §4 start gate.
  - Owner rulings (2026-07-11, in-session decision slate): app-dev lifecycle
    rebaseline = "All 53 → IN_PROGRESS (Recommended)"; piping PKG-00 =
    "→ IN_PROGRESS now (Recommended)". Recorded in both plans' lifecycle
    sections; register transcription + `_STATUS.md` transitions belong to a
    dedicated rebaseline tranche that must precede concordance discovery.
    Run-phase model (ruled-program, three state homes) and shared-kernel
    path (DRAFT at root, ratify after both R0s) settled in the same session.
  - Executed: both concordance plans revised in place (activation mechanics
    with land-on-main hard rule; change-regime lifecycle model with the
    warranted-empty CHECKING trigger; rebaseline rulings recorded; three-home
    run-state model; sibling/kernel cross-references; census corrections;
    pilot-claim markers); `docs/DELIVERABLE_CONCORDANCE_METHOD.md` authored
    at repo root as DRAFT pending ratification. Scope note: two writes
    outside `projects/chirality-app-dev/**` — the piping plan and the root
    kernel — both under the owner grant quoted above. Two fable TASK agents
    (one per plan) + orchestrator-authored kernel.
  - Gate outcome: owner-gated next acts, none started — rebaseline
    transcription tranche (both projects), canon lifecycle-semantics edit
    (`docs/SPEC.md`/`docs/TYPES.md` + D-APP-38 corpus bump), activation
    packets (D-APP-54; piping next-free D-XX, start-gated on the recorded
    suspension declaration + SHA), kernel ratification after both R0s. No
    register row changed this tranche. Branch-first + PR; no self-merge.
  - Checks: self-check severities match pins (REVIEW 27, WARN 6); practitioner
    pytest 263 passed/1 skipped; git diff check pass; frontend gates skipped —
    docs/plans-only tranche, no runtime source changed.

- **2026-07-11 — Receipt 8** (original-author review feedback incorporated into both concordance plans and the DRAFT kernel; owner-quote provenance completed).
  - Start: clean branch `claude/concordance-author-feedback-2026-07-11` off
    `516d6de39` (= `main` at the PR #172 merge); newest prior receipt
    Receipt 7.
  - Owner direction (2026-07-11, in-session, Ryan Tufts), verbatim: "Consider
    this feedback.  Incorporate what has merit." — given with the original
    plan author's review of the PR #172 revisions. Scope note: the two writes
    outside `projects/chirality-app-dev/**` in this tranche — the piping plan
    and the root kernel — are exactly the documents that review addresses and
    execute under this direction; no other outside surface touched.
  - Provenance completion (the review's Receipt-7 finding, accepted): the
    lifecycle propositions Receipt 7 summarized as session-settled are here
    quoted verbatim so each carries its actual authority class.
    - Owner-authored (2026-07-11, in-session, verbatim): "i suggest that the
      primary trigger for checking of a deliverable is what there is no more
      warranted ## Remaining Work."
    - Owner-authored ruling on the three sharpenings (2026-07-11, in-session,
      verbatim): "1. I accept this. 2. No, I disagree. Until the owner
      conducts the review the deliverable is still IN_PROGRESS. That review
      is internal to the claims the deliverable makes about itself. The
      decision to move to CHECKING means no more changes to that deliverable,
      but CHECKING can be reversed to IN_PROGRESS, whereas once something is
      ISSUES, changes trigger a different change management process that
      needs follow `AGENT_SCOPE_CHANGE.md` or similar. Just my thoughts, you
      can disagree. 3. I agree."
    - Owner acceptance of framework recommendations (2026-07-11, in-session,
      verbatim): "So what do you recommend in the first matter? And in this
      second matter I do indeed intend this to be part of Chirality itself,
      and you may proceed as you recommend."
    - Classification of record: the no-deferral-carve-out rule, the
      CHECKING-freeze/reversal semantics, the ISSUED scope-change boundary,
      and warranted-empty-as-primary-trigger are owner-authored (quotes
      above). The "change regime" phrasing, the singular-trigger framing
      (now superseded), and the three-home run-state model are agent
      framework recommendations accepted by the owner via the third quote —
      not owner-authored formulations. Surfaces updated accordingly.
  - Executed (adjudication: all review corrections accepted, one with a
    correction — the no-deferral rule was not unsupported, only unquoted;
    remedied by this receipt rather than by downgrading the rule): both
    plans and the kernel reformulate lifecycle as governed production and
    change-control regimes with maturity/readiness entry conditions (not
    percentage-complete scores; maturity meaning restored); CHECKING entry
    restructured as layered — warranted-empty universal minimum + current
    source-state-bound basis, candidate-specific declared basis (emergent,
    profile-hardened), human declaration and freeze; explicit start-gate
    precondition that the separately ruled canonical lifecycle-semantics
    amendments merge to `main` before concordance discovery; app plan
    "at minimum pushed" corrected to merged-to-`main` before dispatch;
    activation rulings pin the plan revision (commit SHA) as the run's
    execution method; DepClosure/DAG snapshots reframed as provenance
    baselines re-verified at R0/R1; kernel normalization table splits shared
    method from project adoption record; attribution relabeling per the
    classification above. Two fable TASK agents (one per plan) +
    orchestrator-authored kernel revision and this receipt.
  - Gate outcome: no register row changed; no `_STATUS.md` transition; no
    fence crossed. The parked owner-gated acts from Receipt 7 stand
    unchanged. Branch-first + PR; no self-merge.
  - Checks: self-check severities match pins (REVIEW 27, WARN 6); practitioner
    pytest 263 passed/1 skipped; git diff check pass; frontend gates skipped —
    docs/plans-only tranche, no runtime source changed.

- **2026-07-11 — Receipt 9** (root canon ratified out of DRAFT by owner act; PR #173 merged on direction).
  - Owner direction (2026-07-11, in-session, Ryan Tufts), verbatim: "You can
    now take all the `docs/` out of the DRAFT state, making them
    authoritative.  And then merge PR #173." Scope note: the root `docs/`
    writes in this tranche execute under that direction.
  - Executed: `docs/CONTRACT.md`, `docs/DIRECTIVE.md`, `docs/SPEC.md`,
    `docs/TYPES.md` status blocks flipped DRAFT → RATIFIED (owner
    ratification 2026-07-11), each preserving its provenance and recording
    the D-GOV-05 / D-GOV-02 / D-GOV-08 partial ratifications as subsumed
    history; `docs/DELIVERABLE_CONCORDANCE_METHOD.md` ratified — the
    Revision-0 self-declared R0-calibration gate superseded by the owner
    act, post-ratification precedence recorded (kernel governs the shared
    method; project plans govern project-specific adoption parameters;
    conflicts surfaced, never precedence-invented); thesis appendix A's
    present-tense DRAFT restatement updated. `docs/PLAN.md` was already
    ACTIVE (maintainer-adopted 2026-07-01) — no change.
  - Surfaced, not executed (outside this direction's scope): the
    practitioner harness hardcodes the D-GOV-05 partial-basis invariant
    labels (`harness_common.py` RATIFIED_INVARIANTS /
    DRAFT_INVARIANTS_EXPLICIT; findings still annotate e.g. "K-CONFLICT-1
    (DRAFT)"). Updating that map to full ratification is a small follow-up
    tranche touching harness code + fixtures, with D-GOV-05 as the cited
    prior authority. Also noted: ratification makes the CURRENT SPEC/TYPES
    lifecycle text authoritative; the parked lifecycle-semantics amendment
    now amends ratified canon (unchanged as a parked owner-gated act, and
    both concordance plans' start gates already require it to merge first).
  - Gate outcome: ratification is the owner's act — this tranche transcribes
    it; no register row changed; no fence crossed. PR #173 merged on the
    direction quoted above (merge is recorded in the PR/git history).
  - Checks: self-check severities unchanged (REVIEW 27, WARN 6; GEN-4 facts
    now quote the RATIFIED status lines); practitioner pytest 263 passed/1
    skipped; git diff check pass.
