# Sealed Brief — B2-NAV-SESSIONS (Agent 2, opus-5)

**Parent:** HELP_HUMAN Agent 0, run `APPDEV_WOVEN_REDESIGN_2026-07-24`. **Authority:** `../../ADOPTED_BRIEF.md` §3.4 (navigator behavior), §4 (verified session facts), §8-D2 (adopted default: client-side tag-forward). **Design reference:** `../../DESIGN_REFERENCE.html` (rail groups + session lists). **Dispatched after A and B1 landed — read their diffs' navigator/workspace-state shape first (git log/diff on the current branch).**

## Objective
Mode-scoped session history in the woven Navigator:
- Navigator modes Dialogue/Workbench/Pipeline become expandable groups; the ACTIVE mode expands, listing its recent recorded sessions (cap 4 + "All sessions (N)" affordance); inactive modes collapse. Live session marked distinctly (sage dot per design reference).
- **Attribution (adopted D2 default):** additive `sessionSurfaces` map (`sessionId → 'dialogue'|'workbench'|'pipeline'`) in the versioned woven workspace state (`chirality.woven-workspace/v1`, additive field, NO schema-string bump, sanitize-with-fallback, bounded size — evict oldest beyond ~500 entries). The shell records the active surface at session creation. Unattributed sessions appear only under "All sessions".
- Selecting a past session routes through the EXISTING `guardRecordedSessionSelection` → read-only replay lens path (same as Agents projection selection). Never resume/merge/mutate the live dialogue; disable selection while a turn is in flight exactly as the guard dictates.
- Navigator group-expansion state may persist as another additive workspace-state field.

## Write scope
`src/components/woven-dialogue/navigator.tsx` · `src/components/woven-dialogue/woven-dialogue-shell.tsx` (session-list plumbing + surface recording only) · `src/lib/woven-dialogue/woven-workspace-state.ts` (additive fields) · tests: `woven-dialogue-navigator.test.tsx`, `woven-workspace-state.test.ts`, the shell render test added by B1, plus NEW render tests for the session lists (expanded/collapsed/empty/loading/guarded states — D-APP-36 floor).

## Hard constraints
1. Session data comes from the existing `listHarnessSessions` flow already wired in the shell — no new API routes, no daemon/runtime changes, no `src/lib/harness/**` edits.
2. **ARIA polarity:** `aria-expanded`/`aria-pressed` only; `role="tab"`/`tablist` are FORBIDDEN in woven components (test-asserted). Keyboard operable; focus-visible states.
3. `woven-dialogue-navigator.test.tsx` runs with no providers: mock any new dependency there; keep the legacy-footer assertions green. Guard all `window`/`localStorage` access for node-env tests.
4. Do not add a "Resume"-style verb anywhere; the replay lens tests forbid those labels and require exactly one button in the lens — do not add controls to it.
5. No new CSS classes without need; if needed, prefix `rail-` / `navigator-` and add minimal rules ONLY in a clearly-marked `/* Stage B2 */` section at the END of `globals.css` using existing tokens (coordination ruling: appended section, never edits to existing rules).
6. Update `woven-workspace-state.test.ts` `toEqual` for new fields; migration/round-trip assertions stay coherent.
7. Untouched: routes/params, coordination panel, replay lens internals, legacy components, `[data-chat-input="primary"]`.

## Acceptance
From `frontend/`: `npm run typecheck` && `npx vitest run` full green. Return: per-file summary, tests updated/added, gate outcomes, deviations requested explicitly.
