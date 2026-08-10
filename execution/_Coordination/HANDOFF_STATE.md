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
  `execution/_Coordination/_TaskManagement/REGISTER.csv` (21 live rows:
  11 OPEN / 10 DEFERRED; 102 rows archived in `REGISTER_CLOSED.csv`). Receipt
  91 repaired the earlier stale handoff to the then-current generational-pass
  state of 27 live (16 OPEN / 11 DEFERRED) and 95 archived. Receipt 92 then
  recorded the separately owner-ruled closure and archival of TM-ROOT-105,
  TM-ROOT-109, and TM-ROOT-121, producing 24 live (13 OPEN / 11 DEFERRED) and
  98 archived. Receipt 96 subsequently recorded the accepted-repair closure
  and archival of TM-ROOT-112, producing 23 live (12 OPEN / 11 DEFERRED) and
  99 archived. Receipt 102 then recorded the 2026-08-08 generational pass:
  one DEFERRED promotion followed by three owner-ruled closures/archives,
  producing 21 live (12 OPEN / 9 DEFERRED) and 102 archived. This
  2026-08-09 bounded currentness session independently re-derived those
  entry counts from the CSVs; the owner-ruled deferral of TM-ROOT-119 then
  changed only the live split to the current 11 OPEN / 10 DEFERRED, leaving
  the validated totals at 21 live / 102 archived.
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
- Current Root Task Management decision support under
  `execution/_Coordination/_TaskManagement/`: the TM-ROOT-116 exact Step-0
  draft remains derivative decision support; its exact bytes were owner-ruled
  and applied to the standing idle workplan, but TM-ROOT-116 remains OPEN
  pending later disposition after PR/merge evidence. The TM-ROOT-105 drift
  analysis remains derivative evidence for the owner-ruled mechanical
  EvidenceSha re-pin; the archived row's existing ruling and closure meaning
  are unchanged and it was not re-closed. The session report is derivative
  closeout support, not authority.

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

`2026-08-09 BOUNDED GOVERNANCE-CURRENTNESS SESSION CLOSED — ROOT LOOP IDLE AND
RESUMABLE.` Receipt 103 records the terminal Task Management breadcrumb.
TM-ROOT-119 is ruled DEFERRED and recorded verbatim, with no partial
convergence implementation. The stale register counts are refreshed above.
The owner-accepted Step 0 is applied to the standing idle workplan while
`CURRENT_WORKPLAN.md` remains unchanged; TM-ROOT-116 remains OPEN pending
later disposition after publication/merge evidence. Archived TM-ROOT-105 now
pins the current normalized bytes with both-hash/commit provenance; its
EvidenceRef, Disposition, Closed date, EvidenceQuote, ruling text, and closure
meaning are unchanged, and this was not a re-close. The bounded tranche is on
`codex/root-governance-currentness-20260809` for CHANGE publication by
non-draft PR; commit, push, PR, and merge are not closeout facts at this
handoff, and merge remains prohibited in-session.

## 4. Rerun requirement

Refresh this file only when a phase boundary moves: a Stage-B packet is
ruled in a development loop (that trigger has fired — D-APP-83, D-63, and
D-PEC-73 are ruled and TM-ROOT-098/099/100 are closed; the register-count
refresh above records it), a Root
production phase or DEL-02-06 activation is selected, the accepted
decomposition or PRD revision changes, or the owner selects a successor
posture other than idle.

The federation-survey rerun and publication requirement was discharged by
PR #478 (Receipts 82 and 85). No further action is required for that tranche.
Rerun its validation and federation matrix only if the shared Task Management
instruction/tool contract or canonical register-discovery shapes change.

After the human-gated PR merges, re-open the merged workplan and archived row,
reproduce their accepted hashes, and return TM-ROOT-116 to the owner for a
separate disposition; this session supplies no closure authority for that row.
Rerun Root live/archive register validation, invocation-local federation,
available App/Piping receipt validators, Root G0–G4, candidate-whitespace, and
Git diff hygiene if publication rebasing changes any tranche byte. The
repository still has no Root-specific receipt validator at this basis; do not
misstate the App/Piping validators as Root coverage. Manual closeout checks
confirm Receipt 103 is append-only, unique as a new ID, and follows the latest
Receipt 102; they also expose two pre-existing historical headings numbered
Receipt 80. That historical duplicate was not created or altered here and is
outside this bounded repair. The loop remains idle; release requires a
separately authorized bounded lane or an owner-selected successor phase.
