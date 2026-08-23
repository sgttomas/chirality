import { app } from 'electron';
import path from 'node:path';
import {
  AuthRegistry,
  type Agent1ManagerRuntimePort,
  CompatibilitySessionPolicy,
  EngineRegistry,
  GovernedAgent1RunCoordinator,
  ProjectRegistry,
  ResidencyCoordinator,
  RuntimeService,
  SessionStore,
  TurnCoordinator
} from '@chirality/runtime-core';
import { RuntimeDaemon } from '@chirality/runtime-daemon';
import {
  createClaudeEngineAdapter,
  type ClaudeTurnRuntimePort
} from '@chirality/engine-claude';
import {
  createPiOmlxEngineAdapter,
  OmlxClient,
  type PiTurnRuntimePort
} from '@chirality/engine-pi-omlx';
import {
  HarnessError,
  RuntimeError,
  type AgentEnginePort,
  type AgentEngineRunInput,
  type EngineCapabilities,
  type EngineSelection,
  type RuntimeSessionRecord,
  type RuntimeToolDefinition,
  type UIEvent
} from '@chirality/runtime-contracts';
import { AnthropicAgentSdkManager } from '../src/lib/harness/anthropic-agent-sdk-manager';
import { AttachmentResolver } from '../src/lib/harness/attachment-resolver';
import { StubAgentSdkManager } from '../src/lib/harness/agent-sdk-manager';
import { ClaudeAgentSdkManager } from '../src/lib/harness/claude-agent-sdk-manager';
import { LegacyAgentEngineAdapter } from '../src/lib/harness/engine-registry';
import {
  OmlxProviderError,
  requireOmlxModel,
  resolveOmlxProviderConfig
} from '../src/lib/harness/omlx-provider-config';
import { PersonaComposer } from '../src/lib/harness/persona-manager';
import { getPermissionBroker } from '../src/lib/harness/permission-broker';
import { PiAgentEngineAdapter } from '../src/lib/harness/pi-agent-engine-adapter';
import type { PiCustomToolDefinition } from '../src/lib/harness/pi-agent-engine-adapter';
import { scaffoldExecutionRoot } from '../src/lib/harness/scaffold';
import { SafeStorageCredentialStore } from './api-key-storage';

const ANTHROPIC_SDK_PACKAGE_VERSION = '0.93.0';
export const MACOS_UNIX_SOCKET_PATH_MAX_BYTES = 103;

export type RuntimeHost = {
  daemon: RuntimeDaemon;
  operatorTokenFile: string;
  runtimeDirectory: string;
  socketPath: string;
  stop(): Promise<void>;
};

export function assertRuntimeSocketPathSupported(
  socketPath: string,
  platform: NodeJS.Platform = process.platform
): { measuredBytes: number; maximumBytes: number } {
  const measuredBytes = Buffer.byteLength(socketPath, 'utf8');
  if (platform === 'darwin' && measuredBytes > MACOS_UNIX_SOCKET_PATH_MAX_BYTES) {
    throw new Error(
      `Runtime control socket path is ${measuredBytes} UTF-8 bytes; macOS maximum is ${MACOS_UNIX_SOCKET_PATH_MAX_BYTES} bytes`
    );
  }
  return { measuredBytes, maximumBytes: MACOS_UNIX_SOCKET_PATH_MAX_BYTES };
}

function asNonEmptyString(value: string | undefined): string | undefined {
  const normalized = value?.trim();
  return normalized ? normalized : undefined;
}

function requireAnthropicCredential(credentials: SafeStorageCredentialStore) {
  return async (): Promise<void> => {
    if ((await credentials.get('anthropic')) === undefined) {
      throw new Error('Anthropic credential is not configured');
    }
  };
}

function asClaudeTurnRuntime(engine: AgentEnginePort): ClaudeTurnRuntimePort {
  return {
    preflight: (input) => engine.preflight(input),
    startTurn: (input) => engine.startTurn(input),
    interrupt: (sessionId) => engine.interrupt(sessionId)
  };
}

function asPiTurnRuntime(engine: AgentEnginePort): PiTurnRuntimePort {
  return {
    preflight: (input) => engine.preflight(input),
    startTurn: (input) => engine.startTurn(input),
    interrupt: (sessionId) => engine.interrupt(sessionId)
  };
}

