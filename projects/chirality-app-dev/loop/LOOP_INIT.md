# Work Loop — session init and generic loop

You are resuming, as the next bounded operator, the work loop that lives in
this file's directory. This file is the loop: it carries the protocol, the
default posture, the standing constraints, the evidence contract, the checks
by work type, and the pointer index. It carries **no status, no history, and
no work**. Work lives only in deliverable folders. Current state is
re-derived from the live tree every iteration.

Treat this text as orientation and protocol, **not authority**: owner
rulings and directions authorize work; this file never does. Sources govern
on any disagreement.

## 1. Bootstrap

- Resolve `REPO_ROOT` with `git rev-parse --show-toplevel`; work from there.
- The loop's standing surfaces resolve relative to this file's own directory.
- Handoff context (owner directions given outside governed artifacts, gate
  outcomes, stale-map deltas) lives in `LOOP_RECEIPTS.md` beside this file,
  whose local rules govern what a receipt may contain.

## 2. The workplan is an optional overlay

A `WORKPLAN_*.md` beside this file **narrows and orders**. It may name the
owner's current focus, an order among selectable items, temporary
constraints for a period, and pointers. It **never holds a `Remaining` item,
never widens authority, and never relaxes a fence or a gate** named here;
any clause that would do so is void and is reported as a stale-map delta.
When the plan is silent, this file governs. When the plan names a focus,
work inside that focus first and record why anything outside it was taken.
Discovery does not depend on the plan: the work surface is always the
deliverables' `## Remaining` sections (Step 0). (D-APP-105; it reverses
the D-APP-61 M2-A / D-APP-64 arrangement in which the plan carried the
protocol.)

Plan selection is from committed `HEAD`, never the working tree (D-APP-64):
from `REPO_ROOT`, enumerate the `HEAD` tree entries under
`projects/chirality-app-dev/loop/`, keep basenames matching
`^WORKPLAN_.*\.md$`, sort them bytewise (`LC_ALL=C`), and select the last.
Require the selected path to resolve to exactly one `HEAD` tree entry of
mode `100644`, type `blob`, and read the plan bytes only with
`git show HEAD:<path>`. An untracked, staged-only, or worktree-only filename
is never selectable. If no committed plan exists, the loop runs on the
deliverables alone and the receipt says so (D-APP-106). If a plan exists but
validation or committed-byte reading fails, stop before Step 0 and report
the loader failure; never silently select an older plan. Ruled plans are
immutable; a change is a new dated file.

## 3. The loop protocol (every iteration)

### Step 0 — Discover (mandatory core)

Run from `REPO_ROOT` unless stated; `WORKING_ROOT` is
`projects/chirality-app-dev`.

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

What each line establishes, and the rules attached:

- **Git state and branch awareness.** Log since the last receipt. Concurrent
  loops may be live in this monorepo: keep write scopes disjoint from
  `_DomainEngines/**`, `projects/chirality-piping/**`, `projects/pec/**`, and
  treat unrelated dirty files as external state.
- **Receipt validator, then the latest applicable receipt(s).** A validator
  failure blocks use of the cursor until the ledger is repaired through its
  governed path.
- **Committed plan bytes** (§2), if any. Apply its focus and order; nothing
  else.
- **Decision register.** Rulings newer than the last receipt are how work
  unlocks. Look every time.
- **Routed Root notices** under `execution/_Coordination/NOTICE_*`. Root
  acceptances arrive here; they are how `NOT_SELECTABLE_UNTIL` states
  resolve. This loop never writes Root surfaces.
- **D-APP-38 corpus check.** Any drift is repair-first work under selection
  principle (a), regardless of which tranche introduced it.
- **Work surface.** Every `_STATUS.md` with a `## Remaining` section is open
  scope; an absent section means no recorded open scope for that
  deliverable. Lifecycle posture comes from the harness `status` command.
- **Repo-wide `self-check`.**
- **Verify before relying.** The plan, the receipts, any dated assessment,
  and your own tasking are maps with per-claim citations, not authority.
  Before relying on a derivative statement, open its cited source in the
  live tree; on disagreement the live tree wins and the delta goes in the
  receipt, never into the map.
