# Work Loop — session init and generic loop

You are resuming, as the next bounded operator, the work loop that lives in
this file's directory. This file carries the protocol, the fences, the
checks, and the pointer index. It carries **no status, no history, and no
work**. Work lives only in the deliverable folders
`execution/PKG-*/1_Working/DEL-*/`, in each `_STATUS.md` `## Remaining`
section; current state is re-derived from the live tree every iteration.
This text is orientation, **not authority**: owner rulings and directions
authorize work; sources govern on any disagreement.

## 1. Bootstrap

- Resolve `REPO_ROOT` with `git rev-parse --show-toplevel`; work from there.
  `WORKING_ROOT` is `projects/chirality-app-dev`.
- Handoff context (chat-only owner directions, gate outcomes, stale-map
  deltas) lives in `LOOP_RECEIPTS.md` beside this file; its local rules
  govern what a receipt may contain.

## 2. Where live work is re-derived (pointer index; never a status surface)

- **Work surface:** `execution/PKG-*/1_Working/DEL-*/` — `_STATUS.md`
  (lifecycle + `## Remaining`), `MEMORY.md`, `ScopeOfWork.md` or legacy
  four-document kits, `Dependencies.csv` / `_DEPENDENCIES.md`,
  `_run_records/**`.
- **Ruled records:** decision register
  `execution/_Coordination/_DECISIONS/_REGISTER.md` (packets and ruling
  records beside it; open rows are the owner-gated surface) ·
  `execution/_Coordination/_COORDINATION.md` · discovery pointer
  `execution/_Coordination/_LATEST.md` · v3 owner rulings and steers under
  repo-root `plans/steers/` (transcription sources, not authority).
- **Delegation instrument:** D-APP-60 as refined by D-APP-64 §5.
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
  `execution/_Coordination/NEXT_INSTANCE_PROMPT.md` · every superseded
  `loop/WORKPLAN_*.md`.

## 3. Standing constraints — hard fences (all iterations; always stop for a human ruling)

- **F-APP-1 (provider/network):** no provider or network expansion beyond
  the Anthropic path; no remote MCP, plugin, or broad tool-search enablement
  without a fresh ruling (F1 as amended by D-APP-44: owner-permitted,
  default-closed provider/residency configuration).
- **F-APP-2 (release/distribution):** no signing, notarization, publication,
  external distribution, or release-readiness / professional / certification
  claims.
- **F-APP-3 (domain-engine boundary):** domain-engine work happens only
  inside what the tier-0 bridge loop's ruled decisions grant (the `D-APP-4x`
  F-series rows); this loop never writes `_DomainEngines/**` or piping
  surfaces, and never advances integration level, live binding, or
  apply-class tool exposure on its own authority.
- **F-APP-4 (issuance):** no `CHECKING -> ISSUED` lifecycle issuance.
- **F-APP-5 (single-surface rule; owner-adopted 2026-07-10):** work items
  live in deliverable folders (`_STATUS.md` `## Remaining`); owner decisions
  live in `execution/_Coordination/_DECISIONS/_REGISTER.md`; no new standing
  plan, queue, register, or status surface is created without an owner
  ruling. `plans/` is a historical archive; never select work from it.
- **Fresh-ruling stops** (carried from the pre-consolidation coordination
  record): Pi-backed execution (unapproved after D-APP-01/02); concrete
  non-Anthropic provider implementation or routing; write/edit/bash/
  tool-execution exposure beyond the current approved item; changes to the
  project-truth model for sessions, transcripts, chats, runtime logs, or
  completion logs; professional-boundary or release-readiness posture.

Any change to fence wording is an owner act.

## 4. The workplan is an optional overlay

A `WORKPLAN_*.md` beside this file narrows and orders. It never holds a
`Remaining` item, never widens authority, and never relaxes a fence or gate
named here; a clause that would is void and is reported as a stale-map
delta. When the plan is silent, this file governs. (D-APP-105.)

Plan selection is from committed `HEAD`, never the working tree (D-APP-64):
the Step 0 line below selects the bytewise-last `loop/WORKPLAN_*.md` in the
`HEAD` tree and reads it with `git show`. An untracked, staged-only, or
worktree-only file is never selectable. No committed plan means the loop
runs on the deliverables alone and the receipt says so (D-APP-106). Ruled
plans are immutable; a change is a new dated file.

