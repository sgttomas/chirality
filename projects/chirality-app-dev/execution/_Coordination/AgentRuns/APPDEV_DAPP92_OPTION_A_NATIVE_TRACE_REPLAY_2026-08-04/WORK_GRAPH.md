# Work graph — D-APP-92 Option A native trace and sealed replay

- Version: `v1 — frozen before execution`
- Selection authority: exact D-APP-92 Option A owner ruling
- Posture: `TERMINAL_FAN_OUT_IN`, serialized implementer then fresh verifier
- Package/deliverable: `PKG-09 / DEL-09-04`

## Nodes

1. `WI-PKG09-DAPP92-A-SEAL` — manager-owned authority/input rebind, command classification, manifests, and sealed replay transcript.
2. `A2-DAPP92-A-IMPLEMENT-01` — fresh Agent 2, no delegation; execute only enumerated unprivileged preparation and replay commands; stop at the first command-specific privilege/entitlement/GUI-authority boundary; freeze evidence and restore all temporary state.
3. `A2-DAPP92-A-VERIFY-01` — genuinely fresh read-only Agent 2, no delegation; released only after terminal implementer return and rollback; adversarially verify evidence, authority, cleanup, and causal calibration.
4. `WI-PKG09-DAPP92-A-FANIN` — manager validation and exact handoff to App `HELP_HUMAN`.

## Edges and gates

- `SEAL -> IMPLEMENT`: release only after every input hash reproduces and every intended tool/command is individually enumerated.
- `IMPLEMENT -> VERIFY`: release only after raw evidence is frozen, product source is byte-restored, generated/runtime residue is removed, and any approval stop is exact.
- `VERIFY -> FANIN`: no acceptance or next-step claim without fresh verifier PASS.
- Any drift, credential exposure, privilege/entitlement need, GUI automation need, or unenumerated command immediately holds dependent nodes.

## Ownership

The implementer owns only the exact temporary frontend/run-time surfaces and
its instance evidence directory. The verifier is read-only except its return.
The manager owns run-root integration, telemetry summary, DEL run-record
reconciliation if truthful, and handoff. Nodes are serialized because source,
packages, runtime state, and cleanup overlap.

## Acceptance boundary

This run may establish diagnostic evidence only. The unchanged D-APP-88 gate
requires the first ordinary authenticated post-GUI signal to enter App
teardown and bounded Root stop, exit the helper, and remove socket/owner state.
No result automatically accepts D-APP-88, closes DEL-09-04, fires TM-APP-036,
selects a remedy, or grants release/reliance credit.
