# B-PACKAGING — RETURN (Stage B, TRB-APPDEV-DAEMON-SERVICE-2026-07-25)

**Agent:** Agent 2 "B-PACKAGING" (opus). **Branch:** `feat/daemon-service` (no commits made).
**Status:** B1, B2, B3 complete. Gates run in scope: `typecheck` PASS, `vitest run` PASS (990 passed / 4 skipped, 131 files). `desktop:pack` NOT run (Agent 1 / Stage V own it).

## Files changed / created

| Path (repo-relative) | State | Change |
|---|---|---|
| `projects/chirality-app-dev/frontend/package.json` | modified | B1: `"public/**/*"` added to `build.files`; B2: `"icon": "build/icon.icns"` added to `build.mac`. Nothing outside the `build` block touched. |
| `projects/chirality-app-dev/frontend/build/icon-macos.svg` | new | icns-tuned 1024-canvas variant of the quincunx artwork (source of truth for the icns). |
| `projects/chirality-app-dev/frontend/build/icon.icns` | new (binary) | 140,284 bytes, 10 reps, `ic12` type. Committed artifact. |
| `projects/chirality-app-dev/frontend/scripts/generate-macos-icon.mjs` | new | One-time offline generator, NOT in the build graph. |
| `projects/chirality-app-dev/frontend/.gitignore` | modified | **SCOPE DEVIATION — see Integration points #1.** One negation (`!/build/`) + comment; required or the icns cannot be committed. |
| `projects/chirality-app-dev/frontend/electron/cli-launcher.ts` | modified | B3: `renderCliLauncher` gains required `userDataDirectory`; rendered script exports `CHIRALITY_USER_DATA`. |
| `projects/chirality-app-dev/frontend/src/__tests__/electron/cli-launcher.test.ts` | modified | Existing case updated for the new field; 2 new cases (pin + no-override, single-quote quoting). |

`frontend/public/chirality-app-icon.svg` NOT modified (as instructed). `package-lock.json` NOT mutated (verified via `git status --porcelain`). No files under `frontend/electron/**` other than `cli-launcher.ts`; no `frontend/src` files other than the cli-launcher test; no `runtime/**`.

## B2 — icon design decisions (before → after)

Source is a 32-unit viewBox mark drawn to read at 26px in-app; the icns variant is a redraw on a 1024 canvas, not a scale-up.

| Property | Source (`public/chirality-app-icon.svg`) | Naive 32x upscale (rejected) | icns variant (`build/icon-macos.svg`) |
|---|---|---|---|
| Canvas | 32 vb (512 nominal px) | 1024 | 1024 |
| Mark footprint | 31 of 32 = 96.9% of canvas | 992/1024 = 96.9% | **824/1024 = 80.5%** (Apple macOS icon grid) |
| Transparent margin per side | 0.5 vb = 1.6% | 16px = 1.6% | **100px = 9.77%** per side (19.5% total) |
| Tile path | `x/y 0.5, 31x31, rx 7` | `16, 992x992, rx 224` | **`x/y 104, 816x816, rx 181`** |
| Outer silhouette corner radius | 7/31 = 0.2258 | 0.2258 | **185/824 = 0.2245** (181 path radius + 4px outward half-stroke) vs Apple squircle ~185.4/824 = 0.2250 |
| Border stroke | 1 unit = 3.23% of tile | 26.6px = 3.23% (reads as a fat band) | **8px = 0.97% of tile** — 3.32x relative reduction; 4px at the 512 rep, 1px at 128, fades out at 32/16 as intended for a decorative hairline |

Quincunx composition preserved exactly: the five inner squares are the source geometry under a single affine map, scale `824/32 = 25.75`, translate `+100`.

- square size `7.4 → 190.55`; corner radius `1.5 → 38.63`
- positions `4.6 → 218.45`, `12.3 → 416.73`, `20 → 615`
- rotation pivots `8.3 → 313.73`, `16 → 512`, `23.7 → 710.28`
- rotations unchanged: `-3.5 / 3 / 3 / 2 / -2.5`
- colors unchanged: tile `#F0E9D8`, hairline `#D8CFBA`, corners `#4A3423 / #543C28 / #503927 / #46311F`, centre `#BC5A28`
- inner-square-to-tile-edge margin 118.45px on all four sides (symmetric); no shadow, no gradient, no added elements

## B2 — rasterization path chosen

**Chosen: sharp (libvips 8.18.3 / librsvg 2.62.90) already resident in `frontend/node_modules`, then `/usr/bin/iconutil`.**

Rejected alternatives, with reasons:

