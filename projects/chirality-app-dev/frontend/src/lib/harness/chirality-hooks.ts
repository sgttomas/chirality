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
  summarizeShellResultStreams,
  summarizeToolResult
} from './tool-evidence';
import { persistToolResultArtifact } from './tool-result-artifacts';
import { evaluateToolPathPolicy, type HarnessToolPathPolicyAllow } from './tool-path-policy';
import {
  DEFAULT_BASH_TIMEOUT_MS,
  evaluateShellCommandPolicy
} from './tool-shell-policy';
import { getHarnessToolDescriptor, type HarnessToolDescriptor } from './tool-descriptor';
import { evaluateSubagentPreflight } from './subagent-bridge';

const WRITE_HOOK_TIMEOUT_SECONDS = 5;
const SHELL_HOOK_TIMEOUT_SECONDS = 5;
const HASH_INLINE_LIMIT_BYTES = 1024 * 1024;

type ToolAttemptRecord = {
  policyMetadata?: Record<string, unknown>;
  pathMetadata?: HarnessToolPathPolicyAllow;
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

function isShellDescriptor(descriptor: HarnessToolDescriptor | undefined): boolean {
  return Boolean(descriptor?.permissions.includes('shell'));
}

function isSubagentDescriptor(descriptor: HarnessToolDescriptor | undefined): boolean {
  return Boolean(descriptor?.permissions.includes('subagent'));
}

function isGovernedHookDescriptor(descriptor: HarnessToolDescriptor | undefined): boolean {
  return (
    isWorkspaceWriteDescriptor(descriptor) || isShellDescriptor(descriptor) || isSubagentDescriptor(descriptor)
  );
}

function getHookFamily(descriptor: HarnessToolDescriptor | undefined): 'shell' | 'write' | 'subagent' {
  if (isSubagentDescriptor(descriptor)) {
    return 'subagent';
  }
  return isShellDescriptor(descriptor) ? 'shell' : 'write';
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

function allowPreToolUse(updatedInput?: Record<string, unknown>): HookJSONOutput {
  return {
    continue: true,
    hookSpecificOutput: {
      hookEventName: 'PreToolUse',
      permissionDecision: 'allow',
      updatedInput
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
  const attempts = new Map<string, ToolAttemptRecord>();
  const resolveDescriptor = input.resolveDescriptor ?? getHarnessToolDescriptor;

  const preToolUse: HookCallback = async (hookInput) => {
    if (hookInput.hook_event_name !== 'PreToolUse') {
      return { continue: true };
    }

    const preInput = hookInput as PreToolUseHookInput;
    const descriptor = resolveDescriptor(preInput.tool_name);
    if (!isGovernedHookDescriptor(descriptor)) {
      return { continue: true };
    }

    const hookFamily = getHookFamily(descriptor);
    const hookName = `chirality.${hookFamily}.pre_tool_use`;
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

      if (isSubagentDescriptor(descriptor)) {
        const preflight = evaluateSubagentPreflight({
          toolInput: readToolInput(preInput)
        });

        await appendHookEvent({
          ...eventBase,
          type: 'hook.completed',
          data: {
            decision: 'block',
            reason: preflight.reason,
            safeMetadata: preflight.safeMetadata
          }
        });
        return blockPreToolUse(preflight.reason);
      }

      if (isShellDescriptor(descriptor)) {
        const shellPolicy = await evaluateShellCommandPolicy({
          descriptor,
          projectRoot: input.projectRoot,
          instructionRoot: input.instructionRoot,
          toolInput: readToolInput(preInput)
        });

        if (!shellPolicy.allowed) {
          await appendHookEvent({
            ...eventBase,
            type: 'hook.completed',
            data: {
              decision: 'block',
              reason: shellPolicy.reason,
              safeMetadata: shellPolicy.metadata
            }
          });
          return blockPreToolUse(shellPolicy.reason);
        }

        attempts.set(preInput.tool_use_id, {
          policyMetadata: shellPolicy.metadata
        });

        await appendHookEvent({
          ...eventBase,
          type: 'hook.completed',
          data: {
            decision: 'approve',
            shellMetadata: shellPolicy.metadata,
            defaultTimeoutMs: DEFAULT_BASH_TIMEOUT_MS,
            resultBudget: descriptor?.resultBudget
          }
        });
        return allowPreToolUse(shellPolicy.updatedInput);
      }

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
      const message = error instanceof Error ? error.message : 'unknown governed hook failure';
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
      return blockPreToolUse(`Chirality ${hookFamily} hook failed closed. ${message}`);
    }
  };

  const postToolUse: HookCallback = async (hookInput) => {
    if (hookInput.hook_event_name !== 'PostToolUse') {
      return { continue: true };
    }

    const postInput = hookInput as PostToolUseHookInput;
    const descriptor = resolveDescriptor(postInput.tool_name);
    if (!isGovernedHookDescriptor(descriptor)) {
      return { continue: true };
    }

    const hookFamily = getHookFamily(descriptor);
    const hookName = `chirality.${hookFamily}.post_tool_use`;
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

    const afterState = isShellDescriptor(descriptor)
      ? undefined
      : await summarizeFileState(attempt?.pathMetadata?.resolvedPath);
    const resultMetadata = summarizeToolResult(postInput.tool_response, descriptor);
    const artifactMetadata = isShellDescriptor(descriptor)
      ? await persistToolResultArtifact({
          sessionId: input.sessionId,
          toolUseId: postInput.tool_use_id,
          toolName: postInput.tool_name,
          descriptor,
          result: postInput.tool_response
        })
      : undefined;
    await appendHookEvent({
      sessionId: input.sessionId,
      type: 'hook.completed',
      hookName,
      hookEvent: 'PostToolUse',
      toolName: postInput.tool_name,
      toolUseId: postInput.tool_use_id,
      descriptor,
      data: {
        shellMetadata: attempt?.policyMetadata,
        pathMetadata: attempt?.pathMetadata,
        beforeState: attempt?.beforeState,
        afterState,
        durationMs: postInput.duration_ms,
        resultMetadata: {
          ...resultMetadata,
          outputPersisted: Boolean(artifactMetadata)
        },
        shellResultMetadata: isShellDescriptor(descriptor)
          ? summarizeShellResultStreams(postInput.tool_response)
          : undefined,
        artifactMetadata,
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
    if (!isGovernedHookDescriptor(descriptor)) {
      return { continue: true };
    }

    const attempt = attempts.get(failureInput.tool_use_id);
    const hookFamily = getHookFamily(descriptor);
    await appendHookEvent({
      sessionId: input.sessionId,
      type: 'hook.failed',
      hookName: `chirality.${hookFamily}.post_tool_use_failure`,
      hookEvent: 'PostToolUseFailure',
      toolName: failureInput.tool_name,
      toolUseId: failureInput.tool_use_id,
      descriptor,
      data: {
        shellMetadata: attempt?.policyMetadata,
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
        timeout: Math.max(WRITE_HOOK_TIMEOUT_SECONDS, SHELL_HOOK_TIMEOUT_SECONDS),
        hooks: [preToolUse]
      }
    ],
    PostToolUse: [
      {
        timeout: Math.max(WRITE_HOOK_TIMEOUT_SECONDS, SHELL_HOOK_TIMEOUT_SECONDS),
        hooks: [postToolUse]
      }
    ],
    PostToolUseFailure: [
      {
        timeout: Math.max(WRITE_HOOK_TIMEOUT_SECONDS, SHELL_HOOK_TIMEOUT_SECONDS),
        hooks: [postToolUseFailure]
      }
    ]
  };
}
