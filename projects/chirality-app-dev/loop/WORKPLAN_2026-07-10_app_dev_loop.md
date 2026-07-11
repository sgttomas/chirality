# App-Dev Work Loop — standing plan (development loop instructions)

> **Epistemic status: agent-authored plan — not authority.** Written at owner adoption
> (Ryan Tufts, K-AUTH-1) on 2026-07-10; supersedes `WORKPLAN_2026-07-04_app_dev_loop.md`
> in this directory. This plan never authorizes work: owner rulings and directions do.
> Sources govern on any disagreement. This file is the project's single development-loop
> instruction surface — PROTOCOL plus pointer indexes; it carries NO status, NO work
> history, and NO measurements. Each iteration re-derives state from the live tree; loop
> closes append a minimal receipt to `LOOP_RECEIPTS.md` beside this file (rules live at
> the top of that file).

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

**The loop's goal** (agent-phrased; owner may correct the wording): advance
chirality-app-dev per its ruled authorities toward issuance readiness and the PRD
runtime scope, as far as live authority permits — stopping at every owner gate.

## Non-negotiables (the compelling reasons staging remains)

1. **Adoption, ruling, and direction are human acts** (K-AUTH-1; D-GOV-04). **Truthful
   attribution is the one firm limit of the decision-latitude model**: agent decisions
   are recorded as the agent's own; never write a ruling record or `RULED` register row
   attributing to the owner an act that did not occur.
2. **Hard fences below** stop work regardless of eligibility.
3. **Gate state is register-derived** — open `D-APP-XX` rows and per-item `(gated: ...)`
   suffixes in `Remaining` sections are re-derived each iteration, never assumed.

## The loop protocol (every iteration)

0. **Discover (mandatory core).** Clean `git` state and branch awareness (log since the
   last receipt; concurrent loops may be live in this monorepo — keep write scopes
   disjoint from `_DomainEngines/**`, `projects/chirality-piping/**`, `projects/pec/**`,
   and treat unrelated dirty files as external state). Read the latest receipt(s) in
   `LOOP_RECEIPTS.md`. Check `execution/_Coordination/_DECISIONS/_REGISTER.md` for
   rulings newer than the last receipt — new rulings are how work unlocks, look every
   time. Enumerate the work surface from deliverable folders:
   `grep -l '^## Remaining' 'execution/PKG-'*/1_Working/DEL-*/_STATUS.md` for open
   scope, and the repo-root practitioner harness `status` command for lifecycle posture
   (an absent `Remaining` section means no recorded open scope for that deliverable).
   Run repo-wide `PYTHONDONTWRITEBYTECODE=1` harness `self-check`. Verify any derivative
   statement — including this plan and your own tasking — against the live tree before
   relying on it; on disagreement the live tree wins and the delta goes in the receipt.
1. **Select — from deliverable folders only.** A `Remaining` item is *selectable* when
   it carries no `(gated: ...)` / `(stage-gated: ...)` suffix, or its named gate is
   ruled; blockedness beyond gates is re-derived from deliverable-local
   `Dependencies.csv` / `_DEPENDENCIES.md` and the accepted DepClosure snapshot
   (`execution/_Reconciliation/DepClosure/_LATEST.md`) — do not infer blocked/unblocked
   state from any hand-maintained summary. Principles, in order: (a) repair failing
   validation for already-landed work before new scope; (b) work that discharges a gate
   prerequisite beats work that doesn't; (c) owner-directed items beat agent-inferred
   ones; (d) the highest-value ungated `Remaining` item. Apply the CONTRACT
   **K-ENGINE-6** strategic lens to every item — Chirality is a
   governance/UI/audit/lifecycle/adapter layer over provider harness mechanics;
   standalone-harness or feature-parity work is OFF-STRATEGY. Never manufacture work
   outside the recorded `Remaining` scope or revive ruled-shut items (a revival takes a
   new register row).
2. **Brief / slate.** Genuinely material or hard-to-reverse forks (a hard-fence
   question, a K-ENGINE-6 strategy fork, a costly public-contract or data-migration
   change, any `Remaining` item marked as needing its own decision packet) get a
   `PROPOSAL` packet registered in the decision register; within the fences, ordinary
   design forks are resolved with recorded agent decision latitude — decide, proceed,
   note the call.
3. **Gate.** STOP at the hard fences and at owner-shaped acts; adoption/ruling/direction
   is the owner's (K-AUTH-1; D-GOV-04). In-session directions/rulings are quoted
   verbatim in the receipt and recorded in their governed artifact as part of execution.
   Record every gate outcome — including no-ops and their reason.