## 5. The loop protocol (every iteration)

### Step 0 — Discover

Run from `REPO_ROOT`:

```bash
git status --short && git log --oneline -20
python3 tools/validation/validate_app_dev_loop_receipts.py --repo-root .
p=$(git ls-tree --name-only HEAD projects/chirality-app-dev/loop/ | grep -E '/WORKPLAN_.*\.md$' | LC_ALL=C sort | tail -1); [ -n "$p" ] && git show "HEAD:$p" || echo "no committed plan: deliverables alone"
tail -60 projects/chirality-app-dev/loop/LOOP_RECEIPTS.md
grep -n "AWAITING_RULING\|PROPOSAL" projects/chirality-app-dev/execution/_Coordination/_DECISIONS/_REGISTER.md
ls projects/chirality-app-dev/execution/_Coordination/NOTICE_* 2>/dev/null
cd projects/chirality-app-dev && PYTHONDONTWRITEBYTECODE=1 python3 execution/_Reconciliation/References/reconcile_authority_corpus.py status; cd -
grep -l '^## Remaining' projects/chirality-app-dev/execution/PKG-*/1_Working/DEL-*/_STATUS.md
PYTHONDONTWRITEBYTECODE=1 python3 tools/practitioner_harness/harness.py status --project projects/chirality-app-dev
PYTHONDONTWRITEBYTECODE=1 python3 tools/practitioner_harness/harness.py self-check
```

Rules the output does not show you:

- A receipt-validator failure blocks use of the ledger until it is repaired
  through its governed path.
- Rulings newer than the last receipt, and routed Root notices, are how work
  unlocks; this loop never writes Root surfaces.
- Verify before relying: plans, receipts, dated assessments, and your own
  tasking are maps with citations. Open the cited source; on disagreement
  the live tree wins and the delta goes in the receipt, never into the map.
- If the plan pins a reference by hash, recompute it and stop on a mismatch.
- A tranche that will touch `frontend/` declares at Step 0 the A1 re-stage
  consequence (`plans/steers/chirality_app_v3_app_ruling_record_a1_2026-08-23.md`
  lines 28-36) in its run record and receipt.

### Step 1 — Select, from `## Remaining` sections only

A `Remaining` item (deliverable `_STATUS.md`, §2) is selectable when it
carries no `(gated: ...)`, `(stage-gated: ...)`, or `NOT_SELECTABLE_UNTIL:`
marker, or its named gate or act is observable on `main` (a ruling record,
a routed Root notice, or a merged act). Blockedness beyond gates is
re-derived from the deliverable's `Dependencies.csv` / `_DEPENDENCIES.md`
and the accepted DepClosure snapshot (§2), never from a hand-maintained
summary. Precedence: (a) repair failing
validation on landed work; (b) work that discharges a gate prerequisite;
(c) owner-directed over agent-inferred; (d) the plan's focus and order;
(e) the highest-value ungated item. Apply CONTRACT **K-ENGINE-6** to every
item: standalone-harness or feature-parity work is off-strategy. Never
manufacture work outside recorded `Remaining` scope or revive a ruled-shut
item (a revival takes a new register row).

Judgment-shaped forks are triaged under the D-APP-64 §5 contract (fast-reject
boundary first, then the selection method and attribution schema); D-APP-60
is the underlying instrument.

### Step 2 — Brief or slate

Material or hard-to-reverse forks (a fence question, a K-ENGINE-6 strategy
fork, a costly public-contract or data-migration change, an item marked as
needing its own packet) get a `PROPOSAL` packet in the decision register.
Ordinary forks inside the fences are decided by the agent and recorded per
D-APP-64 §5.3. Deliverable work gets CANDIDATE brief(s); coordination work
gets a decision slate (options, non-binding recommendation, on-ruling
mechanism).

### Step 3 — Gate

