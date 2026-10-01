# Independent guard v3 and B02 records backcheck

**No unresolved blocking source or records finding in candidate
`325516a7bb21492458d2c84026db709de8b1b4d9`. The bounded disappearance repair is
suitable for the proposed six-job fast-child qualification when fresh admission
passes. This review does not establish live recovery or grant numerical retry.**

ROOT subsequently reported that the first proposed true fixture refused during
preflight with `quiet-swap-baseline-unstable`, before supervisor/workload launch;
no later fixture ran. That post-freeze report is not a successful operational
qualification and supplies no recovery-branch witness. Thresholds remain fixed.
The actual results of any later qualification need their own assessment before
ROOT resumes numerical work.

Same independent TASK `/root/guard_reviewer`, resumed under `/root` HELP_HUMAN.
I did not implement this repair and did not delegate. Writes are confined to
`Run/instances/GUARD-REVIEW/continuation_02/**`. `Run` is
`projects/chirality-piping/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260930-T3-AUDIT-RESPONSE`.
No live provider, signal, workload, guard, compiler/model, network, installation
or Git/index mutation was performed by this reviewer.

## Frozen coverage

This review covers the complete records delta
`888e388812f65dffce4428c96c18d2ddc8d2ae61` →
`84843dbf9b74c4c3fdb727610998910b740a48ea` (111 paths), then the complete v3
and supplementary-record delta from `84843dbf` to final
`325516a7bb21492458d2c84026db709de8b1b4d9` (32 paths).
Numerical product source remains `3bddc2b05f6106e969c7cf43373b230845c7cc66`.
The final delta SHA256 is
`abb8d2d61e9d8cee59121f480525ba25ecc8e1a8f9426972ddaf78958cc32a76`;
cumulative since `888e3888`:
`a89cc98f822c7266c80544f7a782febdd13270e3c4bd1a533d27ca188d96db60`.
Per-path byte counts/hashes are retained in RECORD_DELTA_84843DBF.json and
FINAL_SCOPE.json. All final working-tree bytes match their candidate blobs.
No duplicate full diff is retained; Git is canonical.

Risk-scaled coverage includes the entire v2-to-v3 executable delta and its
meaningful tests; unchanged core through AST/source comparison; B02 diagnosis,
actual new build/B/incident evidence; both public-export archives and correction;
manager/launch/grant/graph records; native PID-list witness; conditional DESIGN
drafts and their decision/acceptance fences; all new manifest/data integrity.
The old numerical audits and K0 theory were not rerun. The DESIGN draft is
reviewed as an explicitly unselected proposal, not independently accepted proof.

## Repair assessment

V3 source SHA256:
`b32050c72d0bbad0f69526fc98d1f28dcb1fa131115227a2169db8100d66848b`.
Author return SHA256:
`1c834b4e34f6af350ad3acc6795b2b77f8f5a78275027130e954bc87722ae0d3`.

B02's preserved sequence shows worker exit 0, a ps snapshot containing that
worker as Z, then the v2 proc_pidinfo errno-3 refusal, owned-group TERM and
unhealthy completion. Its historical short error string does not identify
which PID/native read failed. The diagnosis appropriately says the evidence
supports a normal exit race; the fake reproduction demonstrates the mechanism
without pretending to reconstruct an unlogged call.

The code admits only an exact failure-shaped ESRCH as a recovery candidate.
A candidate is not absence proof. The provider checks all available partial
PID/start/UID/real-UID/group/session fields before proceeding; observed reuse,
malformation or escape cannot be erased by a later absence. Leader loss never
recovers through this path. EPERM/EIO, unknown/zero errno, short or malformed
return values, still-present PIDs, stale data and contradictory identity remain
failures.

A non-leader allowance requires a new complete global snapshot showing its
absence, followed by complete recollection of surviving and newly appearing
members. Known members missing between acquisitions receive the same explicit
absence treatment. Closing membership changes trigger bounded recollection.
The original acquisition deadline never moves; there are at most two resamples.
Supervisor draining uses native group/global lists only, with one fixed
0.5-second collection budget, and does not create a ps child inside its group.
Monitor sampling and monitor DONE checking share the same collection logic.

Seen/departed identity history survives successful acquisitions and is not
silently evicted. A retired PID reappearing anywhere visible refuses; an unknown
retired identity is not promoted to a fresh worker. The 512-PID job-lifetime
history limit is conservative and explicit. It may refuse a long/churning
compiler tree; it does not qualify such workloads by analogy with these probes.

Validated partial RSS/footprint sums remain acquisition maxima through retries,
so a previously observed cap crossing is not forgotten when a child exits.
An exited, never-validated resource observation is explicitly null and labelled
unmeasured. Matching present zombies are also labelled unmeasured after identity
validation. Returned aggregate observations do not supply an exited worker's
lifetime peak, exit status, or an atomic group-memory snapshot. No zero-memory
or historical peak inference is warranted from absence.

AST/source comparison confirms the new errno import and NativeReadFailure,
provider collection/error changes, and the supervisor's existing event sink
passed into its provider. All other top-level definitions are unchanged.
`validate_compile_argv` and `read_job` are AST-identical to reviewed v2. Caps,
thresholds, sample age, admission, heartbeat, authentication, signal targeting,
TERM/KILL behavior, latch rules and compile grammar were not relaxed. Signals
still originate only from the continuously live owned supervisor; the new
membership/history code introduces no PID/PGID signalling path.

## Independent pure and native-record checks

