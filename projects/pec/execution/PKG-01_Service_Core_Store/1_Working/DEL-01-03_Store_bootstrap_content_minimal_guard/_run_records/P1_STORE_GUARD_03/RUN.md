# RUN — P1_STORE_GUARD_03 (D-PEC-89 A exact-type closure slice)

Role: WORKING_ITEMS (Type 1), instruction-asserted, owning PKG-01 / DEL-01-03
only. Parent: HELP_HUMAN run `HELP-HUMAN-PEC-20260923-SCA005`, node C3.
Brief: `projects/pec/execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260923-SCA005/briefs/C3_D89_EXACT_TYPE_SLICE.md`
(supplied verbatim in the dispatch message; its canonical copy is committed
separately by HELP_HUMAN and was not read from disk by this run). The owner's
direction relayed in the dispatch: "go ahead with the slice".
Date: 2026-09-24 (session date). Host: Claude Code Agent tool, isolated
worktree. Model steer: `claude-opus-5-5`, high reasoning (D-PEC-89 ruling,
owner question 3). The host reports the manager as `claude-opus-5-5`; the
reasoning level is instruction-asserted.

## Basis (actual origins and SHA-256 at `origin/main` `9ffc54afcaa287d1b5fdc57dcda2194f6f1e0abf`)

| Source | SHA-256 |
|---|---|
| `AGENTS.md` (Root) | `c8ce87ef342902cb081bc659b26fc9a4edda1b6dba513814e5cb1e14e0b1dffd` |
| `projects/pec/AGENTS.md` | `46689c36d5379029a34a5c5d26f109445e338fca82b86e590826bcbc39ad3846` |
| `agents/AGENT_WORKING_ITEMS.md` | `9ae4bea25bd95750a6878a9d53fbbbd7cd058d72c652a36baf4aa90601799665` |
| `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-89_RULING_2026-09-24.md` | `536b058873a011a4ef3df60f243fc55ecd389c2900132bfa30592ba414d263e3` |
| `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-89_del_01_03_exact_type_closure_proposal_2026-09-24.md` | `962a7879788e75cac41bc73c8320eb2be11b65fe104fcbb163fff892b49f8a73` (matches the ruling) |
| `projects/pec/execution/_Coordination/_DECISIONS/_REGISTER.md` (D-PEC-89 row, line 106: `RULED A / EFFECTIVE ON MERGE`) | `a833058294b297d71b66f4a5844d0d0cb1630555cb45734ff7c68b5bf670bb05` |
| `projects/pec/docs/PRD.md` | `6833553c33aadca00e4ee6932d56ae4698c2ae7798c30b603bc17e60dae477ba` |
| `workflows/software-bounded-implementation/WORKFLOW.md` (bundled, `chirality-root:bundled:workflow:software-bounded-implementation`; author method; no project or user workflow of that name) | `2ea0ddf4f53241fa94274e709b8042ad9de4d8beb9c82cd1ed1dcd0c6f8f0f7b` |
| `.agents/skills/software-code-review/SKILL.md` (project skill; verifier method) | `06c27b1be5cfbd9e638570918a8f837d8439c8073c40d3ef708e53874f95570a` |
| `workflows/software-code-review/WORKFLOW.md` (bundled; verifier method detail) | `9054dfd47318a680e54fe390b00c67e2baf9595156487d4d1897a83458414810` |

D-PEC-87 slice records under `_run_records/P1_STORE_GUARD_02/` are read for
context only and are not written (`RUN.md`, `VERIFIER_VERDICT_01..03.md`,
`AUTHOR_RETURN_02.md`; hashes as listed in the proposal's provenance table).

## Preconditions

1. Fetched `origin/main` = `9ffc54afcaa287d1b5fdc57dcda2194f6f1e0abf` (PR #895
   merge; `git merge-base --is-ancestor` confirms it). The ruling file and the
   D-PEC-89 register row are present. PR #893 is merged (`0517e0752`, an
   ancestor). PASS.
2. Fresh preimage verification: all five opened paths and the three unopened
   paths match the proposal's rollback table (see `PREIMAGE.md`). PASS.