- **Frontend preflight (A1 re-stage rule).** Whenever a tranche will touch
  any path under `frontend/`, declare at Step 0 that any mutation under
  `projects/chirality-app-dev/frontend/` invalidates the staged R20
  procedure for any future proof claim and requires a newly staged revision
  and a fresh owner-executed proof
  (`plans/steers/chirality_app_v3_app_ruling_record_a1_2026-08-23.md` lines
  28-36). The declaration is recorded in the tranche's run record and
  receipt.
- **Pin preflight.** If the plan pins a reference by hash, recompute the hash
  and stop if it differs.

### Step 1 — Select, from deliverable folders only

A `Remaining` item is *selectable* when it carries no `(gated: ...)` /
`(stage-gated: ...)` suffix and no `NOT_SELECTABLE_UNTIL:` state, or its
named gate is ruled or its named act has occurred on `main`. Blockedness
beyond gates is re-derived from deliverable-local `Dependencies.csv` /
`_DEPENDENCIES.md` and the accepted DepClosure snapshot
(`execution/_Reconciliation/DepClosure/_LATEST.md`); never from a
hand-maintained summary. An item is *executable* only when its accepted
Scope of Work, lifecycle, exact dependencies, named gates, check surface, and
write locus all permit execution. An item whose gate is a Root acceptance, a
Root implementation act, a held DEL-02-06 binding, an owner act, or a
release act stays parked until that gate or act is observable on `main` (a
routed Root notice, a ruling record, or a merged act).

Principles, in order: (a) repair failing validation for already-landed work
before new scope; (b) work that discharges a gate prerequisite beats work
that doesn't; (c) owner-directed items beat agent-inferred ones; (d) the
plan's focus and order, if any; (e) the highest-value ungated `Remaining`
item. Apply the CONTRACT **K-ENGINE-6** strategic lens to every item:
Chirality is a governance/UI/audit/lifecycle/adapter layer over provider
harness mechanics; standalone-harness or feature-parity work is
OFF-STRATEGY. Never manufacture work outside the recorded `Remaining` scope
or revive ruled-shut items (a revival takes a new register row).

*Delegation triage (D-APP-60, refined by D-APP-64).* Before slating any
judgment-shaped fork, apply the class test with fast-reject ordering: any
touch of a recorded limit is owner-class immediately, no lens analysis; the
adversarial four-lens test runs only on survivors. Items that touch a
fast-reject boundary are slated in near-miss form naming the touched
boundary. Among surviving defensible alternatives the agent selects and
advances the one outcome it judges most consistent and coherent across the
four lenses, recording a concise rationale and materially important rejected
alternatives. The asymmetry that governs the default: over-slating costs
owner attention; over-deciding silently converts owner authority; only the
first is cheap to recover from.

### Step 2 — Brief or slate

Genuinely material or hard-to-reverse forks (a hard-fence question, a
K-ENGINE-6 strategy fork, a costly public-contract or data-migration change,
any `Remaining` item marked as needing its own decision packet) get a
`PROPOSAL` packet registered in the decision register. Within the fences,
ordinary design forks are resolved with recorded agent decision latitude:
under the D-APP-60 instrument as refined by D-APP-64 for disposition-class
items (decide, record the rationale artifact, cite the exercise in the
receipt), per-instance latitude otherwise. For deliverable work, generate
CANDIDATE brief(s); for coordination/control work, present a decision slate
(options + non-binding recommendation + on-ruling mechanism).

### Step 3 — Gate

STOP at the hard fences (§6) and at owner-shaped acts. **Adoption, ruling,
and direction are the owner's acts** (K-AUTH-1; D-GOV-04); no command and no
agent performs them. The STOP applies to owner-class items;
disposition-class items proceed under the D-APP-60 method binding and
verifier as refined by D-APP-64: ambiguity about whether a fast-reject
boundary is touched is owner-class; plurality of surviving defensible
outcomes is not itself owner-class. Terminus slates arrive pre-triaged in
near-miss form, each item naming the failed gate or limit. In-session
directions and rulings are recorded verbatim in their governed artifact;
only chat-only directions with no governed home are transcribed into the
receipt, labeled as evidence rather than ruling. Directions fully
recoverable from Git/PR history need no receipt transcription. Record every
gate outcome, including no-ops and their reason.

