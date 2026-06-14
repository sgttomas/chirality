import type { CanUseTool, PermissionResult } from '@anthropic-ai/claude-agent-sdk';
import { randomUUID } from 'node:crypto';
import type { HarnessToolDescriptor } from './tool-descriptor';

export const HARNESS_PERMISSION_POLICY_VERSION = 'harness-permission.v1.overlay-skeleton';

export type HarnessPermissionDecisionValue = 'allow' | 'deny' | 'ask';

export type HarnessPermissionDecisionSource =
  | 'sdk-option'
  | 'sdk-callback'
  | 'chirality-policy'
  | 'hook'
  | 'human'
  | 'prompt-support';

export type NormalizedHarnessPermissionMode =
  | 'readOnly'
  | 'workspaceWrite'
  | 'dontAsk'
  | 'ask'
  | 'bypass';

export type HarnessPermissionDecision = {
  decisionId: string;
  sessionId: string;
  turnId?: string;
  toolName: string;
  decision: HarnessPermissionDecisionValue;
  reason: string;
  source: HarnessPermissionDecisionSource;
  decidedAt: string;
  safeMetadata?: Record<string, unknown>;
};

export type ResolveHarnessPermissionDecisionInput = {
  sessionId?: string;
  turnId?: string;
  toolName: string;
  mode?: string;
  descriptor?: HarnessToolDescriptor;
  source?: HarnessPermissionDecisionSource;
  explicitDeny?: boolean;
  explicitDenyReason?: string;
  safeMetadata?: Record<string, unknown>;
};

export function normalizeHarnessPermissionMode(mode: string | undefined): NormalizedHarnessPermissionMode {
  if (mode === 'readOnly') {
    return 'readOnly';
  }
  if (mode === 'workspaceWrite') {
    return 'workspaceWrite';
  }
  if (mode === 'dontAsk') {
    return 'dontAsk';
  }
  if (mode === 'bypass') {
    return 'bypass';
  }
  return 'ask';
}

function createDecision(
  input: ResolveHarnessPermissionDecisionInput,
  decision: HarnessPermissionDecisionValue,
  reason: string,
  extraMetadata?: Record<string, unknown>
): HarnessPermissionDecision {
  const descriptor = input.descriptor;
  const mode = normalizeHarnessPermissionMode(input.mode);
  return {
    decisionId: `perm_${randomUUID()}`,
    sessionId: input.sessionId ?? 'session:unbound',
    turnId: input.turnId,
    toolName: input.toolName,
    decision,
    reason,
    source: input.source ?? 'chirality-policy',
    decidedAt: new Date().toISOString(),
    safeMetadata: {
      policyVersion: HARNESS_PERMISSION_POLICY_VERSION,
      mode,
      descriptorName: descriptor?.name,
      adapterToolName: descriptor?.adapter.claudeAgentSdk?.toolName,
      permissions: descriptor ? [...descriptor.permissions] : undefined,
      pathScope: descriptor?.pathScope,
      surface: descriptor?.surface,
      humanGate: descriptor?.humanGate,
      ...input.safeMetadata,
      ...extraMetadata
    }
  };
}

function hasDescriptorPermission(
  descriptor: HarnessToolDescriptor,
  permission: HarnessToolDescriptor['permissions'][number]
): boolean {
  return descriptor.permissions.includes(permission);
}

export function resolveHarnessPermissionDecision(
  input: ResolveHarnessPermissionDecisionInput
): HarnessPermissionDecision {
  const descriptor = input.descriptor;
  const mode = normalizeHarnessPermissionMode(input.mode);

  if (input.explicitDeny) {
    return createDecision(
      input,
      'deny',
      input.explicitDenyReason ?? 'Denied by explicit Chirality hard-deny policy.',
      { hardDeny: true }
    );
  }

  if (!descriptor) {
    return createDecision(input, 'deny', `Unknown harness tool '${input.toolName}'.`, {
      hardDeny: true,
      denyClass: 'unknown-tool'
    });
  }

  if (descriptor.surface === 'reserved') {
    return createDecision(input, 'deny', `${descriptor.name} is reserved for future policy.`, {
      hardDeny: true,
      denyClass: 'reserved-tool'
    });
  }

  if (hasDescriptorPermission(descriptor, 'danger')) {
    return createDecision(
      input,
      'deny',
      `${descriptor.name} is denied because it carries a danger-class capability.`,
      {
        hardDeny: true,
        denyClass: 'danger'
      }
    );
  }

  if (hasDescriptorPermission(descriptor, 'shell')) {
    return createDecision(input, 'deny', 'Shell execution is denied until bash controls land.', {
      hardDeny: true,
      denyClass: 'shell'
    });
  }

  if (hasDescriptorPermission(descriptor, 'network')) {
    return createDecision(
      input,
      'deny',
      'Network-capable tools require a future governed implementation tranche.',
      {
        hardDeny: true,
        denyClass: 'network'
      }
    );
  }

  if (hasDescriptorPermission(descriptor, 'subagent')) {
    return createDecision(
      input,
      'deny',
      'Subagent execution requires governed SDK agent definitions and fail-closed hooks.',
      {
        hardDeny: true,
        denyClass: 'subagent'
      }
    );
  }

  if (hasDescriptorPermission(descriptor, 'workspace-write')) {
    if (mode === 'ask' || mode === 'workspaceWrite') {
      return createDecision(
        input,
        'ask',
        `${descriptor.name} requires interactive approval and write hooks before execution.`,
        {
          requiresHumanApproval: true
        }
      );
    }

    return createDecision(
      input,
      'deny',
      `${descriptor.name} is denied in ${mode} mode because it can modify workspace files.`,
      {
        denyClass: 'workspace-write'
      }
    );
  }

  if (hasDescriptorPermission(descriptor, 'read')) {
    return createDecision(input, 'allow', `${descriptor.name} is allowed by ${mode} mode.`, {
      allowClass: 'read'
    });
  }

  return createDecision(input, 'deny', `${descriptor.name} has no supported permission class.`, {
    denyClass: 'unsupported-permission'
  });
}

export function permissionDecisionToSdkResult(
  decision: HarnessPermissionDecision,
  toolUseID?: string
): PermissionResult {
  if (decision.decision === 'allow') {
    return {
      behavior: 'allow',
      toolUseID
    };
  }

  return {
    behavior: 'deny',
    message:
      decision.decision === 'ask'
        ? `Chirality permission requires application approval; denying SDK auto-execution for this tranche. ${decision.reason}`
        : decision.reason,
    toolUseID
  };
}

export function createHarnessCanUseTool(input: {
  sessionId: string;
  mode: string;
  resolveDescriptor: (toolName: string) => HarnessToolDescriptor | undefined;
}): CanUseTool {
  return async (toolName, toolInput, options) => {
    const decision = resolveHarnessPermissionDecision({
      sessionId: input.sessionId,
      mode: input.mode,
      toolName,
      descriptor: input.resolveDescriptor(toolName),
      source: 'sdk-callback',
      safeMetadata: {
        inputKeys: Object.keys(toolInput).sort(),
        blockedPath: options.blockedPath,
        decisionReason: options.decisionReason,
        displayName: options.displayName,
        sdkToolUseId: options.toolUseID
      }
    });

    return permissionDecisionToSdkResult(decision, options.toolUseID);
  };
}
