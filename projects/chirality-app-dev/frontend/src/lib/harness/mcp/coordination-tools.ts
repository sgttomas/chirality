import {
  tool,
  type SdkMcpToolDefinition
} from '@anthropic-ai/claude-agent-sdk';
import type { CallToolResult } from '@modelcontextprotocol/sdk/types.js';
import { z } from 'zod/v4';
import { readFile, writeFile } from 'node:fs/promises';
import path from 'node:path';
import type { SessionRecord } from '@chirality/harness-contract/types';
import {
  acknowledgeAgentUpdate,
  ManagedDelegationService,
  reportCoordinationNotice,
  sendAgentUpdate,
  type DelegateAgentInput,
  type ManagedChildLaunch
} from '../managed-delegation';
import { parseAgentType, readAgentInstruction } from '../agent-instruction';

export type CoordinationMcpContext = {
  projectRoot: string;
  sessionId: string;
  persona: string;
  mode: string;
  tools: readonly string[];
};

function jsonResult(value: unknown): CallToolResult {
  return { content: [{ type: 'text', text: JSON.stringify(value, null, 2) }] };
}

async function parentSession(context: CoordinationMcpContext): Promise<SessionRecord> {
  const { getHarnessRuntime } = await import('../runtime');
  return getHarnessRuntime().sessionManager.getById(context.sessionId);
}

async function launchManagedChild(input: ManagedChildLaunch) {
  const { getHarnessRuntime } = await import('../runtime');
  const runtime = getHarnessRuntime();
  const parentInstruction = await readAgentInstruction(input.parent.persona);
  const parentAgentType = parseAgentType(parentInstruction.content);
  if (parentAgentType !== 0 && parentAgentType !== 1) {
    throw new Error('Managed parent must be Agent 0 or Agent 1');
  }
  const child = await runtime.sessionManager.create({
    projectRoot: input.parent.projectRoot,
    persona: input.childPersona,
    mode: input.parent.mode
  });
  await runtime.sessionManager.save(child.sessionId, {
    orchestrationRunId: input.runId,
    executionRoot: input.parent.executionRoot ?? 'execution',
    agentInstanceId: input.childInstanceId,
    parentSessionId: input.parent.sessionId,
    parentInstanceId: input.parent.agentInstanceId,
    parentAgentType,
    agentType: input.childAgentType,
    childKind: input.childKind,
    planVersion: input.parent.planVersion,
    approvalRef: input.approvalRef,
    instructionPath: input.instructionPath,
    instructionHash: input.instructionHash,
    briefHash: input.briefHash,
    declaredTools: input.tools,
    allowedWriteTargets: input.writeTargets,
    childRunStatus: 'RUNNING'
  });

  const execute = async () => {
    let output = '';
    let failed = false;
    const turn = await runtime.turnEngine.runTurn({
      sessionId: child.sessionId,
      message: input.brief,
      attachments: [],
      opts: {
        persona: input.childPersona,
        mode: input.parent.mode,
        tools: input.tools,
        subagentGovernance: {
          contextSealed: true,
          pipelineRunApproved: true,
          approvalRef: input.approvalRef,
          approvedBy: input.parent.persona
        }
      }
    });
    for await (const event of turn.events) {
      if (event.type === 'chat:complete') output = event.data.text;
      if (event.type === 'turn:error') {
        failed = true;
        output = output || event.data.message;
      }
      if (event.type === 'process:exit' && (event.data.exitCode !== 0 || event.data.error)) {
        failed = true;
        output = output || event.data.error || `Child exited ${event.data.exitCode}`;
      }
    }
    const status = failed ? 'FAILED' : 'COMPLETED';
    await runtime.sessionManager.save(child.sessionId, { childRunStatus: status });
    return { sessionId: child.sessionId, status, output: output || '(child returned no chat output)' } as const;
  };

  if (input.executionMode === 'BACKGROUND') {
    const instanceRoot = path.join(
      input.parent.projectRoot,
      input.parent.executionRoot ?? 'execution',
      '_Coordination',
      'AgentRuns',
      input.runId,
      'instances',
      input.childInstanceId
    );
    void execute()
      .then(async (result) => {
        await writeFile(path.join(instanceRoot, 'RETURN.md'), `${result.output.trimEnd()}\n`, 'utf8');
        const current = JSON.parse(await readFile(path.join(instanceRoot, 'STATUS.json'), 'utf8')) as Record<string, unknown>;
        await writeFile(path.join(instanceRoot, 'STATUS.json'), `${JSON.stringify({ ...current, childSessionId: result.sessionId, status: result.status, outputArtifact: path.join(instanceRoot, 'RETURN.md') }, null, 2)}\n`, 'utf8');
      })
      .catch(async (error) => {
        const current = JSON.parse(await readFile(path.join(instanceRoot, 'STATUS.json'), 'utf8')) as Record<string, unknown>;
        await writeFile(path.join(instanceRoot, 'STATUS.json'), `${JSON.stringify({ ...current, childSessionId: child.sessionId, status: 'FAILED', error: error instanceof Error ? error.message : 'background child failed' }, null, 2)}\n`, 'utf8');
        await runtime.sessionManager.save(child.sessionId, { childRunStatus: 'FAILED' });
      });
    return { sessionId: child.sessionId, status: 'RUNNING', output: 'Managed child launched in background.' } as const;
  }

  return execute();
}

