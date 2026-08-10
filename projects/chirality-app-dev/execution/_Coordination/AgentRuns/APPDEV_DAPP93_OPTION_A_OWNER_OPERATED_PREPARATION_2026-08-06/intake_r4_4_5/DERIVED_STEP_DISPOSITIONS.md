# D-APP-93 R4.4.5 derived step dispositions

Status: `FROZEN DERIVATIVE — TERMINAL FAILURE ROUTE`

These dispositions are intake judgments, not owner-entered PASS claims.

| Steps | Derived disposition | Evidence/reason |
|---|---|---|
| 1-8 | PASS | Approved operations occur once in order; C1146 exits are zero; baseline, candidate, lock, archive, and raw config identities reproduce. |
| 9 | PASS | C1105-C1107 complete outputs exist; each exit sidecar is exactly two records with `command_exit=0`, `tee_exit=0`; C1146.09 is zero. The disclosed C1105 fifth phantom filename remains the accepted packet erratum and did not create a hidden producer or retry. |
| 10 | FAIL | C1108 complete output exists but the exactly-two-record sidecar is `command_exit=1`, `tee_exit=0`; output records the stale D-APP-92 `electronDist` path. C1146.10 merely records the following printf's zero exit and cannot override C1108 failure. |
| 11-22 | NOT_RUN | Package construction failed before package inspection, launch, direct-child binding, C196, signal, trace, or C197. |
| 23 | PASS | C1147.01/.02 created the previously absent returned parent once; C1146.23 is zero. |
| 24 | NOT_RUN | Selected pre-C196 branch prohibits C1144 and C1130. |
| 25 | PASS | C1149.07-.17 copied all eleven applicable evidence primaries once; C1146.25 is zero. |
| 26-27 | NOT_RUN | No helper or GUI PID existed; C1128/C1129 were inapplicable. |
| 28 | PASS | C1131-C1139 restored seven baselines, removed five additions and named derivatives; C1146.28 is zero. |
| 29 | PASS | C1140 reproduced eight rollback hashes exactly; C1141 emitted zero bytes; C1146.29 is zero. |
| 30 | PASS | C1150.R preceded C1148 per the ruled erratum; C1151.T, C1153.01, C1142, C1143, and C1146.30 completed; precleanup copy is byte-identical; temp root is absent; C1146.30 is last. C1151.F then froze the through-cut transcript. |
| 31 | PASS_AS_HANDOFF_INTENT | C1152 completed all 31 literal rows and truthfully recorded `READY_FOR_RAW_RETURN`; C1154.03 froze the form; all other applicable sidecars reproduce; intake observed the directory. This does not turn the run into `PASS_COMPLETE`. |

No unapproved, duplicated, retried, hidden, or out-of-order executable
operation was found through the cut. The route's only ordering variance is the
explicitly ruled C1150.R-before-C1148 packet erratum in
`R4_4_5_STEP10_FAILURE_ROUTE_DISPOSITION.md`, SHA-256
`659089421a760411861bad78d8d0087f3905c32afc8f8b734d39d9c82653043f`.
C196/C197 and `lldb-transcript.txt` were validated separately as `NOT_RUN`;
post-cut C1152/C1154-C1157 are not CONTROL transcript requirements.
