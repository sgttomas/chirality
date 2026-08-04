# ROOT TM-ROOT-112 bounded implementation orchestration

RunID: `ROOT_TM112_IMPLEMENT_2026-08-03`
Parent: HELP_HUMAN
Manager: WORKING_ITEMS (Agent 1)
Package/bounded integration scope: `ROOT-RUNTIME-DAEMON / TM-ROOT-112`
Selected set: `TM-ROOT-112` only
Plan version: `v1 / FROZEN`
Pattern: `TERMINAL_FAN_OUT_IN` with serialized author then fresh refuter
Selection authority: sealed `ROOT-TM112-IMPLEMENT-01` implementation brief and signed `ROOT-TM112-SEMANTICS-01 G2 C1 F1` owner ruling.

## Accepted basis

- `execution/_Coordination/AgentRuns/ROOT_TM112_SEMANTIC_ACCEPTANCE_2026-08-03/IMPLEMENTATION_BRIEF.md`: pre-normalization authoring/execution basis SHA-256 `b8163531fb8f41142d6c067111fa84d2065ebd28c47f1c1e32e9218c16e6a218`; whitespace-normalized published basis SHA-256 `617512278aa93e05a07334b5f666e7a7e1f2e869882c33da6fd63b6fcdc92e9d`. The two forms are semantically identical; the former identifies the bytes sealed at dispatch and the latter identifies the current publication bytes.
- Signed transcript SHA-256 `6396dd26c3fb8b6ed922c1cb7da584f67a08188d5b27525d650bf3ca1560c566`.
- Signed TM112 block SHA-256 `a18f963d4666af73dd44674ea2d43f5052dc7eb96ddfe977f7a84070927f3a53`.
- Accepted clause SHA-256 `fd3ba31a8c53719e165b131d872868a53760adab4dc7ae92015fbd6641a11ead`.
- Frozen source hashes listed in the sealed implementation brief.

The acceptance validator and every frozen source hash passed before dispatch. Root has no project-local `software-workflow.json`; the sealed brief directly authorizes the existing daemon suite, bounded matrix, runtime typecheck/build, and Node-floor/current-Node compatibility checks. No registered profile is inferred.

## Work graph

1. `I1-IMPLEMENTER` — ephemeral Agent 2; integration owner for the three product files; implements the exact accepted shutdown contract and tests, runs authorized checks, and emits a durable return.
2. `I2-FRESH-REFUTER` — fresh ephemeral Agent 2; dependency `I1 accepted`; read-only over product outputs; executes independent code/contract/test refutation and bounded checks; writes only its instance evidence.
3. `I3-BOUNDED-REMEDIATION` — conditional fresh ephemeral Agent 2; released only for bounded I2 findings within the original three product files and run evidence; otherwise scope-change escalation.
4. `I4-BACKCHECK` — fresh read-only ephemeral Agent 2 if I3 runs; validates final candidate.
5. Manager fan-in — validates hashes, commands, scope containment, findings, gaps, derivative status, and terminal handoff; routes candidate to HELP_HUMAN without lifecycle or Git effects.

All overlapping product writes are serialized through I1 or conditional I3. The refuter is evidence-only. Agent 2 children may not delegate.

## Write boundary

Only:

- `docs/SPEC.md` section 14.1;
- `runtime/packages/daemon/src/runtime-daemon.ts`;
- bounded cases in `runtime/tests/daemon.test.ts`;
- `execution/_Coordination/AgentRuns/ROOT_TM112_IMPLEMENT_2026-08-03/**`.

No register, receipt, App/Piping/DEL, other canonical document, lifecycle, or Git write is authorized. The App notice remains held for later human acceptance of the repair.

## Fan-in gates

- Exact G2+C1+F1 behavior fits the authorized three product files.
- Existing daemon tests, all bounded new cases, runtime typecheck/build pass, or a precise unexecuted compatibility gap is returned.
- Fresh refutation has no unresolved material finding.
- No App/process/SIGTERM causal claim, public timing override, or scope expansion.
- Final hashes, commands/results, platform/Node identities, refutation verdict, residual gaps, and handoff are durable.
