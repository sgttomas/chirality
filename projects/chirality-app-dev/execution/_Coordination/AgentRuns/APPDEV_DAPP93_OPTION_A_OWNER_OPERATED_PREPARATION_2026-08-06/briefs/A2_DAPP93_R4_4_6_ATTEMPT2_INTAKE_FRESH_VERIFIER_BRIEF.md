# Sealed brief — fresh read-only verifier for R4.4.6 attempt-2 intake

Role: genuinely fresh Agent 2 read-only verifier.

Read scope is limited to this D-APP-93 run directory, especially:

- `returned_r4_4_6/`;
- `intake_r4_4_6_attempt2/`;
- `R4_4_6_ATTEMPT2_INTAKE_DERIVATIVE.md`;
- `R4_4_6_ATTEMPT2_INTAKE_VERDICT.md`;
- `MANAGER_FREEZE_R4_4_6_ATTEMPT2_INTAKE.md`;
- the accepted R4.4.6 prepared/freeze/verifier/addendum objects cited by the freeze.

Sole write target:
`reviews/A2_DAPP93_R4_4_6_ATTEMPT2_INTAKE_FRESH_VERIFIER_RETURN.md`.

Perform an independent byte-level audit and return exactly one terminal verdict:
`PASS_DAPP93_R4_4_6_ATTEMPT2_INTAKE` or
`BLOCK_DAPP93_R4_4_6_ATTEMPT2_INTAKE`.

Required checks:

1. Initial and final SHA-256 stability of the freeze and every object it binds.
2. `returned_r4_4_6/` and `intake_r4_4_6_attempt2/` each contain exactly 40 regular files and are byte-exact whole-tree matches.
3. Classify exactly 20 primaries and 20 true adjacent sidecars; account correctly for the primary named `c1103-driver-archive.sha256.txt` and its double-suffix adjacent sidecar.
4. Reproduce all 20 adjacent sidecars and the canonical set digest `53f33425ec1353bd4aafd8c41aa3c3a079847a2616c29ec76ad67ae1cf8e2e63`.
5. Confirm C1105–C1108 each record `command_exit=0` and `tee_exit=0` exactly twice.
6. Confirm step records are exactly 01–15, 23, and 25–30, with step 14 raw exit 1 unchanged, step 15 form `DEVIATION` unchanged despite raw exit 0, and step 27 raw exit 1 unchanged.
7. Confirm steps 16–22 are not run and C196/C197/C1121 are absent from execution evidence; confirm the SHA-720AD198 LLDB script is retained and unused.
8. Confirm the cleanup-addendum evidence preserves the exact-PID cleanup branch, rollback evidence, source-retention disposition, C1146 marker sequence, terminal cut at C1146.30, and absence of post-cut CONTROL input without reinterpreting any step form.
9. Confirm source `returned_r4_4_6/` remains retained and the attempt temp root disposition is represented exactly by the evidence.
10. Confirm the derivative and verdict truthfully conclude `STOP_INCOMPLETE`, make no repair/reliance claim, and leave runtime causal propositions unresolved except where the raw evidence directly supports a bounded proposition.
11. Confirm no operational execution, source mutation, move, deletion, overwrite, repair, or scope expansion is implied by the intake.

If any check fails, return BLOCK with the smallest exact blocker. Do not repair,
rewrite, execute, inspect live processes, dispatch another agent, or write any
file other than the sole return. Include exact hashes and a final stability
check in the durable return.