function withPreservedCapabilities(
  promoted: AgentEnginePort,
  capabilities: EngineCapabilities
): AgentEnginePort {
  return {
    ...promoted,
    descriptor: {
      ...promoted.descriptor,
      capabilities
    }
  };
}

function normalizeOmlxFailure(error: unknown): Error {
  if (error instanceof OmlxProviderError) {
    return error;
  }
  return error instanceof Error ? error : new Error('oMLX provider preflight failed');
}

const LEGACY_COORDINATION_TOOLS = new Set([
  'mcp__chirality__delegate_agent',
  'mcp__chirality__report_coordination_notice',
  'mcp__chirality__send_agent_update',
  'mcp__chirality__ack_agent_update'
]);

function rejectLegacyDelegation(input: AgentEngineRunInput): void {
  const requested = input.opts.tools.filter((tool) => LEGACY_COORDINATION_TOOLS.has(tool));
  if (requested.length > 0) {
    throw new HarnessError(
      'ENGINE_UNAVAILABLE',
      409,
      'Legacy in-process coordination tools are disabled in the shared runtime daemon.',
      { requested }
    );
  }
}

export function createEngines(
  credentials: SafeStorageCredentialStore,
  personaManager: PersonaComposer,
  runtimeTools: Map<string, readonly RuntimeToolDefinition[]>,
  promotedRuntime: {
    isExactlyResident(modelId: string): Promise<boolean>;
    transcriptRootFor(sessionId: string): string;
  }
): EngineRegistry {
  const engines = new EngineRegistry();
  const stub = new LegacyAgentEngineAdapter(
    {
      adapterId: 'stub',
      providerId: 'stub',
      capabilities: {
        credentials: false,
        tools: false,
        attachments: true,
        interruption: true,
        durableResume: false,
        compaction: false
      }
    },
    new StubAgentSdkManager()
  );
  const anthropicDirectRuntime = new LegacyAgentEngineAdapter(
    {
      adapterId: 'anthropic-direct',
      providerId: 'anthropic',
      packageName: '@anthropic-ai/sdk',
      capabilities: {
        credentials: true,
        tools: false,
        attachments: true,
        interruption: true,
        durableResume: true,
        compaction: false
      }
    },
    new AnthropicAgentSdkManager(),
    requireAnthropicCredential(credentials)
  );
  const concreteClaude = new ClaudeAgentSdkManager(
    undefined,
    (projectRoot, persona, runtimeMode, tools) =>
      personaManager.buildSystemPrompt(projectRoot, persona, runtimeMode, tools)
  );
  const claudeRuntime: AgentEnginePort = {
    descriptor: concreteClaude.descriptor,
    subject: concreteClaude.subject,
    async preflight(input) {
      rejectLegacyDelegation(input);
      // A headless daemon starts in a fresh process, so the compatibility
      // global consumed by the Claude SDK adapter is empty until safeStorage
      // is read. Rehydrate it for every explicit Claude turn; the credential
      // remains in the main process and never crosses renderer IPC.
      await requireAnthropicCredential(credentials)();
      await concreteClaude.preflight(input);
    },
    startTurn(input) {
      rejectLegacyDelegation(input);
      return concreteClaude.startTurn(input);
    },
    interrupt(sessionId) {
      return concreteClaude.interrupt(sessionId);
    }
  };
  const piRuntime = new PiAgentEngineAdapter({
    resolveProvider: async (input) => {
      try {
        const config = resolveOmlxProviderConfig({
          baseUrl: asNonEmptyString(process.env.CHIRALITY_OMLX_BASE_URL),
          apiKey: await credentials.get('omlx')
        });
        const model = await requireOmlxModel(input.opts.model, config);
        return {
          ...config,
          model: {
            id: model,
            contextWindow: 32_768,
            maxTokens: 4_096
          }
        };
      } catch (error) {
        throw normalizeOmlxFailure(error);
      }
    },
    buildSystemPrompt: (input) =>
      personaManager.buildSystemPrompt(
        input.session.projectRoot,
        input.opts.persona,
        input.opts.mode,
        input.opts.tools
      ),
    resolveCustomTools: async (input) => {
      if (input.session.agentType !== 2) {
        throw new HarnessError(
          'INVALID_REQUEST',
          403,
          'Pi/oMLX is available only to governed Agent 2 children.'
        );
      }
      const tools = runtimeTools.get(input.session.sessionId) ?? [];
      if (
        tools.length !== 1 ||
        tools[0]?.name !== 'read_file' ||
        tools[0].permission.operation !== 'read' ||
        tools[0].permission.effect !== 'allow'
      ) {
        throw new HarnessError(
          'INVALID_REQUEST',
          403,
          'Pi/oMLX requires exactly one runtime-owned read_file tool.'
        );
      }
      return tools.map((tool): PiCustomToolDefinition => ({
        name: tool.name,
        label: 'Read File',
        description: tool.description,
        parameters: tool.inputSchema,
        chirality: {
          descriptorName: tool.name,
          permissions: ['read'],
          pathScope: tool.permission.roots ?? [],
          readOnly: true,
          evidenceSource: 'chirality-tool-bridge'
        },
        execute: async (_toolUseId, params, signal) => {
          const result = await tool.execute(
            params,
            signal ?? new AbortController().signal
          );
          return {
            content: [{ type: 'text', text: JSON.stringify(result) }],
            details: {
              source: 'chirality-tool-bridge',
              chiralityToolName: tool.name
            }
          };
        }
      }));
    }
  });

  const anthropicDirect = withPreservedCapabilities(
    createClaudeEngineAdapter({
      adapterId: 'anthropic-direct',
      packageName: '@anthropic-ai/sdk',
      packageVersion: ANTHROPIC_SDK_PACKAGE_VERSION,
      credentials,
      runtime: asClaudeTurnRuntime(anthropicDirectRuntime)
    }),
    anthropicDirectRuntime.descriptor.capabilities
  );
  const claude = withPreservedCapabilities(
    createClaudeEngineAdapter({
      adapterId: 'claude-agent-sdk',
      packageName: '@anthropic-ai/claude-agent-sdk',
      packageVersion: concreteClaude.descriptor.packageVersion,
      credentials,
      runtime: asClaudeTurnRuntime(claudeRuntime)
    }),
    concreteClaude.descriptor.capabilities
  );
  const pi = createPiOmlxEngineAdapter({
    credentials,
    runtime: asPiTurnRuntime(piRuntime),
    transcriptRootFor: promotedRuntime.transcriptRootFor,
    isExactlyResident: promotedRuntime.isExactlyResident
  });

  for (const engine of [stub, anthropicDirect, claude, pi]) {
    engines.register(engine);
  }
  return engines;
}

