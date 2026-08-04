export const RUNTIME_API_VERSION = "v1";
export const RUNTIME_ROUTES = {
    health: "/v1/health",
    daemonStatus: "/v1/daemon/status",
    projects: "/v1/projects",
    projectRegister: "/v1/projects/register",
    projectStatus: (projectId) => `/v1/projects/${encodeURIComponent(projectId)}/status`,
    sessions: (projectId) => `/v1/projects/${encodeURIComponent(projectId)}/sessions`,
    session: (projectId, sessionId) => `/v1/projects/${encodeURIComponent(projectId)}/sessions/${encodeURIComponent(sessionId)}`,
    sessionBoot: (projectId, sessionId) => `${RUNTIME_ROUTES.session(projectId, sessionId)}/boot`,
    sessionReplay: (projectId, sessionId) => `${RUNTIME_ROUTES.session(projectId, sessionId)}/replay`,
    sessionTurn: (projectId, sessionId) => `${RUNTIME_ROUTES.session(projectId, sessionId)}/turn`,
    sessionInterrupt: (projectId, sessionId) => `${RUNTIME_ROUTES.session(projectId, sessionId)}/interrupt`,
    sessionPermission: (projectId, sessionId) => `${RUNTIME_ROUTES.session(projectId, sessionId)}/permission`,
    agents: (projectId) => `/v1/projects/${encodeURIComponent(projectId)}/agents`,
    scaffold: (projectId) => `/v1/projects/${encodeURIComponent(projectId)}/scaffold`,
    runs: (projectId) => `/v1/projects/${encodeURIComponent(projectId)}/runs`,
    models: "/v1/models",
    modelActivate: (modelId) => `/v1/models/${encodeURIComponent(modelId)}/activate`,
    credentials: (providerId) => `/v1/credentials/${encodeURIComponent(providerId)}`
};
