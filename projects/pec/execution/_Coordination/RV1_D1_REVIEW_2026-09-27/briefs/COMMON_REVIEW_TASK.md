# RV1 REVIEW TASK — common brief (both performers)

Parent: WORKING_ITEMS (Type 1), node RV1 of `HELP-HUMAN-PEC-20260927-RV1-INTAKE`,
brief `AgentRuns/HELP-HUMAN-PEC-20260927-RV1-INTAKE/briefs/RV1A_D1_REVIEW.md`
(`3212458cbeabd09d5590c5a9efc694f087f3c4b8b35c38909ef2ccd478ad5d32`). You are a
fresh Type 2 TASK instance (`pec-task`, Opus 5.5 `claude-opus-5-5`, high
reasoning). You do not delegate. Paths below are relative to the repository
root `{REPO_ROOT}` your launch message names, and `{P}` is
`{REPO_ROOT}/projects/pec/execution`.

## Instruction sources (read, and record each SHA-256 in your return)

- `{REPO_ROOT}/AGENTS.md`, `{REPO_ROOT}/projects/pec/AGENTS.md`,
  `{REPO_ROOT}/agents/AGENT_TASK.md`.
- Authority: `{P}/_Coordination/_DECISIONS/D-PEC-107_OWNER_DIRECTION_2026-09-27.md`
  §"RV1 authorization" and §"Freeze point" (`403a0497…def346`), with the owner's
  confirmation "Yes I still want you to complete the task management work and
  the RV1."; it implements `D-PEC-105` RR1
  (`_DECISIONS/D-PEC-105_RULING_2026-09-27.md`, `401c2419…d0ef`; proposal
  `_DECISIONS/D-PEC-105_d1_premise_amendment_proposal_2026-09-26.md`,
  `07761005…ba89f`).
- Method basis: the bundled `review` workflow **as of commit `2f825f180`**. Read
  it only with `git -C {REPO_ROOT} show 2f825f180:workflows/review/WORKFLOW.md`,
  `…:workflows/review/execution.json`, `…:workflows/review/resources/contract.md`,
  `…:workflows/review/resources/method.md`. Expected SHA-256: `f8a8f240…06bc`,
  `d1c668ae…74df`, `d3d7eb27…b328`, `63c8a395…0daa`. Do **not** read or apply
  the working-tree `workflows/review/**` (the revised edition, `77dbfcb72`
  onward: CHECKING-entry, frozen-SHA, Gate 5 and reversal rules). PEC has not
  adopted it.

## Environment rules (binding)

- The repository worktree is **read-only** for you. Never write, create,
  delete, stage, commit, fetch, check out or switch branches there. Never run
  `git fetch`. Read with `cat`, `sed`, `grep`, `git show`, `git log`.
- Before any shell work: `export TMPDIR="$(mktemp -d {SCRATCH}/{NAME}.XXXXXX)"`
  once, then in **every** shell `export TMPDIR=<that dir>` and
  `export PYTHONDONTWRITEBYTECODE=1`. Create and delete files only inside that
  directory. Never write to `/tmp` or `/var/folders`.
- Tools you may run read-only against the worktree:
  `python3 tools/scope_of_work/derive_review_checklist.py --output $TMPDIR/…`,
  `python3 tools/scope_of_work/validate_scope_of_work.py`,
  `python3 tools/validation/validate_decomposition_registers.py --strict projects/pec/execution`
  (run from `{REPO_ROOT}`; output only to `$TMPDIR`).

## Posture (binding)

- The deliverable is `CHECKING`. It stays `CHECKING`. Never propose, prompt
  about or evaluate a lifecycle transition. **Gate 5 is not entered**, as in
  the 2026-08-09 precedent (`{P}/_Evaluation/Reviews/REV_DEL-00-03_2026-08-09_2136/`
  and `…_2156/`).
- The old method's human gates map as follows (record this mapping):
  Gate 1 human input = `D-PEC-107` RV1 authorization (deliverable and review
  type); Gate 2 checklist = the deterministic derivation (copy every `AC-*`
  verbatim, in emitted order; do not rescan, paraphrase, add, drop or reorder);
  no new owner confirmation of the checklist was given, so say so; Gate 3
  findings are `Origin=AGENT_CHECK` agent checks (no human reviewer exists or is
  inferred); Gate 4 `HumanDisposition` stays `TBD` for every new finding and
  `ProposedDisposition` is a labelled PROPOSAL; Gate 5 not entered.
- Old-method step that relies on something not available to you: Gate 1 step 4
  dispatches a TASK with `audit-decomp`. You cannot delegate. Use the nearest
  current equivalent: the strict register validator plus a direct identity
  check of `_CONTEXT.md`, the SOW and the decomposition registers
  (`Deliverables.csv`, `ScopeLedger.csv`, `SOFTWARE_DECOMP.md`), and record the
  substitution. Record any other substitution you make the same way.
- **No CRITICAL or MAJOR finding may be proposed or recorded as `DEFER` or
  `DEFERRED`** (root `docs/SPEC.md` §3.4 allows no deferral carve-outs, even
  though the old edition would). Any later `CHECKING → ISSUED` step still faces
  SPEC §3.4.
- **Freeze point** (`D-PEC-107`): any correction a finding calls for is
  **recorded only, not prepared**. Describe what would have to change in one
  or two sentences; do not draft replacement text. A finding that needs a
  `ScopeOfWork.md` or artifact change needs an owner-ruled correction packet
  before re-acceptance; say so.
