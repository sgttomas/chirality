# D-APP-47 - PROPOSAL: Shim-importer migration and wrapper retirement

**Status:** PROPOSAL / `AWAITING_RULING` for implementation greenlight.
**Date prepared:** 2026-07-04
**Decision ID:** D-APP-47
**Prepared by:** bridge work loop agent, at owner direction to prepare and execute all agent-lawful coordination/control work on D-APP-47.
**Structural precedent:** Follows the D-APP-46 packet pattern for surfacing a material app-dev package-boundary refactor before code lands.

This packet prepares the decision. It does not migrate imports, delete shim files,
publish a package, open F3, consume anything from piping, advance lifecycle state,
or create release, professional, certification, sealing, authentication, or
code-compliance claims.

## Decision to rule

Decide whether to authorize the internal app-dev refactor that migrates
non-shim frontend importers from `frontend/src/lib/harness/` compatibility
re-export paths to direct `@chirality/harness-contract` imports, and then
retires the compatibility shims that D-APP-46 intentionally retained.

The work is surfaced for owner ruling because D-APP-46 Option A preserved
back-compat shims as part of the extraction ruling. Retiring them is a separate
material package-boundary hardening step.

## Verified basis

| Fact | Source |
|---|---|
| D-APP-46 authorized only the internal dependency-free package extraction and retained re-exports for back-compat. | `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-46_RULING_2026-07-02.md` |
| The package exists as `@chirality/harness-contract`, version `0.0.0-private`, with `private: true`. | `projects/chirality-app-dev/frontend/packages/harness-contract/package.json` |
| The DEL-03-01 readiness baseline measured 64 non-shim frontend files still importing through `frontend/src/lib/harness` paths and zero non-shim direct package imports. | `projects/chirality-app-dev/execution/PKG-03_Runtime_Engine_Contract_and_Turn_Lifecycle/1_Working/DEL-03-01_AgentEnginePort_and_Engine_Conformance_Suite/Evidence_CODEV-002_Harness_Contract_Package_Consumption_Readiness.md` |
| The residual-work row D-APP-47 records shim migration and wrapper retirement as open, beyond D-APP-46's ruled scope. | `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/_REGISTER.md` |
| DEC-041 automation requires a package-consumption posture that does not depend on laborious manual cross-session coordination. | `projects/chirality-piping/execution/_Decomposition/SOFTWARE_DECOMP.md` DEC-041 |

## Options

| ID | Option | Consequence |
|---|---|---|
| **O-A** | **Execute full migration and retire shims.** Migrate all non-shim importers to direct package imports, then remove compatibility shim files once no internal importer depends on them. | Strongest package-boundary signal. Future consumers see the package as the canonical contract surface. Requires broad app-dev frontend test/typecheck coverage because many importers move. |
| **O-B** | **Migrate importers but retain shims temporarily.** Move non-shim importers to direct package imports, keep re-export shims for one more cycle. | Lowers immediate deletion risk while still making package imports the in-repo norm. Leaves cleanup residue and a weaker boundary than O-A. |
| **O-C** | **Defer.** Keep the D-APP-46 back-compat posture. | No implementation risk now, but package-boundary hardening remains open and DEC-041 automation has to judge through a shimmed surface. |

## Recommendation

Recommend **O-A**.

Rationale: the package extraction has already landed and the readiness baseline
shows the remaining boundary weakness precisely. The migration is internal to
app-dev, crosses no F1/F2/F3/F4 fence, and makes the contract package the
single import surface before downstream automated consumption is attempted.

## Scope constraints

- No package publication, registry push, signing, notarization, or release claim.
- No piping dependency declaration or piping-side consumption.
- No `DomainEngineProfile` / `OperationProposal` source types, domain MCP tools,
  protected-path hooks, provider/egress changes, or live binding.
- No deliverable lifecycle transition.
- If ruled, implementation must keep `@chirality/harness-contract` dependency-free
  and must pass the contract dependency lint.

## Validation implications if ruled

- Count non-shim imports before and after migration.
- `npm run harness:validate:contract-deps` in `projects/chirality-app-dev/frontend`.
- App-dev `npm run typecheck`, `npm run test`, and `npm run validate:release-quality`
  unless the implementing brief narrows coverage with a cited reason.
- Bridge closeout `scope-check`, `evidence-check`, `self-check`, `drift --all`,
  and full practitioner-harness pytest as required by the standing bridge plan.

## Human ruling

**Ruling:** OPEN.

The owner may select O-A, O-B, O-C, or give a custom ruling. Only a ruling record
and register update may treat implementation as authorized.
