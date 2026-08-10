# R4.4.3 route-hash-cycle repair backcheck

Verdict: `PASS — AUXILIARY HASH CYCLE REMOVED — READY TO FREEZE`

Authority adoption SHA-256:
`ec94e71ef052c0bda4651896cd78a7f584749574b7462a1a0c1998df8d623a2d`.
Work-graph amendment v1.13 SHA-256:
`62747665ddef8cc7369862abfec3c4abf4bac8a695f58655ae54a5964fad994e`.

## Reproduced blocked basis

| Object | SHA-256 |
|---|---|
| accepted R4.4.3 freeze | `cbbd5b9c0c366e8dc9851dfaa959a7f1260697ad290b703206ef47b94788e5a1` |
| sole fresh-verifier BLOCK | `9e8e0c3be74d35579b484099961d5c6a3b50f5971e3f83254e49a5bd766a6665` |
| blocked handoff | `303b0dd3098c121bc3efd8a9cc43eeddaf2fd66460c76e2f86fc7e5554e0ef5f` |
| Receipt 141 ledger | `310e32ddff0fcaa7eba84bc55b3a0978b25b13d0ec20937747942226eb9165bf` |

## Repaired identities

| Object | SHA-256 |
|---|---|
| `prepared/COMMAND_AUTHORITY_LEDGER.md` | `34cdde1a1c6ee9660e7b15e20b7112b7306fc94b26758404acdc30d497da6aa6` |
| `prepared/FUTURE_OWNER_COMMAND_APPROVAL_REQUEST.md` | `3e907635a53cca4c6c5539252dbf9186ac976fd886384fd9c7aa75132914b9a0` |
| `prepared/PREPARED_PACKET_INDEX.md` | `983d3aa7857e9748369edd123226de69b893f41395b76cf3e57e7e0a86b1e23f` |
| `R4_4_COMMAND_INVENTORY.md` | `3e9b9d9c26acc574c1259f834b428d1813ec860722ece47c5ba6cb84e1663f93` |

The auxiliary terminal-route summary now requires every applicable
then-produced raw-evidence return/copy required by the pre-cut route to succeed
before C1142. It explicitly keeps C1154-C1157 whole-file hashes post-cut after
C1152 and never C1142 prerequisites; C1152 remains only a later
observation/crosscheck. The former “every required copy and hash succeeds”
phrase has zero current occurrences.

## Exact command-byte preservation

- All 93 ledger operation cells reproduce ordered digest
  `f175bfca90b161860225f519204acfd4a95cc09342b3f5d5d48f34b6f4bba1f1`.
- All 87 exact sub-inputs reproduce ordered digest
  `d98d0bdcc52e495d8d8ac3cb80de88ce77044c9f15241f5c4180c2998196d65f`.
- C1142 remains exactly
  `/bin/rm -rf /private/tmp/chirality-dapp93-owner-operated-20260807`.
- C196/C197 exact row hashes remain
  `9fcd7d9f3b804e5706c17d372dd0977d8b4634b7bc7540c9a0b1728fd5772dfb`
  and `610b7d237e37b1532b804b00c88cd5cfd6d35453ad17cb84ad4efbde5435df52`.

## Unaffected identities

| Object | SHA-256 |
|---|---|
| `prepared/PACKAGE_RECONSTRUCTION_MANIFEST.md` | `4ea7a6340e2a24727af496c830ffd4e38b3b619e1c0c58cd06897a908a13b874` |
| `prepared/lldb-signal-trace.txt` | `720ad198b99c45737564ed596147ca438e60586b5b5241cd6852a49838f245f8` |
| `prepared/LLDB_STATIC_REVALIDATION.md` | `46ad16927a5235b59865e6821b53bb0956937584d8c86738a8b4b7bea2211459` |
| `prepared/OWNER_OPERATED_RUNBOOK.md` | `6f82568113ad19033948d824d257f9af474b490083988c597882bf691df8e5ac` |
| `prepared/EVIDENCE_RETURN_PACKET.md` | `4457d1185a45cf112cc1e137e5def73166f0fc4554d4c40da94217d3eab692cc` |
| `prepared/INGESTION_VALIDATION_AND_CAUSAL_MATRIX_CONTRACT.md` | `dc3c5c7b8fbb2edb61c0046cc82934c8b64c18ba820bac70fb188e57d6ecdad7` |
| `R4_4_BRANCH_AND_RAW_BYTE_MATRICES.md` | `fef3fc1ca92797389108ad0d1267ea0b040de80ac8f3a5098a3708f2c7c21531` |

The unchanged runbook, ingestion contract, and branch matrix already place
pre-cut returns before C1142 and C1154-C1157 in the finite post-cut tail.

## Mechanical checks

- all eight prepared-index member hashes reproduce;
- 93 IDs, ordinary C1145→C1144→C1130 order, C1146.30 terminal cut, repaired
  manifest, simplified raw packet, and raw completeness set remain intact;
- candidate whitespace is zero and `git diff --check` passes;
- fixed temporary root and returned directory are absent; and
- all observed dirty paths remain under `projects/chirality-app-dev/`.

No verifier was dispatched. No runtime, debugger, package, helper/GUI, signal,
credential, product, release, reliance, Git mutation, Task Management,
foreign-loop, or other effect occurred.
