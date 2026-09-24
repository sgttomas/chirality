# Frozen Pipes validation checkpoint — R4

Current HEAD is ROOT's continuity-only checkpoint47030e390b1d201a10ae4980ed52f412147bccb3. Current source freeze is `_run_records/COMBINED_FREEZE_R4.json`, complete diff `combined-candidate-r4.diff` SHA-256 ebb1f148ef770648e71a8b05d2326176399df04bfd826b6b95e49a35930bb369. Only `e2e/b4-pipes.spec.ts` changed from R3; all other eight file hashes and all260 maintained WASM source/lock inputs are unchanged. Original review, R1/R2/R3 freezes, failed observations and backchecks remain preserved. R4 is a test-only route correction; its independent source backcheck is clear in REVIEW/R4_BACKCHECK.md, and its browser rerun awaits ROOT lane handback.

## Actual results and stopped resources

- Rust139unit+9integration passed offline/locked with two jobs and isolated target; product files remain identical to the tested Rust freeze.
- Final R3 frontend130/130 and TypeScript passed. Earlier127pass and129pass/1stale-DOM-test failure are separately retained; the corrected live-node assertions passed in the130run.
- Maintained WASM build passed in a fresh isolated target, with no maintained source/lock drift. Its standard unchanged self-weight build step also passed; no shared target was used.
- Exact10 original bound/unbound probe inputs passed against the rebuilt operation artifact. Both originally unsafe unbound equal/greater-wall cases now reject atomically; zero and valid positive controls still apply. Validation-only and unchanged inputs were checked.
- Browser R3 final interrupted evidence:17 reported passes (11desktop,6compact). Desktop no-op setup failed before editing (expected completed, actual failed job); compact no-op has a separate page-fixture timeout/Test ended before its body. Five selected compact existing scenarios have no completion evidence. The earlier12-unrun count was interim and is superseded. No24-case pass is claimed. The failure, error-context and partial trace/resources were preserved. After stalled teardown beyond five minutes, graceful SIGINT did not complete; only the verified owned process tree was terminated. Runner-15 is interruption, not a test pass. All seven known PIDs were absent and ports5174/5175 free before explicit lane release.

Canonical actual outputs: `_run_records/FINAL_CHECKS_R3/`. ROOT now owns the heavy lane for its first-correctness clean sweep. No Pipes test/build/browser/server/native process is running.

## R4 correction and next action

`BROWSER_R4_DIAGNOSIS.md` distinguishes the observed failure from source diagnosis. The old test routed a replacement fixture module, so it did not take the intended edited-model blocked-result path; its empty load-case basis also violates the manifest contract. ROOT authorized a narrow test-only correction: real un-routed default fixture, real zero authoring, browser save/reopen, then the actual edited-model blocked response with matching project/model and complete input basis. R4 keeps strict completed job plus MODEL_INCOMPLETE result/diagnostic assertions, actual receipt/readiness/hash/history retention, and wrong-unit rejection. It neither fabricates results nor changes product/solver code.

The original reviewer’s R4 backcheck is clear. Wait for explicit ROOT lane handback. Then verify the R4 source hashes and rebuilt asset identities. UI/Rust/build/probe checks are not invalidated by this browser-test-only correction; preserve their exact candidate/content binding. Run the seven Pipe scenarios and five selected existing Node/Materials/Sections scenarios under the two declared source viewports (24project/scenario executions), at most two workers, after checking port ownership. Use a new raw output directory and preserve R3 untouched. Stop on unexpected failures; any changed source requires affected review before resumption. Release owned processes/ports afterward.

No native app launch, Git or graph write is authorized here. Actual native witness, final actual-candidate CI, cleanDEC-025 and integration remain ROOT-owned. The blocked browser response is result-state retention evidence, not native solve or physical correctness proof.
