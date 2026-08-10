# D-APP-93 R4.4.6 attempt-2 intake fresh-verifier return

Verdict: `BLOCK_DAPP93_R4_4_6_ATTEMPT2_INTAKE`

Instance statement: I was a genuinely fresh read-only Agent 2 verifier for
this sealed gate. I did not delegate, repair, execute or simulate the packet,
inspect live processes or runtime state, move/delete/overwrite evidence, use
Git, or broaden scope. This file is my sole write.

## Smallest exact blocker

Required check 3 cannot pass. The sealed brief requires accounting for the
primary named `c1103-driver-archive.sha256.txt` and its double-suffix adjacent
sidecar. Neither frozen tree contains that basename or its sidecar. Both trees
instead contain:

- primary `c1103.sha256.txt`, 182 bytes, SHA-256
  `df35907b158b459d0ad7ca2a1ba4d1fa6592955e35bcecc7ce7ff8522898a95f`;
- adjacent sidecar `c1103.sha256.txt.sha256.txt`, 221 bytes, SHA-256
  `08bb1dc3b9a24c5a7f701e61c52f9b4bdb2b2a327112ae8e45396cadaf630dec`.

The intake derivative itself identifies `c1103.sha256.txt` as the twentieth
primary. Thus the bytes do support exactly 20 primaries plus 20 true adjacent
sidecars, but they do not support the exact required basename in the sealed
brief. I did not reinterpret, rename, or repair this mismatch.

## Independent audit results

- The sealed brief reproduced at
  `1ab2d0536148ffa1f337003c76de854240957ae5778e530cd4419b06e0270f9f`.
- `returned_r4_4_6/` and `intake_r4_4_6_attempt2/` each contain exactly 40
  regular files and 271661 bytes. Whole-tree byte comparison is empty.
- Adjacency-based classification independently produces exactly 20 primaries
  and 20 true adjacent sidecars in each tree; all 20 sidecars reproduce in
  each tree. The initial and final canonical sorted
  `basename<TAB>bytes<TAB>sha256` digest is
  `53f33425ec1353bd4aafd8c41aa3c3a079847a2616c29ec76ad67ae1cf8e2e63`
  for each tree.
- C1105, C1106, C1107, and C1108 each record exactly one
  `command_exit=0` and one `tee_exit=0` per tree: exactly twice each across
  the source and derivative.
- Raw CONTROL markers occur exactly once for steps 01-15, 23, and 25-30.
  Step 14 remains raw exit 1; step 15 remains raw exit 0 while the form remains
  `DEVIATION`; step 27 remains raw exit 1. No marker exists for steps 16-22 or
  24.
- C196, C197, and C1121 were not run. The LLDB script remains retained and
  unused at SHA-256
  `720ad198b99c45737564ed596147ca438e60586b5b5241cd6852a49838f245f8`.
- The evidence preserves exact-PID observations for GUI PID 93012 and helper
  PID 92988; GUI TERM, applicable helper KILL, the zero-row GUI fallback test,
  rollback/restoration and empty frontend-status evidence, temporary-root
  removal/absence proof, the ordered C1146 markers, and the terminal cut at
  C1146.30. The through-cut transcript ends at the step-30 marker/prompt and
  contains no post-cut CONTROL input. No recorded step form was reinterpreted.
- The retained source directory remains present. The evidence, without any
  live-state inspection by this verifier, represents the attempt temporary
  root as removed and proved absent after cleanup and rollback.
- The derivative and verdict remain bounded to `STOP_INCOMPLETE`, introduce
  no repair or reliance claim, and leave the unavailable runtime causal
  propositions unresolved. The intake implies no new operational execution,
  source mutation, move, deletion, overwrite, or repair.

Checks 1, 2, and 4-11 otherwise reproduce. Check 3 alone blocks the terminal
PASS.

## Bound identities and final stability

Initial and final identities were identical:

