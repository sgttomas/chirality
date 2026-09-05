# App-Dev Work Loop — standing plan (project development loop)

> **SUPERSEDED 2026-07-10** by `WORKPLAN_2026-07-10_app_dev_loop.md` in this directory
> (owner-adopted consolidation; Receipt 5). Retained as a dated record only — the
> newest `WORKPLAN_*.md` governs. Do not follow this file's protocol or pointers.

> **Epistemic status: agent-authored plan — not authority.** Written at owner direction
> (Ryan Tufts, K-AUTH-1) on 2026-07-04. This plan never authorizes work: owner-adopted
> plans, decision rulings, and directions do. Sources govern on any disagreement. This
> file is a PROTOCOL plus pointer indexes; it carries NO status, NO work history, and NO
> measurements — each loop iteration re-derives state from the live tree, and loop closes
> append a minimal receipt to `LOOP_RECEIPTS.md` beside this file (rules live at the top
> of that file).

## Owner intent (recorded 2026-07-04)

Owner direction of record (quoted verbatim in `LOOP_RECEIPTS.md` Receipt 0): *"All
projects should have the current development loop structure and workflow, and therefore
same type of init prompt."* — converting this project's session entry from the
status-laden `execution/_Coordination/NEXT_INSTANCE_PROMPT.md` convention to the current
loop convention (thin launcher → `LOOP_INIT.md` → this plan → receipts).

**The loop's goal** (agent-phrased under that direction; owner may correct the wording):
advance chirality-app-dev per its coordination authorities and owner-ruled queues as far
as live authority permits — stopping at every owner gate. The pre-existing workflow
authority is unchanged: `_COORDINATION.md` and the ruled decision register remain how
work is authorized and executed; this loop wraps them in the current session convention,
it does not replace them.

## Why any staging remains (the compelling reasons)

1. **Adoption, ruling, and direction are human acts** (K-AUTH-1; D-GOV-04). `D-APP-XX`
   rulings and `*_RULING_*.md` records are the owner's instrument. **Truthful
   attribution is the one firm limit of the decision-latitude model**: agent decisions
   are recorded as the agent's own; never write a ruling record or `RULED` register row
   attributing to the owner an act that did not occur.
2. **Hard fences below** stop work regardless of queue eligibility.
3. **Ruled-queue discipline is register-derived** — whether an owner-adopted queue (and
   any recorded commit discipline it carries, e.g. the D-APP-39 autonomous mode) is
   live, exhausted, or superseded is re-derived from the register and the queue plan's
   own rows each iteration, never assumed from this file.

## The loop protocol (every iteration)

0. **Discover (mandatory core).** Clean `git` state and branch awareness (log since the
   last receipt; concurrent loops may be live in this monorepo — keep write scopes
   disjoint from `_DomainEngines/**`, `projects/chirality-piping/**`, `projects/pec/**`,
   and treat unrelated dirty files as external state). Read the latest receipt(s) in
   `LOOP_RECEIPTS.md` beside this file. Check
   `execution/_Coordination/_DECISIONS/_REGISTER.md` for rulings newer than the last
   receipt — new rulings are how work unlocks, look every time. Re-derive the active
   queue (the newest owner-adopted plan under `plans/` with open rows), discovery
   pointers (`execution/_Coordination/_LATEST.md`), and repo-wide
   `PYTHONDONTWRITEBYTECODE=1` harness `self-check`. Verify any derivative statement —
   including this plan and your own tasking — against the live tree before relying on
   it; on disagreement the live tree wins and the delta goes in the receipt.
1. **Select.** The widest lawful tranche(s) now, re-derived. Principles, in order:
   (a) repair failing validation for already-landed work before new scope; (b) work that
   discharges a gate prerequisite beats work that doesn't; (c) owner-directed items beat
   agent-inferred ones; (d) the highest-priority eligible item from the live
   owner-adopted queue whose prerequisites are met (recompute readiness; do not trust
   recorded status if the filesystem disagrees). Apply the CONTRACT **K-ENGINE-6**
   strategic lens to every item — Chirality is a governance/UI/audit/lifecycle/adapter
   layer over provider harness mechanics; standalone-harness or feature-parity work is
   OFF-STRATEGY. Never revive a completed/closed/retired/superseded plan or invent work
   outside the live queue's backlog.
