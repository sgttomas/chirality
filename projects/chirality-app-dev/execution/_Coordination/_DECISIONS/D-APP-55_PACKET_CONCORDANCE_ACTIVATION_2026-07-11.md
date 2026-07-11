# D-APP-55 — PROPOSAL: Concordance Program Activation (deliverable–implementation reconciliation, run R0 onward)

> **Epistemic status: agent-authored PROPOSAL packet — not authority (K-AUTH-1; D-GOV-04).**
> Prepared 2026-07-11 by the app-dev work loop (Claude Fable 5 session, worktree branch
> `claude/concordance-activation-packets-2026-07-11`) under the owner's 2026-07-11 ruled
> sequence, step 4. Nothing here authorizes work; only an owner ruling recorded in a
> `D-APP-55_RULING_*.md` record does. Options are presented owner-first; the recommendation
> is non-binding. The activation RULING itself is NOT granted by this packet — the register
> row lands `AWAITING_RULING`.

## 1. Decision to be ruled

Whether to **activate the deliverable–implementation concordance program** — run R0
discovery onward — under
`plans/PLAN_2026-07-10_deliverable_implementation_reconciliation.md` as the run's
execution method, and at what scope (whole-corpus vs named package subset). The plan is
a non-governing method record (its own §3/§3b statement); it has no authority to activate
or select work. This decision is the §3b activation vehicle: a new decision-register row
whose owner ruling names the activated scope. The plan's §3b expected this row as
`D-APP-54`; the rebaseline transcription minted first, so activation is **D-APP-55**
(displacement recorded in `D-APP-54_RULING_2026-07-11.md` and the D-APP-54 register row).

## 2. What this decision blocks

Concordance discovery R0 (method calibration) and everything downstream in the plan:
R1 read-only inventory, R2 package concordance waves, R3 cross-package synthesis, the R4
human decision gate, R5 authorized repair tranches (each separately gated at R4
regardless), and R6 backcheck/closeout. The 53 packet-time bootstrap `## Remaining` items
seeded with this packet carry the suffix `(gated: D-APP-55)` and are not selectable until
the ruling flips them.

## 3. Precondition status (plan §4 start gate), with evidence

Both §4 governance preconditions are discharged on `main`:

1. **Lifecycle-semantics amendments merged to `main`** (§4 item 2, the §3a start-gate
   precondition): PR #174, merge commit `b618ab7d8` — root + app-dev `docs/SPEC.md` §4.4
   regime model and `docs/TYPES.md` §5 amendment, plus the D-APP-38 authority-corpus bump
   to v6 (branch commits `a9fb1af4a`, `e925fb9ef`). Amended canonical semantics now
   govern; the "current canonical semantics govern until they land" stop condition no
   longer applies.
