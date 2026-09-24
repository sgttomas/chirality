# Pipes manager return

**Bounded implementation, source review and prescribed local validation complete; suitable for ROOT integration.** Actual HEAD47030e390b1d201a10ae4980ed52f412147bccb3 is a ROOT continuity checkpoint. The nine-file product/test change is frozen in `_run_records/COMBINED_FREEZE_R4.json`; complete diff SHA-256 `ebb1f148ef770648e71a8b05d2326176399df04bfd826b6b95e49a35930bb369`. `SOURCE_WHITELIST.json` gives the exact nine owned paths/hashes. ROOT owns Git/index, graph, native, final actual-candidate CI/cleanDEC-025 and integration. No native application operation, Git mutation or graph write was performed by this manager. Read-only Git identity/diff commands were used.

## Behavior and scope

Pipes now use the existing direct/review table for label and string provenance, actual optional mill-tolerance length, and Material IDs from the current catalog. Omitted and null tolerance remain absent/TBD until the user explicitly enters value and unit; zero is a meaningful authored quantity. Existing quantities retain their actual unit, malformed non-null/numeric-without-unit records stay blocked, and no project-unit fallback is invented. Direct/review operation payloads, retained drafts, Queue/Clear, stale guards, selection/focus and history are covered. From/To/shared Section stay readonly through their existing dedicated routes.

The table equivalence callback now optionally receives the captured unit. Only Pipe equivalence uses that extra argument: same value/unit direct entries avoid backend dispatch/history/result clearing, while wrong-unit entries still reject and absent-to-zero still authors. Existing callbacks and compact geometry are unchanged.

A connected backend probe exposed unbound Pipe tolerance equal to or greater than known wall being accepted while bound Pipes rejected it. ROOT explicitly authorized the minimal operation-applier repair. Known OD/wall/effective-wall relations now apply to the three relevant local quantity paths; incomplete/unconvertible peers remain unknown, unrelated label/material edits remain authorable, and existing bound-cache checks remain strict. There is no frontend physics substitute or solver/frame/runtime change.

Product scope is ModelTree, modelTableAdapter, tableState, EngineeringTable, their two maintained unit-test files, b4-pipes.spec, and operation_applier section_bindings/lib tests: nine files total. The untracked new browser file is included in the complete diff, not merely its hash. No other family or B5 work began. PR883 fit remains the completed predecessor.

## Actual checks

| Check | Result / canonical evidence |
|---|---|
| Rust operation-applier |139unit+9integration passed, offline/locked, two jobs, isolated target. `BACKEND/_run_records/cargo-test.log`; exact source/lock/toolchain identities adjacent. Rust files unchanged since that run. |
| Focused UI and TypeScript |130/130 passed across five suites, then TypeScript exit0. `_run_records/FINAL_CHECKS_R3/`. This UI stage preceded the rebuilt WASM; actual rebuilt-backend integration is separately established below. R4 only changes the browser test. |
| Maintained WASM build |Passed in a fresh isolated target with two jobs, no drift among260 maintained source/lock inputs. Standard build script also rebuilt the unchanged self-weight engine. Original generated artifacts were retained in its recorded temporary custody. Command/source/artifact identities under `FINAL_CHECKS_R3/wasm-*`. |
| Exact backend replay |All10 original bound/unbound inputs passed against the rebuilt module: zero and valid positive apply; negative and equal/greater-wall reject; validate-only publishes no model; rejected results have no diff/model; accepted models equal the explicit expected document. Original unsafe outcomes remain preserved. `FINAL_CHECKS_R3/optional-wall-replay/`. |
| Browser final matrix |24/24 passed: seven Pipe and five selected existing Node/Materials/Sections scenarios across desktop1440×920 and compact1280×800. Separate one-worker project invocations exit0, no skips/flakes/unexpected results, unchanged120s test budget. `_run_records/FINAL_BROWSER_MATRIX.json` binds every identity and both JSON reports under `FINAL_CHECKS_R4_SERIAL/`. |
| Source/runtime identity |All nine final source hashes and both generated WASM asset sets match before/after final browser execution. Actual browser153.0.8010.54 is captured per test. Operation WASM SHA-256 `6bee62d77d4503f4d0e6f0a7fbc34dab899ac823168ff83cf2401974b4219b75`. |
| Independent source review |Fresh Astra/xhigh reviewer found R1 null-admission and R2 explicit-unit no-op defects; both repaired and backchecked. R3 live-cell test correction and R4 actual-fixture route correction each have a distinct clear backcheck. Original findings remain in `REVIEW/RETURN.md`; final source route backcheck is `REVIEW/R4_BACKCHECK.md`. |

The no-op browser witness uses the actual default fixture, actual zero authoring and browser Save/Open, then the real edited-model blocked response. Both viewports assert completed job, zero rows, MODEL_INCOMPLETE, matching project/model/run identity and the specific browser-backend-required diagnostic before comparing exact receipt/readiness/model/history across no-ops. This proves state retention, not a native solve or physical result qualification.

## Preserved failures and recovery

Initial UI tooling/query/geometry-fixture failures are retained. The pre-repair130-case run had129passes and one stale detached-node assertion; the live same-ID cell already owned focus, and the corrected exact live-cell assertion then passed. Review defects R1/R2 were source issues, not hidden by the earlier passing tests.

The first browser run had17 reported passes, a desktop no-op setup assertion failure before editing, a separate compact page-fixture timeout, and five cases without completion evidence. Its routed precision fixture was unsuitable for the intended result-retention route. Error-context, original logs and partial trace/resources remain; owned teardown eventually required interruption and returned-15. The corrected two-worker run then passed all12 desktop bodies but stalled at worker/project transition; ROOT authorized bounded teardown and separate one-worker invocations. It returned130 after interruption. Neither interrupted attempt is a matrix pass. No assertion or timeout was relaxed; final serial reports supply the complete24-identity partition.

Both successful project runners returned0 and released ports5174/5175. Prior interrupted process IDs were checked absent, including the later worker discovered from the final log. The CPU/browser lane was explicitly returned to ROOT. No owned test server or running job remains.

## Attribution and remaining gates

Manager `/root/native_pan_manager` ran WORKING_ITEMS/Astra-high. UI TASK `/root/native_pan_manager/pipes_implementation` and disjoint Rust TASK `/root/native_pan_manager/pipes_backend` each executed Astra-low; independent TASK `/root/native_pan_manager/pipes_review` executed Astra-xhigh. All used delegated-harness-native sessions with full TASK instruction supplied and no Type2 delegation. Refused launches are recorded as nonexecution. ROOT's prospective local-manager repair fallback was not used; every product repair remained with the UI/Rust TASK owners. `ACTIVATION.md` and raw basis records retain origins/hashes, fixed predecessor preparation and scope extensions.

ROOT may integrate these frozen sources and evidence. Native Pipe interaction/result-history witness, final actual-head CI, cleanDEC-025 sweep, PR review/integration and broader B4 completion remain owning gates. Existing root/other-branch passes do not silently qualify this source change. No engineering/practitioner acceptance, performance qualification or release is claimed.
