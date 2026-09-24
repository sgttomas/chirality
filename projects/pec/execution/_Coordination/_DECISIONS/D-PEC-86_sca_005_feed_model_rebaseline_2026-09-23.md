# D-PEC-86 — SCA-005 feed-model rebaseline and companion P1 continuation

Status: **RULED BY OWNER DIRECTION (2026-09-23, in session) / SCA-005 GATE 1
OPENED / CHECKPOINT GROUPS 1–3 REMAIN OWNER ACCEPTANCES.** This record
transcribes the owner's chat direction verbatim and states Agent 0's
interpretation of its scope separately. It creates no decomposition, PRD,
lifecycle, source, release or reliance act. Basis: `origin/main`
`d61981ee2b9e36c82c6cdd28d4f3c12d3d32a69b`.

Prepared by HELP_HUMAN (Agent 0), served by Claude Fable 5.1 as reported by the
host; role instruction-asserted, not mechanically enforced.

## 1. Owner direction of record (verbatim)

Session opening steer (owner, 2026-09-23):

> This session we are going to assess what has transpired with the App and
> Piping projects and how to advance the PEC project in unison.

Agent 0 returned the assessment now preserved at
`../ASSESSMENT_2026-09-23_APP_PIPING_PEC_UNISON.md`, ending with four numbered
recommendations, a list of reserved owner decisions, and the offer: "If you
agree, I will record this assessment under `execution/_Coordination/`, append
Receipt 179, and draft the D-PEC-86 proposal packet for SCA-005 on a branch for
your ruling."

Owner response (verbatim):

> Proceed with SCA-005 and what follows in your recommendations.  You are
> Agent 0, so consider effective delegation to your Type 1 and Type 2
> instances.  Use `opus-5.5` models on `high` reasoning for all subagents.  You
> can continue working within your capacity of HELP_HUMAN, anticipating my
> needs and those of the agents under you.

## 2. Referent — the recommendations the direction adopts

Carried from the assessment record (Agent 0 text, not owner text):

1. Open SCA-005 to rebaseline PEC's feed model on the shared 2026-09-22 method
   and the A2 Runtime topology, producing a PRD v2.3 candidate, decomposition
   revision 1.5 and a Scope of Work currency list; fold in the adopted but
   unapplied PRD §16.3 postimage (D-PEC-79) and the nine TM-PEC-023 objective
   blanks.
2. Use the 2026-09-23 App and Piping trial runs as the first external
   self-ingestion fixtures.
3. Keep P1 moving underneath: the three DEL-01-03 evidence inquiries are
   read-only and independent of SCA-005.
4. Defer PEC's own loop migration to the shared method until SCA-005 closes.

Reserved decisions named in the assessment: authorize SCA-005 or continue P1
as scoped; authorize the DEL-01-03 inquiries; grant the STATUS.md currency
clause; rule when PEC adopts the shared loop method.

## 3. Agent 0 interpretation of scope (interpretation, not owner text)

| Ref | Element | Interpretation | Owner checkpoint that still remains |
|---|---|---|---|
| I-1 | SCA-005 | Opened at Gate 1 under `chirality-root:bundled:workflow:scope-change` (SOFTWARE variant). This run prepares the complete checkpoint-group-1 package (Brief, validated atomic actions, pre-change coverage baseline, Impact Assessment, Decision Log, proposed Amendment_Actions). No canonical truth, register, pointer, SOW, metadata or foreign surface changes before the owner accepts checkpoint group 1. | Checkpoint 1 (impact), 2 (exact amendment and propagation plan), 3 (audited poststate) |
| I-2 | D-PEC-79 PRD v2.3 postimage | Consumed as an exact, immutable input to SCA-005 intake. Its live application remains withheld exactly as D-PEC-79 ruled; SCA-005 checkpoint 2/3 is the candidate "later application tranche" only if the owner accepts it there. | Checkpoint 2 |
| I-3 | TM-PEC-023 nine objective blanks | The prepared decision surface is carried into SCA-005 intake as candidate MODIFY actions per row; no mapping or blank retention is selected by agents. | Checkpoint 2 row-by-row selection by the owner |
| I-4 | DEL-01-03 REM-001..003 | Read as authorized by recommendation 3 together with the owner's "what follows in your recommendations". WORKING_ITEMS may run the three read-only inquiries and create the derivative report and evidence manifest at the exact gated paths, after the exact-target reliance preflight per item, and append a MEMORY run entry. `_STATUS.md` and the Remaining checkboxes are not edited; the return proposes their disposition. No production, contract, test, acceptance or lifecycle act. | Owner disposition of each returned obligation and of the Remaining items |
| I-5 | STATUS.md / README currency | Read as the packet clause the reserved decision named: one bounded present-current refresh of `docs/STATUS.md` and `README.md` prose (current basis, current gates, pointers), performed only after the checkpoint-1 package exists, asserting no acceptance that did not occur. | None beyond ordinary review |
| I-6 | Task Management | The three 2026-09-23 Root notices (`NOTICE_2026-09-23_APP_PIPING_RECEIPTS.md`, `..._EVERGREEN_LOOP_INSTRUCTIONS.md`, `..._SCOPED_PR_CI.md`) are triaged into the PEC register under D-PEC-73 Option A as additive rows; no closure without evidence. | None beyond ordinary review |
| I-7 | PEC loop migration | Deferred per recommendation 4; no act in this run. | Later owner ruling |
| I-8 | Delegation and models | Type 1 and Type 2 instances are dispatched through gitignored `.claude/agents/` definitions `pec-manager`, `pec-task`, `pec-reviewer` with `model: opus` (resolves to `claude-opus-5-5`) and `effort: high`. Role identity is instruction-asserted; serving identity is whatever the host reports. | None |

