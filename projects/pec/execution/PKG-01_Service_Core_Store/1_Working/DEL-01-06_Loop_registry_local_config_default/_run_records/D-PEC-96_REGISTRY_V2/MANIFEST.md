# D-PEC-96 A — Loop-Registry Schema v2 Act Manifest

**Status:** EXECUTED / VALIDATED by the manager. Independent verification is recorded in `VERIFIER_VERDICT_NN.md`; see `HANDOFF_STATE.md`.
**Owning instrument:** `D-PEC-96` option A (revision 4), as the owner's ruling of 2026-09-26 resolves its six questions.
**Executor:** WORKING_ITEMS (Type 1), graph node G1 (the act) of HELP_HUMAN undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`.
**Act date:** 2026-09-26. The act script started at 01:38:04 MDT. `apply_d96_run_time.txt` records that value; `date` wrote it immediately before the script, in the same command line. (Verdict 01 N1 corrected an earlier "01:37".) `/etc/localtime` is America/Edmonton and `TZ` is unset. The product bytes carry no date.
**Branch:** `claude/pec-d96-registry-act`
**Branch basis:** `origin/main` `f90320c1d110cad75d04c96c91a595b7eb244498` (PR #946 merge)
**Act commit (product writes):** `c55362095a5b56e61bb57c588e741513324ea52c`. The run root and preflight were committed at `d7c43074199b20e83dc03e6690460aff14323fc4`, the verification outputs at `590066fddbd9c38e818e0eb32db477fe092c7429`, and `MEMORY.md` at `dd63560a76d6e581c6c2a316e2c5a13e61079c5e`.

This package is derivative run evidence. It cites the ruling and the proposal
and does not replace them. It opens no lifecycle state and carries no
acceptance.

## Authority

| Instrument | SHA-256 |
|---|---|
| `_Coordination/_DECISIONS/D-PEC-96_RULING_2026-09-26.md`. Owner: "D-PEC-96: A; migrated; confirm; reject v1; create MEMORY; defaults" | `852057f0ff6989e0b1180232424ff9fd8de434b3345c1d6c775e76b8defb399e` |
| `_Coordination/_DECISIONS/D-PEC-96_registry_schema_v2_feed_profiles_proposal_2026-09-25.md`, revision 4 (the specification) | `4506597b1bfd6cafd8fc561c688bcb9e803d9c2b04c3abdec9dc05edf155180e` |
| `_Coordination/_DECISIONS/_REGISTER.md` row D-PEC-96 (`RULED A / EFFECTIVE ON MERGE`), observed on fetched `origin/main` `f90320c1d` | file `01b8d184e231dfe7bde5f7c78e169c1e913e53bb04ea413109159ae2816c1a14` |
| `apply_d96.py` (this run root; `cmp`-identical to `_Coordination/PEC_REGISTRY_D96_PREP_2026-09-25/apply_d96.py`) | `80725b4ff0180e858e6a0ecf0cf50fc8bcf19d861fcf53278f115567e6d6bbf3` |
| `mutate_d96.py` (this run root; `cmp`-identical to the preparation copy) | `57c2f03107aec5056f03847c43b9443a6986fbfd522017971c3cab72c3c826f0` |
| `docs/templates/MEMORY_TEMPLATE.md` | `5a9564f4663b000cdf0175bf4f0262001001bc50c719912499df2527d01c6a5a` |
| Brief `G2_D96_REGISTRY_ACT.md` (HELP_HUMAN session scratchpad, not in the repository), verified before work began | `e9dadc1a5a783d5a87597dc98659d6e1ca495a14d5071363d13e66e828594541` |

## Binding command (run once, from the repository root)

```text
PYTHONDONTWRITEBYTECODE=1 python3 projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-06_Loop_registry_local_config_default/_run_records/D-PEC-96_REGISTRY_V2/apply_d96.py --repo <REPO_ROOT>
```

`<REPO_ROOT>` was passed as the literal absolute worktree path. It is equal to
the output of `git rev-parse --show-toplevel`, which the proposal's command
substitutes. The host's worktree-isolation guard refuses a command
substitution inside a Python command line. The interpreter was
`/Library/Frameworks/Python.framework/Versions/3.13/bin/python3` (CPython
3.13.7).

- A `--check-only` run came first (`apply_d96_check_only.out`). It exited 0,
  with 6 UNCHANGED, 11 READ and 11 RENDER lines and `OK option=A files=11
  mode=check-only`. It writes nothing.
- The act run exited 0 with empty stderr (`apply_d96_stderr.txt`). Its report
  (`apply_d96_report.txt`) has 6 UNCHANGED, 11 READ (10 preimages and 1
  absent), 11 WRITE and `OK option=A files=11 mode=written`.
- The script ran once. It was not rerun after writing.

## Exact live-effect manifest (11 product paths: 10 MODIFY, 1 CREATE)

The paths are relative to `projects/pec/`. Every preimage equals the grant
table, and the script's READ lines prove it. Every postimage equals the grant
table and the preparation copy under
`PEC_REGISTRY_D96_PREP_2026-09-25/postimages/optionA_v2/`
(`checks/byte_identity.out`).

| # | Path | Act | Preimage SHA-256 | Postimage SHA-256 |
|---|---|---|---|---|
| 1 | `v2/config/loops.json` | modify | `4ce07ad061abd222acabb2afe0f619fdc840b4cc11d31e49f1dff8fcc299d32e` | `fd342b4f29edf3bece24a8d785b4a03d1a60158e62227753e4e1fa03529f53d7` |
| 2 | `v2/config/loops.schema.json` | modify | `1f4d1f0cf9abe5754ebb4260f588dea0d71e7f3cc37af2487b30b9c4aa39ba9b` | `104ed64820b7a1fa6f24249cb6817653b8a624f43c52ea181ae4fd5d510cb143` |
| 3 | `v2/src/pec_v2/core/ports/loop_registry.py` | modify | `3d5862bef122af27d61883fe5542b80daefb3418bccfba31486e4d60289b3662` | `a509bfb74920172a86ac21aff6a67245cd3248c5d73ef4e7427966069099c8a9` |
| 4 | `v2/src/pec_v2/core/ports/__init__.py` | modify | `669e1569216722509dcea0ae5ed42dc4a0ca856a196676568ee78d7a38a1edeb` | `e44bf7f00c8ef2cfa5f8006ef2834feb020063df63a3b4b8d8cbd8f359174ff7` |
| 5 | `v2/src/pec_v2/core/__init__.py` | modify | `33c54e244e8e19b66cb2c53c81fa747979f6d512f227f7a56e3f8d57cfb9ff4a` | `0e699a54d6bc202ff7a90c25fdb355da5ed2db185709c3a399870c1b0309c42d` |
| 6 | `v2/src/pec_v2/adapters/config/loop_registry.py` | modify | `7101740dea837e6077e048ec2a8ef8600c7d1014bd339915aaea285b8236eb2f` | `620a173d19d881ef396ebb339e4097f5ee4e3a0b6ada231718ca700926832f07` |
| 7 | `v2/tests/config/test_json_loop_registry.py` | modify | `d7efb486287d3703aa9ea007eb5376eba95689286bb322c887eeca8b193ac956` | `8b45495fdc78eb77c12a4ebefdb064d34d40d5602fde573be4b4e817ddbe0c9b` |
| 8 | `v2/tests/config/test_loop_registry_contract.py` | modify | `49b2f6a3b5088bceb82dc393cce050b8800af3a5ac5d34b3b6a3d7b71c01111b` | `b05ed8719c59258998b1c483456b66bd8d4a4d3bc4f68cdd6fb5c02541db7106` |
| 9 | `v2/tests/config/fixtures/duplicate_loop_id.json` | modify | `2e65c719af6c9eb7e170fb25d437b928847dc8d617c056093de213673b3e3396` | `6875f50023f1ad34a45c1af4b0a65316260c45aa05562ce45bb2d9bd8fd13c7e` |
| 10 | `v2/tests/config/fixtures/missing_loop_id.json` | modify | `2155849d9419f0239dca7a69d919ca9ee46a6434106d5326d85bc8c70afc5257` | `f4255b2483a014b542fb7f25c4314ff75dabb5cebbcfe751a2ad3df425f29598` |
| 11 | `v2/tests/config/fixtures/schema_version_1.json` | create | absent | `4ce07ad061abd222acabb2afe0f619fdc840b4cc11d31e49f1dff8fcc299d32e` |

The path-list SHA-256 is `b5db12e59bec0188b1798e8ccf7a3c09300c44e5dbcdf31c16a64aff5e84c73c`, equal to the grant.

**Must-remain files, unchanged:** `v2/tests/config/fixtures/malformed.json`
`f3730349…25b0`, `v2/src/pec_v2/adapters/config/__init__.py` `7a9bdbc5…3cba`,
`v2/src/pec_v2/adapters/__init__.py` `8c80e607…ef22`,
`v2/src/pec_v2/__init__.py` `ae46d431…7c1e`, `software-workflow.json`
`8ec9ba6d…a58b` and `v2/config/service_core_posture.json` `20d64ff3…09ed`.
The script checked them before writing, and they were rehashed afterwards.

**PEC's registry row, as ruled (question 2, "migrated"):**

| Profile | Version | State | Basis |
|---|---|---|---|
| `shared-dev-loop` | 1 | live | `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-94_owner_direction_loop_migration_2026-09-25.md` |
| `loop-receipts-ledger` | 1 | historical | `projects/pec/AGENTS.md` |
| `agentruns-json` | 1 | historical | `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-94_owner_direction_loop_migration_2026-09-25.md` |

`schema_version` is 2. The file has one row, `pec` → `projects/pec/loop/LOOP_INIT.md`. All three basis paths and
the `loop_init_path` exist (`checks/basis_citations.out`).

## Administrative writes

| Path (relative to `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-06_Loop_registry_local_config_default/`) | Act | SHA-256 |
|---|---|---|
| `MEMORY.md` | create, from the template, substituting only `{{DEL-ID}}` → `DEL-01-06`; empty Runs table (the undertaking's closeout writes the run row) | `035ecb8686d72b18eb680531e1239ab4b2df4f5ae1b70811f6e4d667ccf30a3f` |
| `_run_records/D-PEC-96_REGISTRY_V2/**` | create (this run root) | per file in Git |

## Run-root contents

| File | Purpose |
|---|---|
| `apply_d96.py`, `mutate_d96.py` | the bound scripts, exact bytes |
| `apply_d96_check_only.out`, `apply_d96_report.txt`, `apply_d96_stderr.txt`, `apply_d96_run_time.txt` | act script outputs |
| `run_checks.sh` | manager-written, read-only: the five registered checks (through `run_registered_checks.py`) plus verbose registry tests, enforcement tests, harness self-check, receipts validator and strict register validator, for one phase (`pre` or `post`) |
| `post_checks.sh` | manager-written, read-only: selection, mutation evidence, byte identity, basis citations, non-ASCII and vocabulary scans |
| `containment.py` | manager-written, read-only: classifies `git diff --name-status origin/main...HEAD` against the write boundary |
| `checks/` | every output, and `checks/COMMANDS.txt` (each command, cwd and exit code, in order) |
| `MANIFEST.md`, `VALIDATION.md`, `HANDOFF_STATE.md` | this record. Together they form the run record that the proposal's administrative grant calls `RUN.md`. The brief asked for this three-file form, after the D-PEC-95 precedent, so no separate `RUN.md` exists (verdict 01 N2) |
| `VERIFIER_VERDICT_NN.md` | independent verifier verdicts |

The earlier `_run_records/*` files (D-PEC-75, D-PEC-77, TASK_RUN_*) are unchanged.
