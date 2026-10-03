# F independent-review repairs — source ready

Actual parent assignment reopened exact F scope for R2/R3 and coordinated R4 receiver targeting. Isolated checkout only; no source/test execution, builds, process/socket/browser/native/CUA or Git mutation. Product/test sources are handed back with refreshed SOURCE_READY.json; independent backcheck remains required.

R2: Clear now marks unpublished, unresolved live admissions as retired before scheduling queue removal. The controller still settles original and joined requests only when its committed observer sees the entry absent. Already published queues retain the existing withdrawn behavior; observed commits and their historical hashes remain retained. Added controller and real-hook regressions that schedule original submit, joined submit and Clear before publication, require pending promises inside the scheduling interval, and require both cancellation errors after observed absence.

R3: preview captures the hook's current request epoch at invocation, separately from its inspected basis. After asynchronous engine validation, existing current model/workspace/hash guards remain, followed by invocation-epoch and cancellation checks. A Clear-retired invocation returns expired and cannot create a preview reference. A newly invoked preview on the still-current inspected model remains permitted. Added controlled controller and hook regressions holding an actual engine response across Clear, asserting no passed reference/model/history/queue/receipt mutation, followed by a successful fresh request.

R4: resolved installed event.d.ts permits Options.target={kind:"WebviewWindow",label:"main"}; event.js forwards that object to plugin:event|listen instead of its omitted-option Any default. Both listeners now explicitly select that target. The early-registration bridge test asserts both actual registration options while retaining controller/app/dispatch/request correlation assertions. Parent accepted coordination with N's corresponding native EventTarget::WebviewWindow emitter. Targeting alone is not a general confidentiality guarantee; N's narrow local-main event ACL complements it. Actual native ACL/target delivery remains unrun.

Planned affected checks under manager resource release: TypeScript; liveControlController.test.ts; workspaceSession.liveControl.test.tsx; liveControlBridge.test.ts; existing workspaceSession.shell.test.tsx. Native capability/event tests and eventual actual I1/I2/H1/H2 belong to parent integration and remain distinct. No existing test assertions were weakened.

## Consulted repair/source identities

- `projects/chirality-piping/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/LIVE_MANAGER/IMPLEMENTATION/REVIEW/RETURN.md` SHA-256 `eeb939a6c4c93e2e5f41d93e18bc9d12ba815fcd284a7a7d71a5d942643c0ada`
- `projects/chirality-piping/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/LIVE_MANAGER/IMPLEMENTATION/REPAIR_SCOPE.md` SHA-256 `c7546bcdefaf7940b84c93ef9ceceaeefd8e83c2ee1097c2cdb5e2db82496ef1`
- `projects/chirality-piping/node_modules/@tauri-apps/api/event.d.ts` SHA-256 `0d738dff2ba5e25de6ef3fe078235a1f32f4c93438f50c4146cac00c9c0e7456`
- `projects/chirality-piping/node_modules/@tauri-apps/api/event.js` SHA-256 `f00d22c559ce7e58a85d860e35fd60d20826f13d7f534a5f3548a7ef94446e84`
