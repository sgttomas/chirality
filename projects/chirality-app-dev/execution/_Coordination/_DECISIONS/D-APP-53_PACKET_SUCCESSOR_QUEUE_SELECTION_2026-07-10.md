# D-APP-53 — PROPOSAL: Successor Development-Queue Selection (post inspection-orphan closure)

> **Epistemic status: agent-authored PROPOSAL packet — not authority (K-AUTH-1; D-GOV-04).**
> Prepared 2026-07-10 by the app-dev work loop (Claude Fable 5 session, worktree branch
> `claude/app-dev-loop-post-orn-2026-07-10`) because every candidate development tranche is
> blocked by this decision. Nothing here authorizes work; only an owner ruling recorded in a
> `D-APP-53_RULING_*.md` record does. Options are presented owner-first; the recommendation is
> non-binding.

## 1. Why this decision is needed now

- The active queue `plans/PLAN_2026-06-21_inspection_orphan_remediation.md` is **CLOSED**
  (queue exhausted 2026-07-10; `ORN-01`..`ORN-05`, `ORN-07`..`ORN-13` DONE; `ORN-06` DROPPED).
- The decision register has **no open row** before this one: D-APP-01..52 are all RULED.
- A 2026-07-10 discovery sweep (this loop, three-way subagent fan-out) verified against the
  live tree that **every ruled tranche through D-APP-52 has landed** — the D-APP-46/47/48
  package extraction/migration/pull mechanism, the D-APP-49 type modules, the D-APP-50 domain
  MCP tool tranches (with two ruled-conditional residuals noted in §4), the D-APP-51 registry,
  and the D-APP-52 pec transport/proposal tools. No adopted-but-unexecuted brief exists.
- Landed-work validation is green: repo self-check exit 0; authority corpus `v5` no drift;
  practitioner-harness pytest green on a clean checkout of `61d70bdb0` (the one main-tree
  failure is attributable to uncommitted, out-of-project deletions of
  `projects/chirality-governance/**` in the shared working copy — external state);
  frontend typecheck and full Vitest green (667 passed / 4 skipped).

Per `_COORDINATION.md` ("Do not invent a replacement queue; select new work only from an
explicit human direction or a newly accepted plan/ruling") and the loop workplan, the loop
therefore stops here for the owner.

## 2. What this decision blocks

Selection/adoption of any new development queue, and any new development tranche beyond
guidance-surface repair and validation upkeep.

## 3. Options

### Option A — Pre-issuance dependency-row reconciliation queue (recommended)

Adopt a bounded queue that closes the **unsatisfied local dependency rows** left explicit by
the INSP-05 roadmap addendum §5 ("pre-issuance dependency reconciliation": DEL-01-02/01-03/
01-04, DEL-04-01, DEL-09-03, DEL-10-01..05) and by ORN-13's bounded closeout (which kept
dependency-row residuals outside its refresh). Scope: verify each cited pending dependency row
against live evidence, land the evidence or retire/replace rows per the v3.1 schema, and
produce a DepClosure-consistent reconciliation record per deliverable.

- **Why first:** it discharges the standing prerequisite for any future issuance decision
  (principle: gate-prerequisite work beats work that discharges no gate) without itself
  crossing F-APP-4; it is bounded, evidence-shaped, and fully within existing governance.
- **Risks:** low — docs/evidence-heavy; the main risk is over-claiming closure, mitigated by
  citing per-row evidence and keeping issuance explicitly out of scope.
- **Validation implications:** self-check + corpus status per tranche; frontend gates only if
  runtime files are touched; no new capability surface.
- **Affected files:** deliverable-local `Dependencies.csv` / `_DEPENDENCIES.md` /
  `_STATUS.md` / evidence records under `execution/`; a new `plans/PLAN_2026-07-XX_*.md`
  queue authored on adoption.

### Option B — Issuance program activation

