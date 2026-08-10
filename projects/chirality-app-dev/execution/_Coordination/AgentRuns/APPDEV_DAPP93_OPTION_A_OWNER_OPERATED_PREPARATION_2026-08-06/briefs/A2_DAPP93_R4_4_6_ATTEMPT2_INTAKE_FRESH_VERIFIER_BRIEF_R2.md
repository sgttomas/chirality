# Sealed brief R2 — fresh read-only verifier for unchanged R4.4.6 attempt-2 intake

Role: genuinely fresh Agent 2 read-only verifier.

This is a filename-expectation-only successor to the rejected brief SHA-256
`1ab2d0536148ffa1f337003c76de854240957ae5778e530cd4419b06e0270f9f`.
The prior BLOCK return is SHA-256
`252d5e6523c70651693d1836f52b3f0f425daadf267daec269666741263215a7`.
No intake candidate or returned-evidence byte may change.

Read scope is limited to this D-APP-93 run directory, especially:

- `returned_r4_4_6/`;
- `intake_r4_4_6_attempt2/`;
- `R4_4_6_ATTEMPT2_INTAKE_DERIVATIVE.md` at SHA-256 `0ae89ce53e2ceae5aada01de6c2d44eafa1837b463b517434f6bc746e59819d3`;
- `R4_4_6_ATTEMPT2_INTAKE_VERDICT.md` at SHA-256 `d0c307352b804afd5f4e5eae1f3dd1fc111b0551c8ac7460c1c259f36d10e3c9`;
- `MANAGER_FREEZE_R4_4_6_ATTEMPT2_INTAKE.md` at SHA-256 `a7e4d9931ef5cd17a6ef7e1ee25a6d75340652584d7748861417f6803b287884`;
- the accepted R4.4.6 prepared/freeze/verifier/addendum objects cited by that freeze.

Sole write target:
`reviews/A2_DAPP93_R4_4_6_ATTEMPT2_INTAKE_FRESH_VERIFIER_RETURN_R2.md`.

Perform an independent byte-level audit and return exactly one terminal verdict:
`PASS_DAPP93_R4_4_6_ATTEMPT2_INTAKE_R2` or
`BLOCK_DAPP93_R4_4_6_ATTEMPT2_INTAKE_R2`.

Required checks:

1. Initial and final SHA-256 stability of the three unchanged candidate objects above and every object the manager freeze binds.
2. `returned_r4_4_6/` and `intake_r4_4_6_attempt2/` each contain exactly 40 regular files and are byte-exact whole-tree matches.
3. Classify exactly 20 primaries and 20 true adjacent sidecars. The frozen ledger's exact primary is `c1103.sha256.txt` at SHA-256 `df35907b158b459d0ad7ca2a1ba4d1fa6592955e35bcecc7ce7ff8522898a95f`; its exact adjacent sidecar is `c1103.sha256.txt.sha256.txt` at SHA-256 `08bb1dc3b9a24c5a7f701e61c52f9b4bdb2b2a327112ae8e45396cadaf630dec`. Confirm both names and hashes in both trees. Do not expect or require `c1103-driver-archive.sha256.txt`.
4. Reproduce all 20 adjacent sidecars and the canonical set digest `53f33425ec1353bd4aafd8c41aa3c3a079847a2616c29ec76ad67ae1cf8e2e63`.
5. Confirm C1105–C1108 each record `command_exit=0` and `tee_exit=0` exactly twice.
6. Confirm step records are exactly 01–15, 23, and 25–30, with step 14 raw exit 1 unchanged, step 15 form `DEVIATION` unchanged despite raw exit 0, and step 27 raw exit 1 unchanged.
7. Confirm steps 16–22 are not run and C196/C197/C1121 are absent from execution evidence; confirm the SHA-720AD198 LLDB script is retained and unused.
8. Confirm the cleanup-addendum evidence preserves the exact-PID cleanup branch, rollback evidence, source-retention disposition, C1146 marker sequence, terminal cut at C1146.30, and absence of post-cut CONTROL input without reinterpreting any step form.
9. Confirm source `returned_r4_4_6/` remains retained and the attempt temp-root disposition is represented exactly by the evidence.
10. Confirm the derivative and verdict truthfully conclude `STOP_INCOMPLETE`, make no repair/reliance claim, and leave runtime causal propositions unresolved except where raw evidence directly supports a bounded proposition.
11. Confirm no operational execution, source mutation, move, deletion, overwrite, repair, or scope expansion is implied by the intake.
12. Confirm the only semantic change from the rejected brief is correction of the C1103 primary/sidecar filename expectation described above; the unchanged candidate hashes remain exact.

If any check fails, return BLOCK with the smallest exact blocker. Do not repair,
rewrite, execute, inspect live processes, dispatch another agent, or write any
file other than the sole return. Include exact hashes and a final stability
check in the durable return.
