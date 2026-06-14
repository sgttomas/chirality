import { afterEach, describe, expect, it } from 'vitest';
import { buildSdkOptions } from '../../lib/harness/sdk-options-builder';
import type { ResolvedOpts, SessionRecord } from '../../lib/harness/types';

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

afterEach(() => {
  delete process.env.CHIRALITY_SDK_SETTING_SOURCES;
  delete process.env.CHIRALITY_ALLOW_SDK_BYPASS;
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
    expect(options.disallowedTools).toContain('mcp__chirality__status_read');
    expect(options.mcpServers).toEqual({});
    expect(options.resume).toBe('sdk_resume');
    expect(options.model).toBe('claude-test');
    expect(options.maxTurns).toBe(3);
    expect(options.permissionMode).toBe('default');
    expect(options.canUseTool).toBeTypeOf('function');
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
    expect(workspaceWrite.permissionMode).toBe('default');

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

  it('attaches a canUseTool callback backed by Chirality permission decisions', async () => {
    const askOptions = buildSdkOptions({
      session,
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

    await expect(
      askOptions.canUseTool?.(
        'Write',
        { file_path: 'README.md', content: 'changed' },
        {
          signal: new AbortController().signal,
          toolUseID: 'tool_write'
        }
      )
    ).resolves.toMatchObject({
      behavior: 'deny',
      message: expect.stringContaining('requires application approval'),
      toolUseID: 'tool_write'
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
  });
});
