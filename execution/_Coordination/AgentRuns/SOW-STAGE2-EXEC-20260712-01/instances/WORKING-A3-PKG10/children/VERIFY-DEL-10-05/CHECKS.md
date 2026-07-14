# VERIFY-DEL-10-05 Checks

- Accepted APP manifest row: exact `PKG-10` / `DEL-10-05`, `IN_PROGRESS`, non-pilot, non-ISSUED.
- Live source/control kit equals the accepted row and author workspace byte-for-byte; `_STATUS.md` remains `IN_PROGRESS`.
- Candidate exact: `0761ab08daee0d87e69b6efad3216e5228e34be8207a1483e335bfbb237e2c9a` (37,724 bytes; 534 lines).
- Standalone `SOW_V1` and exact-authority `MIGRATION_DUAL`: valid with zero issues.
- Claim map/parity: 36/36 mappings, 318/318 source lines, all `PRESERVED`, zero issues.
- Checklist pair: `d50b78182ff4578f131400d5b922ab0137f129b968caa71b42fcd829e46e7ee9`, byte-identical, one exact `AC-001` linked to `VER-001`.
- HTML pair: `b8accd6ec9e37adac94279f0748a2bec573af0385485dcba11de8d1df00164e1`, byte-identical, source-hash-bound, script-free, and free of external/file resources.
- Missing-kit, unruled-dual, and padded-authority fixtures each return nonzero for validation/checklist and emit no checklist artifact.
- The first render invocation passed a directory to a file-oriented CLI and produced no HTML; its stderr is preserved as `RENDER_PATH_ATTEMPT.stderr`. Both correctly addressed required renders subsequently passed and match the author-accepted hash. This is transparent non-acceptance substrate evidence, not candidate evidence or repair.
- Domain notice, proposal-only, protected-path, operation-gate, lifecycle, and solver-truth authority review: PASS; no new authority or semantic obligation beyond exact source, `SOW-071`, `OBJ-009`, and `OBJ-010`.
- Two accepted checkout-absolute `_DEPENDENCIES.md` literals remain byte-identical and are separately inventoried.
- Replacement plan: exact five rows (one ADD, four DELETE); no action executed.
- Candidate/project/author/sibling/package/Git/lifecycle writes: zero.
