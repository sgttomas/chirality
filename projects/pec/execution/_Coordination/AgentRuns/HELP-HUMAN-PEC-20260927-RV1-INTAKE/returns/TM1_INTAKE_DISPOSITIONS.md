# Return — TM1: intake dispositions, K3 row and Root notice

- **Node:** TM1 of `HELP-HUMAN-PEC-20260927-RV1-INTAKE`. **Role:** WORKING_ITEMS (Type 1), a `pec-manager` instance on `claude-opus-5-5`. **Parent:** HELP_HUMAN.
- **Brief:** `../briefs/TM1_INTAKE_DISPOSITIONS.md`, SHA-256 `5b451dd5d643211e34625fc8bcd5728c357825ed2182f8ae236c8d1927ebebf8`. The copy is byte-identical to the source the parent supplied.
- **Method:** `chirality-root:bundled:workflow:task-management`, applying the owner's dispositions (row maintenance after a bounded intake).
- **Basis:** `origin/main` `acc7d3cc7` (the PR #1018 merge, `D-PEC-107`), fetched 2026-09-27.
- **Worktree and branch:** own worktree `.claude/worktrees/pec-tm1`, branch `claude/pec-tm1-intake-dispositions`.
- **PR:** https://github.com/sgttomas/chirality/pull/1021. Not merged, as the brief requires.

## Sources relied on (SHA-256 at `acc7d3cc7`)

| Source | SHA-256 |
|---|---|
| Root `AGENTS.md` | `c8ce87ef342902cb081bc659b26fc9a4edda1b6dba513814e5cb1e14e0b1dffd` |
| `projects/pec/AGENTS.md` | `df9196d152a01afe59b388111ae0a14381b4ad74f280e95f9c44a1eaee925eb8` |
| `agents/AGENT_WORKING_ITEMS.md` | `9ae4bea25bd95750a6878a9d53fbbbd7cd058d72c652a36baf4aa90601799665` |
| `workflows/task-management/WORKFLOW.md` | `d5e8eff5742326330c0f933dc322e07fbe6a2bb82ad151aadf803b001a02e654` |
| `workflows/task-management/execution.json` | `d1c668ae85f9f5a0edf2ecb312a449e21aa9101f99da9997fc4a7805677074df` |
| `workflows/task-management/resources/contract.md` | `3162f7ed386bcac08c0e16c0feae3b7a7a5109ba4bf4f845acc66bd2d6dfd04e` |
| `workflows/task-management/resources/method.md` | `d52403c983c92b1c65fe2b621d8c6bdc5c10e1fdb8c9ac99e95614137639c61e` |
| `D-PEC-107` record | `403a0497ae65c413f844b656daf6b3f5a58f99ffd65012dfd42b078430def346` |
| Intake `INTAKE.md` (preimage) | `e2ccf3e33b6636c46afe3fe68eff586f22141b405364bcb6b6eeefd63077818a` |
| This undertaking's `WORK_GRAPH.md` | `2b54e3bf70ca2a7a213de0c95798df41f6a243317ad8ef0353a84624c5557289` |
| `tools/taskmgmt/taskmgmt.py` | `9c5cdc562053b2cc2eeb6674b750d95cb7fa47971eb07acee010a404c221d101` |
| `execution/_Scripts/pec_reliance_hold.py` | `b1712e4b6e9f1476c577afd9170a4dd078beaa95878fa5f3b6c46a17b548cd0e` |
| `ACTIVE_RELIANCE_HOLDS.csv` | `f877d9316c7da76218399838aa6b69f1bb51bbd3e59b5b1d19b31f69ad741cbc` |

The sources cited in the rows and the notice, with their hashes, are listed in the row `SourceRef`/`SourceSha` cells and in the notice.

For precedent and form I also consulted: Piping `TM-PIP-030` (`OPEN` with `ElevatedTo` Root, as its owner ruled; corrected by HELP_HUMAN after PR #1021 review 01, which found the original parenthetical mis-cited it), `plans/chirality-task-management/PRD_CANDIDATE_2026-07-31.md` §6.2–6.3, and the earlier PEC harvest outcome sections. None of these is authority here.

## Written

| Item | Result |
|---|---|
| CAND-PEC-2026-09-27-01 | Disposition (b) recorded in `INTAKE.md` "Owner disposition". Not promoted, and no row per item. The item list stays the reference. |
| CAND-PEC-2026-09-27-02 | **`TM-PEC-026`**, `OPEN`. Its resolution is the next PEC scope change plus an instruction-tranche item for the `AGENTS.md` sentence. It carries the per-project consumer-contract design consideration and is marked as a consideration under the freeze point. |
| CAND-PEC-2026-09-27-03 | **`TM-PEC-027`**, `ELEVATED`, `ElevatedTo` `Root`, with `NoticeRef` pointing to the Root notice. The ELEVATED reading is mine and is disclosed in the row. |
| K3 | **`TM-PEC-028`**, `DEFERRED`. Its trigger is a DEL-08-06 production packet that fixes the tool's exact shape (TBD-003/004/006). It carries TBD-007 and CON-002, cites §B6, and includes the PR #994 review 02 wording notes. Its provenance is HELP_HUMAN's interpretation under `D-PEC-107`, which departs from the intake's "already homed" judgment. It is marked as a consideration under the freeze point. The DEFERRED mapping is mine and is disclosed. |
| DEL-01-06 `D-PEC-96` MEMORY row | Kept. The intake Outcome carries a one-line note. |
| Root notice | `execution/_Coordination/NOTICE_2026-09-27_PEC_HOSTED_CI_V2_CHECKS.md`, SHA-256 `62f20ec8fad12d93990df82f522d8515bac139621b977e5886f9beac1b4f4a58`. |
| Federation record | `_TaskManagement/TM_PEC_CLOSEOUT_POST_SCA005_2026-09-27/DISPOSITION_FEDERATION_2026-09-27.md`, SHA-256 `f84379dee684aed20e59b334f87f6090b03bee100f27de9093181f648f12a078`. |

Final hashes:
- `REGISTER.csv`: `5141b554c60c7ab4ae0adc939285223bd2a1a2e9eb992e8e9ac699ff2ec77e92` (was `634641f0…376a`).
- `REGISTER_CLOSED.csv`: unchanged, `3c1349ba…c1cf`.
- `INTAKE.md`: `0c455b9768f4f31a2d089d68159368d127054b41f775c048ccd3098baf345bf0`.

## Checks

All checks ran from the worktree root with CPython 3.13.7 and `PYTHONDONTWRITEBYTECODE=1`, with `TMPDIR` set to a directory under the session scratchpad.

- `python3 tools/taskmgmt/taskmgmt.py validate --register projects/pec/execution/_Coordination/_TaskManagement/REGISTER.csv`: exit 0, PASS, 12 rows. The same command on `REGISTER_CLOSED.csv`: exit 0, PASS, 16 rows.
- The following three commands gave output byte-identical (`cmp`) to the `origin/main` baseline. The baseline was taken on the clean tree before any write.

  | Command | Exit at baseline and after |
  |---|---|
  | `python3 tools/validation/validate_decomposition_registers.py --strict projects/pec/execution` | 1 (0 errors, 26 warnings) |
  | `python3 tools/practitioner_harness/harness.py self-check` | 0 |
  | `python3 tools/validation/validate_pec_loop_receipts.py --repo-root .` | 0 |

- Federation ran before and after the register write, with output to a Git-ignored path. Both runs: COMPLETE, 28 findings, none involving PEC, 0 register writes.
- Reliance-hold preflight: ALLOW for `promote` and `candidate-validation` on `REGISTER.csv` and `INTAKE.md`.
- Hosted CI on `7f97b3dc9`: the required jobs had passed when this return was written (pec, Harness pre-merge, Desktop E2E, selections), except `harness`, which was still running. The first head `3c2b7a8c0` passed every job, including `harness`.

## Verification

A fresh read-only `pec-reviewer` (opus, agent `a75330645dd973510`) reviewed the work. It ran in a private scratch directory and did no fetch or checkout.

- **Review 01 on `3c2b7a8c0`: PASS WITH NOTES.** It reported 0 blocking findings, 2 non-blocking findings and 6 notes. Repairs in `7f97b3dc9`:
  - F1: the notice now names `core`, `server` and `agent-sidecar` as the `npm test` workspaces; `web` is not one of them.
  - F2: the intake column heading and the CAND-02/03 cells now disclose which parts are interpretation.
  - F3: the intake header is in the past tense.
  - F4: the intake now says "only Task Management record".
  - F6: the K3 DEFERRED mapping is disclosed.
  - F7: the federation record names `federation_post.json` and gives the rerun hash.
  - F5 and F8 needed no repair. F5 found `ELEVATED` defensible and disclosed.
- **Backcheck on `7f97b3dc9`: PASS.** All repairs verified. No new findings.

## For the caller to resolve

- Integrate and merge PR #1021 under the standing Git authorization once `harness` completes. The graph's TM1 row, the central receipt link and any STATUS change are HELP_HUMAN's; this node wrote none of them.
- `TM-PEC-027` is elevated without a Root row. If Root opens one, a later PEC row-maintenance act may cite it. No Root row ID was invented.
- Both status mappings are mine and are disclosed: `ELEVATED` for "promote to Root" and `DEFERRED` for K3's trigger. The owner may redirect either one (to `OPEN`, for example) by row maintenance.
- Nothing prompts about CHECKING. No product, lifecycle, source, release or reliance state changed.
