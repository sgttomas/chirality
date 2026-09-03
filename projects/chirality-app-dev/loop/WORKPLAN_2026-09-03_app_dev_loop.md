# App-Dev Work Loop — standing plan (development loop instructions)

> **Epistemic status: agent-authored plan — not authority.** Prepared on
> 2026-09-03 as the App counterpart of Root ruling R17 under the owner's A12
> selection (`plans/steers/chirality_app_v3_app_ruling_record_a12_2026-09-03.md`);
> supersedes `WORKPLAN_2026-07-18b_app_dev_loop.md` in this directory, carried
> forward verbatim except the clauses marked *(A12)*, with the carry-forward gated
> by an independent verifier (the review over the seating PR). This plan
> never authorizes work: owner rulings and directions do. Sources govern on any
> disagreement. This file is the project's single development-loop instruction
> surface — PROTOCOL plus pointer indexes; it carries NO status, NO work
> history, and NO measurements. Each iteration re-derives state from the live
> tree; loop closes append a minimal receipt to `LOOP_RECEIPTS.md` beside this
> file (rules live at the top of that file).

## Owner intent

- **2026-07-04** (Receipt 0): *"All projects should have the current development loop
  structure and workflow, and therefore same type of init prompt."* — this loop is the
  session entry convention (thin launcher → `LOOP_INIT.md` → this plan → receipts).
