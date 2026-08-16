# Sealed Agent 2 brief — packaged adapter loading implementation

- RequestedBy: `WI-PKG04-DEL0401`
- RunID: `APPDEV_PACKAGED_ADAPTER_LOADING_2026-08-16`
- ParentInstanceID: `WI-PKG04-DEL0401`
- ChildInstanceID: `A2-IMPLEMENTER-01`
- PackageID / DeliverableID: `PKG-04` / `DEL-04-01`
- Objective: finish the narrow behavior-preserving App composition that loads
  Root `engine-claude` and `engine-pi-omlx` wrappers, plus automated packaged
  GUI/daemon/CLI proof preserving package/model attribution.
- AcceptedBasis: clean base `65735390590e500dbbea6b63a4a79ba42944bf6d`;
  APP-HOLD-1 dispatch `ALLOW`; D-APP-72, D-APP-73, accepted SCA-APP-003; current
  manager partial diff is the serialized integration predecessor.
- DeclaredReads: affected App frontend sources/tests/build scripts; read-only
  Root `runtime/packages/{engine-claude,engine-pi-omlx,client,daemon,cli,contracts,core}`.
- AllowedTools: repository inspection, `apply_patch`, focused frontend tests,
  typecheck/build-electron, package-lock mechanical refresh.
- AllowedWriteTargets: `projects/chirality-app-dev/frontend/electron/runtime-host.ts`;
  `frontend/scripts/build-electron.mjs`; `frontend/scripts/verify-packaged-dependency-boundary.mjs`;
  `frontend/tsconfig.electron.json`; `frontend/package.json`;
  `frontend/package-lock.json`; focused tests under
  `frontend/src/__tests__/{electron,integration,scripts}/**` only.
- Exclusions: Root `runtime/**`, deliverable/receipt/AgentRuns records,
  lifecycle/approval fields, providers/network, release/distribution, foreign surfaces.
- ExpectedOutputs: compiling production composition; focused automated proof
  that Root wrappers are the packaged daemon engines, Desktop/CLI are clients
  of that daemon, and Claude/Pi package plus model attribution is unchanged;
  exact changed paths and check results.
- AcceptanceCriteria: smallest coherent diff; no new runtime semantics; no UI
  behavior; focused tests and Electron typecheck/build pass; no generated
  build artifacts retained.
- Escalation: any required Root write, attribution change, provider/network or
  release boundary, incompatible Root wrapper semantics, or unclear owner-class choice.
- Delegation: prohibited; this is Agent 2.