| Object | SHA-256 |
|---|---|
| R4.4.6 preparation freeze | `13566daa015b49fe1d88d4048bd0d961a29c19bfb653921a6a22a524033f5f89` |
| R4.4.6 preparation verifier PASS | `25a506b96c0733bd4312450e5d245d6e8fb594ef1ba4700edf64da02800d7748` |
| cleanup-observation addendum freeze | `8ed898eab6199989538f7c8b011d3f2a522edfe5be8c0314ca68a9ac1a8b7fdf` |
| cleanup-observation addendum verifier PASS | `27dc2a89356597ea4e5f5fea8f6e6148094050c3e4e6db788bf7d3441087bc3f` |
| attempt-2 intake manager freeze | `a7e4d9931ef5cd17a6ef7e1ee25a6d75340652584d7748861417f6803b287884` |
| intake derivative | `0ae89ce53e2ceae5aada01de6c2d44eafa1837b463b517434f6bc746e59819d3` |
| intake verdict | `d0c307352b804afd5f4e5eae1f3dd1fc111b0551c8ac7460c1c259f36d10e3c9` |
| retained source canonical set | `53f33425ec1353bd4aafd8c41aa3c3a079847a2616c29ec76ad67ae1cf8e2e63` |
| intake derivative canonical set | `53f33425ec1353bd4aafd8c41aa3c3a079847a2616c29ec76ad67ae1cf8e2e63` |

The preparation-freeze objects also reproduced unchanged: manifest
`c69aa2347e019c45348990c3a04cf583db1bbcdcad34d99fda345e32e839175a`,
overlay `5ae3d79bdb711153c315920ac4f4d584f6bab2d8d9d17fa2f08c31ed9242c7b7`,
LLDB script `720ad198b99c45737564ed596147ca438e60586b5b5241cd6852a49838f245f8`,
LLDB review `46ad16927a5235b59865e6821b53bb0956937584d8c86738a8b4b7bea2211459`,
ledger `1630f2c569f8aad3a91109ff70e5ca4cac597b619e47dbdd35b282dd94474824`,
runbook `9fda14d73d3eca1a0b055ea727853ecec11e824d8cc17fd57161a4ab9f2193d8`,
form `ad2ab87b910a3e028686e3ad28d275f608e70c37db173b9251f2354d6c82e6b3`,
ingestion contract
`283cf88f76c2803a7364bf8c94302501db0b0f09e5ead7bdff1469e51715d2bd`,
withheld token
`b3f917f7c1b0fe7d4a1a99a00e5371a86fb049ff7417d63acc009e7ca2023b4b`,
packet index `1aeeb7f1490f79abe1ef679a11317fed748f4a3a4cbca79d9b7ba898d1706959`,
rebind adoption
`4a824367f52148bdfe9fc0d9034abd0cd545bda7cf842e3aef42f11f78a56c9d`,
work graph `52e59634a42657392ebc260ff4b64e8dcd0f57034bded3f7fccdb7ab5949fcfb`,
rebind backcheck
`99192bb3820f0f9322a52e953c6da55f72fc2ae9cc86745003e2ce4d6c088531`,
inventory `ce44b47f1404b24af67ef474ea1e574d5ef543221ec7536f133047df66553e29`,
and matrices `32a0d9fc9caf4ba5994a181c05e9b4dc2b1c4c95b541ea8da338a074ca5b97db`.

The addendum-bound objects also reproduced unchanged: authority adoption
`f2f441ae79fc8fe7646a61e77d24f9aa889af0796eba30aac8e385b237e548da`,
cleanup addendum
`d109cfdc489f5ce679a696d8def4a599f90d8700c63891991778f6c605da7e33`,
execution token
`8e6dff6b587b37cfbab4b23f1e29ecbe01bb7c301b432c796cfa3cec80118fc8`,
backcheck `5558604c069afd42c6b4ad0f58cae9404a0366620de3d07be049c6ee42bc4986`,
and owner execution adoption
`119979f7b8f730ea382de021de0193e8168b1fbb2a36f7d8aadec5528811963e`.

Final stability: `PASS — NO FROZEN-OBJECT DRIFT`.

Terminal result: `BLOCK_DAPP93_R4_4_6_ATTEMPT2_INTAKE`.
