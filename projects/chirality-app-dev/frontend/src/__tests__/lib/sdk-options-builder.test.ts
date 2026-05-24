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
  it('defaults to SDK settings isolation and exposes no built-in tools in CODEV-001', () => {
    const options = buildSdkOptions({
      session,
      opts,
      abortController: new AbortController(),
      systemPrompt: 'persona prompt'
    });

    expect(options.settingSources).toEqual([]);
    expect(options.tools).toEqual([]);
    expect(options.allowedTools).toEqual([]);
    expect(options.disallowedTools).toContain('Bash');
    expect(options.disallowedTools).toContain('Write');
    expect(options.disallowedTools).toContain('Edit');
    expect(options.resume).toBe('sdk_resume');
    expect(options.model).toBe('claude-test');
    expect(options.maxTurns).toBe(3);
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
});
