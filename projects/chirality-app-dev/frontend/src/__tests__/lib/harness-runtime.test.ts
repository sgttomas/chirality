import { afterEach, describe, expect, it } from 'vitest';
import { AnthropicAgentSdkManager } from '../../lib/harness/anthropic-agent-sdk-manager';
import {
  getHarnessRuntime,
  resetHarnessRuntimeForTests,
  resolveHarnessProviderMode
} from '../../lib/harness/runtime';
import { StubAgentSdkManager } from '../../lib/harness/agent-sdk-manager';
import { ClaudeAgentSdkManager } from '../../lib/harness/claude-agent-sdk-manager';
import { PersonaComposer } from '../../lib/harness/persona-manager';
import { TurnEngine } from '../../lib/harness/turn-engine';

afterEach(() => {
  delete process.env.CHIRALITY_HARNESS_PROVIDER;
  resetHarnessRuntimeForTests();
});

describe('harness runtime provider mode', () => {
  it('defaults to stub provider mode when env is unset', () => {
    expect(resolveHarnessProviderMode()).toBe('stub');
    const runtime = getHarnessRuntime();
    expect(runtime.agentSdkManager).toBeInstanceOf(StubAgentSdkManager);
    expect(runtime.personaManager).toBeInstanceOf(PersonaComposer);
    expect(runtime.turnEngine).toBeInstanceOf(TurnEngine);
  });

  it('selects anthropic provider mode when explicitly configured', () => {
    process.env.CHIRALITY_HARNESS_PROVIDER = 'anthropic';

    expect(resolveHarnessProviderMode()).toBe('anthropic');
    const runtime = getHarnessRuntime();
    expect(runtime.agentSdkManager).toBeInstanceOf(AnthropicAgentSdkManager);
  });

  it('selects Claude Agent SDK provider mode only when explicitly configured', () => {
    process.env.CHIRALITY_HARNESS_PROVIDER = 'agentSdk';

    expect(resolveHarnessProviderMode()).toBe('agentSdk');
    const runtime = getHarnessRuntime();
    expect(runtime.agentSdkManager).toBeInstanceOf(ClaudeAgentSdkManager);
  });
});
