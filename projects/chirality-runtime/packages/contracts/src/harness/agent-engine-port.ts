import { ContentBlock, ResolvedOpts, SessionRecord, UIEvent } from './types.js';
import type { ResolveSelectedContextResponse } from '../v3.js';
import type { RuntimeToolDefinition } from '../engine.js';

export type EngineAdapterSubject = string;

export type EngineCapabilities = {
  credentials: boolean;
  tools: boolean;
  attachments: boolean;
  interruption: boolean;
  durableResume: boolean;
  compaction: boolean;
  /** Adapter bridge can expose the exact Runtime method-lifecycle control callback. */
  runtimeControlTools?: boolean;
};

export type EngineDescriptor = {
  adapterId: EngineAdapterSubject;
  providerId: string;
  packageName?: string;
  packageVersion?: string;
  capabilities: EngineCapabilities;
};

export type AgentEngineRunInput = {
  /** Modern Runtime coordinators supply this; legacy adapters may omit it. */
  projectId?: string;
  session: SessionRecord;
  message: string;
  opts: ResolvedOpts;
  contentBlocks?: ContentBlock[];
  turnId: string;
  /** Effective interaction mode for this turn, including an explicit per-turn override. */
  interactionMode?: "chat" | "native-plan";
  /** Exact runtime-resolved instructions supplied for this turn. */
  instructionContext?: ResolveSelectedContextResponse;
  /** Runtime-owned tools; adapters must expose only definitions admitted by their own tool bridge. */
  runtimeTools?: readonly RuntimeToolDefinition[];
  contextSuccessor?: PreparedContextSuccessor;
};

export interface ContextSuccessorRequest {
  sessionId: string;
  predecessorEngineSessionId: string;
  fromBasisId: string;
  toBasisPreview: { id: string; sha256: string };
  continuationContext: {
    transcript: string;
    sha256: string;
    priorBasisRefs: readonly { basisId: string; sha256: string }[];
  };
}

export interface PreparedContextSuccessor {
  preparationId: string;
  adapterId: string;
  providerId: string;
  predecessorEngineSessionId: string;
  continuationText: string;
  continuationSha256: string;
  targetBasisId: string;
  targetReference: string;
}

export interface AgentEnginePort {
  readonly descriptor: EngineDescriptor;
  /** @deprecated Use descriptor.adapterId. */
  readonly subject: EngineAdapterSubject;
  preflight(input: AgentEngineRunInput): Promise<void>;
  startTurn(input: AgentEngineRunInput): AsyncIterable<UIEvent>;
  interrupt(sessionId: string): Promise<void>;
  prepareContextSuccessor?(request: ContextSuccessorRequest): Promise<PreparedContextSuccessor>;
  cancelContextSuccessor?(preparationId: string): Promise<void>;
}

export type RuntimeEngineContract = {
  port: AgentEnginePort;
  publicUiEvents: readonly UIEvent['type'][];
  providerMetadataAllowed: true;
};

export const PUBLIC_UI_EVENT_NAMES = [
  'session:init',
  'chat:delta',
  'chat:complete',
  'tool:result',
  'session:complete',
  'turn:error',
  'process:exit',
  'harness:event'
] as const satisfies readonly UIEvent['type'][];
