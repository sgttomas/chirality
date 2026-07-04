import { AnthropicAgentSdkManager } from './anthropic-agent-sdk-manager';
import { StubAgentSdkManager } from './agent-sdk-manager';
import { ClaudeAgentSdkManager } from './claude-agent-sdk-manager';
import { AttachmentResolver } from './attachment-resolver';
import { hasUiApiKey } from './api-key-store';
import { PersonaComposer } from './persona-manager';
import { FileSessionManager } from './session-manager';
import { TurnEngine } from './turn-engine';
import { IAgentSdkManager, IAttachmentResolver, IPersonaManager, ISessionManager } from '@chirality/harness-contract/types';

type HarnessRuntime = {
  sessionManager: ISessionManager;
  personaManager: IPersonaManager;
  attachmentResolver: IAttachmentResolver;
  agentSdkManager: IAgentSdkManager;
  turnEngine: TurnEngine;
};

type HarnessRuntimeGlobal = typeof globalThis & {
  __CHIRALITY_HARNESS_RUNTIME__?: HarnessRuntime;
};

const harnessRuntimeGlobal = globalThis as HarnessRuntimeGlobal;

export type HarnessProviderMode = 'stub' | 'anthropic' | 'agentSdk';

function asNonEmptyString(value: string | undefined): string | undefined {
  if (typeof value !== 'string') {
    return undefined;
  }
  const trimmed = value.trim();
  return trimmed.length > 0 ? trimmed : undefined;
}

/**
 * Whether an Anthropic API key is configured via the UI Settings store or the
 * environment. Mirrors the key sources TurnEngine trusts
 * (`hasAnthropicApiKeyConfigured`) so the default provider and the per-turn key
 * gate agree on what "a key is configured" means.
 */
function hasConfiguredAnthropicKey(env: NodeJS.ProcessEnv): boolean {
  return (
    hasUiApiKey() ||
    Boolean(
      asNonEmptyString(env.ANTHROPIC_API_KEY) ?? asNonEmptyString(env.CHIRALITY_ANTHROPIC_API_KEY)
    )
  );
}

export function resolveHarnessProviderMode(env: NodeJS.ProcessEnv = process.env): HarnessProviderMode {
  const raw = asNonEmptyString(env.CHIRALITY_HARNESS_PROVIDER)?.toLowerCase();

  // An explicit CHIRALITY_HARNESS_PROVIDER selection always wins, so dev/CI can
  // pin any provider — including 'stub' — regardless of whether a key is present.
  if (raw === 'agentsdk' || raw === 'agent-sdk' || raw === 'claude-agent-sdk') {
    return 'agentSdk';
  }
  if (raw === 'anthropic') {
    return 'anthropic';
  }
  if (raw === 'stub') {
    return 'stub';
  }

  // D-APP-18 (Option A) key-aware default: with no explicit selection, use the
  // real Claude Agent SDK path when an Anthropic API key is configured (env or
  // UI Settings), otherwise fall back to the keyless stub so development works
  // without a key and never fails a turn on a missing key. The provider manager
  // is selected once at runtime construction; adding a key after a keyless start
  // requires an app restart to switch off the stub.
  return hasConfiguredAnthropicKey(env) ? 'agentSdk' : 'stub';
}

function buildAgentSdkManager(mode: HarnessProviderMode): IAgentSdkManager {
  if (mode === 'anthropic') {
    return new AnthropicAgentSdkManager();
  }
  if (mode === 'agentSdk') {
    return new ClaudeAgentSdkManager(undefined, async (projectRoot, persona, runtimeMode, tools) =>
      harnessRuntimeGlobal.__CHIRALITY_HARNESS_RUNTIME__?.personaManager.buildSystemPrompt(
        projectRoot,
        persona,
        runtimeMode,
        tools
      ) ?? ''
    );
  }
  return new StubAgentSdkManager();
}

export function getHarnessRuntime(): HarnessRuntime {
  if (!harnessRuntimeGlobal.__CHIRALITY_HARNESS_RUNTIME__) {
    const providerMode = resolveHarnessProviderMode();
    const sessionManager = new FileSessionManager();
    const personaManager = new PersonaComposer();
    const attachmentResolver = new AttachmentResolver();
    const agentSdkManager = buildAgentSdkManager(providerMode);

    harnessRuntimeGlobal.__CHIRALITY_HARNESS_RUNTIME__ = {
      sessionManager,
      personaManager,
      attachmentResolver,
      agentSdkManager,
      turnEngine: new TurnEngine({
        sessionManager,
        personaManager,
        attachmentResolver,
        agentSdkManager,
        resolveProviderMode: resolveHarnessProviderMode
      })
    };
  }

  return harnessRuntimeGlobal.__CHIRALITY_HARNESS_RUNTIME__;
}

export function resetHarnessRuntimeForTests(): void {
  delete harnessRuntimeGlobal.__CHIRALITY_HARNESS_RUNTIME__;
}
