# Disposition 04 — PR #632 fixture-mode diagnosis accepted

- Disposition: `RECORD / RELEASE WP-C2`.
- Exact-once `umask 0002` reproduction confirmed the owner-reported mechanism: fixture directories inherited group-writable mode and fixture files inherited group-writable mode, causing the unchanged product snapshot guard to fail.
- Product conclusion: no relevant product runtime directory/file creation relies on umask; private directory/file modes are explicit and chmod-hardened. Launchd creates daemon log files under a product-hardened parent and the guard validates their metadata.
- Authorized implementation scope: only `frontend/src/__tests__/scripts/run-packaged-launchagent-login-proof.test.ts`; pin the diagnosed fixture directory/file creation modes. No product or guard change.
- Evidence: `instances/A2-PKG09-R20-PR632-FIXTURE-DIAGNOSE-01/`.
- Release gate: run focused normal once, post-fix focused under `umask 0002` once, syntax/typecheck/APP-HOLD, then fresh source review. No full suite or build before source commit.
