# R18 whitespace repair cycle 1 — orchestration plan v5

Status: `FROZEN BEFORE REPAIR DISPATCH`

CHANGE found exactly five whitespace-only evidence defects after the fresh
content review. All semantic candidate, scope, hash, JSON, package-lock,
containment, and tracked-diff gates passed. This cycle may normalize only the
five named evidence files, record exact lineage, and obtain a genuinely fresh
whitespace/lineage review. It must not rerun or upgrade any validation.

## Graph

1. `A2-PKG09-R18-WS-REPAIR-01`: preserve compressed exact preimages, normalize
   only trailing CR/horizontal whitespace and surplus blank EOF, record exact
   pre/post counts/hashes/delta classes, and verify one final newline.
2. WORKING_ITEMS freezes repaired evidence and reviewer brief.
3. `A2-PKG09-R18-WS-REVIEW-01`: fresh evidence-only review of preimage lineage,
   content equivalence, all candidate whitespace/staged-equivalent checks,
   semantic frozen hashes, JSON, containment, and empty index.

No tests, build, package, network, proof, receipt, or Git integration. Original
`review-1/REVIEW.md` remains immutable historical pre-repair review evidence.
