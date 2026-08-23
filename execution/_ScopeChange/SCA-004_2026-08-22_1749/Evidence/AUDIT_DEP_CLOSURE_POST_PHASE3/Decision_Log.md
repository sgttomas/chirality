# Decision log — post-Phase-3 dependency closure

## DC-P3-DL-001 — Output and source override

The human steer and sealed brief override the dedicated agent defaults: this
run writes only the named SCA evidence folder, does not update an `_Evaluation`
pointer, and consumes authoritative Root `_DEPENDENCIES.md` rather than generic
`Dependencies.csv`.

## DC-P3-DL-002 — Edge classes

Eight relationships marked gating by accepted dependency truth form the SCC
layer. DEL-04-11's validator relationship and the two cross-loop App
notice/fan-in edges remain non-gating and cannot confer foreign authority.

## DC-P3-DL-003 — Cycle disposition

No non-trivial SCC exists. No decompose, invert, merge, or cut move is needed;
no human-gated decision was made and no edge was silently linearized.

## DC-P3-DL-004 — Coverage warning

All seven SCA-004 carriers have moved from initialized-empty declarations to
grounded Phase-3 extraction, so the Phase-1 warning is cleared. Forty-five
legacy Root containers remain `NOT_RUN_YET`; that broader coverage gap is
preserved as a warning and is not misreported as a closure violation.

## DC-P3-DL-005 — Derivative boundary

This package cites accepted SCA-004 revision 1.3, R7, and N1/N2 outputs. It
must be regenerated after estimates/schedule or any accepted dependency change.
