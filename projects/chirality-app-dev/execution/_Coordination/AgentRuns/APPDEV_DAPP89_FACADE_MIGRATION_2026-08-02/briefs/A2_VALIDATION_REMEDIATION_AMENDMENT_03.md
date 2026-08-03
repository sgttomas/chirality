# A2 Validation-Remediation Amendment 03 — Reversible Root dependency projection

Status: `EFFECTIVE — PARENT AUTHORIZED`

Date: `2026-08-02`

RunID: `APPDEV_DAPP89_FACADE_MIGRATION_2026-08-02`

ChildInstanceID: existing `TASK-DAPP89-MIGRATION-01`, Attempt 02

Purpose: validation environment only. This amendment is not product
implementation, dependency adoption, or permission to persist generated state.

## Exact authority

The App `HELP_HUMAN` parent authorizes only this sequence:

1. Resolve and record identities, hashes, and metadata of the current real
   repo-root `runtime/node_modules` directory (parent observed only `.vite/**`)
   and the exact App
   `projects/chirality-app-dev/frontend/node_modules` directory supplied by
   current-lockfile `npm ci`.
2. If and only if the identity preconditions hold, atomically rename existing
   `runtime/node_modules` to one unique, explicit sibling backup under
   `runtime/`.
3. Create one temporary symlink at `runtime/node_modules` pointing to the exact
   App frontend `node_modules` target.
4. Run the D-APP-89 required Root build/typecheck/focused export checks and any
   App checks that require Root `dist`.
5. Verify `runtime/node_modules` remains the expected symlink to the expected
   target. Remove only that symlink. Atomically rename the preserved backup
   directory back to exactly `runtime/node_modules`.
6. Prove original directory/tree/metadata identity after restoration and zero
   tracked Root diff.

## Hard exclusions

- no Root source, package, lockfile, or tracked-file edit;
- no dependency install, audit fix, scripts approval, cache deletion, package
  upgrade, or persistent projection;
- no removal or alteration of the parent-supplied App frontend dependency
  tree;
- no continuation if any source/target/backup/symlink identity precondition
  fails;
- no release, publication, dependency-security acceptance, or product-runtime
  claim.

The original effective validation brief and Amendments 01/02 remain binding in
every other respect. After restoration, record exact pre/post evidence and
continue the accepted remediation and fresh-verifier sequence.
