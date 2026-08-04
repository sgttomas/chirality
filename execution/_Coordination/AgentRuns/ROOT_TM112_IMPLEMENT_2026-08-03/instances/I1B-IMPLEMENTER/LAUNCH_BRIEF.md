# I1B-IMPLEMENTER sealed Agent 2 retry brief

RequestedBy: WORKING_ITEMS
RunID: `ROOT_TM112_IMPLEMENT_2026-08-03`
ParentInstanceID: WORKING_ITEMS root activation
ChildInstanceID: `I1B-IMPLEMENTER`
AgentType: fresh ephemeral generalist Agent 2; no delegation
PackageID: `ROOT-RUNTIME-DAEMON`
Bounded integration scope: `TM-ROOT-112`
Attempt: `2`, after `I1` ended pre-write without a return.

## Objective and sealed basis

Implement and test the exact accepted N-STOP-1 through N-STOP-7 G2+C1+F1
daemon shutdown contract. Read and obey the complete sealed brief
`execution/_Coordination/AgentRuns/ROOT_TM112_SEMANTIC_ACCEPTANCE_2026-08-03/IMPLEMENTATION_BRIEF.md`
at pre-normalization authoring/execution SHA-256
`b8163531fb8f41142d6c067111fa84d2065ebd28c47f1c1e32e9218c16e6a218`.
Its later semantically identical whitespace-normalized publication SHA-256 is
`617512278aa93e05a07334b5f666e7a7e1f2e869882c33da6fd63b6fcdc92e9d`;
this retry remained historically sealed to the pre-normalization form.
Recheck that brief and the three frozen product hashes before writing; they
were unchanged after the first attempt was interrupted.

## Allowed reads and tools

Root `AGENTS.md`, this brief, the sealed implementation/acceptance/authority
carrier, accepted clauses/transcript, current three product files, runtime
manifest/lock, and read-only imported interfaces. Use read/search,
`apply_patch`, the existing runtime test/typecheck/build commands, Node identity
checks, and deterministic hashing/diff checks. No network install or Git.

## AllowedWriteTargets

- `docs/SPEC.md`, section 14.1 only;
- `runtime/packages/daemon/src/runtime-daemon.ts`;
- bounded regression cases in `runtime/tests/daemon.test.ts`;
- `execution/_Coordination/AgentRuns/ROOT_TM112_IMPLEMENT_2026-08-03/instances/I1B-IMPLEMENTER/**`
  except this launch brief.

## Required return

Write `RETURN.md` with final hashes, N-STOP mapping, exact commands/results,
Node/platform coverage and gaps, observed timings/outcomes, and scope
containment. Run the exact bounded matrix plus existing daemon suite and
runtime typecheck/build. `stop()` must return the identical stored in-flight
Promise to concurrent callers; do not use an `async stop()` wrapper that
changes Promise identity. Production grace/settle policy stays exactly
2000/500ms with no public timing override.

If exact semantics cannot fit the three product files, stop promptly with a
concrete scope-change request in `RETURN.md`. Do not touch registers, receipts,
App/Piping/DEL, other docs/source, lifecycle, or Git. App routing remains held.
