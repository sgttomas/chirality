# Decision07 B resume — stopped on the newly authorized B02

**Result: GUARD_FAILURE.** Exactly one new B02 ran under guard v3. The guard
returned 2 with
`monitoring-failure:Refusal:ESRCH-without-complete-nonleader-absence:93697`.
The workload returned 0, but that does not make this a healthy guarded case.
The ACTIVE latch remains untouched. B03–B16 were not started; no automatic
retry, repeat, repair, advance or C execution occurred. B01 was not rerun and
the original B02 guard-failed record remains unchanged.

The pinned oracle's subsequent lightweight forensic comparison passes all
37 rows, including scale/class/bound and range checks. B02 output says selected
p256/P512, with p128 rejected at member 1, I-end Ux's force stop rule, zero
corrections and 2,015,063 LME. Its complete probe output is byte-identical to
the original B02 output, SHA256
`a293af61d547adba0ff93fe8d3df3824340f5c9919578e177b0f9e9cddad6c19`.
This is two preserved guard-failed observations, not retrospective promotion,
an ungranted determinism test or proof closure. No false published claim was
found in the available output.

## Guard boundary

The current grant, prompt, guard and qualification hashes verified. All 58
qualification manifest entries passed; its earlier changing-swap preflight
refusal was kept distinct from the six healthy fixed jobs. The two portable
export reissues and their original archived manifests also verified through
`PORTABLE_EXPORT_REISSUE_01.json`; path-only export correction was not treated
as numerical source drift. No ACTIVE latch was present before this job.

Three fresh preflight samples and the prelaunch check passed. The native
failure identifies workload PID 93697, `proc-pidinfo-denied-missing-short/0`,
returned 0, errno 3, with no prior or partial native identity. The monitor's
membership row had identified that PID as an owned child. Its attempted fresh
absence confirmation did not satisfy the guard; STOP followed. The supervisor
recorded workload exit 0 and owned-group TERM intent. Authenticated DONE kept
the failure reason. The completion phase later confirmed complete absence and
labelled PID 93697 **exited-unmeasured**. That later observation did not reverse
the earlier stop. `cases/B02/GUARD_EVENT_TRACE.json` preserves the exact sequence;
complete raw membership/provider logs are retained alongside it. No guard
root-cause repair or policy change is selected here.

Elapsed time including preflight was 2.433 seconds. No workload-period resource
sample completed. RSS 9,093,120 bytes and footprint 6,422,768 bytes are prelaunch
supervisor observations, **not B02 workload or lifetime peaks**. The exited
worker is unmeasured, not zero memory. Minimum observed availability was 71%;
no pressure/swap/cap stop was reported. These limited observations support no
performance or memory-bound claim.

The exact granted child argv was `a1_public_probe B02 100000000 100000000 B`,
with one inherited-group guard-v3 job and the decision06 limits: 512-MiB group
RSS/footprint caps, 128-MiB allowance, 60-second timeout, 128-MiB write budget
and 4-GiB reserve. The small clean environment preserved owner HOME and carried
no seeded-fault or inherited Cargo/Rust controls. No compiler ran.

## Result custody and next condition

New coordination/guard candidate:
`325516a7bb21492458d2c84026db709de8b1b4d9`. Frozen numerical source remains
`3bddc2b05f6106e969c7cf43373b230845c7cc66`; binary remains
`426fb26fb52e8f7781ebef8d0876ba74ba6c025ada4a66b5532423b462a9b386`;
oracle remains `35cf4b9321ebe126693e52ad96ea010bed9f280c3058d02fbae98c17275627be`.
All source/probe/oracle/matrix/lock/binary input hashes match before and after.
ROOT remains the successful compile actor. Previous packets are preserved,
with the explicit prior export mapping respected.

The case folder holds full portable job/registry/monitor/supervisor/output
copies, exact raw-file hashes, before/after input checks and forensic comparisons.
Raw originals remain under `scratch/a1-diagnosis/b-tranche-v3-20260930/B02`
and `logs/a1-b-v3-b02-325516a7-20260930-01` in the bound runtime. Retained ACTIVE
bytes are copied and hashed without changing the canonical latch.

`C_CHECKPOINT.md` states the unchanged partial B/C obligations. There is still
only one clean guarded B result, B01. B03–B16's boundary/O9 controls are unrun;
all eight C sources remain unrun and ungranted. Positive W-plus, theta/charge,
refinement, full-layout acceptance and D2 G5a proof dependencies remain open.

Same native TASK `/root/design_manager/a1_diagnosis` under DESIGN, with no
delegation or role/model override. New writes are confined to this continuation
and owned runtime scratch/logs; prompt scope is not a per-child OS sandbox.
No sealed input/target change, install/network, Git/index write, manual signal,
latch removal or protected criterion change occurred. The supervisor's recorded
owned-group TERM was part of the granted guard, not a separate agent action.

Return to DESIGN now. ROOT must disposition this guard failure/latch before
further execution. This is a stopped checkpoint, not completion of B or C
admission. `SHA256SUMS` seals only this new continuation.
