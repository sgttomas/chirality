# Sealed Brief — A-TOKENS-CHROME (Agent 2, opus-5)

**Parent:** HELP_HUMAN Agent 0, run `APPDEV_WOVEN_REDESIGN_2026-07-24`. **Authority:** owner-adopted `../../ADOPTED_BRIEF.md` (read it first — §3 design spec, §4 verified constraints govern you). **Design reference:** `../../DESIGN_REFERENCE.html` (open/read the source; it is the approved mockup).

## Objective
Implement the calm-editorial light-first design system and compact top bar in the live frontend: (1) rewrite the token layer and styling of `src/app/globals.css` to ADOPTED_BRIEF §3.1 values and composition rules; (2) bundle IBM Plex via `next/font/local` (files already at `src/fonts/`); (3) recompose the `ShellFrame` brand header + Working Root card into one compact 48px top bar per §3.4 while keeping every existing control (root input, Apply Path, Choose Folder, Clear, active-root/error line, Runtime & credentials disclosure, PORTAL/WORKSPACE nav); (4) add the theme control (light/dark/system, default **light**, persisted as an additive field in the versioned woven workspace state — no schema-string bump).

## Write scope (exclusive ownership this stage — nothing else)
`frontend/src/app/globals.css` · `frontend/src/app/layout.tsx` · `frontend/src/components/shell/shell-frame.tsx` · `frontend/src/lib/woven-dialogue/woven-workspace-state.ts` (additive `theme` field only) · a new small theme module under `frontend/src/lib/` or `frontend/src/components/shell/` · tests: `frontend/src/__tests__/components/shell-frame.test.tsx`, `frontend/src/__tests__/lib/woven-workspace-state.test.ts`, plus NEW render tests for the recomposed bar + theme control.

## Hard constraints (violations = rejected return)
1. **Do not rename any existing CSS class or `data-*` attribute.** Restyle by changing rule bodies/values, not selectors. Never rename `--pane-handle-width`/`--pane-chat-width`/`--pane-file-tree-width` (exact-string test `lib/layout-state.test.ts:111-120`).
2. Light theme is `:root` default. Dark only under `:root[data-theme="dark"]`, and under `@media (prefers-color-scheme: dark)` only for `data-theme="system"`. Persisted default is `light`. Pre-hydration attribute stamp allowed via a tiny inline script in `layout.tsx` (guard all `window`/`matchMedia`/`localStorage` access — tests run in node env with none of them).
3. Every color in the file flows from the §3.1 tokens; no new hex outside the token blocks (existing non-token hex must be migrated to tokens or token-derived values). CTA styling per composition rules: filled emphasis = `--cta` only; `--accent` strokes/markers only; chips tinted-whisper.
4. Legacy shells/sidebar/portal markup: untouched. They inherit token values through shared classes — that is expected; do not restructure their rules beyond value changes.
5. `shell-frame.test.tsx` may be updated to match the recomposed markup, but the compat contract stays testable: an `<a href="/">` nav element must still exist; update assertions deliberately, never delete coverage. ADD render tests: Working Root controls (input/apply/choose/clear + error state) and theme control states incl. light default (D-APP-36 floor — these controls currently have zero coverage).
6. `woven-workspace-state.test.ts:39-58` exhaustive `toEqual` must be updated for the new `theme` field; keep schema string `chirality.woven-workspace/v1`; sanitize with fallback so stored v1 blobs load unchanged.
7. Fonts: wire `next/font/local` in `layout.tsx` with variables `--font-sans`, `--font-serif`, `--font-mono` (files in `src/fonts/`; weights: sans 400/400i/500/600/700, serif 400/400i/600, mono 400/500); replace the hardcoded `"IBM Plex …"` literals at `globals.css:30, 701, 996, 1205, 1306, 1681` with the variables (`--font-mono` is already referenced-but-undefined at four other sites — defining it fixes them).
8. The new logo tile: keep consuming `/chirality-app-icon.svg` via `<img>` (the asset is replaced by a sibling stage — do not create/modify the SVG yourself); size it for the 48px bar per the mockup (26px tile + wordmark "Chira*lity*" serif with italic accent em).
9. Do not touch: `src/lib/harness/**`, any component not listed, routes, query params, ARIA contracts, `[data-chat-input="primary"]`.

## Acceptance (run yourself from `frontend/`; report results)
`npm run typecheck` · `npx vitest run` (full, green) · `npm run build` (mandatory — sole CSS/font compile proof; ensure no dev server running). Return: summary of changes per file, test deltas (updated/added), gate outcomes, any deviation requests (do NOT exceed scope silently).
