# Dependency Closure Report — SCA-004 post-Phase 3

Verdict: `WARNING` with closure verdict `PASS_ZERO_UNRESOLVED_VIOLATIONS`.

## Scope and authority

The audit covers the exact 53 applied revision-1.3 Root deliverables plus six
packages. It cites R7-A, N1 commit `49844ad30d75171f96715e14065a51a65dbb6456`,
N2 commit `5502aea661225e70bc2341b9eed551f16237c09b`, and their bound returns.
The accepted pointer remains `4335593a4d85b701c8322f83937aca3259be58275195a6915e524a64f914410c`. This is derivative evidence,
not decomposition or deliverable-local dependency authority.

## Closure result

- Authoritative local declarations: 16 rows across eight containers.
- Unique Root relationships: 9 (8 gating; 1 non-gating).
- Cross-loop App notice/fan-in relationships: 2, non-gating.
- Orphan targets: 0.
- Non-trivial SCCs / cycle-participating edges: 0 / 0.
- Hubs / bidirectional gating pairs: 0 / 0.
- Human-gated cut or merge required: no.
- Unresolved closure violations: 0.

The six DEL-02-07..12 evidence fan-in relationships converge on DEL-02-06.
DEL-04-05 and DEL-05-02 supply grounded inputs to DEL-04-11. DEL-04-11's
relationship to DEL-02-06 is validation support only and does not gate SCC
ordering. No relationship points outside the accepted 53-deliverable register.

## Phase-1 warning disposition

All seven SCA-004 carrier dependency containers are now extracted, so the
initialized-empty warning from Phase 1 is cleared. Forty-five legacy containers
remain `NOT_RUN_YET`; this broader coverage gap is retained as a warning because
the Phase-3 extraction authority was bounded to the SCA-004 carrier slice. It is
not an unresolved closure violation in that slice.

## Core-check verdicts

| Check | Result | Reason |
|---|---|---|
| live_node_coverage | `PASS` | 53/53 deliverables and 6/6 packages resolve from the applied register. |
| root_dependency_schema | `WARNING` | 8/53 authoritative _DEPENDENCIES.md containers are extracted for Phase 3; 45 legacy containers remain NOT_RUN_YET outside this bounded propagation slice. |
| phase1_initialized_empty_state | `PASS` | 7/7 SCA-004 carrier containers now contain grounded extraction results; the Phase-1 initialized-empty warning is cleared. |
| orphan_dependency_targets | `PASS` | 0 orphan Root targets across nine unique relationships. |
| circular_dependencies | `PASS` | 53 singleton deliverable SCCs; 0 non-trivial SCCs and 0 cycle-participating edges. |
| anchor_coverage | `NOT_APPLICABLE` | Root _DEPENDENCIES.md has accepted-grounding citations rather than generic Dependencies.csv ANCHOR rows; all 16 local declarations carry grounding evidence. |
| misplaced_fields | `PASS` | 0 malformed local relationship rows and 0 foreign targets in the Root relationship layer. |
| id_format_consistency | `PASS` | All local relationship endpoints resolve to exact accepted long-form deliverable IDs; no normalization required. |
| isolated_deliverables | `INFO` | 43/53 nodes have no Phase-3 gating edge; 45 legacy dependency containers remain outside the bounded extraction slice. |
| hub_analysis | `PASS` | 0 hubs at threshold 20; maximum strict degree is 6. |
| bidirectional_pairs | `PASS` | 0 bidirectional gating pairs. |
| closure_violations | `PASS` | 0 unresolved closure violations in the post-extraction relationship set. |
| notice_authority_boundary | `PASS` | 2 App coupling edges are notice/fan-in only, non-gating, and excluded from Root SCC ordering. |


## Derivative status and rerun

Re-run the graph and this audit after estimates/schedule or any accepted
dependency change. Cycle-participating edges, if introduced later, remain
non-gating until a recorded decompose/invert/merge/cut disposition; cut and
merge return to the owner.
