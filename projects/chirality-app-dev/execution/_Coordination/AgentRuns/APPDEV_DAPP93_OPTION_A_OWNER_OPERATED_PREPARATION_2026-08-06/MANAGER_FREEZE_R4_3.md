# Manager freeze R4.3 — reconciled control successor

Status: `IMMUTABLE CONTROL SUCCESSOR — HELD FOR HELP_HUMAN ACCEPTANCE`

This is the sole current freeze. The following immutable freezes are rejected
history and are not current:

- `MANAGER_FREEZE_R4.md` SHA-256
  `b741231bd7a5c7d589f5217c7f01b2a8a56843928b7bf8cbe3b6cb57c8a72bce`;
- `MANAGER_FREEZE_R4_1.md` SHA-256
  `5a23e4152cf53bf5d90b1e84eca2ab8200314b6d17344278c7f02da0d25daac9`;
- `MANAGER_FREEZE_R4_2.md` SHA-256
  `ea2dd68f9e0aa16f0b2c536652f8259c0286c0b1597644c9c45bd2539a85da6b`.

R4.2's reported C1130 omission was not present in its frozen bytes. This
control successor therefore binds identical prepared bytes plus a complete
ordinary-path producer/copy trace; it does not alter the prepared packet.

| Frozen prepared object | SHA-256 |
|---|---|
| `prepared/PACKAGE_RECONSTRUCTION_MANIFEST.md` | `774fed30b5b98548e3c348fe6b3f0d13d70115f569b2d055935831f02e7ac57f` |
| `prepared/lldb-signal-trace.txt` | `720ad198b99c45737564ed596147ca438e60586b5b5241cd6852a49838f245f8` |
| `prepared/LLDB_STATIC_REVALIDATION.md` | `46ad16927a5235b59865e6821b53bb0956937584d8c86738a8b4b7bea2211459` |
| `prepared/COMMAND_AUTHORITY_LEDGER.md` | `254fb53f09fed4d58b602b011ca6fcb9aad371cf39528bd70c9449db59ecdf9c` |
| `prepared/OWNER_OPERATED_RUNBOOK.md` | `970ad67370f12e9c1a5ef865da09bfe402b87495f5d1dcd1258df7f770d011dd` |
| `prepared/EVIDENCE_RETURN_PACKET.md` | `cef1cf5a14ddfa6486aadddfe629c763e775514d59aeddd57ee564d90316b44a` |
| `prepared/INGESTION_VALIDATION_AND_CAUSAL_MATRIX_CONTRACT.md` | `a41d945a362bef91c79618ee1f5cc689236d7264cc3045533ee1291c4101c8ee` |
| `prepared/FUTURE_OWNER_COMMAND_APPROVAL_REQUEST.md` | `800325abfb000c221f4f2177158778058903c8c233bd99378ce8751d4f715a10` |
| `prepared/PREPARED_PACKET_INDEX.md` | `88d6396293a77e9e4e6a2968b33845cb1095ff1c2d0ce701913c9822e8e72bac` |

Control identities:

- R3 freeze / verifier BLOCK:
  `2957d3f3a2a528a26dabecccfe91e8c2775e5c6942be5785b237a44252c22963` /
  `528d6c3fea76bfb2e811c31891153a40715b0db1f0c35079a67f4902d973c006`;
- owner R4 authority:
  `032691216ac07054d975fad04aedb234e4bf3f1319b638bfac63ffd924b4fd1e`;
- EVALUATION report / handoff:
  `9b4992a285e18040e2ef9ae2d6af4d34fabdb392277d606a587f82efe8d4f2a5` /
  `0b5607afa53151a1f730a3c53a899fa85d321270e820bf97d81435656c2849ff`;
- rejection-recovery amendment v1.9:
  `8b2196042a09716ea4e0b23e5eff22ea83543964bf15b5303002faac86897c1d`;
- C1155 ordinary-path producer/copy trace:
  `e3a0a1ecebf9c9f71f5a94315233fa5e0f0420109c1d9272a6d30c4e1531b24e`;
- control-successor backcheck R4:
  `a1c38706436389a47409071244802a40674cae5314c94d684a94a2526a9af0ea`.

Frozen facts: 93 unique rows C196/C197/C1067-C1157; 31 literal
dispositions; A01-A44 and B01-B40 pass unchanged; C1155 ordinary required
objects are traced 21/21; C1148 produces `SOURCE_SCREEN_RESULTS.txt`; C1130
copies it as source fifteen within C1145→C1144→C1130; C1157/C1154/C1155
consume it. C196/C197 and all unaffected prepared bytes remain preserved.

No packet command was approved or executed. Only static checks were run. Any
byte change to a frozen prepared object or bound control object invalidates
this freeze. The one fresh verifier remains unused pending explicit
HELP_HUMAN acceptance.
