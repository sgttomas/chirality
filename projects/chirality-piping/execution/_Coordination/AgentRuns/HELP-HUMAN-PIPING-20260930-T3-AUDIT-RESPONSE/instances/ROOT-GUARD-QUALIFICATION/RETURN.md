# ROOT live guard qualification checkpoint

The reviewed v1 guard completed three provider samples and eight bounded live
fixture cases on the M3 Air. All unrelated sentinels survived unchanged; every
original workload was gone at final inspection. This supports a later small
direct-command trial after v2's compile-admission repair is backchecked. It
does not admit large models, K6/VR separate-session runners or full DEC-025.

Guard source is the immutable v1 at candidate
`fe6ca966259d29d8d6ed2f05460400f6cb5d5de0`, SHA256
`feb0e1508fde6c764eefb85e2b72bc7a597edf86d48307fb646a80a80eac03db`.
ROOT acted under decision 04 and the independent review's explicit suitability
assessment. No compiler or model ran. v1's two known compile-admission findings
remain applicable to v1; these qualification jobs used Python fixtures only.

## Observed outcomes

| Case | Observed result |
|---|---|
| Read-only providers | Three stable self identities; native RSS/footprint returned; own RSS agreed coarsely with ps; normal pressure, 79% available estimate, stable swap counters. |
| Clean | Workload exit 0, healthy DONE/ACK, owned group drained, ACTIVE cleared. Concurrent second job refused heavy-slot-busy. |
| 16 MiB allocation | Workload exit 0; sampled RSS peak 44,105,728 bytes versus 27,213,824 for clean. ACTIVE cleared. |
| Sleeping parent/child | Supervisor runtime limit sent TERM; owned workloads exited; ACTIVE remained. |
| TERM-ignoring child | Marker proves handler installed. Parent exited on TERM; group KILL followed after 2.001229 s; all owned processes exited. |
| 64 MiB explicit allocation / 64 MiB group cap | RSS cap triggered; sampled group RSS reached 94,208,000 bytes. TERM followed the monitor request after 0.017527 s. |
| Monitor killed | Immediate socket-disconnect stop: TERM after 0.010536 s, group-drained after 0.033096 s. This is a control-loss result, not a heartbeat-expiry witness. |
| Visible escape | Changed group detected and original group stopped; escaped fixture self-expired as designed. Containment refused and latched; no escaped/historical PID was signalled. |
| Monitor stalled | Explicit heartbeat-loss TERM after 3.024372 s; group-drained after 3.048339 s. Controller confirmed both workload PIDs absent by 5.543832 s; live supervisor still held its identity awaiting ACK, then exited. |

Stopped/uncertain jobs refused the next launch until ROOT separately inspected
the return, reread current identities/group membership and moved that exact
ACTIVE file into the job's evidence. No generic kill/search cleanup was used.
All eight cases preserved their sentinel's complete identity. The runtime has
no unresolved ACTIVE latch at this checkpoint.

The monitor-stall witness is a bounded addition to the reviewed sequence: the
kill-monitor case exercised immediate socket failure, so it could not establish
the real stale-heartbeat branch. ROOT stopped only its unreaped direct monitor
handle with SIGSTOP after a complete member sample, checked after 5.5 seconds,
and killed that same retained child handle. The fixture remained two sleepers
under the same 128 MiB grant. `qualify_case_v2.py` preserves this addition;
the original controller remains unchanged. This was ROOT's execution choice,
not a new human approval or an assertion of prior reviewer coverage.

## Scope, provenance and limits

The fixture is copied verbatim from the reviewed LIVE_QUALIFICATION plan;
SHA256 `d0297c6c13d47e3ecb0ef5b73769dddedddc54ace0febdcc504211fd7cad88ec`.
Each job uses 128 MiB group caps except cap64, which uses 64 MiB; 64 MiB
allowance/write budget, 1 GiB disk reserve and an eight-second runtime limit.
The maximum explicit allocation is 64 MiB. Each invocation is serialized.
Controller cleanup addresses only its own unreaped direct monitor/sentinel
handles. Group signals originate only from the live reviewed supervisor.

`LIVE_RESULTS.json` gives derived timing/metric summaries; case folders retain
portable copies of raw job/controller/monitor/supervisor/workload/latch records.
`RAW_INVENTORY.json` binds 83 original runtime files by byte count and SHA256,
and records each portable copy's hash. Path aliases replace host-specific
runtime, checkout, interpreter and home strings; numerical/raw event content
is preserved. Original raw files remain in the isolated runtime. No old M5
evidence was reconstructed or overwritten.

The largest observed normal sample-start interval was 1.076499 s. Sampled peaks
are not true maxima. The cap case overshot its nominal RSS cap by 27,099,136
bytes before observation; this is expected evidence of polling and interpreter
overhead, not a hard 64 MiB memory guarantee. Future grants must include reserve
and allowance. Whole-host availability is an OS estimate, not reserved RAM.

In monitor-stall, the supervisor's final self-KILL came 2.543511 s after TERM
while waiting for ACK with an already drained workload. Do not present that
as a 2.5-second bound. The TERM-ignoring live-child escalation test measured
2.001229 s. The original target of no live workload within six seconds of
monitor loss/stall was met by the workload evidence; general scheduling stalls,
unobserved double-fork escapes and external supervisor SIGKILL remain outside
the qualified guarantee. No direct cargo operation has yet been observed.

Next: independent v2 backcheck and qualification-evidence review, frozen
candidate/GEN-8, then one explicitly budgeted offline locked direct compile.
