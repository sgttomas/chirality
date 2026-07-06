import { mkdir, mkdtemp, rm } from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import { afterEach, describe, expect, it, vi } from 'vitest';
import { buildSdkOptions } from '../../lib/harness/sdk-options-builder';
import {
  getPermissionBroker,
  resetPermissionBrokerForTests
} from '../../lib/harness/permission-broker';
import type { ResolvedOpts, SessionRecord } from '@chirality/harness-contract/types';

/** Wait until the broker has registered a pending request for the session. */
async function waitForPending(sessionId: string): Promise<void> {
  for (let attempt = 0; attempt < 100; attempt += 1) {
    if (getPermissionBroker().pendingCount(sessionId) >= 1) {
      return;
    }
    await new Promise((resolve) => setTimeout(resolve, 5));
  }
  throw new Error('Timed out waiting for a pending permission request');
}

const session: SessionRecord = {
  sessionId: 'sess_1',
  projectRoot: '/tmp/project',
  persona: 'WORKING_ITEMS',
  mode: 'direct',
  createdAt: '2026-02-23T00:00:00.000Z',
  updatedAt: '2026-02-23T00:00:00.000Z',
  sdkSessionId: 'sdk_resume'
};

const opts: ResolvedOpts = {
  model: 'claude-test',
  tools: ['read', 'write', 'bash'],
  maxTurns: 3,
  persona: 'WORKING_ITEMS',
  mode: 'direct'
};

const LIVE_DOMAIN_MCP_TOOL_NAMES = [
  'mcp__chirality__domain_completeness_check',
  'mcp__chirality__domain_rule_check_run'
] as const;

const PARKED_DOMAIN_MCP_TOOL_NAMES = ['mcp__chirality__domain_headless_preview_run'] as const;

// D-APP-52: live pec-scoped proposal tools (write + read grades).
const PEC_PROPOSAL_DOMAIN_MCP_TOOL_NAMES = [
  'mcp__chirality__domain_propose_operation',
  'mcp__chirality__domain_proposal_validate'
] as const;

const DOMAIN_MCP_TOOL_NAMES = [
  ...LIVE_DOMAIN_MCP_TOOL_NAMES,
  ...PARKED_DOMAIN_MCP_TOOL_NAMES,
  ...PEC_PROPOSAL_DOMAIN_MCP_TOOL_NAMES
] as const;

let tmpDir = '';

afterEach(async () => {
  vi.unstubAllEnvs();
  resetPermissionBrokerForTests();
  delete process.env.CHIRALITY_SDK_SETTING_SOURCES;
  delete process.env.CHIRALITY_ALLOW_SDK_BYPASS;
  delete process.env.CHIRALITY_INSTRUCTION_ROOT;
  delete process.env.CHIRALITY_AGENTSDK_SCRIPTED_PROOF;
  if (tmpDir) {
    await rm(tmpDir, { recursive: true, force: true });
    tmpDir = '';
  }
});

