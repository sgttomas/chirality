# Later ingestion, validation, and causal-matrix contract

Status: `R4.4.6 SUCCESSOR CANDIDATE — NO SUCCESSOR EVIDENCE INGESTED`

Successor binding: any later successor execution must reproduce D-APP-93
overlay script SHA-256
`5ae3d79bdb711153c315920ac4f4d584f6bab2d8d9d17fa2f08c31ed9242c7b7`
and exact post-overlay config hashes
`1cb9e4c7325166f69139eeba3a0bdfcfa1d4f871e03acf4af1809aa88fa02a36`
and
`b53a867e8aa7d8874cf7ce2417691a05d449babaa9bf0b905c550deb13b3ac6d`.
The earlier R4.4.5 failed-attempt intake remains frozen separately under
`intake_r4_4_5/` and is never rewritten as successor evidence.
Successor intake accepts bytes only from sibling `returned_r4_4_6/`; accepted
predecessor `returned/` is excluded from successor receipt and completeness.

## Intake gate

App `HELP_HUMAN` routes returned immutable bytes to one bounded
`WORKING_ITEMS` intake. The runbook is a raw producer only. Intake—not the
owner-operated session—derives the returned-file manifest, step/range index,
hash comparisons, completeness, C1105-C1108 exit enforcement, PASS
dispositions, and terminal verdict.

A token, keychain value, API key, secret, memory dump, or environment dump is
rejected from ingestion and returned for separately governed credential-safe
redaction. Raw evidence is never edited in place. All derived records cite the
accepted packet freeze plus immutable raw-file SHA-256 identities and remain
derivative packages rather than execution truth.

## Required later derivations

The intake manager must independently:

1. inventory every returned pathname, byte count, and whole-file SHA-256,
   reject unenumerated paths, and reproduce every C1154-C1157 raw stdout
   sidecar against its named complete primary file;
2. reproduce ruling, prepared packet, approval token, C196/C197, runbook,
   command ledger, LLDB script, source, lock, archive, overlay, package, and
   rollback identities without relying on owner-entered comparisons;
3. parse the immutable CONTROL transcript only through the explicit terminal
   cut. Require C1146.30 as its last CONTROL input, enumerate every approved
   CONTROL-tab operation actually executed before that marker, and reject a
   missing, unapproved, duplicated, retried, hidden, or out-of-order through-cut
   operation. Do not require C1151.F or any post-cut act inside those bytes;
4. validate C196/C197 separately from `lldb-transcript.txt`. The released
   LLDB-shell post-cut hash inputs are intentionally outside that earlier
   C196/C197 transcript and outside the CONTROL transcript;
5. derive zero-based, end-exclusive byte ranges for each observed executable
   step from the C1146.01-C1146.30 raw exit records; verify ordered uniqueness
   through the terminal cut and explicitly mark missing/unclosed/duplicate
   ranges. The finite post-cut tail has no step range;
6. parse the completed evidence form and require one literal observation row
   for steps 1-31. Crosscheck `RECORDED`, `FAILED`, `NOT_RUN`,
   `DEVIATION`, `MISSING`, and `READY_FOR_RAW_RETURN` against through-cut
   transcripts, pre-cut returned copies, cleanup/final-absence outcomes, and
   the selected branch. Treat step 31 only as pre-freeze handoff intent and
   C1152 only as a post-cut observation/crosscheck, never a C1142 prerequisite;
7. validate the finite terminal preservation tail independently: C1151.F's
   returned CONTROL bytes end with C1146.30; C1150.R and applicable C1153.01
   occur before the cut and have byte-identical returned results; C1152
   completes the direct-return form after the cut; C1154.03 freezes that form;
   every remaining C1154-C1157 sidecar reproduces its primary; before C1142,
   all applicable then-produced evidence was returned and either C1140/C1141
   rollback proof completed after a C1079 write or the live CONTROL history
   showed that no C1079 input was entered; C1146.30/C1151.F later froze that
   history; no CONTROL input follows C1146.30; and actual directory receipt is
   observed by intake;
