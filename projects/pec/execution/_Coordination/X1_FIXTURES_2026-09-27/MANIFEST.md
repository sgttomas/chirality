# MANIFEST — D-PEC-106 X1 act (run root `X1_FIXTURES_2026-09-27`)

- **Undertaking:** `HELP-HUMAN-PEC-20260925-POST-SCA005`, work-graph node X1 (the act). Parent: HELP_HUMAN.
- **Role:** WORKING_ITEMS (Type 1). Verifier: one fresh read-only `pec-reviewer` TASK. Models as the host reports them: Opus 5.5 (`claude-opus-5-5`) for both; the `high` effort and the roles are instruction-asserted.
- **Act date `{D}`:** `2026-09-27` (UTC and local).
- **Branch / PR:** `claude/pec-d106-x1-fixtures-act`, PR #1008 against `main` (not merged by WORKING_ITEMS).
- **Base:** `origin/main` `c5d852c4a` at the act (contains the ruling, PR #1006); merged forward to `0adfbc747` without a rebase (merge `0040299f6`).

## Authority and instruction sources (actual origin, SHA-256)

| Source | Origin | SHA-256 |
|---|---|---|
| Brief X1A (copied unchanged to `AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/briefs/X1A_D106_FIXTURES_ACT.md`) | HELP_HUMAN scratch `acts2/X1A.md` | `8cde96bf5779e5339b2c05ac5728d39c5357ebcb5e914300bf0a781b765ab81a` |
| Ruling `_DECISIONS/D-PEC-106_RULING_2026-09-27.md` | `origin/main` `c5d852c4a` | `5161630bd14ce1aee6de89913145534e88a4546d487219aa490f9438880596fe` |
| Proposal `_DECISIONS/D-PEC-106_x1_parser_fixture_suites_proposal_2026-09-26.md` (the specification) | `origin/main` `c5d852c4a` | `677b59f6b1ae19b911e6e07aecfa4df0f39a380fb3ab806903da87c8fa18d279` |
| Register row `D-PEC-106` in `_DECISIONS/_REGISTER.md` | `origin/main` `c5d852c4a` | row reads `RULED A / FX-PEC-0 AND THRESHOLDS CONFIRMED / L / M / EFFECTIVE ON MERGE` |
| Root `AGENTS.md` | worktree at `c5d852c4a` | `c8ce87ef342902cb081bc659b26fc9a4edda1b6dba513814e5cb1e14e0b1dffd` |
| `projects/pec/AGENTS.md` | worktree at `c5d852c4a` | `df9196d152a01afe59b388111ae0a14381b4ad74f280e95f9c44a1eaee925eb8` |
| `agents/AGENT_WORKING_ITEMS.md` | worktree at `c5d852c4a` | `9ae4bea25bd95750a6878a9d53fbbbd7cd058d72c652a36baf4aa90601799665` |
| `.agents/skills/software-code-review/SKILL.md` (applied by the verifier; hashed, not loaded, by WORKING_ITEMS) | worktree | `ee085d589c44f912d11a59eead8edac214f0343761d26b0d33e886a979888bca` |
| `tools/scaffolding/write_status.sh` | worktree | `0bf835f54f4bb9a78a51d0b56392a8686d1f255f06d3c2bcaf7e8665f77bece3` |
| `execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv` / `execution/_Scripts/pec_reliance_hold.py` | worktree | `f877d931…1cbc` / `b1712e4b…cd0e` |
| Root `docs/SPEC.md` | worktree | `feb5e79c0b60b5156ea9ad2b00e32e338ab42c4351da0b0cbca6f30df5f3109e` |

Method: the proposal's generation method and finite verification, run as an ad hoc WORKING_ITEMS plan. No workflow body was loaded by WORKING_ITEMS; no other role's instructions were consulted.

## Bound files copied into this run root

Copied byte for byte from `../PEC_X1_FIXTURES_PREP_2026-09-26/` and checked against its `SHA256SUMS` (45/45 OK, `evidence/row0_bound_copy.out`):

- `apply_x1p.py` — `452ff66af71b7d3de9814301a8e45ca070137d5e577b4e73c202b713d2102428` (bound act script);
- `candidates/projects/pec/…` — the 35 postimages tabled in the proposal's grant;
- check aids (not bound): `test_apply_x1p.py`, `run_x1p_checks.sh`, `run_fixture_suite.sh`, `verify_x1p_bindings.py`, `report_x1p_pins.py`, `negative_controls_x1p.py`, `negative_controls_x1p.sh`, `build_apply_x1p.py`, `apply_x1p.template.py`.

`run_x1p_checks.sh` was run with the prep folder as its `<prep dir>`, because its draft-claims step reads the prep folder's `DRAFT_…`, `claims/` and `evidence/` files; the prep bytes equal the run-root copies.

## Records and evidence written here

- `MANIFEST.md`, `VALIDATION.md`, `HANDOFF_STATE.md`, `VERIFIER_VERDICT_01.md`, `VERIFIER_VERDICT_02.md`, `SHA256SUMS` (every other run-root file).
- `evidence/`: row 0–9 outputs (`row*.out`, `row3_registered.json`), `pre_act_checks_c5d852c4a/`, `rerun_after_merge_0adfbc747/`, `fanin_hold_rely_for_production.out`, and the small read-only aids written for this run (`deps_read.py`, `check_addon_L_slots.py`, `check_bytes_hygiene.py`, `rerun_after_merge_0adfbc747/act_pins_and_targets.py`), plus `hold_targets.txt` and `bound_copy.sums`.
- Two outputs were whitespace-normalized after their first commit; raw captures are at `2886540c0` (`evidence/row1_basis.out`) and `3f1e1a4d7` (`evidence/row1a_addon_L.out`). See `VALIDATION.md`.

## Product and lifecycle writes (outside this run root)

| Path | Change | Writer | SHA-256 after |
|---|---|---|---|
| `projects/pec/v2/tests/parsers/**` (34 files) | created | `apply_x1p.py` (one run, exit 0) | as tabled in the proposal (35/35 verified, `evidence/row2b_bytes_hygiene.out`) |
| `projects/pec/software-workflow.json` | `8ec9ba6d…8a8b` → | `apply_x1p.py` | `d55fff77a1d216a7b1ab78b16e3ff3f2747fb3b542a2b269367ec3afa83e0bbd` |
| DEL-02-03 `_STATUS.md` | `INITIALIZED` → `IN_PROGRESS` | add-on L `write_status.sh` | `84b238d263c6272f9e4845ad7c2804cf871bd417e40b161026e0fc91bf4c9b5e` |
| DEL-02-08 `_STATUS.md` | `INITIALIZED` → `IN_PROGRESS` | add-on L `write_status.sh` | `bfc995867fa2c87fb7c94acaf95c64fbc42aade174ac77c5c92ace14e3451ff6` |
| DEL-02-09 `_STATUS.md` | `INITIALIZED` → `IN_PROGRESS` | add-on L `write_status.sh` | `50bc10f4135b49e669921ee7d733b5e2bda0c4bcf541c7b2f8fb5ce8f034372a` |

## Commit sequence (act branch)

| Commit | Content |
|---|---|
| `2886540c0` | run root, bound copies, row-1 preflight evidence, brief copy |
| `3f1e1a4d7` | add-on L: the three `_STATUS.md` and their evidence (before the act) |
| `26b27b2b0` | the act: 34 creates, `software-workflow.json`, row-2 outputs |
| `7ff6eb7bb`, `f657822b2`, `f4ab6c307` | verification evidence; whitespace normalization; row-9 attempt |
| later commits | verdict 01 and dispositions, fan-in preflight, merge of `origin/main` `0adfbc747` (`0040299f6`), reruns, records, verdict 02, return |
