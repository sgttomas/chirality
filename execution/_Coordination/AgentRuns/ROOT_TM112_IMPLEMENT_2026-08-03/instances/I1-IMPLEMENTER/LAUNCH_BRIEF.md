# I1-IMPLEMENTER sealed Agent 2 brief

RequestedBy: WORKING_ITEMS
RunID: `ROOT_TM112_IMPLEMENT_2026-08-03`
ParentInstanceID: WORKING_ITEMS root activation
ChildInstanceID: `I1-IMPLEMENTER`
AgentType: ephemeral generalist Agent 2; no delegation
PackageID: `ROOT-RUNTIME-DAEMON`
Bounded integration scope: `TM-ROOT-112`

## Objective

Implement and test the exact accepted N-STOP-1 through N-STOP-7 G2+C1+F1 daemon shutdown contract, with no semantic invention and no outward scope expansion.

## Sealed context and reads

- Root `AGENTS.md` and this brief.
- `execution/_Coordination/AgentRuns/ROOT_TM112_SEMANTIC_ACCEPTANCE_2026-08-03/IMPLEMENTATION_BRIEF.md` at pre-normalization authoring/execution SHA-256 `b8163531fb8f41142d6c067111fa84d2065ebd28c47f1c1e32e9218c16e6a218`; its later semantically identical whitespace-normalized publication SHA-256 is `617512278aa93e05a07334b5f666e7a7e1f2e869882c33da6fd63b6fcdc92e9d`. The pre-normalization form was the complete semantic, matrix, acceptance, and prohibition contract sealed for this dispatch.
- The acceptance record, authority binding, signed transcript, accepted clauses, current three product files, runtime manifest/lock, and read-only imports needed to understand existing interfaces.

The parent verified the acceptance validator and all source hashes before dispatch. Recheck the implementation brief and three product hashes before the first product write; stop on drift.

## Allowed tools

Read/search, `apply_patch`, existing package-manager/test/typecheck/build commands needed by the sealed brief, Node runtime identity/version checks, and deterministic hashing/diff/scope checks. No network dependency installation or Git mutation.

## AllowedWriteTargets

- `docs/SPEC.md`, section 14.1 only;
- `runtime/packages/daemon/src/runtime-daemon.ts`;
- bounded regression cases in `runtime/tests/daemon.test.ts`;
- `execution/_Coordination/AgentRuns/ROOT_TM112_IMPLEMENT_2026-08-03/instances/I1-IMPLEMENTER/**` except this parent-owned launch brief.

## Expected outputs

- Exact implementation and bounded tests.
- `RETURN.md` with changed hashes, design mapping N-STOP-1..7, exact commands/results, Node/platform identity, durations and observed outcomes, coverage gaps, and scope statement.
- Raw/structured test evidence as useful, stored only in the instance directory.

## Acceptance criteria

Every behavior, regression-matrix case, check, claim boundary, and prohibition in the sealed implementation brief is mandatory. Do not weaken production 2000/500ms constants through a public timing override. The candidate remains unaccepted and App routing remains held.

## Escalation

If any accepted behavior cannot fit the exact three product files, if a source hash drifted, or if an interface outside scope must change, stop without outward write and return a scope-change request. Agent 2 may not delegate.
