# Sealed Agent 2 brief — packaged proof short-socket remediation 04

- ChildInstanceID: `A2-DAPP100-IMPLEMENT-04`
- ParentInstanceID: `AGENT1-PKG09-WORKING-ITEMS`
- PackageID / DeliverableID: `PKG-09 / DEL-09-04`
- TaskSkill: `software-bounded-implementation`
- ApplyEdits: `true`
- Objective: make the macOS-only packaged isolation proof allocate its runtime/userData temp tree beneath a short canonical temp prefix so `runtime/control.sock` stays within the Unix-domain-socket length limit.
- Detection evidence: unsigned `desktop:pack`, packaged dependency boundary, and instruction-root integrity passed. The first daemon then exited with durable log `runtime.daemon.initialize_failed listen EINVAL .../user-data/runtime/control.sock`; a matching manual launch under `/private/tmp/...` started successfully, while the same long `/private/var/folders/...` prefix reproduced `EINVAL`.
- AllowedWriteTargets: `projects/chirality-app-dev/frontend/scripts/run-packaged-daemon-instruction-root-proof.mjs`; `projects/chirality-app-dev/frontend/src/__tests__/scripts/run-packaged-daemon-instruction-root-proof.test.ts`; this run root `REMEDIATION_RETURN_04.md`.
- AcceptanceCriteria: proof selects a short macOS temp prefix safely and deterministically; computed control-socket path is bounded below the platform limit; isolation/cleanup/freshness/PENDING-FAIL protections remain intact; focused proof tests and syntax pass; no production/runtime/dependency/lockfile/Git changes.
- ExpectedReturn: exact diff, tests, containment, and exact manager host rerun command.
