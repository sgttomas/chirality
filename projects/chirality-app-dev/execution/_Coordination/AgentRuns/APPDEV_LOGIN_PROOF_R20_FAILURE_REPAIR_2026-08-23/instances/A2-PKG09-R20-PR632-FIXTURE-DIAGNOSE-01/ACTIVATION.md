# Activation — PR #632 fixture-mode diagnosis

- RunID: `APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23`
- ParentInstanceID: `WI-PKG09-R20-PR632-FIXTURE-MANAGER-01`
- ChildInstanceID: `A2-PKG09-R20-PR632-FIXTURE-DIAGNOSE-01`
- Role: delegated-harness-native ephemeral generalist in explicit Agent-2 mode; role/non-delegation instruction-asserted.
- Objective: reproduce the focused login-proof fixture failure exactly once under `umask 0002`, freeze complete evidence, and classify fixture versus product path-creation modes read-only.
- AcceptedBasis: branch `codex/app-login-proof-r20-repair`; commit `980f5951dbbfe88302514802384e4ffec33c38b9`; frontend tree `b4c73edda1fe3346815ce75449b2327c80c79bf8`.
- WriteScope: this instance directory only. Frontend, shared RunID records, index, and Git history are read-only.
- Activated: `2026-08-23`.
