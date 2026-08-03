# Post-verifier generated-output cleanup

After the second verifier froze and reproduced the standalone/embedded whole-tree comparison, the manager removed the exact generated R2 standalone build directory:

`projects/chirality-app-dev/frontend/dist-runtime-helper/`

It contained only the rebuildable standalone electron-builder derivative created by R2 and was untracked. The authoritative derivative comparison remains frozen in `instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/package/WHOLE_TREE_COMPARISON.md`, SHA-256 `3818e3bb8d24fc3ff0a7b7681b2ebe2c4c4cb6c1ba8b06657cb8de16e3f8a282`.

Post-removal checks confirmed the exact directory is absent, no R2 temporary tree remains under `/private/tmp`, and `git diff --check` passes. The generated directory is not recoverable in place but is reproducible from the frozen candidate source/config; it is not product truth and must not be committed.

The shared ignored `frontend/dist/` output was not removed because it may be consumed by concurrent validation. Any embedded R2 helper there is derivative/source-misaligned after rollback and must not be committed or treated as current product evidence.
