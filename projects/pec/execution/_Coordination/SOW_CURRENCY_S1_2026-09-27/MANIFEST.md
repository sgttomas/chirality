# D-PEC-104 act — manifest

Run root `projects/pec/execution/_Coordination/SOW_CURRENCY_S1_2026-09-27/`,
undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`, work-graph node S1 (the act).
Act date 2026-09-27 (session and local date, MDT); the UTC timestamps in `evidence/`
read 2026-09-27T17:17Z onward.

## Actors and delegation

| Actor | Role | Mechanism | Model (host-reported) | Scope |
|---|---|---|---|---|
| Manager | WORKING_ITEMS (Type 1) under HELP_HUMAN, `Workflow: chirality-root:bundled:workflow:scope-of-work` (authoring discipline already applied at preparation: `MODE=INIT`, `STATUS_POLICY=NO_STATUS_TOUCH`, `DECOMP_VARIANT=SOFTWARE`; independent `MODE=VERIFY` at the act) | Claude Code subagent launched by HELP_HUMAN; own git worktree `.claude/worktrees/pec-d104-act` on branch `claude/pec-d104-s1-sow-act`, cut from fresh `origin/main` `16010b4ca` | `claude-opus-5-5` (high effort per the owner's "defaults"; instruction-asserted) | run root, act, verification, records, PR, return |
| Verifier | TASK (Type 2), fresh read-only `pec-reviewer`, `MODE=VERIFY` plus basis, byte identity, Part B, DEL-03-06 correction-only, DEL-01-03/DEL-01-05 REQ/AC/VER identity, DEL-04-05 on the landed S4 text, containment | harness-native descendant (Agent tool, `subagent_type=pec-reviewer`, `model=opus`, `run_in_background=false`), agent id `ad6128330fe02ce7a` | `claude-opus-5-5` (host-reported by the verifier) | read-only; own `mktemp -d` under the session scratchpad (`s1av.H2v1zs`) with `TMPDIR` set to it; returned the `VERIFIER_VERDICT_01.md` text through SubagentHandback, saved byte for byte by the manager |

Enforcement limits: role identity and write boundaries are instruction-asserted; the
host enforces only its own permissions. The verifier read the manager's worktree in
place and reported no writes there; containment was checked with `git status` and
`git diff`. The host's file-writing tool refuses paths in another worktree than the
session's own, so the manager wrote every run-root file with shell commands inside its
own worktree (the verdict and these records were first written to the session
scratchpad `s1a/` and copied in).

## Instruction and authority sources relied on (origin, SHA-256)

| Source | SHA-256 |
|---|---|
| Brief `S1A.md` (HELP_HUMAN session scratchpad `acts2/`; copied unchanged to `AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/briefs/S1A_D104_SOW_ACT.md`) | `b60d21dba14d0a6805b74a611eab057d6318f952e31f8c934247b237d590296a` |
| Root `AGENTS.md` (`CLAUDE.md` imports it; `CLAUDE.md` `336cc4fb…ab49`) | `c8ce87ef342902cb081bc659b26fc9a4edda1b6dba513814e5cb1e14e0b1dffd` |
| `projects/pec/AGENTS.md` | `df9196d152a01afe59b388111ae0a14381b4ad74f280e95f9c44a1eaee925eb8` |
| `agents/AGENT_WORKING_ITEMS.md` | `9ae4bea25bd95750a6878a9d53fbbbd7cd058d72c652a36baf4aa90601799665` |
| `_DECISIONS/D-PEC-104_RULING_2026-09-27.md` | `bb88deb5a9850f2444b99740d5abcf9b127901c2f1e5185d4a75a2f1232ec1bd` |
| `_DECISIONS/D-PEC-104_s1_sow_currency_proposal_2026-09-26.md` (the specification) | `35301840d56f9972b0d7ca3c85dae0ee80ffdf5509c44586f219a47ff6545f51` |
| `_DECISIONS/_REGISTER.md` at `16010b4ca` (row `D-PEC-104` `RULED A / PART B, SCOPE AND Q4 CONFIRMED / M / EFFECTIVE ON MERGE`); at `0adfbc747` `5b765729…3766`, the row unchanged | `bf1366b22aa47b5f0cd56ffb54e3dd73937f6221f001a67e598f93ffaec10054` |
| Bound act script `PEC_SOW_CURRENCY_S1_PREP_2026-09-26/apply_s1p.py` (and the run-root copy) | `26b677a70d5d51041f0d49dd34e9a09685120f136071e906d7ff702719f1625f` |
| Prep `SHA256SUMS` (158 entries, all OK; source of the 46 copied files' hashes) | `029b5030200932b0ca26fe7ac7dbb964fe2b8359f214dcc8e4666a41f120f528` |
| `D-PEC-99_REMAINING_RETIREMENT_2026-09-26/EXHIBIT_MOVED_ITEMS.md` (pinned) | `69b646f8481fe39a12b811d8078ed14a4c49622d9a8ab566d87f83683044f45e` |
| `ACTIVE_RELIANCE_HOLDS.csv` / `execution/_Scripts/pec_reliance_hold.py` | `f877d9316c7da76218399838aa6b69f1bb51bbd3e59b5b1d19b31f69ad741cbc` / `b1712e4b6e9f1476c577afd9170a4dd078beaa95878fa5f3b6c46a17b548cd0e` |
| Precedent read (not relied on as authority): `SOW_CURRENCY_S4_2026-09-26/` records, `briefs/S4A_D102_SOW_ACT.md`, `returns/REVIEW_PR998_0{1,2}.md` | at `16010b4ca` |

`agents/AGENT_TASK.md` (`1a13a5b0…8fb7`) is the verifier's role file; the manager hashed
it and named it in the verifier's prompt but did not load it. No other role's
instructions were consulted.

## Method files

Workflow `chirality-root:bundled:workflow:scope-of-work`, resolved from
`workflows/index.json` (`2bfa2c5faae1081c55ce95fd3d81c00b1d87ba1f51d0bc13e03c8fcb6ccdafb3`);
no project (`.chirality/workflows`) or user (`~/.chirality/workflows`) workflow of
that name exists. At `16010b4ca`:

| File | SHA-256 | Use |
|---|---|---|
| `workflows/scope-of-work/WORKFLOW.md` | `84dadde4c573b1d3d9ecd65e1e1be12efee1a95299b4115806c02e9c9cdebc2b` | loaded by the manager and the verifier |
| `workflows/scope-of-work/resources/checks.md` | `44ab41ace2fb14549ef0268c357ced42e798d97b01a325d62a60226767adf188` | loaded by the verifier (`MODE=VERIFY` subset); the manager read its item list |
| `workflows/scope-of-work/execution.json` | `4ad8b7eb42dba41f1609e6b3c61f14baa15ad82a1342f4ad12a095c4a570a26d` | hashed and read |
| `workflows/scope-of-work/resources/brief.md` | `1696cd9a0c13aeda4151ebdd666fff7d0450450c88ea1aa00f7435fdcbf492bc` | hashed only |
| `workflows/scope-of-work/resources/tools.md` | `fbd07771140f6350e964445014ba4f8f79f5d1f5c86df3379607b0489e6e5cc7` | hashed only |
| `workflows/scope-of-work/resources/representation-migration.md` | `698957a5005bc0078322c2bd6f12d73ab20f130999b060fe149aa7d4cb33e3c3` | hashed only (conversion) |
| `docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md` | `26c8254aaf2e2894e7d32096ec1e0d71b3ad881c1445094945031be19741433c` | hashed only |

The manager did not re-author content. Tools (equal to the proposal's pins):
`validate_scope_of_work.py` `f0f10590…fecfe`, `derive_review_checklist.py`
`bfb64dc9…0109`, `check_boundary_owner_resolution.py` `22ef57e0…ae16a`, `common.py`
`61a34722…0389`, `id_catalog.json` `7a1f8a12…e757`;
`tools/validation/validate_decomposition_registers.py` `300a321f…ee20`,
`tools/practitioner_harness/harness.py` `01a9b954…61f3`,
`tools/validation/validate_pec_loop_receipts.py` `8eb62995…bad9`.
Interpreter: Python 3.13.7 (CPython), `PYTHONDONTWRITEBYTECODE=1` exported in every
shell that ran a check (see VALIDATION.md, verifier note N5).

## Write-set decision (brief Act step 1)

`apply_s1p.py` inventories every file under `projects/pec` before and after the write
and leaves out its own directory (`SELF_DIR = Path(__file__).resolve().parent`, pruned
from `os.walk`); its placement guard refuses a directory inside `projects/pec/` that
does not begin `projects/pec/execution/_Coordination/SOW_CURRENCY_S1_`. The run-root
copy was run, so the run root is excluded, and **output was written beside the script
in the run root** (`evidence/apply_run.out`, created by the shell redirect before the
script started; `evidence/` existed before the run). Nothing else under `projects/pec`
was written during the run. The verifier confirmed the decision against the script
(verdict 01, item 1).

## Commits (branch `claude/pec-d104-s1-sow-act`, base `16010b4ca`)

| Commit | Content |
|---|---|
| `053ca4e22` | run root, bound script copy and aids, preconditions, dispatch preflight, pre-act baselines, `--check-only`, brief copy |
| `1e33df616` | the act (twelve replacements), rely preflight |
| `1cc8ce997` | verification rows 2–13, rerun on `16010b4ca` exports, negative controls (the verified candidate) |
| `0b5bcc050` | `VERIFIER_VERDICT_01.md`, rely preflight before fan-in of the verdict |
| `8e09da59f` | no-rebase merge of `origin/main` `0adfbc747` (PR #1006: the `D-PEC-105` and `D-PEC-106` rulings, proposals, register rows, graph, STATUS and review transcriptions; PR #1009: App; no S1 target, pin or quoted locus) |
| `d006036b9` | post-merge rechecks at `0adfbc747` |

Then the run-root records and the return.

## Product writes (the act)

| Path (under `projects/pec/execution/`) | Preimage | Postimage |
|---|---|---|
| `PKG-01_Service_Core_Store/1_Working/DEL-01-03_Store_bootstrap_content_minimal_guard/ScopeOfWork.md` | `986ef155…6341` | `65c7f4086f8a053c41219c4966dd062a3821d43927c24fffe29f4e9046d2a367` |
| `PKG-01_Service_Core_Store/1_Working/DEL-01-04_Self_observability_logging/ScopeOfWork.md` | `4dd777f8…7e62` | `16ac1cd956c90f0e757c9ce54c4e6645eea50e6d46d69b26f8052ad0484cca41` |
| `PKG-01_Service_Core_Store/1_Working/DEL-01-05_Zero_dependency_locality_enforcement/ScopeOfWork.md` | `53ba3be3…de53` | `347f73c7969cc777027110f101faec6ad40c728e17e095aa2270f268498798bb` |
| `PKG-02_File_Truth_Parsers/1_Working/DEL-02-01_STATUS_md_parser/ScopeOfWork.md` | `5d286ec9…4440` | `82caf28a3757089ec07cd9a21ef70f97840fda7b92f1017236ce5062fdf55872` |
| `PKG-02_File_Truth_Parsers/1_Working/DEL-02-02_Decision_register_packet_parser/ScopeOfWork.md` | `5f20b1c4…db6e` | `84e55e58e6632845f7462970180c052ebec5fc677072a4bd883f871a002ffa86` |
| `PKG-03_Reconciliation_Parity/1_Working/DEL-03-01_Full_rebuild_reconciler_one_command/ScopeOfWork.md` | `56495523…92d2` | `5b71d3583b2e661564acf889c0a0d6fef93ce24302f29845c3cda0a367ae8276` |
| `PKG-03_Reconciliation_Parity/1_Working/DEL-03-02_Incremental_reconcile_on_Git_delta/ScopeOfWork.md` | `d1335c01…85b5` | `d823d55d9e714ac3142c02ee5d599d7167e0836c89c1abee7c513b072073a3d0` |
| `PKG-03_Reconciliation_Parity/1_Working/DEL-03-03_Drift_classification/ScopeOfWork.md` | `5ce8ab72…eaa7` | `c2b88cb65c71bf017fc42c85e164470f0ea86696bd100ed0157d4c2a53f79526` |
| `PKG-03_Reconciliation_Parity/1_Working/DEL-03-06_Rebuild_performance_bounds/ScopeOfWork.md` | `90de9c2d…c97e` | `f9c3a057717292e7ccd6def6e0496f69ad6c5100457b15cd17b37477adff8bd4` |
| `PKG-04_Orientation_Services/1_Working/DEL-04-05_Measurement_limitation_honesty/ScopeOfWork.md` | `933c012c…a579` | `9c2ede6ceff643b09a380fcbecb649c953783ed25ca044f35bc6376fd49309db` |
| `PKG-10_Validation_Measurement/1_Working/DEL-10-02_Kill_test_standing_release_gate/ScopeOfWork.md` | `99730e4e…1a82` | `f5590cf55b19f3170cb04e65340e076e672d5d54d8f1e98385372d1dd8f3436e` |
| `PKG-10_Validation_Measurement/1_Working/DEL-10-10_Directed_bootstrap_self_ingest_validation/ScopeOfWork.md` | `640f2371…bd5e` | `813839a080d7e245a0174959bc4f67be265cfabfd5b2177f83cb6fdc934737c8` |

No `_STATUS.md`, `_REVIEW.md`, `Review_Findings.csv`, `MEMORY.md`, register,
dependency, context, reference, decomposition, `v2/**`, PRD or `docs/**` file is
written. Add-on M waits for closeout node M1.

## Run-root contents

- Copied from the prep folder, byte-identical (46 files; `evidence/runroot_copy.sha256`,
  `evidence/runroot_copy_check.out`): `apply_s1p.py`, `test_apply_s1p.py`,
  `verify_s1p_quotes.py`, `verify_s1p_state_claims.py`, `check_qualified_ids.py`,
  `check_dep_quote_currency.py`, `scan_s1_consequences.py`, `aids/audit_quotes.py`,
  `run_s1p_checks.sh`, `negative_controls.sh`, `candidates/…` ×12, `quotes/DEL-*.json`
  ×12, `claims/DEL-*.json` ×12.
- Outputs: `checklist_<DEL>.json` ×12 and `boundary_<DEL>.json` ×12 (proposal rows 3–4);
  `evidence/` (preconditions, reliance preflights, pre-act baselines, the act,
  `post/` for rows 2–13 with its script `post/verify_rows_2_13.zsh`,
  `rerun_16010b4ca/` and `rerun_0adfbc747/` for the rerun method with their consoles,
  `negative_controls.out`, `post_merge_0adfbc747/` with its script `recheck.zsh`).
- Records: `MANIFEST.md`, `VALIDATION.md`, `HANDOFF_STATE.md`, `VERIFIER_VERDICT_01.md`
  (`5dab70b3c7b1725127777b14dd7f37b320e3208ff91b47ce3f039ba1e6361c5f`; byte-identical
  to the `message` of the verifier's SubagentHandback call in the host subagent
  transcript, compared with `cmp`).
- `SHA256SUMS`: every run-root file except itself.

## Scratch and footprint

Scratch lived under the session scratchpad: `s1a/` (the verdict and record drafts, the
extracted handback text) and `s1a_hold.zsh` (the reliance-preflight wrapper), with
`TMPDIR` set to the scratchpad for every check aid; the aids delete their own `mktemp`
directories, and the recheck's `s1a_main_export.*` export was removed by its script.
Nothing was written to `/tmp` or `/var/folders`. No repository file outside the brief's
write boundary was written.

One slip, inside the run root: at 18:01:41Z, while checking whether `origin/main`
`0adfbc747` touched an S1 target or pin, the manager imported the run-root
`apply_s1p.py` in a shell without `PYTHONDONTWRITEBYTECODE=1`, which created
`__pycache__/apply_s1p.cpython-313.pyc` beside it. The file is Git-ignored and was never
committed; it appeared after the act and after the verifier's run, touched nothing the
act or its checks read, and was listed by mistake in the first run-root `SHA256SUMS`
(commit `463e298a8`). The manager removed the cache directory and regenerated
`SHA256SUMS` without it.
