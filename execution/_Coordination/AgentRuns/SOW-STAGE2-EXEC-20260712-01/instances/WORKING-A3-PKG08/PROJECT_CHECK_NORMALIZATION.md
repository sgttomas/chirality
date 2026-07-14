# WORKING-A3-PKG08 Generated Evidence Normalization

Disposition: `PASS — EXACT REVERSIBLE GENERATED-EVIDENCE REPAIR`.

Only generated execution metadata was normalized. Captured checkout-root
literals were replaced by `{REPO_ROOT}` in eleven TASK/terminal records and
by `~` in the two software-check records. Captured harness temporary roots
were replaced by `${TMPDIR}` and `${TMPDIR_SECTION9}` in the check records.
Candidate, copied source/control, map, parity, checklist, render, verdict,
replacement, live project, and lifecycle bytes were not changed.

## Software-check records

| File | Pre SHA-256 / bytes | Substitutions | Post SHA-256 / bytes | Reverse proof |
|---|---|---:|---|---|
| `PROJECT_CHECKS.json` | `4bae15d2a22776f82534637cf375914a9921880c31140d492062fb0eb83f3e9f` / 46,993 | 5 checkout + 2 harness temp | `0f3122b86e60c1546d0ccb727dbfe3dba9d5d222de501c8202b871a3fc6c9367` / 46,663 | exact prehash |
| `PROJECT_CHECKS_PREMERGE.json` | `bcc8c3768cedd341b5c69d994f682b0d1a0e4f598a99f8b368df76761baf5890` / 13,700 | 23 checkout + 2 harness temp + 2 section-9 temp | `85416cc0eeec547d57a83c52bd4ace2012fa89648416aad86a913ab6750d71d1` / 12,572 | exact prehash |

Both postimages parse as JSON, contain zero checkout/temp-root occurrences,
and reverse in memory to their exact preimage hashes. The first preserves its
five PASS checks plus the initial no-server frontend-premerge substrate FAIL;
the second preserves the temporary stub-backed frontend-premerge PASS.

## TASK and terminal records

Exactly 32 checkout-root substitutions were applied across ten TASK run
records and `AUTHOR-DEL-08-03/RETURN.md`. Per-file pre/post hashes, byte
counts, substitution counts, and exact reverse proofs are frozen in
`PORTABILITY_NORMALIZATION.tsv`. All ten child manifests were rebound to the
postimages; their hashes are frozen in `CHILD_MANIFEST_REBINDINGS.tsv`, and
all 441 child-manifest rows reproduce after the repair.

The remaining captured checkout literals are confined to immutable copied
source/control bytes, their marker-bound candidates/renders/fixtures, and
explicit preserved-literal inventories. `PRESERVED_SOURCE_LITERAL_INVENTORY.tsv`
classifies all 105 occurrences in 85 files; unclassified occurrences are zero.
