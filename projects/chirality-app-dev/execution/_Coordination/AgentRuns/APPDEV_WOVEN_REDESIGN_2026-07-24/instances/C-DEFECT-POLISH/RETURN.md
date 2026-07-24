# RETURN — C-DEFECT-POLISH (Agent 2, opus-5), 2026-07-24

Full return in session transcript; condensed:

- **Overlap defect:** root cause was a grid-track defect (six positional rows vs state-dependent child count; transcript track collapsing to ~4px under notice load). Fix: new `chat-composer-dock` wrapper (4 fixed rows), dock capped `fit-content(38%)` with internal scroll, transcript block-padding moved to child margins. Browser-proven: zero overlapping pairs at every panel height 400→110px with all notices present.
- **globals.css:** ONE existing rule edited (`.woven-primary-dialogue > .panel--chat` grid-template-rows + `min-width:0` — named and justified); everything else in the appended `/* Stage C */` section (C1–C6). Token discipline maintained (zero hex below token blocks).
- **Responsive:** real 861–1180px clipping band found and fixed (composer controls/persona clipped at 900px; dialogue column 336→448px; rails relieved; rail headers wrap; top-bar squeeze order defined). Measured overflow list empty at 861/900/960/1180/1280. `--pane-*` and layout-state untouched.
- **Reduced motion:** whole-document `prefers-reduced-motion` policy added (stylesheet has exactly one transition, no keyframes). **Dark parity:** clean; two self-introduced AA misses fixed pre-landing.
- **Documents block styled** (B1 debt discharged): object-card provenance treatment, CSS-only, nested DocumentView de-boxed, dark/light verified.
- **Tests:** new additive `chat-panel-empty-state.test.ts` (4 structural tests); `chat-panel-failed-send.test.ts` untouched and green.
- **Gates:** typecheck PASS; vitest 129 files / 984 passed / 4 skipped; build PASS; diff contained (2 modified + 1 added).

**Escalation (accepted):** 15 pre-existing AA failures from Stage A/B2 `--ink-faint` uses at 9.6–12px functional labels (3.10–3.77:1), identical both themes — outside C's fence; routed to the Agent 1 integration owner (round 5) for a single-point token remedy.

**Deviations ratified by Agent 0:** (1) woven chat header compaction (h2 + meta visually hidden, a11y tree preserved; legacy verified unchanged; 109→37px returned to transcript) — RATIFIED as density decision inside adopted scope; (2) two `!important` declarations in ≤1180/≤900 media blocks to beat inline layout-state style, mirroring pre-existing pattern — RATIFIED; (3) no-screenshot-files note — V2 owns archived image evidence.

**Agent 1 validation:** see `../AGENT1-VALIDATOR/ROUND5_REVIEW.md`.