- **Acceptance status (state it exactly):** the owner's `ACCEPT_EXACT_BYTES` of
  the new hashes has **not** been given. The prior acceptances lapsed when the
  `D-PEC-105` act landed (proposal "Acceptance-lapse account"). The owner-only
  criterion (DEL-00-01 AC-007; DEL-00-03 AC-011) is **unsatisfied** for these
  bytes until the owner's act, which is the next step. Mark it "READY FOR OWNER
  DECISION" (or "NOT READY" with the reason) — never satisfied.
- **Revised-edition consequence (record once, no prompt):** the revised `review`
  edition (not adopted by PEC) would surface a deliverable that entered
  `CHECKING` under an earlier override without a recorded frozen SHA or
  checking basis for a human ruling that records them, or for reversal. Both
  D1 deliverables entered `CHECKING` under the D-PEC-72 override. This is
  recorded as a consequence for the owner's reserved decision under that
  edition if PEC ever adopts it; nothing here prompts about CHECKING.
- Severity scale (old method): CRITICAL blocks issuance (fundamental
  correctness); MAJOR must resolve before advancing (significant technical
  issue, including a criterion the bytes fail); MINOR should resolve (quality);
  OBSERVATION noted for record. Judge honestly; do not inflate or suppress. If
  there are no CRITICAL or MAJOR findings, say so plainly.
- Assess the **current bytes** only, after verifying their SHA-256. Stop and
  return if any differs.

## Inputs common to both

- The derived checklists (already produced by the manager, twice, byte-identical):
  `{P}/_Coordination/RV1_D1_REVIEW_2026-09-27/checklists/checklist_DEL-00-01.json`
  (`6e99f93c…8cf9`) and `…/checklist_DEL-00-03.json` (`a3bc80a0…21b1`).
  Re-derive yours into `$TMPDIR` and confirm it is byte-identical.
- The `D-PEC-105` act run root `{P}/_Coordination/D1_PREMISE_AMEND_2026-09-27/`
  (notably `HANDOFF_STATE.md` items 6–7, `premise/*.json`, `VALIDATION.md`).
- The proposal's "Other findings" 1–11 and "Acceptance-lapse account".
- Intake `{P}/_Coordination/_TaskManagement/TM_PEC_CLOSEOUT_POST_SCA005_2026-09-27/INTAKE.md`
  CAND-PEC-2026-09-27-01, item 8 (and item 6 where it names these
  deliverables). Under `D-PEC-107` CAND-01 (b) these are **inputs** to this
  REVIEW and corrected only by an owner-ruled packet.
- Current basis: decomposition revision 1.6 at `189f205ff`
  (`{P}/_Decomposition/`, `_LATEST.md`), `projects/pec/docs/PRD.md` v2.4.
- The reliance-hold preflight is already run by the manager
  (`…/RV1_D1_REVIEW_2026-09-27/evidence/reliance_hold_preflight.out`: ALLOW ×8,
  `candidate-validation` being the matching review operation). Cite it; do not
  rerun it into the repository.

## What to produce (drafts in `$TMPDIR/out/`, repository-relative paths only, no machine-absolute paths, no trailing whitespace)

1. `_REVIEW.md` — the complete new deliverable review record. Structure:
   - header block: review stage (for example `REVIEW COMPLETE FOR THE D-PEC-105
     BYTES — OWNER EXACT-BYTE ACCEPTANCE PENDING — GATE 5 NOT ENTERED`), review
     type, reviewer identity and independence, date 2026-09-27, lifecycle
     `CHECKING` unchanged, authority (quote the `D-PEC-107` owner lines you rely
     on verbatim), method basis with the four hashes and every substitution;
   - review basis (every input hash), Gate 1 preconditions, Gate 2 checklist
     (AP, all `AC-*` rows with exact text, verification, source binding
     `qualified ID; SOW SHA-256; line`, and result), OC, XD, DS, TB,
     review-type-specific rows, Gate 3/4 findings and the findings summary
     table (Total/Resolved/Open/Deferred — Deferred must be 0 for CRITICAL and
     MAJOR), the acceptance status and next step, the freeze-point limit, the
     revised-edition consequence, and "Transition readiness: no transition
     attempted; Gate 5 not entered";
   - then `## History — prior review record (describes superseded bytes)`:
     one sentence naming the prior file's SHA-256 and saying its acceptance
     lapsed under `D-PEC-105`, followed by the **entire prior `_REVIEW.md` body
     verbatim**, with only its heading levels demoted by one `#` (disclose
     that). Do not alter any quoted owner ruling.
2. `Review_Findings.csv` — the complete file: the existing header and existing
   rows byte-identical, then your new rows (continue `RF-NNN` numbering), with
   the old schema's 14 columns, RFC-4180 quoting, `Date` 2026-09-27,
   `HumanDisposition=TBD`, `Status=OPEN`, `Origin=AGENT_CHECK`,
   `ReviewerID` = your reviewer identity.
3. `snapshot/Brief.md`, `snapshot/RUN_SUMMARY.md`, `snapshot/Review_Summary.md`,
   `snapshot/Decision_Log.md`, `snapshot/QA_Report.md` — in the short form of
   the precedent snapshots. Write `{SNAPSHOT_NAME}` wherever the snapshot's own
   folder name is needed; the manager fills it at finalization.
4. `evidence/` — the commands you ran, their cwd, interpreter and exit codes,
   and outputs (checklist re-derivation, validator, strict registers, the
   hash checks, any grep you rely on for a finding).

## Return (SubagentHandback)

Your reviewer identity and independence statement; the instruction-source and
method hashes you verified; the target hashes; per-row results (AP, AC, OC,
XD, DS, TB, type-specific); every finding with severity, evidence and the
correction it calls for (recorded only); the owner-only criterion status; the
substitutions; the list of drafts with SHA-256; and anything the manager must
resolve. Do not claim acceptance, readiness, release or reliance.
