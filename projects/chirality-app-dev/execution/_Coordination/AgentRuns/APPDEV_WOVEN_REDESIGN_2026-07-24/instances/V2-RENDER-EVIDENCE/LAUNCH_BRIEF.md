# Sealed Brief — V2-RENDER-EVIDENCE (Agent 2, opus-5, D-APP-36 browser evidence)

**Parent:** HELP_HUMAN Agent 0, run `APPDEV_WOVEN_REDESIGN_2026-07-24`. **Write scope:** screenshot/evidence files under `instances/V2-RENDER-EVIDENCE/evidence/` in this run dir ONLY (plus your evidence log `EVIDENCE.md` there). Run the dev server for capture; stop it when done.

## Capture matrix (per D-APP-36: layout/overlap/interaction risk is high here)
Surfaces: (a) top bar incl. root-chip disclosure open; (b) navigator with session groups (expanded active + collapsed inactive); (c) dialogue + composer, INCLUDING the previously-overlapping empty state (prove the Stage C fix); (d) workbench with the Documents block; (e) pipeline; (f) coordination panel Work and Agents; (g) replay lens.
Themes: light AND dark (via the in-app control; also verify Auto follows OS).
Widths: 1440, 1180, 900 (the responsive breakpoints' neighborhoods).
Logo: close crop of the quincunx mark on light and dark bars (cream tile contrast on `--ground #171511` — round-3 note).
First-run state: capture the navigator with EMPTY per-mode session groups + populated "All sessions (N)" — this is the expected post-merge state under adopted D2 (no retroactive attribution), not a bug; label it as such in the log (round-4 note).

## Evidence log requirements (per `docs/ui/UI_POLISH_EXECUTION_PLAN.md`)
For every capture: route, viewport, theme, states exercised, outcome (OK / issue). Plus explicit lines for: brand `alt=""` decorative change (accessible name = wordmark text); `prefers-reduced-motion` honored on new animations (emulate and observe); AA contrast spot-checks for chip text on tints in both themes (report measured ratios for sage/rose/slate on their softs); keyboard walk of the navigator groups and theme control (focus visible, enter/space operable).

## Return
EVIDENCE.md path + file list, issues found (each classified blocking/cosmetic), overall verdict. Your final message is the return.