### Step 4 — Execute and check

Branch-first + PR is the default; never self-merge; write scope stays inside
`projects/chirality-app-dev/**` unless the owner grants wider scope. One
branch, one PR, one receipt, owner merge per iteration; no automatic PR
stacking. An adopted-but-unexecuted brief is live authority: execute it
unless this run's steer says otherwise. Run the checks for the work type
(§8). CI green; owner merges. The independent-review path in `AGENTS.md`
(fresh read-only `TASK + software-code-review` over 100% of the frozen diff)
is mandatory for any product-source change; the APP-HOLD-1 dispatch
preflight in `AGENTS.md` is mandatory before any dispatch. *D-APP-60
verification:* every scope named by the instrument's calibrated verification
requirement must satisfy that requirement before commit; verdicts are
recorded only after they exist, and nothing lands on `BLOCK`.

### Step 5 — Closeout: deliverable state and receipt

Closeout writes deliverable-local state: `_STATUS.md` (`Remaining` updated
to reflect what landed: landed scope removed, newly named residuals added;
lifecycle transitions only through their ruled gates; `**Checking Approval
SHA**` discipline intact), `MEMORY.md`, `_run_records/**`; landed narrative
goes to `plans/PLAN_COMPLETION_LOG.md`. Rationale artifacts for delegation
exercises live in existing homes only: deliverable-scoped in that
deliverable's `_run_records/**`; cross-cutting in the tranche's AgentRuns
record; the artifact records rejections alongside exercises. Receipt
citation convention: `Gate-Outcome` names the exercised judgment; `Pointers`
names the rationale artifact. Append one versioned minimal receipt to
`LOOP_RECEIPTS.md` per its local rules, then rerun
`python3 tools/validation/validate_app_dev_loop_receipts.py --repo-root .`;
receipt validation is a mandatory pre-commit and closeout gate. Next
iteration starts at Step 0.

## 4. First return from Step 0

Your first substantive output is a live orientation return, not a copied
plan or a recap of this file. It names: the live git state and newest
applicable receipt; the latest owner directions and register gates that
matter now; the plan's focus, if any; the widest lawful tranche(s) currently
open; any lane that is parked, and the owner action that would unpark it. If
the live state says the loop is parked pending owner direction, stop after
that return unless the owner has already provided new direction in the
current session.

## 5. Default posture (a per-run steer may override; the gate may not)

- **Pacing (calibrated development pressure; Root R17-E as carried by
  A12).** Once a deliverable item is selectable, prioritize executable
  product, test, and gate-closing engineering work. Select a bounded set of
  independent or dependency-linked nodes only when each node has an accepted
  scope, known write locus, named checks, and no unresolved owner gate.
  Execute compatible independent nodes concurrently where useful. Apply
  accepted decisions as written; do not re-plan them merely to fill an
  iteration. A failed check or required review is a repair loop, not a
  terminal node state: repair and rerun until passing unless a hard fence,
  owner ruling, or forced termination intervenes. A blocked node holds only
  its dependants; independent lawful work continues. Each ordinary iteration
  must materially reduce at least one accepted deliverable obligation.
  Evidence-only work counts when the selected obligation is itself an
  evidence gate. Coordination artifacts support the selected work but do not
  substitute for it. Work absent from accepted deliverable `Remaining` scope
  is not selectable. Development pressure never weakens a human gate,
  evidence bar, containment fence, ownership boundary, or
  truthful-attribution requirement, never turns a plan or pinned reference
  into a queue, and never broadens a write locus.
- **Ambition inside the fence.** Select the widest lawful tranche(s) now,
  re-derived, not pre-assumed; parallelize independent reads, checks, and
  preparation; let dependencies resolve as you work rather than fixing the
  whole iteration up front. Continue until every lawful path of advancement
  is exhausted except human decision.
- **Terminus.** When only human-decision items remain, present them as a
  decision slate and stop; never manufacture lower-value work to stay busy.
