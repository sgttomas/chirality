import {
  HARNESS_TOOL_REGISTRY_VERSION,
  listHarnessToolDescriptors,
  type HarnessToolDescriptor
} from './tool-descriptor';

const CATALOG_PATH = 'frontend/docs/harness/tool_catalog.md';

function escapeMarkdownTableCell(value: string): string {
  return value.replace(/\|/g, '\\|').replace(/\n/g, '<br>');
}

function joinValues(values: readonly string[]): string {
  return values.length > 0 ? values.join(', ') : 'none';
}

function humanGateSummary(descriptor: HarnessToolDescriptor): string {
  if (!descriptor.humanGate.required) {
    return 'none';
  }
  return `${descriptor.humanGate.gate}: ${descriptor.humanGate.reason}`;
}

function exposedSummary(descriptor: HarnessToolDescriptor): string {
  return `${descriptor.runtime.exposedToModel ? 'yes' : 'no'}: ${descriptor.runtime.reason}`;
}

function modeSummary(descriptor: HarnessToolDescriptor): string {
  if (descriptor.surface === 'reserved') {
    return 'reserved / future policy';
  }
  if (descriptor.name === 'agent') {
    return 'subagent bridge gate';
  }
  if (
    descriptor.permissions.includes('workspace-write') ||
    descriptor.permissions.includes('shell')
  ) {
    return 'workspaceWrite';
  }
  return 'readOnly, workspaceWrite';
}

function hookRequirementSummary(descriptor: HarnessToolDescriptor): string {
  if (descriptor.surface === 'chirality-mcp') {
    if (descriptor.permissions.includes('workspace-write')) {
      return 'Handler-level permission/evidence wrapper; project-root path policy; redaction; event logging. SDK canUseTool and hooks do not auto-fire for raw in-process MCP calls.';
    }
    return 'Descriptor allow-list; project-root containment in handler; result budget; redaction; event logging.';
  }

  if (descriptor.surface === 'reserved') {
    return 'Not exposed; future policy must define permission, hook, path, redaction, and event requirements before activation.';
  }

  if (descriptor.name === 'agent') {
    return 'Special case: descriptor remains not exposed by default; buildSdkOptions may add Agent only when the governed subagent bridge allows it.';
  }

  if (descriptor.permissions.includes('shell')) {
    return 'canUseTool permission overlay; PreToolUse and PostToolUse hooks; shell timeout/no-network policy; redaction; event logging.';
  }

  if (descriptor.permissions.includes('workspace-write')) {
    return 'canUseTool permission overlay; PreToolUse and PostToolUse hooks; project-root path policy; redaction; diff/evidence logging.';
  }

  return 'canUseTool permission overlay; PreToolUse and PostToolUse evidence hooks; project-root read policy; result budget.';
}

function adapterName(descriptor: HarnessToolDescriptor): string {
  return descriptor.adapter.claudeAgentSdk?.toolName ?? 'none';
}

function renderDescriptorRow(descriptor: HarnessToolDescriptor): string {
  const values = [
    descriptor.name,
    adapterName(descriptor),
    descriptor.description,
    descriptor.surface,
    joinValues(descriptor.permissions),
    descriptor.pathScope,
    modeSummary(descriptor),
    descriptor.idempotence,
    descriptor.concurrency,
    humanGateSummary(descriptor),
    hookRequirementSummary(descriptor),
    exposedSummary(descriptor)
  ];
  return `| ${values.map(escapeMarkdownTableCell).join(' | ')} |`;
}

export function renderHarnessToolCatalog(): string {
  const descriptors = listHarnessToolDescriptors();
  const rows = descriptors.map(renderDescriptorRow).join('\n');
  return `# Harness Tool Catalog

**Status:** Generated governance/runtime support artifact
**Registry version:** \`${HARNESS_TOOL_REGISTRY_VERSION}\`
**Source:** \`frontend/src/lib/harness/tool-descriptor.ts\`
**Regenerate:** \`npm run harness:generate-tool-catalog\`

This catalog is generated from \`HARNESS_TOOL_DESCRIPTORS\`. Do not edit
\`${CATALOG_PATH}\` by hand; update the descriptor registry and regenerate it. It is
derivative documentation for the local/in-process tool boundary and does not expose new
capability, change provider scope, or create release/professional approval.

## Naming Boundary

Chirality-owned in-process MCP tools use \`mcp__chirality__*\` adapter names. The future
\`mcp__chirality__domain_*\` namespace is reserved for governed domain-profile tools and
must not be implemented or exposed before the future domain-profile amendment.

SDK built-in tool names and Chirality MCP adapter names are collision-checked by the
descriptor registry tests. Unknown tools remain rejected before streaming.

## Exposure Note

\`Agent\` is a special case: the descriptor remains not exposed by default, and
\`buildSdkOptions\` may add the SDK \`Agent\` tool only when the governed subagent bridge is
present and explicitly allows executable delegation.

## Catalog

| Name | Adapter name | Description | Surface | Permissions | Path scope | Modes | Idempotence | Concurrency | Human gate | Hook requirements | Exposed to model |
|---|---|---|---|---|---|---|---|---|---|---|---|
${rows}
`;
}
