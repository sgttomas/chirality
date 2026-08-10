# Later ingestion, validation, and causal-matrix contract

Status: `ATTEMPT-3 CANDIDATE — NO ATTEMPT-3 EVIDENCE INGESTED`

Successor binding: any later successor execution must reproduce D-APP-93
overlay script SHA-256
`750a9c5177c9bfc84166baa4e11a06a7296bac7556c3a2135c3fe1502090d7fe`
and exact post-overlay config hashes
`7deda10bde45936fa9abd2a16ed9c7cf85f9a67cb48dc0b34dcb46c04b3543cb`
and
`c3480540e6d3cd54be74ec29bd67d2db3c8d3326e0b4b8da0154725342d8c1e1`.
The earlier R4.4.5 failed-attempt intake remains frozen separately under
`intake_r4_4_5/` and is never rewritten as successor evidence.
Successor intake accepts bytes only from sibling `returned_attempt3/`; accepted
predecessor `returned/` is excluded from successor receipt and completeness.

## Intake gate

App `HELP_HUMAN` routes returned immutable bytes to one bounded
`WORKING_ITEMS` intake. The runbook is a raw producer only. Intake—not the
owner-operated session—derives the returned-file manifest, step/range index,
hash comparisons, completeness, A3-OP-041-A3-OP-044 exit enforcement, PASS
dispositions, and terminal verdict.

A token, keychain value, API key, secret, memory dump, or environment dump is
rejected from ingestion and returned for separately governed credential-safe
redaction. Raw evidence is never edited in place. All derived records cite the
accepted packet freeze plus immutable raw-file SHA-256 identities and remain
derivative packages rather than execution truth.

## Required later derivations

The intake manager must independently:

1. inventory every returned pathname, byte count, and whole-file SHA-256,
   reject unenumerated paths, and reproduce every A3-OP-090-A3-OP-093 raw stdout
   sidecar against its named complete primary file;
2. reproduce ruling, prepared packet, approval token, A3-OP-001/A3-OP-002, runbook,
   command ledger, LLDB script, source, lock, archive, overlay, package, and
   rollback identities without relying on owner-entered comparisons;
3. parse the immutable CONTROL transcript only through the explicit terminal
   cut. Require A3-OP-082.30 as its last CONTROL input, enumerate every approved
   CONTROL-tab operation actually executed before that marker, and reject a
   missing, unapproved, duplicated, retried, hidden, or out-of-order through-cut
   operation. Do not require A3-OP-087.F or any post-cut act inside those bytes;
4. validate A3-OP-001/A3-OP-002 separately from `lldb-transcript.txt`. The released
   LLDB-shell post-cut hash inputs are intentionally outside that earlier
   A3-OP-001/A3-OP-002 transcript and outside the CONTROL transcript;
5. derive zero-based, end-exclusive byte ranges for each observed executable
   step from the A3-OP-082.01-A3-OP-082.30 raw exit records; verify ordered uniqueness
   through the terminal cut and explicitly mark missing/unclosed/duplicate
   ranges. The finite post-cut tail has no step range;
6. parse the completed evidence form and require one literal observation row
   for steps 1-31. Crosscheck `RECORDED`, `FAILED`, `NOT_RUN`,
   `DEVIATION`, `MISSING`, and `READY_FOR_RAW_RETURN` against through-cut
   transcripts, pre-cut returned copies, cleanup/final-absence outcomes, and
   the selected branch. Treat step 31 only as pre-freeze handoff intent and
   A3-OP-088 only as a post-cut observation/crosscheck, never a A3-OP-078 prerequisite;
7. validate the finite terminal preservation tail independently: A3-OP-087.F's
   returned CONTROL bytes end with A3-OP-082.30; A3-OP-086.R and applicable A3-OP-089.01
   occur before the cut and have byte-identical returned results; A3-OP-088
   completes the direct-return form after the cut; A3-OP-090.03 freezes that form;
   every remaining A3-OP-090-A3-OP-093 sidecar reproduces its primary; before A3-OP-078,
   all applicable then-produced evidence was returned and either A3-OP-076/A3-OP-077
   rollback proof completed after a A3-OP-015 write or the live CONTROL history
   showed that no A3-OP-015 input was entered; A3-OP-082.30/A3-OP-087.F later froze that
   history; no CONTROL input follows A3-OP-082.30; and actual directory receipt is
   observed by intake;
8. derive per-step dispositions only after those crosschecks. A derived PASS
   requires the exact approved operation, satisfied preconditions, raw exit
   zero where applicable, expected raw outputs, no deviation, and required
   identity match. Otherwise derive FAIL, NOT_RUN, MISSING, or DEVIATION;
