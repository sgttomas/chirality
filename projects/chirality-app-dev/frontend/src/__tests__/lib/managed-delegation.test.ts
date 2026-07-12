import { mkdtemp, mkdir, readFile, rm, writeFile } from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import { afterEach, beforeEach, describe, expect, it } from 'vitest';
import type { SessionRecord } from '@chirality/harness-contract/types';
import {
  acknowledgeAgentUpdate,
  ManagedDelegationService,
  reportCoordinationNotice,
  sendAgentUpdate,
  type DelegateAgentInput
} from '../../lib/harness/managed-delegation';

let root = '';
let projectRoot = '';

async function agent(name: string, type: number, frontmatter = ''): Promise<void> {
  await writeFile(
    path.join(root, 'agents', `AGENT_${name}.md`),
    `---\ndescription: test\n${frontmatter}---\n# ${name}\nAGENT_TYPE: ${type}\n`,
    'utf8'
  );
}

function parent(persona: string, agentType: 0 | 1 | 2): SessionRecord {
  return {
    sessionId: `sess_${persona}`,
    projectRoot,
    persona,
    agentType,
    mode: 'workspaceWrite',
    createdAt: '2026-07-11T00:00:00.000Z',
    updatedAt: '2026-07-11T00:00:00.000Z'
  };
}

function request(overrides: Partial<DelegateAgentInput> = {}): DelegateAgentInput {
  return {
    executionRoot: 'execution',
    runId: 'RUN-1',
    planVersion: 'v1',
    selectionAuthority: 'AGENT_0',
    posture: 'MIXED',
    acceptedBasis: ['snapshot-1'],
    workGraph: { nodes: ['child'], edges: [] },
    childKind: 'named',
    agentName: 'WORKING_ITEMS',
    purpose: 'manage package',
    brief: 'Manage PKG-01 and return closure evidence.',
    declaredContext: ['execution/PKG-01'],
    tools: ['read'],
    writeTargets: ['execution/PKG-01'],
    dependencies: [],
    expectedOutput: 'package return',
    acceptanceCriteria: ['valid return'],
    requiredReturnMarkers: ['# Return'],
    contextSealed: true,
    pipelineRunApproved: true,
    approvalRef: 'HUMAN-1',
    ...overrides
  };
}

beforeEach(async () => {
  const temp = await mkdtemp(path.join(os.tmpdir(), 'managed-delegation-'));
  root = path.join(temp, 'instructions');
  projectRoot = path.join(temp, 'project');
  await mkdir(path.join(root, 'agents'), { recursive: true });
  await mkdir(path.join(root, 'docs'), { recursive: true });
  await mkdir(projectRoot, { recursive: true });
  await writeFile(path.join(root, 'README.md'), '# root\n', 'utf8');
  await writeFile(path.join(root, 'AGENTS.md'), '# agents\n', 'utf8');
  for (const name of ['DIRECTIVE', 'CONTRACT', 'SPEC', 'TYPES', 'PLAN']) {
    await writeFile(path.join(root, 'docs', `${name}.md`), `# ${name}\n`, 'utf8');
  }
  await agent('HELP_HUMAN', 0, 'subagents: WORKING_ITEMS, TASK, MISSING\n');
  await agent('WORKING_ITEMS', 1, 'subagents: TASK, WORKING_ITEMS\nallow_generalist_agent2: true\ntools: [read]\n');
  await agent('TASK', 2, 'tools: [read]\n');
  process.env.CHIRALITY_INSTRUCTION_ROOT = root;
  process.env.CHIRALITY_SESSION_ROOT = path.join(path.dirname(root), 'sessions');
});

afterEach(async () => {
  delete process.env.CHIRALITY_INSTRUCTION_ROOT;
  delete process.env.CHIRALITY_SESSION_ROOT;
  if (root) await rm(path.dirname(root), { recursive: true, force: true });
  root = '';
});

