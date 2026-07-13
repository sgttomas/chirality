# Check-Evidence Portability R2 Checks

Authority: A1-PKG01-CHECK-EVIDENCE-PORT-R2-001.

Verdict: PASS.

- PROJECT_CHECKS.json changed only workspace_root from the checkout root to
  portable ~ exactly once. Preimage 45,934 bytes and SHA-256
  756aa875a1279526dc192b4e338f049167a7de1134f18a6478450269931972a3;
  postimage 45,898 bytes and SHA-256
  94e56cfbc1b67b7c6c9d5da81c8aa032cd867117c9accd816a5ee97df78f035d.
- PROJECT_CHECKS_PREMERGE.json changed only workspace_root in the same way
  exactly once. Preimage 12,902 bytes and SHA-256
  9ca4aac07fa13ace3794e1fe1a136a210a751519007991bc026839cd3b8a6638;
  postimage 12,866 bytes and SHA-256
  ec6372e7a1e1de38b17580a8b8ef39e06218d71019856725c40231a89ca8f606.
- Reverse substitution reproduces both exact preimage hashes.
- Both postimages parse as JSON. Commands, statuses, exit codes,
  stdout/stderr, timing values, and results are byte-identical because the
  exact reverse proof differs only at workspace_root.
- All six registered App checks remain PASS: five in PROJECT_CHECKS.json and
  frontend-premerge in PROJECT_CHECKS_PREMERGE.json.
- Historical CHECK_NORMALIZATION_MANIFEST.tsv is unchanged and its R1
  postimages equal these exact R2 preimages.
- The superseded package MANIFEST.tsv preimage has 37 data rows and SHA-256
  77ea1855811612ae3f19226e6fd5b1d80cd737d91b1ee519f80d3dd49068b1b3.
  The regenerated manifest hash and row count are reported by the terminal
  owning-manager return after MANIFEST.tsv is written last.
- Generated evidence has zero checkout-root and local-temp prefixes outside
  the accepted copied-source, fixture, marker-bound candidate/render, and
  PRESERVED_SOURCE_LITERAL inventory.

No member, candidate, replacement/rollback, child, project, lifecycle, Git,
integration, H1/H2, ISSUED, release, or retirement byte was changed.
