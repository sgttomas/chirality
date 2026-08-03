# TASK_MANAGEMENT launch brief — TM-PEC-010 ruling effect

RequestedBy: HELP_HUMAN
RunID: PEC-DPEC77-78-20260802
InstanceID: task-management-tmpec010
InvokingLoop: PEC
RegisterHome: `_DomainEngines/pec/_TaskManagement/`
Mode: owner-ruled resolution assessment / row maintenance

## Objective

Run the mandatory invocation-local federation preflight, evaluate the exact
D-PEC-78 O-A ruling against TM-PEC-010, and determine whether the human act is
sufficient for `CLOSED / RESOLVED_BY_DECISION` at exact evidence. Verify
TM-PEC-009 remains DEFERRED with its trigger unchanged.

If K-TM-3 permits closure on the exact selected packet effect, update only the
PEC register row, archive mechanically with `taskmgmt archive`, validate live
and closed registers, and return evidence. If explicit Task Management
disposition is still required, write no row and return a decision-ready
proposal stating why.

## Authority and evidence

Owner ruling `D-PEC-78: O-A`; presentation packet SHA-256
`426dba045d63136937eec25af6e4842188ac402486f400391f1f30e1f33e5d17`;
ruled D-PEC-78 decision record in the live tree.

## Allowed write targets

- `_DomainEngines/pec/_TaskManagement/REGISTER.csv`
- `_DomainEngines/pec/_TaskManagement/REGISTER_CLOSED.csv`
- a clearly labeled resolution report under `_DomainEngines/pec/_TaskManagement/`
- this instance's `RETURN.md` and `STATUS.json`

Do not write the PEC loop receipt, D-PEC records, SCOPE_CHANGE surfaces, or
any foreign register. HELP_HUMAN owns shared closeout integration.
