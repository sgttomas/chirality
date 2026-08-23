# ACTIVATION — A2-PKG09-R20-PR632-POSTCOMMIT-VALIDATE-01

- RunID: `APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23`.
- ParentInstanceID: `WI-PKG09-R20-PR632-REPAIR-MANAGER-01`.
- ChildInstanceID: `A2-PKG09-R20-PR632-POSTCOMMIT-VALIDATE-01`.
- Role: delegated-harness-native ephemeral generalist in explicit Agent-2 mode; role and non-delegation are instruction-asserted. No delegation was performed.
- Sealed brief: `briefs/A2-PKG09-R20-PR632-POSTCOMMIT-VALIDATE-01.md`.
- Objective: run and freeze only the still-unreached governance/control-plane pre-push gates after the manager-observed exact candidate-whitespace PASS.
- Accepted basis: branch `codex/app-login-proof-r20-repair`; HEAD `de2080a7ac82f636fca3f8be57b20dc0e9a80fa8`; parent `85caafd4882a2ffff204ed87334171608ce462be`; frontend tree `b4c73edda1fe3346815ce75449b2327c80c79bf8`.
- Prior gate retained, not rerun at activation: `python3 tools/validation/validate_candidate_whitespace.py --base-ref origin/main`, exit `0`, exact manager-observed output `PASS: candidate whitespace is clean (untracked binary/symlink paths safely skipped: 0).`
- Write scope: only this instance directory. Shared RunID, Receipt, repair evidence, frontend, package, and proof bytes are read-only.
- Hard exclusions: no product/frontend/runtime tests or typecheck; no build, package, supply or package verifier; no daemon/precheck/proof/procedure; no GUI, launchd, operator/private evidence, signing, release, network, or Git mutation.
- Stop rule: stop immediately on a substantive failure, scope drift, identity mismatch, command ambiguity, or need for an out-of-scope write.
