# Current App Source Rebind

State: `PASS — SOURCE FINGERPRINT UNCHANGED; GIT CONTEXT ADVANCED`

Current `HEAD` and `origin/main`:
`88e7590d3664d4f1daf91bed2a8899bda0748b92`.

Worktree state before run writes: clean; detached at the same commit as
`main`/`origin/main`. The current frontend status digest was the empty-input
SHA-256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.

## Reproduced source identity

The original 185-file architecture corpus reproduced exactly:

`ad262802ab4dfd98475121a06eae49e76d461d71b172e860459e3be775392aa4`.

All 13 critical source/config hashes in the original basis manifest also
reproduced exactly, including `package.json`, lockfile, Next/build config,
Electron main/preload, App layout/page, Woven route/shell, Portal shell,
ShellFrame, and domain-profile registry. D-APP-89 therefore remains the exact
current source baseline; no later source delta requires map reconstruction.

## Reproduced inventory

| Area | Files | Lines |
|---|---:|---:|
| `src/app` | 27 | 4,676 |
| `src/components` | 41 | 9,075 |
| `src/lib` | 88 | 25,379 |
| `electron` | 13 | 3,204 |
| `scripts` | 22 | 7,726 |
| `packages` | 14 | 58 |

Additional counts reproduce: 169 non-test TypeScript/TSX source files, 146
test TypeScript/TSX files, 22 page/route entries, 32 shell/Woven component
files, four workspace-provider components, and zero current exact target-
selector matches. The B extraction-review population remains 61 and the
lower-bound seam sets remain `P=9`, `R=11`, and `P union R=20`.

## Rebind consequence

The original dependency maps and coexistence collision inventory remain
source-current. The only lawful update is to bind the now-known six-node `U`
set and rerun delta-dependent candidate tests. No product or source byte was
changed.
