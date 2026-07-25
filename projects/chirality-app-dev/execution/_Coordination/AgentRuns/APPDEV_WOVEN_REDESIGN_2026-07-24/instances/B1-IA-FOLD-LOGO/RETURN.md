# RETURN — B1-IA-FOLD-LOGO (Agent 2, opus-5), 2026-07-24

Amendment v2 applied. Full return in session transcript; condensed:

**Task 1 (fold):** `'document'` removed from `WovenSurface` and `FocusedDialogueSurface` unions; Artifacts navigator entry removed (Workbench note → "Documents, evidence & contracts"); shell `document` branch + orphaned `DocumentView` import removed; `data-woven-surface={activeSurface}` added to `.woven-workspace` (deviation 1); Documents block (`workbench-card workbench-documents-block`, `aria-label="Documents"`) mounted last in `.workbench-layout` with real `DocumentView`; no CSS added.

**Task 2 (logo):** `public/chirality-app-icon.svg` replaced with the §3.3 quincunx mark (exact geometry); NEW `src/app/icon.svg` (auto-favicon). `layout.tsx`/`shell-frame.tsx` untouched.

**Tests:** viewport fixture re-pointed to `workbench`; workbench test + `vi.mock(document-view)` + 2 new tests; NEW `woven-dialogue-shell.test.tsx` (6 tests, mocks per amendment v2, `Navigator`/`DialogueViewport` real). All exact-string traps pass unchanged.

**Gates:** typecheck PASS; vitest full PASS — 128 files passed / 1 skipped, 952 passed / 4 skipped. No out-of-scope failures at run time.

**Deviations ratified by Agent 0:** (1) `data-woven-surface` on real shell — RATIFIED (aligns component with route-test contract; inert `data-*`); (2) `workbench-documents-block` class, unstyled — RATIFIED per brief prefix rule, styling debt owned by Stage C; (3) browser evidence deferred to Stage V — RATIFIED, V briefs must name the Documents block + new mark in both themes.

**Agent 1 validation:** see `../AGENT1-VALIDATOR/ROUND2_REVIEW.md`.
