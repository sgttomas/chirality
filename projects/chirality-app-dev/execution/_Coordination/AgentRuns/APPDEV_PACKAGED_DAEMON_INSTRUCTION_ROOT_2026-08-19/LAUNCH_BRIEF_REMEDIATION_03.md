# Sealed Agent 2 brief — focused agreement-fixture remediation 03

- ChildInstanceID: `A2-DAPP100-IMPLEMENT-03`
- ParentInstanceID: `AGENT1-PKG09-WORKING-ITEMS`
- PackageID / DeliverableID: `PKG-09 / DEL-09-04`
- TaskSkill: `software-bounded-implementation`
- ApplyEdits: `true`
- Objective: repair the D-APP-100 agreement regression fixture so a manifest whose instruction root differs from working root puts its HELP_HUMAN fixture under the resolved instruction root; preserve the substantive root-agreement assertion.
- Detection evidence: escalated focused run executed 12 tests; resolver/proof tests passed, but the shared daemon integration failed at session creation with `Persona 'HELP_HUMAN' is not available for direct chat` because `createProjectFixture(root, '..')` still wrote `agents/AGENT_HELP_HUMAN.md` beneath working root.
- AllowedWriteTargets: `projects/chirality-app-dev/frontend/src/__tests__/integration/runtime-desktop-cli-shared-daemon.integration.test.ts`; this run root `REMEDIATION_RETURN_03.md`.
- AcceptanceCriteria: fixture writes the agent instruction under the resolved manifest instruction root; manifest/registered root remains distinct from working root; focused three-file D-APP-100 suite passes; no production/proof/runtime/dependency/lockfile/Git changes.
- ExpectedReturn: exact diff, focused result, containment, and fresh-review readiness.
