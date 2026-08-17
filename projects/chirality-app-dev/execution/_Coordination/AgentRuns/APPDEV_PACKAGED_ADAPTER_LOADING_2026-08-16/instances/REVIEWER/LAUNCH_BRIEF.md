# Sealed TASK + software-code-review brief

- RequestedBy: `WI-PKG04-DEL0401`
- RunID: `APPDEV_PACKAGED_ADAPTER_LOADING_2026-08-16`
- ParentInstanceID: `WI-PKG04-DEL0401`
- ChildInstanceID: `A2-REVIEWER-01`
- ScopePath: `projects/chirality-app-dev/frontend`
- TaskSkill: `software-code-review`
- PROFILE_PATH: `projects/chirality-app-dev/software-workflow.json`
- ImplementationBrief: review 100% of the frozen nine-path candidate that
  composes Root Claude/Pi adapters into the App runtime host and adds packaged
  Desktop/daemon/CLI attribution proof.
- AcceptedBasis: clean base `65735390590e500dbbea6b63a4a79ba42944bf6d`;
  APP-HOLD-1 dispatch `ALLOW`; D-APP-72, D-APP-73, accepted SCA-APP-003, and
  the live DEL-04-01 Remaining item.
- DiffBasis: working tree against the AcceptedBasis, restricted to the nine
  exact product/test paths listed below. Their frozen SHA-256 values are:
  `runtime-host.ts` `512a1a9da338e8af9f79bd715c425bbc2955615ec9ac6968ae5af72e7d832b73`;
  `package-lock.json` `717d541fe6ee090aae79d4a386bbde1c8ff6ee136a50242d956500d76e80a458`;
  `package.json` `2f15831e714969a55a92d07012adc41e18890e9554f52effee7f9e71edab0f95`;
  `build-electron.mjs` `a0d6f87d1253cec386996db2d6998b3d81fe18f455dd18fcf94e1b6566f49ce1`;
  `verify-packaged-dependency-boundary.mjs` `bf7dad41d6e0fe105a77376820cfaabaa1eb3c3ed2723ce68dfcdc54f02bb076`;
  `runtime-host-agent1-manager.test.ts` `f3059bf21358235261430bb147c3ced50c4e5a027f874a10669ec17f6aeb04ec`;
  `runtime-desktop-cli-shared-daemon.integration.test.ts` `55e775f3794e3469f10741ea6c003e87f341c8c95c8d80b97dbf46779ec0c921`;
  `verify-packaged-dependency-boundary.test.ts` `65a2a520fa098dfed133a7f6b9972102401f9302de04afb95477a004b6a723d4`;
  `tsconfig.electron.json` `ee4d4461c38b1524290e4079ede3122c6307852f25b9c0a4cec69a229a731e0e`.
- ExactReviewPaths: `frontend/electron/runtime-host.ts`,
  `frontend/package.json`, `frontend/package-lock.json`,
  `frontend/scripts/build-electron.mjs`,
  `frontend/scripts/verify-packaged-dependency-boundary.mjs`,
  `frontend/tsconfig.electron.json`,
  `frontend/src/__tests__/electron/runtime-host-agent1-manager.test.ts`,
  `frontend/src/__tests__/integration/runtime-desktop-cli-shared-daemon.integration.test.ts`,
  `frontend/src/__tests__/scripts/verify-packaged-dependency-boundary.test.ts`.
- AllowedWriteTargets: none.
- ApplyEdits: false.
- VerificationEvidence: focused Vitest 11 pass; typecheck pass; Electron build
  pass; unsigned `desktop:pack` and packaged source proof passed before a final
  verifier-only refactor; the final verifier revision has syntax/import/fixture
  pass, with the real packaged-verifier rerun explicitly manager-owned; diff
  check pass; no Root runtime write.
- ReviewQuestions: trace credentials, capabilities, interrupt/cancel behavior,
  residency and transcript callbacks, EngineRegistry attribution, GUI/daemon/CLI
  ownership, source-map/package verification truth, dependency/lock coherence,
  test realism, errors/concurrency, security, and exact scope. Confirm package
  and model attribution are unchanged and that the CLI remains client-only.
- Exclusions: do not edit, install, package, release, call providers, change
  lifecycle/approval state, or infer owner acceptance.
- ExpectedReturn: `PASS` with no actionable finding and explicit fan-in safety,
  or `BLOCK` with exact file/line, impact, evidence, and remediation direction.
- Delegation: prohibited; this is a fresh read-only Agent 2.
