# Independent guard and response-record review

**Disposition: records suitable for ROOT fan-in; two actionable P2 compile-admission findings require repair and backcheck. The exact proposed low-memory provider witness and qualification fixtures are suitable for ROOT's next bounded invocation. The guard remains inactive and not live-qualified, and no compiler or numerical run is admitted by this review.**

Reviewer: fresh independent TASK `/root/guard_reviewer`, under HELP_HUMAN
`/root`, using native collaboration. I did not author the reviewed code or
records. Same-model independence is not model diversity. No child was spawned.

Final reviewed candidate: `fe6ca966259d29d8d6ed2f05460400f6cb5d5de0`, against
main `292e123db9117e097c2dfbbecaf7a93de86c3c6b`. Its complete binary diff is
byte-identical to original base `3bddc2b05f6106e969c7cf43373b230845c7cc66` through
original candidate `53a7bad25fef1e1ddfe1a9df21688279f823aaf3`:
`31e6c3590ba01c446133ed5861f0014b8552557a0d8eca649c043891f9e96e1c` (SHA256).
All 109 changed paths have identical original-candidate, final-candidate and
review-time working-tree bytes. `FROZEN_SCOPE.json` preserves every path/hash.
The accepted App documentation merged between bases is outside this response;
identical response diffs establish that it introduced no response-code change.

`Run` means
`projects/chirality-piping/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260930-T3-AUDIT-RESPONSE`.
Guard source SHA256:
`feb0e1508fde6c764eefb85e2b72bc7a597edf86d48307fb646a80a80eac03db`.
All locations below refer to those frozen bytes.

## Actionable findings

### GR-01 — P2: Cargo admission accepts controls in workload arguments

- **Location:** `Run/tools/host_guard.py:722-724`.
- **Trigger:** a compile job uses
  `['/fake/cargo', 'run', '--jobs', '8', '--', '--offline', '--locked', '-j', '1']`,
  with the otherwise valid pinned environment and executable hash. `read_job`
  accepts it because it searches the entire argv for three token patterns.
  Arguments after Cargo's `--` belong to the invoked program. They do not set
  Cargo offline/locked mode or constrain its build jobs; the earlier explicit
  `--jobs 8` overrides the environment's job setting.
- **Impact:** the apparent compile-admission check can accept a command that
  accesses dependency state/network and builds with eight jobs on the M3,
  contrary to the serial, offline, locked compile contract. This is a trusted
  operator command-validation defect; no hostile-input security claim is needed.
- **Evidence:** `check_compile_schema.py` and `compile-schema-results.json`
  reproduce acceptance with fake files and every supplied live capability
  blocked. The properly formed build command also passes as a control.
- **Remedy direction:** interpret Cargo's control-argument portion separately
  from forwarded workload arguments, and reject a command whose effective
  concurrency/offline/locked settings do not meet the declared contract.
  Add pure regressions for forwarded flags and explicit conflicting job options.
- **Blocking scope:** blocks relying on this guard's compile-admission checks
  and requires repair/backcheck for the guard implementation. It does not block
  records fan-in or the qualification-only Python fixtures.

### GR-02 — P2: explicit rustup selectors bypass the environment toolchain pin

- **Location:** `Run/tools/host_guard.py:714-724`.
- **Trigger:** with a rustup proxy executable, a compile job supplies
  `cargo +stable build --offline --locked -j 1` or
  `rustc +stable input.rs`, while the environment still names
  `RUSTUP_TOOLCHAIN=1.97.1`. Both are accepted. Rustup's explicit `+toolchain`
  selector overrides the environment selection. This applies to the proposed
  isolated `cargo/bin` proxy route; an actual direct toolchain binary may
  instead reject that selector.
- **Impact:** when the selected alternative is installed, the command can use
  a different compiler while the guard treats the environment as the exact
  version pin. When absent, auto-install suppression can cause a refusal;
  that does not make acceptance of an installed alternative correct. Exact
  toolchain identity is material to later numerical/layout evidence.
