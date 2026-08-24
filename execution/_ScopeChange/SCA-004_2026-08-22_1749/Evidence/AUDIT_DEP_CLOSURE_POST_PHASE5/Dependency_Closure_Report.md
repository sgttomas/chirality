# Dependency Closure Report — SCA-004 post-Phase 5

Verdict: `WARNING` with closure verdict `PASS_ZERO_UNRESOLVED_VIOLATIONS`.

## Scope and authority

The audit covers the exact 53 live applied revision-1.3 Root deliverables plus six packages. It pins current repaired Phase-3 N1 and current N2 returns, accepted estimate/N1 acceptance, and the sealed schedule package. Estimates and schedule are context only; the eight current `_DEPENDENCIES.md` files remain the relationship authority. This snapshot is immutable derivative evidence.

## Closure result

- Authoritative local declarations: 16 rows across eight containers.
- Unique Root relationships: nine (eight gating; one non-gating).
- Cross-loop App notice/fan-in relationships: two, non-gating.
- Orphan targets: zero.
- Non-trivial SCCs / cycle-participating edges: zero / zero.
- Hubs / bidirectional gating pairs: zero / zero.
- Human-gated cut or merge required: no.
- Unresolved closure violations: zero.

The six DEL-02-07..12 evidence fan-ins converge on DEL-02-06. DEL-04-05 and DEL-05-02 supply the two gating inputs to DEL-04-11. DEL-04-11 validation of DEL-02-06 remains non-gating. No relationship points outside the accepted 53-deliverable register.

## Phase-3 comparison and warnings

Current node, membership-edge, dependency-edge, gating, notice-edge, and SCC classifications match Phase 3 exactly. The zero-unresolved-violation verdict is unchanged. All seven initialized-empty warnings remain cleared. Forty-five legacy containers remain `NOT_RUN_YET`, the same bounded warning as Phase 3; no deviation exists.

## Core-check verdicts

| Check | Result | Reason |
|---|---|---|
| live_node_coverage | `PASS` | 53/53 deliverables and 6/6 packages resolve from the live applied register. |
| root_dependency_schema | `WARNING` | 8/53 authoritative _DEPENDENCIES.md containers remain extracted for Phase 3; 45 legacy containers remain NOT_RUN_YET outside this bounded slice. |
| phase1_initialized_empty_state | `PASS` | 7/7 SCA-004 carrier containers contain grounded extraction results; all seven Phase-1 initialized-empty warnings remain cleared. |
| orphan_dependency_targets | `PASS` | 0 orphan Root targets across nine unique relationships. |
| circular_dependencies | `PASS` | 53 singleton deliverable SCCs; 0 non-trivial SCCs and 0 cycle-participating edges. |
| anchor_coverage | `NOT_APPLICABLE` | Root _DEPENDENCIES.md uses accepted-grounding citations; all 16 local declarations carry evidence. |
| misplaced_fields | `PASS` | 0 malformed local relationship rows and 0 foreign targets in the Root relationship layer. |
| id_format_consistency | `PASS` | All relationship endpoints resolve to exact accepted long-form IDs; no normalization required. |
| isolated_deliverables | `INFO` | 43/53 nodes have no gating edge; 45 legacy dependency containers remain outside the bounded extraction slice. |
| hub_analysis | `PASS` | 0 hubs at threshold 20; maximum strict degree is 6. |
| bidirectional_pairs | `PASS` | 0 bidirectional gating pairs. |
| closure_violations | `PASS` | 0 unresolved closure violations in current live state. |
| notice_authority_boundary | `PASS` | 2 App notice/fan-in edges remain non-gating and excluded from Root SCC ordering. |
| phase3_deterministic_comparison | `PASS` | Node, edge, gating, notice, SCC, closure-verdict, and bounded-warning results match Phase 3 exactly. |

## Derivative status and rerun

Immutable derivative evidence. Re-run after any pinned input or accepted dependency truth change. Any later cycle-participating edge remains non-gating until a recorded decompose/invert/merge/cut disposition; cut and merge return to the owner.
