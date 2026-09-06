# Accumulated implementation review — first pass

Verdict: changes required. One actionable P1 defect reproduced; no additional concrete defect identified in this bounded pass. This is independent derivative review evidence, not release acceptance.

## F1 — cancel and drain governed child before publishing manager terminal

Baseline `packages/daemon/src/codex-manager.ts:72–91` races the running hook against a 120000 ms timeout but only retires the hosted manager on failure. `packages/core/src/agent1-run-coordinator.ts:543–562` changes a launched child's stored status without aborting the run controller or draining the actual child. The still-running delegate subsequently executes its success path at lines 388–423 and persists `status: running`, overwriting the already failed run record. Cancellation must reach and drain the actual child; terminal publication and subsequent hooks/writes must be fenced even if drainage cannot complete.

`review-repro.test.ts` invokes the actual new manager port and coordinator, using controlled channel/storage/turn implementations; only the 120000 ms timer is compressed to 30 ms. It asserts: failed terminal emitted; actual child turn still active; zero child interrupts; after releasing the child, the latest persisted record changes from failed to running with completed child. All assertions passed (`repro.log`). It does not use a provider, vendor binary, or credentials. Implementation owners received the finding and reproduction before this report. The port has since added a configurable callback timeout; the core lifecycle repair is still in progress. Source drift is separately recorded; baseline pins must not be read as final source pins.

## Validation

- Controlled reproduction: 1 passed, demonstrating F1 on its baseline.
- Seven focused production suites: 113 passed, `focused-suite-unsandboxed.log`. Covers compiler/actor, actual Pi SDK, observed descendants, delegated broker, supervisor and private socket.
- First restricted run: 69 passed, 44 failed at sandbox-denied sockets, process spawn or nested Seatbelt execution. Recorded in `focused-suite.log`; rerunning the same suites with execution permission passed. These environmental failures are not product findings.
- Source/code inspection covers native compiler deny-pattern preservation and readback; actor dynamic callback identity/size/time bounds; Pi exact model/tool/credential/root binding, bounded provider responses, explicit SDK resources and continuity; tracker observed-only attribution; terminal retirement; manager mailbox/channel and standalone composition.

## Calibrated remaining limits

The known exact-App-Server literal-root directory startup blocker is not a new code defect here. Compiler tables and controlled transport tests do not establish native filesystem/network/descendant kernel enforcement. Actual hosted login/manager use and supplier dynamic-tool dialect remain separate exact-supply/live proof gates. Pi automatic compaction is implemented; durable Pi resume and manual compaction are explicitly not exposed. In-memory Pi tombstone/session capacities require a fresh runtime after exhaustion; they are bounded implementation limits. No owner rulings, activation, compatibility release, source identity disposition or product release are implied by this review.

## Required backcheck

After the lifecycle repair is frozen, independently rerun a positive cancellation/drain regression derived from F1, plus manager/core integration tests, and hash the final reviewed sources. Do not ship the historical reproduction as an auto-discovered assertion that requires the defect to remain present. Preserve its source and successful baseline log as historical evidence.

Attribution: OpenAI GPT-6, exact serving model ID unavailable. Agent 2 role is instruction-asserted and not mechanically enforced.

## F1 backcheck — residual in-flight publication race

The first core repair aborts/drains cooperative child work and fences new queued hook publications, but does not fence an already executing persistence call. At `persistHook`, authority is checked before awaiting `persistAgentRun`; bounded drainage can time out while that call remains pending. The terminal publication then proceeds independently, and the prior running-state write may later overwrite it.

`persistence-repro.test.ts.source` reproduces this with the actual manager port/coordinator and a blocked first child-running persistence call. After 20 ms bounded drain, the failed terminal record with reconciliationRequired is written; releasing the earlier write changes latest record back to running with launched child. The reproduction passed (`persistence-repro.log`). Reported to coordinator owner and parent immediately. A safe fix must order terminal publication after earlier writes, or enforce an actual pre-publication cancellation fence, or give immutable terminal evidence explicit precedence over mutable state. A pre-call liveness check alone is insufficient.

Historical reproduction files now end `.test.ts.source` so ordinary Vitest discovery will not require the defect to remain present. Source bytes are unchanged by renaming. First core repair is not yet accepted by this review.
