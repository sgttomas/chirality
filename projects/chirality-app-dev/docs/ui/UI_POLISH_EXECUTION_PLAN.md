# UI Polish Acceptance Checklist

**Status:** Active evidence-routing checklist
**Applies to:** Chirality App shell and operator-facing UI changes

## Purpose and authority boundary

This checklist makes the UI-quality evidence requested by `docs/PRD.md` FR-006 repeatable. It routes
verification; it does not create product requirements, approve a design, issue a deliverable, or make a
release-readiness or professional claim. Product requirements remain in the authority corpus. The
current information architecture is governed by the completed loop-first design and its recorded
decisions, while the component/render evidence floor is governed by D-APP-36 and
`docs/ISSUE_READINESS_PROFILES.md` Section 4.

## Current source basis

- `docs/PRD.md` FR-006: calm, professional, dense-but-readable interface.
- `execution/_Coordination/_DECISIONS/D-APP-36_RULING_2026-06-21.md`: component/render evidence is
  required for UI/product deliverables.
- `docs/ISSUE_READINESS_PROFILES.md` Section 4: required controls, states, fallbacks, and error paths.
- `plans/DESIGN_2026-06-18_agent_orchestration_ui.md` and
  `plans/PLAN_2026-06-19_loop_first_pivot.md`: current loop-first shell, right sidebar, and tertiary
  surface design.
- Live `frontend/src/**` source and tests: implementation truth.

## Non-negotiable review conditions

- The live loop remains the primary operator surface and the right sidebar remains coherent with it.
- Tool Kit and other local UI state remain convenience controls, never project truth or a bypass of
  runtime governance.
- Dense layouts remain readable: labels, values, status, and primary actions are distinguishable
  without overlap, clipping, or hidden required controls.
- Loading, empty, disabled, error, streaming, interrupted, and completed states do not masquerade as
  one another.
- UI polish changes do not alter the public harness event contract, lifecycle semantics, permission
  plane, or in-flight-turn survival guarantees unless separately authorized.

## Surface checklist

| Surface | Review focus |
|---|---|
| Shell frame and loop shell | Clear hierarchy; stable primary action; no page-level overflow; sidebar collapse does not unmount or obscure the active turn. |
| Workspace sidebar and Tool Kit | Active tab and focus are visible; labels and values remain readable at supported widths; local settings are visibly non-authoritative where that distinction matters. |
| Chat and event stream | Operator, assistant, tool, permission, error, and terminal states remain distinguishable; long content wraps or scrolls locally. |
| File, document, and tertiary forms | Loading/empty/error states are explicit; controls remain reachable by keyboard; dense content retains local containment. |

## Accessibility and interaction checks

- Keyboard focus is visible and follows a usable order.
- Resize and collapse controls retain their documented keyboard behavior.
- Text and state indicators remain legible in the supported theme; color is not the only state signal.
- Motion is restrained and does not conceal state changes; reduced-motion behavior is respected where
  animation exists.

## Required evidence

1. Run component/render tests for changed user-facing controls, meaningful states, fallbacks, and error
   paths as required by D-APP-36. Logic-only tests do not prove visual acceptance.
2. For layout-, viewport-, resize-, overlay-, or interaction-sensitive changes, record browser or
   screenshot review with the route, viewport, states exercised, and outcome.
3. Run the behavior tests needed to prove that polish work did not change governed runtime behavior.
4. Record limitations and unresolved defects. Absence of a finding is not lifecycle issuance or release
   approval.

## Re-review triggers

Repeat the applicable checks when a change affects shell layout, sidebar placement, responsive widths,
typography or color tokens, focus behavior, loading/error states, streaming presentation, overlays, or
the set or placement of primary operator controls.
