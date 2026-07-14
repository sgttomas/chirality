# CHANGE-BATCH-ADOPTION Checks

- Basis: branch `codex/adopt-pkg-batch-workflow` at parent
  `98af1a4bde875a0c2d5878d62fc84b3c1d7506c4`.
- Pre-apply reconciliation: 72/72 live bindings, 252/252 upstream manifest
  rows, 40 forward rows, 40 exact inverse rows, and 8/8 simulations passed.
- Project application: eight clean `ScopeOfWork.md` additions and 32 exact
  legacy-document deletions match the reconciled after-state hashes.
- Preservation: all 40 underscore/control/status/dependency files remain
  byte-identical to the frozen inputs.
- Exclusions: `DEL-01-01`, PKG-00, lifecycle, H1/H2, release, retirement, and
  packages outside the authorized population are untouched.
- Clean validation: 8/8 integrated kits resolve as `SOW_V1`.
- Piping production census: 12 `SOW_V1`, 89 `LEGACY_FOUR_DOC`, zero
  `MIGRATION_DUAL`, and zero `AMBIGUOUS` among the 101 valid production kits.
- Agent instruction validation: two changed manager instructions, zero errors,
  zero warnings.
- Root instruction entrypoints and path anchors: pass.
- Practitioner self-check: byte-identical to the accepted pre-application
  result, with zero blocks. Its unrelated baseline findings remain unchanged.
- Registered practitioner harness: 264 passed in 70.23 seconds.
- Adoption manifests: four manifests and 368 rows rehashed; 92 JSON files
  parsed.
- Tracked project/governance diff check before evidence staging: pass.
- Final staged containment: 426/426 authorized paths, zero outside scope.
- Final `git diff --cached --check`: pass with zero findings.

All CHANGE commit gates pass.
