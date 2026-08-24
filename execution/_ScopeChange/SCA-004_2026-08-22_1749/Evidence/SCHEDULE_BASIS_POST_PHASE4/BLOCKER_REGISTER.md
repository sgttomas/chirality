# Schedule-Basis Blocker and Exclusion Register

- **Status:** all rows remain unresolved, held, excluded, or separately gated
- **Effect:** no row is priced as available work in the accepted effort envelope
- **Authority boundary:** a resolving gate must occur in its owning instrument;
  this derivative candidate cannot perform or imply that act

## Required blocker and exclusion coverage

| ID | Category | Recorded state | Excluded or blocked scope | Recorded resolving gate | Schedule treatment |
|---|---|---|---|---|---|
| `TM-ROOT-106` | Pin/concordance blocker | `OPEN` | Pi 0.82.0 concordance, canonical implementation identity, supply-chain validation, and any pin disposition | Root register closure target `RESOLVED_BY_DECISION`, requiring both an explicit decision record and validation evidence, coordinated with the separately owned App acceptance | Unresolved G1 blocker; no pin assumption or hours |
| `TM-ROOT-122` | Pin/authority blocker | `OPEN` | Electron authority drift and any superseding pin disposition | Separate App disposition of its manifest-owned surface; Root row closes only when App dispositions | Unresolved G1 blocker; no pin assumption or hours |
| `C1` | Artifact-access blocker | not authorized | App Server 0.149.0 artifact download and exact-artifact empirical execution | Separate authorization of the artifact download; resulting exact-artifact evidence remains separately acceptance-gated | Blocked and unpriced; fixture construction does not imply clearance |
| `binding_groups.2_source_and_release_identities.source_identity` | DEL-02-06 binding | `HELD_UNAVAILABLE` | Exact source-identity population and acceptance | The binding's separately named population/satisfaction and acceptance act | Held and unpriced |
| `binding_groups.2_source_and_release_identities.release_identity` | DEL-02-06 binding | `HELD_UNAVAILABLE` | Exact release-identity population and acceptance | The binding's separately named population/satisfaction and acceptance act | Held and unpriced |
| `binding_groups.4_conformance_or_migration_evidence.clients[0]` | DEL-02-06 binding — App | `HELD_UNAVAILABLE` | App client conformance or migration evidence and acceptance | Separately accepted App-owned evidence routed through the DEL-02-12 notice/fan-in boundary, followed by the binding's named acceptance act | Held and unpriced; notice alone is not evidence or a hold lift |
| `binding_groups.4_conformance_or_migration_evidence.clients[1]` | DEL-02-06 binding — Root CLI | `HELD_UNAVAILABLE` | Root CLI conformance or migration evidence and acceptance | Separately produced Root CLI evidence followed by the binding's named acceptance act | Held and unpriced |
| `binding_groups.5_root_semantic_and_regression_evidence` | DEL-02-06 binding | `HELD_UNAVAILABLE` | Root semantic and regression evidence acceptance | Separately produced evidence followed by the named Root acceptance act | Held and unpriced |
| `binding_groups.6_census_relationship_routing_notice_and_findings.notice` | DEL-02-06 binding | `HELD_UNAVAILABLE` | Release-fan-in notice and findings act | The separately named notice act under its owning coordination authority | Held and unpriced; coordination does not equal accepted evidence |
| `binding_groups.6_census_relationship_routing_notice_and_findings.tier_0_relationship` | DEL-02-06 binding | `HELD_UNAVAILABLE` | Tier-0 relationship act | The separately named Tier-0 relationship act under its owning authority | Held and unpriced |
| `binding_groups.8_accountable_human_acts.implementation_act` | DEL-02-06 binding | `HELD_UNAVAILABLE` | Accountable-human implementation authorization/act | Explicit accountable-human implementation act | Held and unpriced; no dispatch |
| `binding_groups.8_accountable_human_acts.cutover_act` | DEL-02-06 binding | `HELD_UNAVAILABLE` | Accountable-human cutover act | Explicit accountable-human cutover act | Held and unpriced |
| `binding_groups.8_accountable_human_acts.release_act` | DEL-02-06 binding | `HELD_UNAVAILABLE` | Accountable-human release act | Explicit accountable-human release act | Held and unpriced |
| `APP-IMPLEMENTATION-OBLIGATIONS` | App-owned exclusion | foreign and unavailable | Every App-owned implementation obligation named by the estimate package | Separate App-loop owner authorization, implementation act, and accepted result in the App-owned instrument | Excluded and unpriced; Root has no authority |
| `APP-CONFORMANCE-OBLIGATIONS` | App-owned exclusion | foreign and unavailable | App-owned conformance production, population, and acceptance | Separately accepted App-owned conformance evidence through the notice/fan-in boundary under App authority | Excluded and unpriced; notice alone is not conformance evidence |
| `APP-EVIDENCE-OBLIGATIONS` | App-owned exclusion | foreign and unavailable | App-owned evidence production, population, and acceptance | Separate App-loop production and acceptance of exact evidence under the owning instrument | Excluded and unpriced; absent evidence stays unresolved |
| `APP-CONSENT-MIRROR-OBLIGATIONS` | App-owned exclusion | foreign and unavailable | App-owned consent-mirror work and acceptance | Separate App-loop owner act and accepted consent-mirror result | Excluded and unpriced; Root consent semantics do not resolve it |
| `APP-RELEASE-OBLIGATIONS` | App-owned exclusion | foreign and unavailable | App-owned release obligations and exact-release reruns | Separate App-loop release authorization, accepted release evidence, and release act | Excluded and unpriced; no release implication |
| `APP-ADAPTER-CLIENT-OBLIGATIONS` | App-owned exclusion | foreign and unavailable | App-owned adapter/client implementation, fixtures, conformance, and evidence | Separate App-loop implementation authorization and accepted adapter/client evidence | Excluded and unpriced; Root API work does not satisfy it |

## Additional candidate and implementation gates

| ID | State | Resolving gate | Effect |
|---|---|---|---|
| `SCHEDULE-OWNER-ACCEPTANCE` | independent review sealed; awaiting owner acceptance | Explicit owner acceptance of the exact sealed bytes | Candidate is not schedule truth or a commitment |
| `DEL-04-11-TOOLS-M2` | not granted | Separate `tools/**` M2 authority | DEL-04-11 effort remains decision support; no implementation authority |
| `GLOBAL-AUTHORITY-EXCLUSIONS` | not granted | Separate accountable-human acts in their owning instruments | No snapshot acceptance, implementation, activation, cutover, public export, release, reliance, or foreign-loop act follows from this package |

## Coverage statement

The required set is complete: two named TM blockers, C1, all ten exact held
binding IDs, and six App-owned obligation categories appearing across the
accepted estimate package. Every item remains unresolved or excluded. Missing
or unavailable work is a grounding gap, not zero-effort work.
