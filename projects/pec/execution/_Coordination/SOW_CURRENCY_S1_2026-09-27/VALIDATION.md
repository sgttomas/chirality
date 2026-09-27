# D-PEC-104 act — validation

Run root `projects/pec/execution/_Coordination/SOW_CURRENCY_S1_2026-09-27/`, branch
`claude/pec-d104-s1-sow-act`, base `origin/main` `16010b4ca9ab6c00247593177e1a8defa97a3ab6`
(PR #1005 merge, which carries the ruling), act commit `1e33df616`, verified candidate
`1cc8ce997`, later merge of `origin/main` `0adfbc747` (`8e09da59f`) with rechecks
(`d006036b9`). All commands ran from the repository root of the act worktree (the
reliance preflight from `projects/pec`), with `PYTHONDONTWRITEBYTECODE=1` exported and
Python 3.13.7 (CPython). Each output file starts with the command line (most with a
`date -u` header) and ends with `exit=<code>`. The row-2–13 commands are in
`evidence/post/verify_rows_2_13.zsh`; the post-merge commands in
`evidence/post_merge_0adfbc747/recheck.zsh`.

## Finite verification (proposal table)

| Row | Check | Command (abbreviated) | Result | Evidence |
|---|---|---|---|---|
| 1 | Preconditions | fetched `origin/main` = `16010b4ca`; ruling, proposal, register, prep `SHA256SUMS`, bound script hashes; register row; base drift since `b0a9a52b6` | ruling `bb88deb5…1bd`, proposal `35301840…6f51`, script `26b677a7…625f`; row `RULED A / PART B, SCOPE AND Q4 CONFIRMED / M / EFFECTIVE ON MERGE`; prep `SHA256SUMS` 158/158 OK; 553 paths changed `b0a9a52b6..16010b4ca` (Piping; in `projects/pec` only `docs/STATUS.md` and `_Coordination/**`: the S1 prep folder, the ruling, proposal and register, the graph and review transcriptions), none an S1 target or pin | `evidence/preconditions.out` |
| 1 | Run-root copy | `shasum -a 256 -c` of the 46 prep `SHA256SUMS` entries for the script, aids, candidates, quotes, claims | 46/46 OK | `evidence/runroot_copy.sha256`, `evidence/runroot_copy_check.out` |
| 1 | Reliance preflight, before dispatch (17:18:24Z, HEAD `16010b4ca`) | `pec_reliance_hold.py --operation dispatch-for-production` ×12 | `ALLOW`, exit 0 ×12 (register header-only, `f877d931…c741cbc`) | `evidence/reliance_dispatch.out` |
| 1 | `--check-only` (17:19:09Z) | `apply_s1p.py --repo <worktree> --candidates <run root>/candidates --check-only` | exit 0, `CHECK preflight passed`; all 12 preimages and 35 pins as tabled | `evidence/apply_check_only.out` |
| — | The act (17:19:45Z, HEAD `053ca4e22`) | same, without `--check-only`, once | exit 0, `CHECK targets 12/12 byte-exact; write set = grant (0 created, 12 modified, 0 removed under projects/pec outside the run root); pinned 35/35 unchanged` | `evidence/apply_run.out` |
| 1 | Reliance preflight, before fan-in of the act (17:19:59Z, before commit `1e33df616`, which contains its output) | `pec_reliance_hold.py --operation rely-for-production` ×12 | `ALLOW`, exit 0 ×12 | `evidence/reliance_rely.out` |
| 1 | Reliance preflight, before fan-in of the verdict (18:01:23Z) | `pec_reliance_hold.py --operation rely-for-production` ×12 | `ALLOW`, exit 0 ×12 | `evidence/reliance_rely_verdict.out` |
| 2 | Contract validity | `validate_scope_of_work.py <DEL folder>` ×12 | `PASS format=SOW_V1` ×12, exit 0 | `evidence/post/validate_<DEL>.out`, `evidence/post/validate_summary.out` |
| 3 | Checklist | `derive_review_checklist.py --output <run root>/checklist_<DEL>.json <DEL folder>`, twice | exit 0 ×24; reruns byte-identical; each equal to the prepared hash in the prep `SHA256SUMS` (`evidence/run_main/checklist_<DEL>.json`) | `checklist_<DEL>.json`, `evidence/post/checklist_*.out`, `evidence/post/checklist_compare.out` |
| 4 | Boundary owners (QA 21) | `check_boundary_owner_resolution.py --json <run root>/boundary_<DEL>.json --show-not-checkable <DEL folder>/ScopeOfWork.md` ×12 | exit 0 ×12; no `UNRESOLVED_OWNER` or `UNDEFINED_CLAIM`; `NOT_CHECKABLE` exactly the proposal's rows (DEL-01-03 REQ-006; DEL-02-01 REQ-002/003/005/012; DEL-02-02 REQ-005; DEL-03-01 REQ-007/009; DEL-03-03 REQ-015; DEL-04-05 REQ-003/005; the other six none); JSON identical to the prepared outputs; hand resolution by the verifier (verdict 01, QA 21 table; note N3) | `boundary_<DEL>.json`, `evidence/post/boundary_*.out`, `evidence/post/boundary_summary.out` |
| 5 | Quote fidelity | `verify_s1p_quotes.py --tree . --gitdir . --prep <run root> --observation 125cfacc1 --obs-exempt DEL-03-06` | `RESULT PASS 884/884`, exit 0 | `evidence/post/quotes.out` |
| 6 | State claims | `verify_s1p_state_claims.py --gitdir . --prep <run root>` | `RESULT PASS 905/905`, exit 0 | `evidence/post/state_claims.out` |
| 7 | Qualified IDs | `check_qualified_ids.py --prep <run root> --gitdir . --observation 125cfacc1` | `RESULT PASS 44/44`, exit 0 | `evidence/post/qualified_ids.out` |
| — | S4 overlay | S4 postimages in place on the basis; the rerun's overlay | DEL-04-01 `98a3a3ec…71a0`, DEL-04-03 `10819cb2…7e18`, neither in the branch diff; rerun summary: both `already-S4-postimage(no-op)` | `evidence/post/s4_postimages.out`, `evidence/rerun_16010b4ca/SUMMARY.out` |
| 8 | Dependency quote currency | `check_dep_quote_currency.py .`, before the act and after | `RESULT PASS 127/127` each; outputs identical | `evidence/dep_quote_currency_pre.out`, `evidence/post/dep_quote_currency_post.out`, `evidence/post/before_after_identity.out` |
| 9 | Lifecycle preserved | `git diff --name-status origin/main...HEAD -- '**/_STATUS.md' '**/_REVIEW.md' '**/Review_Findings.csv' '**/MEMORY.md'` | empty, exit 0 | `evidence/post/lifecycle.out` |
| 10 | Strict registers (D-GOV-48) | `validate_decomposition_registers.py --strict projects/pec/execution`, before and after | identical: exit 1, 0 errors, 26 `XRG-013` (owner-deferred under D-GOV-48) | `evidence/strict_pre.out`, `evidence/post/strict_post.out`, `evidence/post/before_after_identity.out` |
| 11 | Every-PR checks | `harness.py self-check`; `validate_pec_loop_receipts.py --repo-root .`, before and after | exit 0 each; identical before and after | `evidence/{harness,receipts}_pre.out`, `evidence/post/{harness,receipts}_post.out`, `evidence/post/before_after_identity.out` |
| — | Pins and second run | the script's `PINNED` and `TARGETS` hashed at HEAD; `apply_s1p.py --check-only` after the act | 35/35 pins OK, 12/12 postimages; second run refuses (`target does not hold its preimage`) ×12, exit 1 | `evidence/post/pins.out`, `evidence/post/rerun_refuses.out` |
| — | DEL-01-03 / DEL-01-05 REQ/AC/VER lines (manager aid) | definition lines `- **REQ-/AC-/VER-nnn**` at `origin/main` and HEAD | DEL-01-03 29/29, DEL-01-05 32/32, byte-identical in order (the verifier also compared whole blocks) | `evidence/post/req_ac_ver_identity.out` |
| — | DEL-03-06 correction-only (manager aid) | `git diff -U0 origin/main...HEAD -- <DEL-03-06 SOW> \| grep '^@@'` | hunks only at L220, L222–225, L229, L476 | `evidence/post/del_03_06_hunks.out` |
| 12 | Containment | `git diff --name-status origin/main...HEAD` | the twelve `M` contracts, the brief copy and run-root files only (recorded at HEAD `1e33df616`; rechecked at `0adfbc747` after the merge and at the records commit, see the return) | `evidence/post/containment.out`, `evidence/post_merge_0adfbc747/containment_summary.out` |
| 13 | Whitespace | `git diff --check origin/main...HEAD` | clean, exit 0 | `evidence/post/whitespace.out`, `evidence/post_merge_0adfbc747/whitespace.out` |

"Closure" in the brief's list: the proposal's table names no separate closure command.
It is read as the before/after identity of rows 10–11 (the strict validator, whose
families are `SCH`, `EVQ`, `XRG` and `DRB`, and the harness self-check), all identical.

## Rerun method

- `run_s1p_checks.sh <worktree> 16010b4ca <run root> <run root>/evidence/rerun_16010b4ca`,
  `TMPDIR` under the session scratchpad: `OVERALL PASS` — S4 overlay no-op for both
  files; act check-only 0, apply 0, rerun refuses 1; containment 12 differing files,
  all `ScopeOfWork.md`; validate/checklist/boundary ×12; quotes 884/884; state claims
  905/905; qualified IDs 44/44; dependency quote currency 127/127 pre and post;
  informational quote audit `S2-STALE 2 NOTFOUND 0` (the two DEL-03-01 hits the
  proposal explains); strict, harness, receipts identical before and after (export root
  normalized); whitespace; fault injection 9/9.
- The same at `0adfbc747` (`evidence/rerun_0adfbc747/`): `OVERALL PASS`, and its
  `SUMMARY.out` is identical to the `16010b4ca` one apart from the basis line.
- `negative_controls.sh <worktree> 16010b4ca <run root>`: all nine controls caught,
  `RESULT PASS` (`evidence/negative_controls.out`).

## Independent verifier

`VERIFIER_VERDICT_01.md` (fresh read-only `pec-reviewer`, candidate `1cc8ce997`):
**PASS WITH NOTES**, 0 BLOCKING, 0 NON-BLOCKING, 9 NOTEs. Basis, byte identity, the
`MODE=VERIFY` subset (checks.md items 1, 3, 4, 8, 9, 13, 16, 18–21, including the QA 21
hand resolution), semantics (claims, quotations, scope, open items, kept and retired
IDs, the Part B landings byte-exact with gates binding, DEL-03-06 correction-only,
DEL-01-03 and DEL-01-05 REQ/AC/VER blocks byte-identical, DEL-04-05 on the landed S4
text, no Remaining surface, no CHECKING gate), containment and lifecycle all PASS, with
independent reruns matching the recorded evidence. Dispositions:

- **N1** ("(provisional `D-PEC-104`)" in eleven AX entries) and **N2** (process text
  "(manager repair after verdicts 02 and 03)" in DEL-04-05 AX-012): **recorded**. The
  postimages are owner-ruled fixed bytes; nothing is repaired here. Carried in
  `HANDOFF_STATE.md` as later currency items.
- **N3** (QA 21 strict reading: DEL-02-01 REQ-005 and DEL-02-02 REQ-005 unchanged and
  disclosed; the table's "CLM-019" for DEL-03-01 REQ-007's PKG-02 owner resolves through
  CLM-007): **recorded**; pre-existing, disclosed, not introduced by this act. Carried
  as a later currency item (bind the owners to cited claims).
- **N4** (DEL-04-05 matrix L334 gains `, AX-012` from currency edit C9 beside the Part B
  replacements): **recorded**; consistent with the proposal. No action.
- **N5** (the recorded check-only command line omits `PYTHONDONTWRITEBYTECODE=1`):
  **recorded**. The shell that ran it exported `PYTHONDONTWRITEBYTECODE=1` before the
  command (as every check shell did); the recorded line shows only the command. The
  verifier found no `__pycache__` or ignored file. The evidence file is not rewritten.
- **N6** (`evidence/post/containment.out` and `HEADER.out` captured at `1e33df616`):
  **acted on**. Containment was rechecked after the merge
  (`evidence/post_merge_0adfbc747/containment_summary.out`) and at the records commit
  (return).
- **N7** (QA 1 read as `SOW_V1` canonical format): **recorded**; no action.
- **N8** (disclosed consequences): **recorded**; they stand as the ruling and proposal
  record them and are carried in `HANDOFF_STATE.md`.
- **N9** (rely preflight and act commit share the second 17:19:59Z): **recorded**; the
  order is fixed by `reliance_rely.out` being inside commit `1e33df616`.

## Post-merge rechecks at `0adfbc747` (`evidence/post_merge_0adfbc747/`)

`origin/main` moved to `0adfbc747` (PR #1006: the `D-PEC-105` and `D-PEC-106` rulings,
their proposals, register rows, the graph, `docs/STATUS.md` and review transcriptions;
PR #1009: App). The branch merged it without a rebase (`8e09da59f`); none of the nine
`projects/pec` paths it brings is an S1 target, pin or quoted file, and the `D-PEC-104`
register row is unchanged. At HEAD `8e09da59f`:

| Check | Result |
|---|---|
| `apply_s1p.py --check-only` on HEAD | refuses, exit 1 (targets hold postimages; by design) |
| `apply_s1p.py --check-only` on a `git archive 0adfbc747` export | exit 0, `CHECK preflight passed`: preimages and the 35 pins unchanged on the new base |
| Quotes / state claims / qualified IDs | `RESULT PASS 884/884` / `905/905` / `44/44` |
| Pins / postimages | 35/35 / 12/12 |
| Strict, harness, receipts, dependency quote currency | identical to the pre-act baselines (strict exit 1, 0 errors, 26 `XRG-013`; 127/127) |
| Lifecycle | empty |
| Containment | 12 `M` contracts, the brief copy and run-root files |
| Whitespace | clean |
| `run_s1p_checks.sh` at `0adfbc747` | `OVERALL PASS` |

## Later-state rechecks

At the records commit the containment and whitespace rows are rerun against the
then-current merge base; results are in the return.
