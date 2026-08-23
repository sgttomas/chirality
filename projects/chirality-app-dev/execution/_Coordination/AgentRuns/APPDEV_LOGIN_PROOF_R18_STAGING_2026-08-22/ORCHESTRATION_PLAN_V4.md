# DEL-09-04 R18 Tranche A implementation — orchestration plan v4

Status: `FROZEN BEFORE IMPLEMENTATION DISPATCH`

## Accepted sync

- Branch: `codex/app-login-proof-r18-staging`
- HEAD: `f59105ddb606bd46397c3b1aafa41b50ab4e9e8d`
- Parent 1: `166efa82748133e90674be62304b81f8a0a8c1b4`
- Parent 2 / origin/main sync target:
  `b143444bd497eae1b1b638670a33e6df756d9084`
- Main delta under `projects/chirality-app-dev/`: empty
- Index/tracked porcelain: clean; inherited 28 run-root files untracked

The synchronization hold in v3 is satisfied. Attempts 1/2 and accepted
network evidence remain immutable context.

## Graph

1. Fresh `A2-PKG09-R18-IMPLEMENT-04` is the sole overlapping write owner for
   verifier/wrapper/tests/package scripts, one offline evidence build, R18,
   minimal status, and unique executor-4 evidence.
2. WORKING_ITEMS validates fan-in and freezes all remaining non-review bytes.
3. Fresh `A2-PKG09-R18-REVIEW-01` performs the complete evidence-only matrix
   and writes only its unique review record.

At most two repair plus fresh-review cycles. No more network is authorized.

## Fan-in gates

- Fail-closed production verifier pins Electron 43.2.0, exact filename, size,
  hash, official line/URL, and exact package devDependency match; secure path
  and streaming hash rules hold without caller bypass.
- `desktop:pack` retains its name/gates and passes one spaces-safe
  `-c.electronDist=<verified-directory>` argument. `electron:supply-chain`
  verifies independently.
- Required focused fail-closed and pack-argv tests pass.
- Active nested `app-builder-lib/node_modules/@electron/get` 3.1.0 Bypass
  cause is evidenced by exact local source path/hash/line region; top-level
  5.0.0 is distinguished as unrelated.
- Exactly one new post-implementation offline `npm run desktop:pack` exits
  zero, logs custom electronDist use, no download, and passes embedded
  dependency/instruction-root gates. Full log exists.
- Build is explicitly evidence-only and not an adopted proof package.
- R18 records all three attempts, supply freeze, official network evidence,
  implementation/tests/offline build, non-adoption, and R19 separation.
- Status remains `IN_PROGRESS` and unproved; no R19/owner procedure.
- Full validation, hygiene, containment, and fresh review PASS.

## Fences

No network, additional pack/build attempt, package/proof adoption, R19 staged
procedure, GUI, prepare/capture/logout/login, bootstrap/kickstart,
operator/default job/plist/launcher action, sign/notarize/deploy/distribute,
release/proof claim, Receipt 189, stage/commit/push/PR/merge.
