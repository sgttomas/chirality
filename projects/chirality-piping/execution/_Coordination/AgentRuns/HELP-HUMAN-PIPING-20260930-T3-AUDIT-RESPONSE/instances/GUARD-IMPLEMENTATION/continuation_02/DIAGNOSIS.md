# Frozen diagnosis before v3 implementation

Skill: `.agents/skills/software-defect-diagnosis/SKILL.md`, SHA256
`7e423dfd24132c33d3aa8fe6994bf17a1def966c396723f6bd72ac8d2442112b`.
The continuation brief separately authorizes this narrow implementation.

The observed B02 workload exited 0 at 551960.4548745. Its monitoring snapshot
logged at 551960.457240541 contained supervisor 25394 and worker 25401 in state
Z. V2 requested STOP at 551960.4583125 with
`monitoring-failure:Refusal:proc-pidinfo-denied-missing-short:3`.
The supervisor remained live, sent TERM to its own group, drained, and returned
DONE. No workload-period resource sample completed. The later passing numerical
comparison is forensic only; it does not repair that failed guard run.

The original refusal string lacks PID and native call phase. This packet does
not infer an exact failed call/PID from timestamps. ROOT supplied the normal
child-exit race as the diagnosis basis; independent retained evidence strongly
supports it. The deterministic fake below demonstrates the code mechanism, not
a reconstruction of a native call that was not logged. ROOT separately checked
absence and archived the exact latch in ROOT-B02-INCIDENT. This TASK only read
that record and preserves it and B02 bytes; there is no retry or latch action.

`reproduce_v2.py` freezes a complete fake table containing a live leader and Z
worker; fake libproc returns ESRCH for that worker. Capability-fenced execution
produces exactly `proc-pidinfo-denied-missing-short:3`; the result is preserved
in `v2_reproduction.json`. No live provider or process was used. The earliest
code divergence is v2 `MacProvider.identity`: all non-full proc_pidinfo results
are collapsed into Refusal before membership can be refreshed. `group` and
`live_group` propagate it unconditionally. The monitor then stops an otherwise
completed worker; a similar race is possible during completion draining.

Viable alternatives in the historical short string were permission failure,
short native response, leader disappearance, identity reuse, or failed query
at another identity-read boundary. None may be accepted by treating an exception
or Z state as zero memory. V3 must preserve their refusal semantics and capture
operation/PID/errno/return size and available identity provenance explicitly.

Selected bounded repair: distinguish only exact ESRCH failure-shaped native
reads from other failures. For a non-leader candidate, refresh complete global
absence evidence and the complete owned membership, then restart collection
under the same original deadline. Bound retries and remeasure surviving/new
members. Known members disappearing between successful snapshots get the same
absence confirmation and explicit exited/unmeasured record. Never discard a
new member or silently convert an unavailable sample into zero. Any identity
change, reuse, visible escape, leader loss, remaining presence, uncertain or
stale evidence, short read, permission/unknown errno, or repeated churn refuses.

Maintain conservative partial metric maxima within an acquisition so a valid
large reading from a member that subsequently exits is not forgotten by a
retry. Unvalidated resource bytes and never-measured exits remain unmeasured.
No all-time peak or historical workload measurement is fabricated. The change
needs fake-native boundary/negative tests and independent backcheck, then a
small separately granted fast-child live witness before any numerical retry.
