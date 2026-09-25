# RUN — P1_STORE_GUARD_04 (D-PEC-91 A-53 COUNT-domain slice)

Role: WORKING_ITEMS (Type 1), instruction-asserted, owning PKG-01 / DEL-01-03
only. Parent: HELP_HUMAN run `HELP-HUMAN-PEC-20260923-SCA005`, node C4.
Brief: `C4_D91_COUNT_DOMAIN_SLICE.md` in HELP_HUMAN's session scratchpad
(`.../scratchpad/closeout/`), SHA-256
`51a5152699b465f35afa19099c866c6c6e2f2baa19d4bad71d27c9e5832ae497`, read from
disk and hashed by this manager. No other scratchpad file was read.
Date: 2026-09-25 (session date). Host: Claude Code Agent tool, isolated
worktree. Model steer: `claude-opus-5-5`, high reasoning (D-PEC-91 ruling,
owner question 5). The host reports the manager as `claude-opus-5-5`; the
reasoning level is instruction-asserted.

## Basis (actual origins and SHA-256 at `origin/main` `8b6553850aa8a98cb44aed02e9fe91e23b1234bd`)

| Source | SHA-256 |
|---|---|
| `AGENTS.md` (Root) | `c8ce87ef342902cb081bc659b26fc9a4edda1b6dba513814e5cb1e14e0b1dffd` |
| `projects/pec/AGENTS.md` | `46689c36d5379029a34a5c5d26f109445e338fca82b86e590826bcbc39ad3846` |
| `agents/AGENT_WORKING_ITEMS.md` | `9ae4bea25bd95750a6878a9d53fbbbd7cd058d72c652a36baf4aa90601799665` |
| `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-91_RULING_2026-09-25.md` | `5d896204a0afcf39066f5aa56a9e043d199ed8fe7eb96397bcbe054f90ef3fbe` |
| `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-91_del_01_03_count_domain_encoding_residual_proposal_2026-09-25.md` | `5c044b095621bfb098bb3d4e69d55b5a0594a3c73322d58b440a767e2d2413ec` (matches the ruling and the brief) |
| `projects/pec/execution/_Coordination/_DECISIONS/_REGISTER.md` (D-PEC-91 row, line 108: `RULED A-53 / EFFECTIVE ON MERGE`) | `a18b54f872f8df80691647bb982926fa1756b1d2297eb3a7ffe8caab12d85250` |
| `projects/pec/docs/PRD.md` | `6833553c33aadca00e4ee6932d56ae4698c2ae7798c30b603bc17e60dae477ba` |
| DEL-01-03 `ScopeOfWork.md` | `986ef15532cd65f17e8276ee9194b29469f559aca5616d2d3412fa3effca6341` |
| `workflows/software-bounded-implementation/WORKFLOW.md` (bundled, `chirality-root:bundled:workflow:software-bounded-implementation`; author method) | `2ea0ddf4f53241fa94274e709b8042ad9de4d8beb9c82cd1ed1dcd0c6f8f0f7b` |
| `.agents/skills/software-code-review/SKILL.md` (project skill; verifier method) | `06c27b1be5cfbd9e638570918a8f837d8439c8073c40d3ef708e53874f95570a` |
| `agents/AGENT_TASK.md` (read by both children as their role file; not loaded by this manager) | `1a13a5b00b3ce01ff8519efe6b46bcbe0cd6a5b7985e24282fa7efa2c57c8fb7` (as each child reported) |
| `projects/pec/execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260923-SCA005/returns/L2A_REVIEW_DEL-01-03.md` (context, immutable) | `b1f8731613d8645f9454bedefd25c02a41d04f24356ac3bb40587afdb82041c5` |
| `_run_records/P1_STORE_GUARD_03/RUN.md` (context, immutable) | `078914b85147417175fc8e701f80fd4799d48131e13e932d9e7bacbe38bc1b17` |

The specification is the proposal's per-repair table, R15 exact rule, R17
edits D1–D10, finite verification, administrative grant, rollback and limits,
with the ruling's A-53 substitutions and its clarifications N-2..N-5 and
"A-53 consequential wording":

- `_MAX_COUNT = 2**53 - 1`; its comment cites the JSON safe-integer range
  (RFC 8259), not SQLite INTEGER; 16 decimal digits, not 19.
