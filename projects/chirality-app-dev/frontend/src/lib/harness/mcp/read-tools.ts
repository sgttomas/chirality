import {
  createSdkMcpServer,
  tool,
  type McpServerConfig,
  type McpSdkServerConfigWithInstance
} from '@anthropic-ai/claude-agent-sdk';
import type { CallToolResult } from '@modelcontextprotocol/sdk/types.js';
import { realpath } from 'node:fs/promises';
import path from 'node:path';
import { z } from 'zod/v4';
import { previewScaffoldExecutionRoot } from '../scaffold';
import type { CoordinationMode } from '../scaffold';
import { createHarnessEvent } from '../event-schema';
import {
  readDeliverableDependencies,
  readDeliverableStatus
} from '../../workspace/deliverable-contracts';
import { normalizeProjectRoot, scanProjectScopes } from '../../workspace/filesystem';
import { HarnessError } from '../errors';
import { appendHarnessEvent } from '../session-events';
import {
  summarizeToolDescriptor,
  summarizeToolError,
  summarizeToolInput,
  summarizeToolResult
} from '../tool-evidence';
import { getHarnessToolDescriptor } from '../tool-descriptor';
import {
  CHIRALITY_MCP_SERVER_NAME,
  isChiralityMcpAllowedToolName,
  toChiralityMcpAllowedToolName,
  type ChiralityMcpAllowedToolName,
  type ChiralityMcpReadToolName
} from './tool-names';

export type ChiralityReadMcpContext = {
  projectRoot: string;
  sessionId: string;
};

export type StatusReadArgs = {
  deliverablePath: string;
};

export type DependenciesReadArgs = {
  deliverablePath: string;
};

export type ScopeScanArgs = Record<string, never>;

export type ScaffoldPreviewArgs = {
  executionRoot: string;
  decompositionPath: string;
  projectName?: string;
  coordinationMode?: string;
};

function jsonToolResult(value: unknown): CallToolResult {
  return {
    content: [
      {
        type: 'text',
        text: JSON.stringify(value, null, 2)
      }
    ]
  };
}

async function runReadMcpToolWithEvidence(input: {
  context: ChiralityReadMcpContext;
  toolName: ChiralityMcpReadToolName;
  args: unknown;
  execute: () => Promise<CallToolResult>;
}): Promise<CallToolResult> {
  const descriptor = getHarnessToolDescriptor(input.toolName);
  const adapterToolName =
    descriptor?.adapter.claudeAgentSdk?.toolName ?? toChiralityMcpAllowedToolName(input.toolName);
  const eventBase = {
    source: 'chirality-mcp',
    adapterToolName,
    toolName: descriptor?.name ?? input.toolName,
    ...summarizeToolDescriptor(descriptor)
  };
  const startedAt = Date.now();

  await appendHarnessEvent(
    createHarnessEvent({
      sessionId: input.context.sessionId,
      type: 'tool.started',
      data: {
        ...eventBase,
        inputMetadata: summarizeToolInput(input.args)
      }
    })
  );

  try {
    const result = await input.execute();
    await appendHarnessEvent(
      createHarnessEvent({
        sessionId: input.context.sessionId,
        type: 'tool.completed',
        data: {
          ...eventBase,
          durationMs: Date.now() - startedAt,
          resultMetadata: summarizeToolResult(result, descriptor)
        }
      })
    );
    return result;
  } catch (error) {
    try {
      await appendHarnessEvent(
        createHarnessEvent({
          sessionId: input.context.sessionId,
          type: 'tool.failed',
          data: {
            ...eventBase,
            failureSource: 'handler',
            durationMs: Date.now() - startedAt,
            error: summarizeToolError(error)
          }
        })
      );
    } catch {
      // Preserve the original tool failure if failure-evidence persistence also fails.
    }
    throw error;
  }
}

function assertLexicallyWithinProjectRoot(input: {
  projectRoot: string;
  candidatePath: string;
  field: string;
}): string {
  const projectRoot = path.resolve(input.projectRoot);
  const candidatePath = path.resolve(input.candidatePath);
  const relative = path.relative(projectRoot, candidatePath);
  if (relative.startsWith('..') || path.isAbsolute(relative)) {
    throw new HarnessError(
      'INVALID_REQUEST',
      400,
      `${input.field} must resolve inside projectRoot`,
      {
        projectRoot,
        [input.field]: candidatePath
      }
    );
  }
  return candidatePath;
}

