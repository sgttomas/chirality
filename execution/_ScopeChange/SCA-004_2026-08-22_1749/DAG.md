# Root v3 release-pathway DAG — SCA-004 Gate 1

Status: `AWAITING_OWNER_ACCEPTANCE`

## Objective and edge meaning

This graph answers one objective only: what Root governance, carrier,
contract, evidence, and release-control state must precede readiness claims
for the v3 pathway through G0.5/G1 without lifting any held implementation,
cutover, release, client, or evidence binding.

A strict `A -> B` edge means A must be accepted/current before B may claim
sequencing readiness for this objective. A `CROSSCHECK` is a read-only
conformance input. A `NOTICE` is coordination only: it never grants foreign
write authority, changes App truth, or gates readiness.

## Strict acyclic layer

```text
DEL-02-03 -> DEL-02-04 -> DEL-03-01 --+
                                             |
DEL-03-03 -----------------------------------+-> DEL-02-06 -> DEL-05-06 -> DEL-05-07 -> DEL-06-07
DEL-04-02 -----------------------------------+       |                          ^             ^
DEL-05-04 -----------------------------------+       +-> DEL-06-01 ------------+-------------+

DEL-05-02 -> DEL-04-05 -> DEL-05-06
```

The strict layer is acyclic. It sequences accepted role/capability doctrine,
containment, dependency semantics, approval attribution, evidence labelling,
runtime integration, receipt-validator discipline, validation, closure,
self-application, and the separate release judgment.

## App notice layer

```text
DEL-04-04 -------------------------------> APP-NOTICE-SCA-APP-008-ROOT-REQUIREMENTS
DEL-02-06 -------------------------------> APP-NOTICE-SCA-APP-008-ROOT-REQUIREMENTS
APP-NOTICE-SCA-APP-008-ROOT-REQUIREMENTS -> APP-NOTICE-SCA-APP-008-RECIPROCAL
APP-NOTICE-SCA-APP-008-RECIPROCAL -------> DEL-02-06
```

All four are `NOTICE`, candidate-layer, and non-gating. The apparent
reciprocal loop records communication, not sequencing or authority.

## Complete SCC inventory

| SCC | Members | Size | Non-trivial | Proposed move |
|---|---|---:|---|---|
| SCC-001 | DEL-02-03 | 1 | no | none — acyclic singleton |
| SCC-002 | DEL-02-04 | 1 | no | none — acyclic singleton |
| SCC-003 | DEL-03-01 | 1 | no | none — acyclic singleton |
| SCC-004 | DEL-03-03 | 1 | no | none — acyclic singleton |
| SCC-005 | DEL-04-02 | 1 | no | none — acyclic singleton |
| SCC-006 | DEL-04-04 | 1 | no | none — acyclic singleton |
| SCC-007 | DEL-05-02 | 1 | no | none — acyclic singleton |
| SCC-008 | DEL-05-04 | 1 | no | none — acyclic singleton |
| SCC-009 | DEL-04-05 | 1 | no | none — acyclic singleton |
| SCC-010 | DEL-05-06 | 1 | no | none — acyclic singleton |
| SCC-011 | DEL-05-07 | 1 | no | none — acyclic singleton |
| SCC-012 | DEL-06-01 | 1 | no | none — acyclic singleton |
| SCC-013 | DEL-06-07 | 1 | no | none — acyclic singleton |
| SCC-014 | DEL-02-06; Root-requirements App notice; reciprocal App notice | 3 | yes | `DECOMPOSE`: one-way Root notice, independently governed App response, later G0.5 fan-in criterion |

SCC-014 cycle edges E-016/E-017/E-018 remain non-gating. `DECOMPOSE` is a
design refinement and does not itself require a cut/merge owner ruling. If a
later workflow instead proposes `CUT` or `MERGE`, that move is human-gated.

## Held boundaries

- The graph does not schedule implementation. All ten accepted DEL-02-06
  bindings remain held.
- Proposed DEL-02-07..12 and DEL-04-11 carrier IDs are absent from this graph
  because they are not yet live folders. This satisfies the live-node rule
  and prevents a candidate decomposition from masquerading as accepted
  execution state.
- After any accepted carrier amendment and PREPARATION act, the graph must be
  re-derived with the new live nodes and audited again.
- App nodes are named notice edges only. SCA-APP-008 is expected to
  reciprocate; Root cannot write or accept App state.
