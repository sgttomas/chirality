# Attempt-2 intake / D-APP-94 successor fresh-verifier return R2

Verdict: `BLOCK`

Role performed: genuinely fresh, read-only ephemeral Agent 2 adversarial
verifier. No repair, delegation, runtime/process inspection, signal, package,
helper/GUI, keychain, credential, product, Git, Task Management, or foreign-loop
action was performed. This return is the sole write.

## Material blocker

The required sorted-all-40 aggregate did not reproduce under the exact stated
construction. Direct enumeration found exactly 40 regular files: 20 primaries
and 20 adjacent `.sha256.txt` sidecars (including `c1103.sha256.txt` as the
primary and `c1103.sha256.txt.sha256.txt` as its sidecar). All 20 sidecars
reproduced their paired primary. However, sorting the 40 basenames and emitting
one exact `name|byte_count|sha256\n` row per object, using each object's byte
count and whole-file SHA-256, produced:

`480f1817774d2c2a8bc74e7e584674341f9699a2f9e2a9f5132f75050a790cfb`

not the required/frozen:

`97a9d3836b1b3a7557f4171f208a7ac55c4132a87d1a8ab956dc2fdef58c8110`.

Because sealed brief R2 check 1 explicitly requires reproduction of
`97a9d383...110`, this discrepancy is independently sufficient for `BLOCK`.
The individual object counts, byte counts, hashes, and pairings agree with
`R4_4_6_ATTEMPT2_RETURNED_MANIFEST.md`; the blocker is specifically the stated
aggregate identity/construction.

## Other material checks

- The successor repair's two substantive corrections pass. The exact
  `2026-08-08T05:57:26.027Z` / `Unknown project: chirality-app-dev` signature
  is present in both immutable streams: `gui.stdout.txt:5` is the connectivity
  state record and `gui.stderr.txt:1` is the bind-failure record. The successor
  no longer claims otherwise and gives neither record fresh-C1118 or causal
  credit.
- The immutable completed form records predecessor R4.4.5 runbook SHA
  `6f82568113ad19033948d824d257f9af474b490083988c597882bf691df8e5ac`;
  direct hashing of the executed R4.4.6 runbook reproduces
  `9fda14d73d3eca1a0b055ea727853ecec11e824d8cc17fd57161a4ab9f2193d8`.
  The successor retains the unedited-byte mismatch as a deviation and does not
  claim `PASS_COMPLETE`.
- Direct binary parsing of the 80,266-byte transcript reproduced exactly 22
  ordered marker ranges/exits:
  `01 [0,264) 0; 02 [264,1137) 0; 03 [1137,1867) 0; 04 [1867,5182) 0;
  05 [5182,11707) 0; 06 [11707,14030) 0; 07 [14030,14853) 0;
  08 [14853,16289) 0; 09 [16289,23028) 0; 10 [23028,50335) 0;
  11 [50335,64537) 0; 12 [64537,65530) 0; 13 [65530,65973) 0;
  14 [65973,66675) 1; 15 [66675,67664) 0; 23 [67664,68635) 0;
  25 [68635,73872) 0; 26 [73872,74721) 0; 27 [74721,75397) 1;
  28 [75397,77785) 0; 29 [77785,79738) 0; 30 [79738,80156) 0`.
  The remaining `[80156,80266)` is prompt/newline only. Step 14 is correctly
  `FAIL`, step 15 `DEVIATION`, and the terminal verdict remains
  `STOP_INCOMPLETE — ENVIRONMENT DEPENDENCY AT C1118`.
- C1105-C1108 each have complete output, exact two-record exit files, and
  `command_exit=0` / `tee_exit=0`. C1108 records both packages using the same
  run-root Electron archive, dependency verification `PASS`, and
  `localPackageEntries: 0`. Helper PID 92988 and GUI PID 93012 are supported as
  direct children of CONTROL shell 90439 at launch only.
- Returned cleanup evidence preserves GUI `TERM`, helper `KILL`, and the
  step-27 zero-row exit-1 semantics. Current safe read-only hashes reproduce
  all eight C1140 values; C1141 has no output rows; the fixed temp root is
  absent; the returned form records candidate/build derivative absence; and
  LLDB/C196/C197 remain unused.
- All eight signal-path cells remain `UNKNOWN`. Package/direct-child identity
  is supported at launch only, without C1119, attach, or signal credit. No
  D-APP-88, DEL-09-04, TM-APP-036, product, remedy, release, or reliance
  conclusion follows.
- Exactly one register row begins `| D-APP-94 |`; it is `AWAITING_RULING`.
  The packet neutrally presents A/B/C, makes A conditional, grants only the
  exact preparation-only tokens, and requires both fresh C1118 and a separate
  step-14 packet/runbook repair gate before any future attempt.
- Read-only inspection of `electron/api-key-storage.ts`, `runtime-host.ts`,
  `main.ts`, and `api-key-storage.test.ts` confirms live safeStorage
  availability/encrypt/decrypt paths, startup/runtime credential consumers,
  fail-closed behavior when encryption is unavailable, and focused tests.
  A/B/C are plausible planning choices; no already-proven bypass is asserted.

## Final stability hashes

All initial identities reproduced unchanged immediately before this sole
write:

| Object | Final SHA-256 |
|---|---|
| sealed brief R2 | `2dbb9f1bfd23c543c8050573bc128879e0726ecb62f26c21977cc9c24ef6c639` |
| `R4_4_6_ATTEMPT2_INTAKE_FREEZE.md` | `8e318cdf39cc2eba5be6f565fb8cf829ee557fecc6fd93b0290e31c14802067a` |
| `DAPP94_DECISION_PACKET_FREEZE.md` | `4644beb0068357d9598d9dc990d473a51cb7398d27ef9c6def80981c94a5e31f` |
| D-APP-94 packet | `87c26c6cab6c8f4928f7606632a208cb960b886527cf04f7191d5d0d4908687b` |
| decision register | `5698122ebd7cdb8312b138d71c7c8439c3b2cf760f85fd9439825b8104f215ca` |
| repair record | `f01dede0e0a73f87aa0d1f8c30da8e73945efea1315581334911477a547660c4` |
| returned manifest | `6415697209d4c4bc6befdfed49b5eb4e3287b3142af831f259f935a8e20a8009` |
| CONTROL range index | `a7f5d9d00aa1fbe954e0604494acdbdaa0312984fd553d8c8aef153e600b8f54` |
| dispositions/causal matrix | `e5c9a2e30c23add8d0047062bc267e26fce32696e54af96fc0e99c7525504bde` |
| intake validation | `cbfd133a0b1f54c210009eb6e3504778e7054fe871b1adb0064a0057cc61535c` |
| R4.4.6 packet freeze | `13566daa015b49fe1d88d4048bd0d961a29c19bfb653921a6a22a524033f5f89` |
| R4.4.6 packet verifier PASS | `25a506b96c0733bd4312450e5d245d6e8fb594ef1ba4700edf64da02800d7748` |
| cleanup addendum freeze | `8ed898eab6199989538f7c8b011d3f2a522edfe5be8c0314ca68a9ac1a8b7fdf` |
| cleanup addendum verifier PASS | `27dc2a89356597ea4e5f5fea8f6e6148094050c3e4e6db788bf7d3441087bc3f` |
| literal sorted all-40 recomputation | `480f1817774d2c2a8bc74e7e584674341f9699a2f9e2a9f5132f75050a790cfb` |

The successor's semantic repairs pass, but the frozen aggregate gate does not.
