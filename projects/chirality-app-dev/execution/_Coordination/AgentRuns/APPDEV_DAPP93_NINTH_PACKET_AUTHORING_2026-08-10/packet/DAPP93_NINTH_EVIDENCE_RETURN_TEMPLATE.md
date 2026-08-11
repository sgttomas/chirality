# D-APP-93 ninth-lineage evidence return template

Status: `BLANK OWNER FORM — NO EXECUTION CLAIM`

Use `UNKNOWN` for unsupported fields and preserve raw bytes. Never reconstruct
missing evidence.

## Frozen identities

- approved final packet SHA-256:
- packet-index SHA-256:
- runbook SHA-256:
- LLDB-script SHA-256:
- two-tier probe-ledger SHA-256:
- evidence-template SHA-256:
- prepared helper path and SHA-256:
- tool-pin evidence bundle path and SHA-256:

## Step 0 owner preflight

- UTC start:
- `/bin/ps` actual SHA-256:
- exact command: `/bin/ps -p $$ -o pid=,ppid=,comm=`
- actual exit code:
- stdout path/SHA-256:
- stderr path/SHA-256:
- observed output shape:
- all other tool pins matched:
- helper present executable and hash matched:
- LLDB script hash matched packet index:
- verdict (`PASS` or `STOP_UNEXECUTED`):
- deviation or limitation:

If Step 0 fails write `NOT_RUN_STEP0_STOP` in every later field.

## Host and isolated posture

- macOS evidence path/SHA-256:
- architecture evidence path/SHA-256:
- pre-owner default evidence path/SHA-256:
- pre-owner search evidence path/SHA-256:
- isolated keychain creation exit and evidence hashes:
- isolated default evidence path/SHA-256:
- isolated search evidence path/SHA-256:
- prompt (`NONE` or `SHOWN_CANCELLED`):
- credential value entered or observed (`NO` required):

## Exact target

- owner shell PID:
- helper PID:
- relation record path/SHA-256:
- relation stderr path/SHA-256:
- direct-child gate:
- PID revalidated immediately before attach:
- no search alternate PID or retry attestation:

## Trace and first signal

- attach-start UTC epoch:
- LLDB displayed target PID:
- required breakpoint resolution summary:
- unresolved breakpoint or script error:
- Activity Monitor numeric PID:
- Activity Monitor action (`Quit` required):
- first-signal UTC timestamp:
- exactly one first signal attestation:
- raw transcript path/SHA-256:
- trace markers and transcript references:
- same-PTY Control-C observed:
- same-PTY detach response:
- same-PTY quit and shell return:
- attach-end UTC epoch:
- elapsed seconds:
- elapsed gate (`PASS_0_TO_150` or `STOP`):

## Terminal state

- helper wait exit status:
- helper terminality:
- isolated control socket absence:
- helper stdout path/SHA-256:
- helper stderr path/SHA-256:

## Owner state and cleanup

- post-owner default evidence path/SHA-256:
- post-owner search evidence path/SHA-256:
- pre/post default digest comparison:
- pre/post search digest comparison:
- owner-state verdict:
- isolated keychain deletion evidence hashes:
- isolated keychain absence:
- trace-root removal and absence:
- cleanup verdict:
- retained state path if incomplete:

## Deviations limitations and credentials

- literal numbered outcomes:
- skipped step and reason:
- unexpected prompt output or error:
- operator deviation:
- missing raw bytes:
- unresolved symbols:
- timing uncertainty:
- returned set has no token API key keychain value secret memory dump or environment dump (`YES` required):
- withheld suspect evidence path and reason:
- separate redaction required:
- silent normalization (`NO` required):

## Evidence inventory

List each ordinary file exactly once with byte count SHA-256 and evidence class
(`RAW_MACHINE`, `OWNER_ATTESTATION`, or `DERIVED_CHECK`).

## Terminal declaration

Choose exactly one:

- `EVIDENCE_RETURNED CLEANUP_COMPLETE NO_CAUSAL_OR_ACCEPTANCE_CLAIM`
- `EVIDENCE_RETAINED STOPPED_OR_CLEANUP_INCOMPLETE NO_CAUSAL_OR_ACCEPTANCE_CLAIM`
- `STEP0_STOP_UNEXECUTED RETURNED_TO_APPROVAL_GATE`

No causal remedy acceptance release reliance closure or next-step claim is
made by this form.
