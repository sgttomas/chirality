# Evidence ADQ-13 - PKG-02 UI Specs And Render Tests

## Scope

ADQ-13 reconciles PKG-02 local deliverable kit wording against the accepted loop-first app state and applies the D-APP-36 / AMD-01 component-render evidence bar.

In scope:

- DEL-02-01 route/layout wording for primary header Portal, right-sidebar tertiary Workbench/Pipeline, preserved `/workbench` and `/pipeline` deep links, matrix launch semantics, and stable launch keys.
- DEL-02-02 Workbench/Pipeline selector wording for loop-first matrix behavior, lifecycle-control actor support, approval-SHA gating, Pipeline category visibility, TASK split selectors, and contract-boundary evidence.
- Focused React render tests using the project's existing `renderToStaticMarkup` component-test pattern.

Out of scope:

- `_STATUS.md` lifecycle transitions, issuance, dependency satisfaction, release/distribution posture, provider expansion, R7 implementation, professional approval, certification, sealing, authentication, code-compliance acceptance, or release-readiness claims.
- Resolving SOW-007 ownership overlap with PKG-08, package-path mismatch warnings, or PRD hash/source-pointer warnings.

## Accepted Basis

- D-APP-28/D-APP-30/D-APP-31/D-APP-32: loop-first app state with the live loop primary, sidebar-right tertiary surfaces, in-place persona launches, Pipeline as the operative surface, and preserved routes.
- D-APP-36: UI/product deliverables require component-level render tests for user-facing controls, state, and disabled/active behavior. Browser screenshots are required only where layout or interaction risk is high or component tests cannot cover the expectation.

## Document Reconciliation

- `DEL-02-01/Specification.md`, `Procedure.md`, and `Guidance.md` now distinguish primary header navigation from sidebar/deep-link tertiary forms.
- `DEL-02-01` records implementation evidence for `agent`, `row`, `column`, `category`, `taskScopeMode`, `scopeKey`, and `pkg::deliverable` identity keys without treating older source warnings as resolved.
- `DEL-02-02/Specification.md`, `Procedure.md`, and `Guidance.md` now reflect loop-first matrix behavior and name `frontend/src/lib/workspace/deliverable-api.ts` `canAgentTransitionLifecycle` as the current implementation source for Workbench lifecycle-control actor support.
- `DEL-02-01/MEMORY.md` and `DEL-02-02/MEMORY.md` record the ADQ-13 evidence update while preserving all lifecycle and release-boundary disclaimers.

## Render Evidence Added

| Test | Coverage |
|---|---|
| `frontend/src/__tests__/components/loop-tertiary-routes.test.ts` | `/workbench` and `/pipeline` route clients instantiate `LoopTertiaryShell` with matching default sidebar tabs. |
| `frontend/src/__tests__/components/workspace-sidebar.test.ts` | `SidebarRightLoopLayout` keeps primary loop content mounted while a tertiary tab owns the right sidebar. |
| `frontend/src/__tests__/components/agent-matrix-panel.test.ts` | Matrix copy, streaming disabled state, and stable `pkg::deliverable` deliverable launch rows. |
| `frontend/src/__tests__/components/workbench-surface.test.ts` | Unsupported Workbench agents render read-only; human-gated lifecycle targets require approval SHA and lock actor choice to HUMAN; non-human-gated targets keep approval SHA optional. |
| `frontend/src/__tests__/components/pipeline-surface.test.ts` | Pipeline renders `DECOMP`, `PREP`, `TASK`, and `AUDIT`, TASK split selectors, disabled coming-soon options, and unavailable `KNOWLEDGE_TYPES` state. |

Browser screenshots were not run for ADQ-13 because the tranche did not change CSS geometry or browser-only interaction behavior; the AMD-01 expectations for user-facing controls, state, disabled behavior, and route wrapper defaults are covered by component render tests.

## Validation

- 2026-06-21 focused component tests: `npm run test -- src/__tests__/components/agent-matrix-panel.test.ts src/__tests__/components/workspace-sidebar.test.ts src/__tests__/components/loop-tertiary-routes.test.ts src/__tests__/components/workbench-surface.test.ts src/__tests__/components/pipeline-surface.test.ts --testTimeout=15000` passed (5 files / 11 tests).
- 2026-06-21 typecheck: `npm run typecheck` passed.
- 2026-06-21 full frontend suite: `npm run test -- --testTimeout=15000` passed (76 files / 520 tests).
- 2026-06-21 production build: `npm run build` passed; Next prerendered 23 static pages and Electron TypeScript build passed.
- 2026-06-21 repository diff hygiene: `git diff --check` passed.
- 2026-06-21 D-APP-38 authority-corpus status: `python3 execution/_Reconciliation/References/reconcile_authority_corpus.py status` reported corpus `v1` with no drift.
