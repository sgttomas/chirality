# DEL-02-06 R16 Successor Binding-Disposition Snapshot

- **Status:** `R16_TIER0_RELATIONSHIP_DISPOSED__NINE_BINDINGS_HELD`
- **Compatibility identity / epoch:** `root-runtime-1` / `1`
- **Authority:** R16-A and R16-B, owner ruling of 2026-08-27
- **Accepted predecessor snapshot:** `ACCEPTED_COMPATIBILITY_SNAPSHOT.md` at
  SHA-256 `f497cbbd8b9e7af454a82beae0aaed530374476ae6e97ff64195554c20cfe6b4`
- **Accepted predecessor JSON:** `COMPATIBILITY_COMPLETION_CANDIDATE.json` at
  SHA-256 `e5ae4e874bdace43720db082a9bd1ae3ff81b9e731264c65039b02d7f720467c`
- **Predecessor disposition:** preserved byte-identical and not rewritten

## Complete R16-A routing matrix

| Binding | R16 disposition |
| --- | --- |
| `2_source_and_release_identities.source_identity` | Remains `HELD_UNAVAILABLE` until exact proposed implementation bytes exist and the Root accountable human accepts their exact source identity. |
| `2_source_and_release_identities.release_identity` | Remains `HELD_UNAVAILABLE` for the G6a accountable-human release act. |
| `4_conformance_or_migration_evidence.clients[0]` — Chirality App | Remains `HELD_UNAVAILABLE`; routed to the App-owned G5/G7 conformance fan-in. |
| `4_conformance_or_migration_evidence.clients[1]` — Root CLI | Remains `HELD_UNAVAILABLE`; routed to the Root-owned G5/G7 conformance fan-in. |
| `5_root_semantic_and_regression_evidence` | Remains `HELD_UNAVAILABLE`; routed to accepted Root implementation followed by G5/G7 evidence acceptance. |
| `6_census_relationship_routing_notice_and_findings.notice` | Remains `HELD_UNAVAILABLE`; routed to the affected owning loops before cutover/release fan-in. |
| `6_census_relationship_routing_notice_and_findings.tier_0_relationship` | The relationship is substantively disposed by R16-B. Root may materialize an immutable successor relationship record and successor binding-disposition snapshot; it must not rewrite the previously accepted package bytes. |
| `8_accountable_human_acts.implementation_act` | Remains `HELD_UNAVAILABLE` until the feasibility results are frozen or rejected and exact sealed WP-03/WP-05 implementation briefs exist for a separate accountable-human act. |
| `8_accountable_human_acts.cutover_act` | Remains `HELD_UNAVAILABLE` until the required G2-G5 fan-in is accepted. |
| `8_accountable_human_acts.release_act` | Remains `HELD_UNAVAILABLE` for G6a. |

## Substantive disposition proof

The Tier-0 relationship is the only binding that receives a substantive R16
disposition. Its successor state is
`CONTINUE_SEPARATE_WITH_EXPLICIT_COORDINATION_ONLY`, recorded in
`TIER0_RELATIONSHIP_RECORD.md`. The other nine bindings remain held under
their stated owners and gates. In particular, `source_identity` and
`implementation_act` remain unavailable, so G0.5 has not passed.

This successor snapshot creates no App, Piping, or Tier-0 truth, work,
dependency, implementation act, cutover act, release act, pin change, or
foreign-loop authority.
