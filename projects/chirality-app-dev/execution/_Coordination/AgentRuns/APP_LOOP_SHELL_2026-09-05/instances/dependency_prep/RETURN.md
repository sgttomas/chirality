# Dependency preparation return

PASS — completed with parent-authorized pinned dependency retrieval after offline cache response misses. Original checkout App and Root node_modules were absent. No original tracked manifest/lock/source or Root path was changed. Scratch mirror `/private/tmp/chirality-dependencies-rrwmmitz`; source identities in SCRATCH.json. Node v24.18.0; npm 11.16.0; cache `/Users/ryan/.npm`; install-links=false.

## Commands and outcomes

- `npm ci --offline --ignore-scripts --no-audit --no-fund --logs-dir=/private/tmp/chirality-dependencies-rrwmmitz/npm-logs`, cwd scratch `runtime/`: exit 0, added 61 packages.
- `npm run build`, cwd scratch `runtime/`: exit 0 (`tsc -b`). This is scratch runtime build evidence, not original Root execution or accepted runtime supply.
- Same offline ci command, cwd scratch `projects/chirality-app-dev/frontend/`: exit 1, ENOTCACHED for pi-tui 0.82.0 registry tarball URL.
- Verified all available cache content against lock integrity, remapped only scratch lock resolved URLs (SCRATCH_TRANSPORT_REMAP.json), repeated offline ci: exit 1, same URL ENOTCACHED. Source lock untouched.
- Direct extraction experiment `restore_cached.py` is scratch-only and is not accepted/promoted as dependency installation; npm layout correctness requires the ordinary installer.

Runtime exports now exist in scratch runtime/packages/*/dist. Original Root remains untouched. No Electron install scripts/downloads ran. Cache inventory found all darwin-arm64 locked content bytes present, but that does not prove npm registry response-index availability.

## Recommended reliable completion

Restore original package-lock.json in scratch frontend. Parent-authorized network retrieval, if granted, runs `npm ci --ignore-scripts --no-audit --no-fund --logs-dir=/private/tmp/chirality-dependencies-rrwmmitz/npm-logs` there. Keep source and lock hashes verified; no pinned version changes. Move accepted scratch node_modules into App frontend, retarget seven runtime package symlinks to scratch built runtime, and retarget harness-contract workspace link to original App package. Disclose scratch runtime mapping in checks; do not claim original Root runtime was built.

## Completed restoration and checks

Parent authorized the exact ordinary npm-ci retrieval after offline misses. Escalated `npm ci --ignore-scripts --no-audit --no-fund --logs-dir=/private/tmp/chirality-dependencies-rrwmmitz/npm-logs` in scratch frontend with ORIGINAL lock: exit 0; added 753 packages. All 745 installed non-link versions matched the lock. npm performs lock integrity verification. The direct-extraction experiment was deleted/replaced by npm ci and was never promoted.

Promoted npm-created node_modules to original App frontend. Seven runtime links target exact-source built scratch runtime packages, and harness-contract targets original App workspace. INSTALL_RESULT.json binds versions and link targets. Original lock remains SHA-256 717d541fe6ee090aae79d4a386bbde1c8ff6ee136a50242d956500d76e80a458. Root node_modules remains absent. Correct App-cwd binary smoke: TypeScript 5.9.3 and Vitest 4.1.10, exit 0. Earlier binary smoke from repo cwd exited 127 and did not test the installed tools.

Runtime scratch `npm run build`, `npm test -- tests/contracts-and-project.test.ts`, and `npm run typecheck`: all exit 0; canonical stdout/stderr and RUNTIME_CHECKS.json are beside this return. Source hashes rechecked after build in RUNTIME_SOURCE_RECHECK.json. These prove the exact-source scratch build, not execution on original Root or acceptance of a new runtime supply.

Scratch is retained because App dependency links require it. Removing it invalidates App runtime module resolution. No lifecycle/signing/release act, Electron download, or package install script occurred.
