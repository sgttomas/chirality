# Evidence: D-APP-52 Live-LLM pec Demonstration (2026-07-18)

## Basis

D-APP-52 ruling O-A riders 1–11. The demonstration explicitly deferred in the
D-APP-52 packet ("live-LLM demonstration through a harness model session")
was executed as the owner's in-session act on 2026-07-18: owner at screen,
short-lived owner-supplied key, never persisted. Code SHA at capture
`a91f72b19aeb6dbca7e565fe336c91ce7e841421`; model `claude-sonnet-5`
(PACK2 script `frontend/scripts/run-dapp52-live-llm-demo.ts`, new; status
pass; redaction pass).

Artifact: `Evidence_DAPP52_LIVE_LLM_DEMO_2026-07-18_summary.json`
(byte-verbatim copy of the session capture), SHA-256
`9286ad2bbc0bf3bc9c62c6a9b09dc089b217b7e449c7c166f9b4ea660bccd82f`. All
facts below are traceable to that artifact by this SHA-256.

## Actors

- **Owner (human):** at screen; supplied the short-lived key; performed no
  pec accept/screen/apply act.
- **Harness model session (claude-sonnet-5):** a live model session itself
  called the Chirality MCP domain tools through the in-process Chirality MCP
  server.
- **Transport target:** a D-PEC-06-guarded scratch pec server on
  `127.0.0.1:4909` (projectId 2, synthetic CSV only); agent credentials
  runtime-generated, local-env only, secret-scanned absent from artifacts.

## Model-driven acts (stream order, message indexes from the JSON artifact)

| Msg index | Act | Observation |
|---:|---|---|
| 0 | `system/init` | session start; MCP server `chirality` connected |
| 2 | `ToolSearch` (tool_use) | model loads the two deferred domain tools |
| 4 | `mcp__chirality__domain_propose_operation` (mode propose) | proposalId 1 (ref IPR-0001) created; engine.version 2 |
| 7 | `mcp__chirality__domain_proposal_validate` (first) | envelope returned, version 2 |
| 9 | `mcp__chirality__domain_propose_operation` (mode "refresh") | proposalId 1, expectedVersion 2; engine.version 4 after refresh |
| 12 | `mcp__chirality__domain_proposal_validate` (second) | envelope returned, version 4 |
| 15 | `result/success` | terminal `is_error:false` |

Envelope keys observed: `{engine, inputs, mode, ok, profileId,
resultSemantics, toolId, transportStatus}`. `resultSemantics` verbatim:
"transport/evidence envelope only; no domain verdict; a green dry-run is NOT
acceptance — acceptance and application are human acts in pec behind
admin-only RBAC (K-DOMAIN-3/K-DOMAIN-4)".

## Demo-cast acts

NONE occurred. No accept, screen act, or apply happened in this
demonstration; `force` was never used in any form.

## Teardown

Scratch server stopped and its DB (+wal/shm) deleted after capture; agent
credentials were runtime-generated, local-env only, and secret-scanned absent
from the artifacts.

## Deferred-statement discharge

This run discharges exactly the act the D-APP-52 packet deferred ("live-LLM
demonstration through a harness model session"). No further claim is made.

## Boundaries respected

Riders 2/3/5/8/9 and F-APP-3 respected. The evidence home is this
deliverable folder per the D-APP-64 selection recorded in DEL-04-01
`_run_records/TASK_RUN_2026-07-18_DAPP52_live_demonstration_closures.md`;
`_DomainEngines/**` untouched (the pec loop may mirror under its own
authority).