2. **One-time rebaseline transcribed and executed** (§4 stop condition "a corpus still
   showing pre-rebaseline `CHECKING` states"): D-APP-54 ruling record
   (`execution/_Coordination/_DECISIONS/D-APP-54_RULING_2026-07-11.md`) transcribed and
   the 53-file tranche executed — PR #175, merge commit `6ba158933`. Live corpus verified
   at packet time from this worktree (branched from `6ba158933`): **53/53 deliverables
   `IN_PROGRESS`**, zero `CHECKING`. The stop condition is discharged.

Remaining §4 items (owner authorization = this ruling; bootstrap items recorded =
seeded with this packet, §8 below; run-time items 4–8 = R0/R1 acts under the ruling) are
either satisfied by this packet's tranche or execute only after the ruling.

## 4. Options

### Option A — Whole-corpus activation: all 53 deliverables (recommended)

Activate the program over the full corpus, `PKG-00` through `PKG-10`, all 53
`1_Working/DEL-*` deliverables.

- **Why:** the D-APP-54 rebaseline covered all 53 deliverables, and the plan's census
  and QA criteria are corpus-wide (§10: "100% of live deliverables and current
  requirement IDs are indexed"; R3 cross-package synthesis and the §6 unmapped-
  implementation sweep are only meaningful over the whole corpus). A subset activation
  would leave R1/R3 run-level artifacts structurally incomplete and force a second
  activation ruling later.
- **Scope note:** activation is not execution order. R0 calibrates on the
  owner-authorized calibration deliverable(s) first (plan recommends `DEL-02-01` as
  first sample without making it selectable), and R2 proceeds in bounded package waves;
  whole-corpus activation authorizes the program's coverage, not a simultaneous sweep.

### Option B — Named package subset(s)

Activate over one or more named packages (e.g. the runtime spine `PKG-03`..`PKG-06`
only). The ruling must name the packages; only those deliverables' bootstrap gates flip,
and the others stay `(gated: D-APP-55)` pending a widening ruling.

- **Why one might:** bounds owner review surface at R4; limits concurrent-session
  contention.
- **Costs:** R1 inventory and R3 synthesis lose corpus completeness (cross-package
  findings against out-of-scope deliverables can only be recorded, not processed);
  §10 completion criteria become unreachable without a follow-on activation; the
  unmapped-implementation census (implementation with no deliverable owner) is
  unreliable when the deliverable universe is partial.

The recommendation in §10 is non-binding and is disclosed as such.

## 5. Pinned method revision (ruling-record requirement)

Per §3b, the plan has no authority of its own; the activation ruling may incorporate a
pinned revision of the plan as the run's execution method. **The ruling record must
therefore pin the exact plan revision — a commit SHA on `main` — under which the run
executes.** The 53 bootstrap items are seeded with the plan's literal `<commit SHA>`
placeholder; on ruling, the executing loop supplies the pinned SHA (the `main` commit
carrying the ruled plan revision) in the ruling record and in the bootstrap items' source
citations. Later plan edits do not change the method of an in-flight run absent a new
ruling.

## 6. HARD RULE — merge to `main` before any dispatch

Restating §3b verbatim in effect: **the ruling record and register flip must be merged to
`main` before any dispatch — a branch push is not landing on `main`, and there is no
weaker fallback.** Sessions are concurrent and mutually blind; an owner act not yet in
the shared tree caused a real governance collision on 2026-07-10 (two sessions produced
contradictory owner-attributed D-APP-53 states — see that packet's §8 sequencing note).
No concordance session may be dispatched until the D-APP-55 ruling record, the register
row flip to RULED, and the bootstrap gate flips are on `main`.

## 7. Run mechanics summary (plan §3b — for the ruling reader; the plan text governs)

- **Run folder:** `execution/_Reconciliation/DeliverableConcordance/<RunID>/`, created as
  the specifically authorized immutable evidence run (§4 item 8); artifact contract per
  §9 (`RUN_BASIS.md` … `RUN_SUMMARY.md`, append-only, immutable, source-state-bound).
  Evidence artifacts are not queues or selection surfaces; no new `_LATEST.md`, standing
  pointer, register, or status surface absent a separate ruling.
- **Run-level phases:** R1 inventory, R3 synthesis, and R6 backcheck have no owning
  deliverable and need none — they execute directly under this activation ruling as
  ruled-program work (F-APP-5's "without an owner ruling" is satisfied by the ruling
  itself; precedents: DRQ-11 repo-wide snapshot under D-APP-53, DepClosure and
  ScopeClosureAudit runs). R0, R2, and R5 attach to the owning deliverables' seeded
  `## Remaining` items.
- **Three homes of program state** (no control deliverable is created):
  1. one run's phase state — the immutable run folder;
  2. cross-session open/closed visibility — this activation register row's
     ruling-record cell, checked at every loop Step 0 (D-APP-53's row carrying
     execution state is the precedent);
  3. the recurring process asset — checking-entry profiles and maturity feedback, a
     docs profile file beside `docs/ISSUE_READINESS_PROFILES.md`, adopted and amended
     by ruling per the D-APP-34 pattern.
- **Selection unchanged:** selection remains the standing loop's act over
  deliverable-local `## Remaining` items (§11); this plan and this packet select no work.

## 8. Packet-time bootstrap seeding (executed with this packet, per §3b)

§3b prescribes: "At packet time, each in-scope deliverable's `_STATUS.md`
`## Remaining` is seeded with the bootstrap item, in exactly this format." This packet's
tranche therefore seeds all 53 deliverables (the whole corpus is in scope at packet time;
a subset ruling simply leaves the out-of-scope gates unflipped) with:

```
- Run claim-level concordance per the reconciliation method (source: plans/PLAN_2026-07-10_deliverable_implementation_reconciliation.md §§6–8 at pinned main revision <commit SHA>) (gated: D-APP-55)
```

`<commit SHA>` is the plan's literal placeholder, supplied at ruling time per §5. 43
files receive a new `## Remaining` section (placed before `## History` per the existing
10-file precedent); 10 files receive an appended item. Each seeded file also gets one
non-state-bearing `History` line ("Remaining item added: … no state change."), following
the 2026-07-10 "Remaining section added: … no state change." precedent; the line is
parser-verified non-state-bearing under prose-bullet-v1 (drift baseline stays 0/53). No
existing `Remaining` item, suffix, header field, `Current State`, or `Last Updated` is
touched — no lifecycle transition occurs.

## 9. Risks and validation implications (per the Decision Preparation Rules)

- **Discovery is read-only.** R0–R3 produce run-folder evidence artifacts only; they do
  not edit deliverable documents, source, or tests (§8/R1 "Read-only inventory"; R2
  "does not edit deliverable documents").
- **Repair waves are separately gated.** R5 executes only after R4 dispositions are
  ruled or directed and the work is recorded in the owning deliverable's `## Remaining`;
  this ruling does not pre-authorize any repair.
- **No lifecycle transitions occur under discovery.** Lifecycle rows can only recommend
  (`LIFECYCLE_REASSESSMENT_REQUIRED`); R6 verifies "lifecycle states were unchanged
  unless separately authorized". F-APP-4 (issuance) is untouched.
- **Validation gates unchanged.** Practitioner-harness pytest, repo self-check, corpus
  status, and the frontend gates keep their existing contracts; the seeding tranche was
  verified against them (drift baseline 0/53 intact). Discovery adds no new capability
  surface, no F-APP-1/2/3 crossing, no agent-workflow edits (`DEFERRED_AGENT_WORKFLOW`
  rows go to the evidence-only observations artifact).
- **Residual risks:** over-claiming at R2 (mitigated by the §6 evidence columns and §10
  reviewer spot-check); concurrent-session contention (mitigated by the §6 HARD RULE and
  §4 item 7 defer-don't-race); stale inputs if the corpus changes mid-run (`STALE_INPUT`
  rerun rule, plan §4 tail).
- **Affected files (this packet's tranche):** this packet; the register row
  (`execution/_Coordination/_DECISIONS/_REGISTER.md`); 53
  `execution/PKG-*/1_Working/DEL-*/_STATUS.md` bootstrap seedings. On ruling: the ruling
  record, the register flip, the 53 gate/SHA flips, then run-folder artifacts under
  `execution/_Reconciliation/DeliverableConcordance/<RunID>/`.

## 10. Recommendation (non-binding)

**Option A — whole-corpus (all 53 deliverables).** The rebaseline covered all 53, the
plan's census and QA criteria are corpus-wide, and activation cost does not scale with
scope (execution proceeds in R0-calibrated bounded waves regardless). Disclosed as a
non-binding agent recommendation; the owner may rule Option B with named packages, or a
custom disposition.

## 11. On-ruling mechanism

An in-session owner ruling — "D-APP-55: <scope>" with any riders — suffices. The
executing loop then:

1. transcribes the ruling verbatim into a `D-APP-55_RULING_*.md` record, supplying the
   pinned plan revision SHA per §5;
2. flips the register row to RULED (ruling-record cell per the register's conventions,
   carrying open/closed run visibility per §7 home 2);
3. flips the 53 (or the ruled subset's) bootstrap items — `(gated: D-APP-55)` per the
   D-APP-53 packet §7 mechanism precedent — and substitutes the pinned SHA into their
   source citations; and
4. lands all of the above on `main` (branch-first + PR unless the ruling grants a
   recorded commit discipline) **before dispatching any concordance session** (§6 HARD
   RULE).
