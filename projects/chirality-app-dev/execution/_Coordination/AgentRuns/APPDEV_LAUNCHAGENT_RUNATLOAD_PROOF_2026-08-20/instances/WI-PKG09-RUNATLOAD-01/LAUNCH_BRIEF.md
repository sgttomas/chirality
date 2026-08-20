# Launch Brief — WI-PKG09-RUNATLOAD-01

- RequestedBy: HELP_HUMAN
- RunID: `APPDEV_LAUNCHAGENT_RUNATLOAD_PROOF_2026-08-20`
- InstanceID: `WI-PKG09-RUNATLOAD-01`
- Role: `WORKING_ITEMS` (Agent 1)
- PackageID: `PKG-09`
- DeliverableID: `DEL-09-04`
- Objective: implement and validate the smallest product/test tranche that closes the D-APP-97-authorized login-time `RunAtLoad` packaged-service proof gap.
- AcceptedBasis: D-APP-97 C1; live DEL-09-04 SOW/status/dependencies; prior R6 daemon-service evidence; software workflow profile; owner development-pressure and one-tranche steers.
- Dependencies: none; predecessor PRs #586 and #589 are merged.
- DeclaredReads: repo instructions; App loop plan/receipts; D-APP-97; PKG-09/DEL-09-04; frontend packaging/daemon sources and tests; validation/release docs; existing CI workflows.
- AllowedWriteTargets: `projects/chirality-app-dev/frontend/**`; `.github/workflows/**` only if required for the bounded proof; this run root and DEL-09-04 evidence/run-record paths during manager close; do not write receipt/completion-log/shared closeout surfaces before Agent 0 fan-in.
- Exclusions: default `com.chirality.runtime` job or owner LaunchAgent/account state; owner-machine deployment; signing/notarization/publication/distribution; release/lifecycle/reliance claims; provider expansion; dependencies/lockfiles; `_DomainEngines/**`; other projects; decision registers.
- RequiredMethod: load `agents/AGENT_WORKING_ITEMS.md` and `projects/chirality-app-dev/software-workflow.json`; use one bounded TASK/Agent-2 implementation child and fresh review as warranted; freeze the intra-package graph before child dispatch.
- AcceptanceCriteria: fail-closed proof uses a non-default unique label and disposable macOS CI/host account's actual `~/Library/LaunchAgents`; demonstrates `RunAtLoad` launch without `kickstart`; binds to the packaged app identity; proves process/job/plist cleanup; protects default label/path; focused and registered full checks pass; fresh review passes; return names residuals and reruns.
- ReturnContract: validated package return with changed paths, tests/evidence, containment, derivative status, blockers/waivers/reruns, and exact CHANGE handoff. Do not commit or open the PR.
- Escalation: stop and report if closure requires real owner-machine state, destructive cleanup, weakened isolation, unregistered checks, broader public/release contract, or any fenced scope.
