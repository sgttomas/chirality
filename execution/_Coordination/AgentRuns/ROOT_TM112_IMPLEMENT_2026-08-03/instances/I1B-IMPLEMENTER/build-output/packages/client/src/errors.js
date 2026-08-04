import { RUNTIME_ERROR_CODES, RuntimeError } from "@chirality/runtime-contracts";
const runtimeErrorCodes = new Set(RUNTIME_ERROR_CODES);
export class RuntimeTransportError extends Error {
    cause;
    constructor(message, cause) {
        super(message);
        this.name = "RuntimeTransportError";
        if (cause !== undefined)
            this.cause = cause;
    }
}
export function runtimeErrorFromResponse(status, value) {
    if (typeof value === "object" &&
        value !== null &&
        typeof value.error === "object" &&
        value.error !== null) {
        const error = value.error;
        const code = runtimeErrorCodes.has(error.code)
            ? error.code
            : "INTERNAL_FAILURE";
        return new RuntimeError(code, typeof error.message === "string"
            ? error.message
            : `Runtime request failed with HTTP ${status}`, status, error.details);
    }
    return new RuntimeError("INTERNAL_FAILURE", `Runtime request failed with HTTP ${status}`, status);
}
