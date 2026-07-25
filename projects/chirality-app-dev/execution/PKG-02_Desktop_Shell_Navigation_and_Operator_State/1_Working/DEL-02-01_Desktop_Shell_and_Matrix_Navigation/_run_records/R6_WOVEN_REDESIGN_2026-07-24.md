# R6 Woven Dialogue Visual Redesign & IA Consolidation — DEL-02-01

- Date: 2026-07-24
- Run: `APPDEV_WOVEN_REDESIGN_2026-07-24`
- Basis: `TRB-APPDEV-WOVEN-REDESIGN-2026-07-24`
  (`execution/_Coordination/AgentRuns/APPDEV_WOVEN_REDESIGN_2026-07-24/ADOPTED_BRIEF.md`),
  adopted by the owner in-session 2026-07-24 with defaults D1–D4
  (`.../ORCHESTRATION_PLAN.md` §Adopted authority). Authority basis of record
  remains D-APP-74 / SCA-APP-004 (RULED 2026-07-23) and D-APP-36.
- Reconciliation scope: per adopted default D4, this record also reconciles the
  PR #323 Woven Dialogue implementation (merge `403f228f4`, implementation
  commit `7941722f6`, evidence
  `execution/_Coordination/AgentRuns/APPDEV_WOVEN_DIALOGUE_IMPLEMENTATION_2026-07-23/`)
  against this deliverable.
- Lifecycle effect: none. State remains `IN_PROGRESS`; `Authorization Basis`,
  `Directive`, and `Checking Approval SHA` are unchanged by this record.

## What landed for DEL-02-01

**PR #323 (merge `403f228f4`).** The Woven Dialogue shell became the default
composition for `/`, `/chat`, `/workbench`, and `/pipeline`: mounted primary
transcript and composer, Navigator, Work/Agents coordination panel, and
collapsible Activity Shelf. Existing query parameters continue to resolve, and
`?legacy=1` opens the preserved loop-first UI in a separate window so the
primary dialogue is never unmounted
(`.../APPDEV_WOVEN_DIALOGUE_IMPLEMENTATION_2026-07-23/PACKAGE_RETURNS.md`
§PKG-02 and §Integration return; `.../REVIEW.md`; `.../VALIDATION.md`).

**This tranche (branch `feat/woven-redesign`).**

