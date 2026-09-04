# 05 — Logo and Brand

## 1. Decision (SR-15, SR-16)

The Chirality mark is the owner's chalk-on-brick drawing, composed into a whole image: six chalk squares (four dark umber corners, a terracotta and a cream centre pair) on a warm brick-and-chalk ground, no border, no dark-ground variant. It is:

- the macOS app icon (Dock, Finder, DMG), in Apple's rounded-rectangle icon shape;
- the in-app mark wherever a mark is needed **outside the header** (About, first-run, empty states if any). The header itself carries only the wordmark (SR-11);
- the corporate logo, replacing `frontend/artifacts/logos/LOGO.jpg`.

The wordmark is **Chirality** in IBM Plex Serif Regular (400), one colour: `#3a2420` (the dark umber of the squares) on light grounds, `#e6dfd1` (cream) on dark grounds. In the app header the token `--brand-ink` (`#4a3423` light / `#e8e7e2` dark) is used instead so it sits with the Stone palette. Plex Serif Medium (500) is acceptable for the header at 18px; Semibold (600) exists only for signage and slides.

Rejected and not to be revived: the five-tile quincunx vector, the six-tile vector (plain, accent, greyscale), the bordered chalk variant, the greyscale chalk variant, the dark-ground chalk variant, the split `Chira`/`lity` wordmark.

## 2. Assets in this package (`assets/`)

| File | Size | What it is | Use |
|---|---|---|---|
| `painted-field-square-1024.png` | 1024², RGB | **Master.** The composed image, square, no corner rounding. | Source for every other file; corporate use where a square is wanted. |
| `painted-field-1024.png` | 1024², RGBA | Master with the macOS rounded-rectangle mask (corner radius 22.37% of side, drawn at 4× and downsampled). | App icon master; `src/app/icon.png` source. |
| `painted-field-256.png`, `-64`, `-32`, `-16` | RGBA | Lanczos downsamples of the rounded master. | Size checks; favicon-class uses. The 16px reads as six marks. |
| `painted-field.icns` | 3.8MB | Apple icon set built with `iconutil` from the rounded master at 16/32/128/256/512 and their @2x. | Replaces `frontend/build/icon.icns`. |
| `chirality-logo-lockup-400.png` | 3669×1024, RGBA | Rounded mark + "Chirality" Plex Serif 400, umber ink, transparent ground. | Corporate lockup, light backgrounds. |
| `chirality-logo-lockup-400-dark.png` | 3669×1024, RGBA | Same, cream ink. | Corporate lockup, dark backgrounds. |
| `chirality-logo-lockup-400.svg`, `-dark.svg` | 2.7MB each | Self-contained SVG: the mark embedded as PNG data URI, the wordmark converted to outline paths from the repo's own `frontend/src/fonts/` Plex Serif file. Renders identically without the font installed. | Print, web, documents. |

SHA-256 for each file is in `README.md` "Asset integrity".

Lockup geometry: wordmark cap height 0.56 × mark height, gap 0.26 × mark height, baseline aligned to the mark's optical centre. Keep these ratios if the lockup is ever re-rendered at another size.

## 3. The corporate logo folder (owner's machine)

`frontend/artifacts/logos/` is git-ignored (`.gitignore:53`), so **this package is the only tracked copy of the derived assets.** Since 2026-09-04 the folder holds the corporate set in two forms, icon-only and with the name:

| File | Form | Use |
|---|---|---|
| `LOGO-icon.png` | Icon only, rounded macOS icon shape, 1024² on transparent | App icon, avatars, favicons, anywhere a square-ish mark is wanted |
| `LOGO-mark.png` | Icon only, square, 1024², no rounding | Print and layouts that want the full square image |
| `LOGO.png`, `LOGO.svg` | Icon plus "Chirality", transparent | Corporate lockup on light grounds; the SVG is self-contained |
| `LOGO-dark.png`, `LOGO-dark.svg` | Icon plus "Chirality", cream ink, transparent | Corporate lockup on dark grounds |
| `LOGO.jpg` | Icon plus "Chirality", flattened on white | For anything that still expects a JPEG |
| `LOGO-source-photo.jpg` | The drawing photographed (746×609); formerly `LOGO.jpg` | Source. Do not regenerate from it without the owner; the composition was reviewed and chosen. |

