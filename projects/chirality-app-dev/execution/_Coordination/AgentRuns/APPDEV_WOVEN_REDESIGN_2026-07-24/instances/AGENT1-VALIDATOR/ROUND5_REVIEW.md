# Agent 1 Validator — Round 5 (Stage C validation + AA remedy as integration owner), 2026-07-24

**PART 1 — Stage C: ACCEPT-WITH-NOTES.** Validator-reproduced gates on C's diff: vitest 129 files / 984 passed / 4 skipped; typecheck PASS; build PASS. Containment exact (3 files); the whole `globals.css` diff contains exactly ONE deletion line — the named `grid-template-rows` rule — plus pure additions and the EOF append; grid-track-defect justification confirmed (non-additive property, uncorrectable from lower cascade). Trap sweep fully intact (`chat-panel-failed-send.test.ts` untouched; exact `chat-input-row`; `[data-chat-input="primary"]`; bare Send label; attachment-title-once; aria-live/status; PermissionRequests verbatim). Header compaction uses the visually-hidden idiom (a11y tree preserved), scoped so legacy shells are unreachable. Token discipline holds at 3,682 lines. Notes: the new 4-test file asserts the four-row invariant the fix depends on (real regression guard); first `:has()` usage in the stylesheet (fine for Electron/Chromium target); V2 owns archived screenshots and must also cover the styled Documents block + compacted header.

**PART 2 — AA remedy implemented (bounded authorization).** All escalated sites resolve on ground/surface/card (none on tints) → single-point token change sufficient; no site relocation needed. Shipped (HLS-preserving, minimal lightness step):
- `--ink-faint` light `#948B79` → **`#786F5F`**; dark `#79715F` → **`#8F8570`** (all three declaration sites incl. the system-media duplicate).
Measured after: all **16** sites (count corrected from C's "15") clear 4.55–5.00:1 both themes; token vs ground/surface/card = 4.55/4.75/4.87 light, 5.00/4.77/4.56 dark; three-tier ink hierarchy preserved; `--ink`/`--ink-soft` untouched. Gates after edit: vitest 984 / typecheck / build all green. Files touched: `globals.css` token declarations only; hex containment still exact.

**§3.1 table deltas for closeout:** (1) `--ink-faint` light `#786F5F`; (2) `--ink-faint` dark `#8F8570`; (3) `--shade: #060504` dark (Stage A, round-3 note).

**Notes → dispositions (Agent 0):** stale rationale figures in two C comments (`globals.css:3387`, `:3638`) — cosmetic, recorded as residual; V2 evidence must be captured post-remedy (V2 dispatched after this round's commit); carried-open items unchanged (metadata.icons record, dot residual, All-sessions divergence, first-run empty state).

**Agent 0 disposition:** Stage C + Round-5 AA remedy integrated and committed together on `feat/woven-redesign`.
