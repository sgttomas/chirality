# SCOPE_CHANGE launch brief — SCA-004 Gate 4 propagation plan

RequestedBy: HELP_HUMAN
RunID: PEC-DPEC77-78-20260802
InstanceID: scope-change-sca004-gate4
AmendmentID: SCA-004
DecompVariant: SOFTWARE

## Owner Gate 3 authority

Ryan Tufts, in-session, 2026-08-03:

> SCA-004 Gate 3: APPROVE the exact amendments in Amendment_Preview.md
> (SHA-256
> 4a473ca087ba4f0fa63cc98432165ec46a819a36f22c9ab44f3c98778dae245f).
> SCOPE_CHANGE may prepare the Gate 4 propagation plan only; no live
> decomposition edit, pointer move, or downstream repair is authorized.

## Objective

Prepare only the Gate 4 propagation plan for the exact approved SCA-004
postimage. Follow `agents/AGENT_SCOPE_CHANGE.md` Gate 4 and preserve every
boundary and derivative classification already established in the Gate 2
impact assessment and Gate 3 preview.

The plan must distinguish:

- exact Gate 5 authoritative decomposition writes approved at Gate 3;
- variant-local metadata writes that would require a later Gate 4 owner
  approval before Gate 5;
- separately owned downstream repairs/reruns that SCOPE_CHANGE must not
  execute; and
- closure validation required after a future Gate 5 execution.

It must enumerate the DEL-01-06 `_CONTEXT.md` semantic delta, the remaining
63 context provenance re-pins, all 64 reference re-pins, the SOW-077
non-gating requirement anchor, four ScopeOfWork contract-currency reviews,
the DEL-00-03 accepted-SPEC amendment gate, snapshot/pointer materialization,
post-change audit, and ordinary PEC mapping refresh without describing any as
already authorized or complete.

## Required context

- `agents/AGENT_SCOPE_CHANGE.md`
- complete SCA-004 interim package
- approved `Amendment_Preview.md` at the exact SHA above
- accepted Gate 2 impact assessment SHA-256
  `df366142e47063b452e43fc90958b839bba6ab0709f556f336e32d52e9556661`
- accepted decomposition revision 1.3 and its exact companion-register bytes
- relevant downstream metadata/contracts in read-only mode

## Write scope

Only:

- `projects/pec/execution/_ScopeChange/SCA-004_2026-08-02_2325/Propagation_Plan.md`;
- `projects/pec/execution/_ScopeChange/SCA-004_2026-08-02_2325/Amendment_Actions.csv`;
- an optional Gate 4 handoff/validation record in that same interim package;
- this instance's `RETURN.md` and `STATUS.json`.

No live decomposition, companion register, pointer, `_CONTEXT.md`,
`_REFERENCES.md`, `Dependencies.csv`, ScopeOfWork, accepted SPEC, source,
lifecycle, Task Management, decision, receipt, foreign-loop, downstream, or
snapshot write is authorized.

## Return contract

Return the exact plan and action-register hashes, a complete write-owner and
rerun matrix, containment/validation results, and the next owner question:

“Do you approve this SCA-004 propagation plan for later Gate 5 execution?”

No Gate 5 act or acceptance is inferred.
