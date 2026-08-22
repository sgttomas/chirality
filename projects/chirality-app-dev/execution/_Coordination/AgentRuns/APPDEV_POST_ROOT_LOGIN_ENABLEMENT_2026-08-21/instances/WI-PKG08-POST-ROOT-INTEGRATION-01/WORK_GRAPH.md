# Work Graph v1 — PKG-08 / DEL-08-04

Status: `FROZEN BEFORE AGENT 2 DISPATCH`

Posture: `TERMINAL_FAN_OUT_IN`, serialized execution and fresh review.

| Node | Agent | Depends on | Write owner | Required return / gate |
|---|---|---|---|---|
| `A2-PKG08-INTEGRATION-EXECUTE-01` | ephemeral generalist Agent 2 | accepted basis | its unique child instance only | exact commands, exit results, admission/fail-closed matrix, basis hashes, scope result |
| `A2-PKG08-INTEGRATION-REVIEW-01` | fresh ephemeral generalist Agent 2 | frozen executor return and manager candidate | its unique child instance only | 100% review; `PASS` with zero actionable findings or enumerated `BLOCK` |
| `WI-FAN-IN` | WORKING_ITEMS | accepted executor and reviewer | DEL-08-04 status/memory/run record plus manager instance | evidence completeness, write containment, D-APP-103 preservation, notice acknowledgment, derivative disposition |

No implementation or repair node is selected unless the executor or reviewer
finds a concrete App-local defect. Any repair would be separately briefed and
followed by a fresh reviewer, with no more than two repair/review cycles.

Token/context occupancy is not exposed by this runtime and is recorded as an
explicit telemetry measurement limitation rather than inferred.

