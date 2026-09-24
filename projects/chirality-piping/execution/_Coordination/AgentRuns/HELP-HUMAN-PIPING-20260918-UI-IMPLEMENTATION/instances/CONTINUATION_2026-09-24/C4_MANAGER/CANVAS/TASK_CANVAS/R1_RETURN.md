# C4-CANVAS-R1 source repair

Same TASK child and isolated checkout as original return; no delegation, Git mutation, tests/compiler/build/browser/native or resource execution. Parent released a7 source freeze after complete independent review. Read canonical `CANVAS/INDEPENDENT_REVIEW/RETURN.md`; its SHA-256 is 51bfff09283602aff02bda914e01313611ea00fdaf8dc2c0f8499a73e552db15. Original a7 review, original output manifest and failed/passing manager records are preserved. R1_OUTPUTS.json binds this repair's three owned source/test files.

## Repair

Resource context-loss handler now invokes the installed label updater immediately after marking status lost and before cancelNavigation, scheduler.pause (which can publish RAF-count diagnostics), status callbacks or resource notifications. Restoring status likewise invalidates labels before its callbacks. Late lifecycle callbacks on a disposed owner are ignored. The normal current ready-frame route performs recovery; no projection check is bypassed. PipeViewport adds viewportContextStatus to its existing layout-effect dependency list as a React-commit backstop. The fail-closed caller path already removes placed DOM, Tab/accessibility eligibility and owned focus synchronously and clears applied refs; it now also synchronously hides omission disclosure until the queued semantic summary is removed. Successful current placement reveals disclosure again.

## Authored regression; execution pending

New `PipeViewport.contextLabels.test.tsx` mounts the actual component with the actual ViewportResource, real resource event bindings, normal policy/projection and actual diagnostic publisher. GPU renderer and browser layout/RAF are explicit inert fixtures; Three geometry/math and OrbitControls remain real. It starts from an applied label; focuses it; dispatches cancelable context loss with pending work; inspects DOM placed/tab/aria/focus, disclosure and diagnostics within dispatch's act scope before React commit or a next frame; observes unavailable updater results through lost/restoring; restores then checks current placement; unmounts and checks lifecycle ownership/RAF and detached events. This is a simulated lifecycle regression, not real WebGL/native qualification.

Manager must run TypeScript and the focused new test plus affected prior suite sequentially, and return any failures for repair. Child ran no tests/compiler. Independent R1 backcheck and programme browser/native/current-row/profile gates remain outstanding.
