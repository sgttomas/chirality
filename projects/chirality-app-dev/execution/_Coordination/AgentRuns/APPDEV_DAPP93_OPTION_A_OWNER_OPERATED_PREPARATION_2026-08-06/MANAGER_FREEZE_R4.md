# Manager freeze R4 — exhaustive branch/evidence packet repair

Status: `IMMUTABLE R4 FREEZE — HELD FOR HELP_HUMAN ACCEPTANCE BEFORE VERIFIER DISPATCH`

This freeze supersedes R3 for presentation fitness. R3, its verifier `BLOCK`,
the closed no-return audit child, and the accepted EVALUATION audit remain
immutable history.

## Prepared-object identities

| Frozen object | SHA-256 |
|---|---|
| `prepared/PACKAGE_RECONSTRUCTION_MANIFEST.md` | `774fed30b5b98548e3c348fe6b3f0d13d70115f569b2d055935831f02e7ac57f` |
| `prepared/lldb-signal-trace.txt` | `720ad198b99c45737564ed596147ca438e60586b5b5241cd6852a49838f245f8` |
| `prepared/LLDB_STATIC_REVALIDATION.md` | `46ad16927a5235b59865e6821b53bb0956937584d8c86738a8b4b7bea2211459` |
| `prepared/COMMAND_AUTHORITY_LEDGER.md` | `f65e14c8dcbecd5c8c8b14e879b2185577c0ac6680542ddc8fb4384664f8a541` |
| `prepared/OWNER_OPERATED_RUNBOOK.md` | `8b1e2dc90004a439a4f1fd3cf459f76d07a7adc42a5959af655ed2aca22dc25d` |
| `prepared/EVIDENCE_RETURN_PACKET.md` | `8b0146123e8bf01ecaa08a869fcd01a320ac6ce9a87a74ff6db46533bf34e5c1` |
| `prepared/INGESTION_VALIDATION_AND_CAUSAL_MATRIX_CONTRACT.md` | `3fa1e3b3fad043fc4b64e3d73e4fea40c96604b0801e81b8c71dd6844fb2921d` |
| `prepared/FUTURE_OWNER_COMMAND_APPROVAL_REQUEST.md` | `cb56fca435812e4fcb403c32353cde4ac8cad9aa1a1e0a4efaf45a7ec73f70a1` |
| `prepared/PREPARED_PACKET_INDEX.md` | `0ad0bfb3def893a031e9666880dce91c727e3065eec9b28948c05045af179e1f` |

## Repair/control identities

- R3 freeze:
  `2957d3f3a2a528a26dabecccfe91e8c2775e5c6942be5785b237a44252c22963`;
- R3 verifier `BLOCK`:
  `528d6c3fea76bfb2e811c31891153a40715b0db1f0c35079a67f4902d973c006`;
- R4 owner authority adoption:
  `032691216ac07054d975fad04aedb234e4bf3f1319b638bfac63ffd924b4fd1e`;
- work-graph amendment v1.5:
  `e2bbe7d5b38ea14f24e068e25b22226d104ee285dcd3505ed0590575626381d5`;
- audit-method recovery amendment v1.6:
  `ab80a6b27d22ca788833643777399b41291a8bff9179e551b3f3665b89a52809`;
- accepted EVALUATION report:
  `9b4992a285e18040e2ef9ae2d6af4d34fabdb392277d606a587f82efe8d4f2a5`;
- accepted EVALUATION handoff:
  `0b5607afa53151a1f730a3c53a899fa85d321270e820bf97d81435656c2849ff`;
- R4 repair backcheck:
  `73ddf3d88748995e9c86c837fa411a83c119167763c3f6d51a53d2c7b3aa556e`.

## Frozen closure facts

- command rows are C196, C197, and the complete unique contiguous
  C1067-C1151 range (87 total rows);
- C1146-C1151 are the only new IDs;
- C196/C197 exact rows remain unchanged, valid, and unused;
- ordinary post-C196 order remains C1145→C1144→C1130;
- every pre-C196/pre-C197 path uses C1147/C1148 and invokes neither C1144 nor
  C1130;
- pre-C1070, partial-C1070, incomplete-baseline, and post-first-C1079-write
  phases have distinct legal cleanup/rollback prerequisites;
- the return schema contains exactly 31 literal step dispositions;
- complete C1105-C1108 outputs/exits are bound through C1146 ranges/hashes,
  returned through the CONTROL transcript, and checked by C1151;
- C1149 returns the completed derivative form, C1150 creates per-file retained
  evidence identities, and C1151 emits the terminal completeness verdict;
- the three unaffected prepared objects retain their exact R3 identities.

No command is approved or executed by this freeze. Any frozen-byte change
invalidates it. No post-freeze verifier may be dispatched until HELP_HUMAN
accepts this stable freeze for that dispatch.
