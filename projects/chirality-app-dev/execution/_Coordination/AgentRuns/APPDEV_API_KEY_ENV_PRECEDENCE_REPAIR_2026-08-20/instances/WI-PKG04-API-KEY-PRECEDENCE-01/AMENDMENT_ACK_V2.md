# N1 amendment acknowledgment v2

- RunID: `APPDEV_API_KEY_ENV_PRECEDENCE_REPAIR_2026-08-20`
- InstanceID: `WI-PKG04-API-KEY-PRECEDENCE-01`
- Disposition: `AMEND+RELAY`; current N1 reopened in place, no new node.
- FrozenAuthority:
  - `ORCHESTRATION_PLAN_V2.md` SHA-256
    `0c4391db238c354a632769901d87b21d522d5ee5f132ce288890c107b0e2931d`
  - `WORK_GRAPH_V2.md` SHA-256
    `2aa4effb89d49f65ca76b879880bf58eb37407ab65ae701dbf0423baf7d6e0d6`
- ConfirmedDefect: `SafeStorageCredentialStore.status` exposes only
  `{ configured }`, so the PKG-02 IPC consumer cannot distinguish a stored UI
  credential from an environment fallback when both coexist.
- AmendedObjective: expose an accurate non-secret store-owned source token
  `ui | env | none`, preserving provider isolation, accepted environment
  order, and existing get/set/remove semantics.
- WriteOwnership: `frontend/electron/api-key-storage.ts`, its focused test,
  PKG-04 evidence/state, and this instance's run-local controls only.
- DependencyEffect: N2 remains held until Agent 0 accepts and relays the
  amended terminal N1 handoff.
- Exclusions: root runtime contracts, IPC consumer, other packages, provider
  or storage redesign, dependencies/lockfiles, lifecycle/Checking Approval SHA,
  shared fan-in/receipt/completion log, Git and PR actions.

APP-HOLD amendment dispatch preflight: `ALLOW` for DEL-04-05, DEL-02-05,
DEL-09-06, and DEL-09-04; active/scanned held sets empty; register SHA-256
`e7408516cb32ad4414f246b594bdc64a088773d7fd6e1c6629e2184c4ac82f7f`;
scan fingerprint
`8df9d9bd5151935d593ea5e6b51393aa31ed29d036dd15d9c1be476115d83c66`.
