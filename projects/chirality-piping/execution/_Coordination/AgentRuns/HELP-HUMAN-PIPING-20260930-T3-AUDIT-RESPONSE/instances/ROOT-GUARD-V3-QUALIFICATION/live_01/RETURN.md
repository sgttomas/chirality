# Guard v3 fast-child qualification

ROOT executed the reviewed fixed six-job sequence at candidate
`325516a7bb21492458d2c84026db709de8b1b4d9`, guard SHA256
`b32050c72d0bbad0f69526fc98d1f28dcb1fa131115227a2169db8100d66848b`.
All six completed with guard/workload exit 0, unchanged unrelated sentinels,
and no remaining ACTIVE latch. The sequence is true, one short child,
parent-before-child exit, two children, true, two children.

An earlier first invocation refused during preflight because swap usage fell
by 8 MiB between samples; it launched no supervisor/workload and left no latch.
After the owner reported restored internet, ROOT preserved that result, read
three stable swap values and 74% available memory, and granted a fresh sequence
with unchanged thresholds. It is not an automatic retry or a passing witness.

The tail fixture naturally reproduced the relevant native condition: ps had
worker 89878 as a zombie; proc_pidinfo returned 0/ESRCH. V3 recorded the failed
operation and PID, obtained fresh complete absence, recorded its unmeasured
exit and recollected the surviving membership. The job completed normally.
Other jobs also exercised confirmed departures and native completion draining.
Thus the exit-recovery branch was actually observed, separately from the pure
tests; no artificial PID reuse or escape was induced.

Every job retained the reviewed 128 MiB cap, 64 MiB allowance/write budget,
1 GiB disk reserve, eight-second timeout and three-sample preflight. No model
or compiler ran. The largest sampled group RSS was 61,652,992 bytes. These are
sampled values; an exited-unmeasured process supplies no lifetime memory peak.
Sentinel cleanup used only its retained unreaped direct child handle through
the already backchecked cleanup helper. No latch was manually removed.

RESULTS.json summarizes the seven invocations, including the preflight refusal.
RAW_INVENTORY.json binds 53 original runtime files and their portable copies;
case directories preserve job/controller/monitor/supervisor/workload evidence.
The fixture is copied verbatim from the reviewed proposal. The small controller
and exact argv are retained. Fixed source/controller hashes appear per job.

This supports ROOT deciding a bounded B02 retry and the remaining tiny B cases.
It does not grant arbitrary command trees, K6/VR runners, scale cases, full
DEC-025, a hard memory-peak bound or a numerical/design acceptance. General
unobserved escapes, PID-list non-atomicity and scheduling limits remain.
