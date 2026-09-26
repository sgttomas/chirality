# VERIFIER_VERDICT_01: D-PEC-96 option A act (PR #950)

> Transcribed by the manager from the verifier's hand-back (agent `a79a9fdd7f3abb1ed`, `pec-reviewer`, dispatched read-only with `run_in_background: false`). The verifier could not write files. Only two changes were made. The report's indentation was removed, and in "Relevant paths" the absolute worktree prefix `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/agent-a250ffe27d6b8a45c/` was shortened to repository-relative paths.

- **Verifier:** fresh read-only TASK (Type 2). I authored nothing in this candidate and delegated nothing. The host reports the serving model as Opus 5.5 (`claude-opus-5-5`). The role and the `high` effort come from my instructions; the host does not enforce them.
- **Date:** 2026-09-26, America/Edmonton (MDT). Reproduction ran at 01:48:45 MDT.
- **Interpreter:** `/Library/Frameworks/Python.framework/Versions/3.13/bin/python3`, CPython 3.13.7, run with `PYTHONDONTWRITEBYTECODE=1`.
- **Candidate:** PR #950. It is OPEN, and the GitHub API reports its head as `a8e6fd959b959ae28ccb2b591d2b235e313fb2e1` with 73 files. Branch `claude/pec-d96-registry-act`.
- **Basis:** `f90320c1d110cad75d04c96c91a595b7eb244498`, the PR #946 merge and the merge base.
- **origin/main has moved.** After `git fetch origin` it is `53145aaebb23b617e7ba1d2c626a6218d2be9176`: PR #947 merged at 01:39:30 MDT, during the act. That change touches none of the candidate's paths, and `git merge-tree --write-tree origin/main a8e6fd959` merges cleanly (tree `5cf1c20a…`). `f90320c1d` was therefore used as the diff base.
- **Scope of this verdict:** no claim of CHECKING, ISSUED, acceptance, readiness or reliance.

## Instruction sources read (SHA-256, at a8e6fd959)

| Source | SHA-256 |
|---|---|
| `AGENTS.md` (Root) | `c8ce87ef342902cb081bc659b26fc9a4edda1b6dba513814e5cb1e14e0b1dffd` |
| `projects/pec/AGENTS.md` | `c9d3b44dfb5b07cff9790d58a67ff02825e297fcf0d2e290ab1599bf59ee197a` |
| `agents/AGENT_TASK.md` | `1a13a5b00b3ce01ff8519efe6b46bcbe0cd6a5b7985e24282fa7efa2c57c8fb7` |
| `.agents/skills/software-code-review/SKILL.md` (applied) | `ee085d589c44f912d11a59eead8edac214f0343761d26b0d33e886a979888bca` |
| Ruling `D-PEC-96_RULING_2026-09-26.md` | `852057f0ff6989e0b1180232424ff9fd8de434b3345c1d6c775e76b8defb399e` (same at base, head and current origin/main) |
| Proposal revision 4 | `4506597b1bfd6cafd8fc561c688bcb9e803d9c2b04c3abdec9dc05edf155180e` (same at base, head and origin/main) |
| `_REGISTER.md` | `01b8d184e231dfe7bde5f7c78e169c1e913e53bb04ea413109159ae2816c1a14` (same at base, head and origin/main) |
| `D-PEC-94_owner_direction_loop_migration_2026-09-25.md` (basis citation) | `b6814e902c23f24020337ab925a7c287b66b5ee485785bee07b042e25e1e5a6b` |
| `docs/templates/MEMORY_TEMPLATE.md` | `5a9564f4663b000cdf0175bf4f0262001001bc50c719912499df2527d01c6a5a` |

## Export identities

All exports were made with `git archive` under the throwaway directory `/private/tmp/claude-501/d96verify.TBKvuj/`, outside every checkout.

| Export | Commit | Tar SHA-256 | Git tree |
|---|---|---|---|
| Base (reproduction source) | `f90320c1d` | `base.tar` `8cd23c89714451af712822676d41221e79ae7344dc8cb36e8fc346573677e62f` | `fc168aa77cd85875056cc4e45898d2dc287e53f8` |
| Candidate head | `a8e6fd959` | `head.tar` `c5473b193b47a98af599a9b7ab40f8183973a28dffaf861fb218ebdd55f5b042` | `b1dd23d8415fc400d5fafd373c548ceb9f586e8d` |
| Current main | `53145aaeb` | `main.tar` `3f61072707c9921d375cfad099a82f5bc410fd2fffc40516e14af4ec616cae87` | — |

