# Decision log — post-Phase-3 graph derivation

## DG-DL-001 — Root dependency source override

The human steer and sealed brief require the authoritative Root
`_DEPENDENCIES.md` declarations, not generic `Dependencies.csv`, and require
this SCA evidence folder rather than an `_Evaluation` pointer. That override
controls this run.

## DG-DL-002 — Objective and edge semantics

The objective is final integration and release-assurance ordering for the
accepted SCA-004 Root carriers. Eight accepted relationships are gating. The
DEL-04-11 validator relationship, package membership, and two App notice/fan-in
edges are non-gating and do not determine SCC ordering.

## DG-DL-003 — Cycle disposition

No non-trivial SCC exists. No decompose, invert, merge, or cut move is needed;
no human-gated decision was made and no cycle was silently linearized.

## DG-DL-004 — Derivative boundary

This graph cites accepted SCA-004 revision 1.3, R7, and the N1/N2 returns. It
must be re-derived after estimates/schedule or any accepted dependency change.
