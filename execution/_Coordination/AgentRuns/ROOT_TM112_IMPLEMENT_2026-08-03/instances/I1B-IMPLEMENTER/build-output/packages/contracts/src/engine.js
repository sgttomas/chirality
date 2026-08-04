export function asHarnessSession(input, existing) {
    return {
        ...existing,
        sessionId: input.sessionId,
        projectRoot: input.projectRoot,
        engineSelection: input.selection,
        agentType: input.role === "agent0" ? 0 : input.role === "agent1" ? 1 : 2
    };
}
