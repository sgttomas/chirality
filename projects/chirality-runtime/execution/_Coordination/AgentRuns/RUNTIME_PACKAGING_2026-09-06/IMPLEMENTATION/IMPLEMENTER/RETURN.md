# Implementation return — Runtime native Pi packaging boundary

Status: READY_FOR_INDEPENDENT_REVIEW. This is derivative implementation evidence, not decomposition truth, client adoption, hold release, lifecycle promotion, source/supplier acceptance, or product-release authority.

Instance: `/root/packaging_manager/implement`, ephemeral Agent 2 under `/root/packaging_manager` WORKING_ITEMS. OpenAI GPT-6; exact serving ID unavailable. Role and non-delegation are instruction-asserted, not mechanically enforced. No child delegation occurred. Agent 0 role enforcement remains instruction-asserted.

Accepted upstream basis: manager `../PLAN_V1.json`, `../CONTEXT_SHA256.json`, and `../IMPLEMENTER_BRIEF.md`; their exact accepted migration, Gate3 V3, DEL-02-06, owner direction, SPEC_FAN_IN, PLAN_V2, amendment11 and PR737 references apply. `CONTEXT_CHECK.json` verifies every sealed read hash before implementation. This packet does not replace those accepted records.

## Result

Runtime's public barrel previously emitted eager `require('@earendil-works/pi-coding-agent')` in the App-shaped node24/CommonJS bundle. Pi 0.82.0 exposes its root only under the ESM import condition, so loading failed before any turn. `PRE_FIX.log`, `PRE_FIX_SOURCE.ts.txt`, and the retained pre-fix consumer bundle reproduce that exact `ERR_PACKAGE_PATH_NOT_EXPORTED` failure. This is the module-loading defect, not the historical Electron download failure.

The factory remains synchronous. Module-private nonliteral native dynamic imports load both coding-agent and pi-ai during an admitted turn. esbuild preserves these native imports in CJS and ESM; the two SDKs retain one native provider/model state graph. The existing read-tool `Type` import still tree-shakes to typebox with the unchanged App policy (coding-agent external, pi-ai not external); no read-tool/client edits were necessary.

Before awaiting SDK loading, Runtime reserves the session in both histories and active turns, starts the existing deadline, and snapshots caller input/execution. The placeholder history manager is initialized only after the abortable SDK load. Reservations preserve same-session exclusion and distinct-session cache capacity. Interrupt, close, binding release and deadline settle the waiting turn, retire the context and prevent late loading from starting provider work. Existing tool/root/account checks and terminal event mapping remain in place.

## Verification

`FOCUSED_PASS.log`: 46 passed, 2 expected live-provider tests skipped across the five focused Pi files. Sixteen new consumer cases cover CJS and ESM: real SDK offline turns and continuation; cold-loading interrupt/close/binding release/deadline; same-session and distinct-session admission/capacity; caller mutation and accepted account/scope continuity; canonical failed terminal on SDK-load rejection. Every success uses the installed SDK with a supplied synthetic fetch implementation; no operational provider or user account/server state was accessed.

The test load hook instruments real SDK module bodies with top-level-await barriers and completion markers; it does not replace exports with a mock. Cancellation/deadline must deliver the canonical terminal before the test releases the SDK evaluation barrier. Tests then observe completion markers from both real SDK modules and assert zero late provider calls. Native module parsing and synchronous evaluation still share Node's event loop: no JavaScript timer can guarantee a strict wall-clock bound during synchronous CPU work. The test proves cancellation of the asynchronous load wait and a configured 30ms deadline, with a 15s subprocess failure bound; it makes no hard real-time claim.

`TYPECHECK_FREEZE.log`, `POST_FIX_STARTUP.log` and `PRODUCTION_DIFF_CHECK.log` pass. `SOURCE_FREEZE.json` pins all four production/test files, SDK/dependency versions and retained pre/post consumer bundles. `COMMAND_RESULTS.json` records commands, results and all failed fixture attempts. Initial narrow elapsed-time assertions and an async resolver-hook barrier were unsuitable instrumentation: the latter stalled native resolution; evaluation barriers corrected that fixture. Failed logs remain unchanged. The final production implementation was stable throughout those fixture corrections.

## Scope and handoff

Exclusive changed paths:

- `projects/chirality-runtime/packages/engine-pi-omlx/src/pi-turn-runtime.ts`
- `projects/chirality-runtime/tests/pi-packaging.test.ts`
- `projects/chirality-runtime/package.json`
- `projects/chirality-runtime/package-lock.json`

The sole dependency change is explicit dev dependency esbuild 0.28.1, already present in the lock and installed offline. Source/test changes are captured in `PRODUCTION_DIFF.patch` and `NEW_TEST_DIFF.patch`. `SCOPE_STATUS.log` includes concurrent parent/manager evidence under this same Runtime run; this specialist wrote only its declared paths, this evidence directory and owned scratch/test scratch. No frontend, Root governance, sibling, supplier scratch, credentials, binaries, accepted status/hold records, Git commit/push/merge or release acts occurred.

Retained reproduction scratch: `/private/tmp/runtime-packaging-20260906/manager/implement/`, including pre-fix source, pre-fix.cjs and post-fix.cjs with node_modules linked to the current Runtime installation. Do not treat any of these as supplier candidates.

Remaining: independent review, manager validation/fan-in, parent registered whole-suite check and consumer/App integration evidence. This specialist's consumer-shaped proof does not claim Linux/Electron packaged distribution or client acceptance. The separate existing runtime-conformance import.meta CommonJS warning noted by parent remains outside this repair. Required derivative handoff/review and parent acceptance are outstanding; no product closure is asserted. No implementation blocker remains within this brief.