2. **Brief / slate.** Queue items execute under the queue plan's recorded discipline.
   Genuinely material or hard-to-reverse forks (a hard-fence question, a K-ENGINE-6
   strategy fork, a costly public-contract or data-migration change) get a `PROPOSAL`
   packet registered in the decision register; within the fences, ordinary design forks
   are resolved with recorded agent decision latitude — decide, proceed, note the call.
3. **Gate.** STOP at the hard fences and at owner-shaped acts; adoption/ruling/direction
   is the owner's (K-AUTH-1; D-GOV-04). In-session directions/rulings are quoted
   verbatim in the receipt and recorded in their governed artifact as part of execution.
   Record every gate outcome — including no-ops and their reason.
4. **Execute + check.** Branch-first + PR is the default; never self-merge. A live
   owner-adopted queue whose recorded discipline says otherwise (e.g. D-APP-39
   autonomous commit+push) governs for its own items only — and even then stage only
   `projects/chirality-app-dev/**` paths and abort if anything outside is staged.
   Checks per the work type: typecheck + vitest + build/premerge gates
   (`docs/VALIDATION_STRATEGY.md`, `docs/RELEASE_QUALITY_GATES.md`,
   `docs/BUILD_AND_RELEASE.md`), the D-APP-36 render bar for UI work, D-APP-38 corpus
   reconciliation when an authority doc is edited, plus repo-wide `self-check` exit 0
   and full practitioner-harness pytest at closeout. CI green; owner merges.
5. **Receipt.** Append a minimal receipt to `LOOP_RECEIPTS.md` per its local rules —
   pointers, verbatim owner directions, gate outcomes, check pass/fail. No narrative
   here or anywhere else. Next iteration starts at 0.

## Standing constraints — hard fences (all iterations; always stop for a human ruling)

- **F-APP-1 (provider/network):** no provider or network expansion beyond the Anthropic
  path; no remote MCP, plugin, or broad tool-search enablement without a fresh ruling.
- **F-APP-2 (release/distribution):** no signing, notarization, publication, external
  distribution, or release-readiness / professional / certification claims.
- **F-APP-3 (domain-engine boundary):** domain-engine work happens only inside what the
  tier-0 bridge loop's ruled decisions grant (the `D-APP-4x` F-series rows); this loop
  never writes `_DomainEngines/**` or piping surfaces, and never advances integration
  level, live binding, or apply-class tool exposure on its own authority.
- **F-APP-4 (issuance):** no `CHECKING -> ISSUED` lifecycle issuance.

## Where live work is re-derived (pointer index — never a status surface)

- **Workflow authority:** `execution/_Coordination/_COORDINATION.md` · project agent
  posture: `AGENTS.md` · discovery pointers: `execution/_Coordination/_LATEST.md`.
- **Decision register** (open rows are the owner-gated surface):
  `execution/_Coordination/_DECISIONS/_REGISTER.md` (`D-APP-XX` rows, ruling records,
  and the packets/rulings that carry queue and fence state).
- **Queues and plans:** `plans/` (the newest owner-adopted plan with open rows is the
  active queue; the plan's own rows say what is READY/BLOCKED/DONE) · completion log:
  `plans/PLAN_COMPLETION_LOG.md`.
- **Authority documents:** `docs/DIRECTIVE.md`, `docs/CONTRACT.md`, `docs/SPEC.md`,
  `docs/TYPES.md`, `docs/PLAN.md`, `docs/PRD.md` — edits trigger D-APP-38 corpus
  reconciliation (`execution/_Reconciliation/References/reconcile_authority_corpus.py`).
- **Validation gates:** `docs/VALIDATION_STRATEGY.md` · `docs/RELEASE_QUALITY_GATES.md`
  · `docs/BUILD_AND_RELEASE.md` · workflow reference:
  `docs/AGENTIC_DEVELOPMENT_WORKFLOW.md`.
- **Frontend contract surfaces:** `frontend/packages/harness-contract/**` (pull contract
  pinned at `execution/_Coordination/_DECISIONS/D-APP-48_FLOW_A_PULL_CONTRACT_*.json`).
- **Cross-loop awareness:** `_DomainEngines/bridge/LOOP_RECEIPTS.md` (scope dedup only —
  this loop never writes the bridge loop's surfaces).
- **Legacy session entry (historical):** `execution/_Coordination/NEXT_INSTANCE_PROMPT.md`
  — the pre-loop, status-laden entry document. Treat as a dated map, never authority;
  the register and live tree govern on any disagreement.
- **Handoff context** (owner directions, gate outcomes, stale-map deltas):
  `LOOP_RECEIPTS.md` beside this file.