function withoutCoordinatorTerminal(event: UIEvent): boolean {
  return !(
    event.type === 'process:exit' ||
    (event.type === 'harness:event' &&
      ['turn.completed', 'turn.failed', 'turn.cancelled', 'turn.interrupted'].includes(
        event.data.type
      ))
  );
}

export class EngineBackedAgent1Manager implements Agent1ManagerRuntimePort {
  private readonly activeProjects = new Map<string, string>();

  constructor(private readonly turns: TurnCoordinator) {}

  async *execute(
    session: RuntimeSessionRecord,
    request: Parameters<Agent1ManagerRuntimePort['execute']>[1],
    hooks: Parameters<Agent1ManagerRuntimePort['execute']>[2],
    signal: AbortSignal
  ): AsyncIterable<UIEvent> {
    this.activeProjects.set(session.sessionId, session.projectId);
    try {
      if (request.localModel === undefined) {
        yield* this.runManagerTurn(session, request.brief, signal);
        return;
      }

      let sealedBrief = '';
      for await (const event of this.runManagerTurn(
        session,
        [
          'You are the governed Agent 1 manager.',
          'Prepare a concise sealed brief for one read-only Agent 2 worker.',
          'The worker has exactly one read_file tool and cannot delegate.',
          'Return only the brief.',
          '',
          request.brief
        ].join('\n'),
        signal
      )) {
        if (event.type === 'chat:delta') {
          sealedBrief += event.data.text;
        } else if (event.type === 'chat:complete') {
          sealedBrief = event.data.text;
        }
        yield event;
      }
      if (signal.aborted) throw new HarnessError('SDK_FAILURE', 499, 'Agent 1 interrupted');
      const directChildBrief = [
        'You are the bounded Agent 2 worker for a governed Chirality run.',
        'Call the available read_file tool exactly once before answering.',
        `The tool is already bound to ${request.readOnlyTool?.relativePath ?? 'the authorized file'} and accepts an empty JSON object: {}.`,
        'After the tool succeeds, report only the facts needed to answer the original request.',
        'Do not delegate and do not claim to have read the file without using the tool.',
        '',
        `Original request:\n${request.brief}`,
        '',
        'Agent 1 preparation (advisory only):',
        sealedBrief.trim() || request.brief
      ].join('\n');
      const child = await hooks.delegate({
        sealedBrief: directChildBrief
      });

      let reviewText = '';
      for await (const event of this.runManagerTurn(
        session,
        [
          'You are the governed Agent 1 manager reviewing an Agent 2 return.',
          'Start your response with ACCEPT or REJECT, then explain your evidence-based review.',
          '',
          `Original request:\n${request.brief}`,
          '',
          `Agent 2 return (${child.model}, residency ${child.residencyEpoch}):`,
          child.returnText
        ].join('\n'),
        signal
      )) {
        if (event.type === 'chat:delta') {
          reviewText += event.data.text;
        } else if (event.type === 'chat:complete') {
          reviewText = event.data.text;
        }
        yield event;
      }
      const decision =
        reviewText.trimStart().toUpperCase().startsWith('ACCEPT') ? 'accepted' : 'rejected';
      await hooks.review({
        childSessionId: child.childSessionId,
        decision,
        rationale: reviewText.trim() || 'Manager returned no review rationale.'
      });
    } finally {
      this.activeProjects.delete(session.sessionId);
    }
  }

