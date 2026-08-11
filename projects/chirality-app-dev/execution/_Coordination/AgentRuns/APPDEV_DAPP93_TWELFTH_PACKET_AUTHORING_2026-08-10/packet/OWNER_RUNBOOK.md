# D-APP-93 Owner Runbook — Helper SIGTERM Survival Causal Trace

## Immutable-use warning and authority boundary

Use this packet only at its manager-frozen byte identity. No execution authority exists until the owner approves the final frozen packet by its exact SHA-256. That prohibition includes Step 0. Do not alter a frozen packet and continue under an approval for another identity.

This is an owner-operated LLDB trace. It does not authorize an agent to run Step 0, attach LLDB, signal a process, or perform any operative step. It does not preclaim a result or causal conclusion.

## Required owner inputs

- `PACKET_DIR`: this packet directory at the approved frozen identity.
- `EVIDENCE_DIR`: an existing, dedicated evidence directory outside the immutable packet.
- `OWNER_SUPPLIED_PID`: the decimal PID selected by the owner for the helper process.
- `LLDB_TRANSCRIPT`: an existing transcript file inside `EVIDENCE_DIR` after the trace is recorded.

## Step 0 — owner-run environment preflight

Step 0 is forbidden until the exact frozen packet SHA-256 has owner approval.

1. Change directory to `PACKET_DIR`.
2. Record the approved aggregate packet SHA-256 in the evidence copy of `EVIDENCE_CAPTURE.md`.
3. Run exactly:

   `/bin/zsh ./scripts/OWNER_ENVIRONMENT_PREFLIGHT.zsh "$EVIDENCE_DIR"`

4. Preserve the script-created `STEP_ZERO_ENVIRONMENT_PREFLIGHT.txt` in `EVIDENCE_DIR`.
5. Confirm that the record contains actual SHA-256 values equal to these expected identities:

   - `/bin/zsh`: `528da649cc69510bd3c0bc565298cb602076b74a8ac3f18e793211b2a3c725e8`
   - `/usr/bin/lldb`: `44a68ddc1983d6cff3fd35ba3f9ba5f82004216f1dcde69892b3d1b06e408698`
   - `/bin/ps`: `a1d8c4a0a96fb6159f09d8f520f54df829db5f2eae9b9f3448e18f0bee61115c`
   - `/usr/bin/shasum`: `0812595f981a26f813d98dc380af14d4af427626c9339eda29eb849ae13de1e3`
   - `/usr/bin/perl`: `626702a74f85d2664872f6a7aa9b639306a2035211d442a24ea32ef0d48c8afd`

6. Confirm `/usr/bin/lldb --version` exits `0` and its first output line begins `lldb-`.
7. Confirm owner-side `/bin/ps -p $$ -o pid=` exits `0` and produces a numeric PID.

Stop before any operative act if a hash, exit code, or output shape differs, or if the recording is incomplete.

## Operative LLDB causal trace

The owner performs this section only after Step 0 passes and only under approval for the exact frozen packet identity.

1. Record `OWNER_SUPPLIED_PID` in the evidence form. Verify its identity before attachment:

   `/bin/ps -p "$OWNER_SUPPLIED_PID" -o pid=,ppid=,command=`

   Compare the displayed PID, parent PID, and command with the process the owner intended to trace. Stop on any identity or topology variance.

2. Start transcript capture using the owner's normal terminal recording facility, with `LLDB_TRANSCRIPT` inside `EVIDENCE_DIR`. Record the facility and exact transcript path; the packet does not prescribe or launch a recording tool.
3. Attach:

   `/usr/bin/lldb -p "$OWNER_SUPPLIED_PID"`

   Record all LLDB output. Stop if attachment fails or the reported process differs.

4. At the LLDB prompt, configure SIGTERM to stop and notify without passing the signal automatically:

   `process handle SIGTERM -s true -n true -p false`

   Record LLDB's confirmation. Stop if LLDB rejects the command or reports different handling.

5. Establish the pre-signal state with:

   `process status`

   `thread list`

   `thread backtrace all`

   Record the process, thread, and backtrace output. Do not infer a result from absence of a stop.

6. Continue the process:

   `continue`

   The owner may cause the already-defined external reproduction to deliver SIGTERM; this packet neither generates nor authorizes a signal. If LLDB stops, record the complete stop banner and then run:

   `process status`

   `thread list`

   `thread backtrace all`

   Record which thread stopped, the reported stop reason, frames, process state, and any helper-topology variance. Do not fill gaps with inference.

7. When the required observation is complete, or immediately on a stop rule that still permits orderly cleanup, detach without terminating the target:

   `process detach`

   Record the detach response, then run:

   `quit`

8. Verify the target identity and post-detach state:

   `/bin/ps -p "$OWNER_SUPPLIED_PID" -o pid=,ppid=,command=`

   Record the result. A missing or different process is evidence to record, not a conclusion to rewrite.

## Stop rules

Stop and preserve the evidence accumulated so far on any of the following:

- Step 0 hash, command, exit-code, output-shape, or recording mismatch.
- Target PID identity or process-topology mismatch.
- LLDB attach failure or unexpected attached process.
- Process, helper, or thread topology variance from the owner-selected target.
- LLDB command rejection or output variance that prevents the specified observation.
- Transcript, hash, timestamp, process-state, thread-state, or backtrace evidence gap.
- Detach, quit, transcript finalization, or post-detach verification failure.

Never improvise around a stop rule. Record the variance and return the packet to the owner gate unexecuted beyond the point already reached.

## Evidence capture and prohibited scope

Copy the blank `EVIDENCE_CAPTURE.md` into `EVIDENCE_DIR` before recording results. Keep observed facts separate from owner interpretation. After the transcript exists and recording has ended, run from `PACKET_DIR`:

`/bin/zsh ./scripts/CAPTURE_TRACE_EVIDENCE.zsh "$EVIDENCE_DIR" "$LLDB_TRANSCRIPT"`

Confirm that the appended transcript path and SHA-256 refer to the recorded file. Preserve the Step 0 record, completed evidence form, transcript, exit codes, and hashes together.

This packet performs no build, install, overlay, signing, notarization, publication, source mutation, runtime configuration, or network operation.