- **Evidence:** both proxy-style argv examples pass the same capability-fenced,
  fake-filesystem reproducer. No Cargo/rustc/rustup command was executed.
- **Remedy direction:** reject incompatible explicit toolchain selection, or
  bind and validate a direct exact-version executable route with a command
  grammar consistent with that route. Cover both Cargo and rustc using pure
  schema tests; continue recording actual executable hashes/version provenance.
- **Blocking scope:** blocks compile admission on the proxy route until repaired
  and backchecked. It does not affect the qualification-only Python fixtures.

No additional actionable containment or records-integrity defect was found.
ROOT owns repair selection. Preserve the sealed v1 source, tests and manifest;
an additive versioned correction can identify what it supersedes without
rewriting the returned evidence. Subsequent source/record changes require
review coverage of the actual candidate. Records fan-in is not an unconditional
merge or operational acceptance of these outstanding implementation findings.

## Guard review and qualification assessment

I read the complete 928-line implementation and all 455 lines of supplied
meaningful tests, plus provider, limit, qualification and serial-driver records.
The ownership design confines group signals to a continuously live supervisor
that created its session. The monitor authenticates the returned leader against
PID/start/UID/session; workers close control/lock handles and reset handlers.
The supervisor rechecks its current group/session/UID before signalling its own
group. Provider-process cleanup uses unreaped direct child handles. No discovered
or historical workload PID/PGID is passed to an external kill fallback.

Denied/malformed/stale observations route to STOP. Lost monitor heartbeats route
to the independent supervisor watchdog. Stop state is sticky; a late heartbeat
cannot undo a stop. TERM has a bounded intended grace before self-group KILL.
The ACTIVE latch remains on uncertain cleanup, guard/resource stops and lost
containment. Normal completion requires authenticated DONE, live leader identity,
empty live membership, ACK and reaped supervisor; a completed failing workload
keeps its actual return code and is not relabelled a passing test.

Sampling starts its age clock before acquisition; its declared 1.5-second
provider deadline, 2-second freshness limit and one-second post-acquisition
interval are distinguished. RSS and physical footprint are separate sums;
availability is an estimate, not reserved physical bytes. Admission subtracts
the full cap plus allowance, refuses projected availability at/below 40%,
requires stable swap admission, and treats new swapouts/growth separately from
historical swap use. Output/event/member/control bounds and their stop paths
are present. Event-limit failures do not disable the supervisor's stop state.

The SDK structures/signatures/constants inspected locally agree with the
binding derivation and all nine recorded SDK header hashes match. Pure ctypes
layout checks are not native ABI execution. I did not independently retrieve
the author's remote XNU source; its unpinned remote-main references remain
supporting documentation, not host-kernel provenance.

The proposed qualification sequence is proportionate: read-only providers
first; clean completion; bounded allocation; inherited sleepers; TERM-ignore;
cap crossing; monitor loss; visible escape; independent sentinel; and lock/latch
refusal. It preserves new logs, actual timings, exact identities, refusal cases
and source/input hashes. The fixture's explicit allocation is at most 64 MiB;
interpreter/supervisor overhead remains additional and is correctly relevant to
the proposed group caps. Failed prelaunch admission is an incomplete case, not
proof of termination behavior. Missing metrics or inadequate identity/latency
evidence must keep qualification open, as the plan already states.

**Suitable next step:** ROOT may execute exactly that bounded qualification
under its existing permitted host boundary and fresh headroom checks. This
assessment creates no new approval-token interface and grants no compiler/model
scope. Repairing GR-01/02 and backchecking the new guard must precede compile
admission; later direct cargo qualification and all K6/VR/full-driver coverage
remain separate. No live test occurred in this review.

## Complete frozen-diff and records coverage

All 109 additions are scoped to this response's AgentRuns directory and its
WorkGraphs file. No product, test, instruction, historical audit/T3 packet or
other project path changes in the response diff. Coverage was scaled by risk:

