# Guard v2, live evidence and incremental records backcheck

**No unresolved blocking review findings in candidate
`888e388812f65dffce4428c96c18d2ddc8d2ae61`. GR-01 and GR-02 are closed on
host_guard_v2.py. The replay-controller error path discovered during this
continuation, GR-03, is closed on qualify_case_v3.py. The candidate is suitable
for ROOT's records/guard integration, subject to the normal actual-candidate
checks. The evidence supports one separately budgeted, serial, offline/locked
tiny direct-compile trial; direct Cargo operation is not yet qualified by an
observed run.**

This is the same independent TASK `/root/guard_reviewer`, resumed by ROOT for
backcheck. All new reviewer writes are confined to this continuation. Original
review and historical packets remain unchanged. No live provider, signal,
guard, compiler, model, network, install or Git/index mutation was performed.

## Candidate and full incremental coverage

Parent reviewed candidate:
`fe6ca966259d29d8d6ed2f05460400f6cb5d5de0`.
Current candidate:
`888e388812f65dffce4428c96c18d2ddc8d2ae61`.
Upstream base:
`292e123db9117e097c2dfbbecaf7a93de86c3c6b`.

The complete incremental diff contains 181 paths: 180 additions and one work
graph update. Its binary-diff SHA256 is
`b983fddcc239567f4d8d654c31d27d35fd998cdbcd0756a6277555e413275f37`.
The full response diff from upstream has SHA256
`df805bf7cdf63f438e36283dbbbf0bb7629d6700298a848ea5bd2f8f10e49c52`.
`FINAL_SCOPE.json` retains every incremental path, candidate byte count/hash
and working-tree comparison. All match. Git preserves the canonical diff;
no duplicate whole-diff snapshot is retained.

Coverage combines the original complete-diff review with this complete
incremental review. Risk-scaled coverage here includes:

- Detailed source and regression backcheck of the v1-to-v2 guard change,
  original behavior tests rebound to v2, and independently selected argv cases.
- Full source review of the provider witness, executed fixture/controllers,
  monitor-stall extension and additive controller finalizer correction.
- Independent integrity and calculation checks of every qualification case,
  original runtime file and portable evidence copy, including actual ownership,
  sentinel, stop, latch and timing records.
- A0 preparation/probe/command/feature/lock/provenance and manager integration
  claims; the 24-case/880-row matrix's state and structure. Numerical theory,
  complete oracle certification and actual solver outcomes are not substituted
  by this guard/records review. The packet explicitly remains UNRUN and
  compiler-unverified.
- DELIVERY's source-only K0 continuation, unapplied private-layout proposal,
  source/input and patch identities, Rust-src setup records, and the graph's
  continued holds. No new final E_max or measured layout claim is made.
- Decision 04, actual review/repair/A0 launch/continuation records, preserved
  first review packet, and all supporting JSON/JSONL/Python/TOML and manifests.
  Large data blobs receive integrity, structure and claim-consistency checks;
  this review does not redo K0's incomplete theory or historic numerical gates.

No canonical product or historical instruction/audit/T3 source changed. The
A0 and K0 code artifacts are explicitly inert preparation/proposals under
response-owned paths. Prior reviewer-authored evidence is checked for faithful
integration and preservation, not presented as an independent review of itself.

## GR-01 and GR-02 closure

V2 source SHA256:
`533a6f7506da4e031d8a824a27b4e9c496f374a3af8b7e98c72da55e8bbc26b5`.

The complete source delta adds `validate_compile_argv` and calls it from the
existing compile branch of `read_job`. Independent AST comparison shows every
other top-level statement, function and class unchanged. Ownership, sampling,
heartbeat, signals, logging, latch, environment and hash handling are preserved.

**GR-01 closed:** Cargo controls are parsed only before `--`; values are consumed
explicitly; offline, locked and exactly one effective jobs=1 option are required.
Duplicate/contradictory job options and operand/option ambiguity refuse. The
original `--jobs 8 -- --offline --locked -j 1` witness now refuses. Forwarded
arguments cannot satisfy the Cargo control requirements.

