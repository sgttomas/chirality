# Review workflow and CHECKING reversal update

Owner-authorized Root tranche `ROOT-REVIEW-SPEC34-REVERSAL-20260926` aligns the bundled `review` workflow and `tools/scaffolding/write_status.sh` with `docs/SPEC.md` §3.3–3.4:
- Entry to `CHECKING` is a candidacy check: a current candidate-bound account showing no unfulfilled production obligation (a whole-deliverable bounded-reconciliation or concordance comparison where available), a declared checking basis recorded in `_REVIEW.md`, and the human freeze recording the frozen candidate SHA. Deferral is no longer an entry path, and the Gate 1 override from `SEMANTIC_READY`/`INITIALIZED` is removed.
- One severity and disposition rule covers both transitions; `CHECKING → ISSUED` checks that the frozen claim surfaces are unchanged since the frozen SHA.
- Gate 5 runs the owning loop's promotion preflight and honours its issuance fences, finalizes the immutable `REV_*` snapshot and `_LATEST.md` in every branch, and adds a human-ruled reversal branch.
- `write_status.sh` now admits `CHECKING → IN_PROGRESS` for a HUMAN actor with a committed `--ruling` (plus `--approval-sha` where an adapter declares it) and records `[reversal from CHECKING; ruling: …]` in history. Other backward moves, including `ISSUED → IN_PROGRESS`, stay blocked.

This loop holds deliverables in `CHECKING`; the reversal is now the recorded exit from an unsuccessful or withdrawn check for them. Their existing state and records are unchanged. This loop decides its own adoption; this source tranche grants no release or issuance.