3. Reliance-hold `dispatch-for-production` preflight: ALLOW, exit 0, for all
   five opened paths (see `PREIMAGE.md`). PASS.

Branch: `claude/pec-d89-exact-type-slice`, created from fresh `origin/main`
`9ffc54afc` (upstream tracking unset so no push can target `main`).
Interpreter: `/Library/Frameworks/Python.framework/Versions/3.13/bin/python3`,
Python 3.13.7. Git identity (repository config): `Ryan C Tufts <ryan@chirality.ai>`.

## Work graph

| Node | Owner | Act | Depends |
|---|---|---|---|
| N1 | WORKING_ITEMS | Preconditions, branch, run root, `PREIMAGE.md` | — |
| N2 | TASK author (`pec-task`, opus) | Before-reproduction on preimage in scratch; R9–R14 on the five paths under software-bounded-implementation; probe battery under `probes/`; `AUTHOR_RETURN_0N.md` | N1 |
| N3 | WORKING_ITEMS | Five registered checks under `checks/`; mutation list M1–M9 under `checks/` | N2 |
| N4 | TASK verifier (`pec-reviewer`, opus, read-only) | software-code-review; substantive admissibility; independent probes; R14 text vs PRD and code; `VERIFIER_VERDICT_0N.md` | N3 |
| N2'/N4' | author / verifier | Correction cycles while a blocking finding remains | N4 |
| N5 | WORKING_ITEMS | `rely-for-production` preflight, containment, whitespace | N4 PASS |
| N6 | WORKING_ITEMS | One `MEMORY.md` entry | N5 |
| N7 | WORKING_ITEMS | Commit, push, PR (no merge) | N6 |

## Progress log

- N1 complete.
- N2 cycle 1 complete: author record `AUTHOR_RETURN_01.md` (SHA-256
  `e3a465beb60c14bc540366ee31dd7faac26d9f8def735567d984afe67a440614`; agent id
  `afc0ef96373196efc`, host-reported model `claude-opus-5-5`; the final report
  returned directly to this manager through the foreground Agent call). R9–R14
  are applied to the five granted paths. The suite has 13 tests with no new
  test ID. The author's probe script `probes/probe_d89.py` (reimplemented from
  the proposal text) gives 28 of 33 open on the preimage
  (`probes/probe_BEFORE_preimage.out`) and 1 of 33 (C2-4) on the postimage
  (`probes/probe_AFTER_postimage.out`).
  Manager observation: the guard and adapter postimages are byte-identical to
  the proposal's prototype postimage hashes (`2cb21e2d…`, `edb15e2b…`). The
  prototype files sit in HELP_HUMAN's session scratchpad, which this host
  shares with its children. The author states that it wrote the bytes from the
  specification and never read the prototype files. That cannot be verified
  here. The edits are small and exactly specified, so a match is plausible.
  The record therefore does not rely on authorship independence. The verifier
  judged the bytes on their merits.
- N3: manager ran the five registered checks from the repository root as
  `python3 tools/software_workflow/run_registered_checks.py projects/pec/software-workflow.json --check <id> --output <RR>/checks/<id>.json`
  with `PYTHONDONTWRITEBYTECODE=1`. Each exited 0 with status PASS:
  `v2-store-guard` (Ran 13, OK), `v2-core-posture` (`"verdict": "PASS"`),
  `v2-loop-registry` (Ran 12, OK), `v2-api-contract` (Ran 6, OK) and
  `harness-self-check` (INFO=14, NOT_APPLICABLE=1, REVIEW=4, WARN=124, the
  D-PEC-87 baseline). The wrapper's stdout, which only echoed paths, was not
  retained. Verbose storage run from `projects/pec`:
  `python3 -m unittest discover -s v2/tests/storage -p 'test_*.py' -v` gave
  exit 0 with 13 tests `ok` (`checks/v2-store-guard_verbose.out`).
  Mutation list: the manager reran the author's runner (reviewed first) from
  `projects/pec` as
  `PYTHONDONTWRITEBYTECODE=1 python3 <RR>/probes/mutate_d89.py v2`, exit 0,
  output `checks/mutation_manager_run.out`. It is a fresh run. Its bytes equal
  the author's `probes/mutate_AFTER.out` because the runner is deterministic
  and the source path is identical (verifier N-6). M1–M9 are each caught by the
  tests the proposal names.
