# Proposed low-memory live qualification — not executed

Independent review of the sealed source/tests comes first. ROOT then explicitly
invokes a bounded qualification at the host boundary that permits libproc, ps
and sysctl. This document grants nothing and introduces no human token. Do not
start a compiler, model, installer or benchmark as a substitute for these tests.
No command below was executed by GUARD-IMPLEMENTATION.

Use the existing response runtime identified by RUNTIME_BINDING.json and the
supplementary native-Rust setup record. Do not change its older status text.
Derive the repository with `git rev-parse --show-toplevel`; resolve the runtime
from `tempfile.gettempdir()` plus `runtime_directory_name`, and canonicalize it
with `Path.resolve()`. ROOT checks that runtime, guard and logs are owned mode
0700 and that no earlier ACTIVE latch is unresolved. Retain one shared slot.
Existing directory permissions should be reviewed on these exact response-owned
paths, not recursively changed across a user home.

## 1. Read-only provider witness, before launch

Under the later permitted boundary, import the sealed host_guard module and
instantiate `MacProvider(runtime / 'logs')`. Call `identity(os.getpid())` and
`sample()` three times, one second apart. Save the exact module/header hashes,
macOS/Python versions, raw fixed-command outputs, parsed values, monotonic start/
end times, and any error locally. Check the self PID/UID/PGID/session against
`os.getpid/getuid/geteuid/getpgrp/getsid(0)`, and check start seconds/useconds are
stable across reads. Compare a single own-PID RSS with `/bin/ps -p <self> -o rss=`
(KiB); it is a coarse contemporaneous cross-check, not an equality oracle.

For layout qualification, have the reviewer inspect SDK declarations and later
permit a **separate tiny native ABI-only probe** if needed to check sizeof and
member offsets. Do not fold an unreviewed compilation into this read-only stage.
No group is admitted if required permissions or values are unknown, or if the
observed pressure representation does not match the inspected source. Stop for
source repair/review rather than inventing a fallback metric.

## 2. Exact bounded fixture and explicit job

In the later qualification scratch directory, materialize this reviewed fixture
as `fixture.py`. It has no workload above 64 MiB, no network, and a 30-second
self-expiry. The `escape` case is deliberately unsupported, expires in six
seconds, and must be observed as a failed containment test. Its escaped child
must never be cleaned up by a remembered-PGID signal.

```python
import os, signal, subprocess, sys, time
mode = sys.argv[1]
if mode == 'leaf':
    time.sleep(30)
elif mode == 'ignore-leaf':
    signal.signal(signal.SIGTERM, signal.SIG_IGN)
    print('IGNORE-READY', os.getpid(), flush=True)
    time.sleep(30)
elif mode == 'escape-leaf':
    os.setsid()
    print('ESCAPE-READY', os.getpid(), flush=True)
    time.sleep(6)
elif mode in ('sleepers', 'ignore', 'escape'):
    leaf = {'sleepers': 'leaf', 'ignore': 'ignore-leaf', 'escape': 'escape-leaf'}[mode]
    p = subprocess.Popen([sys.executable, __file__, leaf])
    print('PARENT-READY', os.getpid(), 'CHILD', p.pid, flush=True)
    time.sleep(30)
elif mode in ('alloc16', 'cap64'):
    n = (16 if mode == 'alloc16' else 64) * 1024 * 1024
    blob = bytearray(n)
    for index in range(0, n, 4096):
        blob[index] = 1
    print('ALLOCATED', n, os.getpid(), flush=True)
    time.sleep(3 if mode == 'alloc16' else 30)
elif mode == 'clean':
    print('CLEAN-READY', os.getpid(), flush=True)
    time.sleep(3)
else:
    raise SystemExit('unknown fixture')
```

Create each job JSON using this exact schema, substituting resolved owned paths,
unique job IDs, the chosen fixture mode and computed hashes. The interpreter
path is the selected native Python, resolved through `Path(sys.executable)`;
there is no PATH lookup during execution. Hash the interpreter and fixture in
1 MiB chunks. Candidate is the guard review candidate full SHA when available;
record product basis `3bddc2b05f6106e969c7cf43373b230845c7cc66` separately in the
qualification receipt. A working-tree-only source hash is insufficient to claim
an exact committed candidate; preserve both if review precedes commit.

```json
{
  "job_id": "guard-q-clean-01",
  "run_id": "HELP-HUMAN-PIPING-20260930-T3-AUDIT-RESPONSE",
  "candidate_sha": "<40-hex-reviewed-candidate>",
  "input_hashes": {
    "<absolute-python>": "<sha256>",
    "<absolute-fixture.py>": "<sha256>"
  },
  "kind": "qualification",
  "containment": "inherited-group",
  "cwd": "<absolute-owned-qualification-scratch>",
  "command": ["<absolute-python>", "<absolute-fixture.py>", "clean"],
  "env": {"PYTHONDONTWRITEBYTECODE": "1"},
  "limits": {
    "cap_bytes": 134217728,
    "allowance_bytes": 67108864,
    "disk_write_budget_bytes": 67108864,
    "disk_reserve_bytes": 1073741824,
    "max_seconds": 8
  }
}
```

Run each serialized case with this command, using fresh job IDs/logs and
retaining exact stdout/stderr, start/end times and exit codes:

```text
<absolute-python> <repo>/Run/tools/host_guard.py run \
  --runtime-dir <canonical-response-runtime> --job-spec <absolute-case-job.json>
```

