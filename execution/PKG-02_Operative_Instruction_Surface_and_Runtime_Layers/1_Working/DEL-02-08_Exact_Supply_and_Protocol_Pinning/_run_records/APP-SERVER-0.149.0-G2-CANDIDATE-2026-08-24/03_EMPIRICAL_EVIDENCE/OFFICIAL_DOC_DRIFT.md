# Current Official-Documentation Drift

**Candidate state:** `CANDIDATE_AWAITING_G2_OWNER_ACCEPTANCE`

The N1 currentness record pins the retrieved official App Server Markdown at
SHA-256 `9194fc63fd56b8f49bf16c5ecc672eb50a4bc9c08370f3289c183d2a1133844a`
and the official configuration-reference Markdown at SHA-256
`6464159e3897bbda6c81871500497bf79de35c62d7dfd7af354b2a33a158f687`.

| Topic | Current official documentation | Exact 0.149.0 package behavior | Disposition |
| --- | --- | --- | --- |
| schema/types | documents wrapper commands `codex app-server generate-json-schema` and `generate-ts` | pinned dedicated server and ancillary code-mode host expose neither; direct server commands reject both | `UNAVAILABLE_UNDER_BOUNDS`; package/wrapper mismatch |
| curated-plugin synchronization | no dedicated switch or observed destination is named | `features.plugins` default-on governs startup curated/featured plugin work | exact-pin artifact behavior recorded |
| `multi_agent_v2` | absent from current retrieved configuration reference | exact pin accepts, reads back, inventories, and applies precedence for `features.multi_agent_v2` | pin-specific field confirmed |
| `config/read` | documented | effective config, origins, disabled project layer, and session flags observed | concordant |
| `configRequirements/read` | documented | returns `requirements: null` on unmanaged disposable host | concordant |

These are evidence comparisons, not claims that current documentation is a
contract for the historical pin. Exact-pin behavior governs the candidate.