- 111 preserved behavioral/admission tests pass against v3.
- All 39 author fake-native tests pass, including boundary subtests.
- 21 independently implemented fake-native cases pass. These use different
  fake identities and a separate adapter, not the author's Scenario helper.
  Cases cover absence plus new-member inclusion, both resamples, partial
  contradictions, leader failure, permission/unknown/short reads, presence
  outside the native group, retained partial cap readings, shared deadline,
  duplicate/negative global shapes and cross-acquisition reappearance.
- Full logs and exact fake inputs/results are preserved. No native library or
  process capability was activated by those checks.

PID 0 was examined deliberately. V3 permits one PID 0 in PROC_ALL_PIDS, forbids
it as an owned-group PID, and refuses duplicate entries, negatives, misaligned
return counts and buffer saturation. The inspected SDK establishes the flavors
and signatures, but does not itself describe all placeholder/race behavior.
ROOT supplied a separate read-only host witness: three global/group pairs
through the reviewed binding. Each global result has 1,996 returned bytes /
499 PIDs, including exactly one zero; each group result has four bytes / one
positive self PID. All have errno 0, no duplicates/negatives and no saturation.

I recomputed those facts from the retained arrays and fed all six arrays through
v3's `_pid_list` using a fake native function. All are accepted; global zero
never becomes an owned worker. This verifies compatibility with the observed
host representation, not atomic enumeration under every future process race.
Unknown/truncated/duplicate shapes continue to refuse. The witness is ROOT's
execution, not this reviewer's native test or a v3 workload invocation.

## Live proposal disposition

The fixed six-job proposal is appropriately small: true, one inherited short
child, an inherited tail, a pair, then two specified additional jobs only if
prior results are healthy. It retains 128-MiB caps, allowance, ordinary fresh
admission, the sentinel, unique identities/logs, bounded deadlines and the
shared slot. It has no numerical case, compiler, signal/pressure injection,
process-group change, large allocation, adaptive search or automatic retry.

Successful fast completion alone cannot prove native recovery executed. Every
observed recovery needs its operation/PID/errno, available identity, fresh
complete absence, unmeasured/measured status and complete recollection evidence.
A refusal stops the remaining sequence. The reported first preflight refusal
therefore leaves operational qualification open. No B02 retry follows merely
from these pure tests, the PID-list witness or this source-review disposition.

## Build, B outcomes and records

The new records preserve the important distinctions:

- The TASK compile attempt timed out in host permission review before process
  creation. It is not a compiler/guard failure or a completed build.
- ROOT performed the first actual build using the prepared one-shot invocation.
  Its workload and guard returned 0. Four resource samples reproduce the stored
  RSS 476,577,792-byte and footprint 350,127,784-byte sampled maxima. The binary
  hash/size and both Cargo fingerprints independently match current retained
  files; enabled features and rustflags are empty. These are sampled figures
  for one small build, not general compiler/scale qualification.
- B01 is selected p128/P256 with 37 rows and one completed workload sample.
  B02 output says selected p256/P512 with 37 forensic rows, but has zero valid
  workload-period resource samples and an unhealthy guard result. The stored
  comparator records have no violations; this file/record review does not
  replace a new complete mathematical certification of the supplied oracle.
- B02 remains guard-failed after ROOT's exact-latch resolution. The raw event
  chronology, retained latch hash and later absence observations agree. The
  later cleanup is not a guard-complete numerical pass. B03–B16 and all C remain
  unrun at this candidate; neither a false publication nor proof closure is
  established by these outputs.

All 33 raw files inventoried across the build/B packets match retained hashes
and sizes; B portable hashes verify. Both output logs, source/actor distinctions,
refusals, input pins and the numerical/guard status separation remain intact.

**Resolved provenance clarification:** the parent build folder's copied
`controller-POSTCHECK.raw.json` is the earlier TASK timeout observation, not a
postcheck written by the successful one-shot controller. ROOT's additive
`ROOT-A0-BUILD/continuation_01/PROVENANCE.md` now says this explicitly, identifies
the immediate 47-input rehash as ROOT's transcript-backed observation and supplies
a separately timestamped current per-file witness. All 47 current hashes match.
The old file/result/seal is preserved; the new witness is not backdated. This
clarification closes the ambiguity found during review and needs no rerun.

**Portable-export correction verified:** both complete pre-correction packet
manifests match their archived originals, including all 24 original entries.
The three identified exports differ only at 31 string leaves: documented runtime
ancestor/root/Python path aliases. Before/after hashes and regenerated portable
manifests agree. No number, result, code, input, executable or oracle fact was
changed. Earlier referenced return/context hashes remain historical seals, with
an explicit mapping to the portable view rather than silent identity rewriting.

The DESIGN continuation remains conditional and unselected, with independent
DESIGN-VERIFY and owning D1/contract decisions outstanding. It does not expand
the case matrix, alter a protected constant, activate repair or claim a realized
false result. The graph preserves the parent, K0, F2a, acceptance and release
holds. Source-only I21 activity is separate from an authorized heavy job.

## Evidence and remaining limits

The 111-path records delta verifies 100 entries across seven manifests;
67 JSON/JSONL and eight Python files parse. The final 32-path delta verifies
27 entries across four manifests; ten JSON and six Python files parse.
All source and new evidence are bound to the stated candidate. Unchanged prior
review/audit packets were checked for faithful integration, not reissued as new
historical execution. SOURCE_SCOPE, FINAL_SCOPE and the focused check JSONs
retain exact provenance; COMMANDS.md states performed checks and limitations.

No remaining actionable source/records finding blocks fan-in of this candidate.
Normal exact-candidate integration checks remain ROOT's responsibility. Native
I/O/scheduling stalls, non-atomic enumeration, unseen escaped/reparented children,
external supervisor loss, sampled peak limitations and broad command/scale
qualification remain. B02's original result stays failed. Live fast-child
qualification and an explicit ROOT numerical grant still precede continuation.