Also in the folder, untouched: `1769814039333.jpeg`, `icon copy.png`, and photographs `IMG_1382`, `1402`, `1439`, `1449`, `1482`, `1483`, `1506.jpg`. The `assets/` folder of this package carries the same two forms: `painted-field-1024.png` (icon only, rounded), `painted-field-square-1024.png` (icon only, square), and the four `chirality-logo-lockup-400*` files (with the name).

## 4. How the mark was produced (reproducibility record)

Python 3 with Pillow and NumPy; no network; no model-generated pixels. Steps, so that `scripts/generate-macos-icon.mjs`'s requirement of a reproducible icns has a written basis even though the source is raster:

1. Load `LOGO.jpg`, EXIF-transposed, RGB. Target canvas N = 1024.
2. Scale the drawing to width 0.88 N, preserving aspect (height ≈ 0.72 N).
3. Build a ground texture from the drawing's own brick-and-chalk regions: five ground-only rectangles (in source pixels: (232,288,518,362), (220,62,318,248), (462,72,518,248), (236,110,314,240), (300,290,500,360)) are cleaned by pulling saturated or dark pixels toward the ground mean, then quilted over the full canvas as ~900 randomly flipped patches with feathered edges (inset 0.25 of patch, blur 0.18 of patch).
4. Paste the scaled drawing centred on the ground with a feathered mask (feather 3% of width, edge blur 2%), so its edges dissolve into the texture instead of cutting.
5. Rounded variant: mask with a rounded rectangle of radius 0.2237 × N, rendered at 4× and downsampled. (A superellipse n = 4.6 was tried and rejected as too square against real Dock icons.)
6. Downsamples by Lanczos; iconset naming per Apple; `iconutil -c icns`.
7. Lockup: Plex Serif 400 outlined with fontTools (`SVGPathPen` under `TransformPen(scale, 0, 0, -scale, x, 0)`), PNG text rendered by Pillow with the same font file; ink `(58,36,32)` light, `(230,223,209)` dark.

The scratch scripts were not kept. Anyone re-deriving should reproduce the steps above from `LOGO.jpg` and compare against the master's hash; a pixel-exact match is not expected because the quilting uses random patch placement, so compare visually and by the 16/32px renders.

## 5. Where each asset is applied in the product

| Product location | Today | Target | Tranche |
|---|---|---|---|
| Header | `public/chirality-app-icon.svg` + split wordmark | wordmark only | T2 |
| Next `metadata.icons` | `src/app/icon.svg` (file convention; DEL-02-01 record-only note) | `src/app/icon.png` from `painted-field-1024.png` at 512², delete `icon.svg` | T7 |
| macOS app icon | `build/icon.icns` from `build/icon-macos.svg` via `scripts/generate-macos-icon.mjs` | `build/icon.icns` ← `assets/painted-field.icns`; retire `icon-macos.svg`; update the script header (or the script) to state the raster source and this record, so the "reproducible from a committed source" promise is kept by committing `painted-field-1024.png` under `build/` | T7 |
| `public/chirality-app-icon.svg` | header tile | remove once `shell-frame.test.tsx` and any other reference is updated | T2 or T7 |
| About / first-run | none | rounded mark at 64px with the lockup ratios | T6 |
| DMG background, release pages | out of scope (F-APP-2) | — | — |

Any change to `build/icon.icns` is a DEL-09-04 packaging-integrity concern: regenerate whatever manifest or hash list pins it in the same PR, and note that Section 8 preservation is triggered by the `frontend/electron/**` changes that accompany T7, not by the icon bytes alone.

## 6. Cleanup (done 2026-09-04 on the owner's instruction)

`frontend/artifacts/logos/generated/` was reduced from 145 entries to the 19 below; the `LOGO*` files in §3 were written from them and the original photograph was renamed to `LOGO-source-photo.jpg`. Kept:

```
painted-field-square-1024.png  painted-field-1024.png  painted-field-{512,256,128,64,32,22,16}.png
painted-field.iconset/  painted-field.icns
chirality-logo-lockup-400{,-dark}.{png,svg}  chirality-logo-lockup-600{,-dark}.{png,svg}
```

Removed as superseded: `alt-window-*`, `chirality-icon-*`, `chirality-lockup*.svg`, `chirality-mark-*.svg`, `chirality-appicon-field6.svg`, `chirality-quincunx.*`, `chirality.icns`, `chirality.iconset`, `macos-*`, `painted-field-bordered-*`, `painted-field-dark-*`, `painted-field-grey-*`, `painted-grid-*`, `painted-window-*`, `quincunx-painted-*`.