- **2026-07-10** (Receipt 5): consolidation adopted — *deliverables themselves are the
  means of discovering work*; the plans-as-queue convention is retired; this plan
  absorbs `_COORDINATION.md`'s operative mechanics, and that file is reduced to a
  ruled-record surface; open scope is recorded in deliverable-local `_STATUS.md`
  `## Remaining` sections. Which rehomed lanes are live remains the owner's ruling
  (`D-APP-53`, AWAITING_RULING — see its packet's 2026-07-10 addendum).
- **2026-07-17** (D-APP-59; D-APP-60): the standing decision-latitude delegation is
  adopted and refined into the frozen shared block v1 (one template shared with the
  chirality-piping loop, two local bindings); this plan integrates the D-APP-60
  instrument into selection, gating, execution, and closeout.
- **2026-07-18** (D-APP-61 M2-A): runtime hierarchy, role routing, and child-session
  mechanics remain in canonical agent instructions; this plan retains loop-specific
  discovery, authority, gates, checks, and handoff obligations, citing governed
  instruments instead of restating their mechanics.
- **2026-07-18** (D-APP-64): the reasoned-selection refinement — under the owner's
  transcribed standing approval, plurality of surviving defensible outcomes is no
  longer itself a referral condition; inside the overlay's fast-reject boundary the
  agent selects and advances one reasoned outcome, recording a concise rationale
  and materially important rejected alternatives.
- **2026-09-03** (A11; A12) *(A12)*: A11 ruled the G0 Task-Management triage
  dispositions and authorized the separate E2 Electron-drift concordance tranche
  (`plans/steers/chirality_app_v3_app_ruling_record_a11_2026-09-03.md`). A12
  selected the App pathway seating: the owner-adopted v3.0.0-rc.1 completion and
  acceptance reference (Root R17-C) is pinned below; the accepted SCA-APP-008
  carriers are re-based on the applied decomposition and carry deliverable-local
  v3 `Remaining` items bound to WP/gate/AT, dependencies, write locus, checks, and
  return contracts; this successor plan carries the R17 calibrated
  development-pressure posture. Merge of the seating candidate confers
  selectability only; no implementation, lifecycle, host-mutation, signing,
  release, publication, reliance, or Root act is inferred.

**The loop's goal** (agent-phrased; owner may correct the wording): advance
chirality-app-dev per its ruled authorities toward issuance readiness and the PRD
runtime scope, as far as live authority permits — stopping at every owner gate.

## Pinned v3.0.0-rc.1 completion and acceptance reference *(A12)*

`plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html` at SHA-256
`b0a57a917643fbc850b033c043c91a480ea198af84eed213235f5893f257ab5a` is the pinned
completion and acceptance reference for v3.0.0-rc.1 (adopted by the owner at Root
R17-C, 2026-08-27). It is **not authority, not status, and not a queue**: its dated
snapshots are never current-state claims; current `main`, accepted deliverables,
registers, exact dependencies, and later governing instruments control whenever a
claim differs, and the discrepancy is recorded in the receipt rather than by editing
history. The plan may be cited only for what a work package, gate, or acceptance
row *means* when complete. `plans/**` remains non-selectable (F-APP-5); a
plan-only row is never a selectable work item. Work is selectable only through
deliverable-local `Remaining` items.

## Non-negotiables (the compelling reasons staging remains)

1. **Adoption, ruling, and direction are human acts** (K-AUTH-1; D-GOV-04). **Truthful
   attribution is the one firm limit of the decision-latitude model**: agent decisions
   are recorded as the agent's own; never write a ruling record or `RULED` register row
   attributing to the owner an act that did not occur.
2. **Hard fences below** stop work regardless of eligibility.
3. **Gate state is register-derived** — open `D-APP-XX` rows, per-item `(gated: ...)`
   suffixes, and per-item `NOT_SELECTABLE_UNTIL: <gate or act>` states in `Remaining`
   sections are re-derived each iteration, never assumed *(A12)*.

## The loop protocol (every iteration)

0. **Discover (mandatory core).** Clean `git` state and branch awareness (log since the
   last receipt; concurrent loops may be live in this monorepo — keep write scopes
   disjoint from `_DomainEngines/**`, `projects/chirality-piping/**`, `projects/pec/**`,
   and treat unrelated dirty files as external state). Run
   `python3 tools/validation/validate_app_dev_loop_receipts.py --repo-root .` and only
   then read the latest applicable receipt(s) in `LOOP_RECEIPTS.md`; a validator
   failure blocks use of the cursor. Check
   `execution/_Coordination/_DECISIONS/_REGISTER.md` for
   rulings newer than the last receipt — new rulings are how work unlocks, look every
   time. Run the D-APP-38 corpus check from the project root
   (`PYTHONDONTWRITEBYTECODE=1 python3
   execution/_Reconciliation/References/reconcile_authority_corpus.py status`); any
   drift is repair-first work under selection principle (a), regardless of which
   tranche introduced it. Enumerate the work surface from deliverable folders:
   `grep -l '^## Remaining' 'execution/PKG-'*/1_Working/DEL-*/_STATUS.md` for open
   scope, and the repo-root practitioner harness `status` command for lifecycle posture
   (an absent `Remaining` section means no recorded open scope for that deliverable).
   Run repo-wide `PYTHONDONTWRITEBYTECODE=1` harness `self-check`. Verify any derivative
   statement — including this plan and your own tasking — against the live tree before
   relying on it; on disagreement the live tree wins and the delta goes in the receipt.
   *Pin and A1 preflight (A12):* recompute the SHA-256 of the pinned completion
   reference above and stop if it differs; check the routed Root notices under
   `execution/_Coordination/NOTICE_*` for new App-consumable acceptances (these are how
   `NOT_SELECTABLE_UNTIL` states resolve); and whenever a tranche will touch any path
   under `frontend/`, declare at Step 0 the **A1 re-stage rule**
   (`plans/steers/chirality_app_v3_app_ruling_record_a1_2026-08-23.md` lines 28-36):
   any mutation under `projects/chirality-app-dev/frontend/` invalidates the staged R20
   procedure for any future proof claim and requires a newly staged revision and a
   fresh owner-executed proof — the declaration is recorded in the tranche's run
   record and receipt.
1. **Select — from deliverable folders only.** A `Remaining` item is *selectable* when
   it carries no `(gated: ...)` / `(stage-gated: ...)` suffix and no
   `NOT_SELECTABLE_UNTIL:` state, or its named gate is ruled or its named act has
   occurred on `main` *(A12)*; blockedness beyond gates is re-derived from
   deliverable-local `Dependencies.csv` / `_DEPENDENCIES.md` and the accepted DepClosure
   snapshot (`execution/_Reconciliation/DepClosure/_LATEST.md`) — do not infer
   blocked/unblocked state from any hand-maintained summary. *Selectability rule (A12):*
   an item is executable only when its accepted Scope of Work, lifecycle, exact
   dependencies, named gates, check surface, and write locus all permit execution;
   an item whose gate is a Root acceptance, a Root implementation act, a held DEL-02-06
   binding, an owner act, or a release act stays parked until that gate or act is
   observable on `main` (a routed Root notice, a ruling record, or a merged act). Root
   surfaces are never written from this loop. Principles, in order: (a) repair failing
   validation for already-landed work before new scope; (b) work that discharges a gate
   prerequisite beats work that doesn't; (c) owner-directed items beat agent-inferred
   ones; (d) the highest-value ungated `Remaining` item. Apply the CONTRACT
   **K-ENGINE-6** strategic lens to every item — Chirality is a
   governance/UI/audit/lifecycle/adapter layer over provider harness mechanics;
   standalone-harness or feature-parity work is OFF-STRATEGY. Never manufacture work
   outside the recorded `Remaining` scope or revive ruled-shut items (a revival takes a
   new register row). *Delegation triage (D-APP-60):* before slating any
   judgment-shaped fork, apply the class test with fast-reject ordering — any touch of
   a recorded limit is owner-class immediately, no lens analysis; the adversarial
   four-lens test runs only on survivors. Items that touch a fast-reject boundary
   are slated in near-miss form naming the touched boundary; among surviving
   defensible alternatives the agent selects and advances the one outcome it judges
   most consistent and coherent across the four lenses *(D-APP-64)*, recording a
   concise rationale and materially important rejected alternatives. The asymmetry that
   governs the default: over-slating costs owner attention; over-deciding silently
   converts owner authority — only the first is cheap to recover from.
2. **Brief / slate.** Genuinely material or hard-to-reverse forks (a hard-fence
   question, a K-ENGINE-6 strategy fork, a costly public-contract or data-migration
   change, any `Remaining` item marked as needing its own decision packet) get a
   `PROPOSAL` packet registered in the decision register; within the fences, ordinary
   design forks are resolved with recorded agent decision latitude — under the
   D-APP-60 instrument as refined by the D-APP-64 overlay *(D-APP-64)* for
   disposition-class items (decide, record the rationale artifact, cite the
   exercise in the receipt), per-instance latitude otherwise.
3. **Gate.** STOP at the hard fences and at owner-shaped acts; adoption/ruling/direction
   is the owner's (K-AUTH-1; D-GOV-04). The STOP applies to owner-class items;
   disposition-class items proceed under the D-APP-60 method binding and verifier,
   as refined by D-APP-64: ambiguity about whether a fast-reject boundary is
   touched is owner-class; plurality of surviving defensible outcomes is not
   itself owner-class *(D-APP-64)*.
   Terminus slates arrive pre-triaged in near-miss form, each item naming the failed
   gate or limit. In-session directions/rulings are recorded verbatim in their governed
   artifact; only chat-only directions with no governed home are transcribed into the
   receipt, labeled as evidence rather than ruling. Directions fully recoverable from
   Git/PR history need no receipt transcription. Record every gate outcome — including
   no-ops and their reason.
4. **Execute + check.** Branch-first + PR is the default; never self-merge; write scope
   stays inside `projects/chirality-app-dev/**` unless the owner grants wider scope.
   *One branch, one PR, one receipt, owner merge per iteration (A12)*; no automatic PR
   stacking. *Checks per the work type:* typecheck + vitest + build/premerge gates
   (`docs/VALIDATION_STRATEGY.md`, `docs/RELEASE_QUALITY_GATES.md`,
   `docs/BUILD_AND_RELEASE.md`); the D-APP-36 render bar for UI work; D-APP-38 corpus
   reconciliation when an authority doc is edited; for governance/control-plane-only
   tranches record explicitly that frontend gates were skipped because no runtime
   source changed; stop the local dev server before build/package/premerge commands
   unless the command owns the server lifecycle; plus repo-wide `self-check` exit 0 and
   full practitioner-harness pytest at closeout. CI green; owner merges. The
   independent-review path in `AGENTS.md` (fresh read-only `TASK + software-code-review`
   over 100% of the frozen diff) is mandatory for any product-source change; the
   APP-HOLD-1 dispatch preflight is mandatory before any dispatch.
   *D-APP-60 verification:* every scope named by the instrument's calibrated
   verification requirement must satisfy that requirement before commit; verdicts are
   recorded only after they exist, and nothing lands on `BLOCK`.
5. **Update deliverable state + receipt.** Closeout writes deliverable-local state:
   `_STATUS.md` (`Remaining` updated to reflect what landed — landed scope removed,
   newly named residuals added; lifecycle transitions only through their ruled gates,
   `**Checking Approval SHA**` discipline intact), `MEMORY.md`, `_run_records/**`;
   landed narrative goes to `plans/PLAN_COMPLETION_LOG.md`. Rationale artifacts for
   delegation exercises live in existing homes only: deliverable-scoped → that
   deliverable's `_run_records/**`; cross-cutting → the tranche's AgentRuns record;
   the artifact records rejections alongside exercises. Receipt citation convention:
   `Gate-Outcome` names the exercised judgment; `Pointers` names the rationale
   artifact. Append one versioned minimal receipt to `LOOP_RECEIPTS.md` per its local
   rules, then rerun
   `python3 tools/validation/validate_app_dev_loop_receipts.py --repo-root .`; receipt
   validation is a mandatory pre-commit and closeout gate. Next iteration starts at 0.

## Calibrated development pressure *(A12; Root R17-E, App carriers substituted)*

> Once a deliverable item is selectable, prioritize executable product, test,
> and gate-closing engineering work. Select a bounded set of independent or
> dependency-linked nodes only when each node has an accepted scope, known
> write locus, named checks, and no unresolved owner gate. Execute compatible
> independent nodes concurrently where useful. Apply accepted decisions as
> written; do not re-plan them merely to fill an iteration. A failed check or
> required review is a repair loop, not a terminal node state: repair and
> rerun until passing unless a hard fence, owner ruling, or forced termination
> intervenes. A blocked node holds only its dependants; independent lawful
> work continues. Each ordinary iteration must materially reduce at least one
> accepted deliverable obligation. Evidence-only work counts when the selected
> obligation is itself an evidence gate. Coordination artifacts support the
> selected work but do not substitute for it. Work absent from accepted
> deliverable `Remaining` scope is not selectable.

Applied to this loop: the accepted SCA-APP-008 carriers (DEL-01-01, DEL-02-02,
DEL-02-05, DEL-03-01, DEL-03-03, DEL-04-01, DEL-04-05, DEL-05-01, DEL-05-02,
DEL-05-03, DEL-05-04, DEL-08-04, DEL-08-05, DEL-09-01, DEL-09-02, DEL-09-03,
DEL-09-04, DEL-09-05, DEL-09-06) carry the v3 items; Root-gated items (Root
WP-03/WP-05 implementation, the DEL-02-06 implementation act, Root API v2 / event
schema v2 acceptance, G-HELPER, G2 exact-pin claims, live account, signing,
notarization, G6a) stay parked. Development pressure never weakens a human gate,
evidence bar, containment fence, ownership boundary, or truthful-attribution
requirement, and never turns the pinned plan into a queue or broadens a write
locus.

## Evidence contract for empirical, fixture, conformance, and gate-evidence items *(A12; Root R17 N3)*

Every such item's acceptance and return require enough durable **non-secret** bytes
for an independent verifier to recompute the claim — at minimum, as applicable:
exact input/source identities and the complete cited-byte inventory; fixture,
evaluator, validator, and adapted-source bytes; command, arguments, cwd, relevant
effective environment, tool/runtime versions, and exit status; canonical
stdout/stderr and machine-readable results; process, filesystem, containment, and
denied-egress observations; sorted manifests and independent hash recomputation;
cleanup proof for disposable/quarantine state; and an executable or precisely
bounded rerun method. Never preserve credentials, tokens, private account material,
forbidden artifact binaries, or user-wide state. When required underlying bytes
cannot be preserved or independently recomputed, the claim remains unavailable; a
prose summary or remembered digest is not acceptance evidence.

## Standing constraints — hard fences (all iterations; always stop for a human ruling)

- **F-APP-1 (provider/network):** no provider or network expansion beyond the Anthropic
  path; no remote MCP, plugin, or broad tool-search enablement without a fresh ruling
  (F1 as amended by D-APP-44: owner-permitted, default-closed provider/residency
  configuration).
- **F-APP-2 (release/distribution):** no signing, notarization, publication, external
  distribution, or release-readiness / professional / certification claims.
- **F-APP-3 (domain-engine boundary):** domain-engine work happens only inside what the
  tier-0 bridge loop's ruled decisions grant (the `D-APP-4x` F-series rows); this loop
  never writes `_DomainEngines/**` or piping surfaces, and never advances integration
  level, live binding, or apply-class tool exposure on its own authority.
- **F-APP-4 (issuance):** no `CHECKING -> ISSUED` lifecycle issuance.
- **F-APP-5 (single-surface rule; owner-adopted 2026-07-10):** work items live in
  deliverable folders (`_STATUS.md` `## Remaining`); owner decisions live in
  `execution/_Coordination/_DECISIONS/_REGISTER.md`; no new standing plan, queue,
  register, or status surface is created without an owner ruling. `plans/` is a
  historical archive — never select work from it.
- **Fresh-ruling stops** (carried from the pre-consolidation coordination record):
  Pi-backed execution (unapproved after D-APP-01/02); concrete non-Anthropic provider
  implementation or routing; write/edit/bash/tool-execution exposure beyond the current
  approved item; changes to the project-truth model for sessions, transcripts, chats,
  runtime logs, or completion logs; professional-boundary or release-readiness posture.

*A12 note (agent-authored observation beside the fences, not fence text; the fence
bullets above are carried from the 2026-07-18b plan verbatim):* under F-APP-1, App
`docs/CONTRACT.md` K-NET-1 names exact accepted OpenAI account, model, and turn
service endpoints for the delegated-harness adapter; they become usable only through
the gates their carriers' `Remaining` items name, and nothing else is added. Under
F-APP-2, D-APP-97 and F-APP-2 remain active through WP-09 preparation and lift only at
G6a against the exact owner-named candidate (G0 D2). Under F-APP-5, the pinned
completion reference is cited for meaning only. Any change to fence wording itself is
an owner act.

## Where live work is re-derived (pointer index — never a status surface)

- **Work surface (discovery + selection):** `execution/PKG-*/1_Working/DEL-*/` —
  `_STATUS.md` (lifecycle + `## Remaining` open scope), `MEMORY.md`, Scope of Work
  (`ScopeOfWork.md`) or legacy four-document kits, `Dependencies.csv` /
  `_DEPENDENCIES.md`, `_run_records/**`.
- **Ruled records:** `execution/_Coordination/_COORDINATION.md` (ruled-record stub) ·
  decision register `execution/_Coordination/_DECISIONS/_REGISTER.md` (`D-APP-XX`
  rows; packets/ruling records beside it; open rows are the owner-gated surface) ·
  discovery pointers: `execution/_Coordination/_LATEST.md` · v3 owner rulings and
  steers under repo-root `plans/steers/` (`chirality_app_v3_app_ruling_record_a*`,
  `chirality_app_v3_root_ruling_record_r*`; transcription sources, not authority).
- **Delegation instrument:** D-APP-60 (frozen shared block v1 + app-dev local
  bindings; supersedes D-APP-59's reach/method definition by reference), as refined
  by the D-APP-64 reasoned-selection overlay (fast-reject boundary, selection
  method, attribution schema) *(D-APP-64)* — delegation exercises cite D-APP-60
  and follow its method binding, calibrated verifier scope, and rejection-recording
  convention.
- **Dependency evidence:** `execution/_Reconciliation/DepClosure/_LATEST.md` → the
  accepted closure snapshot; the SCA-APP-008 Gate-5 post-application audit under
  `execution/_ScopeChange/SCA-APP-008_2026-08-23_1727_V3_Release_Pathway/Phase5/Audit/`
  (warning-bearing derivative evidence); SCC work follows the shared
  `docs/CYCLE_DRIVEN_RESOLUTION.md` doctrine (repo root).
- **What must be built and why:**
  `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` (applied
  SCA-APP-008 Gate-5 text) · scope amendments: `execution/_ScopeChange/_LATEST.md` ·
  product yardstick: `docs/PRD.md` · strategy: `docs/PLAN.md` (non-governing) ·
  authority documents: `docs/DIRECTIVE.md`, `docs/CONTRACT.md`, `docs/SPEC.md`,
  `docs/TYPES.md` — edits trigger D-APP-38 corpus reconciliation
  (`execution/_Reconciliation/References/reconcile_authority_corpus.py`).
- **v3.0.0-rc.1 completion and acceptance reference *(A12)*:** the pinned plan HTML
  named above — meaning only; never status, authority, or a queue.
- **Cross-loop handoffs *(A12)*:** routed Root notices under
  `execution/_Coordination/NOTICE_*` (Root accepted returns, class rulings, and
  acceptances arrive here; this loop adopts, amends, or declines under its own
  instruments and never writes Root surfaces); APP-HOLD-1 register
  `execution/_Coordination/APP_HOLD_REGISTER.csv`; Task Management register
  `execution/_Coordination/_TaskManagement/REGISTER.csv`.
- **Validation gates:** `docs/VALIDATION_STRATEGY.md` · `docs/RELEASE_QUALITY_GATES.md`
  (§13 Shared Runtime Gate is validation evidence only) · `docs/BUILD_AND_RELEASE.md`.
- **Agent posture:** `AGENTS.md` (personas, dispatch contract, delegation posture,
  independent-review path, host-capability rule, CHANGE closeout).
- **Frontend contract surfaces:** `frontend/packages/harness-contract/**` (pull
  contract pinned at `execution/_Coordination/_DECISIONS/D-APP-48_FLOW_A_PULL_CONTRACT_*.json`).
- **Cross-loop awareness:** `_DomainEngines/bridge/LOOP_RECEIPTS.md` (scope dedup only —
  this loop never writes the bridge loop's surfaces).
- **Historical archive (never selection surfaces):** `plans/**` (queue rows closed or
  rehomed 2026-07-10; see `plans/PLAN_COMPLETION_LOG.md`) ·
  `execution/_Coordination/NEXT_INSTANCE_PROMPT.md` (pre-loop session entry — dated
  historical map, never authority) · `loop/WORKPLAN_2026-07-18b_app_dev_loop.md` and
  earlier plans (superseded; preserved unchanged).
- **Handoff context** (owner directions, gate outcomes, stale-map deltas):
  `LOOP_RECEIPTS.md` beside this file.
