# Root Governance Loop Handoff State

Four-field form per owner ruling 2026-07-31 (Receipt 72; the ruling
verbatim is in that receipt): this file carries only the fields no other
instrument lawfully holds. Posture lives in `CURRENT_WORKPLAN.md`; session
history and owner directions live in `LOOP_RECEIPTS.md`; attention residue
lives in `_TaskManagement/REGISTER.csv` (rows are never scope, acceptance,
or authority — K-TM-5). Per-run and per-phase handoff states remain inside
their run and snapshot directories per the AGENTS.md handoff-state rule.

## 1. Accepted upstream basis

- Root PRD Revision 8 (`docs/PRD_ROOT.md`), merge-gate policy per annex
  §5.3.1 as simplified 2026-07-29 (Receipt 64).
- Root SOFTWARE decomposition revision 1.2 (SCA-002 applied 2026-07-29;
  snapshot `execution/_ScopeChange/SCA-002_2026-07-29_0800/`). All 46
  deliverables `INITIALIZED`; none activated.
- Chirality Task Management PRD Revision 2, adopted by D-GOV-32 (subject
  SHA-256 `97e2ae6525ecbfdc52ff22aee85e1182a751c1090c2aa2f52faaf9e080f35d18`,
  effective `main@c1156837f`); K-TM-1..6 ratified at `docs/CONTRACT.md`
  §1.14 (effective `main@c8c2a6146`). Stage-A instruments: Receipts 66–73;
  workplan `WORKPLAN_2026-07-31_task_management_stage_a.md` (CLOSED) and
  its Amendments 1–2; program register at
  `execution/_Coordination/_TaskManagement/REGISTER.csv` (103 rows:
  48 CLOSED / 53 DEFERRED / 2 OPEN).
- Stage-A trailing merges (step 8, closure) record their own approved and
  effective SHAs in their PRs and Receipts 72–73 per §5.3.1.
- D-GOV-33 invocation-local federation-survey ruling and completed managed
  run at
  `execution/_Coordination/AgentRuns/TM-FEDERATION-SURVEY-20260802/`
  (Receipts 82 and 85). The validated implementation commit is
  `bb44d71c93cc5431d5fc8a902e716cc88966ea9f`; PR #478 published exact
  approved source `08ed85ae1a1ae2be9eba971e6567fad2bb202b56` from final base
  `4d55dea0f375034b66949723a7b849a2c962d8a3`, effective at merge
  `2c25bd2c47c4b2f4190275ad39579a983f8786aa`. All three required checks
  succeeded; the checked-PR publication lane is closed.

## 2. Derivative-package currency

- `execution/_Coordination/_TaskManagement/.candidates/` — taskmgmt scan
  and federation projections: gitignored, rebuildable, never authority
  (D-GOV-01). Project/domain/Domain Engine federation projections follow the
  same beside-register `.candidates/` rule.
- `/tmp/TM-FEDERATION-SURVEY-20260802-*.json` and verifier/acceptance copies —
  historical pre-publication validation evidence; derived, disposable, and
  not accepted register truth.
- `TRIAGE_2026-07-31_SEED_PROPOSALS.md` and
  `AgentRuns/GOV-TM-TRIAGE-CLUSTER-20260731/` — historical decision
  support and run evidence for the first triage; not current state.
- Public export under `exports/chirality-app/` — stale derivative,
  deferred to the next export release (posture unchanged since SCA-002).

## 3. Closure verdict

`TASK MANAGEMENT STAGE A CLOSED — ROOT LOOP IDLE AND RESUMABLE.`
Steps 0–6 complete with owner rulings recorded and merged; step 7 packets
presented on all three loop surfaces with rulings deliberately trailing to
the individual development loops (owner direction, Receipt 72); step 8
shipped. PRD §19.1 falsification clause satisfied (seed triaged in the
first session, 46/101 closures). No root production phase is active;
Task Management runs on demand or owner-scheduled routine via
TASK_MANAGEMENT — never bound to loop entry.

`FEDERATION SURVEY COMPONENT PUBLISHED AND EFFECTIVE — PR #478 CLOSED.`
HELPS_HUMANS and TASK_MANAGEMENT both returned `READY`; all four validation
surveys were `COMPLETE` with unchanged register hashes. D-GOV-33, the shared
agent/tool, tests, manifest, and notices became repository state at effective
merge `2c25bd2c47c4b2f4190275ad39579a983f8786aa` after all required checks
succeeded.

## 4. Rerun requirement

Refresh this file only when a phase boundary moves: a Stage-B packet is
ruled in a development loop (D-APP-83 / D-63 / D-PEC-72 → close the
matching TM-ROOT-098/099/100 row and migrate linked rows), a Root
production phase or DEL-02-06 activation is selected, the accepted
decomposition or PRD revision changes, or the owner selects a successor
posture other than idle.

The federation-survey rerun and publication requirement was discharged by
PR #478 (Receipts 82 and 85). No further action is required for that tranche.
Rerun its validation and federation matrix only if the shared Task Management
instruction/tool contract or canonical register-discovery shapes change.
