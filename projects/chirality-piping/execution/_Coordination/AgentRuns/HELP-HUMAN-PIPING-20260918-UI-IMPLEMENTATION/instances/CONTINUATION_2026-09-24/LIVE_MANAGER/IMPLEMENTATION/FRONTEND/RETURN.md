# Frontend F source-ready handback

Actual executor `/root/live_manager/frontend`, TASK Type 2, parent `/root/live_manager`; no descendants. Initial exact-wire ACK and consulted source origins/hashes are in ACK.md. Parent subsequently released exact F source/test authoring, retaining execution-resource holds. All writes stayed in this isolated checkout and F-owned sources/evidence. No Git mutation, primary checkout, native app, browser, CUA, endpoint or process interaction occurred.

## Implemented candidate

Eight owned source/test files are enumerated with current exact hashes in SOURCE_READY.json. operationsSessionState and existing shell tests did not need changes. Existing public six-slice/no-setter contract remains unchanged.

Private hook controller registry and native bridge expose inspect/preview/submit/status only. Projection creates full invocation-bound agent source_ref and maintained operation fields, calls the existing real engine, freezes basis/ordered operations, reserves idempotency synchronously and recovers historical keys before new-work freshness/owner checks. Queue acknowledgements require exact committed token/key/batch/basis. Local Apply prepares a transition descriptor; the layout observer checks model revision/reference, queue removal, checkpoint and actual applied/batch receipt, empty redo and cleared result/analysis/manifest/rule/history/proof state. It immediately copies the observed model before independent canonical hashing. Incomplete publication remains outcome_unknown rather than a stale-basis claim. Hash failure retains the snapshot for retry.

BatchReceipt gains optional liveReceiptId created by the controller-owned Apply path and observed on its actual receipt; GUI receipts retain existing behavior. Proposal metadata and the live ticket appear in BatchReviewPanel; no external Apply capability was added. Current workspace snapshots remain separate from controller-lifetime ticket recovery across Undo/edit/project changes. Bridge listeners precede registration, buffer early correlated events, serialize StrictMode unregister/register, retire synchronously, and remain inert for browser/disabled responses.

Manager clarification: receipt origin.request_id identifies the preview invocation that authored immutable operations, consistent with source_ref; submit transport request correlation remains native-owned. Neither proves verified actor identity. Canonical fixture rev2 SHA-256 6a35f885b5175ab9ee5c8ae9ea2290cfe118512b6476b59ff986f0aace1af8dc was acknowledged. Maintained tests use semantic engine-generated values, no dated evidence imports. Manager/native owns maintained carrier fixture bytes.

## Validation boundary

Authoring/source inspection only so far: no tests, TypeScript, build, npm or live-resource execution by this child. Manager is preparing dependencies/Wasm and owns sequential execution. Three focused suites authored: real-engine projection and atomic rejection, concurrent reservation/observation/cancellation, stale retained queue, partial Apply uncertainty, historical delayed/failed hash recovery, hook single/two-member Apply/Undo/project-switch/Clear, browser/disabled bridge, early registration event, partial listener failure and StrictMode/cancellation identity. Tests are unrun and are not passing evidence.

Planned manager commands from project root after resource release:
- `./node_modules/.bin/tsc -p apps/desktop/tsconfig.json --noEmit`
- `npm run test:desktop -- src/features/workspace/liveControlController.test.ts src/features/workspace/workspaceSession.liveControl.test.tsx src/services/liveControlBridge.test.ts src/features/workspace/workspaceSession.shell.test.tsx`

Full C1–C8/N1–N3/I1–I2 qualification is not claimed. Save/Open normalized persistence and actual connected-native scenarios still require planned integration evidence; canonical session hash computation and full shared-session regressions need executed checks. Native I1/I2 and actual-human H1/H2 remain unrun. No engineering acceptance, Runtime qualification, issuance or release.

Source files handed back to manager for serialized checks and findings; further edits only when manager returns bounded corrections.

## TypeScript correction

Manager first TypeScript check reported TS2367 in preview success classification. Removed the redundant second applied-status comparison after the preceding throwing guard already rejects applied_model, acceptance, applied_to_session_model and non-validate_only outcomes. The malformed-result guard is unchanged. No check executed by F; source handed back for manager rerun.

Retirement follow-up: current source already assigns terminal reason controller_retired. Added focused regression for concurrent unpublished submit + retire + rebind/retry, asserting uncertainty and no replay. Authored only, awaiting manager execution.

## Bridge async test correction and readability

Manager reported TypeScript pass, then focused suites 30 passed / 3 failed in bridge lifecycle tests. The fixed 15-microtask flush did not establish dynamic-import/listener/register readiness. Replaced it with bounded waitFor observations of actual register resolver, binding, reply and listener cleanup; retained early-event and strict ordering oracles. Each created bridge has idempotent tracked disposal, and held registration promises are released by afterEach even after test assertions fail. No product lifecycle behavior changed in this correction.

Expanded controller blocks and object/intent/receipt construction using the local TypeScript AST printer as a formatting-only operation, then restored two-space indentation. No tests/build/type checks were executed by F. Files handed back for manager rerun; SOURCE_READY.json refreshed.

## Inspection-basis retention clarification

Intentional implementation detail introduced during source authoring before the first SOURCE_READY handback, independently of the later formatting-only change: node inspection reuses the existing opaque basis when workspace/revision/hash match, then retains only that current inspection-basis snapshot. A later node inspection on a changed workspace/revision/hash replaces the stale inspection basis. An old unsubmitted basis therefore returns stale_basis rather than consuming a separate 1,024-basis allowance. The initial draft's extra 1,024 retained inspection-basis limit was removed; it was not a frozen wire limit.

This does not evict frozen previews, tickets, or idempotency associations: each successful preview owns its copied basis/model/operations, and each submission owns its copied preview. Their promised controller-lifetime capacities remain 256 previews and 1,024 idempotency associations, with refusal rather than eviction. No product source or tests changed for this clarification, and no test/resource execution occurred.
