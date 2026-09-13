# Native App F1/F2 repair return

TASK Type 2 native_app_author; delegated-harness-native, parent /root, no delegation. Model inherited from the original campaign assignment (gpt-6-astra medium). Bounded repairs to independent review F1/F2 at candidate `4031c6c54f76760baaaf3d92e2db83819ce3a8ac`. Source changes and focused checks complete; independent re-review remains required. No live account/UI/model/supplier operation, build, Git mutation, or governed acceptance was performed. This is derivative engineering evidence, not authority acceptance.

## F1

A single shared classifier now recognizes the exact five approval methods supported by Runtime, including `execCommandApproval` and `applyPatchApproval`. The live request reader uses that classifier before its answerable-kind filter; inline and attention subscribers therefore receive the same actionable rows. Native permission events remain suppressed from the old fallback component, preserving one actionable card. Tests cover both legacy methods through inline LiveSessionRequests and the real attention observer/dialog, exactly one Approve control, owner-session answer payload, and removal after resolution.

## F2

Check delivery is now a visible action for every unresolved steering receipt. It sends only the retained original operation ID and expected Runtime turn ID to the new receipt-only API; it never invokes the original steering submission route or sends the original text. Runtime owns evidence matching, immutable receipt recording, and the absence-of-evidence verdict. Accepted receipt clears only a matching current draft and updates the existing recorded steering message; unknown stays explicit and never enables resending the same unknown text. The action remains available after turn completion and renderer reload.

The App retains full original operation identity before its first browser request, including the network-before-server-intent case. A bounded session's local receipt records recover identity only; their status is treated as unknown after reload unless canonical steering events establish accepted/rejected. Canonical events can recover receipt identity without local state. Multiple operations retain their separate identities, so a newer update does not erase an earlier unresolved Check delivery action. Local storage writes do not substitute for native receipt evidence.

Parent selected the dedicated receipt-only endpoint after source inspection confirmed that repeating the original POST with a missing journal intent could newly dispatch. native_protocol_mapping owns Runtime `SessionSteerReceiptRequest {operationId, expectedTurnId}`, `sessionTurnSteerReceipt`, receipt route and manager; cross_folder_diagnosis owns the App port interface, unavailable fallback, session router classification, and concrete adapter. Their corresponding source changes are integration dependencies, not this child's edits. This child owns the App API/client, UI, and fake-port fixture additions.

## Validation

- APP-HOLD reliance: entry APP_V3_USER_JOURNEYS_20260912:NATIVE_APP_F1_F2_REPAIR; targets DEL-02-01, DEL-02-02, DEL-02-04, DEL-03-03; ALLOW, all CLEAR/NOT_HELD, HEAD 4031c6c54f76760baaaf3d92e2db83819ce3a8ac. Register d289b248a900122b012ae540b9b197feae3adbe264bf181f3d46556c500f320c; scan 0954ed105705301ccab40f3b6bcaed1fce542bc4f961055d40cc121b91b5dc29.
- Frontend `tsc --noEmit --incremental false`: PASS against emitted additive Runtime contracts/client.
- Focused repair suites: chat-panel-turn-attach, live-session-requests, daemon-proxy-boundary — 52 PASS. Covers late unknown receipt acceptance, unchanged original IDs, no repeated steering dispatch, lost request before journal intent, local identity recovery after reload and turn completion, absent evidence remaining unknown, durable-event identity recovery, and receipt-only proxy routing.
- Adjacent focused suites: chat-panel-folder-binding, request-card, harness-event-views-codex, runtime-daemon-harness-port — 93 PASS. Existing folder-binding test emits its known `act(async)` warning; assertions pass.
- Scoped `git diff --check`: PASS.
- Runtime author's separate return records receipt-only no-prior/no-dispatch, idle/recreated manager late/no echo, explicit rejection, and route/schema tests. These are separate evidence, not tests executed by this App child.

## Handoff

App F1/F2 source frozen; no remaining local blocker. Parent integrates Runtime/port dependencies, independently re-reviews the actual repaired candidate and performs native journeys. No acceptance pointer moved. Source checks do not qualify native UI delivery or release. Original NATIVE_APP_IMPLEMENTATION.md remains historical for the preceding candidate; this repair return describes the subsequent bytes.

## Exact files changed by this child in F1/F2

Relative to projects/chirality-app-dev/frontend:

- `src/components/shell/chat-panel.tsx` — `feec734bbdc1f2fd79aa38226bda5367bad336f5df4b32c610c13ba972dea481`
- `src/components/shell/request-card.tsx` — `10e25874473f3aedde49eb8991eecf75ab649bd7191ae60a3954da6dceb12c6a`
- `src/lib/shell/harness-event-views.ts` — `3692a54b114fbedd789b67173065ee97e3c0f464155aab47f7440a38b99d25a7`
- `src/lib/shell/steering-receipts.ts` — `d4612ea9c6ede7375e55ab64859909e4091cd04a3c6923774604f83f3bd811e7`
- `src/lib/harness/client.ts` — `e25749ae8e4410e45cbb0d6d0b69a81ec66c835760cbd8f300f8ca5f32b0a838`
- `src/app/api/harness/session/[id]/turn/steer/receipt/route.ts` — `db982085d98afbee6c04cf4390de6cd438bb2eae61e2606d53a97f042eb101de`
- `src/__tests__/components/chat-panel-turn-attach.test.tsx` — `82cfd95a35faa155ecbf88361d10e419dce22f31e7ceeacddca1482a39961d3e`
- `src/__tests__/components/live-session-requests.test.tsx` — `79ed2b279a43a8bca1ef8bed33e9d1a4aa2411fa1c84d32a85b7795d6c4e160b`
- `src/__tests__/api/harness/daemon-proxy-boundary.test.ts` — `de9196f4711844ed4e653a6e238e0fb50b595811de0f3a5bf964f519af8cfc8c`
- `src/__tests__/api/harness/fake-daemon-harness-port.ts` — `bef122e27f9b2441cde4c285f3dced3480f77dc8a742edcf83f77c3113cca573`
- `src/__tests__/api/harness/turn-route-attachments.test.ts` — `8963e9efaaf24413f88cc819cc51fd3d4f50a6157f1cbdadf73795b8bcfde78a`

Review basis SHA-256: `66eb07887415bb187888c9937bd01c41077ba72ac9bdb39ab18a2e4a04f73d5d`.