Reactivate the deferred issuance spine (D-APP-19/D-APP-34 Option B evidence profiles):
per-deliverable `CHECKING -> ISSUED` under owner SHA-bound gates. **Crosses F-APP-4**, so it
requires the owner at the gate for every issuance act; Option A is its natural prerequisite
(the addendum's unsatisfied dependency rows would otherwise surface as issuance blockers).

- **Risks:** owner time-intensive; premature without Option A.
- **Validation implications:** issue-readiness profile checks per `docs/ISSUE_READINESS_PROFILES.md`.
- **Affected files:** deliverable `_STATUS.md` lifecycle records, issuance evidence packages.

### Option C — Deferred hardening cluster

Adopt the explicitly deferred, separately-gated hardening items as a queue: D-APP-42 Option C
full tool-result audit policy; arbitrary-secret-registry redaction taxonomy (DEL-05-03);
per-attempt subagent decision-replay artifact (DEL-08-04); content-change SHA revalidation
(DEL-07-04); owner-authority/responsible-party TBD fields (DEL-00-02, DEL-01-03).

- **Risks:** medium code surface; each item was flagged "needs its own gate or decision", so
  the adopting ruling should name which items are in.
- **Validation implications:** frontend typecheck/Vitest + targeted new tests per item.
- **Affected files:** runtime/session/tooling code under `frontend/src/lib/harness/**` + tests.

### Option D — R7 / domain-engine next step

Advance the tier-0-laned domain-engine build per the ADQ-17 R7 amendment brief
(`plans/artifacts/adq17_future_r7_amendment_brief_2026-06-21.md`). Constrained by F-APP-3 and
the D-T0-08 stepwise lane; `operation_applier.apply` exposure is excluded and would need its
own packet (per the D-APP-50 ruling); the two D-APP-50 residuals in §4 are blocked on
piping-side transport soundness regardless.

- **Risks:** highest coordination surface (tier-0/bridge/pec lanes); parts are blocked on
  external dependencies today, so an adopted queue could stall.
- **Validation implications:** full frontend gates + registry/pull-contract repins.
- **Affected files:** `frontend/src/lib/harness/mcp/**`, `frontend/packages/harness-contract/**`.

### Option E — Park at maintenance

Adopt no queue. The loop performs only validation repair and guidance-surface upkeep, and
stops. Zero risk, zero progress; the §4 owner-gated tail stays parked.

## 4. Standing owner-gated items this packet does NOT decide (for visibility)

- PEC **P4 end-to-end rehearsal** — requires owner-at-screen (app-dev Receipts 1–3; pec ledger).
- **D-APP-52 live-LLM demonstration** — explicitly deferred, not authorized (packet lines 51, 116).
- D-APP-50 residuals — `domain_headless_preview_run` live flip and an `open_pipe_stress`-scoped
  proposal transport: already inside the D-APP-50 ruling's grant but conditional on piping-side
  transport soundness (external dependency, not a new app-dev ruling).
- Issuance of the 53 deliverables (F-APP-4), release/distribution posture (F-APP-2), provider
  expansion beyond the ruled residency configuration (F-APP-1 as amended by D-APP-44), and
  tier-0 L2→L3 movement (F-APP-3 lane) — each retains its own gate.

## 5. Recommendation (non-binding)

**Option A**, optionally folding in named Option C items as riders if the owner wants code
work in the same window. It is the only option that discharges a gate prerequisite (issuance
readiness) while staying entirely inside already-ruled governance.

## 6. On-ruling mechanism

An in-session owner ruling ("D-APP-53: Option X" with any riders) suffices; the executing loop
then (1) records the ruling verbatim in a `D-APP-53_RULING_2026-07-XX.md` record and flips the
register row to RULED, (2) authors the successor queue plan under `plans/` with explicit rows
and the ruling as its authority basis, and (3) executes under branch-first + PR discipline
unless the ruling grants a recorded commit discipline (e.g. D-APP-39-style autonomous
commit+push scoped to `projects/chirality-app-dev/**`).
