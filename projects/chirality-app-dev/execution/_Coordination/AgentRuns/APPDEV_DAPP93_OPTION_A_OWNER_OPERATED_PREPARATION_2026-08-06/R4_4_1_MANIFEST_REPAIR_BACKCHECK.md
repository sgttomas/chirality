# R4.4.1 manifest-only repair backcheck

Verdict: `PASS — MANIFEST CONTRADICTION REMOVED — READY TO FREEZE`

Authority adoption SHA-256:
`2114d05a44363f6bba456dd4354af798bd8d0a307394e6b8785e0ce597fd9af4`.
Work-graph amendment v1.11 SHA-256:
`2f34abd3f3bc738730063544b51754088af29a9c19ef394594cf3ae2fa7af666`.

## Reproduced Receipt 139 basis

| Object | SHA-256 | Result |
|---|---|---|
| accepted R4.4.1 freeze | `c5468a2e2098b3ca1640067156c13665890fb829b24bbe72694b4c18fe7ffb75` | PASS |
| sole fresh-verifier BLOCK | `33290eb9f2608aca950f3b8af7df126228cc76af3304348c959ce6c980763e21` | PASS |
| blocked handoff | `b93ec877a181f6643211940db3560052e35c238acd710ffe709194302e19ecaa` | PASS |
| predecessor manifest | `774fed30b5b98548e3c348fe6b3f0d13d70115f569b2d055935831f02e7ac57f` | PASS before repair |
| predecessor prepared index | `cfbfd507d76958a35dd307119620f157eb8183ddc5fceaa0aa64cf963a731667` | PASS before repair |

## Repaired identities

| Object | SHA-256 |
|---|---|
| `prepared/PACKAGE_RECONSTRUCTION_MANIFEST.md` | `4ea7a6340e2a24727af496c830ffd4e38b3b619e1c0c58cd06897a908a13b874` |
| `prepared/PREPARED_PACKET_INDEX.md` | `68d6882cc410ae78f0e56a92519f8a65b83e0f2be5a38e712b95be23391c1393` |

The manifest now removes the exact temporary root only after the selected
route's preservation, rollback, cleanup, and absence-proof prerequisites
succeed. Destination-occupied, prohibited-content, and pre-cut-copy-failure
routes retain applicable state and do not invoke C1142. Cleanup/rollback
failure retains applicable state, stops further destructive cleanup, and does
not retry C1142. An absent fixed root creates no removal obligation.

## Unaffected prepared identities

| Object | SHA-256 | Result |
|---|---|---|
| `prepared/lldb-signal-trace.txt` | `720ad198b99c45737564ed596147ca438e60586b5b5241cd6852a49838f245f8` | unchanged |
| `prepared/LLDB_STATIC_REVALIDATION.md` | `46ad16927a5235b59865e6821b53bb0956937584d8c86738a8b4b7bea2211459` | unchanged |
| `prepared/COMMAND_AUTHORITY_LEDGER.md` | `7e62cb82d8280817d9d444566938ab1706b46b4ec89dd58709f0afeecc722433` | unchanged |
| `prepared/OWNER_OPERATED_RUNBOOK.md` | `2bb2b5f2bcb858ac5edfd630da0574619a40ad4b1f277dc6c16ccc45873c1073` | unchanged |
| `prepared/EVIDENCE_RETURN_PACKET.md` | `4457d1185a45cf112cc1e137e5def73166f0fc4554d4c40da94217d3eab692cc` | unchanged |
| `prepared/INGESTION_VALIDATION_AND_CAUSAL_MATRIX_CONTRACT.md` | `1118756e249ac8935a0ee760ac9234505cb97dec2e297542a6eb428114fe9cbc` | unchanged |
| `prepared/FUTURE_OWNER_COMMAND_APPROVAL_REQUEST.md` | `1531bb31a247c37eba42160aeea7d5580e94246d54ff59768c5207aebc96161d` | unchanged |

The complete command ledger is byte-identical. Its exact newline-terminated
C196/C197 row hashes remain
`9fcd7d9f3b804e5706c17d372dd0977d8b4634b7bc7540c9a0b1728fd5772dfb`
and `610b7d237e37b1532b804b00c88cd5cfd6d35453ad17cb84ad4efbde5435df52`.
Thus every command byte, the 93-ID range, ordinary C1145→C1144→C1130 order,
and the simplified raw packet are unchanged.

## Mechanical checks

- all eight prepared-index member hashes reproduce;
- manifest route requirements agree with the unchanged runbook, branch
  matrix, and ingestion contract;
- candidate whitespace is zero and `git diff --check` passes;
- fixed temporary root and returned directory are absent;
- all 11 observed dirty paths remain under `projects/chirality-app-dev/`;
- no product or frontend byte changed; and
- no verifier or packet operation was dispatched or executed.

No runtime, debugger, package, helper/GUI, signal, credential, product,
release, reliance, Git mutation, Task Management, foreign-loop, or other
effect occurred.
