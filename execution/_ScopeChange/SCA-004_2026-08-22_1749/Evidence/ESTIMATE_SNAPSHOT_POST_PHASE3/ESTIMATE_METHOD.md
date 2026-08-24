# Phase 4 Estimate Method

- **Status:** `DRAFT_AWAITING_OWNER_ACCEPTANCE`
- **Basis:** accepted revision 1.3, R7-accepted carrier SOWs, and Phase-3 dependency extraction
- **Unit:** aggregate work-effort hours
- **Boundary:** derivative decision support only; not an accepted commitment, implementation authority, staffing plan, calendar duration, or schedule

## Estimation rule

Each estimate line is tied to one accepted SOW output and includes bounded
artifact production plus the deliverable-local verification described by that
SOW. Base hours are judgmental effort estimates grounded in the output's stated
artifact and verification breadth; they are not productivity rates. Shared
integration/fan-in effort owned by DEL-02-06 is excluded from the carrier lines
and assessed separately by N2.

The snapshot uses three uncertainty classes:

| Class | Spread from base | Use |
|---|---:|---|
| `LOW_UNCERTAINTY` | -10% / +10% | bounded documentary or reporting output with a stable accepted form |
| `MEDIUM_UNCERTAINTY` | -25% / +25% | defined contract/schema work whose implementation detail remains open |
| `HIGH_UNCERTAINTY` | -50% / +50% | implementation, integration, empirical-fixture, or multi-boundary evidence work with material accepted-detail gaps |

For each line, `low = base × (1 - spread)` and `high = base × (1 + spread)`.
Each result is rounded to the nearest whole hour using half-up rounding. A
deliverable total is the arithmetic sum of its line-item values; totals are
not independently re-rounded. Identical inputs and judgmental base values
therefore reproduce identical ranges.

## Interpretation limits

- Hours are aggregate effort, not elapsed time and not a schedule computation.
- No dates, calendars, staffing, precedence decisions, productivity rates,
  prices, currencies, or cost rates are asserted.
- Phase-3 dependencies shape risk narration only. They are not hours evidence.
- No semantic overlap between carriers is converted into an unrecorded edge.
- A high range expresses uncertainty; it does not authorize contingency scope.
- A held binding's separately named satisfaction/acceptance act is excluded.
  Bounded preparatory output production is estimated only where the accepted
  carrier SOW expressly requires it, and never represented as satisfying the
  hold.

## Global exclusions

The following ten DEL-02-06 bindings and their separately named acts remain
`HELD_UNAVAILABLE` and are excluded from all hours:

1. `binding_groups.2_source_and_release_identities.source_identity`
2. `binding_groups.2_source_and_release_identities.release_identity`
3. `binding_groups.4_conformance_or_migration_evidence.clients[0]` — App
4. `binding_groups.4_conformance_or_migration_evidence.clients[1]` — Root CLI
5. `binding_groups.5_root_semantic_and_regression_evidence`
6. `binding_groups.6_census_relationship_routing_notice_and_findings.notice`
7. `binding_groups.6_census_relationship_routing_notice_and_findings.tier_0_relationship`
8. `binding_groups.8_accountable_human_acts.implementation_act`
9. `binding_groups.8_accountable_human_acts.cutover_act`
10. `binding_groups.8_accountable_human_acts.release_act`

Also excluded globally:

- `TM-ROOT-106` and `TM-ROOT-122` pin decisions or pin amendments;
- `C1`, including the not-yet-authorized App Server 0.149.0 artifact download;
- all App-owned implementation, conformance, evidence, consent-mirror, and
  release obligations; and
- acceptance of this snapshot, implementation authorization, activation,
  cutover, release, and any foreign-loop act.

## Accepted source family

Every carrier estimate cites its exact accepted `ScopeOfWork.md`, `_CONTEXT.md`,
Phase-3 `_DEPENDENCIES.md`, and applied deliverable-register row. The ten-binding
exclusions are transcribed from DEL-02-12 `ScopeOfWork.md`, lines under “All ten
DEL-02-06 compatibility bindings remain `HELD_UNAVAILABLE`.”
