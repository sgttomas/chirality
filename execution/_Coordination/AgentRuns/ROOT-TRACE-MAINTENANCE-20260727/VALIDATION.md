# Validation — ROOT-TRACE-MAINTENANCE-20260727

Status: `PRE-APPLICATION PASS`

## Basis and preimages

- Immutable basis resolves to
  `7b0be4d8772a16e5a4774a17988479587d00acca`.
- The W-A pointer, Root handoff, and full Receipt-55 register match their
  accepted postimage hashes.
- Receipt 55 is the unique current Root cursor.
- All 83 predecessor target paths exist and match their recorded preimage
  hashes: 83 exact, zero stale, zero missing.
- All three proposed run-record targets are absent.

## Candidate results

- Semantic postimages: 38 `ScopeOfWork.md` plus 45 `_CONTEXT.md` = 83.
- Responsibility replacements: 42 plus 45 context tails = 87.
- Closed-conflict current-state replacements: 19.
- Lifecycle trace replacements: eight; `_STATUS.md` remains authoritative and
  unchanged.
- Receipt candidate: exactly Receipt 56 with parent Receipt 55.
- Exact live write inventory: 87 unique rows.
- W-A current-workplan pointer and Root handoff are absent from the write
  inventory.
- Candidate carriage-return, trailing-whitespace, placeholder, reference,
  and containment checks pass.

## Required application-time reruns

1. Require immutable basis identity or prove this basis remains an ancestor
   while every recorded preimage and absence condition remains exact.
2. Re-run the 46/46 register/header assignment and lifecycle censuses.
3. Apply all 87 rows exactly and verify every full postimage hash.
4. Re-run `validate_scope_of_work.py` on all 46 live contracts.
5. Re-run responsibility, closed-conflict, and stale-lifecycle negative scans.
6. Confirm decomposition, register, status, dependency, PRD, runtime,
   instruction-surface, pointer, and Root handoff paths are absent from the
   diff.
7. Run Root G0–G4, path-anchor checks, relevant governance/harness tests, and
   `git diff --check`.
8. Confirm Receipt 56 occurs once, immediately follows Receipt 55, and cites
   Receipt 55 as parent.
9. Return exact path/hash evidence and a separate CHANGE gate.

Validation is evidence, not acceptance.
