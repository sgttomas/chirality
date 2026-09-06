# Shared transport final independent admission

RUN_STATUS: SUCCESS — all three interim findings closed; bounded parent actual diagnostics admitted.
ControlSurface: MERGED. TaskProfile/TaskSkill: NONE.
WriteAuthorization: ALLOWED_WRITE_TARGETS — this new FINAL_BACKCHECK evidence directory only.
ToolPolicyCompliance: PASS.
ToolsUsed: read-only source/diff/report inspection; Python hashes/evidence; no-cache Vitest and noEmit TypeScript.
Attribution: OpenAI GPT-6; exact serving ID unavailable; native Agent2/nondelegation instruction-asserted. No delegation, source/test/config/dist edits, build, supplier/provider/network/account execution.

## Findings closed

Sticky active stdin error: inputError retains synchronous end failure, active asynchronous EPIPE and unavailable stdin while child remains live. Cleanup still runs; every timely-close return path rejects retained inputFailure. Timeout preserves its code/cause. Known-exit EPIPE remains diagnostic and requires genuine timely pipe close. This fixes the actual transport gap: actor.close already fixed its own failure and would ignore a later stdin error. Negative controls demonstrate active failure cannot become success through fallback or close.

Absolute deadline: synchronous close invocation captures monotonic time; EOF/TERM/final deadlines are1000/1500/3500ms from that same request. waitClosed allocates only remaining time and compares close observation timestamp against each deadline. Delayed continuations and late-close callback races cannot gain new time or turn an overdue close into success. Tests exercise both cases. This remains event-loop scheduling semantics, not hard real time while JS is blocked; policy cleanup/census are subsequent caller operations.

Inherited pipes: final deadline destroys only owned stdin/stdout/stderr, emits disposal and unconditionally rejects timeout. Local stream disposal cannot turn that selected failure branch into success or prove process death. Controls verify destroyed streams, zero retained timers, and no signal after known owner exit.

## Combined source review

Production supervisor and public controlled launcher now use the same helper. Its memoized promise joins concurrent/reentrant close, uses actual spawned ChildProcess's original PID/pipes only, sends EOF once and drains output without removing parser listeners. Known exit/close/spawn failure suppress signals; original vendor group is the sole signal target. Old unconditional exit-time group kill is removed. No model/census PID gains authority.

Production close memoizes policy cleanup and preserves transport/policy errors with aggregate/cause where both fail. Existing observedTransport fresh healthy census/identity/survivor gate and retirement-before-durable-terminal ordering remain unchanged. EOF attempted/finished and helper close never replace these proofs. No additional blocking defect found in the fourfile change.

Public fixture pins helper/tests, records phase and teardown path with generation/outer-cleanup status, keeps controlled admission/productionLauncherProven=false, uses remaining inclusive action deadline for public interrupt/terminal wait, and requires clean retirement strictly before probe issuance+7000ms. Issuance precedes the seven-second sleep, so that bound rules out natural expiry as success evidence. Existing readiness/current full identity, gone/reuse/stale rejection, markers/sibling/sentinel, acknowledgement versus pending actor-close rejection, journal and cleanup gates remain. Public interrupted-event parity stays explicitly unresolved.

## Exact freeze and checks

Read final author REPORT e8cfe38d1e2b24589eb77067e34e46763f7cf3db9cd585abe9c6bd6a6476a399. Verified OUTPUTS seal434dac5f2fb9d20ca6c9c1f1284549906a0caa5c9f44c8efaef7a72ec3e9c110 and all listed hashes/sizes. Interim evidence remains immutable.

- helper361eef00340fff883791a3b858504436f1979a11bd9e9ceb7a8acb4998e9a0f1
- helper testb0b9c413690683545ff9e723fe04c007c68f54e5a6e99a5b7d2a7a550e345d48
- supervisorb4b76607ad6650aea47f6aa5d30aeb4c362d39d36c22772d679bcc5173737210
- public fixture672fc53ab7e52d0f8760665e6e38c98d2f4eb2a1dc4ea516b75b119dbd06eabe
- Vitest config18bcdafacd2dce4e20cc816f8d7824570f57afab84c7da4c075445f545560884
- TypeScript config4fed90f9ed1bca52eb935336a423e8a1eaa030c539ad23a854a60f06b804ddb2

Independent no-cache lifecycle14/14 pass; source-alias public7pure pass/actual1skip; strict helper/test noEmit pass; source-alias public noEmit pass. Selected source/config hashes identical before/after. Parent concurrently owns combined build/generated artifacts; reviewer makes no dist-stability claim. Manager reports registered combined build/typecheck and558pass14skip0fail default suite; those are parent evidence, not reviewer execution.

## Parent admission

Admit exact normal then cancel-primary under final parent generation freeze and separately verified supplier in fresh evidence directories. If successful, resume held child/timeout profiles as appropriate. Require real retirement before OUTER fixture cleanup, fulfilled matching generation, correct committed journal, healthy empty independent census, phase/error evidence, unchanged sentinel/positive controls, no natural-expiry substitution and original10s/60s bounds. Helper's recorded owned fallback can be part of real retirement; outer fixture fallback cannot repair failed conformance. Preserve every failure and prepared journal when cleanup is unconfirmed.

Closure: independent bounded implementation review complete; actual public/native retirement still open. Derivative evidence cites accepted owner/SPEC_FAN_IN via manager BASIS/author amendment and prior actual diagnosis. No supplier acceptance, full G-SBX/orphan proof, hosted account, client release, lifecycle/hold or merge authority inferred. No reviewer-owned process/cleanup handoff.

Outputs: REPORT.md; verification; source before/after; four check logs; RUN_RECORD.md; OUTPUTS.json.
MISSING: exact parent public/native profiles; public event parity remains unresolved.
NEEDS_HUMAN_RULING: none for admitted parent diagnostics.
DEPENDENCY_NOTES: parent final source/artifact freeze and actual execution; no cycle.
