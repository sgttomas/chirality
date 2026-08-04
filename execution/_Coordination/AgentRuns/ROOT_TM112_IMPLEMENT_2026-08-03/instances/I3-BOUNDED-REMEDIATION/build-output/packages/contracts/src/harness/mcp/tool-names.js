export const CHIRALITY_MCP_SERVER_NAME = 'chirality';
export const CHIRALITY_MCP_SERVER_VERSION = '2.0.0';
export const CHIRALITY_MCP_READ_TOOL_NAMES = [
    'status_read',
    'deps_read',
    'scope_scan',
    'scaffold_preview'
];
export const CHIRALITY_MCP_MUTATING_TOOL_NAMES = [
    'status_transition',
    'deps_write'
];
export const CHIRALITY_MCP_DOMAIN_TOOL_NAMES = [
    'domain_completeness_check',
    'domain_rule_check_run',
    'domain_headless_preview_run',
    'domain_propose_operation',
    'domain_proposal_validate'
];
export const CHIRALITY_MCP_COORDINATION_TOOL_NAMES = [
    'delegate_agent',
    'report_coordination_notice',
    'send_agent_update',
    'ack_agent_update'
];
export const CHIRALITY_MCP_TOOL_NAMES = [
    ...CHIRALITY_MCP_READ_TOOL_NAMES,
    ...CHIRALITY_MCP_MUTATING_TOOL_NAMES,
    ...CHIRALITY_MCP_DOMAIN_TOOL_NAMES,
    ...CHIRALITY_MCP_COORDINATION_TOOL_NAMES
];
export const CHIRALITY_MCP_ALLOWED_TOOL_NAMES = CHIRALITY_MCP_TOOL_NAMES.map((toolName) => `mcp__${CHIRALITY_MCP_SERVER_NAME}__${toolName}`);
const CHIRALITY_MCP_ALLOWED_TOOL_NAME_SET = new Set(CHIRALITY_MCP_ALLOWED_TOOL_NAMES);
export function toChiralityMcpAllowedToolName(toolName) {
    return `mcp__${CHIRALITY_MCP_SERVER_NAME}__${toolName}`;
}
export function isChiralityMcpAllowedToolName(toolName) {
    return CHIRALITY_MCP_ALLOWED_TOOL_NAME_SET.has(toolName);
}
