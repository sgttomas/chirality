# SCA-004 Phase-4 Estimate Snapshot Summary

- **Status:** `DRAFT_AWAITING_OWNER_ACCEPTANCE`
- **Snapshot posture:** immutable derivative decision support
- **Accepted basis:** revision 1.3, R7-accepted carrier contracts, and
  Phase-3 dependency truth
- **Authority:** Root Phase-4 steer at
  `plans/steers/chirality_app_v3_phase4_steer_root_2026-08-23.md`, SHA-256
  `54595fe5060bed81fb9b871d623d15505ee7ff42b4e7349d238b9c4d0f9cc644`
- **Prior governed state:** Receipt 123 in
  `execution/_Coordination/LOOP_RECEIPTS.md`

This package estimates aggregate work-effort hours. It is not decomposition
truth, an accepted estimate, a commitment, a staffing plan, a calendar
duration, a schedule, a lifecycle change, an implementation act, or authority
to write any anticipated locus. Owner acceptance is a separate act against
these exact bytes.

## Uncertainty method

`ESTIMATE_METHOD.md` defines the deterministic ranges used throughout:

| Class | Low | High | Intended use |
|---|---:|---:|---|
| `LOW_UNCERTAINTY` | base - 10% | base + 10% | stable bounded documentary/reporting output |
| `MEDIUM_UNCERTAINTY` | base - 25% | base + 25% | defined contract/schema output with open implementation detail |
| `HIGH_UNCERTAINTY` | base - 50% | base + 50% | implementation, integration, empirical fixture, or multi-boundary evidence output |

Line results use nearest-whole-hour half-up rounding. Deliverable and package
totals are sums of line results and are not independently rounded.

## Estimate totals

| Deliverable | Estimate posture | Priced elements | Base h | Low h | High h |
|---|---|---:|---:|---:|---:|
| DEL-02-06 | incremental integration/fan-in reassessment | 10 | 116 | 63 | 169 |
| DEL-02-07 | carrier output production and local verification | 5 | 180 | 94 | 266 |
| DEL-02-08 | carrier output production and locally estimable fixture work | 5 | 100 | 57 | 143 |
| DEL-02-09 | carrier output production and local verification | 6 | 148 | 82 | 214 |
| DEL-02-10 | carrier output production and local verification | 6 | 144 | 88 | 200 |
| DEL-02-11 | carrier output production and local verification | 5 | 136 | 72 | 200 |
| DEL-02-12 | currently estimable Root-owned, hold-preserving portions | 5 | 96 | 51 | 141 |
| DEL-04-11 | carrier output production and local verification | 4 | 92 | 53 | 131 |
| **All eight estimates** |  | **46** | **1012** | **560** | **1464** |

### Rollups

| Rollup | Base h | Low h | High h |
|---|---:|---:|---:|
| Seven new carriers (N1) | 896 | 497 | 1295 |
| PKG-02 carriers DEL-02-07..12 | 804 | 444 | 1164 |
| PKG-04 carrier DEL-04-11 | 92 | 53 | 131 |
| DEL-02-06 incremental integration/fan-in (N2) | 116 | 63 | 169 |
| **Combined decision-support envelope** | **1012** | **560** | **1464** |

The combined total is arithmetic aggregation of effort, not elapsed duration.
No concurrency, staffing, precedence, calendar, or critical-path computation
is implied.

## Exclusion boundary

No hours are assigned to satisfaction or acceptance of these ten
`HELD_UNAVAILABLE` bindings:

1. `binding_groups.2_source_and_release_identities.source_identity`
2. `binding_groups.2_source_and_release_identities.release_identity`
3. `binding_groups.4_conformance_or_migration_evidence.clients[0]`
4. `binding_groups.4_conformance_or_migration_evidence.clients[1]`
5. `binding_groups.5_root_semantic_and_regression_evidence`
6. `binding_groups.6_census_relationship_routing_notice_and_findings.notice`
7. `binding_groups.6_census_relationship_routing_notice_and_findings.tier_0_relationship`
8. `binding_groups.8_accountable_human_acts.implementation_act`
9. `binding_groups.8_accountable_human_acts.cutover_act`
10. `binding_groups.8_accountable_human_acts.release_act`

Also excluded are `TM-ROOT-106`, `TM-ROOT-122`, every pin decision or
amendment, C1 and the App Server 0.149.0 artifact download, all App-owned
implementation/conformance/evidence/consent-mirror/release obligations,
foreign-loop acts, snapshot acceptance, implementation authorization,
activation, cutover, public export, release, and reliance. Excluded or held
work is a grounding gap, not zero-hour work.

## Dependency-shaped sequencing risk

- DEL-02-07..DEL-02-12 each have a gating evidence-fan-in edge to DEL-02-06
  for final integration/release assurance. Their production estimates do not
  include DEL-02-06 intake and reconciliation effort.
- The accepted dependency truth declares no strict ordering among those six
  carriers. This package does not silently linearize their semantic overlap.
- DEL-02-12 can remain incomplete after other Root evidence exists because
  its held and App-owned inputs are intentionally unavailable or foreign.
- DEL-04-11 has gating accepted-contract inputs from DEL-04-05 and DEL-05-02,
  plus a non-gating validation relationship to DEL-02-06. Its separately
  required `tools/**` M2 authority is not granted or priced as available.
- DEL-02-06's incremental fan-in can close only after corresponding carrier
  evidence is separately produced and accepted. Its DEL-04-11 intake remains
  optional/non-gating unless a separately accepted report exists.

These are risk statements only. Scheduling occurs, if authorized, only after
owner acceptance of an exact estimate snapshot.

## Review and provenance

`REVIEW.md` records three independent review cycles, the mechanical repair of
four package EOF-whitespace defects, and zero terminal actionable findings.
No estimate or method bytes changed. `INPUT_HASHES.csv` pins the accepted and
controlling inputs plus the derivative estimate method.
`ARTIFACT_HASHES.csv` seals every package artifact except itself.
