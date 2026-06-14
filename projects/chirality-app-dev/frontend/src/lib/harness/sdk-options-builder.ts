import type { Options, PermissionMode, SettingSource } from '@anthropic-ai/claude-agent-sdk';
import { ContentBlock, ResolvedOpts, SessionRecord } from './types';
import {
  createHarnessCanUseTool,
  normalizeHarnessPermissionMode
} from './permission-overlay';
import { getHarnessToolDescriptor, resolveHarnessToolPool } from './tool-descriptor';

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
  if (normalizedMode === 'readOnly') {
    return 'plan';
  }
  if (normalizedMode === 'dontAsk') {
    return 'dontAsk';
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

  return {
    abortController: input.abortController,
    cwd: input.session.projectRoot,
    model: input.opts.model,
    maxTurns: input.opts.maxTurns,
    permissionMode: mapPermissionMode(input.opts.mode),
    tools: [],
    allowedTools: [...toolPool.allowedToolNames],
    disallowedTools: [...toolPool.disallowedToolNames],
    canUseTool: createHarnessCanUseTool({
      sessionId: input.session.sessionId,
      mode: input.opts.mode,
      resolveDescriptor: getHarnessToolDescriptor
    }),
    mcpServers: {},
    resume: input.session.sdkSessionId,
    settingSources: parseSettingSources(process.env.CHIRALITY_SDK_SETTING_SOURCES),
    systemPrompt: {
      type: 'preset',
      preset: 'claude_code',
      append: input.systemPrompt
    }
  };
}
