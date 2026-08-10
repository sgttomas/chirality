# Agent-2 brief — D-APP-92 Attempt-7 timing-only preparation execution

- RequestedBy: `WORKING_ITEMS /root/dapp92_attempt7_preparation`
- RunID: `APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04`
- ParentInstanceID: `/root/dapp92_attempt7_preparation`
- ChildInstanceID: `A2-DAPP92-A-ATTEMPT7-PREPARE-01`
- PackageID: `PKG-09`
- DeliverableID: `DEL-09-04` diagnostic preparation only
- Objective: execute exactly C231-C244 from immutable amendment v1.15 and
  return complete protocol-result, ordering, and cleanup evidence without
  widening authority.
- ScopePath: this run root plus fixed temporary root
  `/private/tmp/chirality-dapp92-attempt6-protocol`.
- AcceptedBasis: D-APP-92 Option A ruling; exact owner Attempt-7 token;
  `OWNER_ATTEMPT7_PREPARATION_APPROVAL_ADOPTION.md`;
  `COMMAND_REGISTER_AMENDMENT_V1_15.md`; bound proposal SHA-256
  `5f4d65f1c44caae38e7ae7499b2cff2c2e489338f67c2decb394f09c1f6677aa`.
- Dependencies: immutable scripts at the two bound hashes; fixed mock root
  absent before C234.
- DeclaredReads: adopted amendment, its bound proposal, its two bound scripts,
  and only the C231-C244 outputs and current frontend Git state for cleanup
  proof.
- AllowedTools: exact C231-C244 commands and existing-session polling without
  bytes only.
- AllowedWriteTargets: fixed mock root; run-local
  `evidence/attempt7-preparation/**`; run-local instance terminal return.
- ExpectedOutputs: exact controller readiness record; controller-record hash;
  matching session-B sentinel; one exact result line; naturally terminated
  session-A result; sole copied protocol-result and hash; command outcomes;
  cleanup proof; terminal return.
- AcceptanceCriteria: exact script hashes; absent root before C234; immediate
  exact readiness schema; matching PID/sentinel; successful controller
  consumption; `/bin/sleep 35` natural exit with code 0/no signal; exact result
  schema; C242 terminal-session confirmation; C243-C244 pass; no fixed-root
  residue; no frontend change; all exclusions hold.
- Escalation: stop on any hash mismatch, pre-existing root, readiness/output/
  schema/PID/state mismatch, early or non-natural child exit, timeout, command
  deviation, or cleanup failure. No retry or alteration.

EXCLUSIONS: no LLDB, attach, package/reconstruction, cache seed, network,
helper, GUI, signal, replay, credential, memory or environment dump, process
inspection, product remedy, release, Git, Task Management, foreign loop, or
other authority. C196/C197 remains approved but unused. Agent 2 does not
delegate and does not invent commands.
