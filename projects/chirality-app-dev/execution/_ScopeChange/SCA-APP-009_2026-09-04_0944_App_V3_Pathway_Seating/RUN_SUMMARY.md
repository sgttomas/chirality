# SCA-APP-009 Gate-5 Pre-Pointer Run Summary

On 2026-09-04, a fresh bounded Agent-2 applicator resumed the already-reviewed
normalized candidate at exact current `origin/main`
`aa8554542e3d6d09a925f69e1114bea8e18532f8`. Execution was
delegated-harness-native; role entry and non-delegation were
instruction-asserted, not mechanism-proven.

The applicator verified all protected preimages and collision absences, then
performed the root live-baseline pin and two authority copies from repository
root as separate operations with separate SHA-256 verification. Only after all
three hashes matched did it run the exact actual-worktree APP-HOLD check from
the App root. That check returned exit zero, top-level `ALLOW`, and
`STRUCTURAL_BOOTSTRAP` for DEL-09-07. The exact five-file reviewed scaffold and
the 42-file SCA snapshot were then materialized.

All required checks passed, including the practitioner harness, the combined
governance suites, G0 through G4, APP-HOLD integrity, authority-corpus status,
receipt validation, whitespace validation, manifest verification, scope and
historical-immutability checks. Detailed results are in
`Evidence/Gate5/CHECKS.md`.

The transaction stops at `POINTER_APPROVAL_READY`. No pointer, receipt, commit,
push, PR, merge, downstream implementation, product, frontend, runtime, signing,
publication, or release-readiness act occurred.