- **Reproduction tree:** a fresh extraction of `base.tar`, with the bound script applied once. Its `projects/pec/v2/` is identical to the head export's (`diff -rq`, no output).
- **harness-self-check and receipts validator:** these need Git. For them the base and head exports were turned into throwaway repositories, as the proposal's "Preparation evidence" describes: `git init`, a read-only `objects/info/alternates` entry pointing at `/Users/ryan/ai-env/projects/chirality/.git/objects`, `read-tree`, and `update-ref HEAD` plus `refs/remotes/origin/main` set to `f90320c1d`. These writes stayed inside the exports.
- **Manager's worktree:** it was only read. It is still clean at `a8e6fd959`.

## Checks

| # | Check | Command (summary) | Exit | Observed |
|---|---|---|---|---|
| 1 | Basis | `git show origin/main:…` via the main export: ruling, proposal and register row | — | The ruling is present on current origin/main with the expected hash. The register row D-PEC-96 reads `RULED A / EFFECTIVE ON MERGE` and quotes the owner's direction. Run-root `apply_d96.py` is `80725b4f…bbf3` and `mutate_d96.py` is `57c2f031…26f0`; both are `cmp`-identical to the prep copies. |
| 1 | Preimages | `grantcheck.py`: grant table parsed from the proposal, compared with base hashes and the script's READ and UNCHANGED lines | 0 | 11/11 READ lines equal the grant preimages, with `schema_version_1.json` recorded as `absent`. 6/6 must-remain files match. Path-list hash is `b5db12e5…c73c`. |
| 2 | Reproduction | `PYTHONDONTWRITEBYTECODE=1 <py3.13> apply_d96.py --repo <fresh base export>` (the prep copy, hash-verified) | 0 | 6 UNCHANGED, 11 READ, **11 WRITE**, `OK option=A files=11 mode=written`, empty stderr. The report is byte-identical to the run root's `apply_d96_report.txt`. All 11 written files are `cmp`-identical to head. `diff -rq` against base shows exactly the 11 paths. |
| 2 | Fail-closed probes | Rerun on the applied tree; `--pec-row remaining` | 1 / 2 | The rerun gives "FAIL preimage mismatch v2/config/loops.json …; nothing written". `--pec-row` is an unrecognized argument. |
| 3 | `v2-loop-registry` | `run_registered_checks.py … --check v2-loop-registry` on head, plus a direct `unittest discover -s v2/tests/config` | 0 | **Ran 19, OK**, against Ran 12, OK on base. My 19 verbose test names equal the manager's `post_loop_registry_verbose.out`. |
| 3 | `v2-store-guard` | registered runner | 0 | Ran 13, OK (base the same) |
| 3 | `v2-api-contract` | registered runner | 0 | Ran 6, OK (base the same) |
| 3 | `v2-core-posture` | registered runner, plus a direct `check_service_core_posture.py` | 0 | PASS with `findings: []`. Core tree is `dd7e1ddaddb269525e45699158e31e5a9ce6d252dab27b14ce59c5b2ad9e6e5a`, against `88f590c019eb…c016` on base. Config `20d64ff3…09ed` and workflow `8ec9ba6d…a58b` are unchanged. |
| 3 | `harness-self-check` | registered runner, plus direct `harness.py self-check` on the base and head throwaway repos | 0 / 0 | `INFO=14, NOT_APPLICABLE=1, REVIEW=4, WARN=126`. Base and head stdout are byte-identical at `8856b78faa65…70fe`, the same hash as the manager's pristine, pre and post outputs. |
| 3 | `v2/tests/enforcement` | `unittest discover -s v2/tests/enforcement` | 0 | Ran 28, OK (base the same) |
| 3 | Selection | `select_affected_checks.py projects/pec/software-workflow.json <11 project-relative paths>` | 0 | Exactly `harness-self-check`, `v2-api-contract`, `v2-core-posture`, `v2-loop-registry`, `v2-store-guard` |
| 3 | Mutation | bound `mutate_d96.py projects/pec` on head (hash-verified copy) | 0 | BASELINE exit=0. M1–M19 are all CAUGHT, 0 NOT_APPLIED, `TOTAL 19/19 CAUGHT`, `RESULT PASS`. The output is byte-identical to the manager's `mutate_d96.out`. |
| 3 | Byte identity | SHA-256 of the 11 head paths against the grant table | 0 | 11/11 equal |
| 3 | Basis citations | `is_file` on `loop_init_path` and each `basis` in the head `loops.json` | 0 | 4/4 present |
| 3 | Non-ASCII and CR | byte scan of the 11 postimages | 0 | 0 non-ASCII bytes, 0 CR |
| 3 | Vocabulary | `grep -rniE 'remaining\|status-remaining' v2/config v2/src v2/tests/config` | 1 | No match |
| 3 | Whitespace | `git diff --check origin/main...a8e6fd959` (merge base `f90320c1d`) | 0 | No output |
| 3 | Receipts validator | `validate_pec_loop_receipts.py --repo-root .` on the base and head throwaway repos | 0 / 0 | VALID. Output is identical apart from the path prefix. The manager's pre and post outputs are `087c6e54…1558` for both. |
| 3 | Strict register validator | `validate_decomposition_registers.py --strict projects/pec/execution` on base and head | 1 / 1 | 0 errors and 26 warnings, all `XRG-013`. Base and head outputs are byte-identical at `0aa450c5…e905`, equal to the manager's pristine, pre and post outputs. No new finding. |
| 4 | Semantics | Adapter, schema, port, tests and fixtures read; proposal JSON and Python blocks compared to the files; schema surfaces compared to `FEED_PROFILE_SURFACES` in code | — | See below. Holds, with the notes in N3 and N6. |
| 5 | Containment | `git diff --name-status origin/main...a8e6fd959` (merge base `f90320c1d`) | 0 | 73 paths: 11 product paths with their granted acts (10 M, 1 A for `schema_version_1.json`), `DEL-01-06/MEMORY.md` A, and 61 files under the run root. Nothing else. None of the files the brief lists as must-stay-unchanged appears in the diff. The return file is absent, which is allowed. |
| 6 | MEMORY.md | `diff` against `docs/templates/MEMORY_TEMPLATE.md` | 1 (expected) | The only difference is line 1, `{{DEL-ID}}` becoming `DEL-01-06`. The Runs table is empty. SHA-256 is `035ecb86…0a3f`, matching `MANIFEST.md`. |
| 7 | Run records | Hashes, SHAs, counts and claims checked against the evidence and live bytes | — | Accurate except N1 and N2. No claim of CHECKING, ISSUED, acceptance, lifecycle change or a fabricated ruling. |
| 8 | Reliance hold | From head `projects/pec`: `pec_reliance_hold.py --register execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv --target <each of 11> --operation rely-for-production` | 0 ×11 | 11/11 `{"operation": "rely-for-production", "status": "ALLOW"}`. The register (`f877d931…41cbc`, header only) and the script (`b1712e4b…cd0e`) are unchanged on current origin/main. |

