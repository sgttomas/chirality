# Root objective-relative work graph — post-Phase 3

Status: `DERIVATIVE_CURRENT_POST_DEPENDENCY_EXTRACTION`

## Basis and objective

This derivative graph is grounded in accepted SCA-004 revision 1.3, R7-A,
N1 lifecycle initialization, and N2's authoritative `_DEPENDENCIES.md`
extraction. It contains the exact 53 register deliverables plus six package
nodes. It does not replace decomposition or deliverable-local dependency truth.

Objective: final integration and release-assurance ordering for the accepted
SCA-004 Root carriers.

## Gating dependency layer

```text
DEL-02-07_Process_Supervisor_and_Purpose_Limited_Control --EVIDENCE_FAN_IN--> DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance
DEL-02-08_Exact_Supply_and_Protocol_Pinning --EVIDENCE_FAN_IN--> DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance
DEL-02-09_Hosted_Account_and_Consent_Boundary --EVIDENCE_FAN_IN--> DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance
DEL-02-10_Adapter_Event_Schema_and_Approval_API_v2 --EVIDENCE_FAN_IN--> DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance
DEL-02-11_Worker_Retirement_Restart_and_Terminal_Reconciliation --EVIDENCE_FAN_IN--> DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance
DEL-02-12_Runtime_Conformance_Evidence_and_Shared_Release_Fan_in --EVIDENCE_FAN_IN--> DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance
DEL-04-05_Root_Governed_Loop_and_Receipt_Discipline --DOCTRINE_INPUT--> DEL-04-11_Root_Loop_Receipt_Validator
DEL-05-02_Snapshot_Handoff_and_Receipt_Discipline --EVIDENCE_CROSSCHECK_INPUT--> DEL-04-11_Root_Loop_Receipt_Validator
```

## Non-gating relationships

```text
DEL-04-11_Root_Loop_Receipt_Validator --VALIDATION_RELATIONSHIP--> DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance
```

The two App coupling relationships are notice/fan-in edges only and are not
foreign authority or part of SCC ordering.

## Structural summary

- Nodes: 59 = 53 deliverables + 6 packages.
- Package-membership edges: 53, structural and non-gating.
- Root relationships: 9 = 8 gating + 1 non-gating.
- Cross-loop notice/fan-in edges: 2, non-gating.
- Strict SCCs: 59 singleton components; non-trivial: 0.
- Human-gated cut/merge required: no.

## Derivative status and rerun

Re-derive this graph after estimates/schedule or any accepted dependency
change. No cycle has been silently linearized; cycle-participating edges
would remain non-gating until their recorded resolution.
