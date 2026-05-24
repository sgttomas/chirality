import { ContentBlock, ResolvedOpts, SessionRecord, UIEvent } from './types';

export type EngineAdapterSubject = 'stub' | 'anthropic-direct' | 'claude-agent-sdk';

export type AgentEngineRunInput = {
  session: SessionRecord;
  message: string;
  opts: ResolvedOpts;
  contentBlocks?: ContentBlock[];
};

export interface AgentEnginePort {
  readonly subject: EngineAdapterSubject;
  startTurn(input: AgentEngineRunInput): AsyncIterable<UIEvent>;
  interrupt(sessionId: string): Promise<void>;
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
  'process:exit'
] as const satisfies readonly UIEvent['type'][];
