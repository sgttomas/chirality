# Agent 1 Validator — Round 7 (V2 remediation), 2026-07-24

**Bounded integration-owner edit.** Single EOF-appended `/* Round 7 */` globals.css section (zero deletions); gates re-run green (typecheck / vitest 984-4 / build); token + `--pane-*` discipline intact.

- **F-1 (blocking) FIXED:** root cause = panel right edge tracks the chip (fixed 276px viewport inset), clipping below 974.4px. Fix: 861–1024px band moves the containing block to the whole top bar (`.shell-header relative; .shell-root-disclosure static; .working-root-bar left/right 0`). Measured: BEFORE reproduces V2's rects exactly (−56px @900); AFTER panel left = page margin 18.4px and right 18.4px inside viewport at 1024/955/900/861; >1024 and ≤860 behaviors unchanged. Note-1 headroom (band top 1024 vs 974 threshold) ACCEPTED by Agent 0 — margin over a fixed-inset assumption beats a zero-margin band; the 976–1024 full-width panel presentation is harmless.
- **F-2 FIXED:** `.chat-input-row input { text-overflow: ellipsis }`.
- **F-3 MITIGATED with corrected diagnosis:** V2's proposed `overflow-wrap:anywhere` was already present (and is what permits the mid-token break); implemented the alternative — provenance label track `minmax(4.5rem, max-content)` freeing ~2.5rem to the value; backstop retained; worst case = unchanged cosmetic wrap, never overflow. Visual confirmation delegated to V2 delta re-shoot.
- **F-4 untouched** per instruction (residual).

**Agent 0 dispositions:** round 7 committed with the final V2 evidence set; V2 tasked with a delta re-shoot (topbar/dialogue @900 both themes; replay provenance) on the post-merge tree; carried residuals unchanged; authoritative post-merge full-gate run owned by Agent 0 at closeout.