- `rsvg-convert`, `inkscape`, `magick`/`convert`, `cairosvg`, `resvg` — all absent (`command -v` returned MISSING for every one).
- `sips` — cannot rasterize SVG (raster/PDF only); used only as a verifier here.
- `qlmanage -t` — unreliable for SVG (per brief) and produces a thumbnail, not a controlled-size render.
- Electron/Chromium headless render — would work but needs an app harness plus screenshot plumbing for 10 sizes; strictly more machinery than a 30-line sharp script.
- electron-builder's own SVG→icns conversion — **explicitly forbidden**: it downloads a toolset from GitHub (`iconConverter.js`), violating the offline packaging posture (F-APP-1..5). A committed `.icns` bypasses that code path entirely.

`sharp` reliance is **transitive only** — `npm ls sharp` → `chirality-frontend → next@15.5.21 → sharp@0.35.3 overridden` (pinned by the existing `overrides` block). No dependency was added to `package.json`; the script header documents the caveat and the fallback instruction if a future `next` drops it. Rendering is in-process (no network); the only subprocess is Apple's `/usr/bin/iconutil`.

Each representation is rendered natively from the vector (librsvg `density = round(72 * size / 1024)`) and then pinned to exact pixel dimensions, so small reps stay crisp rather than being box-filtered down from 1024. The iconset is materialized in an `mkdtemp` directory and deleted after `iconutil` unless `--keep-iconset` is passed, so no intermediate PNGs enter the tree.

## Verification evidence

```
$ node ./scripts/generate-macos-icon.mjs --png-dir <scratch>/iconproof
rendered icon_16x16.png (16x16, 474 bytes) ... icon_512x512@2x.png (1024x1024, 38640 bytes)   [10/10]
wrote .../frontend/build/icon.icns

$ file build/icon.icns
build/icon.icns: Mac OS X icon, 140284 bytes, "ic12" type

$ iconutil -c iconset build/icon.icns -o /tmp/icns-rt/icon.iconset   # round-trip OK, 10 files
$ sips -g pixelWidth -g pixelHeight  (each extracted rep)
16/16, 32/32, 32/32, 64/64, 128/128, 256/256, 256/256, 512/512, 512/512, 1024/1024   # all 10 Apple-required entries, correct dims

$ shasum -a 256 build/icon.icns   (before and after a clean regenerate)
4b85b8f4c7a1a00069108ca808e04c666b4eadf6b2378d24b5a30a25412ff058
4b85b8f4c7a1a00069108ca808e04c666b4eadf6b2378d24b5a30a25412ff058   # byte-identical => deterministic

$ git check-ignore -v frontend/build/icon.icns   -> exit 1 (not ignored)  [was: .gitignore:46 **/build/]
$ git status --porcelain | grep package-lock     -> (empty)

$ npm run typecheck    -> PASS (tsc app + tsc -p tsconfig.electron.json)
$ npx vitest run       -> Test Files 130 passed | 1 skipped (131);  Tests 990 passed | 4 skipped (994)
```

**Visual verification (PNGs read and inspected at 1024, 128, 32):** correct palette; mark centred with symmetric transparent margin; squircle corners; hairline border reads as a hairline at 1024 and 128 (not a band) and correctly disappears at 32; quincunx legible at 32; no clipping at any edge; no aliasing artifacts or colour fringing; alpha background transparent outside the tile.

**Packaging leak check (B2 CHECK item):** `directories` declares only `output: "dist"`, so `buildResources` keeps its default `"build"` — i.e. `frontend/build/` is electron-builder's resource INPUT directory. `build.files` is an explicit allowlist (`dist-electron/**/*`, `.next/**/*`, `public/**/*`, `node_modules/**/*`, `!node_modules/@chirality/**`, `package.json`, `next.config.mjs`) and does not include `build/**`; electron-builder additionally excludes the buildResources directory from `files` by default. Nothing from `build/` can reach the asar. Confirmed `frontend/public/` contains exactly one file (`chirality-app-icon.svg`, 946 bytes), so B1 adds ~1 KB, no unintended payload.

## B3 — CLI launcher userData pinning

Resolved **entirely inside `cli-launcher.ts`** — `main.ts` needs no change. The module already imports `app` from `electron` and already calls `app.getPath('exe')` in `installBundledCliLauncher`, so `app.getPath('userData')` is available at the same call site (`main.ts:444` invokes `installBundledCliLauncher()` with no arguments; that stays valid).

Rendered launcher now contains, after `export ELECTRON_RUN_AS_NODE=1`:

```zsh
app_user_data='<app.getPath('userData')>'
...
if [[ -z "${CHIRALITY_USER_DATA:-}" ]]; then
  export CHIRALITY_USER_DATA="$app_user_data"
fi
```

