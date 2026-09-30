# Later ROOT witness proposal — not executed

Independent review/backcheck of the exact v3 hash comes first. This plan does
not grant a workload, compile or numerical retry. ROOT owns the existing B02
latch disposition; this TASK only read the ROOT-B02-INCIDENT resolution record.
B02 remains guard-failed. Every future witness uses a new job ID and log folder.

Use the established private response runtime, its single slot, selected Python
and hash-pinned new guard. Keep ordinary three-sample admission, 40% early-stop
threshold, swap rules, age/deadlines, heartbeat and ownership unchanged. Proposed
qualification-only limits are group cap 128 MiB, allowance 64 MiB, runtime 8 s,
write budget 64 MiB and disk reserve 1 GiB, as in the original light fixture plan.
These are proposed parameters, not a grant or new M3 overhead measurement.
If the current host cannot admit them, refuse rather than enlarge automatically.

ROOT may materialize this small fixture in its later owned qualification scratch
and hash it with the actual Python executable. It allocates no intentional large
buffer, has no network, creates only inherited-group children, and does not set
signal handlers or process groups:

```python
import subprocess, sys, time
mode = sys.argv[1]
if mode == 'leaf':
    time.sleep(float(sys.argv[2]))
elif mode == 'one':
    subprocess.run([sys.executable, __file__, 'leaf', '0.02'], check=True)
elif mode == 'tail':
    # Parent returns first; supervisor must drain the inherited short-lived leaf.
    subprocess.Popen([sys.executable, __file__, 'leaf', '0.08'])
elif mode == 'pair':
    children = [subprocess.Popen([sys.executable, __file__, 'leaf', d])
                for d in ('0.02', '0.05')]
    for child in children:
        if child.wait() != 0:
            raise SystemExit('leaf failure')
else:
    raise SystemExit('unknown fixture mode')
```

Proposed bounded sequence, each once and serialized:

1. Direct `/usr/bin/true`, then Python fixture `one`.
2. Python fixture `tail`, then `pair`.
3. One further direct `/usr/bin/true` and one `pair` only if all prior cases
   completed with healthy guard disposition. This is a fixed six-job witness,
   not automatic retry of a refused/failed job.

For each case create a normal `kind: qualification`, `containment:
inherited-group` job JSON with exact input hashes, candidate, argv, cwd and
limits. Invoke the reviewed source directly:

```text
<selected-python> <REPO_ROOT>/<Run>/tools/host_guard_v3.py run \
  --runtime-dir <canonical-response-runtime> --job-spec <new-case-json>
```

Retain a direct `/bin/sleep 30` sentinel child in the external controller,
record its live PID/start/UID/group/session before launch, and verify the same
identity and a still-running child handle after each job. Signal only that
controller-owned unreaped sentinel handle during its own cleanup. No discovered
PID, old PGID, broad process search, manual workload signal or latch deletion is
part of this proposal. Native lists and known identities are observed read-only.

Required observations:

- No false STOP solely from a non-leader process that disappeared between
  enumeration and native reads; normal worker/DONE/ACK/guard completion recorded.
- Every recovery must have exact native operation/PID/errno/return evidence,
  available partial and known identity, a **fresh complete global absence**
  observation, explicit exited/unmeasured or previously measured status, and
  a new complete collection including every surviving/newly observed member.
- Supervisor completion uses native group/all-PID enumeration, with no sampler
  subprocess in its group. No incomplete/truncated/denied native list is accepted.
- Retry count at most two; monitor's original acquisition deadline and sample
  age are not reset, and native completion stays inside its one 0.5-second
  collection budget. Record actual acquisition/stop latencies and any refusal.
- The bounded job-lifetime departed record must reject a later reappearing PID
  wherever visible, without eviction. Do not try to force host PID reuse or
  spawn enough children to exhaust this bound in the live witness; those cases
  are deterministic pure regressions.
- Any contradictory partial identity, reuse, visible escape, leader loss,
  permission/unknown/short error, timeout/churn or resource event is a failure.
  Stop the remaining sequence and return evidence; do not retry automatically.
- An exited-unmeasured worker is **not zero RAM** and supplies no workload peak.
  Valid partial maxima retained by v3 are conservative observed sums within an
  acquisition, not true lifetime maxima or a time-exact group snapshot.

The host race is nondeterministic. If no actual ESRCH/recovery occurs, report
that branch as unexercised by the live witness; successful fast commands alone
are not proof that native recovery ran. Fake regressions remain separate logic
evidence. ROOT may decide a later bounded witness; no signal/pressure injection
or timing manipulation is pre-authorized here. After review and operational
qualification, ROOT alone decides any numerical continuation. Hash raw logs
before portable sanitization and preserve each original result without promotion.