8. derive per-step dispositions only after those crosschecks. A derived PASS
   requires the exact approved operation, satisfied preconditions, raw exit
   zero where applicable, expected raw outputs, no deviation, and required
   identity match. Otherwise derive FAIL, NOT_RUN, MISSING, or DEVIATION;
9. parse each C1105-C1108 `.exit.txt` as exactly two records and require
   `command_exit=0` and `tee_exit=0`; crosscheck both zero values with the
   corresponding derived PASS disposition and complete `.output.txt`.
   Nonzero, missing, duplicate, malformed, or inconsistent values block PASS;
10. derive and freeze a retained-evidence manifest containing path, byte count,
    observed SHA-256, producer ID, copy ID, hash-sidecar ID, branch, cut/tail
    classification, and inclusion status for every expected and unexpected
    returned object;
11. validate C1103/C1104 raw configs, archive/source/lock hashes, package
    identity/topology, C1114/C1115/C1119 direct-child binding, five breakpoint
    blocks, exactly one C1121 first signal, byte-exact same-PTY C197, and an
    attach-to-detach duration below 150 seconds;
12. order trace, signal, process, socket/owner, GUI, through-cut preservation,
    cleanup, rollback, post-cut form/hash acts, and actual receipt using raw
    UTC/monotonic evidence while preserving uncertainty where clocks or bytes
    are incomplete;
13. validate the selected terminal branch against the exhaustive matrix below,
    including every prerequisite, source lifetime, required producer/copy/hash,
    prohibited operation, retained-state obligation, and rollback/cleanup
    result;
14. derive `PASS_COMPLETE` only for the complete ordinary post-C196 branch
    when all required primary objects exist, all sidecars reproduce, all steps
    derive PASS, step 31 is truthful `READY_FOR_RAW_RETURN`, actual directory
    receipt is independently observed, C1105-C1108 have both exits zero,
    identity/timing/target/cleanup/rollback checks pass, no prohibited content
    or undisclosed deviation exists, and no extra operation/file is present;
15. derive `STOP_INCOMPLETE` for every early, partial, failed, missing,
    deviated, occupied-destination, prohibited-content, copy/hash-failure, or
    cleanup/rollback-failure return; and
16. retain D-APP-88, DEL-09-04, TM-APP-036, product, release, and reliance as
    unchanged until their own gates are satisfied.

Execution success is not evidence acceptance. A missing conjunct is
`UNKNOWN` or `CONTRADICTED`, never repaired by narrative.

## Ordinary raw-byte completeness set

The complete ordinary branch must contain these 21 primary raw objects plus
one adjacent raw SHA-256 stdout sidecar per object:

- `lldb-transcript.txt`, `control-transcript.txt`,
  `control-transcript-precleanup.txt`, and
  `completed-evidence-return.md`;
- `helper.stdout.txt`, `helper.stderr.txt`, `helper.pid`,
  `gui.stdout.txt`, `gui.stderr.txt`, and `gui.pid`;
- `c1103.sha256.txt`, `c1104.electron-builder.runtime-helper.json`, and
  `c1104.package.json`;
- `c1105.output.txt`, `c1105.exit.txt`, `c1106.output.txt`,
  `c1106.exit.txt`, `c1107.output.txt`, `c1107.exit.txt`,
  `c1108.output.txt`, and `c1108.exit.txt`.

The later manifest may add its own immutable derivative identity only after
the raw set is frozen. It is never returned to or produced by the runbook.

## Exhaustive terminal validation matrix