### Semantics detail (check 4)

- **Proposal blocks equal the files.** The proposal's JSON and Python blocks are byte-equal to head `loops.schema.json`, `loops.json` and `core/ports/loop_registry.py`.
- **Schema fields.** The schema documents every field: `schema_version`, `loops`, `loop_id`, `loop_init_path`, `feed_profiles`, `profile`, `version`, `state` and `basis`.
- **Vocabulary.** The schema's `oneOf` consts, `FEED_PROFILE_VERSIONS` and `FEED_PROFILE_SURFACES` are the same three profiles. Each option's "Surfaces:" list equals the adapter's set.
- **No Remaining terms.** Neither the schema nor the adapter names `## Remaining`, `remaining-items`, `remaining-loop` or `status-remaining`.
- **Coherence rules.** The adapter enforces disjoint surfaces, failing at the later entry's `.profile` (`loop_registry.py` L180–188). It enforces at least one live profile at `.feed_profiles` (L200–201), and duplicate profiles at the second occurrence (L159–163).
- **Failures.** Every failure is located through `_fail(location, …)`. The return is built only after full validation, so no partial set is returned. Messages echo only a validated profile identifier or surface name. Locations name keys, which the packet permits.
- **Version 1.** It is rejected at `$.schema_version` before any row is read (L84–88).
- **Core imports.** Only `dataclasses`, `enum` and `typing`. Posture is PASS.
- **PEC's row matches ruled question 2 ("migrated").**
  - `shared-dev-loop` v1 live cites D-PEC-94. That record's L24 adopts the shared method: work graphs, central receipts and MEMORY.
  - `loop-receipts-ledger` v1 historical cites `projects/pec/AGENTS.md`. Its L289–290 call `loop/LOOP_RECEIPTS.md` "a historical ledger, closed by Receipt 197".
  - `agentruns-json` v1 historical cites D-PEC-94 "by implication", exactly as the ruling states.
- **Test scope.** The tests assert only revision-1.5 SOW-077/094 behaviour, the surviving DEL-01-06 VER-001..006 clauses and packet items: the v2 `$id`, the closed vocabulary, the coherence rules, no echo, and v1 rejection.

