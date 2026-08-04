# E3 dispatch input — exact draft binding

Dispatch time basis: after E1/E2 completion; manager draft remains
non-authoritative and implementation held.

| Input | SHA-256 |
|---|---|
| `OWNER_SEMANTIC_DECISION_PACKET.md` | `eab62217cc60f70f115b884a5f627240e1c8c6d52df76534fc3e0e922046520c` |
| `SEMANTIC_OPTIONS.json` | `b3d1ba6e856208b9923571efc54ae5d580b1aae94f11deac690d76c73820e25f` |
| `CANDIDATE_NORMATIVE_CLAUSES.md` | `743a667da5406b1b3d8af17b6d621fa084ff849756c0492418cd33631cb29c1c` |
| `IMPLEMENTATION_TEST_SCOPE_MAP.md` | `ccb670adff4cd05f466bfd3df467acb8c70ca653dc2781944b7d0ac7c3064efc` |
| `RISKS_AND_CAVEATS.md` | `3b0fbb1e50d2bb2b05d3e54ebfef01c10cea1cce13fd146d777f46fb9e662971` |
| `OWNER_RETURN_TEMPLATES.md` | `aa114226bcdc9bd5f6aafd22e9c9086aba1ef31d46e11ef5a62412eea675b679` |
| `../E1-NODE-BEHAVIOR/RETURN.md` | `641626766f8d515477f4ce7c552f12ee8bdc0335cf09f96b756cf8dae6ee1403` |
| `../E1-NODE-BEHAVIOR/EVIDENCE.md` | `ae4277dc57481a8a25abd31625604fc4ba63aec638ec836e29a1d6ff9c4ddebb` |
| `../E1-NODE-BEHAVIOR/PROBE_RESULTS.json` | `0f189a4b4aec299baf0713f2b5ac80f699ff81e18b837d266d44e0bb3f8ae94e` |
| `../E1-NODE-BEHAVIOR/PROBE_RESULTS_REPEAT.json` | `cbb55139c54c5b4e6186eb59ebe06b88fecc11bb072f2708658dcbd398777d62` |
| `../E2-CONTRACT-MAP/RETURN.md` | `183f5635c8b76e5781be795a8f77f5160912a47eb829216eeec0b785d58a69dc` |
| `../E2-CONTRACT-MAP/SOURCE_CONTRACT_MAP.md` | `8f3d3f9483cb71f06dc7cd17d9385177239db919f292fe374eb67c0c479becd1` |

Refute the whole packet, including the policy judgment behind the exact 2,000
ms grace and 500 ms force-settle cap. Do not assume a recommendation is an
accepted fact. Check that a signed recommended return would be sufficient to
authorize only the already-approved implementation scope and that all other
holds remain visible.

Rebind note: the initial dispatch was interrupted before return after the
manager added an explicit sentence that G2 is a policy judgment rather than an
empirical provider bound. The two updated hashes above are the only input
changes; this file is the controlling redispatch binding.
