# References: DEL-05-04 Runtime Replay, Dialogue, and Agent Transcript Projection

## Authoritative Source Corpus

| RefID | Path | Role | ExpectedSHA256 | ActualSHA256 | Status |
|---|---|---|---|---|---|
| REF-001 | `docs/DIRECTIVE.md` | Intent, authority, professional boundaries | `50b816d5be74021f173e19b39773b4f5d2cc3f434966dc9d6faf9399ddf26099` | `50b816d5be74021f173e19b39773b4f5d2cc3f434966dc9d6faf9399ddf26099` | MATCH |
| REF-002 | `docs/CONTRACT.md` | Invariants and enforcement surfaces | `51ec0d4872dd1eba7921e9419231c0d3dc1b3fb368fe6040623a28a16f788517` | `51ec0d4872dd1eba7921e9419231c0d3dc1b3fb368fe6040623a28a16f788517` | MATCH |
| REF-003 | `docs/SPEC.md` | Physical structures, runtime mechanics, API/file contracts | `c2fb9ecbbc37a98577a64a3e7e641de8c26b3145ad8cc40dc4a9a014aa66a12b` | `c2fb9ecbbc37a98577a64a3e7e641de8c26b3145ad8cc40dc4a9a014aa66a12b` | MATCH |
| REF-004 | `docs/TYPES.md` | Vocabulary, identifiers, enums, type targets | `a8cdc94d39e16271ec4ef7fde5be76969f23ca3fe9e1663ac53ad1915eefd56c` | `a8cdc94d39e16271ec4ef7fde5be76969f23ca3fe9e1663ac53ad1915eefd56c` | MATCH |
| REF-005 | `docs/PLAN.md` | Roadmap and implementation sequencing | `3741bb7ec389c12f0856cf64acc27d4d17b77d1683275564b75182fcdbab5187` | `3741bb7ec389c12f0856cf64acc27d4d17b77d1683275564b75182fcdbab5187` | MATCH |
| REF-006 | `docs/PRD.md` | Product requirements, runtime direction, and approved vNext scope | `87ced649beae245e7b0290b3ef8afb46681d04e671964a0583fdce83a7ccb586` | `87ced649beae245e7b0290b3ef8afb46681d04e671964a0583fdce83a7ccb586` | MATCH |
| REF-007 | `/Users/ryan/ai-env/projects/chirality/agents/AGENT_SOFTWARE_DECOMP.md` | Decomposition method and gate protocol | `ad849d9a927485d8749713070579cf072663a2efab63abef2b7db16efeb43409` | `ad849d9a927485d8749713070579cf072663a2efab63abef2b7db16efeb43409` | MATCH |

## Decomposition Entry

- Decomposition: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`
- DeliverableID: `DEL-05-04`
- PackageID: `PKG-05`

## SCA-APP-004 Authority Lineage

| Source | Role | Treatment |
|---|---|---|
| `execution/_ScopeChange/SCA-APP-004_2026-07-23_Workroom_Agent_Room_IA_Redesign/Amendment_Preview.md` | Owner-approved exact DEL-05-04 amendment and semantic ownership partition | GOVERNING FOR THIS RECONCILIATION |
| `execution/_ScopeChange/SCA-APP-004_2026-07-23_Workroom_Agent_Room_IA_Redesign/Propagation_Plan.md` | Owner-approved Gate-5 write scope, no-change set, and validation obligations | GOVERNING FOR THIS RECONCILIATION |
| `execution/_Coordination/_DECISIONS/D-APP-74_RULING_2026-07-23.md` | Prospective Woven Dialogue ruling and partial supersession record | GATE-5 AUTHORITY; path/hash verified during integration |

The six authority-document hashes above are reconciled to authority corpus v16
after the SCA-APP-004 Gate-5 authority/decomposition fan-in.

## Notes

- TASK runs should ground draft content in accessible source slices from the corpus above.
- Missing or conflicting source evidence must be labeled `TBD`, `ASSUMPTION`, or `PROPOSAL`; it must not be treated as accepted project truth.
- Projection relationships require exact admitted identifiers. Missing,
  conflicting, stale, or unrecorded relationships remain explicit and are not
  inferred from dialogue.
