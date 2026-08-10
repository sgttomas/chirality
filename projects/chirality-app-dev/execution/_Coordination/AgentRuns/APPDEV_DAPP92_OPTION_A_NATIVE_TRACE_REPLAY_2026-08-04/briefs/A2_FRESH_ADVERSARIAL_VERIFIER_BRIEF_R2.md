# Sealed brief — fresh current-byte approval-stop verifier R2

RequestedBy: `WORKING_ITEMS / WI-DAPP92-A-01`

RunID: `APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04`

ChildInstanceID: `A2-DAPP92-A-VERIFY-02`

Objective: perform a genuinely fresh read-only adversarial verification of the
current post-whitespace-repair run package and determine whether it is fit for
the exact C196/C197 approval stop only.

DeclaredReads: this run root; D-APP-92 packet/ruling/adoption handoff; repaired
D-APP-88 R3 evidence; D-APP-89 baseline; DEL-09-04 status/memory/SoW; scoped
Git status/diff and deterministic hash/whitespace evidence.

AllowedTools: read-only filesystem/text/hash/Git inspection and the read-only
candidate-whitespace validator. No build, package, product launch, GUI,
contact, signal, trace, attach, process mutation, network/provider, credential,
owner-HOME/keychain, Git mutation, delegation, or repair.

AllowedWriteTargets: only
`reviews/A2_FRESH_ADVERSARIAL_VERIFIER_RETURN_R2.md`.

Required checks:

1. Reproduce the current hashes of the approval request, implementer terminal
   return, attempt-2 return, cleanup record, v1.8 amendment, runtime ledger and
   summary, and whitespace backcheck.
2. Verify the critical preimage proof: current bytes plus exactly one LF
   reproduce the recorded pre-repair hashes, including approval request
   `12e9e070...`; verify the historical verifier remains exactly
   `dc73abac...` and gives no current-byte credit.
3. Verify the exact C196/C197 owner token is unchanged and the request remains
   bounded to one future numeric direct-child helper PID, 150 seconds, the
   enumerated breakpoint/backtrace capture, and detach, with all prohibited
   authority exclusions intact.
4. Confirm C178's limitation, C179-C184 `NOT_RUN`/`UNKNOWN`, rollback and
   frontend-clean evidence, and the corrected C198/identity/PID/replay
   continuation requirements.
5. Verify current run-root candidate whitespace and scope containment.
6. Return `PASS_FOR_APPROVAL_STOP | BLOCK` with exact findings. A pass supports
   only presenting the command gate; it authorizes no execution or acceptance.

No delegation. Persist the terminal return before responding.
