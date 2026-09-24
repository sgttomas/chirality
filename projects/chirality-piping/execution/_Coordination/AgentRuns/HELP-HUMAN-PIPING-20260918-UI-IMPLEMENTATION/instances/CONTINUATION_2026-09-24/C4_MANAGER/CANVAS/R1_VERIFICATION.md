# R1 lifecycle repair verification

Independent review of complete C4 candidate `a7cc327725f622fa901371e913a308af57d52b9e` returned one confirmed P2, C4-CANVAS-R1. The full review and its 60-file/168-binding manifest are preserved under INDEPENDENT_REVIEW. Manager waited for full review completion before authorizing repair.

The retained Astra/low canvas TASK changed only PipeViewport.tsx, viewportResource.ts and new PipeViewport.contextLabels.test.tsx. Context loss/restoring now synchronously invoke the registered label updater before scheduler/status/resource callbacks. That reaches the existing fail-closed path, retiring applied DOM/input targets, owned focus, diagnostics refs and omission disclosure. Context status is also a label-effect dependency. Disposed lifecycle callbacks return without work. Original review/child manifests remain historical; TASK_CANVAS/R1_OUTPUTS.json and _run_records/r1-candidate-01.json bind the repair.

Manager ran sequentially, using existing isolated dependency/engine setup:

- `./node_modules/.bin/tsc --noEmit -p apps/desktop/tsconfig.json` from projects/chirality-piping: exit0.
- `npm --prefix projects/chirality-piping/apps/desktop test -- --maxWorkers=1 src/features/viewport/PipeViewport.contextLabels.test.tsx src/features/viewport/PipeViewport.labels.test.tsx src/features/viewport/viewportLabelMeasurements.test.ts src/features/viewport/viewportResource.test.ts src/features/workspace/uiDiagnostics.test.ts` from REPO_ROOT: exit0, 5 files/40 tests passed.

Raw outputs are _run_records/r1-typescript-01.txt and r1-focused-vitest-01.txt. All three repair hashes were rechecked after execution. Earlier whole C4 focused run passed nine files/133 tests; this rerun covers the affected lifecycle/resource/component/diagnostic surfaces and adds one regression. Do not describe these separate runs as one full 134-test invocation.

The new regression mounts real PipeViewport/ViewportResource/event bindings, Three scene/math, policy and diagnostics with explicitly inert GPU, layout and RAF fixtures. It first obtains an applied label, focuses it, dispatches context loss with pending work, and asserts DOM data/tab/aria/focus, hidden omissions and zero/unavailable diagnostics inside dispatch before React commit. It then verifies unavailable restoring updates, reapplication against ready projection and disposal/event cleanup. This directly exercises the repaired path but is not real WebGL restoration, browser/native or timing evidence. The existing controls test still emits preserved expected jsdom getContext warnings on its unavailable-renderer route.

ROOT explicitly allowed this limited functional window to overlap primary `01063c7f1cfb7a651261401f62a5a72a5daa94dc` DEC-025. Commands were sequential and Vitest used one worker. No install/build/shared WASM target/browser/socket/native/benchmark work ran; the manager announced start and end and released the lane when both processes ended. Elapsed times in raw output support recovery only, not calibrated performance claims.

ROOT also granted commit-only ownership of supplied C4_CANVAS_ACTIVATION.md. Its bytes were verified equal to the tracked ROOT `adc346bcc` copy: SHA256 `cf47440ab4f198f7160e05576112b6a597f00c2efb65b57d69f93b2f6ca767ba`. It is committed unchanged for replay, not an instruction amendment.

Fresh independent backcheck of this frozen repair/evidence delta is required before a clean source/evidence recommendation. True current-row publication, connected browser/native/full-sweep gates and second-profile freeze/qualification remain open.
