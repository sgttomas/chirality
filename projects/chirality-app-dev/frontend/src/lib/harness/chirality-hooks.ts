import type {
  HookCallback,
  HookCallbackMatcher,
  HookEvent,
  HookInput,
  HookJSONOutput,
  PostToolUseFailureHookInput,
  PostToolUseHookInput,
  PreToolUseHookInput
} from '@anthropic-ai/claude-agent-sdk';
import { createHash } from 'node:crypto';
import { lstat, readFile } from 'node:fs/promises';
import { createHarnessEvent } from './event-schema';
import { appendHarnessEvent } from './session-events';
import {
  summarizeToolDescriptor,
  summarizeToolError,
  summarizeToolInput,
  summarizeToolResult
} from './tool-evidence';
import { evaluateToolPathPolicy, type HarnessToolPathPolicyAllow } from './tool-path-policy';
import { getHarnessToolDescriptor, type HarnessToolDescriptor } from './tool-descriptor';

const WRITE_HOOK_TIMEOUT_SECONDS = 5;
const HASH_INLINE_LIMIT_BYTES = 1024 * 1024;

type WriteAttemptRecord = {
  pathMetadata: HarnessToolPathPolicyAllow;
  beforeState?: FileStateSummary;
};

type FileStateSummary = {
  exists: boolean;
  kind?: 'file' | 'directory' | 'other';
  byteLength?: number;
  sha256?: string;
  hashOmittedReason?: string;
  error?: string;
};

export type ChiralityToolHookInput = {
  sessionId: string;
  projectRoot: string;
  instructionRoot?: string;
  resolveDescriptor?: (toolName: string) => HarnessToolDescriptor | undefined;
};

function isRecord(value: unknown): value is Record<string, unknown> {
  return Boolean(value) && typeof value === 'object' && !Array.isArray(value);
}

function isWorkspaceWriteDescriptor(descriptor: HarnessToolDescriptor | undefined): boolean {
  return Boolean(descriptor?.permissions.includes('workspace-write'));
}

function readToolInput(input: HookInput): Record<string, unknown> {
  if (
    (input.hook_event_name === 'PreToolUse' ||
      input.hook_event_name === 'PostToolUse' ||
      input.hook_event_name === 'PostToolUseFailure') &&
    isRecord(input.tool_input)
  ) {
    return input.tool_input;
  }

  return {};
}

async function summarizeFileState(filePath: string | undefined): Promise<FileStateSummary | undefined> {
  if (!filePath) {
    return undefined;
  }

  try {
    const stats = await lstat(filePath);
    if (stats.isSymbolicLink()) {
      return {
        exists: true,
        kind: 'other',
        hashOmittedReason: 'symbolic-link'
      };
    }
    if (stats.isDirectory()) {
      return {
        exists: true,
        kind: 'directory'
      };
    }
    if (!stats.isFile()) {
      return {
        exists: true,
        kind: 'other'
      };
    }
    const summary: FileStateSummary = {
      exists: true,
      kind: 'file',
      byteLength: stats.size
    };
    if (stats.size > HASH_INLINE_LIMIT_BYTES) {
      return {
        ...summary,
        hashOmittedReason: 'file-too-large'
      };
    }
    const content = await readFile(filePath);
    return {
      ...summary,
      sha256: createHash('sha256').update(content).digest('hex')
    };
  } catch (error) {
    if ((error as NodeJS.ErrnoException).code === 'ENOENT') {
      return {
        exists: false
      };
    }
    return {
      exists: false,
      error: error instanceof Error ? error.message : 'unknown file-state failure'
    };
  }
}

async function appendHookEvent(input: {
  sessionId: string;
  type: 'hook.started' | 'hook.completed' | 'hook.failed';
  hookName: string;
  hookEvent: HookEvent;
  toolName?: string;
  toolUseId?: string;
  descriptor?: HarnessToolDescriptor;
  data?: Record<string, unknown>;
}): Promise<void> {
  await appendHarnessEvent(
    createHarnessEvent({
      sessionId: input.sessionId,
      type: input.type,
      data: {
        hookName: input.hookName,
        hookEvent: input.hookEvent,
        toolName: input.toolName,
        toolUseId: input.toolUseId,
        ...summarizeToolDescriptor(input.descriptor),
        ...input.data
      }
    })
  );
}

function allowPreToolUse(): HookJSONOutput {
  return {
    continue: true,
    hookSpecificOutput: {
      hookEventName: 'PreToolUse',
      permissionDecision: 'allow'
    }
  };
}

function blockPreToolUse(reason: string): HookJSONOutput {
  return {
    continue: false,
    decision: 'block',
    reason,
    hookSpecificOutput: {
      hookEventName: 'PreToolUse',
      permissionDecision: 'deny',
      permissionDecisionReason: reason
    }
  };
}

export function createChiralityToolHooks(input: ChiralityToolHookInput): Partial<
  Record<HookEvent, HookCallbackMatcher[]>
