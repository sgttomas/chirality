# Sealed Brief — B1-IA-FOLD-LOGO (Agent 2, opus-5)

**Parent:** HELP_HUMAN Agent 0, run `APPDEV_WOVEN_REDESIGN_2026-07-24`. **Authority:** owner-adopted `../../ADOPTED_BRIEF.md` (read first; §3.3/§3.4 + §4 govern). **Design reference:** `../../DESIGN_REFERENCE.html`.

## Task 1 — Artifacts→Workbench fold
Remove "Artifacts" as a navigator surface and fold the deliverable-document reader into Workbench:
- `src/components/woven-dialogue/navigator.tsx`: remove `'document'` from `WovenSurface` union (line ~7-11) and the `{ id: 'document', label: 'Artifacts', … }` entry (~line 21); Workbench entry note becomes "Documents, evidence & contracts".
- `src/components/woven-dialogue/woven-dialogue-shell.tsx`: remove the `activeSurface === 'document'` focused-surface branch (~374-380). Keep `defaultSurface` prop contract otherwise identical.
- `src/components/woven-dialogue/dialogue-viewport.tsx`: remove `'document'` from `FocusedDialogueSurface['id']` union (line 6).
- `src/components/workbench/workbench-surface.tsx`: mount `DocumentView` (from `../shell/document-view`) as a new "Documents" block inside the surface (below existing blocks). Do NOT modify `document-view.tsx` itself.

**Test obligations (same stage):**
- `src/__tests__/components/woven-dialogue-viewport.test.tsx`: re-point the `id:'document'/title:'Artifacts'` fixture (~51-62) to `'workbench'`; keep `data-primary-dialogue-mounted` assertions (43-44) and the exactly-one-button expectation intact.
- `src/__tests__/components/workbench-surface.test.ts`: add `vi.mock('../../components/shell/document-view')` (unmocked it drags react-markdown ESM + fetch into node env). Keep every exact-string assertion passing: the exact `disabled=""` count of 4, the verbatim `<option>`/`<button type="submit" disabled="">Apply Transition</button>` strings (add NO className to those elements), and `not.toContain('Apply Transition')` in the read-only case (your mocked block must not emit that substring). Add assertions for the Documents block present/mocked.
- ADD a direct render test for `woven-dialogue-shell.tsx` (it has none; the route test mocks it entirely): mock heavy children; assert navigator surface list = dialogue/workbench/pipeline (no Artifacts), the workbench focused surface renders, and `data-woven-surface` behavior — D-APP-36 floor for the fold.
- `woven-dialogue-navigator.test.tsx` asserts only the legacy footer link — keep green.

## Task 2 — Logo assets (disjoint)
Replace `public/chirality-app-icon.svg` content with the quincunx mark (ADOPTED_BRIEF §3.3, exact geometry in DESIGN_REFERENCE.html's inline `<svg viewBox="0 0 32 32">`: cream tile `#F0E9D8` rx7 with `#D8CFBA` 1px stroke; five 7.4×7.4 rx1.5 squares at (4.6,4.6)/(20,4.6)/(12.3,12.3)/(4.6,20)/(20,20), fills `#4A3423`/`#543C28`/`#BC5A28` center/`#503927`/`#46311F`, rotations −3.5°/3°/3°/2°/−2.5° about their centers). Add `src/app/icon.svg` with the same mark (Next auto-favicon route; no `layout.tsx` change — that file is owned by a sibling stage; do not touch it, nor `shell-frame.tsx`).

## Hard constraints
Write scope = exactly the files above. Do not touch `globals.css`, `layout.tsx`, `shell-frame.tsx`, `src/lib/harness/**`, routes/query params, `document-view.tsx`, legacy components. Preserve `[data-chat-input="primary"]` queries in the shell file you edit. New markup uses existing class names where possible; if a new class is unavoidable, prefix `workbench-documents-*` and add NO styling (sibling stage owns CSS; plain markup must degrade acceptably).

## Acceptance (run from `frontend/`; report)
`npm run typecheck` (the union removals are type-level — this is the gate that catches stragglers) · `npx vitest run` full green. Return: per-file change summary, tests updated/added, gate outcomes, deviations requested explicitly.