**GR-02 closed:** an explicit leading rustup selector is either absent or exactly
`+1.97.1`. The original Cargo/rustc `+stable` witnesses refuse; duplicate or
misplaced selector-like controls refuse. The permitted canonical selector does
not assert that a direct binary accepts proxy syntax or prove a binary version.

The deliberately narrow grammar is documented: finite supported Cargo
subcommands/options; no aliases/unknown configuration controls; explicit
supported forwarding. Rejecting other valid Cargo syntaxes is intentional
scope restriction, not a silent claim of full CLI compatibility. Forwarded
program/compiler/test behavior still needs the exact job's reviewed scope.

Passed checks:

- 41 original behavioral tests against v2, original test bytes unchanged.
- 70 author repair tests.
- 24 independently selected fake-file argv witnesses, including original
  failures, conflicting aliases, separator/value ambiguity, canonical selectors,
  direct-rustc syntax and the proposed compiler-forwarding shape.
- All 15 repair manifest entries.

Only pure fake files/control/provider capabilities were used. Executable hash
checks and environment checks remain required; actual isolated executable,
RUSTC/wrapper/configuration and toolchain provenance are separate obligations.
A0's command plan makes those obligations explicit. An argv pass alone grants
no compilation or numerical execution.

## Live evidence assessment

The live tests were ROOT's execution of reviewed v1, with SHA256
`feb0e1508fde6c764eefb85e2b72bc7a597edf86d48307fb646a80a80eac03db`, at the parent
candidate. This continuation independently inspected their retained files;
it did not perform those live operations. V2's unchanged control/provider code
supports carrying these bounded control observations forward. It does not
relabel v1 records as a v2 or direct-Cargo execution.

`LIVE_CHECKS.json` recomputes and checks:

- All 93 qualification manifest entries and all 83 original runtime file hashes
  and byte counts, plus every portable-copy digest.
- Matching controller/event copies, source/job-spec/registry bindings, all
  eight unchanged sentinel identities outside the owned group, empty controller
  error lists and absence of all recorded original PIDs at final inspection.
- Three preflight samples per case, signal identities matching the registered
  supervisor, exact preserved latch hashes and the expected lock/latch refusals.
- Three stable provider-witness identities, normal pressure, stable swap and
  positive separately obtained own RSS/footprint readings.
- Stored sampled peaks, sample-start gaps, stop/escalation/drain timings and
  controller observation intervals from the event timestamps.

The clean and 16-MiB cases complete normally. The sleeping and TERM-ignore
cases exercise runtime stops. TERM-to-KILL for the ignoring child is
2.001229 seconds. The cap case reaches sampled RSS 94,208,000 bytes and stops
0.017527 seconds after the request; its 27,099,136-byte nominal-cap overshoot is
explicit. The largest observed normal start gap is about 1.076499 seconds.
These observations do not impose hard memory/latency bounds.

Monitor loss takes the immediate `ConnectionResetError` control-loss path;
it is not a stale-heartbeat witness. The separately versioned monitor-stall
case keeps the channel open and records `heartbeat-loss` TERM 3.024372 seconds
after SIGSTOP, group-drained at 3.048339 seconds, and independently observed
absence of both workload PIDs at 5.543832 seconds. Its final self-KILL after
2.543511 seconds of TERM is correctly disclosed while the workload was already
drained; it is not claimed to meet a 2.5-second escalation target.

The visible-escape case records a refusal and stops only the original group;
the escaped child self-expires. It does not establish general escape containment.
Stopped/uncertain jobs preserve their exact latches and refuse a new launch.
ROOT's separate latch-resolution statements are explicitly ROOT-reported fresh
checks; their exact preserved latch hashes and recorded prior exit observations
verify. A file-only check finds no unresolved ACTIVE at backcheck time.

