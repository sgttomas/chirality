# Brief RR3 — D-PEC-99 option-A Remaining retirement act (WORKING_ITEMS)

Parent: HELP_HUMAN, undertaking `HELP-HUMAN-PEC-20260926-REMAINING-RETIREMENT`, work-graph node RR3. Role: WORKING_ITEMS (Type 1), with `Workflow: chirality-root:bundled:workflow:task-management` (legacy-source retirement). Load its `WORKFLOW.md`, `resources/contract.md` and `resources/method.md` and record their SHA-256. Model steer: `claude-opus-5-5`, high reasoning, for you and the verifier. The owner said "defaults".

## Authority and specification

- **Ruling.** `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-99_RULING_2026-09-26.md`. The owner's words: "D-PEC-99: A; Q1 a; Q2 a; Q3 a; confirm F; no MEMORY; defaults".
- **Proposal.** `_DECISIONS/D-PEC-99_remaining_retirement_proposal_2026-09-26.md`, SHA-256 `29e2ff5704d45f0da31f41fd80bf822003743fbf9effdda4ebbc2806306d5c79`. It is your specification: exact product grant (62 paths), generation method, finite verification, independent verifier, administrative grant, rollback and limits. Do not enlarge it.
- **Bound scripts** in `projects/pec/execution/_Coordination/_TaskManagement/TM_PEC_REMAINING_RETIREMENT_2026-09-26/`:
  - `gen_d99.py`, SHA-256 `1fad023951f8fca887974452a6b65cfd312b74c1312997ac99a5260b64ee7237`;
  - `verify_d99.py`, SHA-256 `c1d50dfd267894f8602b6b4497136e41a6fa2cf5f9ffe614efdb4314ea791865`.
- **Slots.** `{N}` = `D-PEC-99`; `--q1 s1`; `{R}` = `2026-09-26`; `{D}` = the local date of the act (the generator checks it). If `{D}` is not 2026-09-26, the postimages differ from the tables only by the slot rule, and the verifier replays with `--reproduction`.

## Preconditions (stop and return if any fails)

- Fetched `origin/main` contains the ruling, the published proposal and register row `D-PEC-99` `RULED A` (PR #954), and PR #943's merge (`db9328789`).
- `projects/pec/AGENTS.md` equals `4400c4e97d5c9dfeda7a9a764b204ed14784c687e55e81bb04875323b6c7139c`, and every pinned `_STATUS.md` preimage holds. The generator checks this itself.
- `pec_reliance_hold.py` (register `projects/pec/execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv`) returns ALLOW for every `projects/pec` target with `dispatch-for-production`, and with `rely-for-production` before fan-in.
- You work in an isolated worktree on branch `claude/pec-d99-remaining-retirement-act`, cut from fresh `origin/main`. On a generator or check failure, discard the worktree and return. Do not repair.

- **Parallel act.** The `D-PEC-98` SOW act (brief S3A) runs at the same time on disjoint paths (two new `ScopeOfWork.md` and, later, the DEL-02-08/09 `_STATUS.md`, which are not in the census). If it merges before you, re-fetch `origin/main` and confirm your pins still hold before your PR merges; report, do not repair, any conflict.

## Act

1. Create the run root `projects/pec/execution/_Coordination/REMAINING_RETIREMENT_D-PEC-99_{D}/`. Copy both scripts into it byte for byte and check their hashes.
2. Run `verify_d99.py --repo . --account-only` (before), then `gen_d99.py … --check-only`. Expect `RESULT PASS`, `CHECK write_set 62` and `CHECK status_sections_removed 57`.
3. Make a `git archive` export of the commit immediately before the generator run, in a `mktemp -d` outside the checkout. Then run the generator (the proposal's command, with the slots above). Capture its output outside `projects/pec` first if it inventories the tree, then copy it into the run root.
4. Immediately after, before any other write, run `verify_d99.py --repo . --pre <export> --decision D-PEC-99 --q1 s1` (with `--allow-extra` only for paths the proposal allows). Expect `RESULT PASS`.
5. Run the rest of the proposal's "Finite verification" table and save each command, exit code and output in the run root: 32/32 SOW validation unchanged; strict registers with **output identical before and after** (baseline at current `origin/main`: exit 1, 0 errors, 28 warnings under D-GOV-48; the proposal's "28" matches); tranche manifest G4 in both modes; instruction entrypoints and the two pytest files; harness self-check and the PEC receipt validator identical before and after; `taskmgmt.py validate` unchanged; containment; `git diff --check`.
6. Write `FINAL_ROW_ACCOUNT.csv` in the Task Management folder (a copy of the account with `AppliedResult` set), and `HANDOFF_STATE.md` in the run root. The D-PEC-95 run root `CURRENCY_REV15_D95_2026-09-25/` is the precedent for form.
7. Dispatch one fresh read-only verifier (`pec-reviewer`, opus) under the proposal's "Independent verifier" section, including reproduction of every postimage on a fresh export and the semantic checks. Save its verdicts as `VERIFIER_VERDICT_NN.md` in the run root. Defects come back to you; repair only within the proposal and ruling.

## Write boundary

You may write only:
- the 62 granted paths, produced by the generator and by nothing else;
- the run root; `FINAL_ROW_ACCOUNT.csv` in the Task Management folder;
- this brief, copied to `projects/pec/execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/briefs/RR3_D99_RETIREMENT_ACT.md`, and your return at `…/returns/RR3_D99_RETIREMENT_ACT.md`.

Do NOT write: any other `_STATUS.md`, any `ScopeOfWork.md`, `MEMORY.md`, `Dependencies.csv`, `_CONTEXT.md`, `_REFERENCES.md`, decomposition, register, `checkpoint_snapshots/**`, `_Evaluation/**`, `loop/**`, `init/**`, `v2/**`, `docs/**` (except the generator's manifest), `README.md`, `_DECISIONS/**` other than the generator's exhibit, either work graph, or any foreign path other than the generator's two notices. HELP_HUMAN adds the graph sentences and STATUS/README in the same PR after you hand back.

Commit work in progress at each step and push early. Commit your return before you hand back.

## Publication

- Commit, ending each message with `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`.
- Push, and open a PR against `main`, ending the body with `🤖 Generated with [Claude Code](https://claude.com/claude-code)`.
- Do not merge. If CI reports "Update the PR base", report it; do not repair it.

## Return

PR URL and head SHA; generator and closure-check reports; the written paths with hashes; check results; verifier verdicts; containment; the Part B keys per node (S1, S2, S4) for HELP_HUMAN's graph sentences; anything unresolved.

## Limits

No lifecycle change; no SOW write; no evidence inquiry executed or selected; no Task Management row; no CHECKING, ISSUED or acceptance. Do not ask the owner about CHECKING.
