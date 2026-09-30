# B-tranche return — stopped at B02 guard failure

**The tranche is stopped.** B01 completed successfully under the guard. B02
produced numerical output but failed guard monitoring; its ACTIVE latch remains
untouched. B03–B16 and C17–C24 are **UNRUN**. No retry, repeat, repair or advance
occurred. No false published claim was found in the two available outputs.

| Case | Numerical output | Exact comparison | Guard disposition |
|---|---|---|---|
| B01 | Selected p128/P256; zero corrections; 1,088,017 LME | 37/37 rows pass; no range, scale, class or bound discrepancy | Guard/workload exit 0; healthy completion; latch cleared |
| B02 | Output says Selected p256/P512; p128 force end-action stop-rule rejection; zero corrections; 2,015,063 LME | Forensic comparison of preserved output: 37/37 rows pass; no discrepancy | Guard exit 2, workload exit 0; identity-query monitoring failure; latch retained |

The B02 stop reason is exactly
`monitoring-failure:Refusal:proc-pidinfo-denied-missing-short:3`.
Three fresh quiet preflight samples passed, and STARTED was recorded. The
supervisor recorded worker exit 0 shortly before the monitor requested STOP;
the supervisor then recorded owned-group TERM intent and returned authenticated
DONE with the same monitoring-failure reason. The controller completed. This
ordering is consistent with a short-lived-process observation race, but the
exact failed identity query is not identified in the error string; no new
guard root-cause or repair is claimed. ROOT owns latch disposition and further
host work. No manual signal or latch cleanup was performed by this TASK.

The pinned independent comparator was deliberately run on B02's already-produced
output after stopping, as lightweight forensic analysis only. Its passing
numerical comparison does not make the failed guard run a clean case pass.
`cases/B02/CASE_RESULT.json` preserves the original stop before comparison;
`FORENSIC_RETURN.json` and `FORENSIC_COMPARISON.json` are the additive analysis.

B01's exact driver `5h/4` publishes as `h`; its coupled translation scale is
`2^-974` and the zero displacement magnitudes carry `2^-1038`. This is a
selected source exhibiting the expected publication/coupling behavior with
honest rows, not a false-claim witness. `C_CHECKPOINT.md` reassesses the C
hypotheses and states the missing B boundary/O9 evidence. Positive W-plus,
theta, charge, refinement and D2 G5a consequences remain open. No C grant,
design amendment, repair or proof closure is inferred.

## Host and evidence

Both jobs used the exact granted binary and `Bxx 100000000 100000000 B` argv,
the canonical reviewed v2 guard in inherited-group mode, unique job IDs, a
small explicit environment preserving owner HOME, and the granted 512-MiB
RSS/footprint cap, 128-MiB allowance, 60-second timeout, 128-MiB disk budget
and 4-GiB reserve. Each took three fresh preflight samples. Observed available
memory was at least 73%; these observations do not reserve host memory.

B01 took 2.964 seconds including guard/preflight and had one workload-period
sample: group RSS 9,715,712 bytes and footprint 6,996,328 bytes, including its
supervisor and observed worker. These are sampled peaks, not true maxima or a
performance claim. B02 took 2.421 seconds including guard/preflight; no valid
workload-period resource sample completed. Its 9,043,968-byte RSS and
6,373,616-byte footprint figures are prelaunch supervisor observations only,
not B02 workload peaks. No resource cap or pressure stop was reported.

Per-case folders retain complete portable copies of job/controller/guard logs,
registry, stdout/stderr (probe stdout/stderr are merged by the guard), full
row comparisons, pre/post hashes and exact raw-file inventory hashes. The
raw originals remain in the bound runtime's owned scratch and canonical job
logs. B02's retained ACTIVE bytes and hash are preserved; no latch was removed.
`TRANCHE_STATUS.json` names every completed, guard-failed and unrun source.

ROOT, **not this TASK**, performed the preceding successful compile. Its
14-entry `ROOT-A0-BUILD` packet verified against RESULT hash
`48536deede0c073e390807b55d5fffecec9534566bfdbca5b9c254d7aa595bb4`;
fingerprints show no enabled features. The historical child compile-timeout
packet remains unchanged. No compilation occurred in this B tranche.

Numerical source stays `3bddc2b05f6106e969c7cf43373b230845c7cc66`;
coordination/build candidate is `888e388812f65dffce4428c96c18d2ddc8d2ae61`.
Pre/post checks preserve the 36-file source snapshot, binary, probe, oracle,
matrix, lock and earlier sealed packets. Binary SHA256 is
`426fb26fb52e8f7781ebef8d0876ba74ba6c025ada4a66b5532423b462a9b386`;
oracle SHA256 is `35cf4b9321ebe126693e52ad96ea010bed9f280c3058d02fbae98c17275627be`.
Actual HEADs and authority/instruction hashes are recorded in `CONTEXT.json`.

Same native TASK `/root/design_manager/a1_diagnosis`, resumed under DESIGN
without model/role override or delegation. Writes are confined to this new
continuation and owned runtime scratch/logs; the shared prompt fence is not
a separate per-child OS sandbox. No sealed source, target, lock, binary or
oracle was changed; no install, network, Git/index write or protected limit
change occurred. Guard-owned native queries/control occurred only within the
two separately admitted job processes.

Return to DESIGN now. The guard failure/latch requires ROOT's disposition
before further execution. This manifest seals the partial checkpoint, not
completion of B01–B16 or admission of C17–C24.