- N4 cycle 1: verifier **PASS**, no blocking finding (`VERIFIER_VERDICT_01.md`;
  agent id `a5eefcc3795adc090`, `pec-reviewer`, host-reported
  `claude-opus-5-5`; returned directly to this manager and saved verbatim).
  The verifier used its own probes: 29 of 29 open on the preimage, and 1 of 29
  (C2-4) on the candidate. It also ran its own mutation runner: M1–M9 are
  caught, and so are extra mutations X1–X4. X5 survives (R12 narrowed to
  `FileExistsError`; N-1). The R14 text was checked verbatim against the
  proposal and judged truthful against the code and the PRD. Notes N-1 to N-6
  are all non-blocking. No author correction cycle was needed.
- Manager disposition of the verifier notes:
  - **N-1.** Recorded as a residual. It is not repaired, because the
    proposal's proving test for R12 was followed exactly and this slice does
    not enlarge the specification.
  - **N-2 to N-4.** Precision notes on the proposal's own verbatim text.
    Recorded for the specification owner; no action in this slice.
  - **N-5.** The manager's `run_registered_checks.py` run left an ignored
    `tools/software_workflow/__pycache__/`. The manager deleted it; no ignored
    or untracked file remains outside `.claude/`.
  - **N-6.** Addressed by this log.
- N5: `rely-for-production` preflight before fan-in, run from `projects/pec`
  with the same register and script as in `PREIMAGE.md`: ALLOW, exit 0, for
  all five opened paths. Containment and whitespace are below.
- N6: one `MEMORY.md` entry appended (postimage
  `54f57151e5ad1a3b6d72b2f7ccc23bfae2a9fc567da7d10daf9feee0db0c2b14`).
  `_STATUS.md` is unchanged (`d9429b4e…555b`).

## Containment and whitespace (N5)

`git diff --name-only 9ffc54afc`, excluding this run root
(`P1_STORE_GUARD_03/**`). The run root holds `RUN.md`, `PREIMAGE.md`,
`AUTHOR_RETURN_01.md`, `VERIFIER_VERDICT_01.md`, `checks/` and `probes/`.

```
projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-03_Store_bootstrap_content_minimal_guard/MEMORY.md
projects/pec/v2/docs/STORE_LIFECYCLE_AND_GUARD.md
projects/pec/v2/src/pec_v2/adapters/storage/sqlite_store.py
projects/pec/v2/src/pec_v2/core/content_minimal_guard.py
projects/pec/v2/tests/storage/test_content_minimal_guard.py
projects/pec/v2/tests/storage/test_store_lifecycle.py
```

That is exactly the five granted paths plus `MEMORY.md`. `git diff --check`
against the base exits 0. No `__pycache__` is staged or present.

`origin/main` advanced during the run to `4f59d3b036cd7e5fcd4bd20b50eeb2bed2fe9b19`,
the PR #896 merge (the reverse-engineer successor basis). That PR touches
seven Root, workflow and sister-project coordination paths, none of which
overlaps this slice. The branch was not rebased. It stays on the verified
base `9ffc54afc`, and the PR diff against `main` contains only the paths
above.

## Final postimages (relative to `projects/pec/`)

