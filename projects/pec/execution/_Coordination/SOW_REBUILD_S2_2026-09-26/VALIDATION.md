# D-PEC-100 act — validation

Run root `projects/pec/execution/_Coordination/SOW_REBUILD_S2_2026-09-26/`, branch
`claude/pec-d100-act`, base `origin/main` `bdae9d66b8e564844830af0d49f51b6b4a1db8ce`
(PR #971 merge), act commit `23e065e4f`. All commands ran from the repository root
of the act worktree (the reliance preflight from `projects/pec`), with
`PYTHONDONTWRITEBYTECODE=1` and Python 3.13.7 (CPython), on 2026-09-26. Each
output file starts with the command line and ends with `exit=<code>`.

## Finite verification (proposal table)

| Row | Check | Command (abbreviated) | Result | Evidence |
|---|---|---|---|---|
| 1 | Preconditions | fetched `origin/main` = `bdae9d66b`; ruling / proposal / bound script hashes; register row | ruling `13690e20…729b`, proposal `39c4331e…e25b`, script (prep and run root) `42dc9553…3d20`; row `RULED A / B CONFIRMED / M / EFFECTIVE ON MERGE` | `evidence/preconditions.out` |
| 1 | Run-root copy | `shasum -a 256 -c` of the 28 prep `SHA256SUMS` entries for the script, aids, candidates, quotes, claims | 28/28 OK | `evidence/runroot_copy.sha256`, `evidence/runroot_copy_check.out` |
| 1 | Reliance preflight (before the act) | `pec_reliance_hold.py --operation dispatch-for-production` ×7 | `ALLOW`, exit 0 ×7 (register header-only, `f877d931…c741cbc`) | `evidence/reliance_dispatch.out` |
| 1 | `--check-only` | `apply_s2p.py --repo <worktree> --candidates <run root>/candidates --check-only` | exit 0, `CHECK preflight passed` | `evidence/apply_check_only.out` |
| — | The act | same, without `--check-only`, once | exit 0, `CHECK targets 7/7 byte-exact; write set = grant (0 created, 7 modified, 0 removed under projects/pec outside the run root); pinned 23/23 unchanged` | `evidence/apply_run.out` |
| 1 | Reliance preflight (before fan-in, before the act commit) | `pec_reliance_hold.py --operation rely-for-production` ×7 | `ALLOW`, exit 0 ×7 | `evidence/reliance_rely.out` |
| 2 | Contract validity | `validate_scope_of_work.py <DEL folder>` ×7 | `PASS format=SOW_V1` ×7, exit 0 | `evidence/post/validate_<DEL>.out` |
| 3 | Checklist | `derive_review_checklist.py --output <run root>/checklist_<DEL>.json <DEL folder>`, twice | exit 0 ×14; reruns byte-identical; each equal to the prepared checklist hash | `checklist_<DEL>.json`, `evidence/post/checklist_*.out`, `evidence/post/checklist_compare.out` |
| 4 | Boundary owners (QA 21) | `check_boundary_owner_resolution.py --json <run root>/boundary_<DEL>.json --show-not-checkable <DEL folder>/ScopeOfWork.md` ×7 | exit 0 ×7; no `UNRESOLVED_OWNER` or `UNDEFINED_CLAIM`; `NOT_CHECKABLE` exactly DEL-01-01 REQ-003/004/005/007/015/016, DEL-02-06 REQ-004/006/009/010, DEL-02-07 REQ-004/006, as tabled; JSON identical to the prepared outputs; hand resolution by the verifier (verdict 01) with a mechanical aid `qa21_hand_resolution.py` (RESULT PASS 13/13 owner tokens) | `boundary_<DEL>.json`, `evidence/post/boundary_*.out`, `evidence/post/boundary_summary.out`, `evidence/post/qa21_hand_resolution.out` |
| 5 | Quote fidelity | `verify_s2p_quotes.py --tree . --gitdir . --prep <run root> --observation aca930622` | `RESULT PASS 460/460`, exit 0 | `evidence/post/quotes.out` |
| 6 | State claims | `verify_s2p_state_claims.py --gitdir . --prep <run root>` | `RESULT PASS 1280/1280`, exit 0 | `evidence/post/state_claims.out` |
| 7 | Sibling IDs | `check_sibling_ids.py <run root>` | `RESULT PASS 92/92`, exit 0 | `evidence/post/sibling_ids.out` |
| 8 | Lifecycle preserved | `git diff --name-status origin/main...HEAD -- '**/_STATUS.md'` | empty, exit 0 | `evidence/post/lifecycle.out` |
| 9 | Strict registers (D-GOV-48) | `validate_decomposition_registers.py --strict projects/pec/execution`, before the act and after | byte-identical: exit 1, 0 errors, 28 warnings (26 `XRG-013`, 2 `DRB-008`) | `evidence/strict_pre.out`, `evidence/post/strict_post.out`, `evidence/post/before_after_identity.out` |
| 10 | Every-PR checks | `harness.py self-check`; `validate_pec_loop_receipts.py --repo-root .`, before and after | exit 0 each; byte-identical before and after | `evidence/{harness,receipts}_pre.out`, `evidence/post/{harness,receipts}_post.out`, `evidence/post/before_after_identity.out` |
| 11 | Containment | `git diff --name-status origin/main...HEAD` | at `23e065e4f`/`eea486f48`: the seven `M` contracts, the brief copy and run-root files only; rechecked at the records commit (below) | `evidence/post/containment.out` |
| 12 | Whitespace | `git diff --check origin/main...HEAD` | clean, exit 0 (see the `.gitattributes` disclosure) | `evidence/post/whitespace.out` |

Informational: `scan_external_quotes.py --tree .` on the post-act tree reports
`SUMMARY stale=0 kept=49` because the tree no longer holds the prior S2 text; the
proposal's consequence scan reads the pre-act tree, and the export rerun below
reproduces its `SUMMARY stale=31 kept=32` (`evidence/post/scan_external_quotes.out`,
`evidence/rerun_bdae9d66b/scan_external_quotes.out`).

## Rerun method

`run_s2p_checks.sh <worktree> bdae9d66b <run root> <scratch out>` on two `git archive`
exports of `bdae9d66b` (scratch, deleted afterwards): `OVERALL PASS` — act check-only 0,
apply 0, rerun refuses 1; containment 7 differing files, all `ScopeOfWork.md`;
validate/checklist/boundary ×7; quotes 460/460; state claims 1280/1280; sibling IDs
92/92; strict, harness, receipts identical before/after (export root normalized);
whitespace; fault injection 9/9. Outputs: `evidence/rerun_bdae9d66b/` (`SUMMARY.out`).

## Independent verifier

`VERIFIER_VERDICT_01.md` (fresh read-only `pec-reviewer`, candidate `eea486f48`):
**PASS WITH NOTES**, no blocking finding. Dispositions:

- **N1** (project-content, non-blocking): DEL-02-07 `ScopeOfWork.md` L120 (`CLM-011`)
  says a fifth file named `adapter.yaml` is a preimage copy under a Root `AgentRuns`
  folder; at `aca930622` there is also a sixth,
  `execution/_Coordination/AgentRuns/ROOT_RUNTIME_MIGRATION_GATE5_2026-09-06/INTEGRATION/CONFIG_CANDIDATES/adapter.yaml`
  (confirmed by the manager with `git ls-tree -r --name-only aca930622`). The sentence is
  observation only and no rule derives from it. The owner-ruled bytes are **not**
  re-pinned (no re-pin is pre-authorized). Carried as a currency note for the next
  DEL-02-07 revision (S1, S4 or a later packet) in `HANDOFF_STATE.md`.
- **N2** (execution-substrate): `.gitattributes` sets `evidence/** -whitespace`, so row 12
  does not examine captured command output. Reason: evidence files are verbatim tool
  output; one line in `evidence/preconditions.out` (the register-row cell extracted
  with `awk`) carries a leading and trailing space. No other added file has trailing
  whitespace (verifier). `projects/pec/AGENTS.md` makes cosmetic whitespace a non-gate.
  The attribute is listed in `MANIFEST.md`.
- **N3**: `MANIFEST.md`, `VALIDATION.md` and `HANDOFF_STATE.md` added in the records
  commit, inside the run root; the return is at the brief's return path.
- **N4**: the ignored `__pycache__/apply_s2p.cpython-313.pyc` in the run root came from
  the manager's `importlib` listing of the script's `TARGETS` during the dispatch
  preflight, which ran without `PYTHONDONTWRITEBYTECODE=1`. It was never committed
  (`.gitignore` `**/__pycache__/`), the act's inventory excludes the run root, and it
  was deleted after the verdict.

## Later-state rechecks

At the records commit the containment and whitespace rows are rerun against the
then-current merge base; results are in `HANDOFF_STATE.md` and the return. Records
added after `eea486f48` are confined to the run root and the return path.