Design choices:

- **Conditional, not unconditional, export.** Documented `chirality ...` commands now work as written (drill 7), while an externally supplied `CHIRALITY_USER_DATA` still wins — required so Stage V's isolated drills (temp userData) and any alternate-root run are not silently redirected at the app's real userData.
- `quoteForShell` + `path.resolve` reused for the new value, so quoting and absolute-path behavior match the existing two variables. `0700` file mode, `wx` temp-then-`rename` install, and the `daemon install --executable` branch are all unchanged.
- `runtime/packages/cli/src/config.ts` untouched: the generic default stays `~/Library/Application Support/Chirality`; the project-specific value is supplied by the frontend caller (D-GOV-20).

Shell-semantics smoke test (rendered template executed under `zsh`, exec lines stubbed to echo):

```
zsh -n                                          -> OK
no env set        -> CHIRALITY_USER_DATA=/Users/o'brien/Library/Application Support/chirality-frontend   (single quote round-trips)
CHIRALITY_USER_DATA=/tmp/isolated-userdata       -> CHIRALITY_USER_DATA=/tmp/isolated-userdata            (override respected)
daemon install     -> EXEC-B ... daemon install --executable <desktop_executable>                        (branch preserved)
```

## Integration points for Agent 1

1. **`frontend/.gitignore` is a declared-scope deviation and needs your ratification.** Root `.gitignore:45-46` has `build/` + `**/build/`, which ignored `frontend/build/` — the icns and its source SVG could not be committed at all. A nested `.gitignore` inside `build/` cannot fix this (git does not descend into an excluded directory), so the negation must live in an ancestor. I put a single scoped negation `!/build/` in `frontend/.gitignore` (with an explanatory comment) rather than editing the repo-root `.gitignore`, which is further outside Stage B's scope. Zero overlap with Stage A. If you prefer the root file, move it there; if you prefer neither, the commit needs `git add -f` and `frontend/build/` stays invisible to `git status` forever (not recommended).
2. **`renderCliLauncher` signature is now breaking:** `userDataDirectory: string` is required. The only production caller (`installBundledCliLauncher`, same file) is updated. If Stage A adds a second caller, `typecheck` will fail loudly — that is deliberate, so no caller can silently emit a launcher without the pin.
3. **Ordering dependency on Stage A's A6.** A6 makes `main.ts` honor `CHIRALITY_USER_DATA` via `app.setPath('userData', ...)`. That `setPath` must execute **before** `installBundledCliLauncher()` (currently `main.ts:444`), otherwise the launcher bakes in the pre-override path. A6's brief already places it "very early in electron/main.ts", so this should hold — please confirm the relative order at integration.
4. **No `main.ts` edit requested from Stage B.** Nothing for you to serialize on `frontend/electron/main.ts`.
5. `build.mac.icon` is set explicitly even though `buildResources` default `"build"` + default icon name `icon.icns` would likely resolve on its own. Explicit is per brief and removes reliance on electron-builder's default lookup.
6. **`desktop:pack` still owed** (Agent 1 / Stage V): confirms `Info.plist` `CFBundleIconFile`, the Finder/Dock icon (drill 5), and that the asar now carries `public/chirality-app-icon.svg` (drill 4). Stage B did not run it, per brief.

## Risks

- **Low — transitive `sharp`.** Regeneration (not the build) breaks if a future `next` stops pulling `sharp`. Mitigated: icns is committed, generation is byte-deterministic, script header records the fallback. No build-graph exposure.
- **Low — `!/build/` breadth.** The negation re-includes the whole directory, so if some future tool writes into `frontend/build/`, it will surface in `git status` instead of being silently ignored. Judged preferable to a per-file negation list; nothing currently writes there (the generator's iconset goes to `mkdtemp`).
- **Low — small-size hairline.** The 8px border resolves to 0.25px at the 32 rep and effectively vanishes. Intentional: the quincunx reads on its own at that size (verified visually) and a heavier border would coarsen the small reps. If the owner wants tile definition against light backgrounds at 16/32, the fix is a dedicated small-size rep, not a heavier stroke — out of scope, not proposed.
- **Low — `public/**/*` and route asymmetry.** B1 makes the file present in the asar; whether `shell-frame.tsx`'s `<img src="/chirality-app-icon.svg">` resolves in the packaged app depends on how Next static assets are served there. Packaged proof is drill 4 (Stage V). No code path in `frontend/src` was touched to accommodate it (out of Stage B scope).
- **None observed — regression surface.** Full vitest suite green at 990 passing; the only behavior change outside packaging config is the launcher's new conditional export.