- Deep code/control review: guard implementation, supplied tests, compile-schema
  validation, SDK declarations, guard brief, provider/limit/live-plan records,
  and proposed DEC-025 serialization boundaries.
- Coordination and claim review: work graph, activation, three ROOT decisions,
  actual launch records, parent/child context/return records, V0 disposition and
  replay/process errata, manager integration returns, runtime binding/setup,
  B0 scope/mapping and environment/recovery accounts.
- Provisional technical packets: A0 matrix/brief/return and derivation context,
  initial DESIGN framing, I21 return/formula/source arithmetic and open-phase
  plan/evidence descriptions. These are assessed for scope, provenance and
  claim limits; this review does not substitute for A0 execution or K0-V1's
  independent complete-formula review.
- Data-heavy supporting files: all JSON parses, all Python syntax trees, every
  new manifest entry and blob identity; selected stored-result counts and
  input/snapshot hash cross-checks. I did not rederive every provisional phase
  inequality or rerun historical numerical audits/gates. No such acceptance
  is claimed by the candidate.

V0's post-merge status, abstract proof gap and realized-source limitations are
faithfully integrated. The replay erratum pins both script and inputs and
preserves originals. M5 evidence remains unavailable-for-now; new M3 evidence
has distinct custody. Decision 03 records the owner's latest safe-recreation/
rerun authorization without waiving protected criteria, gates or acceptance.
The A0 24-case matrix remains an unexecuted plan; source validation, W-plus and
selection predicates are outstanding. K6c N0 remains explicitly incomplete,
with capacity/finish/layout/A1 obligations open. Stored 36 admission/204 heap
comparisons do not turn N0 into an M3 grant.

Historical environment absence and older launch/return statuses remain dated
observations, supplemented by later records. Actual native launches are
explicitly distinguished from draft briefs and proposed launches. Prompt write
fences are not represented as OS-enforced per-agent sandboxes. Dependency
TBD/PENDING states, bounded VR mapping limits, parent holds, and release/
engineering acceptance remain unchanged. No unsupported solver-success or
whole-deliverable readiness claim was identified.

## Independent checks and residual risk

- Supplied pure suite: **41 tests passed**, raw output in `pure-tests.log`.
- Pure compile-schema witnesses: valid control and three invalidly admitted
  argv forms reproduced; `compile-schema-results.json` retains exact inputs.
- **9 new manifests / 83 entries verified**, no mismatch.
- **42 JSON files parsed; 10 Python files parsed as syntax**, without executing
  historical inventory/replay/provider scripts.
- **9 SDK header hashes verified** against the recorded derivation.
- **36 snapshot-descriptor entries match frozen product Git blobs**; the live
  runtime snapshot was not inspected or activated.
- **64 I21 pinned inputs match**; stored summary has 33 models, 36 admissions,
  66 K6B summaries, 204 heap comparisons and no reported negative margin. This
  is an integrity/consistency check, not rerun or final-bound acceptance.

No live providers, signals, guard, sockets, fork, compiler/model, package install,
network access or Git/index mutation was used. All writes are in this review
folder. Read-only Git was explicitly confirmed by ROOT after the abbreviated
launch wording was clarified. Commands and limitations are in `COMMANDS.md`;
actual instruction origins/hashes and parent addenda are in `CONTEXT.json`.

Remaining risks include real ABI/provider permission behavior, native call/I/O
stalls, actual fork/flock/channel/handler operation, sampled peaks/stop latency,
compiler-child races, and performance/usability under conservative refusals.
The implementation explicitly cannot guarantee detection of an unobserved
escaped double-fork or safely recover after external supervisor SIGKILL. Hostile
same-UID interference is outside its trust model. Disk sampling covers the log
volume rather than imposing a hard quota; later job grants must keep target
volumes/write budgets within the qualified scope. No current result supports
large workloads, K6/VR separate-group runners, full DEC-025 or scale admission.
