# RETURN — A-TOKENS-CHROME (Agent 2, opus-5), 2026-07-24

Amendment v2 applied (`--font-display` alias emitted and driving display roles; theme module fully guarded, no `matchMedia` — `system` resolves in CSS). Full return in session transcript; condensed:

- **globals.css 2925→3185:** §3.1 token layer (light `:root` default + `color-scheme: light`; dark only under `[data-theme="dark"]` and `@media dark + [data-theme="system"]`); all legacy token references migrated; zero hex/rgba outside token blocks (ANSI palette, badges, overlays, shadows all tokenized; derived `--*-ink` chip-text tokens for AA ≈5.5:1); composition rules enforced (buttons fill `--cta`; `--accent` strokes-only; running badge → slate); compact top-bar section; old component-level dark-override block deleted; font literals → variables at all 6 sites (+4 previously-undefined `--font-mono` sites now resolve).
- **layout.tsx:** three `next/font/local` faces from `src/fonts/` exposing `--font-sans/serif/mono`; `data-theme="light"` + guarded pre-paint stamp script; 10 woff2 confirmed in build output.
- **shell-frame.tsx:** single 48px bar (logo tile + serif wordmark, kicker/surface/subtitle, root-chip disclosure + nav + theme control); every Working Root control preserved; PORTAL `<a href="/">` contract and exact classes unchanged.
- **theme-control.tsx (new):** Light/Dark/Auto, `role="group"`/`aria-pressed`, guarded persistence helpers.
- **woven-workspace-state.ts:** additive `theme` field under unchanged v1 schema; stored-blob compatibility kept.
- **Tests:** 2 updated (defaults `toEqual` + shell-frame restructure keeping original PORTAL assertions verbatim), 9 added (theme defaults/fallback/persistence/stale-snapshot; root-controls-in-disclosure; chip states; theme control states).
- **Gates:** typecheck PASS; vitest full PASS 128 files / 961 passed / 4 skipped; `npm run build` PASS (no dev server).

**Deviations ratified by Agent 0:** (1) theme-preserving merge in state writer + dedicated theme writer — RATIFIED (prevents silent theme revert by whole-object rewrites; test-covered); (2) grouped-selector split, no renames — RATIFIED; (3) compact bar on both variants — RATIFIED under §2 shared-chrome exception (legacy settings now behind disclosure, still in DOM, tests green; V1 confirms legacy functional); (4) status dot = working-root state, not daemon connectivity — RATIFIED for this tranche; "true runtime-connectivity indicator in top bar" recorded as named residual for closeout; (5) `.shell-brand-meta` wrapper dropped — RATIFIED; (6) consumed committed B1 logo asset — noted.

**Agent 1 validation:** see `../AGENT1-VALIDATOR/ROUND3_REVIEW.md`.
