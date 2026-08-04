import { RuntimeError } from "@chirality/runtime-contracts";
export class CompatibilitySessionPolicy {
    options;
    constructor(options) {
        this.options = options;
    }
    async resolve(input) {
        const env = this.options.env ?? process.env;
        const explicit = env.CHIRALITY_HARNESS_PROVIDER?.trim().toLowerCase();
        const available = new Set(this.options.availableAdapterIds());
        const configured = (await this.options.credentials.status("anthropic")).configured;
        let adapterId;
        let providerId;
        if (explicit === "agentsdk" || explicit === "agent-sdk" || explicit === "claude-agent-sdk") {
            adapterId = "claude-agent-sdk";
            providerId = "anthropic";
        }
        else if (explicit === "anthropic") {
            adapterId = "anthropic-direct";
            providerId = "anthropic";
        }
        else if (explicit === "stub") {
            adapterId = "stub";
            providerId = "stub";
        }
        else {
            adapterId = configured ? "claude-agent-sdk" : "stub";
            providerId = configured ? "anthropic" : "stub";
        }
        if (!available.has(adapterId)) {
            throw new RuntimeError("ENGINE_UNAVAILABLE", `Default engine adapter is unavailable: ${adapterId}`, 503);
        }
        return {
            role: input.agentType === 0 ? "agent0" : "agent1",
            engineSelection: {
                adapterId,
                providerId,
                model: env.CHIRALITY_GLOBAL_MODEL?.trim() || "haiku"
            }
        };
    }
}
