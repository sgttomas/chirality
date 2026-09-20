# Coordination Record - Chirality App Dev

**Epistemic status (rewritten 2026-07-10 at owner adoption, K-AUTH-1).** This file is
now a ruled-record surface and pointer, not the operative protocol. The
development-loop instructions live in `loop/LOOP_INIT.md`. This
file carries only the rules and records that decision packets, register rows, and
receipts name it for. It must never accumulate status, queues, or counts; the
pre-2026-07-10 text is preserved in git history.

Path anchors: resolve `REPO_ROOT` with `git rev-parse --show-toplevel`; set
`WORKING_ROOT` to `{REPO_ROOT}/projects/chirality-app-dev`; paths below are relative
to `WORKING_ROOT`.

## Work discovery (historical ruled record; procedural application superseded)

The paragraph below preserves the 2026-07-10 ruling as history. Its dated
workplan selector and deliverable-only session planning are superseded for
current procedure by the owner-directed amendment recorded in
`AgentRuns/HELP-HUMAN-APP-20260919-LOOP-WORKGRAPH/OWNER_DIRECTION.md` and the
application notice `NOTICE_2026-09-19_APP_LOOP_WORKGRAPH.md`. Current discovery
uses `loop/LOOP_INIT.md`, owner steering and the session work graph, traceable
to the accepted phase DAG. This does not revive any ruled-shut lane or remove
deliverable gates. The original text is not an executable session instruction.

The plans-as-queue convention is retired (owner adoption 2026-07-10, verbatim in
`loop/LOOP_RECEIPTS.md` Receipt 5): work is discovered from deliverable-local
`_STATUS.md` `## Remaining` sections per the newest `loop/WORKPLAN_*.md`. No successor
queue plan will be authored. Which rehomed lanes are live for execution is the
owner's ruling — `D-APP-53` (RULED Option A 2026-07-10,
`_DECISIONS/D-APP-53_RULING_2026-07-10.md`; the ruling preceded the consolidation the
same evening and its dependency-row reconciliation lane is already executed — see the
packet's §7/§8 notes; Option C/D lanes were NOT unlocked). The prior rule
this section replaces — "Do not invent a replacement queue; select new work only from
an explicit human direction or a newly accepted plan/ruling" — survives as: never
manufacture work outside the recorded `Remaining` scope, and honor every `(gated: ...)`
suffix.

## Authority And State Rules (ruled records)

Do not maintain a separate next-instance state file. Current state must be discovered
from authoritative artifacts, dependency evidence, current implementation surfaces,
decision records, validation evidence, and git history. Do not let handoff prose,
completion logs, dependency snapshots, or runtime logs become substitute authority.

Authoritative state:

1. `docs/PRD.md`, `docs/DIRECTIVE.md`, `docs/CONTRACT.md`, `docs/SPEC.md`, and
   `docs/TYPES.md` define requirements, invariants, mechanics, and vocabulary.
2. `docs/PLAN.md` records strategic direction. It is not a work queue.
3. `docs/VALIDATION_STRATEGY.md`, `docs/RELEASE_QUALITY_GATES.md`, and
   `docs/BUILD_AND_RELEASE.md` route evidence and local build/package checks. They do
   not create release readiness, lifecycle issuance, publication authorization, or
   professional acceptance.
4. `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` records the
   package/deliverable decomposition; accepted SCOPE_CHANGE snapshots under
   `execution/_ScopeChange/**` record governed amendments (`SCA-APP-001`:
   provider-adapter generality, Pi pattern-corpus-only posture, capability-forward
   permission governance with explicit hard-deny precedence).
5. Deliverable-local `_STATUS.md` (lifecycle + `## Remaining` open scope), `MEMORY.md`,
   `_run_records/**`, four-document kits, dependency files, and review/evidence files
   carry lifecycle, working memory, and execution evidence inside their ownership
   boundary.
6. Dependency and SCC evidence lives in immutable snapshots under
   `execution/_Reconciliation/DepClosure/**` (`_LATEST.md` is the discovery pointer;
   the accepted snapshot reports strict `scc_count = 0`). Future SCC work follows the
   shared repo-root `docs/CYCLE_DRIVEN_RESOLUTION.md` doctrine: each SCC is resolved by
   a recorded move — decompose / invert / merge / cut (cut/merge human-gated) — and
   cycle-participating edges stay non-gating until resolved.
7. Current implementation truth lives in source, tests, build scripts, validation
   artifacts, and git history.
8. `execution/_Coordination/_DECISIONS/_REGISTER.md` tracks human-gated
   decision-packet status. Agents prepare `PROPOSAL` packets; humans rule.
9. `execution/_Coordination/_LATEST.md` is a discovery pointer for coordination
   surfaces only. It is not authority and must not accumulate state history. There is
   no active `NEXT_INSTANCE_STATE.md`; do not recreate it or use any hand-maintained
   coordination file as the app state.

When guidance surfaces disagree with authoritative surfaces, surface the discrepancy
and correct the guidance surface. Do not silently rewrite authority.

## Active Development Loop

The recurrent procedure lives in `loop/LOOP_INIT.md`; current discovery is
through `_LATEST.md` and the owning run. The session work graph supplies
executable detail, while the owner steers priorities and phase transitions.
It does not replace decomposition truth or authoritative deliverable state.
Historical references to this record's older protocol sections resolve to the
revision cited at the time, retained in Git and the loop archive; they do not
reactivate a dated workplan selector.

## Pointers

- Session entry: `init/dev-loop-init-prompt.md` → `loop/LOOP_INIT.md` → owner-named
  run or applicable discovery/receipt pointers.
- Session plan: owning run work graph; deliverable basis remains
  `execution/PKG-*/1_Working/DEL-*/_STATUS.md` (`## Remaining`) and its contracts.
- Decision register: `execution/_Coordination/_DECISIONS/_REGISTER.md`.
- Discovery pointer: `execution/_Coordination/_LATEST.md`.
- Codex host re-platform (D-GOV-43, topology A2, 2026-09-12): architecture history
  `execution/_Coordination/AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/HANDOFF.md`;
  App application record `_DECISIONS/D-APP-127_RULING_APPLICATION_D-GOV-43_CODEX_HOST_REPLATFORM_A2_2026-09-12.md`.
  The current Shared Runtime Boundary in `{WORKING_ROOT}/AGENTS.md` reflects
  the application-owned Runtime service child, not the retired per-user daemon.
- Role posture: `{REPO_ROOT}/AGENTS.md`, the active role instruction under
  `{REPO_ROOT}/agents/`, and `{WORKING_ROOT}/AGENTS.md`. New chats default to
  HELP_HUMAN; delegation follows the agreed strategy and canonical role rules;
  Git closeout uses the project-scoped `chirality-change` skill.
- Landed-work narrative: `plans/PLAN_COMPLETION_LOG.md` (history, never a queue).
- `execution/_Coordination/NEXT_INSTANCE_PROMPT.md`: dated historical map (pre-loop
  session entry; never authority).