| Path | SHA-256 |
|---|---|
| `v2/src/pec_v2/core/content_minimal_guard.py` | `2cb21e2d251eeffd164d68ad436cb0b9f0d4b8fdabd41358f33a0d7ed40122b3` |
| `v2/src/pec_v2/adapters/storage/sqlite_store.py` | `edb15e2b96eb3b5cdf918c05cf58fce128063b02475233649e30bcc92864ad5c` |
| `v2/tests/storage/test_content_minimal_guard.py` | `3a4c98b32b1e4e07f921d7b567120377c63b7e526e0322480216346828ae8cba` |
| `v2/tests/storage/test_store_lifecycle.py` | `96d9917d6283eeb8fd6310991cd0166ecd24bcf76afccae840afee508ec2fb64` |
| `v2/docs/STORE_LIFECYCLE_AND_GUARD.md` | `1fc417fc6b5461bd0623780e751bf37354df491f3f28e713b98c7d29417130a3` |
| `v2/src/pec_v2/core/ports/store.py` (unopened) | `d7544f7191c38a40df49e55c8aaadbb54ea122003be5eb6ab7a2a1d6400a05eb` |
| `v2/src/pec_v2/adapters/storage/__init__.py` (unopened) | `c9d8b3e5a1338ecf9dbc5a7405c47c69956e3c68e3219f60e3c988c1f1880540` |
| `software-workflow.json` (unopened) | `8ec9ba6dcba7ea6b935923f5b4d846b2a9ac3f3d5cc43f5e160abe0971058a8b` |

## Per-repair status

| Repair | Status | Proving test (in place) |
|---|---|---|
| R9 exact-type rule | done | `test_ver_008_policy_is_fixed_finite_and_domain_checked` (subclass constructors, `ConformingInt`, AST no-`isinstance`); `test_ver_008_forged_wrappers_are_revalidated_and_rejected_without_crashing` (14-input batch, `(14, 0, 14)`) |
| R10 content-minimal failures | done | `test_ver_005_rejections_are_located_and_accounting_has_no_silent_loss_or_substitution` (two tuples changed); forged-wrapper test (E-3 payload inputs) |
| R11 `close()` | done | `test_ver_002_creation_restart_closed_delete_open_reset_and_empty_recreation` |
| R12 `reopen()` mkdir | done | `test_ver_002_…` (regular file at `.pec-v2`; the permission path is covered by probes only, N-1) |
| R13 `delete()` unlink | done | `test_ver_002_…` |
| R14 documentation | done | verifier review, `VERIFIER_VERDICT_01.md` §5 |

## Delegation record

| Child | Mechanism | Parent | Type / model requested | Model reported by host | Cycles | Limits (instruction-asserted) |
|---|---|---|---|---|---|---|
| Author | Claude Code Agent tool, `subagent_type: pec-task`, `model: opus`, foreground | this WORKING_ITEMS manager | TASK (Type 2), `claude-opus-5-5`, high | `claude-opus-5-5` | 1 | Five granted paths plus `probes/**` and `AUTHOR_RETURN_01.md`; no state-changing git; no delegation |
| Verifier | Claude Code Agent tool, `subagent_type: pec-reviewer` (host type without Edit/Write tools), `model: opus`, foreground | this WORKING_ITEMS manager | TASK (Type 2), `claude-opus-5-5`, high | `claude-opus-5-5` | 1 (PASS) | Read-only, host-enforced by the absence of write tools; scratch outside the checkout; independent probes; no repair; no delegation |

The reasoning level is instruction-asserted; neither child could confirm it.
Both final reports returned directly to this manager, so no relay by
HELP_HUMAN was needed.

## Residuals and items for the caller

1. **N-1 (test coverage).** R12's permission-denied `mkdir` path is proven by
   probes only. The in-place test uses the regular-file case, as the proposal
   specifies. Strengthening it would be a later in-place test extension and
   needs its own grant.
2. **N-2 to N-4 (precision of the proposal's verbatim R14 text).** The
   placeholder list omits `<unknown>`, which the guard returns to a non-store
   caller. "Every string in a `GuardedRecord`" loosely includes the
   `FieldClass` enum member, although its persisted `.value` is an exact
   `str`. The unwrapped `connection.close()` inside `reopen()`'s error
   handlers can raise only when that close fails during an open that is
   already failing. None of the three makes the text untrue. Each is for the
   specification owner, if they want it tightened.
3. **C2-4.** Stated threat boundary; it still reproduces by design.
4. No CHECKING, ISSUED or artifact acceptance. DEL-01-03 remains
   `IN_PROGRESS`. The receipt, `docs/STATUS.md`, `README.md` and HELP_HUMAN's
   `RUN.md` are HELP_HUMAN's to maintain.
