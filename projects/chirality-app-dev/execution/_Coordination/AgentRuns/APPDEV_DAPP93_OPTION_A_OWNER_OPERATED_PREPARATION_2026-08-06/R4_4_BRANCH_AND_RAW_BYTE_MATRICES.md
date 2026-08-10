# R4.4 branch/precondition and raw-byte matrices

Status: `COMPLETE — ALL REQUIRED ROWS SATISFIABLE`

R4.4.6 binds every successor return path in this unchanged route matrix to
sibling `returned_r4_4_6/`. Accepted predecessor `returned/` remains immutable
and excluded; branch prerequisites and raw-byte semantics are otherwise exact.

## Branch and precondition matrix

| Class | Entry fact | Through-cut route | Finite tail / satisfiable result |
|---|---|---|---|
| Pre-C1070 | C1067 succeeded; later preflight failed; no fixed root | C1147; C1150.R/C1151.R; failure marker/cut; C1151.F | C1152 readiness/non-success; applicable hashes; intake receipt; no rollback/temp cleanup |
| Partial C1070 | some fixed-root dirs exist; no product write; live CONTROL shows no C1079 input | phase-valid C1151.T/R; applicable C1149; C1150.R/C1153.01 and all applicable then-produced evidence returned before C1142; C1142-C1143; cut/C1151.F freeze the history | C1152 later crosschecks; applicable hashes; intake receipt; never rollback |
| Incomplete baseline | C1070 complete; C1071-C1078 incomplete; no C1079; live CONTROL shows no C1079 input | C1147/C1149; C1150.R/C1153.01 and all applicable then-produced evidence returned; C1142-C1143; cut/C1151.F freeze the history | C1152 later crosschecks; applicable hashes; intake receipt; never rollback |
| Post-first-write/pre-C196 | at least C1079 wrote; C196 never began | C1147/C1149; C1150.R/C1153.01; exact-PID cleanup; C1131-C1141 rollback proof; all applicable then-produced evidence returned; C1142-C1143; cut; C1151.F; no C1144/C1130 | C1152 later crosschecks; hashes; intake receipt; temp retained on failure |
| Post-C196 | C196 began; C197 safely possible/completed | exact C1145→C1144→C1130; C1151.T; C1150.R/C1153.01; exact-PID cleanup; C1131-C1141 rollback proof; all applicable then-produced evidence returned; C1142-C1143; cut; C1151.F | C1152 later crosschecks; C1154.03 first; remaining hashes; intake receipt |
| Destination occupied | C1145.01 or C1147.01 nonzero | no returned write/reuse/alternate; retain state | no returned tail; out-of-band notice; later `STOP_INCOMPLETE` |
| Prohibited content | protected bytes identified before transfer | no affected export/copy; retain source | only non-sensitive safe tail; governed redaction |
| Pre-cut copy failure | named C1130/C1149/C1153 copy nonzero | retain temp source, partial destination, CONTROL state | mandatory rollback when legal; no C1142 |
| Post-cut hash failure | named C1154-C1157 hash nonzero | retain returned primaries and produced sidecars | no retry/form edit; temp may already be validly absent |
| Cleanup/rollback failure | exact cleanup/rollback/proof nonzero | truthful failure marker/cut; safe C1151.F when legal | safe form/hash/receipt only; retain temp/product state |

The terminal cut is C1146.30, after cleanup/final-absence outcomes. C1150.R
and applicable C1153.01 precede destructive temp cleanup and the cut, so all
sources are live and both inputs appear in CONTROL. C1151.F exports complete
through-cut bytes and is followed by no CONTROL input. The finite post-cut
tail is C1152 form completion, C1154.03 form freeze, remaining applicable
whole-file hashes, and actual intake-observed receipt. Neither transcript nor
form is required to contain its own later preservation acts. C1152 is a later
observation/crosscheck and never a C1142 prerequisite.

## Ordinary and partial raw-byte producer/copy/hash matrix

| Primary raw object | Producer/export | Ordinary copy-to-returned | Pre-C196 copy-to-returned | Whole-file raw SHA stdout |
|---|---|---|---|---|
| `lldb-transcript.txt` | C1144 Terminal export | direct returned C1144 | not available pre-C196 | C1154.01 |
| `control-transcript.txt` | C1151.F Terminal export | direct returned C1151.F | direct returned C1151.F | C1154.02 |
| `control-transcript-precleanup.txt` | C1151.T or C1151.R | C1153.01 from temp | C1153.01 or direct C1151.R | C1157.01 |
| `completed-evidence-return.md` | pre-cut C1150.R + post-cut C1152 | direct returned C1150.R | direct returned C1150.R | C1154.03 first post-form-freeze hash |
| `helper.stdout.txt` | C1114 redirect | C1130.01 | C1149.01 when produced | C1155.01 |
| `helper.stderr.txt` | C1114 redirect | C1130.02 | C1149.02 when produced | C1155.02 |
| `helper.pid` | C1114 printf redirect | C1130.03 | C1149.03 when produced | C1155.03 |
| `gui.stdout.txt` | C1117 redirect | C1130.04 | C1149.04 when produced | C1155.04 |
| `gui.stderr.txt` | C1117 redirect | C1130.05 | C1149.05 when produced | C1155.05 |
| `gui.pid` | C1117 printf redirect | C1130.06 | C1149.06 when produced | C1155.06 |
| `c1103.sha256.txt` | C1103 whole-file shasum redirect | C1130.07 | C1149.07 when produced | C1157.02 |
| `c1104.electron-builder.runtime-helper.json` | C1104 literal cp | C1130.08 | C1149.08 when produced | C1157.03 |
| `c1104.package.json` | C1104 literal cp | C1130.09 | C1149.09 when produced | C1157.04 |
| `c1105.output.txt` | C1105 tee | C1130.10 | C1149.10 when produced | C1156.01 |
| `c1105.exit.txt` | C1105 assignment/printf redirect | C1130.11 | C1149.11 when produced | C1156.02 |
| `c1106.output.txt` | C1106 tee | C1130.12 | C1149.12 when produced | C1156.03 |
| `c1106.exit.txt` | C1106 assignment/printf redirect | C1130.13 | C1149.13 when produced | C1156.04 |
| `c1107.output.txt` | C1107 tee | C1130.14 | C1149.14 when produced | C1156.05 |
| `c1107.exit.txt` | C1107 assignment/printf redirect | C1130.15 | C1149.15 when produced | C1156.06 |
| `c1108.output.txt` | C1108 tee | C1130.16 | C1149.16 when produced | C1156.07 |
| `c1108.exit.txt` | C1108 assignment/printf redirect | C1130.17 | C1149.17 when produced | C1156.08 |

Ordinary completeness is 21 primary raw objects and 21 adjacent untouched
SHA-256 stdout sidecars. Early/failure branches invoke only the exact literals
whose sources were actually produced, recording every other member
`MISSING` or `NOT_RUN` in the form. Later ingestion—not the runbook—derives
the returned manifest, step/range index, hash comparisons, completeness,
C1105-C1108 zero-exit/PASS crosscheck, and terminal verdict.
