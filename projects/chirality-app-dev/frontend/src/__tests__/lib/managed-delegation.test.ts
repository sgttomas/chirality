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

function parent(persona: string, agentType: 0 | 1): SessionRecord {
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
  await agent('HELP_HUMAN', 0, 'subagents: WORKING_ITEMS, TASK\n');
  await agent('WORKING_ITEMS', 1, 'subagents: TASK, WORKING_ITEMS\nallow_generalist_agent2: true\ntools: [read]\n');
  await agent('TASK', 2);
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
    const result = await service.delegate(parent('HELP_HUMAN', 0), ['read'], request());
    expect(result).toMatchObject({ status: 'COMPLETED', sessionId: 'sess_child' });
    expect(result.instructionHash).toMatch(/^[a-f0-9]{64}$/);
    expect(result.briefHash).toMatch(/^[a-f0-9]{64}$/);
    const plan = await readFile(path.join(projectRoot, 'execution/_Coordination/AgentRuns/RUN-1/ORCHESTRATION_PLAN.md'), 'utf8');
    expect(plan).toContain('Posture: MIXED');
  });

  it('denies 0→2 and 1→1, but allows an authorized ephemeral generalist Agent 2', async () => {
    const service = new ManagedDelegationService(async () => ({
      sessionId: 'sess_child',
      status: 'COMPLETED',
      output: 'done'
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

  it('fails closed on missing governance metadata and capability inheritance', async () => {
    const service = new ManagedDelegationService(async () => ({ sessionId: 'x', status: 'COMPLETED', output: 'x' }));
    await expect(
      service.delegate(parent('HELP_HUMAN', 0), ['read'], request({ contextSealed: false }))
    ).rejects.toThrow('requires seal');
    await expect(
      service.delegate(parent('HELP_HUMAN', 0), ['read'], request({ tools: ['bash'] }))
    ).rejects.toThrow('exceed');
  });

  it('persists child→parent notices and parent→child updates with acknowledgments', async () => {
    const service = new ManagedDelegationService(async () => ({ sessionId: 'sess_child', status: 'COMPLETED', output: 'done' }));
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
  });

  it('releases dependent work only from a valid return explicitly accepted by the manager', async () => {
    const service = new ManagedDelegationService(async () => ({ sessionId: 'sess_child', status: 'COMPLETED', output: 'valid return' }));
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