- `2**53 - 1` admitted and rendered `"9007199254740991"`.
- `2**53` replaces `2**63` in `invalid_values`.
- Over-bound list `(2**53, 2**63, 10**639, 10**5000)`.
- D1, D2 and D5 use `2**53 - 1` (9,007,199,254,740,991) and `2**53`; D1's
  rationale sentence is the proposal's A-53 sentence (L169); D1's digit count
  is 16.
- D10 states the COUNT bound as `2**53 - 1` rather than "at most 63 bits".
- M2, M3 relative to the A-53 bound; M6 (widening to `10**4000`) unchanged.
- N-4: each run records whether R16's read-only block actually ran.

## Preconditions

1. Fetched `origin/main` = `8b6553850aa8a98cb44aed02e9fe91e23b1234bd`
   (PR #902 merge; `merge-base --is-ancestor` confirms it). The ruling
   file and the D-PEC-91 register row are present. PASS.
2. Fresh preimage verification: all four opened paths and the four unopened
   paths match the proposal's rollback table (see `PREIMAGE.md`). PASS.
3. Reliance-hold `dispatch-for-production` preflight: ALLOW, exit 0, for all
   four opened paths (see `PREIMAGE.md`). PASS.

Branch: `claude/pec-d91-count-domain-slice`, created from fresh `origin/main`
`8b6553850` with `--no-track` (the host permitted the new local branch).
Interpreter: `/Library/Frameworks/Python.framework/Versions/3.13/bin/python3`,
Python 3.13.7; SQLite 3.50.4; `id -u` 501. Commit identity: no
`user.email` is configured (exit 1); commits use the auto-derived identity
`Ryan Tufts <ryan@Ryans-MacBook-Air.local>`, as the base's recent non-merge
commits do (`c906efbc5`, `3dedb4c52`, `ca85173ad`).

## Work graph

| Node | Owner | Act | Depends |
|---|---|---|---|
| N1 | WORKING_ITEMS | Preconditions, branch, run root, `PREIMAGE.md` | — |
| N2 | TASK author (`pec-task`, opus) | F-1 before-reproduction on preimage (run-root scratch, limits default/640/0); R15–R17 with A-53 on the four paths under software-bounded-implementation; after-reproduction; mutation runners under `probes/`; `AUTHOR_RETURN_0N.md` | N1 |
| N3 | WORKING_ITEMS | Five registered checks and verbose storage run under `checks/`; M1–M7 and D-PEC-89 M1–M9 reruns under `checks/` | N2 |
| N4 | TASK verifier (`pec-reviewer`, opus, read-only) | software-code-review; substantive admissibility; independent F-1 reproduction on preimage and candidate; boundary cases; R16 block; R17 text; verdict saved by the manager as `VERIFIER_VERDICT_0N.md` | N3 |
| N2'/N4' | author / verifier | Correction cycles while a blocking finding remains | N4 |
| N5 | WORKING_ITEMS | `rely-for-production` preflight, containment, whitespace, ASCII | N4 PASS |
| N6 | WORKING_ITEMS | One `MEMORY.md` entry | N5 |
| N7 | WORKING_ITEMS | Commit, push, PR (no merge) | N6 |

## Progress log

- N1 complete.
- N2 cycle 1 complete: author record `AUTHOR_RETURN_01.md` (SHA-256
  `c4c661ca7e7654aa9ec1796c3a68d01d44729401e31028888194e92f7d7fb0ae`; agent id
  `a6e31d5e589b2f651`, host-reported model `claude-opus-5-5`; the final report
  returned directly to this manager through the foreground Agent call, so no
  HELP_HUMAN relay was needed). R15–R17 are applied with the A-53
  substitutions to the four granted paths; the suite has 13 tests with no new
  test ID. The author's F-1 probe `probes/probe_d91.py` reproduced F-1 on the
  preimage before any edit (`probes/probe_BEFORE_preimage.out`) and shows it
  closed on the postimage (`probes/probe_AFTER_postimage.out`). R16's block
  ran for the author (`probes/r16_block_probe_AFTER.out`: a marker written
  from inside the block in a scratch copy). Scratch trees and stores lived in
  self-removing temporary directories outside the checkout. Manager review of
  the diff: it matches the specification with the A-53 substitutions; the
  author's judgment calls J1–J7 were passed to the verifier.
- N3: manager ran the five registered checks from the repository root as
  `python3 tools/software_workflow/run_registered_checks.py projects/pec/software-workflow.json --check <id> --output <RR>/checks/<id>.json`
  with `PYTHONDONTWRITEBYTECODE=1`. Each exited 0 with status PASS:
  `v2-store-guard` (Ran 13, OK), `v2-core-posture` (`"verdict": "PASS"`,
  `core_tree_sha256` `88f590c019eb67febfbb569a34ec688831edc7e867f251376ecebe3f7799c016`),
  `v2-loop-registry` (Ran 12, OK), `v2-api-contract` (Ran 6, OK) and
  `harness-self-check` (INFO=14, NOT_APPLICABLE=1, REVIEW=4, WARN=124, the
  prior baseline). The wrapper's stdout, which only echoed paths, was not
  retained. Verbose storage run from `projects/pec`:
  `python3 -m unittest discover -s v2/tests/storage -p 'test_*.py' -v`,
  exit 0, 13 tests `ok` (`checks/v2-store-guard_verbose.out`).
  Mutations (fresh manager reruns after reviewing the author's runner), from
  `projects/pec` with `PYTHONDONTWRITEBYTECODE=1`:
  `python3 <RR>/probes/mutate_d91.py v2` exit 0, `RESULT PASS`, M1–M7 each
  caught by the named tests (`checks/mutate_d91_manager_run.out`; the runner
  reports the host enforces directory permissions: True); and
  `python3 <P1_STORE_GUARD_03>/probes/mutate_d89.py v2` (immutable runner, run
  read-only) exit 0, `RESULT PASS`, D-PEC-89 M1–M9 each caught
  (`checks/mutate_d89_manager_run.out`).
- Candidate commit for review: `d9dcb0126f3cb054ea542f62091d1fcf3122601c`
  (local, before push), containing the four product paths and the run root
  as of N3.
- N4 cycle 1: verifier **PASS**, no blocking finding (`VERIFIER_VERDICT_01.md`;
  agent id `aba7254fd920b8534`, `pec-reviewer`, host-reported
  `claude-opus-5-5`; returned directly to this manager and saved verbatim
  with a provenance header). The verifier reviewed `d9dcb0126`, reproduced
  F-1 independently with its own probe on git-archive exports of the preimage
  and the candidate at limits 4300, 640 and 0, exercised the boundary cases
  (`2**53 - 1`, `2**53`, 0, -1, `True`, `False`, `int` subclasses in and out
  of range, `10**639`, `10**4300`, `10**5000`), applied its own M1–M7 plus
  X1–X3, re-ran the D-PEC-89 runner, confirmed with its own probe that R16's
  block ran on this host (uid 501, `os.access` False, `PermissionError`
  cause), and rebuilt the R17 text from the proposal bytes with the A-53
  substitutions (equal after whitespace collapse; only D7/D9 line breaks
  differ). No author correction cycle was needed.
- Manager disposition of the verifier notes:
  - **N-1** (doc `:122` "nonnegative counts … fit the finite classes" is
    broader than the stated bound). Carried as a residual: the grant keeps
    every other doc line byte-unchanged, so this slice does not edit it.
  - **N-2** (this log incomplete at `d9dcb0126`; `AGENT_TASK.md` hash
    absent). Repaired in this record: N2–N7 are logged and the
    `AGENT_TASK.md` row is added to the basis table.
- N5: `rely-for-production` preflight before fan-in, run from `projects/pec`
  with the same register (`f877d931…41cbc`, header only) and script as in
  `PREIMAGE.md`: `{"operation": "rely-for-production", "status": "ALLOW"}`,
  exit 0, for all four opened paths. Containment and whitespace are below.
  Refetched `origin/main` is still `8b6553850`.
- N6: one `MEMORY.md` entry appended (postimage
  `44b360c57b934c585befe2cf6a0741199d4cc4ac6b8fc64c04f7be33b88bdae6`).
  `_STATUS.md` is unchanged (`d9429b4e…555b`).
- N7: commit, push to `origin/claude/pec-d91-count-domain-slice`, PR against
  `main`. Not merged by this manager. PR URL and head are returned to
  HELP_HUMAN; they are not recorded here because this file is part of that
  head.

## R16 host condition (N-4)

| Run | Host condition | Block ran? | Evidence |
|---|---|---|---|
| Author (N2) | uid 501, macOS, directory permissions enforced | yes | `probes/r16_block_probe_AFTER.out` (marker written inside the block); M7 caught by `test_ver_002` in `probes/mutate_d91_AFTER.out` |
| Manager (N3) | uid 501, same host | yes | `checks/mutate_d91_manager_run.out`: host enforces permissions True; M7 caught by `test_ver_002` |
| Verifier (N4) | uid 501, same host | yes | `VERIFIER_VERDICT_01.md` §6: own probe, `os.access` False, `PermissionError` cause; X1 (block disabled plus M7) survives, M7 caught |

## F-1 before and after

| COUNT input | Preimage, limit 4300 | Preimage, 640 | Preimage, 0 | Postimage (4300, 640, 0) |
|---|---|---|---|---|
| `2**53 - 1` | admitted `"9007199254740991"` | same | same | admitted `"9007199254740991"` |
| `2**53`, `2**63`, `2**64`, `10**639` | admitted; batch `(2, 2, 0)` | same | same | located `INVALID_VALUE`; batch `(2, 1, 1)`, only `good` persisted |
| `10**4300`, `10**5000` | `guard()` and `admit_batch` raise `ValueError`; nothing persisted | same | admitted; 4,301/5,001-digit value persisted | located `INVALID_VALUE`; batch `(2, 1, 1)`, only `good` persisted |
| `-1`, `True`, `int` subclass | located `INVALID_VALUE` | same | same | located `INVALID_VALUE` |

Sources: `probes/probe_BEFORE_preimage.out`, `probes/probe_AFTER_postimage.out`
(author) and `VERIFIER_VERDICT_01.md` §3–§4 (independent).

## Containment and whitespace (N5)

`git diff --cached --name-only origin/main` (`8b6553850`) at fan-in, with the
run root collapsed (`P1_STORE_GUARD_04/**`: `RUN.md`, `PREIMAGE.md`,
`AUTHOR_RETURN_01.md`, `VERIFIER_VERDICT_01.md`, `checks/` (8 files) and
`probes/` (11 files)):

```
projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-03_Store_bootstrap_content_minimal_guard/MEMORY.md
projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-03_Store_bootstrap_content_minimal_guard/_run_records/P1_STORE_GUARD_04/**
projects/pec/v2/docs/STORE_LIFECYCLE_AND_GUARD.md
projects/pec/v2/src/pec_v2/core/content_minimal_guard.py
projects/pec/v2/tests/storage/test_content_minimal_guard.py
projects/pec/v2/tests/storage/test_store_lifecycle.py
```

That is exactly the four granted paths, the run root and `MEMORY.md`.
`git diff --cached --check origin/main` exits 0. Changed `.py` lines are
ASCII-only (verifier §1). No `__pycache__` or `.pec-v2` was created by this
run; `git status --short --ignored` shows nothing outside the staged scope.
Two tracked `__pycache__` directories under the repository-root
`execution/_Coordination/AgentRuns/SOW-PKG02-BATCH-EXPERIMENT-20260714-01/`
pre-exist on the base; they are external state and untouched. No large scratch
export was created in the checkout; every scratch tree lived in a
self-removing or removed temporary directory outside it.

## Final postimages (relative to `projects/pec/`)

| Path | SHA-256 |
|---|---|
| `v2/src/pec_v2/core/content_minimal_guard.py` | `740a4a74122178cc31947bb69c23d6aa55abc15b87c523dcf1c551dee3e19ee9` |
| `v2/tests/storage/test_content_minimal_guard.py` | `d4655f2f95e953b2f27ce43e1d622260be86d883fa6050fa7b3e2e6fe9468ead` |
| `v2/tests/storage/test_store_lifecycle.py` | `b51ca900667d38b47de3dfc514a350d7aabff157f447bb05e6ada9c0edc6d3e7` |
| `v2/docs/STORE_LIFECYCLE_AND_GUARD.md` | `89c3a5fcc722a232a587a721949cb3ec0ef69825f6e266ef36b29fa69d32cadb` |
| `v2/src/pec_v2/adapters/storage/sqlite_store.py` (unopened) | `edb15e2b96eb3b5cdf918c05cf58fce128063b02475233649e30bcc92864ad5c` |
| `v2/src/pec_v2/core/ports/store.py` (unopened) | `d7544f7191c38a40df49e55c8aaadbb54ea122003be5eb6ab7a2a1d6400a05eb` |
| `v2/src/pec_v2/adapters/storage/__init__.py` (unopened) | `c9d8b3e5a1338ecf9dbc5a7405c47c69956e3c68e3219f60e3c988c1f1880540` |
| `software-workflow.json` (unopened) | `8ec9ba6dcba7ea6b935923f5b4d846b2a9ac3f3d5cc43f5e160abe0971058a8b` |

The four product postimages are byte-identical between the reviewed
candidate `d9dcb0126` and the final head; the later commit adds only run-root
records and the `MEMORY.md` entry.

## Per-repair status

| Repair | Closes | Status | Proving test (in place) |
|---|---|---|---|
| R15 COUNT domain `0..2**53 - 1` | F-1 (and the int-limit part of F-6) | done | `test_ver_008_policy_is_fixed_finite_and_domain_checked` (`2**53 - 1` admitted as `"9007199254740991"`; `2**53`, `2**63`, `10**639`, `10**5000` located at limits default/640/0; two added `invalid_values`); `test_ver_005_rejections_are_located_and_accounting_has_no_silent_loss_or_substitution` (input 14 `over-count`, counts `(15, 1, 14)`) |
| R16 read-only checkout | F-4 (D-PEC-89 N-1; X5) | done; block ran on this host | `test_ver_002_creation_restart_closed_delete_open_reset_and_empty_recreation` |
| R17 documentation D1–D10 | F-1 doc; F-2; F-3; F-11; F-6/F-8 wording | done | verifier review, `VERIFIER_VERDICT_01.md` §7 |

## Delegation record

| Child | Mechanism | Parent | Type / model requested | Model reported by host | Cycles | Limits (instruction-asserted) |
|---|---|---|---|---|---|---|
| Author | Claude Code Agent tool, `subagent_type: pec-task`, `model: opus`, foreground; agent id `a6e31d5e589b2f651` | this WORKING_ITEMS manager | TASK (Type 2), `claude-opus-5-5`, high | `claude-opus-5-5` | 1 | Four granted paths plus `probes/**` and `AUTHOR_RETURN_01.md`; scratch outside `v2/**`; no state-changing git; no delegation |
| Verifier | Claude Code Agent tool, `subagent_type: pec-reviewer` (host type without Edit/Write tools), `model: opus`, foreground; agent id `aba7254fd920b8534` | this WORKING_ITEMS manager | TASK (Type 2), `claude-opus-5-5`, high | `claude-opus-5-5` | 1 (PASS) | Read-only (write tools absent by host type; Bash writes limited by instruction to a `mktemp -d` scratch outside the checkout, removed); independent probes; no repair; no delegation |

The reasoning level is instruction-asserted; neither child could confirm it.
Both final reports returned directly to this manager, so no relay by
HELP_HUMAN was needed.

## Residuals and items for the caller

1. **Verifier N-1.** `STORE_LIFECYCLE_AND_GUARD.md:122` ("nonnegative counts
   … fit the finite classes") is broader than the COUNT bound now stated in
   the COUNT row. It stays byte-unchanged because the grant allows only
   D1–D10. A later granted edit of this file could qualify it.
2. **R16 host dependence.** R16 is proven only where directory permissions
   are enforced. On a root runner the block does not run (as D3 states) and
   M7 would survive there. All three runs in this slice enforced permissions.
3. **Carried from the ruling (not part of this grant).** Counts above
   `2**53 - 1` would need a separate decision (string transport);
   response-size budgets belong to the D-PEC-90 amendment (node H6) and the
   API/orientation work.
4. L-2a findings F-5, F-7, F-9, F-10, F-12 remain out of this slice as the
   proposal disposes them.
5. No CHECKING, ISSUED or artifact acceptance. DEL-01-03 remains
   `IN_PROGRESS`. The receipt, `docs/STATUS.md`, `README.md` and HELP_HUMAN's
   `RUN.md` are HELP_HUMAN's to maintain.