describe('buildSdkOptions', () => {
  it('defaults to SDK settings isolation and exposes only requested read-class tools', () => {
    const options = buildSdkOptions({
      session,
      opts,
      abortController: new AbortController(),
      systemPrompt: 'persona prompt'
    });

    expect(options.settingSources).toEqual([]);
    expect(options.tools).toEqual(['Read']);
    expect(options.allowedTools).toEqual(['Read']);
    expect(options.disallowedTools).not.toContain('Read');
    expect(options.disallowedTools).toContain('LS');
    expect(options.disallowedTools).toContain('Bash');
    expect(options.disallowedTools).toContain('Write');
    expect(options.disallowedTools).toContain('Edit');
    expect(options.disallowedTools).toContain('Agent');
    expect(options.tools).not.toContain('Agent');
    expect(options.allowedTools).not.toContain('Agent');
    expect(options.agents).toBeUndefined();
    expect(options.disallowedTools).toContain('mcp__chirality__status_read');
    expect(options.disallowedTools).toEqual(expect.arrayContaining([...DOMAIN_MCP_TOOL_NAMES]));
    expect(options.mcpServers).toEqual({});
    expect(options.hooks?.PreToolUse?.[0]?.hooks[0]).toBeTypeOf('function');
    expect(options.hooks?.PostToolUse?.[0]?.hooks[0]).toBeTypeOf('function');
    expect(options.resume).toBe('sdk_resume');
    expect(options.model).toBe('claude-test');
    expect(options.maxTurns).toBe(3);
    expect(options.permissionMode).toBe('default');
    expect(options.canUseTool).toBeTypeOf('function');
    expect(options.spawnClaudeCodeProcess).toBeUndefined();
  });

  it('exposes the full requested read set and keeps unrequested or denied tools disallowed', () => {
    const options = buildSdkOptions({
      session,
      opts: { ...opts, tools: ['read', 'Glob', 'grep', 'LS'] },
      abortController: new AbortController(),
      systemPrompt: 'persona prompt'
    });

    expect(options.tools).toEqual(['Read', 'Glob', 'Grep', 'LS']);
    expect(options.allowedTools).toEqual(['Read', 'Glob', 'Grep', 'LS']);
    expect(options.disallowedTools).toEqual([
      'mcp__chirality__status_read',
      'mcp__chirality__deps_read',
      'mcp__chirality__scope_scan',
      'mcp__chirality__scaffold_preview',
      'mcp__chirality__status_transition',
      'mcp__chirality__deps_write',
      ...DOMAIN_MCP_TOOL_NAMES,
      'Write',
      'Edit',
      'MultiEdit',
      'NotebookEdit',
      'Bash',
      'WebFetch',
      'WebSearch',
      'Agent'
    ]);
  });

  it('attaches the read-only Chirality MCP server when MCP descriptors are requested', () => {
    const options = buildSdkOptions({
      session,
      opts: { ...opts, tools: ['status_read', 'deps_read'] },
      abortController: new AbortController(),
      systemPrompt: 'persona prompt'
    });

    expect(options.tools).toEqual([
      'mcp__chirality__status_read',
      'mcp__chirality__deps_read'
    ]);
    expect(options.allowedTools).toEqual([
      'mcp__chirality__status_read',
      'mcp__chirality__deps_read'
    ]);
    expect(options.disallowedTools).not.toContain('mcp__chirality__status_read');
    expect(options.disallowedTools).not.toContain('mcp__chirality__deps_read');
    expect(options.disallowedTools).toContain('mcp__chirality__scope_scan');
    expect(options.disallowedTools).toContain('Bash');
    expect(options.disallowedTools).toContain('Write');
    expect(options.disallowedTools).toContain('mcp__chirality__status_transition');
    expect(options.disallowedTools).toEqual(expect.arrayContaining([...DOMAIN_MCP_TOOL_NAMES]));
    expect(options.mcpServers).toMatchObject({
      chirality: {
        type: 'sdk',
        name: 'chirality'
      }
    });
  });

  it('attaches mutating Chirality MCP tools only when requested in workspaceWrite mode', () => {
    const workspaceWrite = buildSdkOptions({
      session,
      opts: {
        ...opts,
        mode: 'workspaceWrite',
        tools: ['status_transition', 'deps_write']
      },
      abortController: new AbortController(),
      systemPrompt: 'persona prompt'
    });

    expect(workspaceWrite.tools).toEqual([
      'mcp__chirality__status_transition',
      'mcp__chirality__deps_write'
    ]);
    expect(workspaceWrite.allowedTools).toEqual([
      'mcp__chirality__status_transition',
      'mcp__chirality__deps_write'
    ]);
    expect(workspaceWrite.disallowedTools).not.toContain('mcp__chirality__status_transition');
    expect(workspaceWrite.disallowedTools).not.toContain('mcp__chirality__deps_write');
    expect(workspaceWrite.mcpServers).toMatchObject({
      chirality: {
        type: 'sdk',
        name: 'chirality'
      }
    });

    const readOnly = buildSdkOptions({
      session,
      opts: {
        ...opts,
        mode: 'readOnly',
        tools: ['status_transition', 'deps_write']
      },
      abortController: new AbortController(),
      systemPrompt: 'persona prompt'
    });

    expect(readOnly.tools).toEqual([]);
    expect(readOnly.allowedTools).toEqual([]);
    expect(readOnly.disallowedTools).toContain('mcp__chirality__status_transition');
    expect(readOnly.disallowedTools).toContain('mcp__chirality__deps_write');
    expect(readOnly.mcpServers).toEqual({});
  });

  it('attaches D-APP-50 tranche-1 read-side domain MCP tools when explicitly requested', () => {
    const options = buildSdkOptions({
      session,
      opts: {
        ...opts,
        mode: 'readOnly',
        tools: ['domain_completeness_check', 'domain_rule_check_run']
      },
      abortController: new AbortController(),
      systemPrompt: 'persona prompt'
    });

    expect(options.tools).toEqual([...LIVE_DOMAIN_MCP_TOOL_NAMES]);
    expect(options.allowedTools).toEqual([...LIVE_DOMAIN_MCP_TOOL_NAMES]);
    expect(options.disallowedTools).not.toContain('mcp__chirality__domain_completeness_check');
    expect(options.disallowedTools).not.toContain('mcp__chirality__domain_rule_check_run');
    expect(options.disallowedTools).toEqual(expect.arrayContaining([...PARKED_DOMAIN_MCP_TOOL_NAMES]));
    expect(options.mcpServers).toMatchObject({
      chirality: {
        type: 'sdk',
        name: 'chirality'
      }
    });
  });

  it('keeps parked domain MCP tools denied even when explicitly requested', () => {
    const options = buildSdkOptions({
      session,
      opts: {
        ...opts,
        mode: 'workspaceWrite',
        tools: ['domain_headless_preview_run']
      },
      abortController: new AbortController(),
      systemPrompt: 'persona prompt'
    });

    expect(options.tools).toEqual([]);
    expect(options.allowedTools).toEqual([]);
    expect(options.disallowedTools).toEqual(expect.arrayContaining([...PARKED_DOMAIN_MCP_TOOL_NAMES]));
    expect(options.mcpServers).toEqual({});
  });

  it('attaches the D-APP-52 pec proposal tools in workspaceWrite mode when explicitly requested', () => {
    const options = buildSdkOptions({
      session,
      opts: {
        ...opts,
        mode: 'workspaceWrite',
        tools: ['domain_propose_operation', 'domain_proposal_validate']
      },
      abortController: new AbortController(),
      systemPrompt: 'persona prompt'
    });

    expect(options.tools).toEqual([...PEC_PROPOSAL_DOMAIN_MCP_TOOL_NAMES]);
    expect(options.allowedTools).toEqual([...PEC_PROPOSAL_DOMAIN_MCP_TOOL_NAMES]);
    expect(options.disallowedTools).not.toContain('mcp__chirality__domain_propose_operation');
    expect(options.disallowedTools).not.toContain('mcp__chirality__domain_proposal_validate');
    expect(options.disallowedTools).toEqual(
      expect.arrayContaining([...PARKED_DOMAIN_MCP_TOOL_NAMES])
    );
    expect(options.mcpServers).toMatchObject({
      chirality: {
        type: 'sdk',
        name: 'chirality'
      }
    });
  });

  it('keeps the write-graded pec proposal tool denied in readOnly mode while validate attaches', () => {
    const options = buildSdkOptions({
      session,
      opts: {
        ...opts,
        mode: 'readOnly',
        tools: ['domain_propose_operation', 'domain_proposal_validate']
      },
      abortController: new AbortController(),
      systemPrompt: 'persona prompt'
    });

    expect(options.tools).toEqual(['mcp__chirality__domain_proposal_validate']);
    expect(options.allowedTools).toEqual(['mcp__chirality__domain_proposal_validate']);
    expect(options.disallowedTools).toContain('mcp__chirality__domain_propose_operation');
    expect(options.mcpServers).toMatchObject({
      chirality: {
        type: 'sdk',
        name: 'chirality'
      }
    });
  });

  it('allows only explicit project settings and never user or local sources', () => {
    process.env.CHIRALITY_SDK_SETTING_SOURCES = 'user,local,project';

    const rejected = buildSdkOptions({
      session,
      opts,
      abortController: new AbortController(),
      systemPrompt: 'persona prompt'
    });
    expect(rejected.settingSources).toEqual([]);

    process.env.CHIRALITY_SDK_SETTING_SOURCES = 'project';
    const projectOnly = buildSdkOptions({
      session,
      opts,
      abortController: new AbortController(),
      systemPrompt: 'persona prompt'
    });
    expect(projectOnly.settingSources).toEqual(['project']);
  });

  it('attaches the scripted SDK subprocess only for explicit development or test proof runs', () => {
    vi.stubEnv('CHIRALITY_AGENTSDK_SCRIPTED_PROOF', '1');
    vi.stubEnv('NODE_ENV', 'test');

    const proofOptions = buildSdkOptions({
      session,
      opts,
      abortController: new AbortController(),
      systemPrompt: 'persona prompt'
    });
    expect(proofOptions.spawnClaudeCodeProcess).toBeTypeOf('function');

    vi.stubEnv('NODE_ENV', 'development');
    const developmentOptions = buildSdkOptions({
      session,
      opts,
      abortController: new AbortController(),
      systemPrompt: 'persona prompt'
    });
    expect(developmentOptions.spawnClaudeCodeProcess).toBeTypeOf('function');

    vi.stubEnv('NODE_ENV', '');
    const unsetOptions = buildSdkOptions({
      session,
      opts,
      abortController: new AbortController(),
      systemPrompt: 'persona prompt'
    });
    expect(unsetOptions.spawnClaudeCodeProcess).toBeUndefined();

    vi.stubEnv('NODE_ENV', 'production');
    const productionOptions = buildSdkOptions({
      session,
      opts,
      abortController: new AbortController(),
      systemPrompt: 'persona prompt'
    });
    expect(productionOptions.spawnClaudeCodeProcess).toBeUndefined();
  });

  it('maps Chirality modes to SDK permission posture without premature write auto-acceptance', () => {
    const readOnly = buildSdkOptions({
      session,
      opts: { ...opts, mode: 'readOnly' },
      abortController: new AbortController(),
      systemPrompt: 'persona prompt'
    });
    expect(readOnly.permissionMode).toBe('dontAsk');

    const workspaceWrite = buildSdkOptions({
      session,
      opts: { ...opts, mode: 'workspaceWrite' },
      abortController: new AbortController(),
      systemPrompt: 'persona prompt'
    });
    expect(workspaceWrite.permissionMode).toBe('acceptEdits');

    const bypassWithoutGate = buildSdkOptions({
      session,
      opts: { ...opts, mode: 'bypass' },
      abortController: new AbortController(),
      systemPrompt: 'persona prompt'
    });
    expect(bypassWithoutGate.permissionMode).toBe('default');

    process.env.CHIRALITY_ALLOW_SDK_BYPASS = '1';
    const bypassWithGate = buildSdkOptions({
      session,
      opts: { ...opts, mode: 'bypass' },
      abortController: new AbortController(),
      systemPrompt: 'persona prompt'
    });
    expect(bypassWithGate.permissionMode).toBe('bypassPermissions');
  });

  it('exposes requested Write/Edit/Bash only in workspaceWrite mode', () => {
    const workspaceWrite = buildSdkOptions({
      session,
      opts: { ...opts, mode: 'workspaceWrite', tools: ['read', 'write', 'Edit', 'bash'] },
      abortController: new AbortController(),
      systemPrompt: 'persona prompt'
    });

    expect(workspaceWrite.tools).toEqual(['Read', 'Write', 'Edit', 'Bash']);
    expect(workspaceWrite.allowedTools).toEqual(['Read', 'Write', 'Edit', 'Bash']);
    expect(workspaceWrite.disallowedTools).not.toContain('Write');
    expect(workspaceWrite.disallowedTools).not.toContain('Edit');
    expect(workspaceWrite.disallowedTools).not.toContain('Bash');
    expect(workspaceWrite.disallowedTools).toContain('MultiEdit');
    expect(workspaceWrite.permissionMode).toBe('acceptEdits');

    const askMode = buildSdkOptions({
      session,
      opts: { ...opts, mode: 'ask', tools: ['write', 'Edit'] },
      abortController: new AbortController(),
      systemPrompt: 'persona prompt'
    });

    expect(askMode.tools).toEqual([]);
    expect(askMode.allowedTools).toEqual([]);
    expect(askMode.disallowedTools).toContain('Write');
    expect(askMode.disallowedTools).toContain('Edit');
    expect(askMode.disallowedTools).toContain('Bash');
    expect(askMode.permissionMode).toBe('default');
  });

  it('attaches executable SDK agents definitions and exposes Agent only when delegated and requested', () => {
    const options = buildSdkOptions({
      session,
      opts: {
        ...opts,
        delegatedSubagents: ['TASK'],
        mode: 'workspaceWrite',
        tools: ['read', 'Agent']
      },
      abortController: new AbortController(),
      systemPrompt: 'persona prompt'
    });

    expect(options.agents).toMatchObject({
      TASK: {
        description: expect.stringContaining('TASK'),
        tools: [],
        disallowedTools: expect.arrayContaining(['Agent', 'Bash', 'Write']),
        maxTurns: 1,
        permissionMode: 'dontAsk'
      }
    });
    expect(options.tools).toEqual(['Read', 'Agent']);
    expect(options.allowedTools).toEqual(['Read', 'Agent']);
    expect(options.disallowedTools).not.toContain('Agent');

    const noDelegation = buildSdkOptions({
      session,
      opts: {
        ...opts,
        tools: ['read', 'Agent']
      },
      abortController: new AbortController(),
      systemPrompt: 'persona prompt'
    });
    expect(noDelegation.tools).toEqual(['Read']);
    expect(noDelegation.allowedTools).toEqual(['Read']);
    expect(noDelegation.disallowedTools).toContain('Agent');
  });

  it('attaches a canUseTool callback backed by Chirality permission decisions', async () => {
    tmpDir = await mkdtemp(path.join(os.tmpdir(), 'chirality-sdk-options-'));
    const writableProjectRoot = path.join(tmpDir, 'project');
    const instructionRoot = path.join(tmpDir, 'instruction-root');
    await mkdir(writableProjectRoot, { recursive: true });
    await mkdir(instructionRoot, { recursive: true });
    process.env.CHIRALITY_INSTRUCTION_ROOT = instructionRoot;
    const callbackSession = { ...session, projectRoot: writableProjectRoot };

    const askOptions = buildSdkOptions({
      session: callbackSession,
      opts: { ...opts, mode: 'ask' },
      abortController: new AbortController(),
      systemPrompt: 'persona prompt'
    });

    await expect(
      askOptions.canUseTool?.(
        'Read',
        { file_path: 'README.md' },
        {
          signal: new AbortController().signal,
          toolUseID: 'tool_read'
        }
      )
    ).resolves.toMatchObject({
      behavior: 'allow',
      toolUseID: 'tool_read'
    });

    // In ask mode a gated tool now suspends for an operator verdict (Phase 3).
    const pendingDenied = askOptions.canUseTool?.(
      'Write',
      { file_path: 'README.md', content: 'changed' },
      {
        signal: new AbortController().signal,
        toolUseID: 'tool_write'
      }
    );
    await waitForPending(callbackSession.sessionId);
    expect(
      getPermissionBroker().decide({
        sessionId: callbackSession.sessionId,
        toolUseId: 'tool_write',
        verdict: 'deny'
      })
    ).toBe(true);
    await expect(pendingDenied).resolves.toMatchObject({
      behavior: 'deny',
      toolUseID: 'tool_write'
    });

    // The same pause resolves to allow when the operator approves.
    const pendingAllowed = askOptions.canUseTool?.(
      'Write',
      { file_path: 'README.md', content: 'changed' },
      {
        signal: new AbortController().signal,
        toolUseID: 'tool_write_ask_allow'
      }
    );
    await waitForPending(callbackSession.sessionId);
    getPermissionBroker().decide({
      sessionId: callbackSession.sessionId,
      toolUseId: 'tool_write_ask_allow',
      verdict: 'allow'
    });
    await expect(pendingAllowed).resolves.toMatchObject({
      behavior: 'allow',
      toolUseID: 'tool_write_ask_allow'
    });

    const workspaceWriteOptions = buildSdkOptions({
      session: callbackSession,
      opts: { ...opts, mode: 'workspaceWrite' },
      abortController: new AbortController(),
      systemPrompt: 'persona prompt'
    });

    await expect(
      workspaceWriteOptions.canUseTool?.(
        'Write',
        { file_path: 'README.md', content: 'changed' },
        {
          signal: new AbortController().signal,
          toolUseID: 'tool_write_allowed'
        }
      )
    ).resolves.toMatchObject({
      behavior: 'allow',
      toolUseID: 'tool_write_allowed'
    });

    await expect(
      workspaceWriteOptions.canUseTool?.(
        'Bash',
        { command: 'npm test' },
        {
          signal: new AbortController().signal,
          toolUseID: 'tool_bash_allowed'
        }
      )
    ).resolves.toMatchObject({
      behavior: 'allow',
      toolUseID: 'tool_bash_allowed'
    });

    // Shell tools in ask mode also suspend for an operator verdict (Phase 3).
    const pendingBash = askOptions.canUseTool?.(
      'Bash',
      { command: 'npm test' },
      {
        signal: new AbortController().signal,
        toolUseID: 'tool_bash_ask'
      }
    );
    await waitForPending(callbackSession.sessionId);
    getPermissionBroker().decide({
      sessionId: callbackSession.sessionId,
      toolUseId: 'tool_bash_ask',
      verdict: 'deny'
    });
    await expect(pendingBash).resolves.toMatchObject({
      behavior: 'deny',
      toolUseID: 'tool_bash_ask'
    });

    await expect(
      askOptions.canUseTool?.(
        'mystery',
        {},
        {
          signal: new AbortController().signal,
          toolUseID: 'tool_unknown'
        }
      )
    ).resolves.toMatchObject({
      behavior: 'deny',
      message: expect.stringContaining("Unknown harness tool 'mystery'"),
      toolUseID: 'tool_unknown'
    });

    // A gated ask with no addressable toolUseID must not register an unreachable
    // pending entry; it denies immediately instead of suspending.
    await expect(
      askOptions.canUseTool?.(
        'Write',
        { file_path: 'README.md', content: 'changed' },
        {
          signal: new AbortController().signal,
          toolUseID: ''
        }
      )
    ).resolves.toMatchObject({ behavior: 'deny' });
    expect(getPermissionBroker().pendingCount(callbackSession.sessionId)).toBe(0);
  });

  it('allows Agent permission callbacks only for delegated children in workspaceWrite mode', async () => {
    tmpDir = await mkdtemp(path.join(os.tmpdir(), 'chirality-sdk-agent-options-'));
    const writableProjectRoot = path.join(tmpDir, 'project');
    await mkdir(writableProjectRoot, { recursive: true });

    const options = buildSdkOptions({
      session: { ...session, projectRoot: writableProjectRoot },
      opts: {
        ...opts,
        mode: 'workspaceWrite',
        delegatedSubagents: ['TASK'],
        tools: ['Agent']
      },
      abortController: new AbortController(),
      systemPrompt: 'persona prompt'
    });

    await expect(
      options.canUseTool?.(
        'Agent',
        { agent: 'TASK', prompt: 'run this' },
        {
          signal: new AbortController().signal,
          toolUseID: 'tool_agent'
        }
      )
    ).resolves.toMatchObject({
      behavior: 'allow',
      toolUseID: 'tool_agent'
    });

    await expect(
      options.canUseTool?.(
        'Agent',
        { agent: 'UNKNOWN', prompt: 'run this' },
        {
          signal: new AbortController().signal,
          toolUseID: 'tool_agent_unknown'
        }
      )
    ).resolves.toMatchObject({
      behavior: 'deny',
      message: expect.stringContaining('not eligible')
    });
  });
});
