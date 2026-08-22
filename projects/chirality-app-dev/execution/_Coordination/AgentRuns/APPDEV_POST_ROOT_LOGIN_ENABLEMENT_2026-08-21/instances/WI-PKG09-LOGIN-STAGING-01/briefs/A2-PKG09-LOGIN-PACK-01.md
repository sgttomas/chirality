# Sealed brief — A2-PKG09-LOGIN-PACK-01

- RequestedBy: `WI-PKG09-LOGIN-STAGING-01`
- RunID: `APPDEV_POST_ROOT_LOGIN_ENABLEMENT_2026-08-21`
- ParentInstanceID: `WI-PKG09-LOGIN-STAGING-01`
- ChildInstanceID: `A2-PKG09-LOGIN-PACK-01`
- AgentType: ephemeral generalist Agent 2 (no delegation)
- PackageID / DeliverableID: `PKG-09` / `DEL-09-04`
- AcceptedBasis: `1b375af4f1219ecfc00fc2755854aa7fd4220901`
- Dependency: frozen owner direction and R12 preparation record

## Objective

Execute the single authorized unsigned app-directory packaging command from
`projects/chirality-app-dev/frontend`, preserve auditable command evidence,
and return the exact packaged app and source identities without launching or
deploying anything.

## Declared reads and tools

Read the root instructions; current run plan/transcription; DEL-09-04 status,
R12, and owner baseline ruling; `software-workflow.json`; build docs; package
manifest/scripts; current Git state. Tools: read-only shell inspection and the
single `npm run desktop:pack` execution. Do not use network or install/update
dependencies.

## Allowed writes

- Documented ignored build/evidence outputs under
  `projects/chirality-app-dev/frontend/{.next,dist-electron,dist-runtime,dist,artifacts}`.
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_POST_ROOT_LOGIN_ENABLEMENT_2026-08-21/instances/WI-PKG09-LOGIN-STAGING-01/executor/**`.

No tracked source or package-truth edit is allowed.

## Required execution and return

1. Record exact 40-character `git rev-parse HEAD`, branch, Node/npm versions,
   and porcelain status before execution.
2. Record read-only before observations for the forbidden operator label,
   plist, and CLI launcher if safely available. Never mutate them.
3. Run exactly `npm run desktop:pack` from `frontend` with no artifact-proof
   label and capture the transcript/exit/duration.
4. Do not launch `Chirality.app` or run the login-proof script.
5. Verify the absolute `frontend/dist/mac-arm64/Chirality.app` path exists;
   inspect only safe identity/posture fields needed for the return.
6. Record the integrity-summary verdict and current HELP_HUMAN SHA-256 if
   exposed by the generated evidence.
7. Prove the frontend diff command is empty from build commit to current HEAD,
   and record post-command porcelain status.
8. Repeat the read-only forbidden-target observations and report whether they
   changed.
9. Write `executor/RETURN.md` and raw log(s), then return PASS or a calibrated
   blocker. Do not stage, commit, push, open a PR, or write shared surfaces.

## Escalation / fail-closed conditions

Stop if the command would require signing/notarization/distribution, dependency
installation, GUI launch, operator deployment, `prepare`/`capture`,
`launchctl` mutation, or mutation of the forbidden plist/launcher paths. Stop
on any tracked write outside the declared persistent scope.

