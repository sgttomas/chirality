# Agent-2 brief — D-APP-92 Attempt-6 preparation execution

- RequestedBy: `WORKING_ITEMS /root/dapp92_attempt6_preparation`
- RunID: `APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04`
- ParentInstanceID: `/root/dapp92_attempt6_preparation`
- ChildInstanceID: `A2-DAPP92-A-ATTEMPT6-PREPARE-01`
- PackageID: `PKG-09`
- DeliverableID: `DEL-09-04` diagnostic preparation only
- Objective: execute exactly C217-C230 from immutable amendment v1.14 and
  return complete evidence without widening authority.
- ScopePath: this run root plus fixed temporary root
  `/private/tmp/chirality-dapp92-attempt6-protocol`.
- AcceptedBasis: D-APP-92 Option A ruling; exact owner Attempt-6 token;
  `OWNER_ATTEMPT6_PREPARATION_APPROVAL_ADOPTION.md`;
  `COMMAND_REGISTER_AMENDMENT_V1_14.md`; bound proposal SHA-256
  `cf929fa33828a59db388576555dc37467710ac6246526ef262df0c39b42dfd45`.
- Dependencies: immutable scripts at the two bound hashes; fixed mock root
  absent before C221.
- DeclaredReads: adopted amendment, its bound proposal, its two bound scripts,
  and only the C217-C230 outputs.
- AllowedTools: exact C217-C230 commands and PTY byte writes only.
- AllowedWriteTargets: fixed mock root; run-local
  `evidence/attempt6-preparation/**`; run-local instance terminal return.
- ExpectedOutputs: public no-target LLDB help/prompt capture; exact mock
  protocol result and hash; command outcomes; cleanup proof; terminal return.
- AcceptanceCriteria: C217 has no target; C218 returns help only; C219 exits
  cleanly; exact script hashes; direct-child PID and sentinel match; mock child
  exits naturally; C229-C230 pass; no fixed-root residue; no frontend change;
  all exclusions hold.
- Escalation: stop on target, privilege/entitlement prompt, PID/sentinel
  mismatch, timeout, command deviation, hash mismatch, or cleanup failure.

EXCLUSIONS: no attach, package/reconstruction, cache seed, network, helper,
GUI, signal, replay, credential, memory or environment dump, product remedy,
release, Git, Task Management, foreign loop, process inspection beyond the
script's own direct-child PID record, or other authority. C196/C197 remains
approved but unused. Agent 2 does not delegate and does not invent commands.
