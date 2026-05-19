# Brief — EQUATION_AUDIT proof-case snapshot

**Status:** PROOF-CASE. This snapshot was created by the end-to-end Phase 0 → Phase 6 smoke test for the EQUATION_AUDIT workflow. It is NOT a real closure of the MWK_1956 audit — the workflow ran in dry-run mode for Phase 3c (fix-apply) so live per-page MDs were not modified. The snapshot captures the post-migration state of the working/ folder so the snapshot mechanic itself is demonstrable.

## Runtime parameters

- BOOK: MWK_1956
- WORK_DIR: domain-test/domains/piping-design/_Sources/MWK_1956_pdf2md_work
- SOURCE_AUDIT_ROOT: domain-test/domains/piping-design/_Sources/MWK_1956/audit/equations
- SOURCE_MD: domain-test/domains/piping-design/_Sources/MWK_1956.md
- TITLE: "MWK 1956 — Strength of Materials (proof case)"
- ALLOW_UNREVIEWED: (proof-case override — full coverage NOT required)
- ENABLE_CROPS: false
- BATCH_SIZE: 5

## What this proves

- Phase 0 state scan against the post-migration layout returns coherent counts.
- Phase 1 audit_equations.py re-extracts cleanly under audit/equations/working/.
- Phase 3a equation-flag-interpret dispatch (via TASK + skill) converts a synthetic prose correction note into valid LaTeX preserving the equation's structure.
- Phase 3b validate_flagged_schema.py refuses prose-shaped descriptions before fix-apply, and PASSes once the interpreter has run.
- Phase 3c process_flagged.py --dry-run identifies the target hash in live per-page MDs and computes the new hash without modifying anything.
- Phase 6 snapshot promotion produces an immutable directory under snapshots/ and updates _LATEST.md.

## What this does NOT prove

- A real closure of MWK_1956's audit (4 flagged + 8 backcheck items remain pending real human review).
- equation-bbox-detect end-to-end with crop_equation_regions.py (smoke-tested separately in Task #17 against page 5 of MWK_1956; crops not generated against full source as ENABLE_CROPS=false here).

## Created at

2026-05-17T02:35:42Z
