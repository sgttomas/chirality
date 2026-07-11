# RUN_BASIS — Deliverable–Implementation Concordance Run

> **Epistemic status: immutable, append-only, source-state-bound evidence artifact.**
> Not a queue, not a selection surface, not authority (plan §9; kernel §5).

- **RunID:** `RUN_D55_CONCORDANCE_2026-07-11_1904Z`
- **Activation authority:** D-APP-55 ruling — Option A, whole corpus (all 53
  deliverables), no riders. Ruling record:
  `execution/_Coordination/_DECISIONS/D-APP-55_RULING_2026-07-11.md`; register
  row RULED; both merged to `main` at `4c8ed8907` (PR #178) before this
  dispatch (§3b/§6 hard rule satisfied).
- **Pinned execution method (plan §3b / packet §5):**
  `plans/PLAN_2026-07-10_deliverable_implementation_reconciliation.md` at
  pinned `main` revision **`551f84ef6`** (plan content revision `ef137e025`).
  Verified byte-identical between `551f84ef6` and this run's source state.
  Shared method kernel: `docs/DELIVERABLE_CONCORDANCE_METHOD.md` (RATIFIED
  2026-07-11); kernel governs the shared method, the pinned plan governs
  project adoption parameters; conflicts are surfaced (`AUTHORITY_CONFLICT`),
  never precedence-invented.
- **Source state under review:** `main` = `4c8ed8907` (PR #178 merge),
  worktree branch `claude/app-dev-concordance-da0910` fast-forwarded to it.
  Every evidence citation in this run binds to `4c8ed8907` unless a row says
  otherwise; material corpus change during the run marks affected claims
  `STALE_INPUT` (plan §4 tail).
- **Corpus census at dispatch (re-enumerated live):** 11 packages
  (`PKG-00`..`PKG-10`), 53 `1_Working/DEL-*` deliverables, 53/53
  `IN_PROGRESS`, zero `CHECKING`, zero `ISSUED`; all 53 carry the ungated
  concordance bootstrap `## Remaining` item at pinned revision `551f84ef6`.
- **Concurrent-session check (plan §4 item 7):** primary checkout dirty state
  at dispatch touches only surfaces outside `projects/chirality-app-dev/**`
  (root `AGENTS.md`, `domains/piping-design/**` audit data,
  `projects/chirality-governance/**` deletions — the known external-state
  delta of loop Receipt 4). No app-dev file is being modified by another
  session; nothing deferred for contention at R0 dispatch.
- **Phase discipline:** R0 method calibration FIRST on the sample below; R0
  findings are reported to the owner before any R2 scaling (owner launch
  direction, quoted in the ruling record). Discovery (R0–R3) is read-only
  outside this run folder; repair is R5, separately gated at the R4 human
  decision gate; no lifecycle transitions; no `CHECKING -> ISSUED` (F-APP-4);
  claim-level dispositions only; no agent disposition is represented as a
  human ruling.

## R0 calibration sample (three deliverables, deliberately diverse claim character)

| Deliverable | Why in the sample |
|---|---|
| `DEL-02-01_Desktop_Shell_and_Matrix_Navigation` | Plan §8/R0 recommended first sample: the pilot observed stale-assessment risk here (assessment reporting the loop-first pivot as drift; plan §2, unverified — re-derived by this run). UI claim class exercises the D-APP-36 render-test evidence bar. |
| `DEL-03-04_Interrupt_Cancel_and_Terminal_Outcome_Handling` | Behavioral runtime claim class with test evidence and a governing ruling (D-APP-40 terminal taxonomy) — exercises `LatestDecision` mapping and implementation/verification evidence binding. |
| `DEL-10-01_DomainEngineProfile_Contract_Draft` | Doc-only acceptance basis (D-APP-37) with gated residuals (D-APP-50/D-APP-52 descriptor-only scope) — exercises `RemainingGate` / `SelectableUnderCurrentLoop` derivation and the F-APP-3 domain-engine boundary discipline. |

R0 does not rewrite deliverables (plan §8/R0). The run-local method is revised
per R0 findings before R1/R2 scaling; method revisions are recorded in the R0
calibration report in `R0_CALIBRATION/`.

## Execution roster

Orchestrator: app-dev work loop session (Claude Fable 5), branch
`claude/app-dev-concordance-da0910`. R0 fan-out: three `fable` TASK agents at
high reasoning effort (owner steer of record: fable models only), one per
sample deliverable, disjoint write scopes — each writes exactly
`R0_CALIBRATION/<DEL-ID>_claims.csv` and `R0_CALIBRATION/<DEL-ID>_notes.md`
in this run folder and nothing else.
