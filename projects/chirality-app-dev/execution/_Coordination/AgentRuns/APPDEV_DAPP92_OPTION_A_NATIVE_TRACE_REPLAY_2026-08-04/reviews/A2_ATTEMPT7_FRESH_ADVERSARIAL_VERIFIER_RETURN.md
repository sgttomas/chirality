# Fresh adversarial verifier return — D-APP-92 Attempt 7 preparation

Verdict: `PASS_FOR_REAL_RUNTIME_PACKET_PREPARATION_ONLY — REAL_RUNTIME_EXECUTION_REMAINS_OWNER_GATED`

## Independence and scope

This was a genuinely fresh, read-only adversarial review. I did not rerun any
Attempt-7 command, alter temporary or frontend state, inspect a live process,
or write outside this return. The review covered the exact owner token,
approval adoption, immutable v1.15 graph and bound proposal, frozen scripts,
sealed executor brief, prior R5 handoff, executor terminal return, retained
Attempt-7 evidence, current fixed-root absence, current frontend Git state,
and the governing D-APP-92 ruling/register and Receipt-125 bytes.

## Bound-byte verification

All current-byte identities independently recompute as follows:

| Artifact | SHA-256 | Assessment |
|---|---|---|
| Proposed amendment v1.15 | `5f4d65f1c44caae38e7ae7499b2cff2c2e489338f67c2decb394f09c1f6677aa` | Exact bound identity |
| Attempt-7 approval request | `f147259fef667d81285aaae25bd0909e22c59d00b176da4fdef6d0a6f1083061` | Exact bound identity |
| Prior handoff R5 | `91dd4d0802b86994d15d40a764403ec2d4b4844e79b8425852cab8bd24b5786f` | Exact bound identity |
| v2 controller script | `9a756a7eb272bcc270e3a482f2664b8290cffac5f236230ccf7a4dfe38ebb9c4` | Exact bound identity |
| Unchanged session-B script | `02d651afbc13e7145de744977673aa54f4e9d7dd2411c06e2665537550ade11b` | Exact bound identity |
| Approval adoption | `d6fb32b9cfcdacdb6149c8620aee67e54861e325bdafa6f3e34cb4d71696e2b4` | Current identity |
| Immutable amendment v1.15 | `2c086fb823d1f34f51bc5bec57ff69f4a686468ef41abc87e23529ae533ade4a` | Current identity; incorporates the exact proposal without amendment |
| Sealed executor brief | `c8be5d5491cccdc5f68e8f0a2592c9469e119280737ff1a41dceda663ef2b3c8` | Current identity |
| Executor terminal return | `14fbe0794fe216055fee2a362f52e72a03c497198ea34ff5f6d393da03621ccc` | Exact verifier dependency |
| Command outcomes | `695436bfa09abbe4a3664237756f3c7db37993e3933bc656836f21d593c1cccc` | Current identity |
| Protocol ordering and bytes | `0ab6571e97bc8b10c25d007aee6883a7b16bd58041625653744a9fc55725051a` | Current identity |
| Cleanup evidence | `5281bc9cef6c21a5c38c7590b8f984765aecab322f5bf4fae660465361a83ea1` | Current identity |
| Copied protocol result | `0409681a1bab450372e5374d2726822e847da35671b067344ac22eabbe7905a9` | Exact C241 identity |

The owner token transcribed in the adoption record is byte-for-byte the token
supplied in the HELP_HUMAN coordination session. It grants exactly C231-C244
and expressly excludes LLDB, attach, package, cache seed, network, helper,
GUI, signal, replay, credential, memory/environment dump, process inspection,
release, Git, and all other authority.

The selected D-APP-92 packet and ruling also retain their registered SHA-256
identities `644c80ecff11577c9ab0f4f4fae4fa9b1f609cdaa2d801f118ffe052bfad77c6`
and `391b96507bfc877050ca4d1e4cb0ce421c60171becfabd13a13ab65d98fe1c78`.
The decision register remains RULED Option A and preserves the diagnostic-only
and no-automatic-effect boundary.

## Exact C231-C244 accounting

The command-outcome table contains exactly one disposition row for every ID
C231 through C244. The retained evidence supports those dispositions:

