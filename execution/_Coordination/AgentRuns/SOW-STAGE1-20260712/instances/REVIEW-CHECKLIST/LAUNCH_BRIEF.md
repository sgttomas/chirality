# REVIEW-CHECKLIST Launch Brief — v1

Role: `REVIEW` (Agent 1, lifecycle-neutral evidence mode)
Objective: prove deterministic repeated checklist derivation directly from
the `AC-*` definitions in all ten frozen Stage-1 candidates.
Basis: D-GOV-15; schema freeze; App commit `fb83ffca8...`; Piping commit
`31c35ea97...`; frozen main `2770fda4c...`.
Reads: REVIEW instructions, candidate standard, ten candidates, accepted
decomposition/objective context, and D-GOV-15.
Writes: only `REVIEW_CHECKLIST_EVIDENCE/` under the root run directory.
Method: resolve authorized candidate mode, derive the common candidate
checklist plus one item per `AC-*` directly from each candidate twice in fresh
temporary runs, preserve source references, compare byte identity and item
ordering, and report matrix linkage to `VER-*`/human-review methods.
Denied: project writes, `_REVIEW.md`, checklist acceptance, finding
disposition, lifecycle/status changes, source/candidate edits, canon, PR/merge.
Return: per-deliverable hashes/counts, aggregate PASS/FAIL, blockers and rerun
requirements. This run proves derivation determinism only; it is not a formal
review or lifecycle acceptance.