| Commit | Content bearing on DEL-02-01 |
|---|---|
| `f29b27a1f` | Stage 0 — bundled IBM Plex latin woff2 faces + OFL license under `frontend/src/fonts/` (no runtime network) |
| `2afcd8474` | Stage A — calm-editorial light-first token layer in `globals.css`; `next/font/local` wiring in `layout.tsx`; ShellFrame recomposed into a single 48px top bar (logo tile, serif wordmark, surface identity, working-root chip disclosure, nav, theme control); new `theme-control.tsx` (Light/Dark/Auto, light default, `role="group"`/`aria-pressed`); guarded pre-paint theme stamp; every Working Root control preserved and newly render-covered |
| `b6c6784f3` | Stage B1 — quincunx mark replacing `public/chirality-app-icon.svg`; new `src/app/icon.svg` (Next file-convention favicon); `data-woven-surface` emitted by the real shell |
| `b17ab9d39` | Stage B2 — navigator recomposed as mode-scoped session history (expandable Dialogue/Workbench/Pipeline groups); new `woven-dialogue-shell.test.tsx` extended |
| `04d3b4f5f` | Stage C — composer-dock grid-track fix, 861–1180px responsive band, whole-document `prefers-reduced-motion` policy, dark-parity pass, Documents-block styling |
| `af52af478` | Round 6 — light `--accent` `#9C5730` → `#99552F` AA remedy (V1 adversarial find) |
| `787e18146` | Round 7 — root-chip disclosure clipping fix (861–1024px band) + V2 evidence archive |
| `1cfd3e293` | Merge of `main` into `feat/woven-redesign` (upstream PRs #324–#327; no file-level overlap) |

Compatibility and invariants were independently re-proven rather than assumed:
V1 returned **CONFIRMED 6/6** over the §4 hook/contract set, all routes and
query parameters, browser-proven legacy click-through (Runtime & credentials
panel operable behind the new nested disclosure; all 11 legacy tabs
functional), projection non-authority wording, live replay isolation, and a
fence audit showing all 47 changed paths inside
`projects/chirality-app-dev/**`
(`.../instances/V1-INVARIANT-SWEEP/RETURN.md`).

## Evidence pointers

- `execution/_Coordination/AgentRuns/APPDEV_WOVEN_REDESIGN_2026-07-24/instances/A-TOKENS-CHROME/RETURN.md`
  (Stage A return; 2 tests updated, 9 added; typecheck / vitest 961-4 / build PASS)
- `.../instances/AGENT1-VALIDATOR/ROUND3_REVIEW.md` (Stage A validation:
  token discipline exact at 3,185 lines; PORTAL contract verbatim;
  `[data-chat-input="primary"]` untouched; `--pane-*` intact)
- `.../instances/AGENT1-VALIDATOR/ROUND1_REVIEW.md` (item 3) and
  `.../ROUND3_REVIEW.md` (note 3) — `metadata.icons` file-convention
  substitution recorded
- `.../instances/V1-INVARIANT-SWEEP/RETURN.md` (invariant sweep, AA find,
  upstream-merge risk)
- `.../instances/V2-RENDER-EVIDENCE/EVIDENCE.md` + `.../evidence/` (70 PNG +
  10 JSON, DPR-2; `topbar-*`, `navigator-*`, `logo-*`, `legacy-*`,
  `route-*` frames at 900/1180/1440 in light and dark; top bar measured at
  exactly 48px; zero horizontal overflow in all 48 matrix frames)
- `.../instances/AGENT1-VALIDATOR/ROUND7_REVIEW.md` (V2 F-1 blocking
  disclosure-clipping fix, measured before/after)

## Residuals recorded in `_STATUS.md` `## Remaining`

1. Packaged Desktop smoke evidence for the redesigned shell — an SCA-APP-004
   handoff acceptance item that this tranche did not run (the packaging gate
   was untriggered: fonts live under `src/`, and swapping
   `public/chirality-app-icon.svg` changes no `build.files`/`extraResources`
   entry; ADOPTED_BRIEF §6).
2. The top-bar runtime-status dot reports working-root state, not daemon
   connectivity (Stage A deviation 4, ratified for this tranche only;
   `.../instances/A-TOKENS-CHROME/RETURN.md`, disposition in
   `.../AGENT1-VALIDATOR/ROUND3_REVIEW.md` note 4). A true
   runtime-connectivity indicator is owed.
3. `metadata.icons` is intentionally satisfied through the Next
   `src/app/icon.svg` file convention — record-only, no code owed.
4. `.icns` / electron-builder packaged app icon remains unshipped (adopted D3
   residual); cross-referenced to DEL-09-04.

## Other notes of record

- ADOPTED_BRIEF §4 cites a permission `role="alertdialog"`/`aria-modal`
  contract; the code deliberately uses `role="region"` (test-asserted
  `not.toContain('alertdialog')`) and `aria-modal` lives in
  `file-picker.tsx`. Brief-text defect only — both files untouched
  (`.../instances/V1-INVARIANT-SWEEP/RETURN.md`;
  `.../AGENT1-VALIDATOR/ROUND6_REVIEW.md`).
- §3.1 token-table deltas against the adopted brief: `--ink-faint` light
  `#786F5F` / dark `#8F8570` (round 5), `--accent` light `#99552F` (round 6),
  undeclared derived `--shade` dark `#060504` (Stage A)
  (`.../AGENT1-VALIDATOR/ROUND5_REVIEW.md`, `.../ROUND6_REVIEW.md`).
- All gate figures cited above were measured before the `1cfd3e293` upstream
  merge; the authoritative post-merge full-gate run is owned by Agent 0 at
  closeout (`.../AGENT1-VALIDATOR/ROUND6_REVIEW.md`, `.../ROUND7_REVIEW.md`).
