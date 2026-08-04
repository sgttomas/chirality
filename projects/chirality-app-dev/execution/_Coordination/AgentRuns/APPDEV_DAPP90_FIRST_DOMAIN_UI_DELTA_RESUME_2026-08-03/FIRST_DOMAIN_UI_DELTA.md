# Exact First-Domain UI Delta Inventory — Piping

State: `COMPLETE AS DERIVATIVE PLANNING EVIDENCE — NOT PRODUCT AUTHORITY`

Qualifying input: committed response Git blob
`a71145ec0952cc5ad62b1b12635be44deebffbd3`, SHA-256
`e38c5614351ce45d77535c4bb234580bbbb1916a68a482660b6c3f4e230235e7`.

## Delta contract

The Piping per-domain control plane needs six minimum conceptual modules. This
is the exact affected set `U`; each item counts once in the structural
migration index regardless of A/B/C placement.

| U ID | Required App presentation or evidence module | Exact Piping semantics carried | Evidence |
|---|---|---|---|
| U-01 | `PipingNavigationWorkspaceDescriptor` | Domain navigation over model tree, viewport, properties, operations, loads, libraries, rule packs, solve, results/comparison, reports, project storage, export, and evidence/boundary surfaces. | E-03 |
| U-02 | `PipingStructuredInformationView` | Read-only presentation of model/state/run/result identities and hashes, diagnostics, units/dimensions, mapping and tolerance-profile references, audit/provenance, redaction, and explicit unsupported/incompatible/missing states. | E-03, E-11, E-13, E-17, E-18, E-19, E-21 |
| U-03 | `PipingWorkflowView` | Structured-operation validate/apply flow and solve-job start/progress/cancel/failure/result flow; partial/cancelled results never silently become final; browser fixtures never evidence authoritative success. | E-04, E-05, E-06, E-08, E-10, E-11, E-13 |
| U-04 | `PipingDecisionGateView` | Show deterministic diff, validation/diagnostics, model basis, professional-boundary fields, and an explicit human acceptance act before retaining a new model document. Agent proposals remain review-only and cannot auto-accept. | E-05, E-07, E-08, E-09, E-10, E-11 |
| U-05 | `PipingTypedAgentReviewView` | Present typed proposal identity, validation, audit/provenance, rationale/boundary state, capability denial/unavailability, and relation to the operation-review ledger. It presents no operative application-agent runtime because none exists. | E-07, E-09, E-11, E-12, E-14 |
| U-06 | `PipingUiAgentConformanceProfile` | Evidence mapping for read, edit, job, security, comparison, and claims equivalence across human UI/service seams and agent/API seams. Current CLI operations and draft API are represented accurately; TBD transport/runtime and absent orchestrator remain unavailable/fail-closed. | E-03, E-05, E-07, E-08, E-10, E-11, E-12, E-13, E-14, E-16, E-17, E-18, E-19, E-21 |

Therefore `U = {U-01, U-02, U-03, U-04, U-05, U-06}` and `|U| = 6`.

## Common presentation states

Each U item must distinguish available, unavailable, stale, conflict,
empty, permission-denied, blocked, cancelled, partial, failed, and succeeded
where applicable. Evidence/source references and Piping-owned identities stay
visible. No state may upgrade solver mechanics, comparison, rule-check,
proposal, or handoff output into human/professional acceptance.

## Slot binding by architecture candidate

| U item | A — profile field/module | B — domain-shell composition | C — closed build-time slot/adapter |
|---|---|---|---|
| U-01 | profile navigation/workspace descriptor | Piping shell navigation/workspace composer | `NavigationSlot` adapter |
| U-02 | structured-information module ref | domain information panel over shared record components | `InformationSlot` adapter |
| U-03 | workflow module ref | domain operation/job workflow composer | `WorkflowSlot` adapter |
| U-04 | decision-gate module ref | domain gate panel using shared guarded-action primitives | `DecisionGateSlot` adapter |
| U-05 | typed-agent review module ref | domain proposal-review panel using shared projection primitives | `TypedAgentSlot` adapter |
| U-06 | validation/conformance profile ref | shared-core conformance fixtures plus both shell consumers | build-target conformance profile over closed adapters |

The response supplies no product icon, color/token scheme, App navigation
order, actual bundle/data identity, executable name, route URL, or runtime
contract. Those remain later App/Root owner gates and are not invented here.

## Non-effects

These modules are derivative planning nodes, not files to create and not
accepted product requirements. They do not define Piping domain truth, grant
tools, expose Agent-2 Bash, select provider/network or generic runtime
semantics, accept an agent proposal, mutate a model, or make a professional
claim.