const delegateSchema = {
  executionRoot: z.string().min(1),
  runId: z.string().min(1),
  planVersion: z.string().min(1),
  selectionAuthority: z.enum(['HUMAN', 'AGENT_0', 'AGENT_1']),
  posture: z.enum(['TERMINAL_FAN_OUT_IN', 'SUPERVISED_MANY_TO_MANY', 'MIXED']),
  acceptedBasis: z.array(z.string()),
  workGraph: z.record(z.string(), z.unknown()).optional(),
  childKind: z.enum(['named', 'task', 'generalist']),
  agentName: z.string().optional(),
  purpose: z.string().min(1),
  brief: z.string().min(1),
  declaredContext: z.array(z.string()),
  tools: z.array(z.string()),
  writeTargets: z.array(z.string()),
  dependencies: z.array(z.string()),
  acceptedPredecessors: z.array(z.string()).optional(),
  expectedOutput: z.string().min(1),
  acceptanceCriteria: z.array(z.string()),
  executionMode: z.enum(['WAIT', 'BACKGROUND']).optional(),
  contextSealed: z.boolean(),
  pipelineRunApproved: z.boolean(),
  approvalRef: z.string().min(1)
};

export function buildCoordinationMcpTools(input: {
  context: CoordinationMcpContext;
  allowedToolNames: ReadonlySet<string>;
}): SdkMcpToolDefinition<any>[] {
  const tools: SdkMcpToolDefinition<any>[] = [];
  if (input.allowedToolNames.has('mcp__chirality__delegate_agent')) {
    tools.push(tool(
      'delegate_agent',
      'Launch one governed direct child session and persist its orchestration records.',
      delegateSchema,
      async (args) => {
        const runtimeModule = await import('../runtime');
        const runtime = runtimeModule.getHarnessRuntime();
        const existing = await runtime.sessionManager.getById(input.context.sessionId);
        if (existing.orchestrationRunId && existing.orchestrationRunId !== args.runId) {
          throw new Error('Managed child must remain in the parent orchestration run');
        }
        const parent = await runtime.sessionManager.save(existing.sessionId, {
          orchestrationRunId: args.runId,
          executionRoot: args.executionRoot,
          planVersion: args.planVersion,
          declaredTools: [...input.context.tools]
        });
        const service = new ManagedDelegationService(launchManagedChild);
        return jsonResult(await service.delegate(parent, input.context.tools, args as DelegateAgentInput));
      }
    ));
  }
  if (input.allowedToolNames.has('mcp__chirality__report_coordination_notice')) {
    tools.push(tool(
      'report_coordination_notice',
      'Report a typed coordination notice to the direct parent.',
      {
        noticeType: z.string().min(1),
        claimStatus: z.enum(['PROVISIONAL', 'VALIDATED', 'ACCEPTED', 'DISPUTED']),
        summary: z.string().min(1),
        evidenceRefs: z.array(z.string()),
        affectedScopes: z.array(z.string()),
        requestedAction: z.string().min(1),
        blocking: z.boolean(),
        humanDecisionRequired: z.boolean(),
        acceptedBasisRef: z.string().min(1)
      },
      async (args) => jsonResult(await reportCoordinationNotice(await parentSession(input.context), args))
    ));
  }
  if (input.allowedToolNames.has('mcp__chirality__send_agent_update')) {
    tools.push(tool(
      'send_agent_update',
      'Relay information or a versioned brief amendment to one direct child.',
      {
        childInstanceId: z.string().min(1),
        noticeId: z.string().optional(),
        disposition: z.enum(['RECORD', 'RELAY', 'AMEND', 'HOLD', 'REPLAN', 'ESCALATE', 'ROUTE']),
        summary: z.string().min(1),
        claimStatus: z.enum(['PROVISIONAL', 'VALIDATED', 'ACCEPTED', 'DISPUTED']),
        evidenceRefs: z.array(z.string()),
        consequential: z.boolean(),
        humanRulingRef: z.string().optional(),
        amendment: z.string().optional()
      },
      async (args) => jsonResult(await sendAgentUpdate(await parentSession(input.context), args))
    ));
  }
  if (input.allowedToolNames.has('mcp__chirality__ack_agent_update')) {
    tools.push(tool(
      'ack_agent_update',
      'Acknowledge an update from the direct parent.',
      {
        updateId: z.string().min(1),
        acknowledgment: z.enum(['INCORPORATED', 'NO_EFFECT', 'BLOCKED', 'CONFLICT', 'HUMAN_DECISION_REQUIRED']),
        summary: z.string().optional()
      },
      async (args) => jsonResult(await acknowledgeAgentUpdate(await parentSession(input.context), args))
    ));
  }
  return tools;
}
