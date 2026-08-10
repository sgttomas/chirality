# Agent-2 brief — D-APP-92 Attempt-7 fresh adversarial verification

- RequestedBy: `WORKING_ITEMS /root/dapp92_attempt7_preparation`
- RunID: `APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04`
- ParentInstanceID: `/root/dapp92_attempt7_preparation`
- ChildInstanceID: `A2-DAPP92-A-ATTEMPT7-VERIFY-01`
- PackageID: `PKG-09`
- DeliverableID: `DEL-09-04` diagnostic preparation only
- Objective: independently and adversarially verify whether Attempt 7 executed
  exactly C231-C244 once, satisfied the repaired mock two-session protocol,
  obeyed the terminal-session-before-cleanup invariant, cleaned all temporary
  state, and supports preparation—but not execution—of a real-runtime packet.
- ScopePath: read-only over the D-APP-92 run root, fixed mock-root absence,
  frontend Git state, and relevant ruling/register/receipt bytes.
- AcceptedBasis: D-APP-92 Option A ruling; exact owner Attempt-7 token;
  immutable amendment v1.15; sealed executor brief; prior R5 handoff; executor
  terminal return and all Attempt-7 evidence.
- Dependencies: executor terminal return SHA-256
  `14fbe0794fe216055fee2a362f52e72a03c497198ea34ff5f6d393da03621ccc`.
- DeclaredReads: the current bytes named above, frozen mock scripts, current
  mock-root absence, frontend Git state, and no other runtime/process surface.
- AllowedTools: read-only file reads, SHA-256, JSON parsing, `git status`/
  `git diff` limited to frontend and declared run root, fixed-path absence test,
  and textual searches needed for exact command/exclusion accounting.
- AllowedWriteTargets: only
  `reviews/A2_ATTEMPT7_FRESH_ADVERSARIAL_VERIFIER_RETURN.md`.
- ExpectedOutputs: exact hash recomputation; command-ID accounting; independent
  protocol/schema/PID/state/natural-exit/order assessment; cleanup and
  containment assessment; scope-exclusion assessment; calibrated verdict and
  next gate.
- AcceptanceCriteria: every C231-C244 ID has exactly one supported disposition;
  all bound hashes reproduce; protocol result matches frozen script semantics;
  C242 precedes cleanup; fixed root absent; frontend clean; no excluded effect;
  no stronger runtime or causal inference.
- Escalation: return `BLOCK` on any missing/contradictory evidence, hash/schema/
  command mismatch, live residue, unauthorized action, or unsupported claim.

EXCLUSIONS: no execution, repair, retry, LLDB, attach, package, cache, network,
helper, GUI, signal, replay, credential, memory/environment dump, process
inspection, product remedy, release, Git mutation, Task Management, foreign
loop, or other action. The verifier does not delegate.
