# Evidence — DEL-00-03 RV1 PEER_REVIEW

Reviewer `REVIEW-PEER-DEL-00-03-20260927-RV1`, 2026-09-27. Every numbered
file was written by `scripts/run.sh`, which records the working directory
(`{REPO_ROOT}`, branch `claude/pec-rv1-d1-review`, HEAD `a1735cc3b`), the
interpreter (`python3`, CPython 3.13.7), the environment
(`TMPDIR=<review scratch dir>`, `PYTHONDONTWRITEBYTECODE=1`), the exact
command, its combined output (with the scratch directory rendered as
`$TMPDIR` and the checkout as `{REPO_ROOT}`) and its exit code. All outputs
went to the review scratch directory; nothing was written into the
repository by these commands. Rerun method: `scripts/run.sh <name> '<command>'`
from any checkout at `a1735cc3b`, with `TMPDIR` outside the repository.

| File | What it shows |
|---|---|
| `01_instruction_and_method_hashes.txt` | Instruction sources, authority records, briefs, intake, preflight output, routed checklist; the four `review` files at `2f825f180` (all match). Its last two lines are a wrong path for the parent brief, corrected in file 19 |
| `02_target_and_record_hashes.txt` | SPEC `f84c067b…`, SOW `0fed4ecb…` and the deliverable's companion files |
| `03_checklist_rederivation.txt` | Two derivations, byte-identical to each other and to the routed checklist `a3bc80a0…` |
| `04_prior_checklist_diff.txt` | Derivation from the prior SOW `3e4f0efc…` (`1c4d4927…`) and the full diff to the current checklist |
| `05_validate_scope_of_work.txt` | `PASS format=SOW_V1`, zero issues |
| `06_strict_registers.txt` | Strict register validation: 0 errors, 26 `XRG-013` warnings, exit 1 (the recorded baseline) |
| `07_basis_identity.txt` | Decomposition registers and PRD byte-identical at HEAD and `189f205ff`; front matter |
| `08_register_counts.txt` | 100 items (74/18/8); 68 rows, 4 retired; per-package ranges (`scripts/counts.py`) |
| `09_spec_token_resolution.txt` | PRD 49 requirements and 11 invariants; 225 SPEC identifiers, 0 unresolved; family-to-scope cross-check (`scripts/tokens.py`) |
| `10_open_issue_dispositions_r14_vs_r16.txt` | OPEN/RESOLVED status of OI-001..013 at revision 1.4 and 1.6, and the ledger status of their scope items. The "closes:" column came out blank (a column-index choice) and is not relied on |
| `11_open_issue_text_diff_r14_r16.txt` | Full text diff of `SOFTWARE_DECOMP.md` §10 between revisions 1.4 and 1.6 |
| `12_act_run_root_hashes.txt` | Hashes of the act's `HANDOFF_STATE.md`, `VALIDATION.md`, premise ledgers and candidates; run-root `SHA256SUMS` check |
| `13_premise_ledger_replay.txt` | The 22 SPEC and 15 SOW hunks replayed on the preimages at `7c250e370^` reproduce the current bytes (`scripts/hunks.py`) |
| `14_commit_resolution.txt` | Commit objects cited by the bytes; `3623b958b` does not resolve (RF-005) |
| `15_spec_greps.txt` | "package" uses, vocabulary tokens, retired families (none), TBD counts, trailing whitespace (none) |
| `16_act_change_set_and_paths.txt` | Act commit change set (four PKG-00 product paths); `docs/` listing; the SPEC path in the D-PEC-72 packet |
| `17_identity_check.txt` | Direct identity check (substitution for `audit-decomp`) |
| `18_prd_k_rows_v22_v24.txt` | Only PEC-K-03 changed from PRD v2.2 to v2.4; the seven v2.4 non-goals (RF-004) |
| `19_other_input_hashes.txt` | Parent brief, CU-001, holds register and preflight script, SCA plans, the D-PEC-72 packet, tools, precedent snapshots. One mistyped SCA-006 path fails there; the next line hashes the correct path |
| `20_worktree_state_and_boundary_incident.txt` | Worktree clean for tracked files; the one ignored bytecode cache described below |
| `21_root_spec_section_3_4.txt` | Root `docs/SPEC.md` hash and the §3.4 "no disclosed-deferral carve-outs" line |
| `checklist_DEL-00-03_rederived.json` | The re-derived checklist (`a3bc80a0…21b1`) |
| `checklist_DEL-00-03_prior_sow_3e4f0efc.json` | The checklist derived from the prior SOW (`1c4d4927…fbdb`) |
| `scripts/` | The wrapper and the three read-only helper scripts used above |

Reading-only commands that are not logged individually above (`cat`, `sed`,
`grep`, `git show`, `git log` of the named sources) informed the review; each
relied-on fact is reproduced by a numbered file.

## Boundary incident (disclosed)

Before the logged runs, one unlogged `python3 tools/scope_of_work/derive_review_checklist.py --help`
(and `validate_scope_of_work.py --help`) was run from `{REPO_ROOT}` without
`PYTHONDONTWRITEBYTECODE=1`. Python wrote the bytecode cache
`tools/scope_of_work/__pycache__/common.cpython-313.pyc` into the worktree
(created 2026-09-27 15:35:41 local). The path is Git-ignored
(`.gitignore:26:**/__pycache__/`); `git status --short` shows no tracked or
untracked change (file 20). It affects no reviewed byte or check. The
reviewer did not delete it, because the brief permits deletion only inside
the review scratch directory; the manager decides whether to remove it.