> {
  const attempts = new Map<string, WriteAttemptRecord>();
  const resolveDescriptor = input.resolveDescriptor ?? getHarnessToolDescriptor;

  const preToolUse: HookCallback = async (hookInput) => {
    if (hookInput.hook_event_name !== 'PreToolUse') {
      return { continue: true };
    }

    const preInput = hookInput as PreToolUseHookInput;
    const descriptor = resolveDescriptor(preInput.tool_name);
    if (!isWorkspaceWriteDescriptor(descriptor)) {
      return { continue: true };
    }

    const hookName = 'chirality.write.pre_tool_use';
    const eventBase = {
      sessionId: input.sessionId,
      hookName,
      hookEvent: 'PreToolUse' as const,
      toolName: preInput.tool_name,
      toolUseId: preInput.tool_use_id,
      descriptor
    };

    try {
      await appendHookEvent({
        ...eventBase,
        type: 'hook.started',
        data: {
          inputMetadata: summarizeToolInput(preInput.tool_input)
        }
      });

      const pathPolicy = await evaluateToolPathPolicy({
        descriptor,
        projectRoot: input.projectRoot,
        instructionRoot: input.instructionRoot,
        toolInput: readToolInput(preInput)
      });

      if (!pathPolicy.allowed) {
        await appendHookEvent({
          ...eventBase,
          type: 'hook.completed',
          data: {
            decision: 'block',
            reason: pathPolicy.reason,
            safeMetadata: pathPolicy.metadata
          }
        });
        return blockPreToolUse(pathPolicy.reason);
      }

      const beforeState = await summarizeFileState(pathPolicy.metadata.resolvedPath);
      attempts.set(preInput.tool_use_id, {
        pathMetadata: pathPolicy.metadata,
        beforeState
      });

      await appendHookEvent({
        ...eventBase,
        type: 'hook.completed',
        data: {
          decision: 'approve',
          pathMetadata: pathPolicy.metadata,
          beforeState,
          recordsDiff: descriptor?.provenance.recordsDiff
        }
      });
      return allowPreToolUse();
    } catch (error) {
      const message = error instanceof Error ? error.message : 'unknown write hook failure';
      try {
        await appendHookEvent({
          ...eventBase,
          type: 'hook.failed',
          data: {
            error: summarizeToolError(error),
            decision: 'block'
          }
        });
      } catch {
        // The pre-tool hook still fails closed if audit persistence is unavailable.
      }
      return blockPreToolUse(`Chirality write hook failed closed. ${message}`);
    }
  };

  const postToolUse: HookCallback = async (hookInput) => {
    if (hookInput.hook_event_name !== 'PostToolUse') {
      return { continue: true };
    }

    const postInput = hookInput as PostToolUseHookInput;
    const descriptor = resolveDescriptor(postInput.tool_name);
    if (!isWorkspaceWriteDescriptor(descriptor)) {
      return { continue: true };
    }

    const hookName = 'chirality.write.post_tool_use';
    const attempt = attempts.get(postInput.tool_use_id);
    await appendHookEvent({
      sessionId: input.sessionId,
      type: 'hook.started',
      hookName,
      hookEvent: 'PostToolUse',
      toolName: postInput.tool_name,
      toolUseId: postInput.tool_use_id,
      descriptor
    });

    const afterState = await summarizeFileState(attempt?.pathMetadata.resolvedPath);
    await appendHookEvent({
      sessionId: input.sessionId,
      type: 'hook.completed',
      hookName,
      hookEvent: 'PostToolUse',
      toolName: postInput.tool_name,
      toolUseId: postInput.tool_use_id,
      descriptor,
      data: {
        pathMetadata: attempt?.pathMetadata,
        beforeState: attempt?.beforeState,
        afterState,
        durationMs: postInput.duration_ms,
        resultMetadata: summarizeToolResult(postInput.tool_response, descriptor),
        recordsDiff: descriptor?.provenance.recordsDiff
      }
    });
    attempts.delete(postInput.tool_use_id);
    return {
      continue: true,
      hookSpecificOutput: {
        hookEventName: 'PostToolUse'
      }
    };
  };

  const postToolUseFailure: HookCallback = async (hookInput) => {
    if (hookInput.hook_event_name !== 'PostToolUseFailure') {
      return { continue: true };
    }

    const failureInput = hookInput as PostToolUseFailureHookInput;
    const descriptor = resolveDescriptor(failureInput.tool_name);
    if (!isWorkspaceWriteDescriptor(descriptor)) {
      return { continue: true };
    }

    const attempt = attempts.get(failureInput.tool_use_id);
    await appendHookEvent({
      sessionId: input.sessionId,
      type: 'hook.failed',
      hookName: 'chirality.write.post_tool_use_failure',
      hookEvent: 'PostToolUseFailure',
      toolName: failureInput.tool_name,
      toolUseId: failureInput.tool_use_id,
      descriptor,
      data: {
        pathMetadata: attempt?.pathMetadata,
        beforeState: attempt?.beforeState,
        durationMs: failureInput.duration_ms,
        error: failureInput.error,
        interrupted: failureInput.is_interrupt
      }
    });
    attempts.delete(failureInput.tool_use_id);
    return {
      continue: true,
      hookSpecificOutput: {
        hookEventName: 'PostToolUseFailure'
      }
    };
  };

  return {
    PreToolUse: [
      {
        timeout: WRITE_HOOK_TIMEOUT_SECONDS,
        hooks: [preToolUse]
      }
    ],
    PostToolUse: [
      {
        timeout: WRITE_HOOK_TIMEOUT_SECONDS,
        hooks: [postToolUse]
      }
    ],
    PostToolUseFailure: [
      {
        timeout: WRITE_HOOK_TIMEOUT_SECONDS,
        hooks: [postToolUseFailure]
      }
    ]
  };
}
