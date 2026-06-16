import { describe, expect, it } from 'vitest';
import {
  createNonExecutableAgentDefinition,
  createNonExecutableSubagentBridge,
  evaluateSubagentPreflight,
  SUBAGENT_BRIDGE_POLICY_VERSION,
  SUBAGENT_BRIDGE_RULING_REF,
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
  it('creates inert SDK agent definitions for delegated Type 2 candidates', () => {
    const definition = createNonExecutableAgentDefinition('TASK');

    expect(definition).toMatchObject({
      description: expect.stringContaining('TASK'),
      tools: [],
      maxTurns: 0,
      permissionMode: 'dontAsk'
    });
    expect(definition.prompt).toContain('non-executable');
    expect(definition.disallowedTools).toContain('Agent');
    expect(definition.disallowedTools).toContain('Bash');
    expect(definition.disallowedTools).toContain('Write');
  });

  it('returns an SDK agents option-shape only when delegated candidates exist', () => {
    const bridge = createNonExecutableSubagentBridge({ session, opts });

    expect(bridge).toMatchObject({
      policyVersion: SUBAGENT_BRIDGE_POLICY_VERSION,
      rulingRef: SUBAGENT_BRIDGE_RULING_REF,
      sessionId: 'sess_bridge',
      delegatedSubagents: ['TASK'],
      agents: {
        TASK: {
          tools: [],
          disallowedTools: expect.arrayContaining(['Agent']),
          maxTurns: 0,
          permissionMode: 'dontAsk'
        }
      }
    });

    expect(
      createNonExecutableSubagentBridge({
        session,
        opts: { ...opts, delegatedSubagents: [] }
      })
    ).toBeUndefined();
  });

  it('hard-denies Agent preflight while recording child eligibility metadata', () => {
    const decision = evaluateSubagentPreflight({
      toolInput: {
        agent: 'TASK',
        prompt: 'run this'
      },
      eligibleAgentNames: ['TASK']
    });

    expect(decision).toEqual({
      allowed: false,
      reason: SUBAGENT_EXECUTION_DENIED_REASON,
      safeMetadata: {
        policyVersion: SUBAGENT_BRIDGE_POLICY_VERSION,
        rulingRef: SUBAGENT_BRIDGE_RULING_REF,
        denyClass: 'subagent-execution',
        executionPosture: 'hard-denied',
        nonExecutableBridge: true,
        requestedAgent: 'TASK',
        eligibleAgentNames: ['TASK'],
        eligibleChildDefinition: true
      }
    });

    expect(
      evaluateSubagentPreflight({
        toolInput: {
          agent: 'UNKNOWN'
        },
        eligibleAgentNames: ['TASK']
      }).safeMetadata
    ).toMatchObject({
      requestedAgent: 'UNKNOWN',
      eligibleChildDefinition: false
    });
  });
});
