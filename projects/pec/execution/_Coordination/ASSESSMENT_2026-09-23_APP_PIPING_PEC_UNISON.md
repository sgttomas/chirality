# Assessment — App, Piping and PEC in unison (2026-09-23)

Prepared by HELP_HUMAN (Agent 0) at the owner's request for this session.
Basis: `origin/main` `d61981ee2b9e36c82c6cdd28d4f3c12d3d32a69b` (observed after
fetch; the assessment itself was read at `06aff05a412b9e25ad022e5fc629c77ee51efbc6`,
which differs only by the Piping D-76 merge). This is an orientation record and
Agent 0 judgment, not a ruling, a scope change, or a lifecycle act. Cited files
govern on disagreement.

## Where the three projects stand

**App.** v3.0.0 is released for Apple Silicon with Codex as the only engine.
D-GOV-43 topology A2 replaced the per-user Runtime daemon with a Runtime
service the App starts and owns as a child process, with app-private tokens.
The whole-corpus deliverable concordance RUN_D128 ran R0 to R6 and closed on
2026-09-22 (D-APP-128 to D-APP-131). On 2026-09-22/23 the App retired its
legacy `## Remaining` lists into Scope of Work and Task Management, adopted the
evergreen development loop, and ran its first trial on it (DEL-05-04 replay
boundary; PRs #866 and #868 merged). Task Management: 7 open, 14 deferred.

**Piping.** D-70 to D-76 landed in the last week (UI redesign sequencing,
performance criteria, whole-corpus reconciliation D-73 through R6, MIT
relicense, DEC-046 and nonlinear unit corrections). Piping retired its live
`## Remaining` sections on 2026-09-23, carrying 204 clauses into governing
documents. Two loop trials ran and merged the same day (DEC-025 clean-base
repair, PRs #872/#873; linter scope boundary, PRs #867/#876), each ending with
one central receipt under `AgentRuns/<RunID>/RECEIPT.md`. Task Management:
7 open, 32 deferred.

**Runtime.** PR #880 added `docs/APPLICATION_CONSUMER_GUIDE.md` for a second
host: Piping's first path is a development Codex session over the Piping JSON
CLI; any new consumer runs its own Runtime instance rather than attaching to
the App's socket. PEC compatibility is stated as unverified and not an MVP
prerequisite.

**PEC.** Loop consolidated under D-PEC-80; D-PEC-81 to 84 applied Remaining
concordance and scanner repair; D-PEC-85 produced the first store and
content-minimal guard slice (DEL-01-03 `IN_PROGRESS`). Lifecycle census at
this basis: 32 OPEN, 26 INITIALIZED, 4 CHECKING, 2 IN_PROGRESS; 89 Remaining
items across 57 deliverables, every one owner-gated. Receipt validator, hold
preflight and Task Management validators pass. `docs/STATUS.md` still
describes early August. Three 2026-09-23 Root notices post-date the last
federation pass (Receipt 178).

## The unison problem

PEC's accepted basis (PRD v2.2, decomposition revision 1.4) models the sister
loops as they were in July. Both loops converged this week on one shared file
shape. PEC's ingest contract (PRD row PEC-RCN-002) and the PKG-02 parser
contracts now name surfaces those loops no longer write.

| PEC basis assumes | App and Piping now write |
|---|---|
| `WORK_GRAPH.json` under AgentRuns | `WORK_GRAPH.md` under `execution/_Coordination/WorkGraphs/<undertaking>/` |
| Per-loop `LOOP_RECEIPTS.md` grammars (D-APP-57) | One `AgentRuns/<RunID>/RECEIPT.md` per undertaking; ledgers historical |
| `## Remaining` as the work surface | Retired; Scope of Work, decisions, graph and Task Management govern |
| Workplan and LOOP_INIT with steps and gates | Evergreen LOOP_INIT; workplans retired |
| Shared Runtime daemon for presence and SSE | App-owned Runtime service per application (D-GOV-43 A2) |
| MEMORY as decisions and evidence | MEMORY `## Runs` index table |

PKG-06 and PKG-07 carry no Scope of Work yet, so the daemon-topology drift
sits in the PRD and decomposition. PRD §12 anticipates this: generality is
tested against a structurally different loop, and observed drift becomes a
scope-change request rather than silent parser work.

## Recommendation (as given to the owner)

1. Open SCA-005 to rebaseline PEC's feed model on the shared 2026-09-22 method
   and the A2 Runtime topology, producing a PRD v2.3 candidate, decomposition
   revision 1.5 and a Scope of Work currency list; fold in the adopted but
   unapplied §16.3 postimage (D-PEC-79) and the nine TM-PEC-023 objective
   blanks.
2. Use the 2026-09-23 App and Piping trial runs as the first external
   self-ingestion fixtures.
3. Keep P1 moving underneath: the three DEL-01-03 evidence inquiries are
   read-only and independent of SCA-005.
4. Defer PEC's own loop migration to the shared method until SCA-005 closes.

Owner decisions reserved at the time: authorize SCA-005 or continue P1 as
scoped; authorize the DEL-01-03 inquiries; grant the STATUS.md currency
clause; rule when PEC adopts the shared loop method. The owner's response is
recorded verbatim in `_DECISIONS/D-PEC-86_sca_005_feed_model_rebaseline_2026-09-23.md`.

## Correction appended 2026-09-23 (after survey A1, DR-13)

The Piping paragraph above says both 2026-09-23 trials ended "with one central
receipt under `AgentRuns/<RunID>/RECEIPT.md`". The hash-bound survey
(`SCA-005_PREP_2026-09-23/SURVEY_SISTER_LOOP_FILE_TRUTH.md`, DR-13) shows only
the linter-scope run has a `RECEIPT.md`; the DEC-025 clean-base run recorded
`AgentRuns/PIP-DEC025-BASELINE-2026-09-23/EVIDENCE.md`, and the App replay
trial has no AgentRuns record. The survey also counts six loops rather than
five (Runtime added; Bridge inactive since 2026-08-02). The original text is
left in place as the record of what was presented to the owner.
