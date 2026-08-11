# Stage 5 — structural validation

Status: `PASS`

Ledger:
`STAGE_5_COMMAND_AUTHORITY_LEDGER.csv`, SHA-256
`dfdab5d0e760797b51d86dc0d0aa0345e46ab2af5a4e537d87a24bb5e319c809`.

| Check | Observed result |
|---|---|
| Header/schema | PASS — exact 13 columns: `command_id,phase,actor,exact_command,purpose,preconditions,authority_class,required_owner_approval,expected_outputs,success_gate,failure_route,cleanup_or_rollback,source_basis` |
| F04 field count | PASS — Stage 3, Stage 4, and Stage 5 each report 13 header fields |
| Row count | PASS — Stage 3 has 43 rows, Stage 4 has 37 rows, Stage 5 has 80 rows |
| Fan-in byte-field equality | PASS — Stage 3 rows followed by Stage 4 rows equal all Stage 5 parsed field bytes in order |
| Namespace | PASS — exactly contiguous `L3-CMD-001` through `L3-CMD-080` |
| Identity uniqueness | PASS — 80 unique IDs |
| Required fields | PASS — no empty field in any row |
| Allowed actors | PASS — only `owner-terminal`, `owner-gui`, and `owner-debugger-input` |
| Allowed authority classes | PASS — only `OWNER_OPERATED_NEW`, `OWNER_OPERATED_PRESERVED_FENCE`, and `OWNER_ATTESTATION` |
| Approval fence | PASS — every row is exactly `YES — exact frozen-packet hash approval` |
| Failure route | PASS — nonempty in all 80 rows |
| Cleanup/rollback disposition | PASS — nonempty in all 80 rows |
| Historical-ID criterion | PASS — Stage 2 full-pattern scan exited 1 with stdout 0 bytes |
| Live provenance | PASS — Stage 3 resolves 41/41 inventory identities; Stage 4 resolves 80/80 ledger rows |

Actual invocations: F03 once on the Stage 5 ledger header; F04 once on each of
the Stage 3, Stage 4, and Stage 5 CSVs; and one F06 isolated standard-library
CSV validation expression over those three explicit files. All exited `0`.
No repair or substitution was made. Native context telemetry: unavailable.