  async interrupt(sessionId: string): Promise<void> {
    const projectId = this.activeProjects.get(sessionId);
    if (projectId !== undefined) {
      await this.turns.interrupt(projectId, sessionId);
    }
  }

  private async *runManagerTurn(
    session: RuntimeSessionRecord,
    prompt: string,
    signal: AbortSignal
  ): AsyncIterable<UIEvent> {
    if (signal.aborted) {
      throw new RuntimeError('INTERRUPTED', 'Agent 1 interrupted', 499);
    }
    let processExit: Extract<UIEvent, { type: 'process:exit' }> | undefined;
    let terminalHarnessEvent:
      | Extract<UIEvent, { type: 'harness:event' }>['data']
      | undefined;
    let fatalTurnError: Extract<UIEvent, { type: 'turn:error' }> | undefined;
    let interruptRequested = false;
    for await (const event of this.turns.run(session.projectId, session.sessionId, {
      prompt,
      opts: { tools: [], maxTurns: 50 }
    })) {
      if (signal.aborted && !interruptRequested) {
        interruptRequested = true;
        await this.turns.interrupt(session.projectId, session.sessionId);
      }
      if (event.type === 'process:exit') {
        processExit = event;
      } else if (
        event.type === 'harness:event' &&
        ['turn.completed', 'turn.failed', 'turn.cancelled', 'turn.interrupted'].includes(
          event.data.type
        )
      ) {
        terminalHarnessEvent = event.data;
      } else if (event.type === 'turn:error' && event.data.fatal) {
        fatalTurnError = event;
      }
      if (withoutCoordinatorTerminal(event)) yield event;
    }
    if (
      signal.aborted ||
      processExit?.data.interrupted === true ||
      terminalHarnessEvent?.type === 'turn.interrupted' ||
      terminalHarnessEvent?.type === 'turn.cancelled'
    ) {
      throw new RuntimeError('INTERRUPTED', 'Agent 1 interrupted', 499);
    }
    if (processExit === undefined) {
      throw new RuntimeError(
        'ENGINE_UNAVAILABLE',
        'Agent 1 manager stream ended without process:exit',
        502
      );
    }
    if (processExit.data.exitCode !== 0) {
      throw new RuntimeError(
        'ENGINE_UNAVAILABLE',
        processExit.data.error ?? fatalTurnError?.data.message ?? 'Agent 1 manager turn failed',
        processExit.data.status ?? fatalTurnError?.data.status ?? 502
      );
    }
    if (fatalTurnError !== undefined) {
      throw new RuntimeError(
        'ENGINE_UNAVAILABLE',
        fatalTurnError.data.message,
        fatalTurnError.data.status
      );
    }
    if (terminalHarnessEvent?.type !== 'turn.completed') {
      throw new RuntimeError(
        'ENGINE_UNAVAILABLE',
        'Agent 1 manager stream ended without successful turn completion',
        502
      );
    }
  }
}

