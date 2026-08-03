# A2 Validation-Remediation Amendment 04 — Hold projection through App validation

Status: `EFFECTIVE — PARENT AUTHORIZED`

Date: `2026-08-02`

RunID: `APPDEV_DAPP89_FACADE_MIGRATION_2026-08-02`

ChildInstanceID: existing `TASK-DAPP89-MIGRATION-01`, Attempt 02

## Reason and preserved evidence

Amendment 03 proved the reversible Root projection and restored the original
`runtime/node_modules` before the complete App validation. The parent then
attempted an unsandboxed `npm run test` after restoration. It returned 13
failed suites, 4 failed tests, 1009 passed, and 42 skipped solely because
built Root workspace packages could not resolve
`@chirality/runtime-contracts` / `@chirality/runtime-client` through the
restored `.vite`-only `runtime/node_modules`. This is parent-provided
environment evidence and not a migration-source defect.

## Corrected exact sequence

Repeat Amendment 03's full identity-gated reversible projection, with these
changes:

1. Re-establish the same verified atomic backup and temporary symlink from
   `runtime/node_modules` to the exact current-lockfile App frontend
   `node_modules`.
2. Keep the projection active through the entire dependency-backed set:
   - exact Root build, typecheck, and focused export/identity tests;
   - App focused rollback identity test;
   - App full test, typecheck, contract-dependency validator, build, and
     `desktop:pack` with its existing `--publish never` posture.
3. The exact full App test and Desktop-pack commands may request/execute
   unsandboxed local-socket/network access only as required to overcome the
   already observed `listen EPERM` and `github.com ENOTFOUND` environment
   denials. No publication, dependency install/change, audit fix, scripts
   approval, cache manipulation, or extra network action is authorized.
4. Restore only after every exact Root/App command completes. Verify the
   symlink target immediately before removing the symlink; rename the preserved
   original real directory back; prove the original directory/tree/metadata
   identity, backup absence, and zero tracked Root diff.

If a required check still fails, diagnose and remediate only a demonstrated
D-APP-89 migration defect inside the original write fence; otherwise stop with
exact evidence. No acceptance, retirement, release, or persistent projection
is authorized.
