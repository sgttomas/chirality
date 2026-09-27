# Brief TM1 — record the owner's intake dispositions and the K3 row, and route CAND-03 to Root (WORKING_ITEMS)

- **Parent:** HELP_HUMAN.
- **Undertaking:** `HELP-HUMAN-PEC-20260927-RV1-INTAKE`, node TM1 (graph `projects/pec/execution/_Coordination/WorkGraphs/HELP-HUMAN-PEC-20260927-RV1-INTAKE/WORK_GRAPH.md`).
- **Role:** WORKING_ITEMS (Type 1), running `chirality-root:bundled:workflow:task-management`. Record the SHA-256 of each method file you load.
- **Model:** `claude-opus-5-5`, high reasoning.
- **Branch:** `claude/pec-tm1-intake-dispositions`, in your own isolated worktree, cut from fresh `origin/main`, which contains PR #1018 (`D-PEC-107`).

## Authority

The authority is the owner's direction recorded in `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-107_OWNER_DIRECTION_2026-09-27.md`, including its §Freeze point. The owner also confirmed, verbatim: "Yes I still want you to complete the task management work and the RV1." Promotion and disposition are the owner's acts. The owner has made them; you record them faithfully and invent none.

The intake is `projects/pec/execution/_Coordination/_TaskManagement/TM_PEC_CLOSEOUT_POST_SCA005_2026-09-27/INTAKE.md`. The live register is `projects/pec/execution/_Coordination/_TaskManagement/REGISTER.csv`, with the closed register beside it. Follow PEC's existing Task Management conventions: row IDs `TM-PEC-NNN`, fields, status vocabulary, evidence columns, and `taskmgmt validate`.

## Do

1. **CAND-PEC-2026-09-27-01.** Record the owner's disposition (b) on the candidate in the intake record, in PEC's convention for a candidate that is disposed without promotion.
   - Each residual contract item is absorbed by its own deliverable's first production or currency packet. The PKG-02 items go with the first parser packet. The DEL-00-01 and DEL-00-03 items go with RV1: they are inputs to that REVIEW, and any correction needs an owner-ruled packet.
   - Do not create one register row per item. The candidate's item list stays the reference those packets use.
2. **CAND-PEC-2026-09-27-02.** Promote it to one register row.
   - Its resolution is the next PEC scope change (bundling the listed decomposition and PRD wording), plus an instruction-tranche item for the `AGENTS.md` sentence.
   - Add to that row, as a design consideration, the per-project consumer contract with PEC: what each project takes from PEC and on what terms, as the counterpart of each loop's feed-profile row; who writes each side; and its relation to the PRD §12 reliance gate.
   - Mark the row plainly as a consideration for the owner's ground-up reassessment under the `D-PEC-107` freeze point, not as scheduled work.
3. **CAND-PEC-2026-09-27-03.** Promote it to one register row and route it to Root.
   - Write one coordination notice at `execution/_Coordination/NOTICE_2026-09-27_PEC_HOSTED_CI_V2_CHECKS.md` (Root's coordination folder, the form of earlier PEC notices there, e.g. `NOTICE_2026-09-25_PEC_DEVELOPMENT_LOOP_ADOPTION.md`).
   - The notice asks Root to consider allocating hosted CI for PEC v2's registered checks, with a full-history checkout. Its evidence is `pec-tests.yml` running only the frozen `npm test`, and `v2/**` routing to that job.
   - Make clear it is a request for Root's own intake decision, and that PEC is at an owner-declared freeze point.
4. **K3.** Open one register row for the tier-0 publication record: a single tool entry in `_DomainEngines/profiles/pec.yaml`, a tier-0 act the owner rules. It replaces the carried graph node.
   - **Trigger:** a DEL-08-06 production packet that fixes the tool's exact shape (DEL-08-06 TBD-003, TBD-004 and TBD-006).
   - **Include:** DEL-08-06 TBD-007 and CON-002, the question whether producing and testing tool definitions inside PEC before this act counts as declaring or invoking.
   - **Source:** SCA-006 `Propagation_Plan.md` §B6. PEC decides what it publishes, and consumers enable it themselves.
   - **Wording notes (PR #994 review 02):** TBD-004's owners include the access-class decision-logic owners, and CON-002 is the owner's question.
   - **Provenance:** state that the row is HELP_HUMAN's interpretation under `D-PEC-107`, and that it departs from the intake's "already homed" judgment. Mark the row as a consideration under the freeze point.
5. **DEL-01-06 `D-PEC-96` MEMORY row:** kept. Record nothing beyond a one-line note in the intake record's outcome.
6. **Validation.** Run `taskmgmt validate`, or the repository's Task Management validator, on both registers. It must pass, and the strict decomposition registers, the harness self-check (`tools/practitioner_harness/harness.py self-check`) and `validate_pec_loop_receipts.py` must give output identical to `origin/main`.
7. **Verification.** Have one fresh read-only `pec-reviewer` (opus) verify that the rows and dispositions faithfully record `D-PEC-107` and follow conventions. Wait for it inside your turn.

## Write boundary

You may write only these paths:
- `projects/pec/execution/_Coordination/_TaskManagement/**`, for the register rows and the intake record's disposition/outcome;
- the Root notice above;
- this brief, copied to `projects/pec/execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260927-RV1-INTAKE/briefs/TM1_INTAKE_DISPOSITIONS.md`;
- your return, at `…/AgentRuns/HELP-HUMAN-PEC-20260927-RV1-INTAKE/returns/TM1_INTAKE_DISPOSITIONS.md`.

Write nothing else: no graph, STATUS, `_DECISIONS/**`, contract, `_STATUS.md` or `_DomainEngines/**` file, and no other project's folders.

## Publication and rules

- Export `TMPDIR` to your own directory under the session scratchpad `/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/`, and set `PYTHONDONTWRITEBYTECODE=1`. Never write to `/tmp` or `/var/folders`. Children follow the same rules and never run `git fetch`.
- Commit and push early.
- Open a PR against `main`, and do not merge it.
- Commit messages end with `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`. The PR body ends with `🤖 Generated with [Claude Code](https://claude.com/claude-code)`.
- **Return:** the PR URL and head, the rows and dispositions written (IDs), the notice path and hash, the checks and the verdict.
- Never prompt about CHECKING.
