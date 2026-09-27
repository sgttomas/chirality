# D-PEC-102 act — validation

Run root `projects/pec/execution/_Coordination/SOW_CURRENCY_S4_2026-09-26/`, branch
`claude/pec-d102-s4-sow-act`, base `origin/main` `4c2a7768ff43ef2d3590a37a28e53c519de744d9`
(PR #994 merge, which carries the ruling), act commit `5d13cfdb8`, verified candidate
`a26ca1613`. All commands ran from the repository root of the act worktree (the
reliance preflight from `projects/pec`), with `PYTHONDONTWRITEBYTECODE=1` and Python
3.13.7 (CPython). Each output file starts with the command line (some with a
`date -u` header) and ends with `exit=<code>`. The row-2–12 commands are in
`evidence/post/verify_rows_2_12.zsh`.

## Finite verification (proposal table)

| Row | Check | Command (abbreviated) | Result | Evidence |
|---|---|---|---|---|
| 1 | Preconditions | fetched `origin/main` = `4c2a7768f`; ruling, proposal, register, prep `SHA256SUMS`, bound script hashes; register row | ruling `782ee02f…d288`, proposal `baf17812…dfdd`, script (prep and run root) `2b6792fe…4869`; row `RULED A / PART B AND 3a, 3b CONFIRMED / M / EFFECTIVE ON MERGE`; prep `SHA256SUMS` 107/107 OK | `evidence/preconditions.out` |
| 1 | Run-root copy | `shasum -a 256 -c` of the 36 prep `SHA256SUMS` entries for the script, aids, candidates, quotes, claims | 36/36 OK | `evidence/runroot_copy.sha256`, `evidence/runroot_copy_check.out` |
| 1 | Reliance preflight, before dispatch (04:51:45Z) | `pec_reliance_hold.py --operation dispatch-for-production` ×8 | `ALLOW`, exit 0 ×8 (register header-only, `f877d931…c741cbc`) | `evidence/reliance_dispatch.out` |
| 1 | `--check-only` | `apply_s4p.py --repo <worktree> --candidates <run root>/candidates --check-only` | exit 0, `CHECK preflight passed`; all 8 preimages and 19 pins as tabled | `evidence/apply_check_only.out` |
| — | The act (04:53:46Z) | same, without `--check-only`, once | exit 0, `CHECK targets 8/8 byte-exact; write set = grant (0 created, 8 modified, 0 removed under projects/pec outside the run root); pinned 19/19 unchanged` | `evidence/apply_run.out` |
| 1 | Reliance preflight, before fan-in of the act (04:54:03Z, before commit `5d13cfdb8`) | `pec_reliance_hold.py --operation rely-for-production` ×8 | `ALLOW`, exit 0 ×8 | `evidence/reliance_rely.out` |
| 1 | Reliance preflight, before fan-in of the verdict (05:22:53Z) | `pec_reliance_hold.py --operation rely-for-production` ×8 | `ALLOW`, exit 0 ×8 | `evidence/reliance_rely_verdict.out` |
| 2 | Contract validity | `validate_scope_of_work.py <DEL folder>` ×8 | `PASS format=SOW_V1` ×8, exit 0 | `evidence/post/validate_<DEL>.out` |
| 3 | Checklist | `derive_review_checklist.py --output <run root>/checklist_<DEL>.json <DEL folder>`, twice | exit 0 ×16; reruns byte-identical; each equal to the prepared hash | `checklist_<DEL>.json`, `evidence/post/checklist_*.out`, `evidence/post/checklist_compare.out` |
| 4 | Boundary owners (QA 21) | `check_boundary_owner_resolution.py --json <run root>/boundary_<DEL>.json --show-not-checkable <DEL folder>/ScopeOfWork.md` ×8 | exit 0 ×8; no `UNRESOLVED_OWNER` or `UNDEFINED_CLAIM`; `NOT_CHECKABLE` exactly the proposal's rows (DEL-04-01 REQ-003/005/006/011/018; DEL-04-02 REQ-006/007/008/010; DEL-08-01 none; DEL-08-03 REQ-004/008/009/011/017/018/020; DEL-08-04 REQ-012; DEL-04-03 REQ-006/008/021; DEL-03-04 REQ-003/008; DEL-10-03 REQ-013); JSON identical to the prepared outputs; hand resolution by the verifier (verdict 01, item 21; F1 below) | `boundary_<DEL>.json`, `evidence/post/boundary_*.out`, `evidence/post/boundary_summary.out` |
| 5 | Quote fidelity | `verify_s4p_quotes.py --tree . --gitdir . --prep <run root> --observation 125cfacc1` | `RESULT PASS 740/740`, exit 0 | `evidence/post/quotes.out` |
| 6 | State claims | `verify_s4p_state_claims.py --gitdir . --prep <run root>` | `RESULT PASS 1144/1144`, exit 0 | `evidence/post/state_claims.out` |
| 7 | Sibling and external IDs; S2 scan | `check_sibling_ids.py <run root> .`; `scan_s2_quotes.py --tree . --gitdir . --prior-commit ce934ac33 --candidates <run root>` | `RESULT PASS 57/57`; `SUMMARY stale=0 kept=2` | `evidence/post/sibling_ids.out`, `evidence/post/scan_s2_quotes.out` |
| 8 | Lifecycle preserved | `git diff --name-status origin/main...HEAD -- '**/_STATUS.md' '**/_REVIEW.md' '**/Review_Findings.csv' '**/MEMORY.md'` | empty, exit 0 | `evidence/post/lifecycle.out` |
| 9 | Registers and quote currency | `validate_decomposition_registers.py --strict projects/pec/execution`; `check_quote_currency.py --tree .`; before the act and after | identical: strict exit 1, 0 errors, 26 `XRG-013` (owner-deferred under D-GOV-48); `SUMMARY active_execution_quotes_verbatim 127/127` | `evidence/strict_pre.out`, `evidence/quote_currency_pre.out`, `evidence/post/strict_post.out`, `evidence/post/quote_currency_post.out`, `evidence/post/before_after_identity.out` |
| 10 | Every-PR checks | `harness.py self-check`; `validate_pec_loop_receipts.py --repo-root .`, before and after | exit 0 each; identical before and after | `evidence/{harness,receipts}_pre.out`, `evidence/post/{harness,receipts}_post.out`, `evidence/post/before_after_identity.out` |
| — | Pins and second run | the script's `PINNED` and `TARGETS` hashed at HEAD; `apply_s4p.py --check-only` after the act | 19/19 pins OK, 8/8 postimages; second run refuses (`target does not hold its preimage`), exit 1 | `evidence/post/pins.out`, `evidence/post/rerun_refuses.out` |
| 11 | Containment | `git diff --name-status origin/main...HEAD` | at `a26ca1613`: the eight `M` contracts, the brief copy and run-root files only; rechecked after the merge (below) and at the records commit (return) | `evidence/post/containment.out` |
| 12 | Whitespace | `git diff --check origin/main...HEAD` | clean, exit 0 (no `.gitattributes` exemption is used) | `evidence/post/whitespace.out` |

Informational: `scan_external_quotes.py --tree .` on the post-act tree reports
`SUMMARY stale=0 kept=33`, because that tree already holds the postimages. The export
reruns read the pre-act tree and give `SUMMARY stale=13 kept=26`; the preparation run
at `d385b6a19` gave `stale=13 kept=25`. The one added line is
`KEPT DEL-08-06 quotes DEL-04-01: 'the versioned additive API schema is `DEL-08-02` (`SOW-042`);'`,
from the `D-PEC-103` act's new DEL-08-06 contract; the quoted DEL-04-01 text is still
in the postimage, so it has no consequence.

## Rerun method

- `run_s4p_checks.sh <worktree> 4c2a7768f <run root> <run root>/evidence/rerun_4c2a7768f`,
  `TMPDIR` under the session scratchpad: `OVERALL PASS` — act check-only 0, apply 0,
  rerun refuses 1; containment 8 differing files, all `ScopeOfWork.md`;
  validate/checklist/boundary ×8; quotes 740/740; state claims 1144/1144; sibling and
  external IDs 57/57; S2 scan stale=0; strict, harness, receipts identical before and
  after (export root normalized); dependency quote currency 127/127 identical;
  whitespace; fault injection 9/9.
- The same at `78e74f590` (`evidence/rerun_78e74f590/`): `OVERALL PASS`, and its
  `SUMMARY.out` is identical to the `4c2a7768f` one apart from the basis line.
- `negative_controls.sh <worktree> 4c2a7768f <run root>`: all six controls tripped,
  `RESULT PASS negative controls` (`evidence/negative_controls.out`).

## Independent verifier

`VERIFIER_VERDICT_01.md` (fresh read-only `pec-reviewer`, candidate `a26ca1613`):
**PASS WITH NOTES**, no blocking finding. Basis, byte identity, the `MODE=VERIFY`
subset (items 1, 3, 4, 8, 9, 13, 16, 18–21), semantics (claims, quotations, scope,
open items, kept IDs, no verify-before-rely rebuild, the Part B landings verbatim with
the DEL-04-01 gates binding, readings 3a and 3b, seven-component consistency, no
Remaining surface), containment and lifecycle all PASS, with independent reruns
matching the recorded evidence. Dispositions:

- **F1** (non-blocking, record): the proposal's QA 21 hand-resolution row for DEL-10-03
  gives the owner `DEL-08-01` of REQ-013 as named in "(CLM-008, CLM-016)" without the
  "not cited" annotation its own convention calls for, and the preamble's "carried from
  the prior contracts" does not fit REQ-013, which is new in this pass. The owner is
  resolved in substance: REQ-013 names `DEL-08-01` in its own text, and the tool-checked
  REQ-015 excludes the access-class decision citing CLM-016, which names it. The
  proposal and the postimage are owner-ruled fixed bytes, so nothing is repaired here.
  **Recorded** here and carried in `HANDOFF_STATE.md` as a currency note for a later
  DEL-10-03 revision (cite CLM-016 in REQ-013 so the tool can reach it).
- **N1** (`origin/main` moved to `78e74f590`, PR #995): **acted on**. The manager merged
  `origin/main` without a rebase (`c8b3a8f9c`; PR #995 touched no `projects/pec`,
  `tools/`, `workflows/` or `agents/` path) and reran the checks (below). As the
  verifier notes, `--check-only` on the post-act tree refuses by design; it was run
  both there (refuses, as expected) and on an export of `78e74f590` (passes).
- **N2** (the three DEL-04-01 REM-002 verification sentences are verbatim after
  whitespace normalization, not as one raw byte run; the clause paragraphs and Gate
  lines are raw-byte verbatim): **recorded**; the proposal's "verbatim" is met in the
  Markdown sense, and the quote verifier checks it that way. No action.
- **N3** (DEL-04-02 L19's accepted exhibit sentence beside L146's carried
  `_CONTEXT.md` "(none)" claim, true at `125cfacc1`): **recorded**; no falsehood, no
  action.
- **N4** (dated "provisional / not yet ruled" wording in the eight postimages):
  **recorded**; disclosed at proposal L243 and true under each contract's observation
  clause. Carried in `HANDOFF_STATE.md`.
- **N5** (`evidence/apply_check_only.out` has no timestamp line; negative control 6
  prints an empty detail): **recorded**; the order is fixed by commit `70a3cebf9` and
  the `apply_run.out` header. The evidence file is not rewritten.
- **N6** (DEL-08-04 `CLM-005`/`CON-006` read `D-PEC-62` more precisely, verified):
  **recorded**; consistent, no action.

## Post-merge rechecks at `78e74f590` (`evidence/post_merge_78e74f590/`)

After the no-rebase merge (`c8b3a8f9c`), at HEAD `c8b3a8f9c`:

| Check | Result |
|---|---|
| `apply_s4p.py --check-only` on HEAD | refuses, exit 1 (targets hold postimages; by design) |
| `apply_s4p.py --check-only` on a `git archive 78e74f590` export (`$X` in the recorded command is that scratch export) | exit 0, `CHECK preflight passed`: preimages and the 19 pins unchanged on the new base |
| Quotes | `RESULT PASS 740/740` |
| State claims | `RESULT PASS 1144/1144` |
| Sibling and external IDs | `RESULT PASS 57/57` |
| Pins / postimages | 19/19 / 8/8 |
| Strict, harness, receipts, quote currency | identical to the pre-act baselines (strict exit 1, 0 errors, 26 `XRG-013`; 127/127) |
| Lifecycle | empty |
| Containment | eight `M` contracts, the brief copy and run-root files |
| Whitespace | clean |

## Later-state rechecks

At the records commit the containment and whitespace rows are rerun against the
then-current merge base; results are in the return. Records added after `a26ca1613`
are confined to the run root and the brief's return path, apart from the merge of
`origin/main`.
