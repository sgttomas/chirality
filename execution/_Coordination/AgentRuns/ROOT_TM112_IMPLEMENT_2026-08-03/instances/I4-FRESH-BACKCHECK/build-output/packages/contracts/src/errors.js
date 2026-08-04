export const RUNTIME_ERROR_CODES = [
    "INVALID_REQUEST",
    "UNAUTHORIZED",
    "FORBIDDEN",
    "NOT_FOUND",
    "PROJECT_NOT_FOUND",
    "PROJECT_MANIFEST_INVALID",
    "PROJECT_MANIFEST_DRIFT",
    "SESSION_NOT_FOUND",
    "SESSION_TURN_IN_PROGRESS",
    "ENGINE_UNAVAILABLE",
    "MODEL_UNAVAILABLE",
    "MODEL_NOT_RESIDENT",
    "RESIDENCY_TRANSITION_IN_PROGRESS",
    "RESIDENCY_DRAIN_TIMEOUT",
    "RESIDENCY_UNMANAGED_CONFLICT",
    "OMLX_AUTHENTICATION_FAILED",
    "OMLX_PROTOCOL_FAILURE",
    "OMLX_UNAVAILABLE",
    "REQUIRED_DELEGATION_MISSING",
    "DELEGATION_POLICY_VIOLATION",
    "INTERRUPTED",
    "INTERNAL_FAILURE"
];
export class RuntimeError extends Error {
    code;
    status;
    details;
    constructor(code, message, status = 400, details) {
        super(message);
        this.name = "RuntimeError";
        this.code = code;
        this.status = status;
        if (details !== undefined)
            this.details = details;
    }
}
