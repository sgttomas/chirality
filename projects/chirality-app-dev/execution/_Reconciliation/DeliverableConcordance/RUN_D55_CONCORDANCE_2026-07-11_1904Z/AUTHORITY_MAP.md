# AUTHORITY_MAP — run-local authority map (plan §5)

> **Epistemic status: immutable, source-state-bound evidence artifact** of run
> `RUN_D55_CONCORDANCE_2026-07-11_1904Z` at source state `4c8ed8907`. This map
> classifies surfaces for THIS run; it is not authority and never selects work.
> If two live normative surfaces conflict and precedence is not explicit,
> record `AUTHORITY_CONFLICT` — do not choose.

All paths are relative to `projects/chirality-app-dev/` unless marked
`(repo root)`.

## Function classification (plan §5 table applied to live surfaces)

### Normative scope (defines what is required)
- `docs/PRD.md` — product yardstick.
- `docs/SPEC.md`, `docs/TYPES.md`, `docs/CONTRACT.md`, `docs/DIRECTIVE.md` —
  authority corpus, RATIFIED 2026-07-11, at corpus snapshot **v6** (lifecycle
  regime semantics §4.4 included; D-APP-38 reconciliation applied).
- `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` —
  deliverable decomposition of record; scope amendments via
  `execution/_ScopeChange/_LATEST.md` (resolve live).
- (repo root) `docs/CONTRACT.md`, `docs/SPEC.md`, `docs/TYPES.md`,
  `docs/DIRECTIVE.md` — root canon, RATIFIED 2026-07-11; K-ENGINE-6 strategic
  lens; root SPEC §3.1–3.4 lifecycle regime model.

### Accepted decisions (change or interpret scope through human authority)
- `execution/_Coordination/_DECISIONS/_REGISTER.md` — D-APP-01..55, all RULED;
  ruling records beside it. Notably load-bearing for R0: D-APP-36 (UI
  render-test bar), D-APP-37 (PKG-10 doc-only acceptance), D-APP-40 (terminal
  taxonomy), D-APP-50/D-APP-52 (domain MCP descriptor-only residuals), D-APP-53
  (dep reconciliation), D-APP-54 (lifecycle rebaseline), D-APP-55 (this run).
- (repo root) `docs/governance_harness/_DECISIONS/` — D-GOV-01..09 (root canon
  ratification D-GOV-09).

### Declared current state
- Each deliverable's four-document kit: `Specification.md`, `Datasheet.md`,
  `Procedure.md`, `Guidance.md`, plus `_CONTEXT.md`.
- `_STATUS.md` header fields (`Current State`, SHAs) — also lifecycle evidence.

### Recorded remaining work (sole current work-discovery surface)
- `_STATUS.md` `## Remaining` per deliverable, including source citations and
  `(gated: ...)`/`(stage-gated: ...)` suffixes — preserved unless their owning
  authority changes them.

### Implementation evidence (live behavior/structure; never scope authority)
- `frontend/` — Next.js/Electron app source (`frontend/src/**`,
  `frontend/electron/**`, `frontend/packages/harness-contract/**` pinned per
  D-APP-48).
- Generated caches (`node_modules`, `.next`, `dist`, packaged apps, runtime
  sessions) — evidence only when specifically needed, never source truth.

### Verification evidence (behavior at a named source state)
- `frontend/**/*.test.*` (Vitest), typecheck/build gates;
  `docs/VALIDATION_STRATEGY.md`, `docs/RELEASE_QUALITY_GATES.md`,
  `docs/BUILD_AND_RELEASE.md` — gate definitions.
- (repo root) `tools/practitioner_harness/**` — self-check/status/pytest.
- `execution/PKG-*/1_Working/DEL-*/_run_records/**` — dated run evidence.

### Lifecycle evidence (workflow state; never completeness proof)
- `_STATUS.md` lifecycle rows + `## History`; D-APP-54 rebaseline of record
  (53/53 `IN_PROGRESS` at this run's source state).

### Execution protocol (constrains how work runs; creates no scope)
- `loop/WORKPLAN_2026-07-10_app_dev_loop.md` (newest), `loop/LOOP_INIT.md`,
  `loop/LOOP_RECEIPTS.md` (newest receipt 14) — protocol + handoff context.
- (repo root) `docs/DELIVERABLE_CONCORDANCE_METHOD.md` (RATIFIED) — shared
  method; pinned plan `plans/PLAN_2026-07-10_deliverable_implementation_reconciliation.md`
  @ `551f84ef6` — this run's execution method (provenance class below
  notwithstanding: the pinned revision is incorporated by the D-APP-55 ruling).

### Provenance baselines (re-verify against live tree before relying on)
- `execution/_Reconciliation/DepClosure/_LATEST.md` →
  `CLOSURE_D53A_DEP_RECONCILIATION_2026-07-11_0224Z` (89/100 SATISFIED, 11
  deliberately-open gated rows; per-row bases in the ten
  `Evidence_D53A_Dependency_Reconciliation_2026-07-10.md` records). R0 agents
  re-verify their deliverable's rows; R1 re-verifies the rest.
- Deliverable-local `Dependencies.csv` / `_DEPENDENCIES.md` — live registers
  (current), with the snapshot as baseline.
- `Assessment_INSP-03_*.md` and other inspection assessments — **evidence
  records, not current truth** (plan §1); recency classified per claim row
  (`AssessmentEvidence`; `STALE_ASSESSMENT` where overtaken).
- `execution/_Reconciliation/References/` corpus snapshots — authority-doc
  reference integrity (v6 current).

### FROZEN_PROCESS_INPUT (readable; never judged or repaired by this run)
- (repo root and project) `AGENTS.md`, `agents/AGENT_*.md`, agent matrices,
  skill contracts, agent-workflow guidance. Findings whose resolution requires
  changing these route unchanged to `AGENT_WORKFLOW_OBSERVATIONS.md` as
  `DEFERRED_AGENT_WORKFLOW` (plan §3 boundary 8).

### Historical context (explains provenance; cannot override live authority)
- `plans/**` (incl. this run's pinned plan in its capacity as archive),
  `execution/_Coordination/NEXT_INSTANCE_PROMPT.md`,
  `execution/_Coordination/_COORDINATION.md` (ruled-record stub),
  `plans/PLAN_COMPLETION_LOG.md`, closed queue plans, pilot observations.

## Precedence notes for R0 rows

1. Authority corpus (RATIFIED, v6) > deliverable four-doc kit > implementation
   (evidence only). A ruled decision (register) may amend/interpret either;
   cite it in `LatestDecision`.
2. The D-APP-54 rebaseline demoted lifecycle state without invalidating prior
   evidence — `CHECKING`-era approval SHAs and History are historical
   evidence, usable as inputs to a future declared checking basis, never
   current-state claims.
3. Domain-engine surfaces: F-APP-3 — this run reads, never judges, integration
   level or `_DomainEngines/**`; PKG-10 claims bind to the D-APP-4x F-series
   grants and D-APP-37 doc-only acceptance basis.
4. Cross-project surfaces (`projects/chirality-piping/**`, root canon) are
   read-only context; no piping surface is audited by this run.
