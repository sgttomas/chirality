import { afterEach, beforeEach, describe, expect, it } from 'vitest';
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

const UI_API_KEY_GLOBAL = '__CHIRALITY_UI_API_KEY__';

function clearProviderState(): void {
  delete process.env.CHIRALITY_HARNESS_PROVIDER;
  delete process.env.ANTHROPIC_API_KEY;
  delete process.env.CHIRALITY_ANTHROPIC_API_KEY;
  delete (globalThis as Record<string, unknown>)[UI_API_KEY_GLOBAL];
}

beforeEach(() => {
  clearProviderState();
  resetHarnessRuntimeForTests();
});

afterEach(() => {
  clearProviderState();
  resetHarnessRuntimeForTests();
});

describe('harness runtime provider mode', () => {
  it('defaults to stub provider mode when env is unset and no API key is configured', () => {
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

  it('selects Claude Agent SDK provider mode when explicitly configured', () => {
    process.env.CHIRALITY_HARNESS_PROVIDER = 'agentSdk';

    expect(resolveHarnessProviderMode()).toBe('agentSdk');
    const runtime = getHarnessRuntime();
    expect(runtime.agentSdkManager).toBeInstanceOf(ClaudeAgentSdkManager);
  });

  // D-APP-18 (Option A) key-aware default — agentSdk becomes the default once an
  // Anthropic API key is configured; the keyless stub remains the fallback.
  it('defaults to agentSdk when ANTHROPIC_API_KEY is set and no provider is configured', () => {
    process.env.ANTHROPIC_API_KEY = 'sk-ant-test-key';

    expect(resolveHarnessProviderMode()).toBe('agentSdk');
    const runtime = getHarnessRuntime();
    expect(runtime.agentSdkManager).toBeInstanceOf(ClaudeAgentSdkManager);
  });

  it('treats CHIRALITY_ANTHROPIC_API_KEY as a key-aware default trigger', () => {
    process.env.CHIRALITY_ANTHROPIC_API_KEY = 'sk-ant-alt-key';

    expect(resolveHarnessProviderMode()).toBe('agentSdk');
  });

  it('defaults to agentSdk when a UI Settings API key is present and no provider is configured', () => {
    (globalThis as Record<string, unknown>)[UI_API_KEY_GLOBAL] = 'sk-ant-ui-key';

    expect(resolveHarnessProviderMode()).toBe('agentSdk');
  });

  it('honors an explicit stub selection even when an API key is configured', () => {
    process.env.ANTHROPIC_API_KEY = 'sk-ant-test-key';
    process.env.CHIRALITY_HARNESS_PROVIDER = 'stub';

    expect(resolveHarnessProviderMode()).toBe('stub');
    const runtime = getHarnessRuntime();
    expect(runtime.agentSdkManager).toBeInstanceOf(StubAgentSdkManager);
  });
});
