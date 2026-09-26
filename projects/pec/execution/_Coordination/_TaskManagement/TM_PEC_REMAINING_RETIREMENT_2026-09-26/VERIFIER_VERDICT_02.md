# RR1 verifier verdict 02 (backcheck) — transcription and repair map

Reviewer: the same read-only `pec-reviewer` TASK as review 01 (it authored
nothing). Candidate: PR #951 at `4f4534ab6c824ab21f6be2b2646d9712c235160c`
(merge-base `db9328789`, PR #943 merged). The manager transcribes the verdict
in condensed form; the repair column is the manager's.

**Verdict: PASS WITH NOTES (0 BLOCKING, 2 NON-BLOCKING, 8 NOTE).** The
reviewer confirmed repairs 1–13 in the repository files. It reproduced:
`gen_d99.py --check-only` on the live worktree (62 paths, exit 0, no
substitution); all 62 POST hashes and 57 preimages; the act and second-run
refusal; `verify_d99.py` account mode PASS and act mode 17/17 (with the
review-01 verifier); `--q1 park` and `--q1 decline` (each passes with its own
answer and fails when checked as s1); the `--allow-extra` allowlist (fails
closed); manifest `G4 PASS` (128); entrypoints PASS; strict registers
identical pre/post. Every full hash in the run basis (62) and the packet
(142) matched a recomputed file, the historical ones being so marked.
Containment: the TM folder and the RR1 return only.

| # | Class | Finding (reviewer) | Manager repair |
|---|---|---|---|
| 1 | NON-BLOCKING | PR body still says (d) 81 and that #943 must merge first | PR body rewritten: (d) 82 (71 + 11); #943 merged as `db9328789`; q1 park/decline |
| 2 | NON-BLOCKING | 34 exhibit currency notes call SCA-006 pending or #943 unmerged, frozen into a post-#943 decision file | Exhibit Part A intro now states the notes predate the #943 merge (`db9328789`) and that SCA-006 has since merged; generator, exhibit POST and tables regenerated (only the exhibit postimage changed) |
| 3 | NOTE | Packet status line says D-PEC-98 is in open PR #944 | Updated: #944 merged; no D-PEC-99 row on `db9328789`; number still provisional |
| 4 | NOTE | Limits omit option A″ | Added |
| 5 | NOTE | Under park, DEL-03-06-REM-004 is labelled an evidence inquiry | New class `EXHIBIT_A_PARKED`: own heading "parked documentary correction", own History label, Part A count shows "plus 1 parked correction" |
| 6 | NOTE | Exhibit presupposes question 4 | Question 4 now says the provenance line presupposes confirmation; without it the act waits or the packet is amended |
| 7 | NOTE | Verifier does not discriminate decline | Added `declined_items_absent_from_exhibit`; a decline check on the s1 tree now fails |
| 8 | NOTE | Act mode reads an unpinned account from `--repo` | Act mode now reads the account and census from `--pre` |
| 9 | NOTE | RR1 return still interim | Replaced at handback |
| 10 | NOTE | Strict register validator exits 1 pre and post | Recorded in the packet's verification table and the run basis |

Reviewer's scratch: `…/scratchpad/rr1/review02/` (manager scratch, not tracked).
