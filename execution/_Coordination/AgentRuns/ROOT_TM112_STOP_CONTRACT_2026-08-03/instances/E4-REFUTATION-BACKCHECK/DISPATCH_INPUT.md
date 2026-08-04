# E4 exact repair binding

| Input | SHA-256 |
|---|---|
| `OWNER_SEMANTIC_DECISION_PACKET.md` | `25155b680ba3a824578605f4780cb80c7723e9e4f4910d11615868ef609fc2be` |
| `SEMANTIC_OPTIONS.json` | `cb6abdf02920f733533a131da094c0ff2f481ac348cc790b5c601857152377d0` |
| `CANDIDATE_NORMATIVE_CLAUSES.md` | `2428824746c5a6928c2894619d67bbc817717bed536f5ee64b11cdafda0db62e` |
| `IMPLEMENTATION_TEST_SCOPE_MAP.md` | `b945dda1a93d256d8980e188b48776cfb98395fb1e4174f70cfe6923c517fbcb` |
| `RISKS_AND_CAVEATS.md` | `6152d5ab14c8ef6df40797e4f7e5902eaea195d21da7fa902e1219d4eb34d49a` |
| `OWNER_RETURN_TEMPLATES.md` | `3906f9008d65148f25c936012acc5ab17caabb2feb87078afd43f3534b3cc1bf` |
| `../E3-INDEPENDENT-REFUTER/REFUTATION.md` | `46a66d4f08eb29642fdd33ef35d1bfd24b3c8dbe5c69eb4bcf6ef5cb09377c10` |
| `../E3-INDEPENDENT-REFUTER/RETURN.md` | `5d3ec8b7e5c86ab4a2a0c948d64e7aed840fe0eeb57ef576564210e4ac0cad29` |

Repair claims to verify:

1. connection bound is selected grace + 500, not fixed 2,500 for alternates;
2. interruption versus cleanup failures have explicit states/recovery;
3. 500 ms is expressly accepted as policy uncertainty;
4. concurrent-start testing is mapped; and
5. pre-identity latch expires at force and is generation-owned/tested.
