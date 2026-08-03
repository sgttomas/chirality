# W6 N4 brief amendment 1 — disposition of N5-F01

- RequestedBy: `WORKING_ITEMS/W6-DEL0206-POST-N0-PLANNING`
- Runtime integration owner: `/root/w1_del0206/n4_w6`
- Predecessor launch SHA-256: `afa7d439917382fa0ff5aca3fefd06fd542d9f5bf2a5d4de4e475d01da78de7b`.
- Accepted N5 finding capture: `children/N5/SESSION_RETURN.md`, manager-authored capture SHA-256 `30c1178643ad4aa5405e2109df2ca461dc074b7c3e79e7a777228e1f812d169f`.
- Disposition: `REMEDIATE_WITHIN_EXISTING_N4_SCOPE_AND_RETURN_FOR_FRESH_N5_RECHECK`.

## Bounded objective

Address only `N5-F01` without selecting any semantic value: revise
`integration/DEGRADED_MODE_DELTA_CANDIDATE.md` into a complete ten-condition
candidate grounded in the already-declared accepted `ScopeOfWork.md`. Add a
one-to-one matrix covering client configuration/project access, runtime
credential readiness, registration, authorization, project adapter,
Unix-socket transport, compatibility mismatch, wire/protocol validity,
provider/engine/model, and daemon operational/recovery state. Each row must
state boundary, candidate required behavior, recovery, exact class or
unresolved item, retry posture, redaction/evidence, positive verification,
and negative/adversarial verification. Keep exact class/retry/redaction fields
unresolved where the owner has not ruled them.

Then update only `integration/N4_SELF_CHECK.md` and
`integration/N4_RETURN.md` so their hashes and completeness claims bind the
revised artifact. Preserve every other N4 output byte-identically.

## Authority and containment

- Reads: existing N4 declared reads and this manager-relayed finding only.
- Additional reads: none; do not read the accepted base candidate bytes.
- Writes: only the three existing N4-owned targets named above.
- No write-scope, authority, semantic, client, dependency, profile/check, or lifecycle expansion.
- Allowed tools: non-shell Node reads/hashes/parsing and `apply_patch` for the three exact targets only.
- No Bash, network, executable test/check, runtime execution, implementation, repair outside N4 outputs, delegation, Git, or foreign write.
- Return: exact pre/post hashes, ten-row validation, unchanged hashes for the other four N4 outputs, verdict `ADMIT_FOR_FRESH_N5_RECHECK` or `RETURN_TO_MANAGER`, and full tool/write statement.
