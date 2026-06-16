# Gate 3 — Category Proposal (chirality-app-dev)

**Status:** PROPOSED — awaiting human Gate-3 confirmation.

## Method
Faithful-to-author reconciliation (operator directive). Categories reconcile the
cross-source TOC structures: the 11 author packages PKG-00..10 are preserved 1:1,
plus 5 cross-cutting categories for the docs/, governance, and frontend bodies.
Assignment is deterministic **source-routing** (gate3_assign.py, rules G3BR-001..007):
each IN atom inherits the category owning its author-placed PKG / source group.
No atom splits, no UnitStatement/ContentHash edits (lossless).

## Result
- 16 flat categories; **11,140 IN atoms** assigned (exactly one each); 562 TBD and
  107 OUT left uncategorized (TBD deferred per OI-013).
- Binding retrieval ratification (gate3_ratify.py) over the dense V2 index
  (`SRCIDX_20260616T043733Z`, BAAI/bge-base-en-v1.5):
  **16/16 CLUSTER_COHERENT, 0 blocking.** Own-centroid cosine median 0.71–0.77
  (every category is a tight, separable content cluster; ~7.5x the 1/16 random
  baseline). Scope-query cosine + BM25 retained as diagnostics (0.75 human-gated,
  G3BR-012).
- **330 misassignment candidates** (2.96% of IN atoms) — atoms whose nearest
  content centroid is a *different* category by margin >0.05. These are semantic
  adjacencies (e.g. PRD atoms near the runtime/domain-engine features they specify;
  frontend-code atoms near the agent/runtime logic they implement), correctly
  disambiguated by author document-of-origin. Proposed resolution:
  RESOLVE_SOURCE_ROUTING (retain by author placement) — pending operator confirmation.

## Integrity
`validate_domain_decomposition_integrity.py`: 4 CRITICAL findings, all
expected-absent future-gate annexes (knowledge_types/subjects → Gate 4,
objectives → Gate 4/5, coverage → Gate 5). No Gate-3 (category/ledger) integrity
problem.

## Drift note (OI-011)
A handful of categories include atoms from sources that drifted post-intake
(re-stamped, re-atomization deferred): CAT-012/013 (docs/PLAN, README,
VALIDATION_STRATEGY, AGENTIC_DEVELOPMENT_WORKFLOW), CAT-016 (frontend harness
code), CAT-014/015 (_Coordination/_REGISTER, runtime_engine_contract). Category
assignment is robust to this; flagged for the pre-Gate-6 reconciliation.