4. **Execute + check.** Branch-first + PR is the default; never self-merge; write scope
   stays inside `projects/chirality-app-dev/**` unless the owner grants wider scope.
   *Bounded workers:* spawn `TASK` agents only for separable subscopes with explicit
   briefs (sources to read, files it may write, validation expected, prod-code vs
   docs-only) and disjoint write scopes; after a validated tranche, hand off to a
   `CHANGE` agent for final Git/file-state review under `AGENTS.md` closeout discipline.
   *Checks per the work type:* typecheck + vitest + build/premerge gates
   (`docs/VALIDATION_STRATEGY.md`, `docs/RELEASE_QUALITY_GATES.md`,
   `docs/BUILD_AND_RELEASE.md`); the D-APP-36 render bar for UI work; D-APP-38 corpus
   reconciliation when an authority doc is edited; for governance/control-plane-only
   tranches record explicitly that frontend gates were skipped because no runtime
   source changed; stop the local dev server before build/package/premerge commands
   unless the command owns the server lifecycle; plus repo-wide `self-check` exit 0 and
   full practitioner-harness pytest at closeout. CI green; owner merges.
5. **Update deliverable state + receipt.** Closeout writes deliverable-local state:
   `_STATUS.md` (`Remaining` updated to reflect what landed — landed scope removed,
   newly named residuals added; lifecycle transitions only through their ruled gates,
   `**Checking Approval SHA**` discipline intact), `MEMORY.md`, `_run_records/**`;
   landed narrative goes to `plans/PLAN_COMPLETION_LOG.md`. Append a minimal receipt to
   `LOOP_RECEIPTS.md` per its local rules. Next iteration starts at 0.

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

## Where live work is re-derived (pointer index — never a status surface)

- **Work surface (discovery + selection):** `execution/PKG-*/1_Working/DEL-*/` —
  `_STATUS.md` (lifecycle + `## Remaining` open scope), `MEMORY.md`, four-document
  kits, `Dependencies.csv` / `_DEPENDENCIES.md`, `_run_records/**`.
- **Ruled records:** `execution/_Coordination/_COORDINATION.md` (ruled-record stub) ·
  decision register `execution/_Coordination/_DECISIONS/_REGISTER.md` (`D-APP-XX`
  rows; packets/ruling records beside it; open rows are the owner-gated surface) ·
  discovery pointers: `execution/_Coordination/_LATEST.md`.
- **Dependency evidence:** `execution/_Reconciliation/DepClosure/_LATEST.md` → the
  accepted closure snapshot; SCC work follows the shared
  `docs/CYCLE_DRIVEN_RESOLUTION.md` doctrine (repo root).
- **What must be built and why:**
  `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` · scope
  amendments: `execution/_ScopeChange/_LATEST.md` · product yardstick: `docs/PRD.md` ·
  strategy: `docs/PLAN.md` (non-governing) · authority documents: `docs/DIRECTIVE.md`,
  `docs/CONTRACT.md`, `docs/SPEC.md`, `docs/TYPES.md` — edits trigger D-APP-38 corpus
  reconciliation (`execution/_Reconciliation/References/reconcile_authority_corpus.py`).
- **Validation gates:** `docs/VALIDATION_STRATEGY.md` · `docs/RELEASE_QUALITY_GATES.md`
  · `docs/BUILD_AND_RELEASE.md`.
- **Agent posture:** `AGENTS.md` (personas, dispatch contract, CHANGE closeout).
- **Frontend contract surfaces:** `frontend/packages/harness-contract/**` (pull
  contract pinned at `execution/_Coordination/_DECISIONS/D-APP-48_FLOW_A_PULL_CONTRACT_*.json`).
- **Cross-loop awareness:** `_DomainEngines/bridge/LOOP_RECEIPTS.md` (scope dedup only —
  this loop never writes the bridge loop's surfaces).
- **Historical archive (never selection surfaces):** `plans/**` (queue rows closed or
  rehomed 2026-07-10; see `plans/PLAN_COMPLETION_LOG.md`) ·
  `execution/_Coordination/NEXT_INSTANCE_PROMPT.md` (pre-loop session entry — dated
  historical map, never authority).
- **Handoff context** (owner directions, gate outcomes, stale-map deltas):
  `LOOP_RECEIPTS.md` beside this file.
