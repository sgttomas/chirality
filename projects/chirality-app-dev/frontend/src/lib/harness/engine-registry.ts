import type {
  AgentEnginePort,
  AgentEngineRunInput,
  EngineDescriptor
} from '@chirality/runtime-contracts/agent-engine-port';
import { HarnessError } from '@chirality/runtime-contracts/errors';
import type {
  EngineSelection,
  IAgentSdkManager,
  ResolvedOpts,
  SessionRecord,
  UIEvent
} from '@chirality/runtime-contracts/types';

type LegacyManager = IAgentSdkManager & {
  cancel?(sessionId: string): Promise<void>;
  startTurn(
    session: SessionRecord,
    message: string,
    opts: ResolvedOpts,
    contentBlocks?: AgentEngineRunInput['contentBlocks'],
    turnId?: string
  ): AsyncIterable<UIEvent>;
};

export type EnginePreflight = (input: AgentEngineRunInput) => Promise<void> | void;

export class LegacyAgentEngineAdapter implements AgentEnginePort {
  readonly subject: string;

  constructor(
    readonly descriptor: EngineDescriptor,
    readonly manager: LegacyManager,
    private readonly runPreflight: EnginePreflight = () => undefined
  ) {
    this.subject = descriptor.adapterId;
  }

  async preflight(input: AgentEngineRunInput): Promise<void> {
    await this.runPreflight(input);
  }

  startTurn(input: AgentEngineRunInput): AsyncIterable<UIEvent> {
    return this.manager.startTurn(
      input.session,
      input.message,
      input.opts,
      input.contentBlocks,
      input.turnId
    );
  }

  async interrupt(sessionId: string): Promise<void> {
    await this.manager.interrupt(sessionId);
  }

  async cancel(sessionId: string): Promise<void> {
    await this.manager.cancel?.(sessionId);
  }
}

export type ResolvedEngine = {
  port: AgentEnginePort;
  selection: EngineSelection;
};

export type EngineAdapterFactory = (selection: EngineSelection) => AgentEnginePort;

export class AgentEngineRegistry {
  private readonly factories = new Map<string, EngineAdapterFactory>();
  private readonly instances = new Map<string, AgentEnginePort>();

  register(adapterId: string, factory: EngineAdapterFactory): void {
    if (!adapterId.trim()) {
      throw new Error('Engine adapter ID must be non-empty');
    }
    this.factories.set(adapterId, factory);
  }

  has(adapterId: string): boolean {
    return this.factories.has(adapterId);
  }

  resolve(selection: EngineSelection): ResolvedEngine {
    const factory = this.factories.get(selection.adapterId);
    if (!factory) {
      throw new HarnessError(
        'ENGINE_UNAVAILABLE',
        503,
        `Engine adapter '${selection.adapterId}' is not registered`,
        { adapterId: selection.adapterId, providerId: selection.providerId }
      );
    }

    const cacheKey = `${selection.adapterId}\u0000${selection.providerId}`;
    let port = this.instances.get(cacheKey);
    if (!port) {
      port = factory(selection);
      if (
        port.descriptor.adapterId !== selection.adapterId ||
        port.descriptor.providerId !== selection.providerId
      ) {
        throw new HarnessError(
          'ENGINE_UNAVAILABLE',
          503,
          'Engine adapter descriptor does not match the requested selection',
          {
            requested: selection,
            descriptor: port.descriptor
          }
        );
      }
      this.instances.set(cacheKey, port);
    }

    return { port, selection };
  }
}
