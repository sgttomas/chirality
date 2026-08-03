# D-APP-89 Option B — Attempt 02 command results

Status: `PASS — COMPLETE DEPENDENCY-BACKED SET`

Date: `2026-08-02`

The candidate implementation bytes were not repaired in Attempt 02. Once the
exact-lockfile App dependency tree was projected reversibly at the Root
workspace resolution point under Amendments 03 and 04, every required Root and
App command passed.

## Exact dependency source

- Parent materialization command: `npm ci` from
  `projects/chirality-app-dev/frontend/package-lock.json`.
- Frontend lock SHA-256:
  `5c8fce2a3c0e2e7b55730ac673ccb07424dcae1e4bbbb408260b1090040c1a56`.
- Materialized `.package-lock.json` SHA-256:
  `63da91e45b9b90e1354c89880a162a0c3f3e8d53d6ef98c0da041e8908d3ce1d`.
- No install, audit fix, scripts approval, dependency edit, or package upgrade
  was performed by this TASK instance.

## Amendment 04 authoritative pass

The temporary projection remained active for all nine commands in this table,
then was restored.

| # | Exact command | Exit | Normalized result |
|---|---|---:|---|
| 1 | `npm --prefix runtime run build` | 0 | PASS — `tsc -b` |
| 2 | `npm --prefix runtime run typecheck` | 0 | PASS — `tsc -b --pretty false` |
| 3 | `npm --prefix runtime test -- tests/contracts-and-project.test.ts` | 0 | PASS — 1 file, 8 tests |
| 4 | `npm --prefix projects/chirality-app-dev/frontend test -- src/__tests__/lib/harness-contract-rollback.test.ts` | 0 | PASS — 1 file, 13 tests |
| 5 | `npm run test` from App frontend | 0 | PASS — 142 files passed, 1 skipped; 1,111 tests passed, 4 skipped |
| 6 | `npm run typecheck` from App frontend | 0 | PASS — browser and Electron TypeScript checks |
| 7 | `npm run harness:validate:contract-deps` from App frontend | 0 | PASS — `harness contract dependency lint passed` |
| 8 | `npm run build` from App frontend | 0 | PASS — Next 24/24 static pages, Electron and runtime CLI bundles |
| 9 | `npm run desktop:pack` from App frontend | 0 | PASS — macOS arm64 directory pack with `--publish never`; packaged dependency boundary PASS; instruction-root integrity PASS |

Command 5 used the Amendment 04 local-socket permission because the sandboxed
attempt had produced 19 `listen EPERM` environment failures. Command 9 used
the Amendment 04 network permission because the sandboxed attempt had failed
`ENOTFOUND github.com`; electron-builder downloaded its Electron archive and
did not publish. The package verifier reported zero local-package entries, no
forbidden development packages, and all required packages present.

`instruction-root:integrity` reported `status: pass` over 43 checked files. Its
separate source-completeness field remains `needs_remediation`; this is not a
D-APP-89 migration failure and was not altered.

## Projection identity and restoration

Before projection, repo-root `runtime/node_modules` was a real directory with:

- inode `22189023`;
- metadata `drwxr-xr-x`, uid `501`, gid `20`, size `96`, mtime `1785698126`;
- file-tree aggregate
  `1061e05a417ec98bc49a5272fc970385b02dc57501f8c6b977dd27e486b446b8`;
- empty symlink aggregate
  `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.

The real directory was atomically renamed to
`runtime/node_modules.dapp89-attempt02-backup`; the temporary symlink pointed
exactly to
`/Users/ryan/.codex/worktrees/5bef/chirality/projects/chirality-app-dev/frontend/node_modules`.
Immediately before restoration, the symlink target was reverified. Only that
symlink was unlinked and the preserved real directory was renamed back.

Post-restoration inode, metadata, file aggregate, and link aggregate exactly
match the values above; the backup is absent and `git diff -- runtime` is
empty.

## Earlier environment-only observations retained

- Without the projection, Root commands exited 127 because `tsc`/`vitest`
  were not resolvable and App checks could not resolve built Root packages.
- With the first Amendment 03 projection, Root build/typecheck/focused tests,
  App focused test/typecheck/validator/build all passed; the sandboxed full App
  suite was blocked only by local-socket `EPERM`, and desktop packing only by
  `github.com ENOTFOUND`.
- The Amendment 04 run above supersedes those environment blockers without
  weakening any acceptance check.

## Preservation

- No migration-caused source defect was found; no Attempt 02 product-source
  repair was made.
- The compatibility facade is byte-identical to Git base
  `97678a841ef58345c73d3470ed8de57c9b1405d2`.
- DEL-03-01 remains `IN_PROGRESS`; Checking Approval SHA remains
  `8c6d55d3e8b07d8d3c8d98c510cf6672766d7bec`.
- The six D-APP-81 `HISTORICAL_RELATION_UNKNOWN` rows remain exactly six and
  their authoritative file has no diff.
