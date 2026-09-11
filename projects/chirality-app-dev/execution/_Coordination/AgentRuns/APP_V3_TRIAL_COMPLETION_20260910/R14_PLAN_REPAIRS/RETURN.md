# R14 plan repairs return

Source implemented, awaiting parent integration/review and one consolidated native retrial; no acceptance or publishing claimed.

- Added shared nativePlanText display projection; object `{type:plan,text}` yields exact Markdown, string and unknown structured legacy shapes remain inspectable. Raw events/revisions/hashes unchanged.
- Native Save plan uses origin-authorized Electron save dialog; returns project-relative target after containment and symlink checks. Runtime is sole writer, still exports with overwrite false first. 409 requires explicit native Replace confirmation; browser prompt/confirm fallback retained. Cancellation makes no export request and is visible.
- Successful plan-only turn with new persisted revision removes empty assistant placeholder. Failed/no-plan turns retain existing handling.
- New-chat role switch preserves model/reasoning choice while catalog validity continues to be checked. Role-specific text drafts remain separate.
- Turn basis and recorded instruction events remain available under one collapsed Turn details control. Parent owns separate footer cleanup.
- Applied parent-requested history integration: acceptedTurn.turnId or legacy turnId role lookup and attachment-only user transcript entries.

Validation: focused Vitest three files / 48 tests PASS: plan-export-dialog, chat-panel-folder-binding, chat-panel-model-selectors. Native dialog tests use temp directories and cover cancel, contained selection, outside-root/symlink rejection, unauthorized sender, overwrite cancel/accept. Component tests cover real native object shape, plan-only output, Execute/workflow Markdown, export cancel and conflict, model/role change. Existing Runtime native object export and revision3 test are baseline source and were not modified.

Write targets: frontend/src/components/shell/chat-panel.tsx; frontend/src/lib/harness/native-plan-text.ts; frontend/electron/{main.ts,preload.ts,plan-export-dialog.ts,plan-export-ipc-contract.ts}; frontend/src/types/chirality-window.d.ts; frontend/src/__tests__/lib/plan-export-dialog.test.ts; frontend/src/__tests__/components/{chat-panel-folder-binding.test.tsx,chat-panel-model-selectors.test.tsx}; this evidence folder.

Handoff: derivative repair evidence only, accepted upstream signed source basis above. Closure pending independent whole-tranche review and native consolidated trial (save dialog, actual file export, role change). No source commit/build/signing/native launch performed. Concurrent history changes may require Runtime contract build before global typecheck; parent owns integration.
