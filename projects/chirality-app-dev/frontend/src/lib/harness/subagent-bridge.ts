import type { AgentDefinition } from '@anthropic-ai/claude-agent-sdk';
import type { ResolvedOpts, SessionRecord } from './types';
import { getCurrentTrancheDisallowedToolNames } from './tool-descriptor';

export const SUBAGENT_BRIDGE_POLICY_VERSION = 'subagent-bridge.v1.non-executable';
export const SUBAGENT_BRIDGE_RULING_REF = 'D-APP-09 Option B';

export const SUBAGENT_EXECUTION_DENIED_REASON =
  'Subagent execution is hard-denied by the D-APP-09 Option B non-executable bridge.';

export type NonExecutableSubagentBridge = {
  policyVersion: typeof SUBAGENT_BRIDGE_POLICY_VERSION;
  rulingRef: typeof SUBAGENT_BRIDGE_RULING_REF;
  sessionId: string;
  delegatedSubagents: string[];
  agents: Record<string, AgentDefinition>;
};

export type SubagentPreflightDecision = {
  allowed: false;
  reason: string;
  safeMetadata: {
    policyVersion: typeof SUBAGENT_BRIDGE_POLICY_VERSION;
    rulingRef: typeof SUBAGENT_BRIDGE_RULING_REF;
    denyClass: 'subagent-execution';
    executionPosture: 'hard-denied';
    nonExecutableBridge: true;
    requestedAgent?: string;
    eligibleAgentNames: string[];
    eligibleChildDefinition: boolean;
  };
};

function uniqueNames(names: readonly string[] | undefined): string[] {
  return Array.from(
    new Set(
      (names ?? [])
        .map((name) => name.trim())
        .filter((name) => name.length > 0)
    )
  );
}

function readStringField(input: Record<string, unknown>, fields: readonly string[]): string | undefined {
  for (const field of fields) {
    const value = input[field];
    if (typeof value === 'string' && value.trim().length > 0) {
      return value.trim();
    }
  }
  return undefined;
}

export function extractRequestedSubagentName(toolInput: Record<string, unknown>): string | undefined {
  return readStringField(toolInput, ['agent', 'agentName', 'subagent_type', 'subagentType']);
}

export function createNonExecutableAgentDefinition(agentName: string): AgentDefinition {
  const disallowedTools = getCurrentTrancheDisallowedToolNames([]);
  return {
    description: `Governed Type 2 subagent candidate ${agentName}; non-executable bridge only.`,
    prompt:
      'This Chirality bridge definition is non-executable. D-APP-09 Option B permits child definition eligibility, SDK agents option shape, and an Agent preflight gate only; it does not approve child turns, executable output artifacts, inherited capabilities, provider routing, or network expansion.',
    tools: [],
    disallowedTools,
    maxTurns: 0,
    permissionMode: 'dontAsk'
  };
}

export function createNonExecutableSubagentBridge(input: {
  session: SessionRecord;
  opts: ResolvedOpts;
}): NonExecutableSubagentBridge | undefined {
  const delegatedSubagents = uniqueNames(input.opts.delegatedSubagents);
  if (delegatedSubagents.length === 0) {
    return undefined;
  }

  return {
    policyVersion: SUBAGENT_BRIDGE_POLICY_VERSION,
    rulingRef: SUBAGENT_BRIDGE_RULING_REF,
    sessionId: input.session.sessionId,
    delegatedSubagents,
    agents: Object.fromEntries(
      delegatedSubagents.map((agentName) => [
        agentName,
        createNonExecutableAgentDefinition(agentName)
      ])
    )
  };
}

export function evaluateSubagentPreflight(input: {
  toolInput: Record<string, unknown>;
  eligibleAgentNames?: readonly string[];
}): SubagentPreflightDecision {
  const eligibleAgentNames = uniqueNames(input.eligibleAgentNames);
  const requestedAgent = extractRequestedSubagentName(input.toolInput);

  return {
    allowed: false,
    reason: SUBAGENT_EXECUTION_DENIED_REASON,
    safeMetadata: {
      policyVersion: SUBAGENT_BRIDGE_POLICY_VERSION,
      rulingRef: SUBAGENT_BRIDGE_RULING_REF,
      denyClass: 'subagent-execution',
      executionPosture: 'hard-denied',
      nonExecutableBridge: true,
      requestedAgent,
      eligibleAgentNames,
      eligibleChildDefinition: Boolean(requestedAgent && eligibleAgentNames.includes(requestedAgent))
    }
  };
}
