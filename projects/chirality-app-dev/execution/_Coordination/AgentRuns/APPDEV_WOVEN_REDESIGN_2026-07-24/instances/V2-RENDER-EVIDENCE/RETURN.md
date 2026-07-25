# RETURN — V2-RENDER-EVIDENCE (Agent 2, opus-5), 2026-07-24

**Verdict: PASS WITH ONE BLOCKING FINDING.** Evidence: `EVIDENCE.md` + `evidence/` (70 PNG + 10 JSON, ~25MB, DPR-2; every shipped frame passed a per-frame render-integrity gate after a mid-run dev-server disruption forced a full re-capture; all frames post-`#99552F` — round-6 contrast independently corroborated at 4.58 light / 4.61 dark rendered).

**Blocking F-1:** root-chip disclosure panel anchored `right:0` to the chip with `width:min(680px, calc(100vw - 2.4rem))` → left edge −56px at 900px viewport (threshold ≈ <955px); `Apply Path` half off-screen; labels truncated. → Round 7.

**Cosmetic:** F-2 composer placeholder clipped at 900; F-3 replay `Source` value wraps mid-token; F-4 "All sessions (N)" label does not invert when expanded (aria-expanded correct) — F-2/F-3 routed to round 7 CSS; F-4 recorded residual (component-label logic; not reopening navigator.tsx post-verification).

**Proven good:** target overlap defect fixed at all widths/states (0px gap, no overlap); top bar exactly 48px; zero horizontal overflow in all 48 matrix frames; chip AA measured (sage/rose/slate 5.54/5.29/6.05 light, 7.64/7.44/6.79 dark); `alt=""` decorative confirmed; reduced-motion honored (transitions neutralized); full keyboard walk incl. session-row → replay lens; focus-visible on every new control; Documents block correct; Auto follows OS both directions; legacy + deep-link routes load; first-run empty-groups state captured and labeled expected-under-D2.

**Caveats of record:** (1) no runtime daemon — session list/replay captured via declared fixture pass-through (`session/list`, `session/:id/events` only); replay transcript-item rendering unevidenced; unstubbed truth in `*-nostub.png`; (2) captures are DPR-2 (25MB) — retained as-is for authenticity; (3) `[data-legacy]` absent from real DOM at `?legacy=1` — pre-existing mock-only contract in `woven-dialogue-route.test.tsx` (sole `src` occurrence), recorded residual, not a tranche regression.