| ID | Disposition | Independent assessment |
|---|---|---|
| C231 | PASS | Current v2-controller hash equals the frozen identity. |
| C232 | PASS | Current session-B-script hash equals the frozen identity. |
| C233 | PASS | The executor records the fixed root absent before creation; no contrary evidence exists. |
| C234 | PASS | One exact fixed-root creation is recorded. |
| C235 | PASS | One readiness record identifies controller PID `13085`, positive direct-child PID `13086`, `/bin/sleep 35`, and `ATTACH_READY`; no bytes sent to session A are recorded. |
| C236 | PASS | Reconstructing the controller's exact pretty-printed durable bytes from the retained readiness record yields SHA-256 `f30f66344085e1d906fdee51695f99e9e5b6b9f474099fd52d10bfb3df8acae0`, exactly the recorded digest. |
| C237 | PASS | One retained sentinel line has the exact sentinel schema, PID `13086`, and `SECOND_SESSION_ACKNOWLEDGED` state and records exit `0`. |
| C238 | PASS | Existing-session no-byte polling records one exact result line and terminal exit `0` within the 45-second bound. |
| C239 | PASS | The declared run-local evidence directory exists. |
| C240 | PASS | The fixed-root payload preserved into the run is only `protocol-result.json`; neither controller nor sentinel was copied. |
| C241 | PASS | The copied result reproduces SHA-256 `0409681a1bab450372e5374d2726822e847da35671b067344ac22eabbe7905a9`. |
| C242 | PASS | C238 had already established terminal exit `0`; the recorded additional zero-byte poll found no existing session. Both occur before cleanup in the ordered evidence. |
| C243 | PASS | Exact fixed-root removal is recorded only after the C242 terminal confirmation. |
| C244 | PASS | The exact fixed root is currently absent. |

The records are singular, internally consistent, and contain no retry or
altered-command claim. Mandatory C242 is accounted for after C235 and before
C243. C243-C244 are both accounted for after the only C234 creation.

## Protocol and causal calibration

The frozen v2 controller semantics are narrow and fail closed. The script:

- creates only its direct child `/bin/sleep 35`;
- registers child exit before readiness;
- durably writes the controller record before emitting `ATTACH_READY`;
- accepts only the exact sentinel schema, direct-child PID, and state within
  30 seconds and before observed child exit;
- waits for natural child exit; and
- writes a result only for exit code `0` with no signal.

The retained `protocol-result.json` parses as one object with exactly the ten
expected keys. It reports schema
`chirality-dapp92-two-session-result/v2`, PID `13086`, matching sentinel state,
`/bin/sleep` with argv `["35"]`, `sentinelWindowMs: 30000`, exit code `0`,
`childSignal: null`, and `controllerState: "COMPLETE"`. These values match the
frozen script's only success construction and the exact readiness/sentinel/
result bytes retained in the ordering record.

The deleted controller record is necessarily unavailable after mandatory
cleanup, but its recorded hash is independently reproducible from the retained
exact controller bytes. The deleted sentinel and the command-tool poll stream
are represented by the executor's immutable outcome and ordering records
rather than separate raw files. That retention shape is adequate for this
mock preparation verdict, but it supports no inference about a real helper,
Electron, LLDB attachment, signal delivery, callback entry, teardown, Root
stop, or replay behavior.

## Cleanup, containment, and exclusions

- `/private/tmp/chirality-dapp92-attempt6-protocol` is currently absent.
- `git status --short --untracked-files=all -- projects/chirality-app-dev/frontend`
  is empty.
- `git diff --exit-code -- projects/chirality-app-dev/frontend` exits `0`.
- The Attempt-7 evidence directory contains the sole copied protocol result
  plus its three run-local explanatory evidence records; no controller,
  sentinel, environment, memory, credential, or process data is retained.
- The complete command accounting and retained bytes evidence no LLDB,
  attach, package/reconstruction, cache seed, network, helper, GUI, signal,
  replay, credential, memory/environment dump, process inspection, product
  remedy, release, Git mutation, Task Management, or foreign-loop action.
  C196/C197 remain separately approved but unused.

## Gate disposition

Attempt 7 passes as a bounded mock preparation probe with successful protocol
completion, natural direct-child exit, mandatory session quiescence, cleanup,
and frontend containment. This pass authorizes WORKING_ITEMS to prepare a
fresh, immutable, separately owner-gated real-runtime command packet only.

It does **not** authorize that packet, any helper or GUI launch, LLDB attach,
signal, replay, runtime execution, product remedy, D-APP-88 acceptance,
DEL-09-04 closure, TM-APP-036 firing, release, reliance, or Git action. Every
real-runtime command remains subject to the D-APP-92 ruling's individual
enumeration and applicable owner-approval gates.