The three provider samples and eight small cases support the limited next
trial. Actual direct Cargo child churn may still cause conservative identity-race
refusals, and the compiler's memory/output behavior is not inferred from Python
fixtures. ROOT must bind a fresh explicit job, source/executable/lock hashes,
correct isolated environment, current headroom, allowance/cap/disk/time budgets
and one heavy slot. Preserve all refusals; no automatic retry, larger model,
K6/VR, layout-overlay execution or full DEC-025 grant follows.

## GR-03 — P2 replay-controller cleanup; reproduced and closed

Original location:
`Run/instances/ROOT-GUARD-QUALIFICATION/qualify_case_v2.py:154-159`.
Here `Run` is the response AgentRuns directory identified by the parent review.

An exception after SIGSTOP but before the ordinary `monitor.kill()` enters a
finalizer that sends TERM to the stopped direct monitor and then waits. A
stopped process cannot handle the pending TERM; `TimeoutExpired` escapes,
skipping sentinel cleanup and controller-result persistence. This is an
unexercised replay error path, not a failure observed in the successful live
packet and not a guard-core defect.

`reproduce_stopped_cleanup.py` executes only that finalizer AST with fake
monitor/sentinel/storage and reproduces both skipped actions. ROOT supplied
an additive correction at
`ROOT-GUARD-QUALIFICATION/continuation_01/qualify_case_v3.py`, SHA256
`119940763e3092fa61ca397d0d647f389f03917b880bfeef6cb2a6d310203cea`.
It kills only its still-unreaped direct monitor handle, isolates per-child
cleanup failures, provides a direct-handle sentinel fallback and preserves
unconfirmed cleanup errors while continuing to result persistence.

The five supplied pure tests pass. `check_repaired_cleanup.py` additionally
executes the actual v3 helper/finalizer AST against the same stopped-monitor
trigger and a persistent wait-failure variant. Both reach sentinel cleanup
and result persistence; the failure variant retains unconfirmed cleanup.
The four-entry correction manifest verifies. **GR-03 is closed for v3; use v3
for future replay.** Executed v1/v2 controller bytes and evidence remain intact.

## Incremental records findings and checks

No additional actionable record or scope defect was found. A0's authored
version-4 two-package lock is truthfully distinguished from Cargo generation
and supersedes the inadmissible generate-lockfile proposal through an additive
grant. It remains to be validated by an offline locked build. All 24 cases are
UNRUN, with 880 stored mathematical truth rows; no selected publication, solver
counterexample or proof closure is asserted.

K0 source work is a manager-prepared continuation, not an unrecorded TASK launch.
The layout overlay remains unapplied/uncompiled; its source preimage, overlay,
postimage append and patch hashes agree, and it lists 126 proposed type rows.
Rust-src availability is distinct from a completed phase/capacity proof. The
full formula, final A1 impact and measured W1 admission remain open. The graph
updates execution state without promoting dependencies, waiving criteria or
claiming a heavy compiler/model run already occurred. Owner-held and parent
holds, unavailable-for-now M5 originals, and new-evidence provenance persist.

Mechanical incremental checks pass: 9 manifests / 169 entries, 98 JSON or JSONL
files parsed, 15 Python syntax trees parsed, two Cargo TOML files parsed, 181
candidate/worktree paths identical. Exact outputs are in INCREMENTAL_CHECKS.json.
Historical/current provider scripts, A0 oracle and K0 helpers were not run by
this reviewer. ROOT separately reported candidate checks/GEN-8; this review
neither re-witnesses nor substitutes for those merge gates.

Residual limits remain scheduling/I/O/native-call stalls, sampled peaks,
unobserved reparent/escape behavior, external supervisor loss, trusted input
immutability/configuration and command-type qualification. There is no new
unresolved blocker for the bounded record/guard slice or for ROOT to select
one tiny direct-compile trial within these limits. Broader numerical/design,
release and final acceptance remain outside this disposition.