- **Truthful attribution** is the one firm limit of the decision-latitude
  model: agent decisions are recorded as the agent's own; never write a
  ruling record or `RULED` register row attributing to the owner an act that
  did not occur.
- **Gate state is register-derived.** Open `D-APP-XX` rows, per-item
  `(gated: ...)` suffixes, and per-item `NOT_SELECTABLE_UNTIL:` states are
  re-derived each iteration, never assumed.

## 6. Standing constraints — hard fences (all iterations; always stop for a human ruling)

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

*Observation beside the fences (agent-authored, carried from the A12 plan;
not fence text):* under F-APP-1, App `docs/CONTRACT.md` K-NET-1 names exact
accepted OpenAI account, model, and turn service endpoints for the
delegated-harness adapter; they become usable only through the gates their
carriers' `Remaining` items name, and nothing else is added. Under F-APP-2,
D-APP-97 and F-APP-2 remain active through WP-09 preparation and lift only
at G6a against the exact owner-named candidate (G0 D2). Under F-APP-5, a
pinned completion reference is cited for meaning only. Any change to fence
wording itself is an owner act.

## 7. Evidence contract for empirical, fixture, conformance, and gate-evidence items (A12; Root R17 N3)

Every such item's acceptance and return require enough durable
**non-secret** bytes for an independent verifier to recompute the claim; at
minimum, as applicable: exact input/source identities and the complete
cited-byte inventory; fixture, evaluator, validator, and adapted-source
bytes; command, arguments, cwd, relevant effective environment, tool/runtime
versions, and exit status; canonical stdout/stderr and machine-readable
results; process, filesystem, containment, and denied-egress observations;
sorted manifests and independent hash recomputation; cleanup proof for
disposable/quarantine state; and an executable or precisely bounded rerun
method. Never preserve credentials, tokens, private account material,
forbidden artifact binaries, or user-wide state. When required underlying
bytes cannot be preserved or independently recomputed, the claim remains
unavailable; a prose summary or remembered digest is not acceptance
evidence.

## 8. Checks by work type

| Work type | Required before push | Notes |
|---|---|---|
| Any tranche | repo-wide `self-check` exit 0; full practitioner-harness pytest at closeout; receipt validator pass before and after appending; `git diff --check` | Always. |
| Product source (`frontend/src/**` outside `__tests__/**`, `frontend/electron/**`, `frontend/packages/**`, `frontend/scripts/**`, build/packaging config) | typecheck + vitest + build/premerge gates (`docs/VALIDATION_STRATEGY.md`, `docs/RELEASE_QUALITY_GATES.md`, `docs/BUILD_AND_RELEASE.md`); independent review path per `AGENTS.md`; A1 re-stage declaration | Stop the local dev server before build/package/premerge commands unless the command owns the server lifecycle. |
| UI work | the above plus the D-APP-36 render bar (`docs/ISSUE_READINESS_PROFILES.md` §4) | Evidence routed per `docs/ui/UI_POLISH_EXECUTION_PLAN.md`. |
| Authority docs (`docs/DIRECTIVE.md`, `CONTRACT.md`, `SPEC.md`, `TYPES.md`) | D-APP-38 corpus reconciliation (`execution/_Reconciliation/References/reconcile_authority_corpus.py`) | Drift is repair-first. |
| Governance / control-plane only | record explicitly that frontend gates were skipped because no runtime source changed | |
| Any dispatch | APP-HOLD-1 preflight (`AGENTS.md`) | Before the dispatch, every time. |
| Host-only surfaces (packaged launch, browser proof, keychain, LaunchAgent) | run in-session under per-command escalation per `AGENTS.md` "Host-capability execution" | Park `HOST_RERUN_REQUIRED` only when escalation itself is declined. |

## 9. Where live work is re-derived (pointer index; never a status surface)

- **Work surface:** `execution/PKG-*/1_Working/DEL-*/` — `_STATUS.md`
  (lifecycle + `## Remaining`), `MEMORY.md`, `ScopeOfWork.md` or legacy
  four-document kits, `Dependencies.csv` / `_DEPENDENCIES.md`,
  `_run_records/**`.
