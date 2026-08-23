# Source-site matrix

## Guard and rejected path

| Class | Path/site | Creation or validation | Mode behavior | Finding |
|---|---|---|---|---|
| Product guard | `frontend/scripts/run-packaged-launchagent-login-proof.mjs:709-719` | `assertSafeSnapshotMetadata` rejects any directory/file with `mode & 0o022` | Explicit fail-closed validation | Correct; do not weaken. |
| Product guard | same file `:726-743` | Checks `runtime-data`, `runtime`, `logs`, `auth`, `tokens` in order | First unsafe entry aborts | `runtime-data` is `0700`; the first divergence under this fixture is `runtime-data/runtime`, created as `0775` under `umask 0002`. |
| Product guard | same file `:746-773` | Opens stdout, stderr, token with `O_NOFOLLOW`, then validates descriptor and path metadata | Files with group/other write are rejected | The fixture files would be `0664`; ancestor validation fails before these file checks. |

## Fixture-created runtime-data sites

| Runtime-data path | Fixture site/API | Explicit mode? | Mode under `umask 0002` | Classification |
|---|---|---:|---:|---|
| `runtime-data/runtime` | focused test `:120-121`; intermediate created by `mkdir(.../runtime/logs, {recursive:true})` | No | `0775` | Defect; first rejected path. |
| `runtime-data/runtime/logs` | focused test `:121`; `mkdir(..., {recursive:true})` | No | `0775` | Defect. |
| `runtime-data/runtime/auth` | focused test `:122`; intermediate created by recursive `mkdir(.../auth/tokens)` | No | `0775` | Defect. |
| `runtime-data/runtime/auth/tokens` | focused test `:122`; `mkdir(..., {recursive:true})` | No | `0775` | Defect. |
| `runtime-data/runtime/logs/daemon.stdout.log` | focused test `:123`; `writeFile(path, bytes)` | No | `0664` | Defect. |
| `runtime-data/runtime/logs/daemon.stderr.log` | focused test `:124`; `writeFile(path, bytes)` | No | `0664` | Defect. |
| `runtime-data/runtime/auth/tokens/operator.token` | focused test `:125-127`; `writeFile(path, bytes)` | No | `0664` | Defect. |

The session root and `runtime-data` parent are not made by the fake install: the actual proof harness creates the absent session root with `mode: 0o700` at `run-packaged-launchagent-login-proof.mjs:1493-1501`, then creates `runtime-data` with `mode: 0o700` at `:1093-1094`.

## Product runtime creation sites relevant to the guard

| Product path | Source/API | Mode treatment before guard reliance | Conclusion |
|---|---|---|---|
| `runtime-data/runtime` and `runtime-data/runtime/logs` | `runtime/packages/cli/src/launch-agent.ts:322-324,350-352` | `mkdir(..., mode: 0o700)` followed by unconditional `chmod(..., 0o700)` | No umask reliance. |
| `runtime-data/runtime` / socket parent | `runtime/packages/daemon/src/runtime-daemon.ts:109-113`, through core `ensurePrivateDirectory` | Explicit `0700` plus unconditional `chmod 0700` | No umask reliance. |
| `runtime-data/runtime/auth` | core `atomicWriteJson` in `runtime/packages/core/src/fs.ts:5-21`, used for `clients.json` | Parent uses explicit `0700` plus chmod; temp file uses `open(..., 0o600)` and final file is chmodded `0600` | No umask reliance. |
| `runtime-data/runtime/auth/tokens` | `runtime/packages/core/src/auth-registry.ts:68-73` | `ensurePrivateDirectory` gives explicit/chmodded `0700` | No umask reliance. |
| `operator.token` | same file `:70-73` | `writeFile(..., mode: 0o600)` then unconditional `chmod 0o600` | No umask reliance. |
| owner/client JSON files | core `atomicWriteJson`, `fs.ts:10-21` | `open(..., 0o600)` then unconditional `chmod 0o600` | No umask reliance. |
| `daemon.stdout.log`, `daemon.stderr.log` | plist paths rendered at `runtime/packages/cli/src/launch-agent.ts:239,261-264` | Created by `launchd`, not by a product filesystem creation call; product first hardens the containing `logs` directory to `0700`, and the proof guard validates the resulting files before copying | No product directory-creation defect. The product does not have a JS creation call on which to pass a file mode; retained guard validation is necessary. |
| proof-owned `failed-logs` copies | proof harness `run-packaged-launchagent-login-proof.mjs:890-901` | directory `0700`; both files `0600` with `wx` | No umask reliance. |

## Product answer

No product-owned runtime directory relevant to the snapshot guard lacks an explicit private mode or a safe `chmod` before reliance. The only mode omissions that reproduce PR #632 are the focused test's fake packaged-install sites. The two daemon log files are launchd-created endpoints named by the plist rather than files created by product JavaScript; their parent is explicitly hardened and their resulting metadata is intentionally fail-closed by the unchanged guard.
