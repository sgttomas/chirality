# D-PEC-105 act — manifest

Run root `projects/pec/execution/_Coordination/D1_PREMISE_AMEND_2026-09-27/`,
undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005`, work-graph node D1 (the act).
Act date 2026-09-27 (session and local date, MDT); the UTC timestamps in `evidence/`
read 2026-09-27T17:36Z onward.

## Actors and delegation

| Actor | Role | Mechanism | Model (host-reported) | Scope |
|---|---|---|---|---|
| Manager | WORKING_ITEMS (Type 1) under HELP_HUMAN. Owning discipline as the proposal records it: the bounded candidate edit and its deterministic checks from the 2026-08-09 route (the edit itself was made at preparation; this run only applies the bound bytes), and `Workflow: chirality-root:bundled:workflow:scope-of-work` `MODE=VERIFY` for the two contracts (run by the verifier) | Claude Code subagent (`pec-manager`) launched by HELP_HUMAN; own git worktree `.claude/worktrees/pec-d105-act` on branch `claude/pec-d105-d1-premise-act` from fresh `origin/main` `c5d852c4a` | `claude-opus-5-5` (high effort per the owner's "defaults"; instruction-asserted) | run root, act, verification, records, PR, return |
| Verifier | TASK (Type 2), fresh read-only `pec-reviewer`: basis, byte identity, `MODE=VERIFY` on both contracts, premise-only discipline on every hunk, readings 4(a) and 4(b), posture 3 and add-on P agreement, coherence, finite verification reproduced, containment, the manager's write-set decision | harness-native descendant (Agent tool, `subagent_type=pec-reviewer`, `model=opus`, `run_in_background=false`), agent id `a0ca92e7a661911d8` | `claude-opus-5-5` (host-reported by the verifier) | read-only; own `mktemp -d` under the session scratchpad (`d105ver.zpaexX`) with `TMPDIR` set to it, deleted at the end; returned the `VERIFIER_VERDICT_01.md` text, saved by the manager |

Enforcement limits: role identity and write boundaries are instruction-asserted; the
host enforces only its own permissions. The verifier read the manager's worktree in
place and reported no writes there and no git writes; containment was checked with
`git status` and `git diff`. The manager wrote run-root files with shell commands
inside its own worktree (the host's file-write tool refuses paths in another worktree
than the session's, so files drafted in the session scratchpad were copied in by shell).

## Instruction and authority sources relied on (origin, SHA-256)

| Source | SHA-256 |
|---|---|
| Brief `D1A.md` (HELP_HUMAN session scratchpad `acts2/`; copied unchanged to `AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/briefs/D1A_D105_PREMISE_ACT.md`) | `fbc69cee8a52530d8c8fbf33abf4a743d43eb83d7614974692cf3d8a097a3895` |
| Root `AGENTS.md` (`CLAUDE.md` imports it; `CLAUDE.md` `336cc4fb…ab49`) | `c8ce87ef342902cb081bc659b26fc9a4edda1b6dba513814e5cb1e14e0b1dffd` |
| `projects/pec/AGENTS.md` | `df9196d152a01afe59b388111ae0a14381b4ad74f280e95f9c44a1eaee925eb8` |
| `agents/AGENT_WORKING_ITEMS.md` | `9ae4bea25bd95750a6878a9d53fbbbd7cd058d72c652a36baf4aa90601799665` |
| `_DECISIONS/D-PEC-105_RULING_2026-09-27.md` | `401c2419ba26c8a43610d8416663e745a80d8061363d5abb73459dea931bd0ef` |
| `_DECISIONS/D-PEC-105_d1_premise_amendment_proposal_2026-09-26.md` (the specification) | `077610057791063e2308d932cf08a7ac44cd02793fe60925c744d969fd6ba89f` |
| `_DECISIONS/_REGISTER.md` at `c5d852c4a` (row `D-PEC-105` `RULED A + P / RR1 / 4a, 4b CONFIRMED / M / EFFECTIVE ON MERGE`) | `5b7657292facd19762bb64454ee379a5c3ab0511c60b7d489a5b11ca8daa3766` |
| Bound act script `PEC_D1_PREMISE_PREP_2026-09-26/apply_d1p.py` (and the run-root copy) | `952a7512fd74e1b77f2f6b948d3cf46c876448ee1dee5370759f627236399d4d` |
| Prep `SHA256SUMS` (102 entries, all OK, no prep file unlisted; source of the 28 copied files' hashes) | `4641f5916fa7b5a99ac1a66735cd9f640ddacc121ed2f0ddb90dd6c56ec61d6b` |
| `ACTIVE_RELIANCE_HOLDS.csv` / `execution/_Scripts/pec_reliance_hold.py` | `f877d9316c7da76218399838aa6b69f1bb51bbd3e59b5b1d19b31f69ad741cbc` / `b1712e4b6e9f1476c577afd9170a4dd078beaa95878fa5f3b6c46a17b548cd0e` |
| Precedent read (not relied on as authority): `SOW_CURRENCY_S4_2026-09-26/` records (`MANIFEST.md`, `VALIDATION.md`, `HANDOFF_STATE.md`, evidence layout), `returns/REVIEW_PR998_0{1,2}.md` | at `c5d852c4a` |

## Method files

Workflow `chirality-root:bundled:workflow:scope-of-work`, resolved from
`workflows/index.json` (`2bfa2c5faae1081c55ce95fd3d81c00b1d87ba1f51d0bc13e03c8fcb6ccdafb3`);
no project (`.chirality/workflows`) or user (`~/.chirality/workflows`) workflow of
that name exists. `MODE=REVISE` is not used (the owner has deferred adopting it in
PEC; ruling Limits). At `c5d852c4a`:

| File | SHA-256 | Use |
|---|---|---|
| `workflows/scope-of-work/WORKFLOW.md` | `84dadde4c573b1d3d9ecd65e1e1be12efee1a95299b4115806c02e9c9cdebc2b` | loaded by the manager and the verifier |
| `workflows/scope-of-work/resources/checks.md` | `44ab41ace2fb14549ef0268c357ced42e798d97b01a325d62a60226767adf188` | loaded by the verifier (`MODE=VERIFY` subset) |
| `workflows/scope-of-work/resources/tools.md` | `fbd07771140f6350e964445014ba4f8f79f5d1f5c86df3379607b0489e6e5cc7` | loaded by the verifier; hashed by the manager |
| `workflows/scope-of-work/execution.json` | `4ad8b7eb42dba41f1609e6b3c61f14baa15ad82a1342f4ad12a095c4a570a26d` | hashed only |
| `workflows/scope-of-work/resources/brief.md` | `1696cd9a0c13aeda4151ebdd666fff7d0450450c88ea1aa00f7435fdcbf492bc` | hashed only |
| `workflows/scope-of-work/resources/representation-migration.md` | `698957a5005bc0078322c2bd6f12d73ab20f130999b060fe149aa7d4cb33e3c3` | hashed only (conversion) |
| `docs/DELIVERABLE_SCOPE_OF_WORK_STANDARD.md` | `26c8254aaf2e2894e7d32096ec1e0d71b3ad881c1445094945031be19741433c` | §7 read by the verifier; hashed by the manager |
| `workflows/review/WORKFLOW.md` | `99eae11d69671c283828818d4cb10c865d1f0a7af568ba267c54cee303e907ab` | hashed only (no REVIEW act; the revised edition is not adopted) |

The verifier also recorded `agents/AGENT_TASK.md` `1a13a5b0…c8fb7`, and a wider
consultation of Root `docs/CONTRACT.md` `510f6a84…3f71` (K-RUNTIME-1) and
`docs/DIRECTIVE.md` `b191750c…7fbf` (§7) for check 6.

The manager authored no product content. Tools (equal to the proposal's pins):
`validate_scope_of_work.py` `f0f10590…fecfe`, `derive_review_checklist.py`
`bfb64dc9…0109`, `check_boundary_owner_resolution.py` `22ef57e0…ae16a`, `common.py`
`61a34722…0389`, `id_catalog.json` `7a1f8a12…757`;
`tools/validation/validate_decomposition_registers.py` `300a321f…ee20`.
Interpreter: Python 3.13.7 (CPython), `PYTHONDONTWRITEBYTECODE=1` throughout.

## Write-set decision (brief Act step 1)

`apply_d1p.py` inventories every file under `projects/pec` before and after the write
and leaves out its own directory (`SELF_DIR = Path(__file__).resolve().parent`, pruned
from `os.walk`); its placement guard accepts an in-tree script directory only if it
begins `projects/pec/execution/_Coordination/D1_PREMISE_AMEND_`. The run-root copy was
run from the repository root, so the run root is excluded, and **output was written
beside the script in the run root** (`evidence/apply_run.out`, created by the shell
redirect before the script started). Nothing else under `projects/pec` was written
during the run. The verifier confirmed the decision is consistent with the script and
the proposal (verdict 01, item 9).

## Commits (branch `claude/pec-d105-d1-premise-act`, base `c5d852c4a`)

| Commit | Content |
|---|---|
| `8043bb1e5` | run root, bound script copy and aids, preconditions, dispatch preflight, pre-act baselines, `--check-only`, brief copy |
| `7c250e370` | the act (four replacements), rely preflight |
| `c58a6b535` | verification rows 2–12, runner rerun on `c5d852c4a` exports, negative controls (the verified candidate) |
| `bc974d340` | `VERIFIER_VERDICT_01.md`, rely preflight before fan-in of the verdict |
| `8d85a9b6e` | no-rebase merge of `origin/main` `0adfbc747` (PR #1009; `projects/chirality-app-dev/**` only, 312 paths) |
| `6718b29f9` | post-merge rechecks at `0adfbc747` |

Then the run-root records and the return. PR #1007.

## Product writes (the act)

| Path (under `projects/pec/execution/PKG-00_Architecture_Runway_Contracts/1_Working/`) | Preimage | Postimage |
|---|---|---|
| `DEL-00-03_v2_SPEC_seed/artifacts/v2/SPEC.md` | `cc9f4754…1bae` | `f84c067bf8388cbd348541dd821af040cee4e84fb34fe4e3e3ab473acdd5f617` |
| `DEL-00-03_v2_SPEC_seed/ScopeOfWork.md` | `3e4f0efc…5741` | `0fed4ecb771ccef8f8575dd08420e13792629cd7ac9d14f720423eba6c2ae843` |
| `DEL-00-01_v2_first_ADRs_core_isolation_carried_postures/artifacts/v2/ADRs.md` | `f63ecc27…5db5` | `ad6bab7ee00779e0cff5900d74d986e5e05c66b7dc469f5ddd9b224ecc65c49e` |
| `DEL-00-01_v2_first_ADRs_core_isolation_carried_postures/ScopeOfWork.md` (add-on P) | `43346150…1740` | `3757632b507d1f5a5668ccefb99d87b9e2a30a9e6bd38d7349e9f4721c5da647` |

No `_STATUS.md`, `_REVIEW.md`, `Review_Findings.csv`, `REV_*`, `MEMORY.md`, register,
dependency, context, reference, decomposition, `v2/**`, PRD or `docs/**` file is
written. Add-on M waits for closeout node M1.

## Run-root contents

- Copied from the prep folder, byte-identical (28 files; `evidence/runroot_copy.sha256`,
  `evidence/runroot_copy_check.out`): `apply_d1p.py`, `apply_d1p.template.py`,
  `build_apply_d1p.py`, `render_candidates.py`, `verify_d1p_quotes.py`,
  `verify_d1p_state_claims.py`, `check_quote_currency.py`, `scan_external_quotes.py`,
  `test_apply_d1p.py`, `run_d1p_checks.sh`, `negative_controls.sh`, `targets.json`,
  `candidates/…` ×4, `premise/DEL-*.json` ×4, `quotes/DEL-*.json` ×4,
  `claims/DEL-*.json` ×4. Not copied: `DRAFTER_BRIEF.md`, `VERIFIER_BRIEF.md`, the
  prep verdicts, the draft proposal and the prep `evidence/` (they stay in the prep
  folder).
- Outputs: `checklist_<KEY>.json` ×2 and `boundary_<KEY>.json` ×2 (proposal rows 4–5);
  `evidence/` (preconditions, reliance preflights, baselines, check-only, act, `post/`
  for rows 2–12, `rerun_c5d852c4a/` and `rerun_0adfbc747/` for the rerun method with
  their consoles, `negative_controls/` with its console, `post_merge_0adfbc747/`).
- **Scan rendering (verdict 01 NB-1).** In both rerun folders,
  `scan_external_quotes.out` is not the runner's raw output: the manager replaced it by
  its `--no-kept` rendering, as the prep evidence did. The raw file (SHA-256
  `38095b883af8238b8aa2b55606215166bec1b7e923958efd2cca48d9c637bf29`, 48,144 lines, the
  same at `c5d852c4a` and at `0adfbc747`) was filtered with
  `grep -vE '^(HISTORY-)?KEPT '`, leaving 2,343 lines (SHA-256
  `0710d29345a313ca682ce0487040f6a1b48e50f05586406d7dc8690ae6b44d68`), including the
  unchanged `SUMMARY` line with every count. That filter equals what
  `scan_external_quotes.py --no-kept` prints (script L104–110 skip only KEPT-class rows,
  which include `HISTORY-KEPT`); the verifier reproduced both and found them byte-equal.
  To regenerate the raw file: `run_d1p_checks.sh <REPO_ROOT> <commit> <run root> <out>`,
  or `scan_external_quotes.py --tree <pre-act export> --prep <run root>`.
- Records: `MANIFEST.md`, `VALIDATION.md`, `HANDOFF_STATE.md`, `VERIFIER_VERDICT_01.md`
  (`7cebb458ce89b226d9b2b30f71413785596f912bdb9245fd0d397085de40fb9a`; the verifier's
  `SubagentHandback` text as the host subagent transcript stores it, SHA-256
  `d9b295c2c191590829d14ee174b46b49a53d3fc8ac995bf8cfb19ab8ba183ee3`, plus one final
  newline; no other change).
- `SHA256SUMS`: every run-root file except itself.

## Scratch and footprint

Scratch lived under the session scratchpad (`d1a.4VVrfj/`: the environment helper,
the rerun consoles before copying, the extracted verdict text, the drafted records,
the PR body and `tmp/` as `TMPDIR` for the check aids, which delete their own `mktemp`
directories; one `git archive` export of `0adfbc747` for the post-merge
`--check-only`, deleted after use). Nothing was written to `/tmp` or `/var/folders`.
No repository file outside the brief's write boundary was written.
