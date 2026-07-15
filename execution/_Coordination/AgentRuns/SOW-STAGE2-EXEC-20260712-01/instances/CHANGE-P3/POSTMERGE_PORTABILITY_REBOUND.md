# CHANGE-P3 Postmerge Portability Rebound

Verdict: `PASS — SAFE MECHANICAL BINDING REPAIR`.

The fresh exact-main worktree exposed three ignored `__pycache__` bindings
that existed in the source worktree but were never tracked. They are generated
runtime residue, not candidate, project, source, control, lifecycle,
dependency, semantic, or acceptance evidence.

Exact repairs:

- PKG-10 AUTHOR-B1 manifest: two stale rows removed; SHA-256 changed from
  `a07f54b3630858a943bc977bb7fdb8238460bdf6a9af6e63bfd23af3d00797bb`
  to `2f8e384756a60c9c149d04231caae5dcce0283b44a23e3cfd5e7f684205ffa9a`.
- PKG-10 manager manifest: transitively rebuilt from
  `4856fe725d0feaf4866d39a749d2e3769031204b452268466119cf210023ed0a`
  to `5bc18da54167c7c157398aed6e3000d1811a80245a738e59e973cc7a2f98ed49`.
- PKG-12 VERIFY-B1-R1 manifest: one stale row removed; SHA-256 changed from
  `fadfb2f1f91fdcedd208d285cd90ec7eaa154c3bf1b83ed6229bca04086d26bc`
  to `b6546d26164807c7a9bb4a9e1352aebf334cacc1ba54f442201e9a17e942ea79`.
- PKG-12 manager manifest: transitively rebuilt from
  `ab265d917a4d51e6e1bae7f0e9c2aa75e0f36cb9f82f329e783f345c8793a417`
  to `87f78e9108f4c425b2bf52196a5b9572cf0b4f0a33356ee161494e8911d2a52e`.

All ten current W-P3 package/child manifests validate: 8,796 bindings,
portable existence/byte/hash checks PASS, zero ignored-residue rows. The
accepted preintegration snapshot remains immutable at its accepted hash and
is retained as historical acceptance evidence; this rebound corrects the
current derivative package bindings without changing its project or semantic
verdict.
