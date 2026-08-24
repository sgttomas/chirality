# Decision Log

## DEC-001 — human override of the generic tool root

The sealed brief records the owner's Gate-5 write-set override. The generic `AGENT_AUDIT_DEP_CLOSURE.md` output root under `_Evaluation/DepClosure` and its pointer-update step are not used. This audit writes content only to this Phase5 snapshot and control evidence only to the named child control root. No `_LATEST.md` pointer is moved.

## DEC-002 — registered analyzer identity and invocation

The registered analyzer was run exactly once:

```text
PYTHONDONTWRITEBYTECODE=1 python3 tools/coordination/analyze_dep_closure.py projects/chirality-app-dev/execution --output-dir projects/chirality-app-dev/execution/_ScopeChange/SCA-APP-008_2026-08-23_1727_V3_Release_Pathway/Phase5/Audit/SCA-APP-008-GATE5-POST-APPLICATION_2026-08-24/Evidence
```

Analyzer SHA-256: `e10abf213925df3aae69353c3a8c0dd5cfbb0402957d37c3766a3a9858c97b91`. An exact run-time copy is preserved as `analyze_closure.py`.

## DEC-003 — current analyzer output gap

The registered analyzer does not emit `cycles_sample.csv`, although the dedicated-agent package contract requires it. The analyzer was not rerun or changed. A deterministic, bounded enumeration over the analyzer's same 98-edge directed graph produced the 10 elementary cycles recorded in `Evidence/cycles_sample.csv`. The enumeration applies the same ACTIVE + EXECUTION + DELIVERABLE filters and the same `UPSTREAM` / `DOWNSTREAM` direction mapping. This additive evidence does not alter `Evidence/closure_summary.json`.

The analyzer emitted `Evidence/closure_summary.json` without a terminal LF. After parsing and before hash pinning, the evidence file received exactly one terminal LF to satisfy the repository's semantic-whitespace convention; SHA-256 lineage is `e0a7680d74cc8eab7a659ca341a5f45b1b48d715c638defbef87833545da4312` to `88e07de9d40a9fa659c10301c1eef28bf48d0cd2ace8b5dcc120d2c38e72d662`, and its parsed JSON values are unchanged.

## DEC-004 — `orphans.csv` interpretation

The analyzer implementation uses `orphans.csv` for deliverables with zero active deliverable-to-deliverable EXECUTION edges. All 112 active deliverable endpoints resolve to one of the 51 discovered deliverables, so there are zero orphan endpoint references. The five rows in `orphans.csv` are therefore reported as isolated deliverables, not unresolved targets.

## DEC-005 — objective-relative graph versus live register graph

The accepted SCA DAG and the live dependency-register graph are distinct derivatives. The accepted DAG preserves E-018, E-020, and E-032 as non-gating objective feedback edges and records the `DECOMPOSE`, `DECOMPOSE`, and `INVERT` moves. The live graph is built only from registered ACTIVE EXECUTION rows and must not invent a feedback row merely to recreate an objective-relative SCC. The one live nine-node SCC is reported independently and is not silently mapped onto any accepted SCA SCC.

## DEC-006 — verdict calibration

The audit returns `WARNINGS`: schema, anchor, evidence, refreshed-register identity, endpoint-resolution, descendant-class, and accepted-ordering checks pass; the live nine-node SCC and five isolated deliverables remain visible warnings. Nothing in the sealed brief declares those findings an automatic blocker, and the audit does not resolve, cut, merge, or linearize the SCC.
