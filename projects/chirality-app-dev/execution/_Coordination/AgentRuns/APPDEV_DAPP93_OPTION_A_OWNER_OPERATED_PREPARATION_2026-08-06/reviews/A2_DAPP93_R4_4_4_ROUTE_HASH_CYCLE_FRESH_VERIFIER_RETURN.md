# D-APP-93 R4.4.4 route-hash-cycle fresh verifier return

Verdict: `PASS`

Instance statement: I was the sole genuinely fresh read-only ephemeral Agent 2
verifier for this gate. I did not delegate, execute or simulate packet bytes,
or repair the candidate. This file is my sole write.

## Exact identity and freeze audit

The sealed brief reproduced SHA-256
`099a193aa6b65d26218283bf5b74deab1f1b83e3242df4437544901b56460278`.
The accepted candidate freeze reproduced before inspection and again after the
complete audit at
`4f655120a009bb27167c7d4334aaf46755626b8c0b3a03e688905e62ec8d6954`.

Every other bound identity reproduced exactly:

- authority adoption `ec94e71ef052c0bda4651896cd78a7f584749574b7462a1a0c1998df8d623a2d`;
- work-graph amendment v1.13 `62747665ddef8cc7369862abfec3c4abf4bac8a695f58655ae54a5964fad994e`;
- predecessor freeze `cbbd5b9c0c366e8dc9851dfaa959a7f1260697ad290b703206ef47b94788e5a1`, sole verifier BLOCK `9e8e0c3be74d35579b484099961d5c6a3b50f5971e3f83254e49a5bd766a6665`, blocked handoff `303b0dd3098c121bc3efd8a9cc43eeddaf2fd66460c76e2f86fc7e5554e0ef5f`, and Receipt-141 ledger `310e32ddff0fcaa7eba84bc55b3a0978b25b13d0ec20937747942226eb9165bf`;
- prepared manifest `4ea7a6340e2a24727af496c830ffd4e38b3b619e1c0c58cd06897a908a13b874`, LLDB script `720ad198b99c45737564ed596147ca438e60586b5b5241cd6852a49838f245f8`, static revalidation `46ad16927a5235b59865e6821b53bb0956937584d8c86738a8b4b7bea2211459`, ledger `34cdde1a1c6ee9660e7b15e20b7112b7306fc94b26758404acdc30d497da6aa6`, runbook `6f82568113ad19033948d824d257f9af474b490083988c597882bf691df8e5ac`, return packet `4457d1185a45cf112cc1e137e5def73166f0fc4554d4c40da94217d3eab692cc`, ingestion contract `dc3c5c7b8fbb2edb61c0046cc82934c8b64c18ba820bac70fb188e57d6ecdad7`, token `3e907635a53cca4c6c5539252dbf9186ac976fd886384fd9c7aa75132914b9a0`, and index `983d3aa7857e9748369edd123226de69b893f41395b76cf3e57e7e0a86b1e23f`;
- command inventory `3e9b9d9c26acc574c1259f834b428d1813ec860722ece47c5ba6cb84e1663f93`, branch/raw matrix `fef3fc1ca92797389108ad0d1267ea0b040de80ac8f3a5098a3708f2c7c21531`, repair backcheck `b9c0b9505d327c781d9aa835226b1afac91febc817aca76342aad8d6fafa871f`, validation `6baca6d0e6e88cb37917655ce6f7a954623b9cc53e60ef33836816d1178ee6a7`, manager return `8995a2f8f3d1531eb416c406e84058b9a2cd3dbee43ff36c923f0cbf567206a5`, and handoff `ef1d78ffd65a79721fc408076409380c9c5b7882f4f05582f619307a4100aad6`.

## Exact-byte and authorized-delta audit

- The ledger has exactly 93 unique primary rows: C196, C197, and contiguous
  C1067-C1157. The independently extracted ordered operation-cell digest is
  `f175bfca90b161860225f519204acfd4a95cc09342b3f5d5d48f34b6f4bba1f1`.
