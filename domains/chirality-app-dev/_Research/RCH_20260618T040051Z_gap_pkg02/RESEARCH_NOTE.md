# Research Note - PKG-02 Desktop Shell, Navigation, and Operator State: gap-to-issuance

Status: DERIVATIVE_RESEARCH_PACKET

## Question

For each PKG-02 deliverable (DEL-02-01..05): what does the Specification require, how complete is the LIVE implementation/tests vs that spec, and what concretely remains to advance IN_PROGRESS -> CHECKING -> ISSUED?

## Accepted Basis

Live execution tree + git HEAD of projects/chirality-app-dev. Retrieval snapshot SRCIDX_20260616T043733Z is STALE (discovery only). Live source under frontend/src; tests under frontend/src/__tests__; deliverable docs under execution/PKG-02_.../1_Working/DEL-02-0x/.

## Short Answer

PKG-02 runtime is SUBSTANTIAL-to-COMPLETE in the live tree and proven by an executed test suite (54/54 green across 10 targeted files), but ZERO of the 5 deliverables has been advanced past IN_PROGRESS. The dominant gap is process, not code: (1) no Evidence_*.md consolidation exists in any deliverable dir, and (2) UI requirements are verified at the logic-module/API-route layer with no React component-render tests, which several Spec verification clauses nominally call for. The IN_PROGRESS -> CHECKING -> ISSUED transition machinery exists and is tested (approvalSha-gated, HUMAN actor) but has never been exercised for PKG-02. No HARD FENCE and no AWAITING decision-register ruling blocks PKG-02.

## Evidence

Per-deliverable (see Evidence_Map.csv EV-01..EV-17; all load-bearing rows VerificationSource=LIVE_TREE):

- DEL-02-01 (Shell & Matrix Nav) — COMPLETE impl. agent-matrix.tsx:15-106 encodes the canonical 3x4 matrix (rows NORMATIVE/OPERATIVE/EVALUATIVE, cols GUIDING/APPLYING/JUDGING/REVIEWING), routing NORMATIVE+EVALUATIVE -> /workbench and OPERATIVE -> /pipeline, with coming-soon `*` labels visible. app-shell.tsx:51-52,367-380 provides header nav + usePathname active-route class. Routes /, /pipeline, /workbench all exist. navigation-intent.test.ts (3 tests, RUN green).
- DEL-02-02 (Workbench & Pipeline UX) — SUBSTANTIAL impl. pipeline-client.tsx:28-106 has DECOMP/PREP/TASK/AUDIT categories, '(coming soon)' for disabled options, TASK split selectors (agent vs scope), scope modes DELIVERABLES/KNOWLEDGE_TYPES. workbench-client.tsx:58-77,174-282 reads agent/row/column with defaults, consumes status+dependency contract APIs, gates lifecycle controls via canAgentTransitionLifecycle. task-scope-selection.test.ts (6 tests, RUN green) covers stale-selection reset (REQ-007/008).
- DEL-02-03 (File Tree & Scope Scan) — SUBSTANTIAL impl. file-tree-panel.tsx bounds depth (TREE_DEPTH=3), renders truncation marker, resets on root change, shows typed errors. REQ-005 skipped-directory filtering fully realized in filesystem.ts:7-13 (SKIP_DIRECTORY_NAMES = exactly .git/.next/node_modules/dist/dist-electron/out). tree-route.test.ts (3 tests, RUN green).
- DEL-02-04 (Toolkit & Local UI State) — SUBSTANTIAL impl. layout-state.ts:53-185 persists/sanitizes pane widths+collapse (key chirality.layout.v1), clamps, swallows write failures. layout-state.test.ts (5), harness-chat-draft.test.ts (9), harness-toolkit.test.ts (5) all RUN green. Drag/keyboard Home/End interaction is in app-shell but not render-tested.
- DEL-02-05 (API Key UI & Runtime Feedback) — SUBSTANTIAL impl. api-key-settings.tsx shows source ui/env/none without key material, encryption-unavailable warning, IPC bridge store/remove/status. api-key-storage.test.ts (5), api-key-ipc.test.ts (6, status precedence ui>env>none, fail-closed), harness-error-display.test.ts (8, typed errors -> title/message/nextStep) all RUN green.

Process state (EV-14..EV-16): all 5 _STATUS.md = IN_PROGRESS (set 2026-06-16 HUMAN); no 2_Checking/ dir; 3_Issued/ empty; no Evidence_*.md in any dir (only _run_records/TASK_RUN_*.md dated 2026-05-20/23, pre-implementation); Dependencies.csv populated. Lifecycle transition + approvalSha gating tested (lifecycle-status.test.ts, deliverable-contracts.test.ts) but never run for PKG-02.

## Interpretation

The brief's framing holds for PKG-02: runtime code is implemented and proven, yet no deliverable has been advanced through the formal CHECKING -> ISSUED lifecycle. The gap to issuance is uniform across all five: (a) assemble a per-deliverable Evidence_*.md mapping each REQ to the live module + the executed test that proves it; (b) obtain a ruling on whether the existing logic/API-route coverage satisfies the Spec's "UI test" clauses or whether component-render tests are a hard gate (AMD-01); (c) the human-gated CHECKING then ISSUED transitions (approvalSha-bearing). DEL-02-01 is the closest to issuance (most direct, fully-realized, lowest residual ambiguity).

## Caveats

- STALE retrieval snapshot (discovery only); load-bearing claims re-verified LIVE.
- No component-render test infra exists; UI-render judgments are :READ of the component + :RUN of adjacent logic, not :RUN of a rendered component.
- Ran 10 targeted test files (54/54 green), not the full repo suite.

## Open Questions

- OQ-01 (OPEN): Do Spec "UI test" clauses require component-render tests for CHECKING, or is logic/API coverage acceptable? Needs ORCHESTRATOR/human ruling.
- OQ-02 (RESOLVED): skipped-directory filtering confirmed in filesystem.ts.

## Handoff / Next Action

AMD-01 -> SCOPE_CHANGE/ORCHESTRATOR (acceptance-bar ruling). AMD-02 -> CHANGE/implementer (Evidence consolidation). Then human-gated CHECKING/ISSUED. No fence crossed; no register ruling blocks PKG-02.
