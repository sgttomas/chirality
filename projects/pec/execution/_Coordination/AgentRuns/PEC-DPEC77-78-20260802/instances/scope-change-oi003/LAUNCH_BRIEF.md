# SCOPE_CHANGE launch brief — SOW-077 / OI-003 propagation intake

RequestedBy: HELP_HUMAN
RunID: PEC-DPEC77-78-20260802
InstanceID: scope-change-oi003
DecompVariant: SOFTWARE
ContextRoot: `projects/pec/execution/`
DecompositionPath: `projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md`

## Objective

Process the human-initiated D-PEC-78 O-A product decision into a Gate-1-ready
SCOPE_CHANGE intake for propagating SOW-077/OI-003 from TBD/open to the ruled
PEC-local long-term service-registry decision. Parse the atomic action,
identify the next SCA ID, inspect the accepted current basis and downstream
impact, and return the exact Gate 1 owner interface.

Do not modify decomposition truth, `_LATEST.md`, any prior SCA, deliverable
contract, source, register, or decision record. Gates 1–5 remain human acts.

## Declared reads

D-PEC-78 packet and ruled decision record; PRD §16.3; accepted SOFTWARE_DECOMP
revision 1.3; ScopeLedger row SOW-077; OI-003; SOW-094/DEL-01-06 basis;
current `_ScopeChange/` snapshots and downstream references.

## Allowed write targets

- this instance's `RETURN.md` and `STATUS.json` only

## Return contract

Return next SCA ID, action classification and affected exact fields, baseline
and invariant checks, preliminary impact/derivative classification, open
unknowns, and the Gate 1 question. Do not claim Gate 1 confirmation.
