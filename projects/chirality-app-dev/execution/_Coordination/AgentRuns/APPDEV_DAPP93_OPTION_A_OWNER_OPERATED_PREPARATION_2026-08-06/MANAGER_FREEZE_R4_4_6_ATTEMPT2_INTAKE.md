# Manager freeze — D-APP-93 R4.4.6 attempt-2 evidence intake

Status: `IMMUTABLE DERIVATIVE INTAKE — SOLE FRESH VERIFIER GATE`

Accepted prepared-state anchors:

- R4.4.6 preparation freeze: `13566daa015b49fe1d88d4048bd0d961a29c19bfb653921a6a22a524033f5f89`;
- R4.4.6 preparation fresh-verifier PASS: `25a506b96c0733bd4312450e5d245d6e8fb594ef1ba4700edf64da02800d7748`;
- cleanup-observation addendum freeze: `8ed898eab6199989538f7c8b011d3f2a522edfe5be8c0314ca68a9ac1a8b7fdf`;
- cleanup-observation addendum fresh-verifier PASS: `27dc2a89356597ea4e5f5fea8f6e6148094050c3e4e6db788bf7d3441087bc3f`.

Frozen intake objects:

| Object | SHA-256 |
|---|---|
| `R4_4_6_ATTEMPT2_INTAKE_DERIVATIVE.md` | `0ae89ce53e2ceae5aada01de6c2d44eafa1837b463b517434f6bc746e59819d3` |
| `R4_4_6_ATTEMPT2_INTAKE_VERDICT.md` | `d0c307352b804afd5f4e5eae1f3dd1fc111b0551c8ac7460c1c259f36d10e3c9` |

Source and derivative identity:

- retained source: `returned_r4_4_6/`;
- immutable derivative copy: `intake_r4_4_6_attempt2/`;
- source count: 40 objects; derivative count: 40 objects;
- classification: 20 primaries plus 20 true adjacent SHA-256 sidecars;
- total bytes in either set: 271661;
- canonical sorted `basename<TAB>bytes<TAB>sha256` set digest for either set: `53f33425ec1353bd4aafd8c41aa3c3a079847a2616c29ec76ad67ae1cf8e2e63`;
- whole-tree byte comparison: exact;
- all 20 adjacent sidecars reproduce.

Frozen interpretation boundary:

- terminal verdict is `STOP_INCOMPLETE`, not `PASS_COMPLETE`;
- step 14 remains recorded raw exit 1;
- step 15 remains `DEVIATION` despite raw exit 0;
- step 27 remains recorded raw exit 1;
- cleanup-addendum exact-PID evidence and preservation ordering are evidence, not a rewrite of the recorded step forms;
- C196, C197, C1121, and steps 16–22 remain not run;
- the SHA-256 `720ad198b99c45737564ed596147ca438e60586b5b5241cd6852a49838f245f8` LLDB script remains preserved and unused;
- no causal completion, reliance, repair, or reinterpretation is introduced.

The retained source is not moved, deleted, overwritten, or authoritative-state
substituted by this derivative intake. Any byte change to a frozen object above
invalidates this freeze. Exactly one genuinely fresh read-only verifier may
write the return named in the sealed brief; no other action is authorized.
