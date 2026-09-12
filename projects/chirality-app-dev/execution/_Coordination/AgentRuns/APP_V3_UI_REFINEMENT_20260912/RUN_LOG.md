# RUN_LOG — APP_V3_UI_REFINEMENT_20260912

Owner directive (Ryan Tufts, 2026-09-12, in chat): implement twelve Chirality
App refinements (message distinction, single-action sign-in, compact
activity, streaming follow, account area, menu closing, Plan tab, update
discovery, account icon, search headings, workflow navigation
Core/Specialist/Project Specific, read-only Skills tab). Basis: main
19bca4930 (merge of PR #774). Branch: claude/chirality-ui-refinement-20260912.

Implementing session: Fable 5.1 (HELP_HUMAN posture, WORKING_ITEMS for this
package). Bounded Type 2 dispatches: Fable 5.1 medium. Independent source
review: fresh Fable 5.1 session without authorship.

| UTC | Entry |
|---|---|
| 2026-09-12T17:10Z | (Timestamp corrected from a mistaken 18:10Z; orientation preceded the 17:41Z entry below.) Orientation complete: four read-only Explore maps (conversation and Plan, account and menus, catalog layer, Electron and release). Findings recorded in WORK_GRAPH.md. Branch created from 19bca4930. |
| 2026-09-12T17:41Z | Implementation complete in the working tree. Dispatched TASK A (catalog navigation, briefs/TASK_A_CATALOG_NAVIGATION.md, return returns/TASK_A_RETURN.md) and TASK B (update discovery, briefs/TASK_B_APP_UPDATE.md, return returns/TASK_B_RETURN.md); both Fable 5.1 medium, no delegation. Session work (node C): messages, sign-in, activity, follow, account, menus, Plan tab, icon, headings, library view, Skills tab. Checks: frontend `npm run typecheck` PASS; frontend `npx vitest run` 2112 passed, 4 skipped, exit 0 (an earlier run showed the known Pi/oMLX wire load-only flake once); Runtime `npx vitest run` 317 of 318 passed, the one failure `app-owned-composition > settles a session a hard-killed service left running` is timing-sensitive under full-suite load and passed on two isolated reruns (daemon code untouched by this run). Fixed during testing: ChatPanel default-prop arrays were recreated per render and re-published the Plan model to its host on every render (hoisted to module constants). |
| 2026-09-12T17:45Z | Governance records written: tranche manifest docs/governance_harness/tranche_manifests/ROOT-WORKFLOW-NAVIGATION-20260912.yaml (approved_source_sha pinned to the basis for now, re-pinned before merge), notices to the Runtime and App loops (NOTICE_2026-09-12_ROOT_WORKFLOW_NAVIGATION.md), and the separate report PROMOTED_WORKFLOW_ASSUMPTIONS.md. APP-HOLD-1: no App deliverable target; owner-directed refinement, consistent with the prior run. Owner direction received mid-run: hold the packaged rebuild until additional items arrive; test as we go. |
