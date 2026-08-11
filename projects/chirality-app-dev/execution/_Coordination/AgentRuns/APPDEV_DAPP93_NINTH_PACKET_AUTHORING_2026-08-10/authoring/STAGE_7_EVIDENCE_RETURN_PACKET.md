# Stage 7 — credential-safe evidence return packet

Status: `AUTHORED — BLANK OWNER RETURN FORM — NO EXECUTION CLAIM`

Complete without deleting raw diagnostic bytes. If a field cannot be supported
write `UNKNOWN` and explain why. Never reconstruct missing bytes.

## Frozen identities

- approved final packet SHA-256:
- packet-index SHA-256:
- runbook SHA-256:
- LLDB-script SHA-256:
- two-tier probe-ledger SHA-256:
- evidence-return-template SHA-256:
- prepared helper executable path:
- prepared helper executable SHA-256:
- tool-pin verification bundle path/SHA-256:

## Step 0 owner preflight

- UTC start:
- `/bin/ps` actual SHA-256:
- exact restricted command:
  `/bin/ps -p $$ -o pid=,ppid=,comm=`
- actual exit code:
- stdout path/SHA-256:
- stderr path/SHA-256:
- observed output shape:
- all other tool pins matched (`YES` or `NO`):
- helper subject present/executable/hash matched (`YES` or `NO`):
- script hash matched frozen index (`YES` or `NO`):
- Step-0 verdict (`PASS` or `STOP_UNEXECUTED`):
- deviation/limitation:

If Step 0 did not pass leave every later field `NOT_RUN_STEP0_STOP`.

## Host and isolated posture

- macOS identity evidence path/SHA-256:
- architecture evidence path/SHA-256:
- pre-owner default observation path/SHA-256:
- pre-owner search observation path/SHA-256:
- isolated keychain creation exit/path hashes:
- isolated default observation path/SHA-256:
- isolated search observation path/SHA-256:
- prompt observation (`NONE` or `SHOWN_CANCELLED`):
- credential value entered or observed (`NO` required):

## Exact target binding

- owner shell PID:
- helper PID:
- helper relation record path/SHA-256:
- relation stderr path/SHA-256:
- direct-child gate (`PASS` or `STOP`):
- PID revalidated immediately before attach (`YES` or `NO`):
- no alternate PID/search/retry attestation (`YES` or `NO`):

## Trace and first signal

- attach-start UTC epoch:
- exact LLDB displayed target PID:
- required breakpoint resolution summary:
- unresolved breakpoint or script error:
- Activity Monitor numeric PID selected:
- Activity Monitor action (`Quit` required; never `Force Quit`):
- first-signal UTC timestamp:
- exactly one first signal attestation:
- raw LLDB transcript path/SHA-256:
- trace markers observed with transcript byte offsets or line references:
- same-PTY Control-C observed:
- same-PTY detach response:
- same-PTY quit and terminal return:
- attach-end UTC epoch:
- elapsed seconds:
- elapsed bound gate (`PASS_0_TO_150` or `STOP`):

## Target terminal and teardown state

- exact helper wait exit status:
- helper terminality (`PROVEN` or `UNKNOWN`):
- isolated control socket absence (`PASS` or `FAIL_OR_UNKNOWN`):
- helper stdout path/SHA-256:
- helper stderr path/SHA-256:

## Owner-state and cleanup

- post-owner default observation path/SHA-256:
- post-owner search observation path/SHA-256:
- pre/post default content-digest comparison:
- pre/post search content-digest comparison:
- owner-state verdict (`MATCH` or `DRIFT_OR_UNKNOWN`):
- isolated keychain deletion exit/path hashes:
- isolated keychain absence:
- fixed trace-root removal exit:
- fixed trace-root absence:
- cleanup verdict (`COMPLETE` or `INCOMPLETE_RETAINED_STATE`):
- retained state path if incomplete:

## Deviations and limitations

- literal numbered step outcomes:
- skipped step and reason:
- unexpected prompt/output/error:
- operator deviation:
- missing raw bytes:
- unresolved symbols:
- timing uncertainty:
- other limitation:

## Credential-safety declaration

- Returned set contains no token API key keychain value secret memory dump or
  environment dump (`YES` required):
- Withheld suspect evidence path and reason:
- Separately governed redaction required (`YES` or `NO`):
- Silent normalization performed (`NO` required):

## Evidence inventory

List each returned ordinary file exactly once with byte count and SHA-256.
Distinguish raw machine evidence operator attestation and derived checks.

## Terminal declaration

Choose exactly one:

- `EVIDENCE_RETURNED CLEANUP_COMPLETE NO_CAUSAL_OR_ACCEPTANCE_CLAIM`
- `EVIDENCE_RETAINED STOPPED_OR_CLEANUP_INCOMPLETE NO_CAUSAL_OR_ACCEPTANCE_CLAIM`
- `STEP0_STOP_UNEXECUTED RETURNED_TO_APPROVAL_GATE`

This return supports later governed ingestion only. It makes no causal remedy
acceptance release reliance closure or next-step claim.
