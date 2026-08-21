# Agent 0 direct bounded Agent 2 launch brief — durable manager intake

- RequestedBy: Agent 0 `HELP_HUMAN`
- RuntimeTaskName: `/root/login_proof_direct_fix`
- RunID: `APPDEV_LAUNCHAGENT_LOGIN_PROOF_PREP_2026-08-21`
- ChildInstanceID: `A2-PKG09-LOGIN-PROOF-PREP-DIRECT-01`
- PackageID: `PKG-09`; DeliverableID: `DEL-09-04`
- Objective: directly repair the unvalidated login-proof candidate after the
  manager child failed to advance, without bypassing WORKING_ITEMS acceptance,
  review, checks, state, or fan-in.
- AllowedWriteTargets: exactly the new login-proof script and focused test.
- Acceptance: implement the original prepare/capture brief, including exact
  argv/session/source identity, redaction, stale-state refusal, bounded cleanup,
  default/launcher exclusion, and focused tests.
- Exclusions: no host harness/LaunchAgent action, logout/login, bootstrap,
  kickstart, other file, Git, proof claim, or scope expansion.
- ReturnRoute: direct child terminal update relayed to
  `WI-PKG09-LOGIN-PROOF-PREP-02` for manager validation.

This record transcribes the Agent 0 sealed dispatch relayed to the replacement
manager; it does not claim the manager launched or supervised the direct child.