STOP at the hard fences (§3) and at owner acts: adoption, ruling, and
direction are the owner's (K-AUTH-1; D-GOV-04). Ambiguity about whether a
fast-reject boundary is touched is itself owner-class. In-session directions
are recorded verbatim in their governed artifact; chat-only directions with
no governed home go in the receipt, labeled evidence rather than ruling.
Record every gate outcome, including no-ops and their reason.

### Step 4 — Execute and check

Branch-first plus PR; never self-merge; one branch, one PR, one receipt,
owner merge per iteration; write scope stays inside
`projects/chirality-app-dev/**` unless the owner grants wider scope. An
adopted-but-unexecuted brief is live authority. Run the checks for the work
type (§8) and, for evidence items, meet the §9 bar. The independent-review
path, the APP-HOLD-1 preflight, the host-capability rule, and git closeout
discipline are in `AGENTS.md` beside this project.

### Step 5 — Closeout

Write deliverable-local state: `_STATUS.md` (`Remaining` updated to what
landed and what remains; lifecycle transitions only through ruled gates;
`**Checking Approval SHA**` discipline intact), `MEMORY.md`,
`_run_records/**`; landed narrative goes to `plans/PLAN_COMPLETION_LOG.md`.
Append one receipt to `LOOP_RECEIPTS.md` per its rules and rerun the receipt
validator before commit. The next iteration starts at Step 0.

## 6. First return from Step 0

Your first substantive output is a live orientation return, not a recap of
this file: the git state and newest applicable receipt; the owner directions
and register gates that matter now; the plan's focus, if any; the widest
lawful tranche(s) open; any parked lane and the owner act that unparks it.
If the loop is parked pending owner direction, stop there.

## 7. Default posture (a per-run steer may override; the gate may not)

- Select the widest lawful tranche(s), re-derived each iteration; execute
  independent nodes concurrently; a failed check is a repair loop, not a
  terminal state; each ordinary iteration reduces at least one accepted
  deliverable obligation. Pressure never weakens a gate, evidence bar, fence,
  ownership boundary, or write locus (Root R17-E as carried by A12).
- When only owner decisions remain, present a slate and stop; never
  manufacture lower-value work to stay busy.
- Truthful attribution: agent decisions are recorded as the agent's own;
  never write a ruling record or `RULED` row for an act that did not occur.

## 8. Checks by work type

| Work type | Required before push | Notes |
|---|---|---|
| Any tranche | repo-wide `self-check` exit 0; practitioner-harness pytest at closeout; receipt validator pass before and after appending; `git diff --check` | Always. |
| Product source (`frontend/src/**` outside `__tests__/**`, `frontend/electron/**`, `frontend/packages/**`, `frontend/scripts/**`, build/packaging config) | typecheck + vitest + build/premerge gates (`docs/VALIDATION_STRATEGY.md`, `docs/RELEASE_QUALITY_GATES.md`, `docs/BUILD_AND_RELEASE.md`); independent review per `AGENTS.md`; A1 re-stage declaration | Stop the dev server before build/package/premerge commands. |
| UI work | the above plus the D-APP-36 render bar (`docs/ISSUE_READINESS_PROFILES.md` §4) | Evidence per `docs/ui/UI_POLISH_EXECUTION_PLAN.md`. |
| Authority docs (`docs/DIRECTIVE.md`, `CONTRACT.md`, `SPEC.md`, `TYPES.md`) | D-APP-38 corpus reconciliation (`execution/_Reconciliation/References/reconcile_authority_corpus.py`) | Drift is repair-first. |
| Governance / control-plane only | record that frontend gates were skipped because no runtime source changed | |
| Any dispatch | APP-HOLD-1 preflight (`AGENTS.md`) | Every time. |
| Host-only surfaces | per-command escalation per `AGENTS.md` "Host-capability execution" | Park `HOST_RERUN_REQUIRED` only when escalation is declined. |

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
their message, or a line below), honor it over §7's defaults and on top of
the plan; this file still governs the protocol, the fences, and the gate.
Historical receipts cite the section numbers of the revision current when
they were written: "LOOP_INIT §7 defaults" is the former session-conventions
section quoted verbatim in D-APP-61; §1 to §10 of receipts before D-APP-112
refer to the D-APP-105 text in git history.
