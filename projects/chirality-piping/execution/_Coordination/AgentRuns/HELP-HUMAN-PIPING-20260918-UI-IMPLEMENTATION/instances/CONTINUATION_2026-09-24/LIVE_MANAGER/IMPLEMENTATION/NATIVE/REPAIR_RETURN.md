# Native repair validation return — ready for independent backcheck

Native heavyweight slot released after all four serial Cargo commands finished. Tested product candidate: `de52a7cfc6cca083877ef53df559f5ee73701615`; actual HEAD and pre-run tool/source identities are in REPAIR_PRE_RUN.json. Native repair source remained byte-identical throughout testing, checked in REPAIR_FINAL_SOURCE.json. No failure or further source repair occurred in this slot. Original review, prior failed sandbox run and prior evidence remain preserved.

## Actual results

- Library live_control tests: **8 pass** (102 unrelated filtered).
- Owned transport/capability tests: **7 pass**.
- CLI binary unit regressions: **4 pass**, including every R5 requested negative and explicit-null-error case.
- CLI integration: **3 pass**, including actual private fixture CLI response correlation and nonzero errors.
- Explicit feature-gated CLI build: **pass**.
- Regenerated capability/manifest/source-target check: **pass**.

REPAIR_RUNS.json records exact commands, zero exit statuses, raw logs/hashes and supported permission escalation for process-owned temporary Unix socket fixtures. Every Cargo command used locked/offline resolution, two build jobs and the isolated target directory. Two prior nonfatal dead-code warnings remain in the desktop library variant. No app bundle/desktop launch, real endpoint, browser/CUA, forbidden ports, old native PID, preferences or Git mutation occurred.

## R1/R4 admission and target evidence

Fresh generated `gen/schemas/capabilities.json` and both desktop build-output capability files contain exactly the source `live-control` capability: `local:true`, `webviews:["main"]`, and only `core:event:allow-listen` / `core:event:allow-unlisten`. No window-wide target, remote origin, default group, emit, fs or shell grant exists. Resolved generated core:event manifest definitions map those identifiers to only `listen` and `unlisten`, respectively. All generated source/schema/manifest/build-output identities and exact checked definitions are retained in repair-acl-check.log; REPAIR_ACL_CHECK.py is the bounded rerun method.

Native compiled the explicit `emit_to(EventTarget::webview_window("main"), ...)` shared emitter used by requests and cancellations. Source check confirms both frontend listeners use matching `WebviewWindow/main` targets. Actual invoking-main and registration/dispatch guards remain. Supplier Any listeners can still receive targeted events; explicit target routing is not claimed as an independent confidentiality boundary.

## Remaining gates

Build-time generated ACL/source checks do not prove actual Tauri listener admission, main-window dispatch or non-main/remote denial. Real listener/register/reply/unregister handshake, native I1/I2, app/default package/disabled-startup/saved-edited-load evidence, timeout/concurrent connection behavior and actual-human H1/H2 remain outstanding. This controlled carrier evidence grants no engineering, Runtime, lifecycle or release acceptance. Independent reviewer must backcheck the complete repaired candidate; ROOT owns later integration and resource scheduling.
