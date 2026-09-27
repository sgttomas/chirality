# PROJECT_SETUP — D-PEC-101 revision-1.6 currency and setup (K1, K4 with add-on C, add-on V): Manifest

**Status:** EXECUTED / VALIDATED; independent verification PASS WITH NOTES (`VERIFIER_VERDICT_01.md`)
**Owning instrument:** WORKING_ITEMS under `chirality-root:bundled:workflow:project-setup`, `D-PEC-101` (K4 with C; K1; V)
**Act date `{D}`:** 2026-09-26 (local date at the K1 generator run; America/Denver, MDT; no clock or time-zone manipulation)
**Branch / basis:** `claude/pec-d101-act` from `origin/main` `f392294b573dcc0b17fff8cd9b5a8c2cf4dd252d` (PR #969); `origin/main` `17da1a013` merged at `dc68b5afd` before the PR
**Commits:** K1 `345266081`; K4 with C `62230fa46`; checks `62ceea8ff`, `c061f830c`; verifier record `39e30684d`; add-on V and pointer `674de6a90`

This package is derivative coordination evidence. It cites accepted upstream truth and does not
replace decomposition, scope-change or decision authority.

## Authority and method

| Instrument | SHA-256 |
|---|---|
| `_DECISIONS/D-PEC-101_RULING_2026-09-26.md` (owner: "D-PEC-101: K4 with C; K1; V; Notes a; defaults") | `baa4fc09525aaef89cdb519b934b00c90e699a2111a5c604f906fc5ed2edba28` |
| `_DECISIONS/D-PEC-101_rev16_currency_setup_proposal_2026-09-26.md` (the specification) | `7ad176063b10b4cb3093bc9c1d5c6efbab83fcdb5e6a059e6122c466fd095a25` |
| `_DECISIONS/_REGISTER.md` row D-PEC-101 (`RULED K4+C / K1 / V / EFFECTIVE ON MERGE`), observed on fetched `origin/main` `f392294b5` | register `9fd06376…7c858` at that commit |
| Brief K14A (HELP_HUMAN), copy at `AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/briefs/K14A_D101_ACT.md` | `b253797178dfb4b117491d5d056120a23e2b2538485fa83119c5e4851961d2ec` |
| Root `AGENTS.md` / `projects/pec/AGENTS.md` / `agents/AGENT_WORKING_ITEMS.md` | `c8ce87ef…ffd` / `df9196d1…eb8` / `9ae4bea2…665` |
| `workflows/index.json`; `project-setup` `WORKFLOW.md` / `method.md` / `contract.md` (at `f392294b5`) | `2bfa2c5f…fb3`; `7aa4c30a…dd6d` / `37c285a2…f042` / `e9f0d11b…c218e` |
| `preparation` `SKILL.md` (K1 TASK); `audit-decomp` `WORKFLOW.md` / `contract.md` / `method.md` (V TASK); `software-code-review` `SKILL.md` (verifier); `agents/AGENT_TASK.md` | `0662dc88…6d38`; `7ba6291c…246b` / `704929c7…4e75` / `51a0c69b…8827`; `ee085d58…888bca`; `1a13a5b0…c8fb7` |
| `gen_d101_k1.py` / `gen_d101_k4.py` (this run root; byte-identical to the preparation folder) | `4892c6a3c7fab4ba405b1ca201b7cab423c8c59644dee5f1d675d2e5f692cecb` / `075036f0a8c214a156aec151aaa52f6d1b78c2694f4306d410579ffcef9f0e73` |
| `verify_d101_k1.py` / `verify_d101_k4.py` | `8b42926edad0cceef8a109f230081de58a805855a880712bc97a479b2320cc42` / `39f9bbd07a56e88ea06fb105d11d382b05c4a8fd796068342c42101191bc240f` |

Other instructions consulted deliberately: none beyond the above. Skill and workflow origins are
the bundled Root library (`chirality-root:bundled`); no project `.chirality/workflows` or user
origin exists on this host.

## Binding commands (each run once, from the repository root)

```text
PYTHONDONTWRITEBYTECODE=1 python3 projects/pec/execution/_Coordination/REV16_CURRENCY_SETUP_D101_2026-09-26/gen_d101_k1.py --repo /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-d101-act --act-date 2026-09-26
PYTHONDONTWRITEBYTECODE=1 python3 projects/pec/execution/_Coordination/REV16_CURRENCY_SETUP_D101_2026-09-26/gen_d101_k4.py --repo /Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-d101-act --covers
```

K1: TASK `pec-task` as the `preparation` actor, default `--actor TASK+preparation`, no
`--reproduction`, 16:25:08 MDT, after a clean `--check-only`. K4: the manager, 16:27:10 MDT, after
a clean `--check-only`. The literal `--repo` equals `git rev-parse --show-toplevel`. Both exit 0,
empty stderr. Order K1 then K4 (the ruling's method choice).

## Exact live-effect manifest

161 product paths plus, with V, one audit folder and one pointer. Per-path postimage hashes are in
`checks/32_final_k1_postimages.out` (32 rows) and `checks/33_final_k4c_postimages.out` (129 rows);
each equals the proposal's table.

| Set | Files | Path list SHA-256 | Post bytes SHA-256 | Proposal |
|---|---:|---|---|---|
| K4 with C (63 `_CONTEXT.md`, 66 `_REFERENCES.md`; all MODIFY) | 129 | `bbd1374c165624fcadf37ccf7e788599a5e5a07c6886af59f40e62fbfc7bf7f3` | `01bd1f7bcdc28519e8b4ed5a767a3a362004d412bd350fe3816eabd425576b3d` | `all_A+C` equal |
| K1 all | 32 | `c1fbca79ae25d68c5e34aed84f536197c727dce2ae13d602bd82b8f1224fa7f4` | `483ec2393ac4a9256fe2c0ab294c7f563c622349076a9a87ba36dc862d020234` | `all_K1` equal |
| K1 modified (4 `Dependencies.csv`, 16 `_DEPENDENCIES.md`) | 20 | `8c569e6091905c043113aff302804066daaae50aaf76ea54b79042792a92db2f` | `186d9c72282424bd8eb317106d9dbc72b9d595b35e4227822f2869fc9bb06e8f` | `modified_K1` equal |
| K1 created (DEL-08-06 and DEL-10-13 folders, 6 files each) | 12 | `bfca84fab01676f7380f7af04241e83719501236cbcc2d966b90f63c83be7eef` | `e72fc7e9702f5f7acb4e2870cb1b53385b2b874635c7a6fd60b01e2a3f35e887` | `created_K1` equal |

New folders: `PKG-08_API_Access/1_Working/DEL-08-06_Agent_tool_call_query_surface/` and
`PKG-10_Validation_Measurement/1_Working/DEL-10-13_Reliance_advertisement_gate/`; both `_STATUS.md`
at `OPEN`, 2026-09-26, `(TASK+preparation)` (`73e21846…2511`, `c7a5705d…543b`). Rows: 22 added
(4 new-folder ANCHOR, 2 appended ANCHOR, 16 EXECUTION, E-P84..E-P99), 2 refreshed
(DEP-09-06-003, DEP-10-03-003), 0 retired, 0 deleted.

Add-on V:

| Path | Act | SHA-256 |
|---|---|---|
| `_Evaluation/DecompCoverage/COV_D101_POSTSETUP_2026-09-26_1651/` (11 files; hashes in `HANDOFF_STATE.md`) | CREATE (TASK) | — |
| `_Evaluation/DecompCoverage/_LATEST.md` | MODIFY (manager, `update_latest_pointer.sh` `21899520…15bc`; 0 BLOCKERs) | `f8469f88…a9dea` → `e5ad5190f88a9cd29038aaa2e31f23bdae989bae42d0b5c2103472d4e6421c8e` |

## Run root contents

Generator copies and verify scripts; generator reports and stderr (`gen_d101_k{1,4}_*`); helper
scripts (`check_hashes.py`, `check_k4_extras.py`, `containment.py`, `run_holds.sh`); `checks/`
(every command's output and `COMMANDS.txt`); `closure_pre/` and `closure/`; `child_briefs/`
(`T_K1_ACT.md` `ad2aec24…0de8`, `T_VERIFIER.md` `0be5a112…5f02`, `T_V_AUDIT.md` `d9e3f4e7…4194`);
`child_returns/` (manager transcription and verbatim hand-backs of the K1 and V TASKs);
`VERIFIER_VERDICT_01.md` (`73b23f35…005c`) and its dispositions; this manifest, `VALIDATION.md`,
`HANDOFF_STATE.md`; `.gitattributes`; `SHA256SUMS` (every other run-root file). No `_run_records/`
entry was written in any deliverable.

## Delegation record

| Child | Mechanism | Brief | Scope | Result |
|---|---|---|---|---|
| K1 author | Claude Code `Agent` subagent `pec-task`, foreground, parent this manager | `child_briefs/T_K1_ACT.md` | the 32 K1 paths via the generator; four report copies | done; see `child_returns/` |
| Independent verifier | `Agent` subagent `pec-reviewer` (read-only tools), background; its hand-back reached HELP_HUMAN after this manager's forced interim handbacks and was relayed verbatim | `child_briefs/T_VERIFIER.md` | read-only; scratch only | PASS WITH NOTES |
| Add-on V auditor | `Agent` subagent `pec-task`, foreground | `child_briefs/T_V_AUDIT.md` | the new snapshot folder only | 0 BLOCKER; see `child_returns/` |

Model steer `claude-opus-5-5` at high reasoning for every child; the host reports Opus 5.5. Role
identity is instruction-asserted, not mechanically enforced.