9. parse each A3-OP-041-A3-OP-044 `.exit.txt` as exactly two records and require
   `command_exit=0` and `tee_exit=0`; crosscheck both zero values with the
   corresponding derived PASS disposition and complete `.output.txt`.
   Nonzero, missing, duplicate, malformed, or inconsistent values block PASS;
10. derive and freeze a retained-evidence manifest containing path, byte count,
    observed SHA-256, producer ID, copy ID, hash-sidecar ID, branch, cut/tail
    classification, and inclusion status for every expected and unexpected
    returned object;
11. validate the exact Option-A sequence and raw bytes: `umask 077`, sealed
    HOME, initial isolated default/search observations, exact
    `create-keychain -p ''`, absence of explicit unlock and isolated
    default/search bind writes, synthesized one-element readbacks, prompt
    `NONE`, owner pre/post state and mismatch-only backstop, raw-evidence
    archive/sidecar committed before destructive isolated cleanup, and exact
    HOME/user-data on every relevant Electron/helper invocation;
12. validate fresh attempt-3 contact independently from the two returned
    primaries, two reproducing sidecars, contemporaneous GUI bytes, and exact
    owner-visible signature. Historical attempt-2 and R8 evidence cannot
    satisfy this gate; absence or contradiction blocks trace completeness;
13. validate A3-OP-039/A3-OP-040 raw configs, archive/source/lock hashes, package
    identity/topology, A3-OP-050/A3-OP-051/A3-OP-055 direct-child binding, five breakpoint
    blocks, exactly one A3-OP-057 first signal, byte-exact same-PTY A3-OP-002, and an
    attach-to-detach duration below 150 seconds;
14. order trace, signal, process, socket/owner, GUI, through-cut preservation,
    cleanup, rollback, post-cut form/hash acts, and actual receipt using raw
    UTC/monotonic evidence while preserving uncertainty where clocks or bytes
    are incomplete;
15. validate the selected terminal branch against the exhaustive matrix below,
    including every prerequisite, source lifetime, required producer/copy/hash,
    prohibited operation, retained-state obligation, and rollback/cleanup
    result;
16. derive `PASS_COMPLETE` only for the complete ordinary post-A3-OP-001 branch
    when all required primary objects exist, all sidecars reproduce, all steps
    derive PASS, step 31 is truthful `READY_FOR_RAW_RETURN`, actual directory
    receipt is independently observed, A3-OP-041-A3-OP-044 have both exits zero,
    identity/timing/target/cleanup/rollback checks pass, no prohibited content
    or undisclosed deviation exists, and no extra operation/file is present;
17. derive `STOP_INCOMPLETE` for every early, partial, failed, missing,
    deviated, occupied-destination, prohibited-content, copy/hash-failure, or
    cleanup/rollback-failure return; and
18. retain D-APP-88, DEL-09-04, TM-APP-036, product, release, and reliance as
    unchanged until their own gates are satisfied.

Execution success is not evidence acceptance. A missing conjunct is
`UNKNOWN` or `CONTRADICTED`, never repaired by narrative.

## Ordinary raw-byte completeness set

The complete ordinary branch must contain these 24 primary raw objects plus
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
  `c1108.output.txt`, and `c1108.exit.txt`;
- `fresh-authenticated-contact.txt`, `fresh-contact-gui.stderr.txt`, and
  `raw-evidence.zip` (the archive contains every then-produced Option-A,
  owner-state, build, helper, GUI, and runtime evidence file before cleanup).

The later manifest may add its own immutable derivative identity only after
the raw set is frozen. It is never returned to or produced by the runbook.

## Exhaustive terminal validation matrix

