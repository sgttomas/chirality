# WORKING-P3-PKG11 Attempts

- The author normalized one template-only wording inconsistency in owned
  evidence. Exact before/after hashes are retained in `MECHANICAL_REPAIR.md`;
  no candidate or live-project byte changed, and terminal checks plus the
  complete manifest were rebuilt.
- Manager's first verifier-manifest reproduction probe treated verifier-local
  paths as repository-relative. It failed read-only on `ATTEMPTS.md`; no file
  was written. The probe was corrected to the manifest's declared child-relative
  convention and all 493 entries reproduced.
- The manager fan-in helper was mechanically derived from the accepted PKG-10
  helper with package/member/totals bindings changed and syntax checked before
  execution. Its output was independently reviewed against child and frozen
  rows.
- Syntax checks left generated `__pycache__` directories inside owned evidence.
  They were removed as non-semantic build residue before closeout, the manager
  manifest was rebuilt, and terminal containment was rerun.
- No semantic, candidate, source, lifecycle, authority, or acceptance repair
  occurred. Every affected manager binding and check was rerun.
- Direct RECON later identified that the accepted author manifest still bound
  two absent ignored `.pyc` files removed during closeout. Brief v2 authorized
  this owned-evidence repair. Both stale rows and the old manifest hash are
  preserved in `REBINDING_V2.md`; the active child and package manifests were
  rebuilt and the full fan-in rerun without a new child session.
