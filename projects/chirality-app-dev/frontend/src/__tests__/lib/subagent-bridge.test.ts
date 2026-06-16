import { describe, expect, it } from 'vitest';
import {
  createExecutableAgentDefinition,
  createExecutableSubagentBridge,
  evaluateSubagentPreflight,
  SUBAGENT_BRIDGE_POLICY_VERSION,
  SUBAGENT_BRIDGE_RULING_REF,
  SUBAGENT_EXECUTION_ALLOWED_REASON,
  SUBAGENT_EXECUTION_DENIED_REASON
} from '../../lib/harness/subagent-bridge';
import type { ResolvedOpts, SessionRecord } from '../../lib/harness/types';

const session: SessionRecord = {
  sessionId: 'sess_bridge',
  projectRoot: '/tmp/project',
  persona: 'WORKING_ITEMS',
  mode: 'direct',
  createdAt: '2026-02-23T00:00:00.000Z',
  updatedAt: '2026-02-23T00:00:00.000Z'
};

const opts: ResolvedOpts = {
  model: 'claude-test',
  tools: ['read'],
  maxTurns: 3,
  persona: 'WORKING_ITEMS',
  mode: 'direct',
  delegatedSubagents: ['TASK']
};

describe('subagent bridge', () => {
  it('creates executable SDK agent definitions without inherited tools', () => {
    const definition = createExecutableAgentDefinition('TASK');

    expect(definition).toMatchObject({
      description: expect.stringContaining('TASK'),
      tools: [],
      maxTurns: 1,
      permissionMode: 'dontAsk'
    });
    expect(definition.prompt).toContain('D-APP-10 Option C');
    expect(definition.disallowedTools).toContain('Agent');
    expect(definition.disallowedTools).toContain('Bash');
    expect(definition.disallowedTools).toContain('Write');
  });

  it('returns an SDK agents option-shape only when delegated candidates exist', () => {
    const bridge = createExecutableSubagentBridge({ session, opts });

    expect(bridge).toMatchObject({
      policyVersion: SUBAGENT_BRIDGE_POLICY_VERSION,
      rulingRef: SUBAGENT_BRIDGE_RULING_REF,
      sessionId: 'sess_bridge',
      delegatedSubagents: ['TASK'],
      agents: {
        TASK: {
          tools: [],
          disallowedTools: expect.arrayContaining(['Agent']),
          maxTurns: 1,
          permissionMode: 'dontAsk'
        }
      }
    });

    expect(
      createExecutableSubagentBridge({
        session,
        opts: { ...opts, delegatedSubagents: [] }
      })
    ).toBeUndefined();
  });

  it('allows only eligible Agent preflight requests and records child metadata', () => {
    const decision = evaluateSubagentPreflight({
      toolInput: {
        agent: 'TASK',
        prompt: 'run this'
      },
      eligibleAgentNames: ['TASK']
    });

    expect(decision).toEqual({
      allowed: true,
      reason: SUBAGENT_EXECUTION_ALLOWED_REASON,
      safeMetadata: {
        policyVersion: SUBAGENT_BRIDGE_POLICY_VERSION,
        rulingRef: SUBAGENT_BRIDGE_RULING_REF,
        allowClass: 'subagent-execution',
        denyClass: undefined,
        executionPosture: 'executable',
        executableBridge: true,
        requestedAgent: 'TASK',
        eligibleAgentNames: ['TASK'],
        eligibleChildDefinition: true,
        childToolNames: [],
        childCapabilityInheritance: false
      }
    });

    const denied = evaluateSubagentPreflight({
      toolInput: {
        agent: 'UNKNOWN'
      },
      eligibleAgentNames: ['TASK']
    });
    expect(denied).toMatchObject({
      allowed: false,
      reason: SUBAGENT_EXECUTION_DENIED_REASON
    });
    expect(denied.safeMetadata).toMatchObject({
      executionPosture: 'hard-denied',
      requestedAgent: 'UNKNOWN',
      eligibleChildDefinition: false
    });
  });
});