- The 87 exact evidence sub-inputs count as 17 C1130, 30 C1146, 17 C1149,
  one C1150.R, one C1153.01, three C1154, six C1155, eight C1156, and four
  C1157 inputs. Their independently extracted ordered digest is
  `d98d0bdcc52e495d8d8ac3cb80de88ce77044c9f15241f5c4180c2998196d65f`.
- C1142 remains exactly
  `/bin/rm -rf /private/tmp/chirality-dapp93-owner-operated-20260807`.
  C196/C197 newline-terminated row hashes reproduce
  `9fcd7d9f3b804e5706c17d372dd0977d8b4634b7bc7540c9a0b1728fd5772dfb`
  and `610b7d237e37b1532b804b00c88cd5cfd6d35453ad17cb84ad4efbde5435df52`;
  both rows remain `OWNER_APPROVED — VALID — UNUSED`.
- Against the R4.4.3 freeze, the repaired ledger, mechanically corresponding
  inventory, token, and index are the only packet members whose identities
  changed. The manifest, runbook, evidence form, ingestion contract,
  branch/raw matrix, LLDB script/static review, and all other unaffected
  prepared bytes reproduce their predecessor hashes. This is exactly the
  adopted route-hash-cycle repair boundary.

## Adversarial route and source-lifetime audit

The predecessor cycle is removed. Ledger lines 234-239 now require only every
applicable then-produced raw-evidence return/copy required by the pre-cut route
to succeed before C1142; they explicitly place C1154-C1157 whole-file hashes
post-cut after C1152 and make neither those hashes nor C1152 a C1142
prerequisite. The former operative phrase “every required copy and hash
succeeds” has zero occurrences in the ledger.

The same phase distinction is consistent in the C1142/C1151-C1153 rows,
runbook steps 30-31 and its exhaustive matrix, the ingestion derivation and
terminal matrices, the branch/raw matrix, token, index, inventory, freeze, and
same-run cross-references. No equivalent hidden dependency remains:

- Pre-C1070 has no fixed-root removal obligation.
- Partial C1070 and Incomplete baseline return every applicable produced raw
  source before conditional C1142, use live CONTROL to establish no C1079
  input, and freeze that history only later through C1146.30/C1151.F.
- Every post-C1079 route completes C1131-C1141 rollback proof before any legal
  C1142; copy, cleanup, or rollback failure retains state and prohibits C1142.
- Destination-occupied and prohibited-content routes retain source/state and
  perform no universal or alternate removal.
- Post-cut hash failure retains returned primaries and produced sidecars; it
  cannot invalidate an already lawful pre-cut cleanup by circular dependency.

The ordinary route retains exact C1145→C1144→C1130 order. Applicable C1150.R
and C1153.01 precede temp deletion; C1146.30 is the truthful last CONTROL
input; C1151.F is the non-input through-cut export; C1152, C1154.03, remaining
C1154-C1157 hashes, and intake receipt form a finite non-self-referential tail.
No post-cut operation reads the deleted fixed temporary root.

## Evidence and authority audit

The raw matrix and ingestion contract exhaustively cover 21 ordinary primary
raw objects plus one adjacent whole-file SHA stdout sidecar per object. They
include complete C1105-C1108 combined output and immediate two-record
command/tee exit sidecars. Manifest/range derivation, hash comparison,
completeness, exact-zero/PASS crosschecks, and the terminal verdict remain
later-ingestion-only. The token and packet index bind the same simplified raw
packet and explicitly grant no authority by presence.

The fixed temporary root and the returned-evidence directory were absent at
audit completion. I performed no runtime, debugger, package, helper/GUI,
signal, credential, product, release, reliance, Git, Task Management,
foreign-loop, or other unauthorized action. No execution authority issued.

`PASS_PACKET_ROUTE_HASH_CYCLE_REPAIR`
