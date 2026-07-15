# RECON-P3 Attempts

## Attempt 1 — held for upstream manifest rebind

- The direct full-wave harness began by creating the empty snapshot directory
  and auditing upstream manager and child manifests before member
  reconstruction.
- Complete read-only enumeration found exactly two defects. Both are stale
  existence bindings in
  `WORKING-P3-PKG11/children/AUTHOR-B1/MANIFEST.tsv`:
  `__pycache__/finalize_author_pkg11.cpython-313.pyc` (manifest row 19) and
  `__pycache__/run_author_pkg11.cpython-313.pyc` (manifest row 20) are absent.
- PKG-10 manager/author/verifier, PKG-11 manager/verifier, and PKG-12
  manager/author/initial-verifier/replacement-verifier manifests have zero
  path-existence, content-hash, or byte-count defects. All three manager
  manifests retain their expected row counts and SHA-256 identities.
- PKG-12 independence remained valid: the initial verifier is terminal
  `BLOCKED` and excluded; the accepted `VERIFY-B1-R1` command ledger contains
  112 commands and zero targets beneath the prohibited author or failed
  verifier trees.
- Classification: upstream evidence-binding defect outside RECON write
  authority. No candidate or project bytes were evaluated or changed, and no
  member reconstruction began.
- Disposition: parent directed HOLD while routing repair/rebinding to the
  owning package manager under a versioned amendment. The empty incomplete
  snapshot directory is removed before a from-scratch rerun; this attempt
  record remains immutable evidence of the interruption.

## Attempt 2 — failed-verifier status-key compatibility

- After PKG-11 returned `PASS_REBOUND`, the full reconciliation restarted
  from the beginning and revalidated all manager and child manifest rows.
- The RECON-owned harness then attempted to read the retained PKG-12 failed
  verifier's terminal value from `STATUS.json.status`; that historical record
  uses the equivalent key `result` and raised `KeyError` before member
  reconstruction.
- Classification: safe RECON-owned evidence-harness compatibility defect. No
  upstream, candidate, or project file was modified.
- Repair: accept either `status` or `result` while retaining the mandatory
  exact value `BLOCKED`, remove the empty incomplete snapshot directory, and
  restart the complete reconciliation from the beginning.