| Terminal class | Through-cut route | Finite post-cut tail | Intake disposition |
|---|---|---|---|
| Before C1070 | C1147; C1150.R/C1151.R; applicable failure marker; C1151.F | C1152; applicable hashes; actual receipt | `STOP_INCOMPLETE` |
| Partial C1070 | live CONTROL shows no C1079 input; phase-valid C1151.T/R; applicable C1149; C1150.R/C1153.01 and all applicable then-produced evidence returned before C1142; C1142-C1143; cut/C1151.F freeze the history | C1152 later crosschecks; applicable hashes; actual receipt | `STOP_INCOMPLETE` |
| Incomplete baseline | live CONTROL shows no C1079 input; C1147; C1151.T; C1148; applicable C1149; C1150.R/C1153.01 and all applicable then-produced evidence returned before C1142; C1142-C1143; cut/C1151.F freeze the history | C1152 later crosschecks; applicable hashes; actual receipt | `STOP_INCOMPLETE` |
| Post-first-write/pre-C196 | C1147/C1149; C1150.R/C1153.01; exact-PID cleanup; C1131-C1141 rollback proof; all applicable then-produced evidence returned; C1142-C1143; cut; C1151.F; no C1144/C1130 | C1152 later crosschecks; applicable hashes; actual receipt | `STOP_INCOMPLETE` |
| Post-C196 ordinary | C1148 then exact C1145→C1144→C1130; C1151.T; C1150.R/C1153.01; exact-PID cleanup; C1131-C1141 rollback proof; all applicable then-produced evidence returned; C1142-C1143; cut; C1151.F | C1152 later crosschecks; C1154.03 first; remaining hashes; actual receipt | eligible for `PASS_COMPLETE` only after every independent check |
| Post-C196 failure | byte-exact C197 when safely possible; same route through first failure and a truthful cut when legal | only safe form/hash/receipt acts whose prerequisites hold | `STOP_INCOMPLETE` |
| Destination occupied | no write/reuse/alternate destination; out-of-band notice | none against returned | `STOP_INCOMPLETE` |
| Prohibited content | affected bytes not transferred; source retained | non-sensitive safe tail only; governed redaction required | `STOP_INCOMPLETE` |
| Pre-cut copy failure | immutable partial destination plus retained temp source/CONTROL state | no temp deletion; mandatory rollback when required | `STOP_INCOMPLETE` |
| Post-cut hash failure | returned primaries plus produced hash sidecars after a truthful cut | no retry/form edit; temp may already be validly absent | `STOP_INCOMPLETE` |
| Cleanup or rollback failure | truthful failure marker/cut and safe C1151.F when legal | safe direct form/hash/receipt only; retain temp/product state | `STOP_INCOMPLETE` |

## Causal matrix template

| Candidate seam / proposition | Required direct evidence | Supporting bytes | Contradicting bytes | Status (`SUPPORTED`/`CONTRADICTED`/`UNKNOWN`) | Limits / alternatives |
|---|---|---|---|---|---|
| SIGTERM reached native `__sigtramp` | matching trace event after exact C1121 | `TBD` | `TBD` | `UNKNOWN` | `TBD` |
| libuv signal handler ran | `uv__signal_handler` event/backtrace | `TBD` | `TBD` | `UNKNOWN` | `TBD` |
| Node SignalWrap callback ran | SignalWrap event/backtrace | `TBD` | `TBD` | `UNKNOWN` | `TBD` |
| Electron quit path ran | Browser.Quit and/or NSApplication event | `TBD` | `TBD` | `UNKNOWN` | `TBD` |
| App shutdown path completed | exact helper log events and zero exit | `TBD` | `TBD` | `UNKNOWN` | `TBD` |
| active GUI connection held Root stop pending | ordered trace/log/socket/process evidence | `TBD` | `TBD` | `UNKNOWN` | correlation alone is insufficient |
| socket and owner record removed after first signal | exact stat/absence evidence | `TBD` | `TBD` | `UNKNOWN` | `TBD` |
| GUI transport behavior followed helper transition | exact GUI log/owner observation | `TBD` | `TBD` | `UNKNOWN` | operator observation calibrated |
| package/runtime identity matched frozen inputs | complete hash/topology chain | `TBD` | `TBD` | `UNKNOWN` | `TBD` |

The later author must cite exact evidence bytes for every non-`UNKNOWN` cell,
state viable alternatives, and distinguish signal receipt, callback entry,
shutdown initiation, awaited Root stop, socket cleanup, and process exit.

## Mandatory post-execution verification

Only after intake validation, derived packages, causal matrix, and terminal
verdict are frozen may `WORKING_ITEMS` request separately authorized fresh
read-only adversarial verification. The verifier never repairs. `BLOCK`
returns to a separately authorized repair; no causal, remedy, acceptance,
release, or reliance claim issues before PASS.
