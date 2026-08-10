# Agent-2 brief — D-APP-92 Attempt-8 packet adversarial verification

- RequestedBy: `WORKING_ITEMS /root/dapp92_attempt7_preparation`
- RunID: `APPDEV_DAPP92_OPTION_A_NATIVE_TRACE_REPLAY_2026-08-04`
- ParentInstanceID: `/root/dapp92_attempt7_preparation`
- ChildInstanceID: `A2-DAPP92-A-ATTEMPT8-PACKET-VERIFY-01`
- PackageID: `PKG-09`
- DeliverableID: `DEL-09-04` packet verification only
- Objective: adversarially determine whether proposed v1.16 and its three
  scripts/request are exact, internally coherent, executable as written, safe
  on every stop path, and decision-ready under D-APP-92 without granting or
  performing runtime execution.
- ScopePath: read-only over the D-APP-92 run root, cited candidate/baseline
  bytes, live frontend/source paths, and current fixed-root/frontend state.
- AcceptedBasis: Attempt-7 verifier SHA-256
  `1546dc33b24bbbd86d43d6b547b404113267e594b4eb6f0247c59455ad13ce6f`;
  packet-preparer return SHA-256
  `b337532eff788b3e256d5bdd3b21ff7d2989d480163522c84e037863d699237a`;
  current proposal/request/script hashes stated in that return.
- DeclaredReads: proposal/request/scripts/return, every prior command amendment,
  manifests, accepted package evidence, candidate source, current baseline,
  and relevant Root/App source for exact CLI/runtime semantics.
- AllowedTools: read-only file/search/hash/JSON checks; `node --check` on the
  three proposal scripts; shell syntax/read-only path-existence checks that do
  not execute proposed behavior; frontend Git status/diff; no process/runtime
  inspection.
- AllowedWriteTargets: only
  `reviews/A2_ATTEMPT8_PACKET_FRESH_ADVERSARIAL_VERIFIER_RETURN.md`.
- ExpectedOutputs: recomputed hashes, command range/uniqueness/accounting,
  script syntax result, command/path/cwd validity, timing and two-session
  protocol analysis, every-terminal-path cleanup/rollback analysis,
  credential/redaction/exclusion analysis, findings with severity, and a
  calibrated `PASS_DECISION_READY` or `BLOCK_PACKET_REPAIR_REQUIRED` verdict.
- AcceptanceCriteria: no stale hash/path/ID; every internal executable/tool
  command is exactly enumerated and owner-gated; dynamic substitutions are
  fail-closed; C196/C197 are byte-preserved and not widened; debugger/
  controller terminality precedes evidence cleanup; every C247-or-later stop
  has an executable cleanup/rollback path; no PID-reuse or unrelated-process
  hazard; exact D-APP-89 restoration; no credential value/raw registration
  output; no unbounded process/memory/environment surface; no unsupported
  historical/causal/acceptance claim.
- Escalation: `BLOCK_PACKET_REPAIR_REQUIRED` for any executable-path, command,
  timing, cleanup, authorization, hash, safety, or evidence-retention defect.

EXCLUSIONS: execute no proposed command except `node --check`; make no repair;
no package/helper/GUI/LLDB/attach/signal/replay/network/credential/process
inspection/product/release/Git/TM/foreign-loop action. Do not delegate.
