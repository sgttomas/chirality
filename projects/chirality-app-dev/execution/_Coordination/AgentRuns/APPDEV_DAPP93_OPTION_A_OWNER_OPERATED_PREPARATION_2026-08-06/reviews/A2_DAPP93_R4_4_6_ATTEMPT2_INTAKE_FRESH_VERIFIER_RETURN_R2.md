# D-APP-93 R4.4.6 attempt-2 intake fresh-verifier return R2

Verdict: `PASS_DAPP93_R4_4_6_ATTEMPT2_INTAKE_R2`

Instance statement: I was the one genuinely fresh read-only Agent 2 verifier
released for this R2 gate. I did not delegate, repair, execute or simulate the
packet, inspect live processes or runtime state, move/delete/overwrite source
evidence, mutate any candidate, use Git, or broaden scope. This file is my sole
write.

## Sealed scope and frozen identities

The R2 sealed brief reproduced at SHA-256
`e2bb6ac1c05034a685a4aa64af2a81faaff75907364c03f6c695bd0282141639`.
The rejected predecessor brief and its BLOCK return reproduced respectively at
`1ab2d0536148ffa1f337003c76de854240957ae5778e530cd4419b06e0270f9f` and
`252d5e6523c70651693d1836f52b3f0f425daadf267daec269666741263215a7`.

Initial and final pre-return identities were identical:

| Object | Initial SHA-256 | Final SHA-256 |
|---|---|---|
| attempt-2 intake derivative | `0ae89ce53e2ceae5aada01de6c2d44eafa1837b463b517434f6bc746e59819d3` | `0ae89ce53e2ceae5aada01de6c2d44eafa1837b463b517434f6bc746e59819d3` |
| attempt-2 intake verdict | `d0c307352b804afd5f4e5eae1f3dd1fc111b0551c8ac7460c1c259f36d10e3c9` | `d0c307352b804afd5f4e5eae1f3dd1fc111b0551c8ac7460c1c259f36d10e3c9` |
| attempt-2 intake manager freeze | `a7e4d9931ef5cd17a6ef7e1ee25a6d75340652584d7748861417f6803b287884` | `a7e4d9931ef5cd17a6ef7e1ee25a6d75340652584d7748861417f6803b287884` |
| R4.4.6 preparation freeze | `13566daa015b49fe1d88d4048bd0d961a29c19bfb653921a6a22a524033f5f89` | `13566daa015b49fe1d88d4048bd0d961a29c19bfb653921a6a22a524033f5f89` |
| R4.4.6 preparation verifier PASS | `25a506b96c0733bd4312450e5d245d6e8fb594ef1ba4700edf64da02800d7748` | `25a506b96c0733bd4312450e5d245d6e8fb594ef1ba4700edf64da02800d7748` |
| cleanup-addendum freeze | `8ed898eab6199989538f7c8b011d3f2a522edfe5be8c0314ca68a9ac1a8b7fdf` | `8ed898eab6199989538f7c8b011d3f2a522edfe5be8c0314ca68a9ac1a8b7fdf` |
| cleanup-addendum verifier PASS | `27dc2a89356597ea4e5f5fea8f6e6148094050c3e4e6db788bf7d3441087bc3f` | `27dc2a89356597ea4e5f5fea8f6e6148094050c3e4e6db788bf7d3441087bc3f` |

The preparation-freeze objects also reproduced unchanged: manifest
`c69aa2347e019c45348990c3a04cf583db1bbcdcad34d99fda345e32e839175a`,
overlay `5ae3d79bdb711153c315920ac4f4d584f6bab2d8d9d17fa2f08c31ed9242c7b7`,
LLDB script `720ad198b99c45737564ed596147ca438e60586b5b5241cd6852a49838f245f8`,
LLDB static review `46ad16927a5235b59865e6821b53bb0956937584d8c86738a8b4b7bea2211459`,
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
All 27 directly and transitively checked frozen objects had zero final hash
mismatches.

## Independent byte-level audit

- `returned_r4_4_6/` and `intake_r4_4_6_attempt2/` each contain exactly 40
  regular files, 40 total immediate entries, and 271661 bytes. Whole-tree
  comparison is empty.