- **Ruled records:** `execution/_Coordination/_COORDINATION.md` (ruled-record
  stub) · decision register `execution/_Coordination/_DECISIONS/_REGISTER.md`
  (`D-APP-XX` rows; packets and ruling records beside it; open rows are the
  owner-gated surface) · discovery pointers `execution/_Coordination/_LATEST.md`
  · v3 owner rulings and steers under repo-root `plans/steers/`
  (`chirality_app_v3_app_ruling_record_a*`,
  `chirality_app_v3_root_ruling_record_r*`; transcription sources, not
  authority).
- **Delegation instrument:** D-APP-60 (frozen shared block v1 + app-dev local
  bindings; supersedes D-APP-59 by reference) as refined by the D-APP-64
  reasoned-selection overlay (fast-reject boundary, selection method,
  attribution schema).
- **Dependency evidence:** `execution/_Reconciliation/DepClosure/_LATEST.md`
  · the SCA-APP-008 Gate-5 post-application audit under
  `execution/_ScopeChange/SCA-APP-008_2026-08-23_1727_V3_Release_Pathway/Phase5/Audit/`
  (warning-bearing derivative evidence) · SCC work follows repo-root
  `docs/CYCLE_DRIVEN_RESOLUTION.md`.
- **What must be built and why:**
  `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`
  (applied SCA-APP-008 Gate-5 text) · scope amendments
  `execution/_ScopeChange/_LATEST.md` · product yardstick `docs/PRD.md` ·
  strategy `docs/PLAN.md` (non-governing) · authority documents
  `docs/DIRECTIVE.md`, `docs/CONTRACT.md`, `docs/SPEC.md`, `docs/TYPES.md`.
- **Cross-loop handoffs:** routed Root notices `execution/_Coordination/NOTICE_*`
  (this loop adopts, amends, or declines under its own instruments and never
  writes Root surfaces) · APP-HOLD-1 register
  `execution/_Coordination/APP_HOLD_REGISTER.csv` · Task Management register
  `execution/_Coordination/_TaskManagement/REGISTER.csv` ·
  `_DomainEngines/bridge/LOOP_RECEIPTS.md` (scope dedup only).
- **Validation gates:** `docs/VALIDATION_STRATEGY.md` ·
  `docs/RELEASE_QUALITY_GATES.md` (§13 Shared Runtime Gate is validation
  evidence only) · `docs/BUILD_AND_RELEASE.md`.
- **Agent posture:** `AGENTS.md` (personas, dispatch contract, delegation
  posture, independent-review path, host-capability rule, closeout and git
  discipline).
- **Frontend contract surfaces:** `frontend/packages/harness-contract/**`
  (pull contract pinned at
  `execution/_Coordination/_DECISIONS/D-APP-48_FLOW_A_PULL_CONTRACT_*.json`).
- **Historical archive (never selection surfaces):** `plans/**`
  (`plans/PLAN_COMPLETION_LOG.md` holds landed narrative) ·
  `execution/_Coordination/NEXT_INSTANCE_PROMPT.md` · every superseded
  `loop/WORKPLAN_*.md` (preserved unchanged).

## 10. Per-run steer

If the owner appended a steer for this run (the launcher's `Steer` line,
their message, or a line below), honor it on top of the plan and over §5's
defaults; this file still governs the protocol, the fences, and the gate in
Step 3. Historical receipts that say a steer overrides "LOOP_INIT §7
defaults" refer to the former session-conventions section quoted verbatim in
D-APP-61.

## Appendix — provenance of the rules above (one line each; the records govern)

2026-07-04 Receipt 0 (loop created; thin launcher convention) · 2026-07-10
Receipt 5 (deliverables are the work surface; F-APP-5) · D-APP-59/D-APP-60
(decision-latitude instrument) · D-APP-61 (loop-entry instruction
separation; historical §7 mapping) · D-APP-64 (reasoned-selection overlay;
committed-HEAD loader) · A1 2026-08-23 (re-stage rule) · Root R17 / A12
2026-09-03 (calibrated pressure; evidence contract; selectability rule; one
branch, one PR, one receipt) · D-APP-105 2026-09-04 (this file carries the
generic loop; the workplan is an optional narrowing overlay; D-APP-106 makes
it optional in existence: validator and loader relaxed).