## Findings

**N1 — NON-BLOCKING (record accuracy).**
- **Where:** `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-06_Loop_registry_local_config_default/_run_records/D-PEC-96_REGISTRY_V2/MANIFEST.md` line 6.
- **Defect:** it states "The act script ran at 01:37 MDT (`apply_d96_run_time.txt`)", but the cited file reads `Sat Sep 26 01:38:04 MDT 2026`. The act commit `c55362095` is at 01:38:11 and the post phase began at 01:38:21, so 01:38:04 is consistent with a timestamp taken at or just after the run.
- **Repair:** quote the file's value exactly (01:38:04 MDT) and say whether it marks the start or the end of the run, or drop the minute-level claim.

**N2 — NOTE (record format).**
- **Where:** the proposal's "Administrative grant" says the run root holds a `RUN.md`. The run root has none. `MANIFEST.md`, `VALIDATION.md` and `HANDOFF_STATE.md` carry that content instead, and the "Run-root contents" table in `MANIFEST.md` (lines 97–108) does not disclose the substitution.
- **Repair:** add one sentence to `MANIFEST.md` stating that these three files form the run record the grant calls `RUN.md`, or add a short `RUN.md` pointing to them. Both are inside the run-root `**` grant.

**N3 — NOTE (bound bytes; no repair possible in this act; carry with proposal finding 3).** The adapter is slightly stricter than the schema text in places, mostly inherited from version 1:
- JSON Schema 2020-12 `"type": "integer"` with `const 2` or `const 1` admits `2.0` or `1.0`, but the adapter rejects floats with `type(x) is not int` (`loop_registry.py` L84, L166; schema L49, L88).
- `loop_id` uniqueness (adapter L112–116) and `loop_init_path` normalization (L118–120, L204–210) are enforced but not stated in the schema (L65, L71). By contrast, `basis` normalization and profile uniqueness are stated.
- The unknown-field location echoes the offending key name (L218–223), which the packet allows as "Locations name keys, as before".

Each deviation is fail-closed. Suggested home: a later packet, or the S2 rebuild, together with path-normalization residual 5.

**N4 — NOTE (basis movement).** origin/main is now `53145aaeb` (PR #947, Root change workflow). It is disjoint from this candidate and the merge is clean. It adds `projects/pec/execution/_Coordination/NOTICE_2026-09-26_CHANGE_GENERIC.md`, which states that PEC defers action and records it for the record only. It does not change the ruling, the register, the hold register or any grant path. CI and review should cover the actual merge candidate as Root requires.

**N5 — NOTE (unverifiable).** The brief `G2_D96_REGISTRY_ACT.md` (`e9dadc1a…4594`, cited in `MANIFEST.md` L25) is outside the repository, so its hash could not be recomputed. The optional return file is not yet present, and `HANDOFF_STATE.md` L29 correctly describes it as the future home of the final state.

**N6 — NOTE (test thoroughness; bound bytes).** In `projects/pec/v2/tests/config/test_json_loop_registry.py`, L230 confirms the probes' removal only from `FEED_PROFILE_VERSIONS`, not from `FEED_PROFILE_SURFACES`. `mock.patch.dict` restores both, so this is not a defect. If the test is revised later, add `self.assertNotIn("probe-ledger", FEED_PROFILE_SURFACES)`.

No BLOCKING findings. The return is suitable for manager fan-in. Remaining risk:
- The inherited path-normalization residual.
- The SOW revision-1.4 wording lag until S2 lands.
- The stale "declares `remaining-loop` now" text carried to S2.

`HANDOFF_STATE.md` records all three accurately.

## Relevant paths

- `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-06_Loop_registry_local_config_default/_run_records/D-PEC-96_REGISTRY_V2/MANIFEST.md`
- `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-06_Loop_registry_local_config_default/_run_records/D-PEC-96_REGISTRY_V2/VALIDATION.md`
- `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-06_Loop_registry_local_config_default/_run_records/D-PEC-96_REGISTRY_V2/HANDOFF_STATE.md`
- `projects/pec/v2/src/pec_v2/adapters/config/loop_registry.py`
- `projects/pec/v2/config/loops.schema.json`
- `projects/pec/v2/tests/config/test_json_loop_registry.py`
- Throwaway evidence: `/private/tmp/claude-501/d96verify.TBKvuj/`, holding `repro_report.txt`, `out_head/`, `out_base/`, `grantcheck.py` and the three tars.

VERDICT: PASS WITH NOTES
