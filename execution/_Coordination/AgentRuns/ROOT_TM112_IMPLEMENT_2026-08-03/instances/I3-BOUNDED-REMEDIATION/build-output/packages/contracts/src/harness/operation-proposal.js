/**
 * `OperationProposal` — inert source-type mirror of the framework-root domain-engine
 * persona's "Valid Operation Proposal" section (20-field table).
 *
 * Mirror source (canonical per D-T0-01):
 * `agents/AGENT_DOMAIN_ENGINE.md@77a327727605f05da5f304288f1ddd87dc09659d`.
 * App-dev conformance mirror: `docs/TYPES.md` §11.2 (20-field table).
 * Lifecycle and risk-class enums mirror
 * `tools/validation/validate_domain_engine_profile.py` (same contract-source pin);
 * the lifecycle tuple order is contractual.
 *
 * Types + type guards only (D-APP-49 O-A, riders 1-2): no runtime behavior beyond the
 * guards, no persistence, no UI, no I/O, no imports. A proposal remains non-binding
 * project evidence until deterministic checks, required human gates, and
 * domain-engine-controlled apply or external terminal acceptance records exist
 * (K-DOMAIN-3); nothing here accepts, applies, or transitions a proposal.
 */
/**
 * Order-exact canonical proposal lifecycle
 * (`validate_domain_engine_profile.py` `OPERATION_LIFECYCLE_VALUES`). `accepted` and
 * `applied` require a human approval record bound to a git SHA per K-AUTH-2 and, where
 * the engine has a terminal human-accepted lifecycle state, that external record.
 */
export const OPERATION_PROPOSAL_LIFECYCLE_STATES = [
    'draft',
    'ready_for_review',
    'accepted',
    'rejected',
    'applied'
];
/**
 * Canonical operation risk classes
 * (`validate_domain_engine_profile.py` `OPERATION_RISK_CLASS_VALUES`). Use
 * `engine_silent` when correctness depends on judgment values or premises the engine
 * cannot independently verify.
 */
export const OPERATION_PROPOSAL_RISK_CLASSES = ['engine_checkable', 'engine_silent'];
/**
 * Constant proposal-only status classification (`docs/TYPES.md` §11.2 `status`);
 * `lifecycle` carries review and application progression.
 */
export const OPERATION_PROPOSAL_STATUS = 'proposal_only';
const OPERATION_PROPOSAL_LIFECYCLE_STATE_SET = new Set(OPERATION_PROPOSAL_LIFECYCLE_STATES);
const OPERATION_PROPOSAL_RISK_CLASS_SET = new Set(OPERATION_PROPOSAL_RISK_CLASSES);
function isRecord(value) {
    return typeof value === 'object' && value !== null && !Array.isArray(value);
}
function isNonEmptyString(value) {
    return typeof value === 'string' && value.trim().length > 0;
}
function isStringList(value) {
    return Array.isArray(value) && value.every(isNonEmptyString);
}
export function isOperationProposalLifecycleState(value) {
    return typeof value === 'string' && OPERATION_PROPOSAL_LIFECYCLE_STATE_SET.has(value);
}
export function isOperationProposalRiskClass(value) {
    return typeof value === 'string' && OPERATION_PROPOSAL_RISK_CLASS_SET.has(value);
}
export function isOperationProposalStatus(value) {
    return value === OPERATION_PROPOSAL_STATUS;
}
export function isOperationProposal(value) {
    if (!isRecord(value)) {
        return false;
    }
    return (isNonEmptyString(value.proposal_id) &&
        isNonEmptyString(value.profile_id) &&
        isNonEmptyString(value.base_state) &&
        isNonEmptyString(value.operation_name) &&
        isOperationProposalStatus(value.status) &&
        isOperationProposalLifecycleState(value.lifecycle) &&
        isNonEmptyString(value.created_at) &&
        isNonEmptyString(value.created_by) &&
        isStringList(value.input_refs) &&
        isStringList(value.intended_changes) &&
        isStringList(value.deterministic_checks) &&
        isStringList(value.expected_output_refs) &&
        isStringList(value.risks) &&
        isStringList(value.assumptions) &&
        isStringList(value.blockers) &&
        isNonEmptyString(value.boundary_notice) &&
        isNonEmptyString(value.required_human_gate) &&
        isOperationProposalRiskClass(value.operation_risk_class) &&
        isNonEmptyString(value.provenance_on_judgment_values) &&
        isNonEmptyString(value.storage_path));
}