describe('managed delegation', () => {
  it('allows 0→named 1, persists the graph, and records instruction and brief hashes', async () => {
    const service = new ManagedDelegationService(async (launch) => ({
      sessionId: 'sess_child',
      status: 'COMPLETED',
      output: `# Return\n${launch.childPersona}`
    }));
    const result = await service.delegate(
      parent('HELP_HUMAN', 0),
      ['read'],
      request({ selectionAuthority: 'HUMAN', posture: 'TERMINAL_FAN_OUT_IN' })
    );
    expect(result).toMatchObject({ status: 'COMPLETED', sessionId: 'sess_child' });
    expect(result.instructionHash).toMatch(/^[a-f0-9]{64}$/);
    expect(result.briefHash).toMatch(/^[a-f0-9]{64}$/);
    const plan = await readFile(path.join(projectRoot, 'execution/_Coordination/AgentRuns/RUN-1/ORCHESTRATION_PLAN.md'), 'utf8');
    expect(plan).toContain('SelectionAuthority: HUMAN');
    expect(plan).toContain('Posture: TERMINAL_FAN_OUT_IN');
  });

  it('denies 0→2 and 1→1, but allows an authorized ephemeral generalist Agent 2', async () => {
    const service = new ManagedDelegationService(async () => ({
      sessionId: 'sess_child',
      status: 'COMPLETED',
      output: '# Return\ndone'
    }));
    await expect(
      service.delegate(parent('HELP_HUMAN', 0), ['read'], request({ childKind: 'named', agentName: 'TASK' }))
    ).rejects.toThrow('only to named Agent 1');
    await expect(
      service.delegate(parent('WORKING_ITEMS', 1), ['read'], request())
    ).rejects.toThrow('only to Agent 2');
    const result = await service.delegate(
      parent('WORKING_ITEMS', 1),
      ['read'],
      request({ runId: 'RUN-2', selectionAuthority: 'AGENT_1', childKind: 'generalist', agentName: undefined })
    );
    expect(result.status).toBe('COMPLETED');
    expect(result.instructionHash).toBeUndefined();
  });

  it('allows Agent 1→TASK and denies every delegation attempt from Agent 2', async () => {
    const service = new ManagedDelegationService(async () => ({
      sessionId: 'sess_task',
      status: 'COMPLETED',
      output: '# Return\ntask complete'
    }));
    const task = await service.delegate(
      parent('WORKING_ITEMS', 1),
      ['read'],
      request({
        runId: 'RUN-TASK',
        selectionAuthority: 'AGENT_1',
        childKind: 'task',
        agentName: 'TASK'
      })
    );
    expect(task).toMatchObject({ status: 'COMPLETED', sessionId: 'sess_task' });
    await expect(
      service.delegate(
        parent('TASK', 2),
        ['read'],
        request({ runId: 'RUN-A2', childKind: 'task', agentName: 'TASK' })
      )
    ).rejects.toThrow('Agent 2 may not delegate');
  });

  it('fails closed on missing governance metadata and capability inheritance', async () => {
    const service = new ManagedDelegationService(async () => ({ sessionId: 'x', status: 'COMPLETED', output: '# Return\nx' }));
    await expect(
      service.delegate(parent('HELP_HUMAN', 0), ['read'], request({ contextSealed: false }))
    ).rejects.toThrow('requires seal');
    await expect(
      service.delegate(parent('HELP_HUMAN', 0), ['read'], request({ tools: ['bash'] }))
    ).rejects.toThrow('exceed');
    await expect(
      service.delegate(parent('HELP_HUMAN', 0), ['read'], request({ runId: 'RUN-NO-BRIEF', brief: '' }))
    ).rejects.toThrow('brief must be non-empty');
    await expect(
      service.delegate(
        parent('HELP_HUMAN', 0),
        ['read'],
        request({ runId: 'RUN-NO-INSTRUCTION', agentName: 'MISSING' })
      )
    ).rejects.toThrow();
    await expect(
      service.delegate(
        parent('WORKING_ITEMS', 1),
        ['write'],
        request({
          runId: 'RUN-NO-WRITE-BOUNDARY',
          selectionAuthority: 'AGENT_1',
          childKind: 'generalist',
          agentName: undefined,
          tools: ['write'],
          writeTargets: []
        })
      )
    ).rejects.toThrow('require at least one declared write target');
  });

  it('fails closed on escaped context, escaped writes, and unbounded Bash', async () => {
    const service = new ManagedDelegationService(async () => ({
      sessionId: 'sess_child',
      status: 'COMPLETED',
      output: '# Return\ndone'
    }));
    await expect(
      service.delegate(
        parent('HELP_HUMAN', 0),
        ['read'],
        request({ runId: 'RUN-ESCAPE-READ', declaredContext: ['../outside'] })
      )
    ).rejects.toThrow('escapes the project root');
    await expect(
      service.delegate(
        parent('HELP_HUMAN', 0),
        ['read'],
        request({ runId: 'RUN-ESCAPE-WRITE', writeTargets: ['../outside'] })
      )
    ).rejects.toThrow('escapes the project root');
    await expect(
      service.delegate(
        parent('WORKING_ITEMS', 1),
        ['read', 'bash'],
        request({
          runId: 'RUN-SHELL',
          selectionAuthority: 'AGENT_1',
          childKind: 'generalist',
          agentName: undefined,
          tools: ['bash']
        })
      )
    ).rejects.toThrow('Managed Bash requires declared read and write scope');
  });

  it('rejects active exact and ancestor-overlapping sibling writes', async () => {
    const service = new ManagedDelegationService(async () => ({
      sessionId: 'sess_running',
      status: 'RUNNING',
      output: 'running'
    }));
    await service.delegate(parent('HELP_HUMAN', 0), ['read'], request({ runId: 'RUN-OVERLAP' }));
    await expect(
      service.delegate(
        parent('HELP_HUMAN', 0),
        ['read'],
        request({
          runId: 'RUN-OVERLAP',
          workGraph: undefined,
          writeTargets: ['execution/PKG-01/nested']
        })
      )
    ).rejects.toThrow('Concurrent write overlap');
  });

  it('keeps disjoint siblings active and reconstructs an existing run with a new service instance', async () => {
    const runningLauncher = async () => ({
      sessionId: 'sess_running',
      status: 'RUNNING' as const,
      output: 'running'
    });
    const firstService = new ManagedDelegationService(runningLauncher);
    await firstService.delegate(parent('HELP_HUMAN', 0), ['read'], request({ runId: 'RUN-RESTART' }));
    await firstService.delegate(
      parent('HELP_HUMAN', 0),
      ['read'],
      request({
        runId: 'RUN-RESTART',
        workGraph: undefined,
        declaredContext: ['execution/PKG-02'],
        writeTargets: ['execution/PKG-02']
      })
    );
    const restartedService = new ManagedDelegationService(runningLauncher);
    const third = await restartedService.delegate(
      parent('HELP_HUMAN', 0),
      ['read'],
      request({
        runId: 'RUN-RESTART',
        workGraph: undefined,
        declaredContext: ['execution/PKG-03'],
        writeTargets: ['execution/PKG-03']
      })
    );
    expect(third.status).toBe('RUNNING');
    const handoff = await readFile(
      path.join(projectRoot, 'execution/_Coordination/AgentRuns/RUN-RESTART/HANDOFF_STATE.md'),
      'utf8'
    );
    expect(handoff.match(/\| RUNNING \|/g)).toHaveLength(3);
  });

  it('isolates a failed node so independent work can continue', async () => {
    const failing = new ManagedDelegationService(async () => {
      throw new Error('child crashed');
    });
    await expect(
      failing.delegate(parent('HELP_HUMAN', 0), ['read'], request({ runId: 'RUN-FAILURE' }))
    ).rejects.toThrow('child crashed');
    const succeeding = new ManagedDelegationService(async () => ({
      sessionId: 'sess_independent',
      status: 'COMPLETED',
      output: '# Return\nindependent complete'
    }));
    const independent = await succeeding.delegate(
      parent('HELP_HUMAN', 0),
      ['read'],
      request({
        runId: 'RUN-FAILURE',
        workGraph: undefined,
        declaredContext: ['execution/PKG-02'],
        writeTargets: ['execution/PKG-02']
      })
    );
    expect(independent.status).toBe('COMPLETED');
  });

  it('rejects schema-invalid terminal returns and records the failed fan-in', async () => {
    const service = new ManagedDelegationService(async () => ({
      sessionId: 'sess_invalid',
      status: 'COMPLETED',
      output: 'missing required structure'
    }));
    await expect(
      service.delegate(parent('HELP_HUMAN', 0), ['read'], request({ runId: 'RUN-INVALID' }))
    ).rejects.toThrow('schema-invalid');
    const handoff = await readFile(
      path.join(projectRoot, 'execution/_Coordination/AgentRuns/RUN-INVALID/HANDOFF_STATE.md'),
      'utf8'
    );
    expect(handoff).toContain('FAILED');
  });

  it('persists child→parent notices and parent→child updates with acknowledgments', async () => {
    const service = new ManagedDelegationService(async () => ({ sessionId: 'sess_child', status: 'RUNNING', output: 'running' }));
    const parentRecord = { ...parent('HELP_HUMAN', 0), orchestrationRunId: 'RUN-3', executionRoot: 'execution', planVersion: 'v1' };
    const delegated = await service.delegate(parentRecord, ['read'], request({ runId: 'RUN-3' }));
    const child: SessionRecord = {
      ...parent('WORKING_ITEMS', 1),
      sessionId: 'sess_child',
      orchestrationRunId: 'RUN-3',
      executionRoot: 'execution',
      agentInstanceId: delegated.instanceId,
      parentSessionId: parentRecord.sessionId
    };
    const notice = await reportCoordinationNotice(child, {
      noticeType: 'DEPENDENCY',
      claimStatus: 'PROVISIONAL',
      summary: 'Sibling may depend on changed contract.',
      evidenceRefs: ['src/a.ts:10'],
      affectedScopes: ['PKG-02'],
      requestedAction: 'relay',
      blocking: false,
      humanDecisionRequired: false,
      acceptedBasisRef: 'snapshot-1'
    });
    await expect(
      reportCoordinationNotice(
        { ...child, sessionId: 'sess_forged_sibling' },
        {
          noticeType: 'DEPENDENCY',
          claimStatus: 'PROVISIONAL',
          summary: 'Attempt to bypass the direct-parent channel.',
          evidenceRefs: [],
          affectedScopes: [],
          requestedAction: 'relay',
          blocking: false,
          humanDecisionRequired: false,
          acceptedBasisRef: 'snapshot-1'
        }
      )
    ).rejects.toThrow('not the recorded direct child');
    await expect(
      sendAgentUpdate(
        { ...parentRecord, sessionId: 'sess_sibling' },
        {
          childInstanceId: delegated.instanceId,
          disposition: 'RELAY',
          summary: 'Attempt direct sibling update.',
          claimStatus: 'PROVISIONAL',
          evidenceRefs: [],
          consequential: false
        }
      )
    ).rejects.toThrow('only to a direct child');
    await expect(
      sendAgentUpdate(parentRecord, {
        childInstanceId: delegated.instanceId,
        noticeId: notice.noticeId,
        disposition: 'RELAY',
        summary: 'Illegally promote the claim.',
        claimStatus: 'ACCEPTED',
        evidenceRefs: ['src/a.ts:10'],
        consequential: false
      })
    ).rejects.toThrow('must preserve');
    await expect(
      sendAgentUpdate(parentRecord, {
        childInstanceId: delegated.instanceId,
        disposition: 'AMEND',
        summary: 'Consequential change.',
        claimStatus: 'VALIDATED',
        evidenceRefs: [],
        consequential: true,
        amendment: 'Change the objective.'
      })
    ).rejects.toThrow('requires humanRulingRef');
    const update = await sendAgentUpdate(parentRecord, {
      childInstanceId: delegated.instanceId,
      noticeId: notice.noticeId,
      disposition: 'RELAY',
      summary: 'Preserve provisional status.',
      claimStatus: 'PROVISIONAL',
      evidenceRefs: ['src/a.ts:10'],
      consequential: false
    });
    const acknowledgment = await acknowledgeAgentUpdate(child, {
      updateId: update.updateId,
      acknowledgment: 'INCORPORATED'
    });
    expect(acknowledgment.acknowledgment).toBe('INCORPORATED');
    expect(await readFile(path.join(projectRoot, `execution/_Coordination/AgentRuns/RUN-3/notices/${notice.noticeId}.json`), 'utf8')).toContain('PROVISIONAL');

    await sendAgentUpdate(parentRecord, {
      childInstanceId: delegated.instanceId,
      disposition: 'REPLAN',
      summary: 'Add a dependency-valid second stage.',
      claimStatus: 'VALIDATED',
      evidenceRefs: ['src/a.ts:10'],
      consequential: false,
      amendment: 'Use plan v2 for downstream dispatch.',
      planVersion: 'v2',
      selectionAuthority: 'AGENT_0',
      posture: 'MIXED',
      acceptedBasis: ['snapshot-1'],
      workGraph: { nodes: ['child', 'downstream'], edges: [['child', 'downstream']] }
    });
    const versioned = await readFile(
      path.join(projectRoot, 'execution/_Coordination/AgentRuns/RUN-3/plans/v2/WORK_GRAPH.json'),
      'utf8'
    );
    expect(versioned).toContain('downstream');
  });

  it('releases dependent work only from a valid return explicitly accepted by the manager', async () => {
    const service = new ManagedDelegationService(async () => ({ sessionId: 'sess_child', status: 'COMPLETED', output: '# Return\nvalid return' }));
    const first = await service.delegate(parent('HELP_HUMAN', 0), ['read'], request({ runId: 'RUN-4' }));
    await expect(service.delegate(
      parent('HELP_HUMAN', 0),
      ['read'],
      request({ runId: 'RUN-4', workGraph: undefined, dependencies: [first.instanceId] })
    )).rejects.toThrow('no manager acceptance');
    const second = await service.delegate(
      parent('HELP_HUMAN', 0),
      ['read'],
      request({ runId: 'RUN-4', workGraph: undefined, dependencies: [first.instanceId], acceptedPredecessors: [first.instanceId] })
    );
    expect(second.status).toBe('COMPLETED');
  });
});
