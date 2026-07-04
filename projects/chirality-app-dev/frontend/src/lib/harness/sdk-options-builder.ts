import type { Options, PermissionMode, SettingSource } from '@anthropic-ai/claude-agent-sdk';
import { createChiralityToolHooks } from './chirality-hooks';
import { ContentBlock, ResolvedOpts, SessionRecord } from '@chirality/harness-contract/types';
import {
  createHarnessCanUseTool,
  normalizeHarnessPermissionMode
} from './permission-overlay';
import { getPermissionBroker } from './permission-broker';
import { getPermissionEventChannel } from './permission-event-channel';
import { resolveHarnessToolPool } from './tool-pool';
import { getHarnessToolDescriptor } from '@chirality/harness-contract/tool-descriptor';
import {
  createChiralityMcpServers,
  filterChiralityMcpAllowedToolNames
} from './mcp/read-tools';
import { createScriptedAgentSdkProofSpawn } from './scripted-agent-sdk-proof';
import { createExecutableSubagentBridge } from './subagent-bridge';

export type SdkProbeOptions = Options & {
  settingSources: SettingSource[];
};

function parseSettingSources(raw: string | undefined): SettingSource[] {
  if (!raw || raw.trim().length === 0) {
    return [];
  }

  const requested = raw
    .split(',')
    .map((item) => item.trim())
    .filter(Boolean);

  if (requested.length === 1 && requested[0] === 'project') {
    return ['project'];
  }

  return [];
}

function mapPermissionMode(mode: string): PermissionMode {
  const normalizedMode = normalizeHarnessPermissionMode(mode);
  if (normalizedMode === 'readOnly' || normalizedMode === 'dontAsk') {
    return 'dontAsk';
  }
  if (normalizedMode === 'workspaceWrite') {
    return 'acceptEdits';
  }
  if (
    normalizedMode === 'bypass' &&
    process.env.CHIRALITY_ALLOW_SDK_BYPASS === '1'
  ) {
    return 'bypassPermissions';
  }
  return 'default';
}

function contentBlocksToPrompt(message: string, contentBlocks?: ContentBlock[]): string {
  if (!contentBlocks || contentBlocks.length === 0) {
    return message;
  }

  const attachmentSummary = contentBlocks
    .map((block) => {
      if (block.type === 'text') {
        return block.text;
      }
      return `[Attachment: ${block.path} (${block.mimeType})]`;
    })
    .join('\n\n');

  return [message, attachmentSummary].filter((part) => part.trim().length > 0).join('\n\n');
}

export function buildSdkPrompt(message: string, contentBlocks?: ContentBlock[]): string {
  return contentBlocksToPrompt(message, contentBlocks);
}

function requestedAgentTool(toolNames: readonly string[]): boolean {
  return toolNames.some((toolName) => getHarnessToolDescriptor(toolName)?.name === 'agent');
}

export function buildSdkOptions(input: {
  session: SessionRecord;
  opts: ResolvedOpts;
  abortController: AbortController;
  systemPrompt: string;
}): SdkProbeOptions {
  const toolPool = resolveHarnessToolPool({
    sessionId: input.session.sessionId,
    requestedTools: input.opts.tools,
    mode: input.opts.mode
  });
  const subagentBridge = createExecutableSubagentBridge({
    session: input.session,
    opts: input.opts
  });
  const allowExecutableAgent = Boolean(subagentBridge && requestedAgentTool(input.opts.tools));
  const allowedToolNames = allowExecutableAgent
    ? [...toolPool.allowedToolNames, 'Agent' as const]
    : [...toolPool.allowedToolNames];
  const disallowedToolNames = allowExecutableAgent
    ? toolPool.disallowedToolNames.filter((toolName) => toolName !== 'Agent')
    : [...toolPool.disallowedToolNames];
  const allowedChiralityMcpToolNames = filterChiralityMcpAllowedToolNames(allowedToolNames);
  const scriptedAgentSdkProofSpawn = createScriptedAgentSdkProofSpawn();

  return {
    abortController: input.abortController,
    agents: subagentBridge?.agents,
    cwd: input.session.projectRoot,
    model: input.opts.model,
    maxTurns: input.opts.maxTurns,
    permissionMode: mapPermissionMode(input.opts.mode),
    tools: allowedToolNames,
    allowedTools: allowedToolNames,
    disallowedTools: disallowedToolNames,
    canUseTool: createHarnessCanUseTool({
      sessionId: input.session.sessionId,
      mode: input.opts.mode,
      projectRoot: input.session.projectRoot,
      delegatedSubagents: subagentBridge?.delegatedSubagents,
      resolveDescriptor: getHarnessToolDescriptor,
      requestHumanDecision: ({ sessionId, toolUseId }) =>
        getPermissionBroker().request({
          sessionId,
          toolUseId,
          // The turn's AbortController is its identity, so teardown can scope the
          // clear to this turn and not deny a newer same-session turn's approvals.
          turnToken: input.abortController
        }).verdict,
      publishEvent: (event) =>
        getPermissionEventChannel().publish(input.session.sessionId, event)
    }),
    hooks: createChiralityToolHooks({
      sessionId: input.session.sessionId,
      projectRoot: input.session.projectRoot,
      delegatedSubagents: subagentBridge?.delegatedSubagents,
      resolveDescriptor: getHarnessToolDescriptor
    }),
    mcpServers: createChiralityMcpServers({
      context: {
        projectRoot: input.session.projectRoot,
        sessionId: input.session.sessionId
      },
      allowedToolNames: allowedChiralityMcpToolNames,
      mode: input.opts.mode
    }),
    resume: input.session.sdkSessionId,
    settingSources: parseSettingSources(process.env.CHIRALITY_SDK_SETTING_SOURCES),
    systemPrompt: {
      type: 'preset',
      preset: 'claude_code',
      append: input.systemPrompt
    },
    ...(scriptedAgentSdkProofSpawn
      ? { spawnClaudeCodeProcess: scriptedAgentSdkProofSpawn }
      : {})
  };
}
