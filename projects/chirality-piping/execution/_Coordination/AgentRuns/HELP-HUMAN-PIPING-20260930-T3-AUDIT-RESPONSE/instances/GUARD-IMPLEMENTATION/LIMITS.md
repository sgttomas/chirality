# Initial guard scope and limits

This source is offered for independent review. No host qualification, heavy
slot, compiler run, engineering acceptance or observation admission is claimed.
Initial command scope is direct cargo/rustc and tiny probes whose descendants
inherit their group. Qualification-only sleepers/fault fixtures are a later
explicit ROOT invocation. There is no server, scheduler, approval token,
background installation, global setting change or automatic retry mechanism.

ROOT invokes `host_guard.py run --runtime-dir <canonical-private-runtime>
--job-spec <explicit-job.json>`. A private shared `guard/slot.lock` serializes
launches using that runtime. All response grants must use the **same** runtime;
it cannot block an unrelated process or an independently chosen second root.
The invocation itself is the grant. The JSON names run/job, candidate, input
SHA-256s (including executable), command, cwd, environment, command kind,
`inherited-group` contract, and explicit memory/disk/duration limits. Inputs
are hashed before launch but not made immutable by the tool; ROOT must supply
frozen owned files. Candidate SHA is recorded, not inferred from a dirty cwd.

The forked supervisor calls setsid and remains session/group leader. Before
launch, monitor and supervisor use a private inherited socketpair with a random
nonce and monotonic sequence numbers. Neither the secret nor an open endpoint
is published. Registry records a nonce hash, monitor and supervisor PID/start,
UID/real UID, PGID/session, specification hash, limits and candidate/inputs.
Workers close control/lock descriptors, explicitly reset TERM/INT/HUP/PIPE to
SIG_DFL, and exec without shell interpretation. Their stdin is /dev/null.

Only the supervisor signals its own group. It is continuously alive while
sending TERM, surviving a 2-second grace, and sending one final group KILL that
also kills itself. Before each signal it verifies current PID, UID/effective
UID, group and session against its captured ownership. A continuously running
process cannot have recycled its own PID/start; no stale numeric PGID lookup
is needed. The monitor never signals a discovered workload identity. It sends
STOP through the authenticated inherited channel; on monitor death or loss of
fresh heartbeats for 3 seconds the supervisor independently stops its group.
The emergency exception path is confined to the fresh supervisor's own session
and original UID. It uses immediate KILL, not a repeated historical target.

`guard/ACTIVE.json` is created before supervisor launch. Normal completion
requires authenticated DONE, matching live leader identity, no live owned
members, ACK, and confirmed supervisor exit. A normally completed failing
workload retains its original exit code in evidence and may release the slot;
the CLI returns 2, so it is not a pass. Any resource stop, interruption, guard
loss, uncertain cleanup or supervisor death leaves ACTIVE latched. New jobs
refuse until ROOT inspects the evidence and resolves that **exact** latch.
There is no generic cleanup or automatic recovery command. Do not simply delete
an unresolved latch while an old workload may remain. The supervisor inherits
the flock, so monitor death alone does not release the active slot.

Operating defaults derived from the brief/E0 proposal, not measured guarantees:

- Group RSS and physical-footprint caps are each the explicit grant, at most
  2 GiB (including supervisor overhead). Binary heap caps remain separate and
  are never removed or rewritten. A 2 GiB heap cap does not fit automatically
  under a 2 GiB group cap. Compilation has its own explicit grant.
- Availability stops at or below 40%, ahead of the 35% reserve policy floor.
  Admission requires three normal/stable samples and projected availability
  above 40% after consuming the full group cap plus positive explicit allowance.
- New swapouts, at least 64 MiB swap growth, non-normal pressure, any unavailable
  metric, or insufficient disk free bytes stop/refuse. No causation attribution
  to the job is made from host-wide pressure/swap.
- At most 512 selected members; two 8 MiB event logs; 8 MiB retained combined
  workload output; 1 MiB per fixed provider command; 4 KiB control packets;
  64 KiB workload-drain chunk per supervisor loop. Logging limits stop the job.
  Disk write budget must be at least 32 MiB plus a positive separate reserve.
  Maximum requested runtime is 3600 seconds. These bounds are intentionally
  narrow for first direct probes, not a complete DEC-025 output allocation.

Remaining limits that pure tests cannot establish:

1. macOS APIs, sandbox permissions, ABI behavior, socket/fork correctness,
   actual flock survival, signal/reset/TERM-ignore behavior, sampling/stop
   latency, process-group emptying, disk errors and real peak overshoot.
2. Global table plus observed ancestry detects visible escape, UID/session
   change and PID reuse. It **cannot guarantee detection of an unobserved
   short-lived child that double-forks, reparents and escapes between samples**.
   It is not a kernel containment boundary. Unknown/recycled/escaped identities
   are never separately signalled. A detected escape fails qualification; its
   cleanup must use its separately retained owner, never a broad search.
3. If the supervisor is itself externally SIGKILLed, the monitor cannot safely
   kill an old group without a live owner. It retains the latch and reports
   lost containment. This initial implementation does not claim dual-failure
   containment. A hostile same-UID debugger or a worker that intentionally
   kills its supervisor is also outside the trust model.
4. All Python and OS scheduling/I/O can stall; RSS/footprint sampling can miss
   peaks. Unrelated applications can consume reserve faster than a sampled
   stop. An allowance and measured stop latency are prerequisites for scale.
5. Host state and inputs are not snapshotted atomically. Identity/table races
   conservatively stop; very short-lived cargo children may need a separately
   reviewed provider refinement after low-memory observation.

K6's `launch` explicitly uses `start_new_session=True`, and the VR scale runner
imports that launcher. Those runners and their process-group-creating tests
are **unsupported**, even if someone labels them `tiny-probe`. Labels do not
establish command qualification. Their existing watchdog, heap backstop,
resource-refusal classification and kill-matrix tests remain unchanged.

The smallest later extension is an explicit registration adapter: a runner
asks the same single-slot monitor to create/register an owned supervisor for
its observation group before exec, hands the runner a private authenticated
control handle, and records PID/start/UID/session and limits for that group.
The runner's existing RSS/timeout decision logic and binary heap backstop stay;
its stop operation delegates to the still-live registered owner. Monitor loss
must stop every registered group and runner exit must revoke admission before
any next observation. Unknown subgroups refuse. It needs an independent diff
review and real interruption/TERM-ignore/escape tests for both K6 and VR.
Merely removing start_new_session or broadening kill targets is not proposed.