async function assertExistingPathWithinProjectRoot(input: {
  projectRoot: string;
  candidatePath: string;
  field: string;
}): Promise<string> {
  const projectRoot = await realpath(path.resolve(input.projectRoot));
  const candidatePath = await realpath(path.resolve(input.candidatePath));
  const relative = path.relative(projectRoot, candidatePath);
  if (relative.startsWith('..') || path.isAbsolute(relative)) {
    throw new HarnessError(
      'INVALID_REQUEST',
      400,
      `${input.field} must resolve inside projectRoot`,
      {
        projectRoot,
        [input.field]: candidatePath
      }
    );
  }
  return candidatePath;
}

export async function statusReadTool(
  context: ChiralityReadMcpContext,
  args: StatusReadArgs
): Promise<CallToolResult> {
  return runReadMcpToolWithEvidence({
    context,
    toolName: 'status_read',
    args,
    execute: async () =>
      jsonToolResult(await readDeliverableStatus(context.projectRoot, args.deliverablePath))
  });
}

export async function dependenciesReadTool(
  context: ChiralityReadMcpContext,
  args: DependenciesReadArgs
): Promise<CallToolResult> {
  return runReadMcpToolWithEvidence({
    context,
    toolName: 'deps_read',
    args,
    execute: async () =>
      jsonToolResult(await readDeliverableDependencies(context.projectRoot, args.deliverablePath))
  });
}

export async function scopeScanTool(
  context: ChiralityReadMcpContext,
  _args: ScopeScanArgs = {}
): Promise<CallToolResult> {
  return runReadMcpToolWithEvidence({
    context,
    toolName: 'scope_scan',
    args: _args,
    execute: async () => {
      const projectRoot = await normalizeProjectRoot(context.projectRoot);
      return jsonToolResult({
        projectRoot,
        scannedAt: new Date().toISOString(),
        ...(await scanProjectScopes(projectRoot))
      });
    }
  });
}

export async function scaffoldPreviewTool(
  context: ChiralityReadMcpContext,
  args: ScaffoldPreviewArgs
): Promise<CallToolResult> {
  return runReadMcpToolWithEvidence({
    context,
    toolName: 'scaffold_preview',
    args,
    execute: async () => {
      const executionRoot = assertLexicallyWithinProjectRoot({
        projectRoot: context.projectRoot,
        candidatePath: args.executionRoot,
        field: 'executionRoot'
      });
      const decompositionPath = await assertExistingPathWithinProjectRoot({
        projectRoot: context.projectRoot,
        candidatePath: args.decompositionPath,
        field: 'decompositionPath'
      });

      return jsonToolResult(
        await previewScaffoldExecutionRoot({
          executionRoot,
          decompositionPath,
          projectName: args.projectName,
          coordinationMode: args.coordinationMode as CoordinationMode | undefined
        })
      );
    }
  });
}

export function createChiralityReadMcpServer(
  context: ChiralityReadMcpContext
): McpSdkServerConfigWithInstance {
  return createSdkMcpServer({
    name: CHIRALITY_MCP_SERVER_NAME,
    version: '1.0.0',
    instructions:
      'Chirality read-only MCP tools expose project status, dependency, scope, and scaffold-preview data. They do not write files, run shell commands, or access networks.',
    tools: [
      tool(
        'status_read',
        'Read parsed lifecycle state from a deliverable _STATUS.md file.',
        {
          deliverablePath: z.string().min(1)
        },
        (args) => statusReadTool(context, args)
      ),
      tool(
        'deps_read',
        'Read parsed dependency rows and warnings from a deliverable Dependencies.csv file.',
        {
          deliverablePath: z.string().min(1)
        },
        (args) => dependenciesReadTool(context, args)
      ),
      tool(
        'scope_scan',
        'Scan project-root deliverable and knowledge-type scopes without reading document bodies.',
        {},
        (args) => scopeScanTool(context, args)
      ),
      tool(
        'scaffold_preview',
        'Preview execution-root scaffold paths from a decomposition markdown file without writing files.',
        {
          executionRoot: z.string().min(1),
          decompositionPath: z.string().min(1),
          projectName: z.string().optional(),
          coordinationMode: z.string().optional()
        },
        (args) => scaffoldPreviewTool(context, args)
      )
    ]
  });
}

export function createChiralityReadMcpServers(input: {
  context: ChiralityReadMcpContext;
  allowedToolNames: readonly string[];
}): Record<string, McpServerConfig> {
  const hasAllowedReadMcpTool = input.allowedToolNames.some(isChiralityMcpAllowedToolName);
  if (!hasAllowedReadMcpTool) {
    return {};
  }

  return {
    [CHIRALITY_MCP_SERVER_NAME]: createChiralityReadMcpServer(input.context)
  };
}

export function filterChiralityMcpAllowedToolNames(
  toolNames: readonly string[]
): ChiralityMcpAllowedToolName[] {
  return toolNames.filter(isChiralityMcpAllowedToolName);
}
