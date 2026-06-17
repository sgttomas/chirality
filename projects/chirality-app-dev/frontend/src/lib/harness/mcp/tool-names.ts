export const CHIRALITY_MCP_SERVER_NAME = 'chirality';

export const CHIRALITY_MCP_READ_TOOL_NAMES = [
  'status_read',
  'deps_read',
  'scope_scan',
  'scaffold_preview'
] as const;

export const CHIRALITY_MCP_MUTATING_TOOL_NAMES = [
  'status_transition',
  'deps_write'
] as const;

export type ChiralityMcpReadToolName = (typeof CHIRALITY_MCP_READ_TOOL_NAMES)[number];
export type ChiralityMcpMutatingToolName = (typeof CHIRALITY_MCP_MUTATING_TOOL_NAMES)[number];
export type ChiralityMcpToolName = ChiralityMcpReadToolName | ChiralityMcpMutatingToolName;

export type ChiralityMcpAllowedToolName =
  `mcp__${typeof CHIRALITY_MCP_SERVER_NAME}__${ChiralityMcpToolName}`;

export const CHIRALITY_MCP_TOOL_NAMES = [
  ...CHIRALITY_MCP_READ_TOOL_NAMES,
  ...CHIRALITY_MCP_MUTATING_TOOL_NAMES
] as const satisfies readonly ChiralityMcpToolName[];

export const CHIRALITY_MCP_ALLOWED_TOOL_NAMES = CHIRALITY_MCP_TOOL_NAMES.map(
  (toolName) => `mcp__${CHIRALITY_MCP_SERVER_NAME}__${toolName}` as ChiralityMcpAllowedToolName
) as readonly ChiralityMcpAllowedToolName[];

const CHIRALITY_MCP_ALLOWED_TOOL_NAME_SET = new Set<string>(
  CHIRALITY_MCP_ALLOWED_TOOL_NAMES
);

export function toChiralityMcpAllowedToolName(
  toolName: ChiralityMcpToolName
): ChiralityMcpAllowedToolName {
  return `mcp__${CHIRALITY_MCP_SERVER_NAME}__${toolName}`;
}

export function isChiralityMcpAllowedToolName(
  toolName: string
): toolName is ChiralityMcpAllowedToolName {
  return CHIRALITY_MCP_ALLOWED_TOOL_NAME_SET.has(toolName);
}
