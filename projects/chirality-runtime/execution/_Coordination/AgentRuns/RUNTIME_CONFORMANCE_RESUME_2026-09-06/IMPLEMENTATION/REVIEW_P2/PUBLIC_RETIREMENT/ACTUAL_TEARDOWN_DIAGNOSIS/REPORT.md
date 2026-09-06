# Independent actual public teardown diagnosis

RUN_STATUS: SUCCESS — diagnosis/proposal only; conformance failure remains.
ControlSurface: MERGED (manager read-only actual-failure dispatch)
TaskProfile: NONE
TaskSkill: NONE
WriteAuthorization: ALLOWED_WRITE_TARGETS — this evidence directory only.
ToolPolicyCompliance: PASS
ToolsUsed: scoped repository/supplier-source/evidence reads; Python hashes/extract/report writes. No tests, supplier/process/network/account execution, source/dist/build/config edits or delegation.
Attribution: OpenAI GPT-6; exact serving ID unavailable; native Agent2 role/nondelegation instruction-asserted.

## Independently verified outcome

PARENT_CHECKS/P2_PUBLIC_CANCEL_PRIMARY_CANDIDATE2_02 is an actual public cancellation attempt. Readiness succeeded: tracked shell71873 and sleep71877 in separate PGID71873, with independent current identity matching and genuine foreground/signal-denial/ready markers. Public interrupt began at1788722264970; real generation-bound retirement began at1788722264988 before outer fixture cleanup, and rejected49ms later with DESCENDANT_RECONCILIATION_REQUIRED. Controlled transport close returned fulfilled in3ms, but healthy independent census subsequently retained both separate-group processes; shell parent changed to1. The vendor group was gone. Source before/after are identical and supplier hash bc4bad750a7d7cdf4f02c2bb7f78cbac40be2727dc41bb0b1b4f2967efb21bf9 stayed unchanged.

The real public interrupt and pending public turn both rejected reconciliation. Durable state remained prepared without terminal, with exited worker entry retained. The repaired Runtime commitment barrier therefore failed closed in this actual case. This is not the earlier marker/census race and not merely an expected pending-run session-close response: retirement itself failed. No cancellation proof or public event parity follows.

Outer cleanup then made another retirement attempt and preserved daemon-stop/workers-close reconciliation errors. Final census was empty after9815ms total, consistent with the seven-second natural fixture lifetime. The record does not establish which later cleanup/natural event caused disappearance. Sibling signal count1 means the pre-control ran, but positive post-control was not reached; sentinel remained unchanged and provider/census failures were empty. Historical PIDs are evidence only, never current signal targets.

## Source chain and cause

Runtime production codex-supervisor.ts:151-165 spawns an owned detached vendor group then closes it by immediate group SIGTERM, waits up to500ms for close, then SIGKILL. It also signals the vendor group on leader exit. The public fixture copies that lifecycle and truthfully marks productionLauncherProven=false. ObservedTransport at:115-140 joins owned transport close with actual tracker reconciliation and rejects any detached/remaining/identity-changed/census-failed state. CodexSupervisor.retire preserves that rejection, and current DelegatedRuntime gates durable terminal on successful retirement.

The frozen supplier source explains the separate process group: utils/pty/src/pipe.rs:158-164 invokes detach_from_tty before command exec; process_group.rs implements setsid (or setpgid fallback). PipeChildTerminator retains the spawned tool process-group identity (:216-219,:304-307). On macOS its kill path calls the supplier's existing group/member fallback (:70-73); non-Linux parent-death setup is a no-op. Killing only the vendor PGID does not encompass this intentionally detached tool group.

Crucially app-server/src/lib.rs:723-725 enables its graceful signal handler only outside stdio mode. Therefore current Runtime SIGTERM close does not select the supplier's graceful thread shutdown in this stdio topology. The observed rapid vendor exit, orphaned shell and live sleep are consistent with the owner process being killed before its tool-group cleanup runs. This is a source-grounded causal explanation, not direct instrumentation proving which Rust cleanup branch ran.

An existing owned EOF path is available: app-server-transport/src/transport/stdio.rs:50-78 reads stdin EOF and sends ConnectionClosed; app-server/lib.rs:1012-1032 closes the RPC gate, queues connection cleanup and exits the stdio event loop. When not forced, :1173-1182 drains active RPC/connection/background tasks and calls shutdown_threads. request_processors/thread_processor.rs:1209-1213 invokes shutdown_all_threads_bounded(10s). core/thread_manager.rs:1102-1136 snapshots all tracked threads and concurrently calls each shutdown_and_wait under that timeout. session/mod.rs:885-887 submits Op::Shutdown; session/handlers.rs:396-409 aborts tasks and calls unified_exec_manager.terminate_all_processes. process_manager.rs:1520 drains its own process registry and calls terminate on each; in-flight processes are stored before initial yield (:525-546), so the foreground fixture tool is already owned. UnifiedExecProcess/ProcessHandle forwards termination to the owning pipe handle, rather than a Runtime census PID.

