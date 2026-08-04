# Runtime summary

RunID: `ROOT_TM112_IMPLEMENT_2026-08-03`
Status: `TERMINAL / COMPLETE PAIRS RECORDED`

| Node | Attempt | Terminal disposition | Evidence |
|---|---:|---|---|
| I1 implementer | 1 | interrupted pre-write after no patch/status return | `instances/I1-IMPLEMENTER/ATTEMPT_DISPOSITION.md` |
| I1B implementer | 2 | interrupted post-validation; manager recovered frozen product/evidence | `instances/I1B-IMPLEMENTER/MANAGER_RECOVERED_RETURN.md` |
| I2 fresh refuter | 1 | interrupted post-evidence; manager recovered two reproduced material findings | `instances/I2-FRESH-REFUTER/MANAGER_RECOVERED_REFUTATION.md` |
| I3 remediation | 1 | PASS; exact two defects repaired | `instances/I3-BOUNDED-REMEDIATION/RETURN.md` |
| I4 fresh backcheck | 1 | PASS_WITH_NONBLOCKING_FINDINGS | `instances/I4-FRESH-BACKCHECK/RETURN.md` |

Reason codes: `AGENT_RETURN_TIMEOUT_PREWRITE`,
`AGENT_RETURN_TIMEOUT_POSTVALIDATION`,
`AGENT_RETURN_TIMEOUT_POSTEVIDENCE`, `BOUNDED_MATERIAL_REMEDIATION`, and
`FRESH_FINAL_BACKCHECK_PASS`.

The collaboration runtime did not expose token/context occupancy per child, so
that measurement remains explicitly unavailable. Session start/finish timing
was not emitted as machine-readable telemetry; durable launch briefs, attempt
dispositions, check durations, messages, terminal returns, and final hashes are
the available derivative runtime evidence. This limitation does not alter
authority or product acceptance.
