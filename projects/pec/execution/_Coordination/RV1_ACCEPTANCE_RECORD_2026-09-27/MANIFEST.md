# RV1 acceptance record — run manifest (ACCCLOSE, 2026-09-27)

- **Undertaking and nodes:** `HELP-HUMAN-PEC-20260927-RV1-INTAKE`, ACC (recording the owner's act) and M1 (MEMORY rows).
- **Role:** WORKING_ITEMS (Type 1) manager, dispatched by HELP_HUMAN as a Claude Code subagent (`pec-manager`). The host reports the model as Opus 5.5 (`claude-opus-5-5`); role identity is instruction-asserted.
- **Branch and basis:** `claude/pec-rv1-intake-closeout`, cut from `origin/main` `31a90f3e6` (the PR #1023 merge, RV1 REVIEW) after one `git fetch origin`.
- **Brief:** `../AgentRuns/HELP-HUMAN-PEC-20260927-RV1-INTAKE/briefs/ACCCLOSE_ACCEPTANCE_AND_MEMORY.md`, SHA-256 `facf2974e882afca57e57e9441263f21fa7b77e77f5d507f1bf7cbbb936ec461` (copied byte-identical from HELP_HUMAN's scratchpad).
- **Mid-run clarification from HELP_HUMAN (it clarifies, not enlarges, the brief), summarized:** the owner made no severity call on DEL-00-01 RF-001, which stays MAJOR; its disposition is `ACCEPT_AS_IS`, AC-002 is accepted as partly met, and `ACCEPT_AS_IS` is not `DEFERRED`. The findings covered are DEL-00-01 RF-001..RF-005 and DEL-00-03 RF-004..RF-010. The optional successor custom item (to CU-001) and the optional C-05 line are left out, because the owner took neither. The ruling record's final name is `_DECISIONS/D-PEC-108_D1_REACCEPTANCE_2026-09-27.md`.

## Authority relied on

- The owner's ruling of 2026-09-27, verbatim as quoted in the brief: "ACC: option 1; accept all findings as is; re-accept DEL-00-01 and DEL-00-03 exact bytes; retire CU-001". The option-1 content (AC-007, contract, AC-011, findings, CU-001, scope) is HELP_HUMAN's presentation as the brief states it, and is labelled as such in each record. HELP_HUMAN writes the ruling record `_DECISIONS/D-PEC-108_D1_REACCEPTANCE_2026-09-27.md` in this PR after this manager hands back. This manager has not seen that record.
- The MEMORY grant: `_DECISIONS/D-PEC-107_MEMORY_GRANT_2026-09-27.md`, SHA-256 `89d5ce4aa32706412c415893d4cc0fecc0197db33698b2b23db713ab5abc5bc3` (supplementing `D-PEC-107_OWNER_DIRECTION_2026-09-27.md`, `403a0497ae65c413f844b656daf6b3f5a58f99ffd65012dfd42b078430def346`).

## Instruction and method sources loaded (SHA-256)

| Source | Origin | SHA-256 |
|---|---|---|
| Root `AGENTS.md` | worktree at `31a90f3e6` | `c8ce87ef342902cb081bc659b26fc9a4edda1b6dba513814e5cb1e14e0b1dffd` |
| `projects/pec/AGENTS.md` | worktree at `31a90f3e6` | `df9196d152a01afe59b388111ae0a14381b4ad74f280e95f9c44a1eaee925eb8` |
| `agents/AGENT_WORKING_ITEMS.md` | worktree at `31a90f3e6` | `9ae4bea25bd95750a6878a9d53fbbbd7cd058d72c652a36baf4aa90601799665` |
| `workflows/review/WORKFLOW.md` | `git show 2f825f180:` (the RV1 method basis) | `f8a8f240a034395dd1d069799449215eca29ce14887a20653f1cec9a674906bc` |
| `workflows/review/execution.json` | `git show 2f825f180:` | `d1c668ae85f9f5a0edf2ecb312a449e21aa9101f99da9997fc4a7805677074df` |
| `workflows/review/resources/contract.md` | `git show 2f825f180:` | `d3d7eb27993068fbdf4ea3b06c78a19106ff4d145f149d5cf50040756144b328` |
| `workflows/review/resources/method.md` | `git show 2f825f180:` | `63c8a3959cd6286f95acf30ae87e42a5dd99d951b2ae2ab3ec6212a81f930daa` |
| `tools/scaffolding/create_snapshot_folder.sh` (run twice) | worktree | `7db42ee6963dbe8306047dc5afbeb911be7fecdd92b05a239987be05c8d95640` |
| `tools/scaffolding/update_latest_pointer.sh` (read, not run) | worktree | `21899520ab84e0d88056b19a4318810cc3a730bc4b6d22e7ec66291549f015bc` |
| `execution/_Scripts/pec_reliance_hold.py` | worktree | `b1712e4b6e9f1476c577afd9170a4dd078beaa95878fa5f3b6c46a17b548cd0e` |
| `execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv` (header-only) | worktree | `f877d9316c7da76218399838aa6b69f1bb51bbd3e59b5b1d19b31f69ad741cbc` |

The working-tree `workflows/review/**` (revised edition) was not read or applied. The method's Gate 4 rule applied to the CSVs: "Update `Status` to `RESOLVED` if disposition is final" (`method.md` Gate 4 step 2). `update_latest_pointer.sh` was not run, because it would drop the narrative the 2026-08-09 precedent pointer carries; `_LATEST.md` was written by hand in the precedent's form.

## Precedent followed

The 2026-08-09 exact-byte acceptance: DEL-00-03 `_REVIEW.md` "Exact-byte acceptance and remaining gates" (commit `e92a82ca9`) and snapshot `_Evaluation/Reviews/REV_DEL-00-03_2026-08-09_2156/` (five files: `Brief.md`, `Decision_Log.md`, `QA_Report.md`, `RUN_SUMMARY.md`, `Review_Summary.md`), with `_LATEST.md` moved to it. As there, the review stage line was updated, the owner's ruling was quoted near the top, and a closing acceptance section was added. Differences: the RV1 body is otherwise kept verbatim, including its AC-002 (PARTIAL), AC-007/AC-011 and findings text as recorded at review time, and the new section states the current state; the prior stage line is quoted in that section.

## Written paths

- `…/DEL-00-01_v2_first_ADRs_core_isolation_carried_postures/_REVIEW.md`, `Review_Findings.csv`, `MEMORY.md`
- `…/DEL-00-03_v2_SPEC_seed/_REVIEW.md`, `Review_Findings.csv`, `MEMORY.md`
- `_Evaluation/Reviews/REV_DEL-00-01_2026-09-27_1655/` (five files), `_Evaluation/Reviews/REV_DEL-00-03_2026-09-27_1658/` (five files), `_Evaluation/Reviews/_LATEST.md` (now `REV_DEL-00-03_2026-09-27_1658`)
- this folder; the brief copy; the return `../AgentRuns/HELP-HUMAN-PEC-20260927-RV1-INTAKE/returns/ACCCLOSE_ACCEPTANCE_AND_MEMORY.md`

Nothing else: no `_DECISIONS/**`, graph, STATUS, README, receipt, `_STATUS.md`, `ScopeOfWork.md`, artifact or foreign file.

## Checks (commands, cwd, interpreter; outputs in `evidence/`)

Python 3.13.7, `PYTHONDONTWRITEBYTECODE=1`, `TMPDIR` under the session scratchpad.

| Check | Command (cwd) | origin/main `31a90f3e6` | Candidate | Comparison |
|---|---|---|---|---|
| Strict registers | `python3 tools/validation/validate_decomposition_registers.py --strict projects/pec/execution` (repo root) | exit 1; 0 errors, 26 warnings | exit 1; 0 errors, 26 warnings | byte-identical (`strict_*.out`) |
| Practitioner harness | `python3 tools/practitioner_harness/harness.py self-check` (repo root) | exit 0 | exit 0 | byte-identical (`harness_*.out`) |
| Loop receipts | `python3 tools/validation/validate_pec_loop_receipts.py --repo-root .` (repo root) | exit 0 | exit 0 | byte-identical (`receipts_*.out`) |
| Whitespace | `git diff --check` (with untracked files intent-added) | — | clean, exit 0 | — |
| Reliance-hold preflight | `python3 execution/_Scripts/pec_reliance_hold.py --register execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv --target <t> --operation <op>` (`projects/pec`) | — | 22 runs, all `ALLOW`, exit 0 | `reliance_hold_preflight.out` |
| Accepted hashes | `shasum -a 256` over the four accepted objects and both deliverables' `_STATUS.md` and `Dependencies.csv` | — | all reproduce; no diff against `origin/main` | `accepted_hashes.out` |

Preflight targets: `promote` on the ADRs, both contracts and the SPEC; `candidate-validation` and `promote` on each written review record, both MEMORY files, `_LATEST.md` and both snapshot folders. Disclosure of order: the four accepted hashes were reproduced before any write. The two `Review_Findings.csv` edits and the DEL-00-01 `_REVIEW.md` insertion were made in the working tree shortly before the first preflight batch ran, and the DEL-00-03 snapshot folder was preflighted after it was created, before its files were written. The register is header-only, so the order changed no outcome.

The bytes a check reads are the candidate's working tree before commit. Rerun: check out this PR's head and rerun the commands above, comparing against a checkout of `31a90f3e6`.

## Independent review

One fresh read-only `pec-reviewer` (opus) reviews the complete candidate diff; its verdict is recorded in the return.
