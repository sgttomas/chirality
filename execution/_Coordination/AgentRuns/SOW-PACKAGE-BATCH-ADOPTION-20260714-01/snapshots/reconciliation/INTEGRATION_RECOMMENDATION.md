# Exact Integration Recommendation to CHANGE

Recommendation: `PROCEED`.

CHANGE may release A4 only while HEAD remains
`98af1a4bde875a0c2d5878d62fc84b3c1d7506c4` and all 72 frozen live hashes
still match. Any drift invalidates this recommendation and returns the package
for revalidation.

A4 should:

1. recheck branch, HEAD, the eight-member census, and all 72 live bindings;
2. apply exactly `snapshots/reconciliation/REPLACEMENT_MANIFEST.tsv`: add the
   eight candidate `production/ScopeOfWork.md` files at their named live paths
   and delete only each member's four legacy documents;
3. leave `_STATUS.md`, `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and
   `Dependencies.csv` byte-unchanged;
4. never copy an `evidence/ScopeOfWork.md` or `finalization.json` into a project
   deliverable;
5. confirm exact inverse rollback from `ROLLBACK_MANIFEST.tsv`, validate all
   eight clean contracts, rerun Piping package checks, practitioner self-check,
   and the complete registered harness, and verify `DEL-01-01` and PKG-00 are
   untouched;
6. stage only the authorized A1 instruction/plan/amendment surfaces, this
   adoption run's evidence, and the exact eight project replacements; exclude
   unrelated dirty and `.claude-worktrees/**` state;
7. review the staged diff and containment, commit on
   `codex/adopt-pkg-batch-workflow`, push, open the human-authorized PR, and
   merge only after required checks and review pass; and
8. hand synchronized-main evidence to A5 so the standing loop can resume from
   the next dependency-valid ordinary package.

No lifecycle promotion, H1/H2 action, PKG-00 change, substantive engineering
approval, or additional package integration is part of this recommendation.