`Run` expands to the response directory, not a literal repository folder. For
`cap64`, set cap_bytes to **67108864**; allocation is bounded at 64 MiB, with
supervisor/interpreter overhead expected to cross the group cap. If prelaunch
supervisor usage already reaches that cap, report a refusal and do not launch;
ROOT then records/reviews a bounded adjustment, never increases fixture size
blindly. The 128 MiB grant and 64 MiB allowance are proposed qualification-only
operating choices, not proven overhead or production limits.

## 3. Sentinel and monitor-loss controller

For each case retain an unrelated sentinel as a direct `subprocess.Popen`
object in a small controller outside the guard. A concrete controller fragment:

```python
sentinel = subprocess.Popen(['/bin/sleep', '45'])
sentinel_identity, _ = provider.identity(sentinel.pid)
monitor = subprocess.Popen([python_path, guard_path, 'run',
                           '--runtime-dir', str(runtime),
                           '--job-spec', str(job_path)],
                          stdout=controller_out, stderr=controller_err)
```

Capture registry and both event streams. Wait at most 15 seconds for STARTED,
then for a valid live sample naming the supervisor, fixture parent and child
before any injected monitor-loss action. Save those complete identities. A
refusal before this point is a failed/incomplete qualification case, not a
successful kill test.

For the `sleepers` **monitor-loss** case only, perform `monitor.kill()` while
that direct child is still unreaped (`monitor.poll() is None`). This exact child
handle supplies ownership; do not load a PID from a previous log. Wait/reap the
monitor, then observe the original registered identities read-only for at most
8 seconds. Supervisor logs must show heartbeat-loss TERM and eventual draining
or KILL. Do not send a signal to its former numeric PGID after it exits.

On every case, `sentinel.poll()` must still be None and
`provider.identity(sentinel.pid)[0]` must equal `sentinel_identity`. Then clean
up only that direct sentinel handle with `sentinel.terminate(); sentinel.wait()`.
A missing/denied sentinel observation is an incomplete test. If a controller
error interrupts qualification, retain all identities and use only still-owned
unreaped direct child handles for cleanup. Never issue pkill or pgrep-based kills.

For absence confirmation, read a complete current `provider.table(deadline)`.
For each previously recorded owned PID: absence is evidence of exit; a present
row requires a matching/changed start-identity check. A changed identity is
reported as reuse and is never signalled; a matching zombie is reported as
non-running, not silently removed from the evidence. Any denial or malformed
row is unknown. Reading old numbers is acceptable for diagnosis; targeting
them with a signal is not.

## 4. Case order and required evidence

| Order | Fixture / action | Required outcome |
|---|---|---|
| 1 | `clean` | Three admissible quiet samples, authenticated registry, ordinary completion and ACK, no live members, workload exit 0, ACTIVE cleared. |
| 2 | `alloc16` | Independent live RSS/footprint samples show the small allocation, complete output, no guard stop, sentinel unchanged. |
| 3 | `sleepers`, let 8-second runtime expire | Parent/child share registered group/session; only that group receives TERM; bounded stop and sentinel unchanged. |
| 4 | `ignore` | Marker proves TERM-ignore installed; parent exits on TERM while child survives until group KILL; supervisor survives TERM until escalation; unrelated sentinel unchanged. |
| 5 | `cap64` | Valid sample reaches RSS or footprint cap; reason identifies which metric; bounded termination; preserve actual peak/latency without calling sampled peak a true maximum. |
| 6 | `sleepers`, kill monitor as above | Supervisor's heartbeat path stops owned sleepers after monitor death; ACTIVE remains; no new slot admission; sentinel unchanged. |
| 7 | `escape` | Monitor detects visible changed group/session and requests stop of the original group only; escaped child self-expires by six seconds; qualification reports unsupported containment and stays latched. |

After cases 3–7, ROOT inspects records and verifies owned identities are gone or
non-running before resolving the exact ACTIVE latch. A second invocation while
first job is live must refuse `heavy-slot-busy`; a second invocation after a
stopped/unresolved job must refuse `previous-job-not-cleared-by-root`. Perform
these lock/latch probes using distinct job IDs; they launch no workload.

Use monotonic event timestamps to measure stop-request to TERM, TERM to KILL,
and last accepted heartbeat to stop. Proposed initial acceptance observations
are TERM within 0.5 seconds of received STOP, KILL within 2.5 seconds of TERM
for a TERM-ignoring child, and no live original owned workload by 6 seconds after
monitor loss. These are **test targets**, not measurements or guarantees. A
miss means qualification failed; investigate without relaxing a bound silently.
The acquisition/cadence maximum and observed RSS/footprint overshoot must also
be recorded. A stop without adequate metric/identity evidence is incomplete.

Once these pass and independent review backchecks any repairs, ROOT may grant
one tiny direct Rust compile/probe under pinned isolated 1.97.1, offline/locked
cargo -j 1, RUST_TEST_THREADS=1 and an owned target. That is a separate grant
with a new explicit cap, allowance, candidate/input hashes and output budget.
It establishes direct-command qualification only. Preserve the observation
binary's independent heap refusal and classify it separately when that binary
is eventually admitted. K6/VR adapter and full DEC-025 qualification remain open.

Hash raw runtime logs before producing sanitized repository evidence. Substitute
portable aliases for personal runtime/home/checkout paths in committed records;
retain raw hashes and per-file byte counts. Preserve every refusal/failure and
unrun case. ROOT owns any changed operating decision and next grant.
