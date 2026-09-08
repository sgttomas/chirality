# Root Runtime account-authority adoption handoff

Status: `APPLIED_LOCALLY_VALIDATED_PENDING_INDEPENDENT_REVIEW_AND_PUBLICATION`.

Accepted upstream basis is the existing D-GOV-36 narrow semantic approval, D-GOV-37 Root implementation direction, and Runtime's immutable Gate 5 chain: owner acceptance `edfd03dfc559438531af1e714532210caf54aae4b959f246e9065f75eba0365e`; exact subject `0fcaae692e617419b6ea34fc4b57aaf6c855317803adbe3e88ebec2ff963470b`; acceptance manifest `a4cd1680631e44835e3f89c008ea791251d874c20052ca7ec4351fb92d332990`; SCA-002 snapshot `8865716ba1fb55188658ae39ae9cef06ef17290b0801552621e93faee76aeda3`; SCA-003 snapshot `ce84376323a5d213c8a6dadcbf47534ecba407a9128543250f55e4b13eaaaa48`.

D-GOV-39 records application of existing authority without a repeated semantic vote. The new immutable policy preserves the two prior adoption objects exactly and appends `D36_ACCOUNT_AUTHORITY`. The helper selects that policy and verifies the full acceptance/snapshot/member chain plus exact bounded predecessor/postimage continuity. It permits only the exact account-control companion path beyond preserved scope. Branch-local exact canonical state resolves all three adoptions as pending publication and grants no execution authority.

This run package is derivative validation evidence, not Runtime decomposition truth. The M2/G4 manifest and routed notices are current for this tranche. No `agents/` file or pinned instruction corpus changed, so the agent-index change-notice rule does not trigger corpus regeneration. Runtime canonical bytes, SOWs, earlier policies/runs/history, the four effective-state YAML files, `.gitattributes`, source/product, supplier, fixture, lifecycle, holds and release state remain untouched.

Checks are summarized in `FINAL_CHECKS.md`; detailed outputs are in `CHECKS.json`, `COMPOSITION_RESULT.json` and `check-*.log`. Independent review must verify the complete path/hash manifest and exact candidate diff. Then the parent may perform its authorized Git/PR work. Fresh CI and fetched-main post-publication recognition remain required; Runtime and App keep their own adoption, implementation, qualification and release gates.

Authorship: nondelegating ephemeral Agent 2; role and nondelegation instruction-asserted. No Git index, commit, push or merge mutation was performed.