If the owner reads any element differently, the corresponding writes are new
files or additive rows and revert cleanly (see §6).

## 4. Exact write targets opened by this record (all under `projects/pec/`)

| Target | Act | Owner |
|---|---|---|
| `execution/_Coordination/_DECISIONS/D-PEC-86_sca_005_feed_model_rebaseline_2026-09-23.md` and one `_REGISTER.md` row | Create / add row | HELP_HUMAN |
| `execution/_Coordination/ASSESSMENT_2026-09-23_APP_PIPING_PEC_UNISON.md` | Create | HELP_HUMAN |
| `execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260923-SCA005/**` | Create run record, briefs, supplied basis, returns | HELP_HUMAN |
| `execution/_Coordination/SCA-005_PREP_2026-09-23/**` | Create survey, impact inventory, feed-model design annex | TASK / HELPS_HUMANS instances |
| `execution/_ScopeChange/SCA-005_<YYYY-MM-DD>_<HHMM>/{Brief.md,Impact_Assessment.md,Pre_Change_Coverage.json,Decision_Log.md,Amendment_Actions.csv,Handoff_State.md}` | Create checkpoint-group-1 package only (the contract requires `Handoff_State.md`; added 2026-09-23 after review F1 noted its omission from this list); `_LATEST.md` and `checkpoint_snapshots/` untouched until owner acceptance | WORKING_ITEMS (scope-change) |
| `execution/_Evaluation/DecompCoverage/COV_SCA005_PRECHANGE_<ts>/**` | Create immutable pre-change audit snapshot; `_LATEST.md` untouched | TASK (audit-decomp) |
| `execution/PKG-01_Service_Core_Store/1_Working/DEL-01-03_Store_bootstrap_content_minimal_guard/_run_records/REMAINING_EVIDENCE_DEL-01-03-REM-00{1,2,3}/**` and that deliverable's `MEMORY.md` | Create reports and evidence manifests; append one MEMORY run entry | WORKING_ITEMS (DEL-01-03) |
| `execution/_Coordination/_TaskManagement/REGISTER.csv` and `_TaskManagement/NOTICE_TRIAGE_2026-09-23.md` | Additive rows; triage record | TASK (task-management) |
| `docs/STATUS.md`, `README.md` | Present-current prose refresh only | TASK, after checkpoint-1 package exists |
| `loop/LOOP_RECEIPTS.md` | Append Receipt 179 (and later receipts in this run) | HELP_HUMAN |

Not opened: any `v2/**` source, test or configuration; `software-workflow.json`;
any `ScopeOfWork.md`; any `_STATUS.md`; live `docs/PRD.md`; live
`_Decomposition/**`; `_ScopeChange/_LATEST.md`; `_DomainEngines/**`; any
App, Piping, Runtime or Root path; live materialization of D-PEC-79.

## 5. Checks

`python3 tools/validation/validate_pec_loop_receipts.py --repo-root .` before
and after each receipt; `PYTHONDONTWRITEBYTECODE=1 python3
tools/practitioner_harness/harness.py self-check`; Task Management validators
on both registers; `python3 tools/validation/validate_decomposition_registers.py
projects/pec/execution --strict` (read-only confirmation that no register
changed); PEC reliance-hold preflight per exact target and operation; fresh
read-only independent review (`pec-reviewer`) of the whole candidate before
the PR; hosted CI on the actual head. Merge under the 2026-09-12 standing Git
authorization only when CI passes and review has no unresolved blocking
finding; the owner's checkpoint acceptances are never inferred from a merge.

## 6. Rollback

Revert the run's PR. Every write is a new file, an additive register/receipt
row, a MEMORY append, or present-current prose in STATUS/README; no preimage of
canonical truth changes.

## 7. What the owner will be asked next

Checkpoint group 1: confirm or modify the parsed SCA-005 change set and accept
the Impact Assessment (exact SHA-256 will be quoted). Separately: the DEL-01-03
inquiry returns list exact unresolved obligations for disposition.

## 8. Corrections appended 2026-09-23 (after independent review F1)

- §3 row I-8 and the packet's original wording said dispatch went through the
  gitignored `.claude/agents/` definitions `pec-manager`, `pec-task` and
  `pec-reviewer`. The host's agent roster is fixed at session start, so those
  definitions were not selectable. Every Type 1 and Type 2 instance actually
  ran as the host's `general-purpose` agent with `model: opus`
  (`claude-opus-5-5`); high reasoning was requested in each brief and is not
  tool-pinned; read-only limits are instruction-asserted. The authoritative
  record is `../AgentRuns/HELP-HUMAN-PEC-20260923-SCA005/SUPPLIED_BASIS.json`.
- §4 originally omitted `Handoff_State.md` from the SCA-005 snapshot row; the
  scope-change contract requires it and SCA-004 carries one. The row above is
  amended in place because this packet is still uncommitted; no ruling text
  changed.
- Reliance-hold preflights were recorded for the C1 (×3), B1 (×5 plus the
  audit child) and D1 (×2) targets. A1, A2, A4, E1 and HELP_HUMAN's own
  coordination writes did not record a preflight; the register is header-only
  at this basis, so every such check would return `ALLOW`, and Receipt 179's
  wording is narrowed accordingly.
