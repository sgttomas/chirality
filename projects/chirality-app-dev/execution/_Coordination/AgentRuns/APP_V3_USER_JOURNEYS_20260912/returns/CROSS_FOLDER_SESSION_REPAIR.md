# Cross-folder session routing repair

Status: implemented; focused checks pass; parent live browser recheck and fresh independent full-diff review remain. TASK / Type 2; actual dispatch gpt-6-astra, medium, explicit no-history-fork dispatch. No delegation. Parent-authorized bounded repair; no Runtime, UI component, instruction, Electron, packaging, authentication, or live operational changes. Existing native steering additions preserved.

## Changes

All product changes are inside `projects/chirality-app-dev/frontend/`:

- `src/lib/runtime-client/daemon-harness-port.ts`: retain verified per-root ports and project identity; expose a routing facade covering every interface method. Session operations use immutable learned ownership or verified owner discovery, never the currently selected folder. Create/list results establish ownership; uncached native-child/history sessions use scoped lookup, with authorized Runtime owner recovery when needed after restart. Root operations select the retained root port. Existing per-project adapters continue enforcing authorization and containment. Signals propagate into lookup and execution. Current selection survives independently from retained bindings.
- `src/lib/runtime-client/runtime-daemon-harness-port.ts`: retain verified hosted bindings by root; old-root bind/status and account reads revalidate their own binding. Existing latest-selection race rejection remains, while a separately verified superseded root is retained for subsequent explicit root requests. Recovery uses Runtime's existing authorized session-owner lookup, verifies the project through launch and project-scoped clients, and confirms the session through the scoped port. Rebinding cannot change a retained root's project identity.
- `src/__tests__/lib/runtime-daemon-harness-port.test.ts`: revise obsolete old-root-conflict expectation and add an actual registry + project-scoped ports + HTTP turn/steering regression. Test A turn, B turn, A correction, old A replay/state/stream/requests/answer/steering/Stop, uncached A child, old-root create/list/status, failure/drift preservation, missing session, and registry restart with B selected and A history restored authoritatively. Existing out-of-order initialization test now checks retained A usability after B wins selection.
- Corrected diagnosis dispatch attribution as requested.

No HTTP endpoint, client request shape, Runtime session store, token policy, or UI changes were needed.

## Checks

APP-HOLD-1: `python3 execution/_Scripts/app_hold.py check --operation dispatch --entry-path APP_V3_USER_JOURNEYS_20260912:CROSS_FOLDER_SESSION_REPAIR --target DEL-03-01`, from App root: ALLOW; target CLEAR / NOT_HELD, no active holds. Register SHA-256 `d289b248a900122b012ae540b9b197feae3adbe264bf181f3d46556c500f320c`; scan `350872de553b81ba726bca5d8bcff1e105e8b5bd7407bdec15bb8e9f08cdeffe`.

- `npx vitest run src/__tests__/lib/runtime-daemon-harness-port.test.ts src/__tests__/api/harness`: PASS, 11 files / 105 tests.
- `npm run typecheck`: PASS (frontend and Electron TypeScript).
- Final test-only assertions added for old-root creation and post-recovery list/state; reran `npx vitest run src/__tests__/lib/runtime-daemon-harness-port.test.ts`: PASS, 31 tests.

Tests use isolated temporary fake project fixtures and fake RuntimeClients. No live account, profile, token, event, session store or supplier operation was performed. No build or Git mutation performed. Read-only source comparison was used during diagnosis; this is not a claim of release or whole-candidate acceptance.

## Handoff

Parent owns integrated browser repeat and fresh independent review. Re-run J02/J03 with the integrated source loaded into a fresh server process so process-global route objects cannot retain earlier hot-reload closures. Confirm both origins' subsequent turns, old-folder replay and attention/Stop routing. Existing manifest drift and missing-session failures remain failures; session IDs are never retried as new chats or under the active selection. The unscoped legacy `listAgents` catalog operation still uses the selected project; all session operations declare owner routing explicitly.

This return is derivative repair evidence against the campaign's frozen 26657ff90 diagnosis basis and active candidate, not authoritative decomposition truth or publication acceptance. Diagnosis closed; implementation locally checked; integrated functional acceptance remains open pending parent browser evidence and independent review.

## Independent-review F3 repair (2026-09-13 follow-up)

F3 corrected in `daemon-harness-port.ts`: uncached ownership probes defer only `WORKING_ROOT_CONFLICT` and `WORKING_ROOT_INACCESSIBLE` while allowing another retained scoped port to prove ownership. That successful port must still pass its own project and session checks. Deferred failures are preserved when no verified owner is found; authoritative recovery does not turn a failed actual-owner validation into success. Authentication/authorization, transport, and unexpected errors remain immediately fatal. Cached-owner operations retain their existing direct authorization/manifest checks. Ownership consistency checks execute outside the probe-error handler.

Regression now exercises both unrelated A manifest drift and A inaccessibility before healthy uncached B child lookup, proves B's own scoped lookup succeeded, and confirms uncached actual-owner B drift still rejects without dispatching a turn. An explicit FORBIDDEN probe remains fatal and is not swallowed. Tests also retain the prior known-owner drift and restart assertions.

Under the parent's serialized F2 coordination, this port owner additionally added `steerReceipt` to the port interface, unavailable implementation, explicit session routing map, and project-scoped Runtime adapter. The native App author owns API/client/UI/fake-port integration. The old-folder routing regression includes receipt-only lookup and confirms it calls only A's scoped client after B selection.

Follow-up preflight: APP-HOLD-1 dispatch entry `APP_V3_USER_JOURNEYS_20260912:CROSS_FOLDER_SESSION_REPAIR:F3`, target DEL-03-01: ALLOW / CLEAR, no active holds; source HEAD reported by preflight `4031c6c54f76760baaaf3d92e2db83819ce3a8ac`. Register hash unchanged; scan `0954ed105705301ccab40f3b6bcaed1fce542bc4f961055d40cc121b91b5dc29`.

Final focused check: `npx vitest run src/__tests__/lib/runtime-daemon-harness-port.test.ts` PASS, 31 tests. `npm run typecheck` was attempted and is currently blocked by the in-progress additive F2 integration: installed Runtime declarations do not yet expose SessionSteerReceiptRequest/sessionTurnSteerReceipt, and the three harness fake-port constructors require steerReceipt. These exact seams were routed to parent/native App author; this child did not build Runtime or alter those other-owner files. The earlier passing typecheck applies to the pre-F2 candidate only. Parent must refresh Runtime declarations and run integrated typecheck after F2 fan-in, then obtain independent re-review. Product port files and focused port test are released for fan-in. No live operations, builds, Runtime source edits, or Git operations were performed during F3 repair.
