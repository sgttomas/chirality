# Brief — R0 TASK: assemble the v3 "done" declaration candidate

**Role.** TASK (Type 2). You do not delegate. You carry the assignment to its result and
return evidence to HELP_HUMAN.

**Run.** `RUN_D128_CONCORDANCE_2026-09-21_1614Z` (D-APP-128). Placeholders are supplied
at dispatch:

- `<FROZEN_TREE>`: a read-only checkout at `00115c719`.
- `<RUN>`: the run folder in the working repository.

## Purpose

The owner steered the v3 push by a dependency graph and a declaration of what "done"
looked like. The owner says that declaration "took shape across sessions" and is not
recorded in one place. Assemble the best-evidenced candidate for the owner to confirm or
edit at the R0 gate. Until confirmed, it is CONTEXT only.

## Read, from `<FROZEN_TREE>` only

1. `plans/chirality_app_v3_release_execution_plan_final_2026-08-22.html`:
   - §3 (release definition and scope; 3.1, 3.2 success criteria);
   - §8 (required instruments, held bindings);
   - §10 (critical path; 10.1 gate definitions).
   - Strip tags with a small Python snippet rather than reading raw HTML.
2. `plans/steers/chirality_app_v3_g0_record_2026-08-22.md`: owner rulings A1–A12+ that
   amend the plan.
3. `plans/steers/chirality_app_v3_*`: the a1–a15 and r1–r18 ruling records and the phase
   and gate steers. Read these for any later change to scope, gates or done-ness.
4. `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/`:
   - D-APP-97 (release preparation);
   - D-APP-125, 126 and 127;
   - `plans/steers/chirality_app_v3_codex_host_replatform_direction_2026-09-11.md` (D-GOV-43).
5. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/`:
   - `APP_V3_*` handoffs, only where they record the owner changing what "done" meant;
   - the 2026-09-19 owner direction in `HELP-HUMAN-APP-20260919-LOOP-WORKGRAPH/OWNER_DIRECTION.md`
     ("published as v3.0.0").
6. `projects/chirality-app-dev/loop/LOOP_RECEIPTS.md`: search it for verbatim
   `Owner-Direction` records about release scope after 2026-08-22.

## Write exactly one file

`<RUN>/R0_DONE_DECLARATION/V3_DONE_DECLARATION_CANDIDATE.md`, containing:

- **Banner.** "CANDIDATE, CONTEXT-class, not authority until the owner confirms at the
  R0 gate."
- **§1 Done criteria,** as a numbered list `DONE-01`… Each item:
  - states one criterion in plain words;
  - cites its sources as path + section/anchor + a quote of at most 15 words;
  - gives a **status**: `ORIGINAL` (plan) · `AMENDED BY <record>` · `SUPERSEDED BY <record>` · `ADDED BY <record>`;
  - maps it to the App packages or deliverables it most concerns, where evident, marked
    `provisional`.
- **§2 Explicitly out of scope for v3,** in the same format.
- **§3 Gates,** as a table of gate → pass evidence required → final recorded outcome, if
  any record states one, with a citation.
- **§4 Gaps and conflicts:** places where the records disagree, or where "done" was
  evidently decided in a session without a record. Write each as a question to the owner.
- **§5 Sources read,** with SHA-256 of each file.

## Rules

- Read-only everywhere except that one file.
- No git operations, installs or test runs.
- No absolute machine paths in the output; use repo-relative paths.
- Never present your synthesis as an owner ruling. Where you infer, write "inferred".

## Return

Return, briefly:

- the output path and its SHA-256;
- the counts of DONE, out-of-scope and gap items;
- the three most consequential gaps.
