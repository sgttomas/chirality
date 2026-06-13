import { AnthropicAgentSdkManager } from './anthropic-agent-sdk-manager';
import { StubAgentSdkManager } from './agent-sdk-manager';
import { ClaudeAgentSdkManager } from './claude-agent-sdk-manager';
import { AttachmentResolver } from './attachment-resolver';
import { StubPersonaManager } from './persona-manager';
import { FileSessionManager } from './session-manager';
import { TurnEngine } from './turn-engine';
import { IAgentSdkManager, IAttachmentResolver, IPersonaManager, ISessionManager } from './types';

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

export function resolveHarnessProviderMode(env: NodeJS.ProcessEnv = process.env): HarnessProviderMode {
  const raw = asNonEmptyString(env.CHIRALITY_HARNESS_PROVIDER)?.toLowerCase();
  if (raw === 'agentsdk' || raw === 'agent-sdk' || raw === 'claude-agent-sdk') {
    return 'agentSdk';
  }
  return raw === 'anthropic' ? 'anthropic' : 'stub';
}

function buildAgentSdkManager(mode: HarnessProviderMode): IAgentSdkManager {
  if (mode === 'anthropic') {
    return new AnthropicAgentSdkManager();
  }
  if (mode === 'agentSdk') {
    return new ClaudeAgentSdkManager(undefined, async (projectRoot, persona, runtimeMode) =>
      harnessRuntimeGlobal.__CHIRALITY_HARNESS_RUNTIME__?.personaManager.buildSystemPrompt(
        projectRoot,
        persona,
        runtimeMode
      ) ?? ''
    );
  }
  return new StubAgentSdkManager();
}

export function getHarnessRuntime(): HarnessRuntime {
  if (!harnessRuntimeGlobal.__CHIRALITY_HARNESS_RUNTIME__) {
    const providerMode = resolveHarnessProviderMode();
    const sessionManager = new FileSessionManager();
    const personaManager = new StubPersonaManager();
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