- Adjacency-based classification produces exactly 20 primaries and 20 true
  adjacent sidecars in each tree. All 20 sidecars reproduce their adjacent
  primary in each tree; mismatch count is zero.
- Both trees independently reproduce the canonical sorted
  `basename<TAB>bytes<TAB>sha256` digest
  `53f33425ec1353bd4aafd8c41aa3c3a079847a2616c29ec76ad67ae1cf8e2e63`
  initially and finally.
- The exact frozen-ledger primary is `c1103.sha256.txt`, SHA-256
  `df35907b158b459d0ad7ca2a1ba4d1fa6592955e35bcecc7ce7ff8522898a95f`,
  and its exact adjacent sidecar is `c1103.sha256.txt.sha256.txt`, SHA-256
  `08bb1dc3b9a24c5a7f701e61c52f9b4bdb2b2a327112ae8e45396cadaf630dec`,
  in both trees. `c1103-driver-archive.sha256.txt` is absent and is correctly
  neither expected nor required.
- C1105, C1106, C1107, and C1108 each contain exactly one
  `command_exit=0` and one `tee_exit=0` per tree, hence exactly twice each
  across the retained source and derivative.

## Recorded branch, cleanup, and interpretation boundary

The emitted CONTROL step records occur once each and in exact order:
`01-15, 23, 25-30` (22 records). Step 14 remains raw exit 1; step 15 remains
raw exit 0 while the frozen form records `DEVIATION`; step 27 remains raw exit
1. Steps 16-22 and 24 have no raw marker and remain `NOT_RUN`. C196, C197, and
C1121 were not executed; no LLDB/trace operation appears in the raw transcript,
and the SHA-720AD198 script remains retained and unused.

The cleanup evidence preserves the addendum's exact-PID branch without
reinterpreting any form state: A1117.ID and A1128.PRE match GUI PID 93012 and
PPID 90439 before GUI C1128 TERM; A1129.H matches helper PID 92988 and PPID
90439 before helper C1129 KILL; A1129.G returns zero rows after the GUI exits,
so GUI fallback KILL is not applicable. The raw rollback sequence restores the
seven baselines, retains the lock identity, removes five additions and build
derivatives, reproduces all eight baseline/lock hashes, and records empty
frontend-status bytes.

The retained source directory remains present and unchanged. The evidence—not
any live inspection by this verifier—records removal of the fixed attempt root
followed by a successful absence proof. `control-transcript.txt`, SHA-256
`ff78e462c81563c97ada775c590412ca9cc27e4ea474e68aea353873c323690a`,
ends at the C1146.30 output and terminal prompt with no later CONTROL input;
the pre-cleanup preservation copy remains SHA-256
`982ae86e49a5f5ebe611dca0c6f789f34c785fbcc39ef2a2d237d9c72b60988e`.
The post-cut form remains SHA-256
`033002556ca64c1dbe531ccbd5f3c425494f22cbdf8f7941cb583b9943cb5e98`.

The derivative and verdict truthfully conclude `STOP_INCOMPLETE`, not
`PASS_COMPLETE`. They introduce no repair, reliance, release, or causal
completion claim. Native signal delivery, libuv/SignalWrap/Electron shutdown,
Root-stop causation, and post-signal transport/socket propositions remain
unresolved; only bounded package/runtime identity, exact raw observations,
preservation, cleanup, and rollback propositions are supported. The intake
implies no new operational execution, source mutation, move, deletion,
overwrite, repair, or scope expansion.

## R2 correction and final stability

Direct comparison to the rejected brief confirms that the only material
acceptance-semantic change is correction of its false C1103 filename
expectation to the exact frozen primary/sidecar names and hashes above. The
remaining R2 differences are provenance, explicit unchanged-object hash pins,
R2 output identifiers, and the check that records this correction; they do not
alter candidate or returned-evidence bytes. The three candidate hashes remain
exactly unchanged.

Final stability: `PASS — NO FROZEN-OBJECT OR TREE DRIFT`.

Sole-write attestation: only
`reviews/A2_DAPP93_R4_4_6_ATTEMPT2_INTAKE_FRESH_VERIFIER_RETURN_R2.md` was
written. Its whole-file SHA-256 is computed after this write and reported in
the dispatch return; embedding it here would change the hashed file.
