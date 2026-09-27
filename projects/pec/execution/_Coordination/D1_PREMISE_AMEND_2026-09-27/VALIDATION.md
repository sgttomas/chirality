# D-PEC-105 act — validation

Run root `projects/pec/execution/_Coordination/D1_PREMISE_AMEND_2026-09-27/`, branch
`claude/pec-d105-d1-premise-act`, base `origin/main` `c5d852c4a95a478f34d9e4e4375d603e08245e25`
(PR #1006 merge, which carries the ruling and the register row), act commit
`7c250e370`, verified candidate `c58a6b535`. All commands ran from the repository root
of the act worktree (the reliance preflight from `projects/pec`), with
`PYTHONDONTWRITEBYTECODE=1`, `TMPDIR` in the session scratchpad outside the
repository, and Python 3.13.7 (CPython). Each output file starts with a `date -u` /
HEAD header and the command line and ends with `exit=<code>`. The row-2–12 commands
are in `evidence/post/verify_rows_2_12.zsh`.

## Finite verification (proposal table, checks 1–12)

| Row | Check | Command (abbreviated) | Result | Evidence |
|---|---|---|---|---|
| 1 | Preconditions | fetched `origin/main` = `c5d852c4a`; ruling, proposal, register, prep `SHA256SUMS`, bound script hashes; register row | ruling `401c2419…0bd0ef`, proposal `07761005…ba89f`, script `952a7512…9d4d`; row `RULED A + P / RR1 / 4a, 4b CONFIRMED / M / EFFECTIVE ON MERGE`; prep `SHA256SUMS` 102/102 OK, no prep file unlisted | `evidence/preconditions.out` |
| 1 | Run-root copy | `shasum -a 256 -c` of the 28 prep `SHA256SUMS` entries for the script, aids, candidates, ledgers, quotes, claims and `targets.json` | 28/28 OK | `evidence/runroot_copy.sha256`, `evidence/runroot_copy_check.out` |
| 1 | Reliance preflight, before dispatch (17:36:57Z) | `pec_reliance_hold.py --operation dispatch-for-production` ×4 | `ALLOW`, exit 0 ×4 (register header-only, `f877d931…c741cbc`) | `evidence/reliance_dispatch.out` |
| 1 | `--check-only` (17:37:42Z) | `apply_d1p.py --repo <worktree> --candidates <run root>/candidates --with-addon-p --check-only` | exit 0, `CHECK preflight passed; mode A+P`; all 4 preimages and all 18 pins as tabled (including both deliverables' `_STATUS.md`, `_REVIEW.md` and `Review_Findings.csv`) | `evidence/apply_check_only.out` |
| — | The act (17:38:17Z) | same, without `--check-only`, once | exit 0, `CHECK mode A+P; targets 4/4 byte-exact; write set = grant (0 created, 4 modified, 0 removed under projects/pec outside the run root); held at preimage 0/0; pinned 18/18 unchanged` | `evidence/apply_run.out` |
| 1 | Reliance preflight, before fan-in of the act (17:38:29Z, before commit `7c250e370` at 17:38:30Z) | `pec_reliance_hold.py --operation rely-for-production` ×4 | `ALLOW`, exit 0 ×4 | `evidence/reliance_rely.out` |
| 1 | Reliance preflight, before fan-in of the verdict (18:03:31Z, before commit `bc974d340`) | `pec_reliance_hold.py --operation rely-for-production` ×4 | `ALLOW`, exit 0 ×4 | `evidence/reliance_rely_verdict.out` |
| 2 | Ledger rendering and byte identity | `render_candidates.py --gitdir . --prep <run root>`; each target compared with its run-root candidate and tabled postimage | `RESULT PASS fails=0`; 4/4 targets equal their candidates and postimages | `evidence/post/render_candidates.out`, `evidence/post/byte_identity.out` |
| 3 | Contract validity | `validate_scope_of_work.py <DEL folder>` for DEL-00-03 and DEL-00-01 | `PASS format=SOW_V1` ×2, exit 0 | `evidence/post/validate_<KEY>.out` |
| 4 | Checklist | `derive_review_checklist.py --output <run root>/checklist_<KEY>.json <DEL folder>`, twice | exit 0 ×4; reruns byte-identical; DEL-00-03 `a3bc80a0db9a1917aa54337f62cd2057ce154bdc792f3802d982012f667121b1`, DEL-00-01 `6e99f93c37c761b140c60d870ab0048bae814427d65143a60364f36896bb8cf9`, each equal to the prepared hash | `checklist_<KEY>.json`, `evidence/post/checklist_*.out`, `evidence/post/checklist_compare.out` |
| 5 | Boundary owners (QA 21) | `check_boundary_owner_resolution.py --json <run root>/boundary_<KEY>.json --show-not-checkable <DEL folder>/ScopeOfWork.md` ×2 | exit 0 ×2; no `UNRESOLVED_OWNER` or `UNDEFINED_CLAIM`; 0 `NOT_CHECKABLE`; JSON identical to the prepared outputs | `boundary_<KEY>.json`, `evidence/post/boundary_*.out`, `evidence/post/boundary_summary.out` |
| 6 | Quote fidelity | `verify_d1p_quotes.py --tree . --gitdir . --prep <run root> --observation 6c6cc1b00` | `RESULT PASS 74/74`, exit 0 | `evidence/post/quotes.out` |
| 7 | State claims | `verify_d1p_state_claims.py --gitdir . --prep <run root>` | `RESULT PASS 126/126`, exit 0 | `evidence/post/state_claims.out` |
| 8 | Lifecycle and review records preserved | `git diff --name-status origin/main...HEAD -- '**/_STATUS.md' '**/_REVIEW.md' '**/Review_Findings.csv' '**/MEMORY.md' '**/REV_*'` | empty, exit 0 | `evidence/post/lifecycle.out` |
| 9 | Registers and quote currency | `validate_decomposition_registers.py --strict projects/pec/execution`; `check_quote_currency.py --tree . --prep <run root>`; before the act and after | identical: strict exit 1, 0 errors, 26 `XRG-013` (owner-deferred under D-GOV-48); `SUMMARY active_execution_quotes_verbatim 127/127`; `TARGET-cited active rows: 0` | `evidence/strict_pre.out`, `evidence/quote_currency_pre.out`, `evidence/post/strict_post.out`, `evidence/post/quote_currency_post.out`, `evidence/post/before_after_identity.out` |
| 10 | Every-PR checks | `harness.py self-check`; `validate_pec_loop_receipts.py --repo-root .`, before and after | exit 0 each; identical before and after | `evidence/{harness,receipts}_pre.out`, `evidence/post/{harness,receipts}_post.out`, `evidence/post/before_after_identity.out` |
| — | Pins and second run | the script's `PINNED` hashed at HEAD; `apply_d1p.py --with-addon-p --check-only` after the act | 18/18 pins OK; second run refuses (`target does not hold its preimage (already applied or changed)` ×4), exit 1 | `evidence/post/pins.out`, `evidence/post/rerun_refuses.out` |
| 11 | Containment | `git diff --name-status origin/main...HEAD` | at `c58a6b535`: the four `M` targets, the brief copy and run-root files only; rechecked after the merge (below) and at the records commit (return) | `evidence/post/containment.out` |
| 12 | Whitespace | `git diff --check origin/main...HEAD`; the runner's evidence-whitespace row | clean, exit 0 (no `.gitattributes` exemption is used); runner: 0 files with trailing whitespace or a blank line at EOF | `evidence/post/whitespace.out`, `evidence/rerun_*/SUMMARY.out` |

Informational: `scan_external_quotes.py --tree . --no-kept` on the post-act tree
reports `stale=0 anchor=9`, because that tree already holds the postimages. The
export reruns read the pre-act tree and report `stale=99 anchor=2213 history-anchor=30`;
the preparation run at `f0a6159c9` reported `stale=82 anchor=2198`. The 17 added STALE
lines are all in records of this packet published since: 13 in the published
proposal, 3 in `returns/D1P_PREMISE_PROPOSAL.md` and 1 in `returns/REVIEW_PR997_01.md`
(history; the verifier confirmed none is lost and none is elsewhere).

## Rerun method

- `run_d1p_checks.sh {REPO_ROOT} c5d852c4a {RUN_ROOT} {RUN_ROOT}/evidence/rerun_c5d852c4a`,
  with `TMPDIR` outside the repository: `OVERALL PASS` — `apply_d1p.py` equals a fresh
  rendering at its basis `f0a6159c9`; ledger rendering; act modes A and AP (check-only 0,
  apply 0, rerun refuses 1; containment exactly 3 and 4 files); validate / checklist
  (rerun byte-identical) / boundary for both contracts; quotes 74/74; state claims
  126/126; strict, harness and receipts identical before and after in both modes
  (export root normalized); dependency quote currency 127/127 identical; candidate
  whitespace; fault injection 24/24; evidence whitespace 0.
- The same at `0adfbc747` (`evidence/rerun_0adfbc747/`): `OVERALL PASS`, and its
  `SUMMARY.out` is identical to the `c5d852c4a` one apart from the basis line; its
  scan rendering is byte-identical too.
- `negative_controls.sh {REPO_ROOT} c5d852c4a {RUN_ROOT} {RUN_ROOT}/evidence/negative_controls`:
  all six controls tripped after passing on undamaged copies,
  `RESULT PASS negative controls 6/6` (`evidence/negative_controls_console.out`).
- Rows 2–12 on the act tree: `evidence/post/verify_rows_2_12.zsh`. Its first line sets
  `W` to this act's worktree path, and several outputs record that absolute `--repo`
  path (verdict 01 Note 1). To rerun from another checkout, set `W` to that checkout's
  `{REPO_ROOT}` (`git rev-parse --show-toplevel`) on a commit that holds the
  postimages; `{RUN_ROOT}` is `{REPO_ROOT}/projects/pec/execution/_Coordination/D1_PREMISE_AMEND_2026-09-27`.
  `--check-only` passes only on a tree that holds the preimages (an export of the
  base); on the act tree it refuses by design.
- Scan outputs in both rerun folders are the `--no-kept` rendering of the runner's raw
  file (see `MANIFEST.md`, "Scan rendering"; verdict 01 NB-1).

## Independent verifier

`VERIFIER_VERDICT_01.md` (fresh read-only `pec-reviewer`, candidate `c58a6b535`):
**PASS WITH NOTES**, no blocking finding. Basis, byte identity (including an
independent renderer of the verifier's own), `MODE=VERIFY` on both contracts
(items 1, 3, 4, 8, 9, 13, 16, 18–21), premise-only discipline on every hunk (22, 15,
6 and 3), readings 4(a) and 4(b), posture 3 and add-on P agreement, coherence of the
amended SPEC with the amended DEL-00-03 contract, the reproduced finite verification,
containment and lifecycle, and the manager's write-set decision all PASS.
Dispositions:

- **NB-1** (the `--no-kept` scan replacement was not yet disclosed in a committed
  file): **repaired** in `MANIFEST.md` ("Scan rendering"), with the raw file's hash and
  line count, the filter, its equivalence to `--no-kept`, and the regeneration
  command; referenced above.
- **Note 1** (`verify_rows_2_12.zsh` hard-codes this worktree path; outputs record
  the absolute `--repo` path): **acted on** by stating the rerun method with
  `{REPO_ROOT}` above. The evidence files are not rewritten.
- **Note 2** (DEL-00-01 REQ-004 cites `D-GOV-43` A2 and reaches K-RUNTIME-1 through
  CLM-005): **recorded**; owner and elements are identical, not a defect; the bytes
  are owner-ruled.
- **Note 3** (AX-009 does not repeat the P02 SCA-004-era label, which lives in the
  ledger and the proposal): **recorded**; the contract bytes are ruled exact.
- **Note 4** (the uniform ADR note names SCA-005 and SCA-006 although every ADR hunk is
  an SCA-005 cause): **recorded**; by design and not false (proposal L110).

## Base drift and post-merge rechecks at `0adfbc747` (`evidence/post_merge_0adfbc747/`)

`origin/main` moved from `c5d852c4a` to `0adfbc747` (PR #1009) while the verifier
ran. It changed only `projects/chirality-app-dev/**` (312 paths): no target, pin,
quoted locus, `tools/`, `workflows/`, `agents/`, `docs/` or `projects/pec` path. The
manager merged it without a rebase (`8d85a9b6e`) and reran, at HEAD `8d85a9b6e`:

| Check | Result |
|---|---|
| `apply_d1p.py --with-addon-p --check-only` on a `git archive 0adfbc747 projects/pec` export | exit 0, `CHECK preflight passed`: the 4 preimages and 18 pins unchanged on the new base |
| `apply_d1p.py --with-addon-p --check-only` on HEAD | refuses, exit 1 (targets hold postimages; by design) |
| `run_d1p_checks.sh` on `0adfbc747` exports | `OVERALL PASS` (above) |
| Ledger rendering | `RESULT PASS fails=0` |
| Quotes | `RESULT PASS 74/74` |
| State claims | `RESULT PASS 126/126` |
| Pins / postimages | 18/18 / 4/4 |
| Strict, harness, receipts, quote currency | identical to the pre-act baselines (strict exit 1, 0 errors, 26 `XRG-013`; 127/127; target-cited rows 0) |
| Lifecycle | empty |
| Containment | four `M` targets, the brief copy and run-root files |
| Whitespace | clean |
| Merge paths | `git diff --name-only bc974d340 HEAD`: 312 paths, all `projects/chirality-app-dev/**` |

## Later-state rechecks

At the records commit the containment and whitespace rows are rerun against the
then-current merge base; results are in the return. Records added after `c58a6b535`
are confined to the run root and the brief's return path, apart from the merge of
`origin/main`; HELP_HUMAN's graph and STATUS records follow in their own commits.
