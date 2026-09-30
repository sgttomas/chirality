# RETURN — additive guard v3 normal-exit race repair candidate

**Diagnosis and pure repair complete; independent backcheck and operational
qualification remain required.** This is original author TASK
`/root/delivery_manager/guard_implementation`, returning to DELIVERY
`/root/delivery_manager` under ROOT `/root`. No numerical retry or live witness
was performed or granted by this checkpoint.

Launch coordination basis remains `888e388812f65dffce4428c96c18d2ddc8d2ae61`.
ROOT later supplied `84843dbf9b74c4c3fdb727610998910b740a48ea`; no Git command
was used here. Product source remains `3bddc2b05f6106e969c7cf43373b230845c7cc66`.
The sealed uncommitted v3 brief, skill and B02 return hashes were verified.
`CONTEXT.json` preserves actual instruction/skill/evidence origins, hashes,
parentage, steering, scope and test commands.

## Diagnosis and selected repair

`DIAGNOSIS.md` was frozen before writing v3. B02's worker exit 0 occurred at
551960.4548745; the failing table at 551960.457240541 retained worker 25401 as Z;
v2 refused at 551960.4583125 with proc_pidinfo ESRCH. The exact failed native
call/PID is absent from the historical error string and is not invented here.
`reproduce_v2.py` reproduces that code mechanism with a deterministic fake Z
snapshot and ESRCH, preserving the exact original v2 refusal in
`v2_reproduction.json`. This simulation is not a reconstruction of unlogged
native operations. B02 remains guard-failed; forensic numerical passes are not
promoted. ROOT's later exact latch resolution is read-only evidence here.

New `Run/tools/host_guard_v3.py` changes only the affected provider collection
and error-provenance paths, plus passing the existing supervisor event sink to
its provider. V1 and v2 remain untouched.

- Exact failure-shaped ESRCH reads become **candidates** for disappearance,
  never permission to skip a PID. Operation, PID, errno, return size, known and
  available partial identity are retained. EPERM, unknown/zero errno, malformed
  or short returns still refuse.
- Before any allowance, every available partial PID/start/UID/real-UID/PGID/SID
  field is checked against the known identity and leader. Already observed
  reuse, UID/group/session change or malformed fields refuse even if a later
  table could show absence. Unknown fields are not fabricated.
- Non-leader disappearance requires a newly acquired **complete global absence**
  snapshot. Still-present, escaped, reused, leader-loss or contradictory cases
  refuse. A Z row alone never bypasses a native identity read. Known members
  missing between samples receive the same fresh confirmation.
- The guard recollects the full surviving/new membership, with at most two
  retries inside the original deadline and age bound. Additions or losses at
  the closing snapshot trigger bounded recollection. Reappearing retired PIDs
  throughout the provider/job lifetime refuse, including visible presence outside
  the group in a later acquisition. Churn or exhausted time stops normally.
- Valid partial RSS/footprint sums from an interrupted pass are retained as
  conservative acquisition maxima, so an observed cap crossing is not erased
  by a later exit. Missing/unvalidated worker metrics are recorded as
  `exited-unmeasured` with null resource observation, not zero. Absence proves
  no exit status and no lifetime memory peak. Matching present zombies are
  explicitly listed as unmeasured after their identity is checked.
- Monitor sampling and monitor DONE draining share that logic. Supervisor
  draining uses native group enumeration and, when needed, a bounded complete
  all-PID enumeration; it never spawns ps inside its own group. Its collection
  uses one fixed 0.5-second budget, not a renewed budget per departed child.

No cap, threshold, allowance, heap backstop, stop/control/signal/ownership rule,
authentication, latch policy, compile grammar, schema, or grant interface was
relaxed. V2 `validate_compile_argv` and `read_job` remain AST-identical. Existing
provider ctypes layouts/signatures remain unchanged. Global PID enumeration is
bounded at 32768 plus one spare slot to detect saturation; unknown/truncated or
malformed enumeration refuses. The job-lifetime seen/departed record retains at
most 512 observed owned PIDs (the existing MAX_MEMBERS bound); exhaustion refuses
newly seen PIDs rather than evicting history. This is an additional conservative
metadata limit, not support for arbitrarily large compiler process trees.

## Verification and exact scope

- **111 preserved tests pass**, exit 0: all original 41 behavioral tests and all
  v2’s 70 admission/preservation tests run against v3 via an additive in-memory
  binding. None of those sealed suites was edited.
- **39 new fake-native tests pass**, exit 0, with additional boundary subtests.
  They cover all identity/get-session/rusage read boundaries; Z-then-ESRCH;
  known/new workers; partial-identity contradictions; fresh absence versus
  presence/reuse/escape; leader loss/zombie; denied/unknown/short/malformed reads;
  deadline/age exhaustion; bounded churn; new members during retry/end snapshot;
  sentinel preservation; both completion paths; cross-acquisition PID
  reappearance inside/outside the group; bounded history without eviction;
  unmeasured provenance; retained
  partial cap crossing; and monitor HEARTBEAT versus STOP decisions.
- `scenario_results.json` retains five bounded fake traces, including the
  unmeasured Z worker, new-member inclusion, partial maxima, contradictory
  identity refusal and non-spawning native completion route. These are not live
  memory/process measurements.
- **78 pre-existing source/packet/B02/ROOT-incident files are byte-identical**
  before and after. Preservation records include v1/v2 manifests and all old
  guard packets. Original results and ROOT's resolved latch bytes are unchanged.
- AST scope: add `NativeReadFailure` and `errno` import; modify MacProvider's
  `__init__`, `identity`, `live_group`, `group`, and add six bounded private helpers;
  supervisor change is only supplying its existing event sink. Every other
  top-level definition and module statement is unchanged. Full textual delta
  is `host_guard_v2_to_v3.diff`.

V3 source SHA-256:
`b32050c72d0bbad0f69526fc98d1f28dcb1fa131115227a2169db8100d66848b`.
`VALIDATION.json` and `SHA256SUMS` retain exact source/test/reproducer/trace/log
hashes and observed exit results. The manifest seals only the new additive
packet and v3 source; it does not replace old seals.

## Remaining limits and return route

Native ABI/permission behavior, real polling latency, actual exit timing and
API completeness under load remain operational checks. A successful ps or
native list is a completed provider snapshot, not an atomic reservation of
process existence. Unobserved double-fork escapes and external supervisor
SIGKILL retain the original limitations. Short-lived workers can remain
unmeasured; only explicit validated resource observations may be reported.
Conservative identity/terminal-state changes, persistent zombies, truncation,
process churn or slow native calls may still refuse. The small retry budget is
not an attempt to guarantee every rapidly changing compiler process tree.
K6/VR and full DEC-025 scope remain separately unqualified.

`LIVE_FAST_CHILD_PROPOSAL.md` supplies a later bounded six-job ROOT witness with
ordinary fast exits, small inherited children, tail draining, independent
sentinel and explicit recovery evidence. It is a proposal only. A run that
never exercises recovery must say so; it cannot claim that branch live-tested.
No numerical execution, compiler, model, provider, guard activation, signal,
network, installation, setting change, Git command or delegation occurred in
this TASK. All writes are the new v3 source and this continuation folder.
Return this exact candidate to independent backcheck before any ROOT decision
to resume numerical work. This author does not resolve its own review gate.