| Terminal class | Through-cut route | Finite post-cut tail | Intake disposition |
|---|---|---|---|
| Before A3-OP-006 | A3-OP-083; A3-OP-086.R/A3-OP-087.R; applicable failure marker; A3-OP-087.F | A3-OP-088; applicable hashes; actual receipt | `STOP_INCOMPLETE` |
| Partial A3-OP-006 | live CONTROL shows no A3-OP-015 input; phase-valid A3-OP-087.T/R; applicable A3-OP-085; A3-OP-086.R/A3-OP-089.01 and all applicable then-produced evidence returned before A3-OP-078; A3-OP-078-A3-OP-079; cut/A3-OP-087.F freeze the history | A3-OP-088 later crosschecks; applicable hashes; actual receipt | `STOP_INCOMPLETE` |
| Incomplete baseline | live CONTROL shows no A3-OP-015 input; A3-OP-083; A3-OP-087.T; A3-OP-084; applicable A3-OP-085; A3-OP-086.R/A3-OP-089.01 and all applicable then-produced evidence returned before A3-OP-078; A3-OP-078-A3-OP-079; cut/A3-OP-087.F freeze the history | A3-OP-088 later crosschecks; applicable hashes; actual receipt | `STOP_INCOMPLETE` |
| Post-first-write/pre-A3-OP-001 | A3-OP-083/A3-OP-085; A3-OP-086.R/A3-OP-089.01; exact-PID cleanup; A3-OP-067-A3-OP-077 rollback proof; all applicable then-produced evidence returned; A3-OP-078-A3-OP-079; cut; A3-OP-087.F; no A3-OP-080/A3-OP-066 | A3-OP-088 later crosschecks; applicable hashes; actual receipt | `STOP_INCOMPLETE` |
| Post-A3-OP-001 ordinary | A3-OP-084 then exact A3-OP-081→A3-OP-080→A3-OP-066; A3-OP-087.T; A3-OP-086.R/A3-OP-089.01; exact-PID cleanup; A3-OP-067-A3-OP-077 rollback proof; all applicable then-produced evidence returned; A3-OP-078-A3-OP-079; cut; A3-OP-087.F | A3-OP-088 later crosschecks; A3-OP-090.03 first; remaining hashes; actual receipt | eligible for `PASS_COMPLETE` only after every independent check |
| Post-A3-OP-001 failure | byte-exact A3-OP-002 when safely possible; same route through first failure and a truthful cut when legal | only safe form/hash/receipt acts whose prerequisites hold | `STOP_INCOMPLETE` |
| Destination occupied | no write/reuse/alternate destination; out-of-band notice | none against returned | `STOP_INCOMPLETE` |
| Prohibited content | affected bytes not transferred; source retained | non-sensitive safe tail only; governed redaction required | `STOP_INCOMPLETE` |
| Pre-cut copy failure | immutable partial destination plus retained temp source/CONTROL state | no temp deletion; mandatory rollback when required | `STOP_INCOMPLETE` |
| Post-cut hash failure | returned primaries plus produced hash sidecars after a truthful cut | no retry/form edit; temp may already be validly absent | `STOP_INCOMPLETE` |
| Cleanup or rollback failure | truthful failure marker/cut and safe A3-OP-087.F when legal | safe direct form/hash/receipt only; retain temp/product state | `STOP_INCOMPLETE` |

## Causal matrix template

| Candidate seam / proposition | Required direct evidence | Supporting bytes | Contradicting bytes | Status (`SUPPORTED`/`CONTRADICTED`/`UNKNOWN`) | Limits / alternatives |
|---|---|---|---|---|---|
| SIGTERM reached native `__sigtramp` | matching trace event after exact A3-OP-057 | `NOT_OBSERVED` | `NOT_OBSERVED` | `UNKNOWN` | evidence required |
| libuv signal handler ran | `uv__signal_handler` event/backtrace | `NOT_OBSERVED` | `NOT_OBSERVED` | `UNKNOWN` | evidence required |
| Node SignalWrap callback ran | SignalWrap event/backtrace | `NOT_OBSERVED` | `NOT_OBSERVED` | `UNKNOWN` | evidence required |
| Electron quit path ran | Browser.Quit and/or NSApplication event | `NOT_OBSERVED` | `NOT_OBSERVED` | `UNKNOWN` | evidence required |
| App shutdown path completed | exact helper log events and zero exit | `NOT_OBSERVED` | `NOT_OBSERVED` | `UNKNOWN` | evidence required |
| active GUI connection held Root stop pending | ordered trace/log/socket/process evidence | `NOT_OBSERVED` | `NOT_OBSERVED` | `UNKNOWN` | correlation alone is insufficient |
| socket and owner record removed after first signal | exact stat/absence evidence | `NOT_OBSERVED` | `NOT_OBSERVED` | `UNKNOWN` | evidence required |
| GUI transport behavior followed helper transition | exact GUI log/owner observation | `NOT_OBSERVED` | `NOT_OBSERVED` | `UNKNOWN` | operator observation calibrated |
| package/runtime identity matched frozen inputs | complete hash/topology chain | `NOT_OBSERVED` | `NOT_OBSERVED` | `UNKNOWN` | evidence required |

The later author must cite exact evidence bytes for every non-`UNKNOWN` cell,
state viable alternatives, and distinguish signal receipt, callback entry,
shutdown initiation, awaited Root stop, socket cleanup, and process exit.

## Mandatory post-execution verification

Only after intake validation, derived packages, causal matrix, and terminal
verdict are frozen may `WORKING_ITEMS` request separately authorized fresh
read-only adversarial verification. The verifier never repairs. `BLOCK`
returns to a separately authorized repair; no causal, remedy, acceptance,
release, or reliance claim issues before PASS.
