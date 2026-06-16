import type { AgentDefinition } from '@anthropic-ai/claude-agent-sdk';
import type { ResolvedOpts, SessionRecord } from './types';
import { getCurrentTrancheDisallowedToolNames } from './tool-descriptor';

export const SUBAGENT_BRIDGE_POLICY_VERSION = 'subagent-bridge.v2.executable-r5';
export const SUBAGENT_BRIDGE_RULING_REF = 'D-APP-10 Option C';

export const SUBAGENT_EXECUTION_DENIED_REASON =
  'Subagent execution is denied because the requested child is not eligible for the D-APP-10 Option C executable bridge.';

export const SUBAGENT_EXECUTION_ALLOWED_REASON =
  'Subagent execution is allowed by the D-APP-10 Option C executable bridge.';

export type ExecutableSubagentBridge = {
  policyVersion: typeof SUBAGENT_BRIDGE_POLICY_VERSION;
  rulingRef: typeof SUBAGENT_BRIDGE_RULING_REF;
  sessionId: string;
  delegatedSubagents: string[];
  agents: Record<string, AgentDefinition>;
};

export type SubagentPreflightDecision = {
  allowed: boolean;
  reason: string;
  safeMetadata: {
    policyVersion: typeof SUBAGENT_BRIDGE_POLICY_VERSION;
    rulingRef: typeof SUBAGENT_BRIDGE_RULING_REF;
    denyClass?: 'subagent-execution';
    allowClass?: 'subagent-execution';
    executionPosture: 'hard-denied' | 'executable';
    executableBridge: boolean;
    requestedAgent?: string;
    eligibleAgentNames: string[];
    eligibleChildDefinition: boolean;
    childToolNames: [];
    childCapabilityInheritance: false;
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

export function createExecutableAgentDefinition(agentName: string): AgentDefinition {
  const disallowedTools = getCurrentTrancheDisallowedToolNames([]);
  return {
    description: `Governed Type 2 subagent ${agentName}; executable R5 child turn with no inherited tools.`,
    prompt:
      'You are a governed Chirality Type 2 subagent running under D-APP-10 Option C. Execute only the delegated child turn. Do not claim inherited parent capabilities, provider routing, network expansion, Pi runtime access, release readiness, professional approval, certification, sealing, authentication, or code-compliance acceptance.',
    tools: [],
    disallowedTools,
    maxTurns: 1,
    permissionMode: 'dontAsk'
  };
}

export function createExecutableSubagentBridge(input: {
  session: SessionRecord;
  opts: ResolvedOpts;
}): ExecutableSubagentBridge | undefined {
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
        createExecutableAgentDefinition(agentName)
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
  const eligibleChildDefinition = Boolean(
    requestedAgent && eligibleAgentNames.includes(requestedAgent)
  );

  return {
    allowed: eligibleChildDefinition,
    reason: eligibleChildDefinition
      ? SUBAGENT_EXECUTION_ALLOWED_REASON
      : SUBAGENT_EXECUTION_DENIED_REASON,
    safeMetadata: {
      policyVersion: SUBAGENT_BRIDGE_POLICY_VERSION,
      rulingRef: SUBAGENT_BRIDGE_RULING_REF,
      denyClass: eligibleChildDefinition ? undefined : 'subagent-execution',
      allowClass: eligibleChildDefinition ? 'subagent-execution' : undefined,
      executionPosture: eligibleChildDefinition ? 'executable' : 'hard-denied',
      executableBridge: true,
      requestedAgent,
      eligibleAgentNames,
      eligibleChildDefinition,
      childToolNames: [],
      childCapabilityInheritance: false
    }
  };
}
