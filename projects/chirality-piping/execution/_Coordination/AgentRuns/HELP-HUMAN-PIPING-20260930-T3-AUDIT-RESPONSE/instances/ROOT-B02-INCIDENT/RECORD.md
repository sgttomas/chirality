# B02 guard exit-race incident and disposition

The partial B packet is preserved in A1-DIAGNOSIS/continuation_03. B01 completed
cleanly at p128/P256: 37 honest rows, 1,088,017 LME, no corrections. Its raw
rotation truth 5h/4 publishes h and its published translation scale is 2^-974.
This is a selected scale-construction witness, not a false-publication result.

B02 emitted a selected p256/P512 result and exited 0; its 37 forensic row
comparisons pass. The p128 force end-action stop rule rejected before escalation;
total work was 2,015,063 LME with no corrections. However, its guard failed
on proc-pidinfo errno 3 before any complete workload resource sample. It remains
**GUARD_FAILURE**, not a completed guarded numerical check. B03–B16/all C are
unrun. No false solver publication is established.

Job: `a1-b-b02-888e3888-20260930-01`, candidate
`888e388812f65dffce4428c96c18d2ddc8d2ae61`, unchanged probe/source and guard v2.
The recorded monotonic sequence is:

- 551960.4548745: supervisor records worker 25401 exit 0;
- 551960.457240541: ps snapshot lists supervisor 25394 and worker 25401 as Z;
- 551960.4583125: monitor reports proc-pidinfo-denied-missing-short:3;
- 551960.475195458: live supervisor sends its own group TERM;
- 551960.562390708: group-drained with original worker exit 0;
- 551960.59698075: final ps snapshot contains only the supervisor;
- 551960.598573291: monitor records guard unhealthy/result 2, latch retained.

This supports a normal zombie/reaped-child sampling race. v2's error text does
not itself identify the failed PID; the table/lifetime evidence supplies the
causal context. The source repair must distinguish confirmed disappearance
from permission loss, reuse, escape, stale data or leader failure.

ROOT subsequently read a fresh complete process table: monitor 25362,
supervisor 25394 and worker 25401 were absent, with no live member of the
registered group. ROOT moved only this exact ACTIVE file into its job evidence,
without signalling any process. LATCH_RESOLUTION.json retains that read and
ACTIVE.resolved.json preserves the original bytes. Cleanup does not promote
the earlier guard-failed numerical run.

ROOT granted DELIVERY's original guard TASK a source-only additive v3 repair
under `tools/host_guard_v3.py` and GUARD-IMPLEMENTATION/continuation_02. The
other TASK is I21 source closure. No live guard/model retry is granted. Preserve
resource/age/ownership limits and fail closed on unknowns; any disappearance
handling requires bounded fresh absence/membership evidence and provenance.
Independent backcheck and a small relevant live qualification precede B02 retry.
All v1/v2 source and evidence remain unchanged. No product path was changed.
