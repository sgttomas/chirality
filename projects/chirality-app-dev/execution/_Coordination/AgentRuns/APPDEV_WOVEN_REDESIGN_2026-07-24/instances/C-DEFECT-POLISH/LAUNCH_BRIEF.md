# Sealed Brief — C-DEFECT-POLISH (Agent 2, opus-5)

**Parent:** HELP_HUMAN Agent 0, run `APPDEV_WOVEN_REDESIGN_2026-07-24`. **Authority:** `../../ADOPTED_BRIEF.md` §5 Stage C, §4 traps. **Dispatched after A, B1, B2 landed — read the branch diff first.**

## Objective
1. **Fix the composer overlap defect:** in the woven Dialogue surface at ~1280×720, the chat empty-state text ("Select a Working Root before starting a harness turn.", class `panel-empty`, `chat-panel.tsx`) overlaps the Attachments row/buttons in both themes. Diagnose in the browser (a dev-server run is permitted for diagnosis; STOP the server before any build), fix in `chat-panel.tsx` markup and/or a `/* Stage C */` section appended to `globals.css`. The empty-state string itself is unasserted (rewording allowed); the attachment chip `title` must appear exactly once; `chat-input-row` keeps its exact single className; Send stays a bare text label.
2. **Density/responsive pass:** verify the recomposed shell at 1180px and 860/900px breakpoints; adjust the responsive blocks for the new top bar/rail; keep `--pane-*` custom-property NAMES and `lib/shell/layout-state` constants untouched (exact-value tests).
3. **Reduced-motion + dark parity audit:** every new animation honors `prefers-reduced-motion`; sweep all new surfaces in dark theme for missed token pairs.
4. Render tests for the fixed empty-state arrangement (D-APP-36).
5. **Inherited styling debt (Agent 1 round-1 carry-forward):** the Workbench "Documents" block landed from Stage B1 as intentionally unstyled markup (`workbench-documents-*` class prefix, no CSS). Style it in your appended `/* Stage C */` section using existing tokens, consistent with the design reference's block treatment.

## Write scope
`src/components/shell/chat-panel.tsx` · appended `/* Stage C */` section of `globals.css` (edit existing rules ONLY where the overlap fix demands it — name each such rule in your return) · responsive/media-query blocks in `globals.css` · `src/__tests__/components/chat-panel-failed-send.test.ts` (only if unavoidable; prefer additive new test file).

## Hard constraints
The §4 trap list of the adopted brief binds you (exact-string tests, disabled-counts, bare labels, ARIA polarity). No new controls in permission cards, replay lens, work projection. No renames. Stop any dev server before `npm run build`.

## Acceptance
From `frontend/`: `npm run typecheck` && `npx vitest run` && `npm run build` all green. Return: per-file summary incl. every existing `globals.css` rule you edited, tests updated/added, gate outcomes, before/after screenshot paths if captured, deviations requested explicitly.
