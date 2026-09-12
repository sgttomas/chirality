# Independent actual v6 evidence review

**FAIL is reliable against the fixture's retirement assertion; it does not establish a supplier regression.** Direct six-case results and the pair's six shell cases pass. The later raw turn/interrupt does not retire the sleep process within the fixture's observation window. Pinned supplier source deliberately separates turn interruption from background terminal cleanup, so the fixture's assumed equivalence exceeds that primitive's semantics. Overall qualification remains incomplete.

## What the evidence establishes

Read the original result, not only summary. All paths below are under `/private/tmp/chirality-supplier-root-directory-fix-20260911-01/qualification`:

- `direct-run-v6/result.json`, SHA256 `5e871d54546bef9e62f02530cc2172d3f9cda7cba09d66f20a166fc3423c5d5b`: six cases; positive exits 0 and exact output; negative exits 1, marker plus denial; all signals null. Current synthetic disk contents still match README/result/secret/read-only expectations and both forbidden new files remain absent.
- `pair-run-v6/result.json`, SHA256 `8d1ced38c8c0c7ca463e67e0c7f27af36977c27347242a689fb71b7baddd7e13`: six uniquely bound native exec outputs (`fixture-1,3,5,7,9,11`) have terminal exits 0/1 and correct output. All six matching turns complete. The seventh provider request issues the sole `/bin/sleep 30`; no previous case issues sleep. Pair disk invariants also match.
- `pair-run-v6/summary.json`, SHA256 `66646a8005559355c8e379f889ec2f2bc6cdccfa8a45ce60f4323530074fcf07`, agrees with the original result. Reviewed executed fixture hash remains `13e07b3685e080d87af644cd4a73317bc8dca9ba7c43ed152cd63f77d5f168a5`.

Using zero-based original RPC indices: [106] starts request 10; [108] returns turn `01a092d7-0624-7a40-ba25-8513b083d494`; [113] sends request 11 turn/interrupt with that exact turn and thread `01a092d6-fa78-7b32-a3cf-d4b9043bd5ba`; [116] acknowledges `{}`; [118] completes the same turn as interrupted at emittedAtMs 1789169960696. Prior terminal events were consumed and identity-checked; no stale or wrong-turn completion explains the result.

Census [0–6] contains supplier PID 1369 and host PID 1379 only. [7] first adds `1394 1369 1394 /bin/sleep 30`; every census [8–58] retains that exact PID/PPID/PGID/command. By the frozen control flow, [7] precedes interrupt, [8–57] are the fifty post-terminal checks with 100ms waits, and [58] is the failing final check. This is current process-table evidence with direct parentage, not a historical knownProcesses-only match. No competing fixture sleep, synthetic callback output, or parser failure explains it.

RPC [119] then records commandExecution item/started for the same turn and command, source unifiedExecStartup, at emittedAtMs 1789169960709, 13ms after terminal emission. Its processId 17734 is the supplier's logical exec identifier, not OS PID 1394. This is event-order evidence; it alone does not prove a startup race defect.

## Semantics and limits

Independently inspected pinned isolated supplier `source/codex-rs/app-server/src/request_processors/turn_processor.rs:1437–1482`: nonempty turn identity is validated and response waits for TurnAborted, not OS-child retirement. `core/src/session/handlers.rs:60–65` separates interrupt_task from clean_background_terminals/close_unified_exec_processes. `core/src/session/mod.rs:4152` aborts active tasks. `core/src/unified_exec/process_manager.rs:526` explicitly stores live sessions before the initial yield so interrupting the turn cannot drop the last Arc and terminate the background process. The observed persistence is consistent with that intentional raw supplier behavior. This review does not claim to prove Runtime's stronger close/cleanup lifecycle; that path was not invoked by this fixture.

Census entries lack per-snapshot timestamps, process start time and state. They establish continued listed process presence and nonretirement; they do not independently distinguish running/sleeping from unreaped state or measure exact wall time. The nominal five-second interval follows the frozen fixture control flow. These limits do not justify converting FAIL to PASS. Cleanup records SIGTERM to 1369, 1379, 1394, no cleanup-error entry, and supplier exit by SIGTERM. The cleanup's final empty-census assertion is implied by error-free control flow but its raw snapshot was not saved. No fresh process probe was run by this reviewer.

The failure stops before the after-interrupt README turn and clean normal App Server shutdown. Thus neither recovery/follow-up nor graceful retirement passed. The appropriate remaining question is whether the actual approved lifecycle closes/retires the worker and safely continues, not whether raw interruption alone kills intentional background sessions. Any continuation must retain this failure and its semantics, and provide separate lifecycle evidence; this review authorizes no retry or source change.

Independent TASK/Type2, gpt-6-astra high under the continuing parent-recorded exception; same instruction/worktree basis as REVIEW_FIXTURE_V4.md. Read-only evidence and limited raw-interrupt source inspection; no fixture/supplier/compiler execution, source edit, retry, delegation, or protected actual-trial access. Derivative review complete; overall qualification and native/packaging acceptance remain open. Return only through HELP_HUMAN.
