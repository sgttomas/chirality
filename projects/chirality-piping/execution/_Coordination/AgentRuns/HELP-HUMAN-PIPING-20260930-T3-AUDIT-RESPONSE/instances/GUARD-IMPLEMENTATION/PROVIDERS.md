# Provider derivation and execution boundary

Status: source-derived and fake-tested, **not live-qualified**. No libproc library,
process enumeration, monitoring, signals, or workload was invoked by this TASK.
The ctypes structures are calculated in pure tests; this is not a compiled ABI
witness or proof that the host permits the API. ROOT's approved host observations
establish that sandbox denial is not absence of host capability. Any denied,
short, malformed, unknown or stale provider result refuses or stops this job.

`<SDK>` means the installed Command Line Tools `MacOSX26.5.sdk`. Exact local
header content hashes and normalized origins are in `CONTEXT.json`. Read-only
inspection covered `<SDK>/usr/include/libproc.h`, `sys/proc_info.h`,
`sys/resource.h`, `sys/param.h`, `sys/_types.h`, `sys/_types/_uid_t.h`,
`sys/proc.h`, `dispatch/source.h`, and `sys/event.h`. No SDK code was compiled.

| Binding | Declaration / derivation | Guard use |
|---|---|---|
| `proc_pidinfo` | `int(int,int,uint64_t,void*,int)`, `PROC_PIDTBSDINFO=3` | Both reads must return exactly `sizeof(proc_bsdinfo)`; bracket session lookup and compare stable identity fields. |
| `proc_bsdinfo` | Twelve 32-bit fields; `comm[16]`, `name[32]`; five 32-bit fields; signed 32-bit nice; two 64-bit start fields. `MAXCOMLEN=16`, UID/GID are 32-bit. | LP64 size 136, start seconds offset 120, microseconds offset 128. PID/start/UID/real UID/PGID/session checked. `SZOMB=5` from `sys/proc.h`. |
| `proc_pid_rusage` | `int(int,int,rusage_info_t*)`, `rusage_info_t` is `void*`, `RUSAGE_INFO_V0=0` | Pass address of the complete V0 buffer, cast to declared pointer type. This is not a pointer to a separately allocated pointer value. Success is return 0; surrounding identity reads must agree. |
| `rusage_info_v0` | UUID[16] followed by ten 64-bit fields in exact SDK order | Size 96. `ri_resident_size` offset 64; `ri_phys_footprint` offset 72; start absolute-time offset 80, exit offset 88. Reject zero start / nonzero exit for a live sample. |
| `proc_listpids` | `int(uint32_t,uint32_t,void*,int)`, `PROC_PGRP_ONLY=2` | Supervisor cleanup uses a fixed 513-int buffer and rejects full/partial/zero/negative results, absent leader, duplicates and invalid PIDs. It never spawns a sampler inside its own workload group. |

Apple's [libproc implementation](https://raw.githubusercontent.com/apple-oss-distributions/xnu/main/libsyscall/wrappers/libproc/libproc.c)
shows `proc_listpgrppids` dividing `proc_listpids`'s result by `sizeof(int)`;
this supports interpreting the underlying result as bytes. The inspected upstream
`main` source is supporting documentation, not a pin of this host's kernel.
The local SDK declaration hashes remain the binding source.

The live provider separates the following quantities:

- RSS sums `ri_resident_size` for live group members, including the supervisor.
  Shared pages may be counted in several processes. It is an operational sum,
  not heap allocation and not a group-unique memory measurement.
- Physical footprint sums `ri_phys_footprint` independently. It is OS process
  accounting, with group/shared-resource attribution limitations; it is not
  inferred from RSS or the allocator. Short-lived peaks can be missed.
- `memory_pressure -Q` supplies the system-wide available percentage estimate.
  It is not byte-exact free RAM. `sysctl -n hw.memsize` supplies physical total;
  projecting percentage minus full group cap plus explicit allowance is an
  operating assumption requiring M3 calibration, not an allocation guarantee.
- `sysctl -n kern.memorystatus_vm_pressure_level` must return decimal `1`.
  Every other numeric value stops; malformed/denied results fail closed.
  Apple's [memory-status handler](https://raw.githubusercontent.com/apple-oss-distributions/xnu/main/bsd/kern/kern_memorystatus_notify.c)
  converts the internal level to dispatch pressure flags before returning it.
  The installed `dispatch/source.h` defines normal as 1, warning as 2 and
  critical as 4. No pressure-trigger sysctl is used or proposed.
- `sysctl -n vm.swapusage` records baseline and current used bytes. The parser
  accepts the observed M-unit form only. `vm_stat` supplies the independent
  cumulative swapout page counter. Stable high baseline swap is allowed.
  Any new swapout, counter reversal, or at least 64 MiB new used swap stops.
  Quiet admission requires three samples with unchanged used swap and swapouts.
- `statvfs` supplies free disk bytes. A grant explicitly names its write budget
  and disk reserve. Sampling cannot impose a hard disk quota on workload files.

Fixed absolute provider commands have no shell, a 1 MiB output bound, and a
shared 1.5-second sample deadline. The sample timestamp is acquisition start,
never the time the last command completed. Samples older than 2 seconds or
from the future fail closed. The interval is one second after acquisition;
observed cadence therefore includes acquisition time. A blocked native call or
OS scheduling stall cannot have a proven userspace bound. The independent
supervisor watchdog does not invoke the external host-metric providers.

The monitor's global `ps` metadata rows supply ancestry and PGID membership;
libproc supplies start identity, UID, session and memory for selected members.
Any row-to-identity race fails closed, even if a short-lived compiler child
merely exited. Later direct-cargo qualification must measure whether this
conservative behavior is usable. Unrelated process arguments/paths are not
queried. The supervisor uses native group enumeration only for draining.

All provider command outputs, parsed metric samples, owned identities, job
parameters, decisions and signal intent records stay under the private runtime
job directory. Normal completion logs the original workload exit separately
from guard health. Provider/output failures retain bounded evidence and mark
failure; complete output is not claimed after an output/log-limit stop.
`/usr/bin/time -l` may be additional post-run peak evidence later. It is not a
live provider and is not used by this implementation.
