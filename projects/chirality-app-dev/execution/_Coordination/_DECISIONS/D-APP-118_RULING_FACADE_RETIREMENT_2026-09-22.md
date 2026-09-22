# D-APP-118 — Ruling: retire the old facade

Status: **RULED — RETIRE**  
Owner: Ryan Tufts  
Recorded: 2026-09-22 by HELP_HUMAN (Agent 0)

## Owner words and effect

> For the App audit, other than D-APP-118, these appear to be issues of governance about governance and whether to make things more robust and complete or allow for alternatives and ambiguity?  Help me understand.  For D-APP-118 my ruling is a clear "Retire the old facade" we will not be using it and retaining support for it and tests related to it is a waste.

The quoted current conversation message is one owner act, applied here to its App retirement and shared Root coordination consequences. It is not two invented project approvals or personal owner review of the final code diff. SHA-256 of the quoted UTF-8 text (without a trailing newline): `a4b4e816e75887159702a828ff7d0a330aeff86e84cd50e1e566599a242470e9`.

Retire `@chirality/harness-contract`, its rollback-only test, its facade-presence/import-count validator, and obsolete workspace/lockfile/script wiring. This expressly ends the retained, tested facade rollback obligation established for the D-APP-89 migration cycle. It supersedes D-APP-118's HOLD recommendation and the later proposal's recommendation to retain it. Those historical records remain unchanged. Retiring the test's purpose is part of the owner's instruction, not removal of a still-required check merely to obtain a pass.

The required current consumer census, exact reviewed diff, affected App/Runtime checks and independent review establish safe application. The prior demand for literal zero consumers cannot count the deliberately retired support test as a reason to preserve its subject forever. No further vote on keeping or removing that support is required. Git preserves the exact preimages and inverse patch; the facade is no longer a supported rollback product.

## Application scope

- Delete the private App facade package and its dedicated rollback test and validator. Remove their package and release-quality wiring without dependency-version churn.
- Preserve direct canonical `@chirality/runtime-contracts` imports, current Runtime contracts and applicable behavior/containment tests. Correct the generated catalog's obsolete source label in Runtime and its App output; no Runtime API semantics change.
- Repoint current contract and reliance-register source locators; refresh the local export inventory. The dated TYPES forward note and SHA-pinned historical consumption records describe earlier source and remain historical, not current package support. No external export target is replaced or published.
- Apply this ruling in the decision register and DEL-03-01 claim/Remaining records. D-APP-101's packet/routing purpose is fulfilled by the current cross-project retirement work; Root and Runtime receive the linked coordination record.

The source census establishes tracked repository consumers, not absence of every external or dynamically constructed import. The package was private; no external compatibility guarantee is added. The exact change and observed checks are recorded in `execution/_Coordination/AgentRuns/APP-FACADE-RETIREMENT-20260922/` and the Root integration record at `execution/_Coordination/AgentRuns/HELP-HUMAN-20260922-FACADE-RETIREMENT/` (repository-relative).

## Preserved decisions and limits

This closes the facade-retention choice only. D-APP-48 successor identity, Tier-0 integration gaps, DEL-03-01's other conformance residuals, lifecycle and Checking Approval SHA retain their existing status. D-APP-116, D-APP-117, D-APP-119 and P-01's two reserved keys are not ruled by the owner's explanatory question. No provider expansion, changed Codex policy, release, signing, notarization, distribution or professional reliance is authorized.
