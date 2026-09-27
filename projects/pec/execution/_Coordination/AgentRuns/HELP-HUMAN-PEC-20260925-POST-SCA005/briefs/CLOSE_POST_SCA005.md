# Brief CLOSE — closeout of undertaking HELP-HUMAN-PEC-20260925-POST-SCA005: C1 comparisons, Task Management intake, M1 MEMORY records (WORKING_ITEMS)

- **Parent:** HELP_HUMAN.
- **Undertaking:** `HELP-HUMAN-PEC-20260925-POST-SCA005`; graph `projects/pec/execution/_Coordination/WorkGraphs/HELP-HUMAN-PEC-20260925-POST-SCA005/WORK_GRAPH.md`. Nodes C1 and M1 are yours to carry out; HELP_HUMAN keeps the graph and receipt.
- **Role:** WORKING_ITEMS (Type 1).
- **Method:** `projects/pec/loop/LOOP_INIT.md` §§3–5. Use `chirality-root:bundled:workflow:bounded-reconciliation` for per-deliverable comparisons as needed, and `chirality-root:bundled:workflow:task-management` for intake only. Record the SHA-256 of each method file you load.
- **Model:** `claude-opus-5-5`, high reasoning, for you and any child. This is the owner's standing steer.
- **Branch:** `claude/pec-post-sca005-closeout`, in your own isolated worktree, cut from fresh `origin/main` (at or after `5d0680951`, the PR #1008 merge).

## Basis (all merged on `origin/main`)

The undertaking's acts:

| Ruling | Act | What it did |
|---|---|---|
| `D-PEC-95` | PR #924 | re-pin |
| `D-PEC-96` | PR #950 | registry |
| `D-PEC-98` | PR #958 | DEL-02-08 and DEL-02-09 first SOWs and add-on S |
| `D-PEC-99` | PR #957 | retirement, a separate undertaking, already closed |
| `D-PEC-101` | PR #976 | K1, K4 |
| `D-PEC-100` | PR #979 | S2, seven SOWs |
| `D-PEC-103` | PR #992 | DEL-08-06 and DEL-10-13 SOWs, add-ons S and C8 |
| `D-PEC-102` | PR #998 | S4, eight SOWs |
| `D-PEC-104` | PR #1010 | S1, twelve SOWs |
| `D-PEC-105` | PR #1007 | D1 premise amendments |
| `D-PEC-106` | PR #1008 | X1 fixtures and add-on L |

- Each ruling record is `_DECISIONS/D-PEC-NNN_RULING_*.md`.
- Each act has its run root and `HANDOFF_STATE.md` under `execution/_Coordination/`.
- HELP_HUMAN's PR reviews are under `AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/returns/REVIEW_PR*.md`.

## 1. C1: bounded documentation and governance closeout

For each deliverable this undertaking touched:
- **SOW written or replaced:** DEL-01-01, 01-03, 01-04, 01-05, 01-06, 02-01, 02-02, 02-03..09, 03-01, 03-02, 03-03, 03-04, 03-06, 04-01, 04-02, 04-03, 04-05, 08-01, 08-03, 08-04, 08-06, 10-02, 10-03, 10-10, 10-13.
- **Artifacts amended:** DEL-00-01, DEL-00-03.
- **Fixtures committed:** DEL-02-03, 02-08, 02-09.

Compare what was delivered, and its evidence, with that deliverable's actual Scope of Work, dependency and governance records. Find any inconsistency this undertaking introduced or left that a record must now reflect. Examples:
- a `_STATUS.md` history line that disagrees with an act;
- a `_DEPENDENCIES.md` or `Dependencies.csv` quotation made non-verbatim that the act accounts did not already list;
- a context or reference file now false.

**Bounds**
- A supported no-change result is sufficient.
- Stay proportionate: rely on each act's verifier and HELP_HUMAN's reviews. Do not redo them. Sample where the act accounts are thin.
- Fenced writes outside `_Coordination/**` need an owner-ruled packet. **Do not make them.** Report each warranted edit with evidence and a proposed home.
- `_Coordination/**` records you may correct directly, with a note.

Write the comparison account to `projects/pec/execution/_Coordination/CLOSEOUT_POST_SCA005_2026-09-27/C1_ACCOUNT.md`, together with any evidence files.

## 2. Task Management intake (bounded, LOOP_INIT §4)

Only a **material, evidenced concern without a current or identified successor home** qualifies.

**Candidates.** They are recorded in the graph's next-work and carry lines, the act `HANDOFF_STATE.md` files and the ruling records. Judge each one:

1. **Contract currency items no packet owns yet:**
   - DEL-10-11 `CLM-014`;
   - DEL-03-04's quotation of DEL-03-01 `CON-005`;
   - DEL-02-07 `CON-003` and DEL-10-13 `CON-003`, whose premises are partly overtaken;
   - eleven S1 contracts' "(provisional `D-PEC-104`)" AX text, and the "not yet ruled" text in the eight S4 contracts;
   - DEL-04-05 AX-012;
   - the QA 21 owner binding in DEL-02-01 and DEL-02-02 REQ-005;
   - the rest of DEL-03-06's stale text and its two sibling quotations;
   - DEL-10-03 `REQ-013`'s QA 21 note;
   - the DEL-02-08/09 contract-wording items;
   - the DEL-02-07 `CLM-011` count;
   - the stale quotations in DEL-01-05 (`CLM-009`, `CON-001`, `TBD-005` "accepted"), DEL-01-03 (the old §12 P1 row) and DEL-08-02 (which is CHECKING; name only, and ask nothing about CHECKING);
   - DEL-01-01 `CLM-009`'s hash anchors;
   - the D1 "Other findings" 1–11.
2. **Lapsed owner acceptances without a scheduled re-review:**
   - DEL-02-07 and DEL-01-06, both replaced under `D-PEC-100`;
   - DEL-04-01 (`D-PEC-102`);
   - DEL-03-01 (`D-PEC-104`).

   The D1 ones are carried as RV1, which the receipt names for the next undertaking. Give RV1 a home there, not here.
3. **K3**, the tier-0 profile act. It is held until a DEL-08-06 production packet. Is that an identified successor home?
4. **The possible dependency amends** DEL-08-06 → DEL-04-03 and DEL-10-13 → DEL-02-07, and the missing PEC v2 release process (DEL-10-13 CON-004). These are recorded as CON items in the governing contracts, so they may already have a home.
5. **X1's residuals** for the first parser packet: field attribution, AST guard gaps, partial-clone detection, `.DS_Store`, widening the `v2-parsers` path rule, and hosted CI not running v2 checks.

**Procedure**
- Group the items sensibly. Prefer a few well-formed intake rows over many.
- Run the task-management workflow's federation preflight.
- Record the intake in PEC's Task Management surface (`projects/pec/execution/_TaskManagement/`), following its existing conventions.
- Intake only. **Promotion, disposition and external assignment are the owner's acts**, so do not perform them.
- For each item you judge already homed, say where.

## 3. M1: MEMORY records (add-on M of each packet)

Create or append exactly what each ruled packet's add-on M section tables, using its template (`docs/templates/MEMORY_TEMPLATE.md`, `5a9564f4…6a5a`) and its row text:
- **`D-PEC-98`:** DEL-02-08 and DEL-02-09 (create).
- **`D-PEC-100`:** DEL-01-01 and DEL-02-03..07 (create), plus one row in DEL-01-06's existing file, after the `D-PEC-96` row.
- **`D-PEC-103`:** DEL-08-06 and DEL-10-13 (create).
- **`D-PEC-102`:** DEL-04-01, 04-02, 04-03, 08-01, 08-03, 08-04, 03-04 and 10-03 (create).
- **`D-PEC-104`:** DEL-01-04, 01-05, 02-01, 02-02, 03-01, 03-02, 03-03, 03-06, 04-05, 10-02 and 10-10 (create), plus one section appended to DEL-01-03's existing file.
- **`D-PEC-105`:** DEL-00-01 and DEL-00-03 (create).
- **`D-PEC-106`:** one row appended to each of DEL-02-03, DEL-02-08 and DEL-02-09, after the rows the `D-PEC-100` and `D-PEC-98` add-ons write.

**Slots**
- `{D}` = `2026-09-27`, the closeout date.
- `{PR}` = each packet's act PR (numbers above).
- **Receipt link:** `execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/RECEIPT.md`, written relative to each file's location in the form the packets and existing MEMORY rows use. HELP_HUMAN writes the receipt in this PR.
- **Ruling link:** each packet's ruling record.

Where a packet's table fixes the exact row text, use it byte for byte. Preserve existing history in DEL-01-03 and DEL-01-06.

**Checks.** Before writing, run `pec_reliance_hold.py` with `--operation exact-correction-preparation`, or the operation the packets name, on every MEMORY target. After writing, have one fresh read-only `pec-reviewer` (opus) verify that:
- every file equals the template with only the tabled slots filled;
- appended rows keep prior bytes;
- no other file changed.

## Write boundary

You may write:
- the `MEMORY.md` files above;
- `projects/pec/execution/_Coordination/CLOSEOUT_POST_SCA005_2026-09-27/**`;
- intake rows in `projects/pec/execution/_TaskManagement/**`, following its conventions;
- this brief, copied to `…/AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/briefs/CLOSE_POST_SCA005.md`;
- your return, at `…/returns/CLOSE_POST_SCA005.md`.

Write nothing else. In particular, do not touch any `ScopeOfWork.md`, `_STATUS.md`, `_DEPENDENCIES.md`, `Dependencies.csv`, context, reference, register, `v2/**`, PRD, `docs/**`, `README.md`, `_DECISIONS/**` or the work graph.

## Checks, publication and return

- Strict registers, the harness self-check and `validate_pec_loop_receipts.py` must give output identical before and after your changes. Record them. `git diff --check` must be clean.
- In every shell, export `TMPDIR` to a scratch directory under `/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/`, and set `PYTHONDONTWRITEBYTECODE=1`. Never write to `/tmp` or `/var/folders`. Children follow the same rules and delete only their own directories.
- Commit and push early. Open a PR against `main` titled as the undertaking's final PR (F1). Do not merge it. HELP_HUMAN adds the receipt, the graph completion and STATUS, then reviews and merges.
- Commit messages end with `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`. The PR body ends with `🤖 Generated with [Claude Code](https://claude.com/claude-code)`.
- **Return:**
  - PR URL and head;
  - C1 account summary, with each warranted edit and its proposed home;
  - the intake rows and what was judged already homed;
  - the MEMORY files written, with hashes;
  - the verifier verdict;
  - checks.
- Run children in the foreground, or wait for them inside your turn.

## Limits

- No lifecycle change, acceptance, REVIEW or CHECKING act. Never prompt about CHECKING.
- No ruling.
- No promotion or disposition of Task Management rows.
