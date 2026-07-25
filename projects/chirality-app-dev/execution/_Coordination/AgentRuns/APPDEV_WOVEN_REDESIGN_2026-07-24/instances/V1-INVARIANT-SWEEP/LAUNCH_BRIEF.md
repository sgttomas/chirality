# Sealed Brief — V1-INVARIANT-SWEEP (Agent 2, opus-5, adversarial, read-only + browser)

**Parent:** HELP_HUMAN Agent 0, run `APPDEV_WOVEN_REDESIGN_2026-07-24`. **Posture:** attempt to REFUTE the tranche's compliance claims; your value is in what you catch. **Write scope: NONE** (no file edits; you may run a dev server for click-through and must stop it when done).

## Sweep list (each item: verify against the live branch diff `git diff main`, and state PASS/FAIL with evidence)
1. **Hooks/contracts:** `[data-chat-input="primary"]` (both query sites + target); `data-primary-dialogue-mounted`; `data-woven-surface`; `data-work-class`/`data-replay-*`/`data-legacy`; ARIA: resize separators + value attrs, `aria-pressed` toggles, permission `alertdialog`, `aria-live`; `role="tab"` present in WorkspaceSidebar, absent in woven components.
2. **Routes/params:** `/`, `/chat`, `/workbench`, `/pipeline` render; `?agent=` persona selection works; `?legacy=1` opens legacy; unknown params tolerated. No route/API/SSE surface changed (diff-path audit: `src/app/api/**`, `src/lib/harness/**` byte-untouched vs main).
3. **Legacy click-through (round-3 note 1):** on `/?legacy=1`, click through the nested top-bar disclosures and confirm `Runtime & credentials` → RuntimeSettings AND ApiKeySettings are actually reachable/operable, not merely in the DOM; legacy loop/matrix/sidebar tabs function.
4. **Projection non-authority wording:** Work/Agents panel, Documents block, session lists — no wording implying approval/certification/issuance; draft/proposal/runtime evidence visually distinct from human-accepted truth (F-APP-2 + RQG §9 copy review).
5. **Replay-lens isolation:** selecting a recorded session from the new navigator lists opens the read-only lens; primary dialogue stays mounted; no draft/context transfer; exactly one button; forbidden verbs absent.
6. **Fence audit:** diff confined to `projects/chirality-app-dev/**`; nothing in `_DomainEngines/**`, `projects/chirality-piping/**`, `projects/pec/**`, root `runtime/**`.

## Return
Verdict per item + overall CONFIRMED/REFUTED(with items), evidence pointers (commands run, elements clicked). Your final message is the return.