EOF is therefore feasible as a teardown request that reaches existing native ownership paths. It is not yet proven effective for actual parent/native-child cancellation or timeout. Shutdown has other awaits (conversation/hooks/connection/background draining); the ten-second thread bound is not a global EOF completion deadline. Native ProcessHandle.request_terminate discards kill errors (utils/pty/src/process.rs:221-225), so even normal supplier exit cannot replace Runtime independent reconciliation. Preserve that barrier.

## Narrow proposed repair boundary

First propose a shared Runtime-owned transport lifecycle implementation used by BOTH production CodexSupervisor launch and the public controlled supplier launcher. Suggested exact new files: packages/daemon/src/codex-transport-lifecycle.ts and tests/codex-transport-lifecycle.test.ts; edits to packages/daemon/src/codex-supervisor.ts and tests/exact-process-runtime-conformance.test.ts, with focused supervisor tests if required. These are proposed paths only; no source write authority was exercised here. Keep supplier source/binaries and frozen prior fixtures/evidence unchanged. Parent must allocate exclusive ownership and source-generation pause before implementation.

The helper should accept the actual spawned ChildProcess/stdin/close ownership, never an arbitrary target PID from model output or census. On one memoized close request, stop further writes, end owned stdin to deliver EOF, keep output/error pipes drained and wait for bounded graceful completion. If EOF/write or grace fails, use only the already-owned vendor group TERM/KILL fallback with explicit bounded close wait; preserve graceful/fallback phase diagnostics and original failure. Do not blindly wait the supplier's10s maximum on top of the fixture10s action limit: select a reviewed shutdown budget within the existing overall bounded action and preserve timeout/cancel error causality. A hung child or inherited pipe must not keep helper close pending without bound. Normal early exit/spawn failure/concurrent closes must remain idempotent and cannot signal a new process after ownership has ended.

After helper close, real observedTransport must still require fresh independent clean census and preserve reconciliation failure for survivors, changed identity or failed scan. The shared helper closes the implementation gap between production and test, but controlled no-account launch/admission and exact production-launch acceptance remain distinct. Do not add Runtime killpg for the detached census PGID, member-by-member ps PID kills, blanket process grants or marker-derived signal authority. Coarse lstart plus getpgid checks are observations and leave a check/signal reuse race; they do not authorize killing unrelated processes. The existing supplier's own retained handles are the appropriate first teardown boundary.

Validation proposal: meaningful pure/controlled lifecycle tests for EOF ordering and no early group signal, joined close/idempotence, grace timeout escalation, stdin failure, early exit, never-ending close/pipe, and rejected reconciliation despite superficially fulfilled transport. Then fresh exact source/config/supplier hashes and actual public normal/cancel-primary; if clean, child cancellation and timeout profiles. Require owned EOF/phase evidence, retirement before fallback, correct journal and matching generation, unchanged sentinels/sibling controls, no detached survivors before outer cleanup, and original10s/60s bounds. A failure preserves its source-pinned record and does not become pass when outer cleanup or natural sleep finishes.

If EOF reaches native shutdown yet owned tool groups survive or its bounded drain is insufficient, route a separately scoped supplier-manager investigation of the existing shutdown/ProcessHandle/pipe termination chain using a new source/candidate identity. Do not modify/relabel Candidate2 or weaken Runtime reconciliation. No supplier patch necessity is established before the narrow shared Runtime lifecycle experiment.

## Handoff

Closure: independent diagnosis complete; public process retirement remains failed/unproven. Parent's hold on redundant lifetime profiles is consistent with the demonstrated common teardown boundary. Parent may continue unrelated authorized checks under its own scope. This derivative diagnosis cites exact actual JSON and frozen Runtime/supplier sources in INPUTS.json, plus accepted owner/SPEC_FAN_IN basis through manager briefs and supplier MANAGER_RETURN. No accepted decomposition, lifecycle/hold/release/supplier/account/client state changes.

Outputs: REPORT.md; INPUTS.json; ACTUAL_EVIDENCE_EXTRACT.json; RUN_RECORD.md; OUTPUTS.json.
MISSING: owner/manager allocation of exact shared-helper implementation scope, source review and actual public retirement evidence; event parity remains unresolved.
NEEDS_HUMAN_RULING: none for diagnosis; proposed source writes await parent concrete scope disposition.
DEPENDENCY_NOTES: shared lifecycle implementation/review then parent exact profiles; no cycle. No active reviewer-owned process or cleanup responsibility transfers.