export async function startRuntimeHost(): Promise<RuntimeHost> {
  const runtimeDirectory = path.join(app.getPath('userData'), 'runtime');
  const socketPath = path.join(runtimeDirectory, 'control.sock');
  assertRuntimeSocketPathSupported(socketPath);
  process.env.CHIRALITY_RUNTIME_SOCKET_PATH = socketPath;
  process.env.CHIRALITY_RUNTIME_TOKEN_FILE = path.join(
    runtimeDirectory,
    'auth',
    'tokens',
    'operator.token'
  );
  // Compatibility adapters may emit their own evidence. Keep it daemon-owned
  // and outside every project-local legacy session root.
  process.env.CHIRALITY_SESSION_ROOT = path.join(runtimeDirectory, 'adapter-events');

  const credentials = new SafeStorageCredentialStore();
  const projects = new ProjectRegistry(runtimeDirectory);
  const sessions = new SessionStore(runtimeDirectory, projects);
  const auth = new AuthRegistry(runtimeDirectory);
  const personaManager = new PersonaComposer();
  const runtimeTools = new Map<string, readonly RuntimeToolDefinition[]>();
  const omlx = new OmlxClient({
    credentials,
    baseUrl: asNonEmptyString(process.env.CHIRALITY_OMLX_BASE_URL)
  });
  const residency = new ResidencyCoordinator(omlx, runtimeDirectory);
  const engines = createEngines(credentials, personaManager, runtimeTools, {
    async isExactlyResident(modelId) {
      const status = await residency.status();
      return status.phase === 'READY' && status.managedModelId === modelId;
    },
    transcriptRootFor: (sessionId) =>
      path.join(runtimeDirectory, 'adapter-events', sessionId)
  });
  const attachments = new AttachmentResolver();
  const turns = new TurnCoordinator(projects, sessions, engines, residency, attachments);
  const sessionPolicy = new CompatibilitySessionPolicy({
    credentials,
    availableAdapterIds: () => engines.descriptors().map((item) => item.adapterId)
  });
  const permissionBroker = getPermissionBroker();
  const manager = new EngineBackedAgent1Manager(turns);
  const resolveManagerSelection = async (): Promise<EngineSelection> => {
    const resolved = await sessionPolicy.resolve({
      projectId: 'runtime-manager',
      persona: 'WORKING_ITEMS',
      mode: 'direct',
      agentType: 1
    });
    return resolved.engineSelection;
  };
  const agent1Runs = new GovernedAgent1RunCoordinator({
    projects,
    sessions,
    turns,
    residency,
    manager,
    tools: {
      async bind(sessionId, tools) {
        if (runtimeTools.has(sessionId)) {
          throw new Error(`Runtime tools are already bound for '${sessionId}'`);
        }
        runtimeTools.set(sessionId, tools);
        return async () => {
          runtimeTools.delete(sessionId);
        };
      }
    },
    resolveManagerSelection
  });
  const service = new RuntimeService(
    projects,
    sessions,
    engines,
    residency,
    turns,
    auth,
    credentials,
    {
      scaffold: async (_projectId, request) => scaffoldExecutionRoot(request)
    },
    agent1Runs,
    {
      submit: async (_projectId, sessionId, request) => {
        const accepted = permissionBroker.decide({
          sessionId,
          toolUseId: request.requestId,
          verdict: request.decision
        });
        if (!accepted) {
          throw new Error(`No pending permission request '${request.requestId}'`);
        }
      }
    },
    sessionPolicy
  );
  const daemon = new RuntimeDaemon({ runtimeDirectory, socketPath, service });
  const started = await daemon.start();

  return {
    daemon,
    operatorTokenFile: started.operatorTokenFile,
    runtimeDirectory,
    socketPath,
    stop: () => daemon.stop()
  };
}
