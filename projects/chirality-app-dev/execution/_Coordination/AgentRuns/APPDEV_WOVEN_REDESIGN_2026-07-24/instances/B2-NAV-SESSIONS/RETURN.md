# RETURN — B2-NAV-SESSIONS (Agent 2, opus-5), 2026-07-24

Full return in session transcript; condensed:

- **woven-workspace-state.ts:** additive v1 fields `sessionSurfaces` (bounded 500, first-attribution-wins, oldest-evicted) + `navigatorExpandedSurfaces`; sanitize-with-fallback readers; pure writers `recordWovenSessionSurface`/`toggleWovenNavigatorExpandedSurface`; schema string unchanged; insertion positions keep existing exact `JSON.stringify` write assertions.
- **navigator.tsx:** expandable mode groups (`aria-expanded`, chevron `aria-hidden`); ≤4 recent attributed sessions per group (`aria-pressed`, `disabled` in-flight, `data-session-id`); live sage dot (`role="img"` labeled); "All sessions (N)"; exported pure `buildNavigatorSessionGroups` + clock-free `formatSessionWhen`; `WovenSurface` now aliases the lib union; all new props optional; zero new runtime deps.
- **woven-dialogue-shell.tsx:** surface recorded at first appearance of a new `primarySessionId` (post-hydration, `activeSurfaceRef` = surface at creation); route-follows-expansion invariant; `onSelectSession={loadReplay}` — existing guarded replay path unchanged.
- **globals.css:** one EOF-appended `/* Stage B2 */` section (126 lines), existing tokens only.
- **Tests:** workspace-state 11→18, navigator 1→11 (legacy-footer untouched), shell 6→8. Suite 961→980 passed / 4 skipped; typecheck PASS; build PASS (extra insurance); `git diff --check` clean.

**Deviations ratified by Agent 0:** (1) "All sessions (N)" = total per Working Root, full recency list incl. unattributed — RATIFIED (only reading that honors the unattributed-only-under-All rule; visual difference from mockup's per-group counts flagged for owner at closeout); (2) `woven-navigator-*` CSS prefix — RATIFIED (fits existing namespace, avoids B1 test regex); (3) new fields survive project-scoped clear — RATIFIED (session ids globally unique; expansion is layout preference); (4) session label = persona, id via `data-session-id` — RATIFIED (records carry no title; canonical-evidence honesty); (5) route's group never left collapsed — RATIFIED.

**Agent 1 validation:** see `../AGENT1-VALIDATOR/ROUND4_REVIEW.md`.
