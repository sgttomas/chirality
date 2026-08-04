# Degraded-mode contract composite candidate V2

- Status: `DERIVATIVE_SEMANTIC_CANDIDATE_NOT_ACCEPTED`
- Accepted base candidate: `accepted_inputs/DEGRADED_MODE_CONTRACT_CANDIDATE.md` @ `2a54da97a8c0931a430fc64321fcde41dfcb754f67f4da36c3792ef457a5c917`
- Upstream delta candidate: `9fc965ac4b07532adf8890c97a2197e65db305fe9170c47d49aeb3d0caabe16b`

## Composite rule

This candidate preserves the accepted base by exact hash and adds the recovery
delta below. Later adoption must bind and reproduce the base bytes plus this
complete ten-condition delta; a base-hash mismatch returns rather than being
treated as equivalent. Nothing here adopts either component or changes
runtime behavior.

## Recovery readiness and retained functions

While the daemon is `RECOVERY_REQUIRED`, `RECOVERY_SCANNING`, or
`RECOVERY_BLOCKED`, these non-mutating surfaces may remain available only when
their no-write property and truthful output are proven:

- health and daemon status, explicitly reporting the exact recovery state;
- byte-stable session/event replay that exposes malformed or partial truth and
  performs no repair; and
- project/session list and get diagnostics with no migration, registration,
  status repair, or other mutation.

Every consequential or mutating route and direct service entry is blocked,
including turn and governed Agent 1 run, session boot, model activation and
local admission, registration, session create/delete, credential mutation,
scaffold, permissions mutation, tool execution, and replay-induced mutation.
File-native governance remains separately owned and is not an alternate agent
runtime. App retained functions and presentation remain App-owned. PEC remains
unresolved.

## Ten-condition identifiers and envelopes

Every failure uses the common safe envelope fields `code`, `operation_id`,
`project_id`, `boundary`, `retryable`, `consequential_work_started`,
`evidence_ref`, and `diagnostic`. The exact distinct identifiers are:

| Precedence | Condition | Exact `code` | Required fail-closed behavior | Recovery boundary |
|---:|---|---|---|---|
| 1 | client configuration / project access | `CLIENT_CONFIGURATION_OR_PROJECT_ACCESS_INVALID` | stop before transport; preserve client/project ownership | owner repairs exact configuration/access, then rerun all gates |
| 2 | runtime credential readiness | `RUNTIME_CREDENTIAL_NOT_READY` | reject without credential transfer or client-side repair | authorized daemon credential repair, then rerun all gates |
| 3 | registration | `PROJECT_REGISTRATION_INVALID` | stop project runtime work; no implicit registration | separately authorized registration, then rerun all gates |
| 4 | authorization | `PROJECT_OPERATION_UNAUTHORIZED` | reject exact operation; never broaden scopes | owning authority corrects exact grant, then rerun all gates |
| 5 | project adapter | `PROJECT_ADAPTER_UNAVAILABLE` | block only adapter-dependent operation; no generic substitution | project-owned adapter gate, then rerun all gates |
| 6 | Unix-socket transport | `RUNTIME_TRANSPORT_UNAVAILABLE` | no TCP, in-process, alternate daemon, or alternate runtime | authorized reconnect/rebind, then rerun all gates without resend |
| 7 | compatibility mismatch | `RUNTIME_COMPATIBILITY_MISMATCH` | reject before consequential work; no range/downgrade inference | bind an exact accepted equal pair, then rerun all gates |
| 8 | wire / protocol validity | `RUNTIME_PROTOCOL_INVALID` | preserve exact malformed/protocol truth; never recast as transport | accept corrected exact contract/evidence, then rerun without replay |
| 9 | provider / engine / model | `RUNTIME_EXECUTION_FAILED` | preserve actual execution-domain cause; no alternate model/provider | authorized repair or activation, then rerun without replay |
| 10 | daemon operational / recovery state | `RUNTIME_RECOVERY_REQUIRED` | block consequential paths and preserve terminal/drain truth | complete the accepted evidence-bearing recovery pass |

The order is deterministic. Evaluation stops the response at the first
blocking applicable condition, while the append-only redacted audit records
all safely observable evaluated conditions. A later failure cannot overwrite
an earlier blocker or be recast as another boundary.

## Precedence retry and evidence fields

All ten envelopes set `retryable` to `false` under the selected no-retry
policy. No retry delay or automatic resend exists. Reconnect, rebind, or
authorized repair starts a new precondition evaluation, not a retry of
indeterminate work.

The redacted audit for every evaluated condition contains stable run and
operation identities, condition code, boundary, compared safe identities,
source/contract basis hashes, before/after state, decision authority,
`consequential_work_started`, outcome, and evidence references. It excludes
secret values, credentials, authorization tokens, private payloads,
machine-specific absolute paths, and private adapter evidence. Missing
required evidence is itself a truthful fail-closed diagnostic.

## Recovery and presentation

Exit from degraded recovery posture requires the complete state-machine exit
criteria in `ROOT_RECOVERY_SEMANTIC_CANDIDATE_V2.md`. Root CLI and generic
client must preserve the exact machine code and envelope. App mapping and
conformance require a separate App-owned accepted tranche. No Piping work or
dependency exists; PEC is not classified by this contract.

## No-effect boundary

No identifier, response, route, direct entry, retry, redaction mechanism,
runtime/client/App/PEC/Piping/Tier-0 byte, check result, implementation,
lifecycle, release, reliance, or Git effect occurs here.
