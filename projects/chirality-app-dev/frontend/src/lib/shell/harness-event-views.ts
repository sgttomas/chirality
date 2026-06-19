import type { HarnessEvent, HarnessEventType } from '../harness/event-schema';

/**
 * Pure derivations over the bridged `harness:event` stream. These power the
 * Tools and Subagents views of the workspace sidebar. They are intentionally
 * DOM-free and side-effect-free so they can be unit-tested in the node test
 * environment, and so the live stream and the persisted replay log derive to
 * the same rows ("replay is free" — see DESIGN §4).
 */

export type ToolActivityStatus = 'queued' | 'permission' | 'running' | 'completed' | 'failed';

export type ToolActivityRow = {
  /** Stable grouping key for the tool invocation. */
  key: string;
  toolName: string;
  status: ToolActivityStatus;
  source?: string;
  surface?: string;
  /** Redacted safe path fields surfaced from the tool input metadata. */
  pathFields: Record<string, string>;
  /** Latest harness event type observed for this invocation. */
  lastEventType: HarnessEventType;
  timestamp: string;
  eventCount: number;
};

export type SubagentActivityStatus = 'running' | 'completed' | 'failed';

export type SubagentActivityRow = {
  key: string;
  agentName: string;
  status: SubagentActivityStatus;
  description?: string;
  summary?: string;
  lastToolName?: string;
  outputArtifactPath?: string;
  lastEventType: HarnessEventType;
  timestamp: string;
  eventCount: number;
};

export type PermissionRequestStatus = 'pending' | 'allowed' | 'denied';

export type PermissionRequestRow = {
  key: string;
  toolName: string;
  reason: string;
  status: PermissionRequestStatus;
  mode?: string;
  pathFields: Record<string, string>;
  timestamp: string;
};

const TOOL_STATUS_BY_TYPE: Partial<Record<HarnessEventType, ToolActivityStatus>> = {
  'tool.queued': 'queued',
  'tool.permission': 'permission',
  'tool.started': 'running',
  'tool.progress': 'running',
  'tool.completed': 'completed',
  'tool.failed': 'failed'
};

const SUBAGENT_STATUS_BY_TYPE: Partial<Record<HarnessEventType, SubagentActivityStatus>> = {
  'subagent.started': 'running',
  'subagent.progress': 'running',
  'subagent.completed': 'completed',
  'subagent.failed': 'failed'
};

function readString(value: unknown): string | undefined {
  return typeof value === 'string' && value.length > 0 ? value : undefined;
}

function readStringRecord(value: unknown): Record<string, string> {
  if (!value || typeof value !== 'object') {
    return {};
  }
  const result: Record<string, string> = {};
  for (const [fieldName, fieldValue] of Object.entries(value as Record<string, unknown>)) {
    const text = readString(fieldValue);
    if (text) {
      result[fieldName] = text;
    }
  }
  return result;
}

function readStringArray(value: unknown): string[] {
  if (!Array.isArray(value)) {
    return [];
  }
  return value.flatMap((item) => {
    const text = readString(item);
    return text ? [text] : [];
  });
}

function markRowCompletion(
  rows: Map<string, ToolActivityRow>,
  key: string,
  status: ToolActivityStatus,
  event: HarnessEvent
): boolean {
  const target = rows.get(key);
  if (!target) {
    return false;
  }
  // Map.set on an existing key updates the value in place (insertion order kept).
  rows.set(key, {
    ...target,
    status,
    lastEventType: event.type,
    timestamp: event.timestamp,
    eventCount: target.eventCount + 1
  });
  return true;
}

/**
 * Collapse the ordered tool.* lifecycle events into one row per tool
 * invocation, keyed by `toolUseId`, in first-seen order. The row reflects the
 * latest observed status; identifying fields (name, source, path metadata) are
 * filled from whichever lifecycle event carried them.
 *
 * The SDK's `tool_use_summary` message emits a `tool.completed` event that has
 * no id of its own — only `precedingToolUseIds`. Such an event completes the
 * tools it follows rather than starting a row of its own, so it is folded onto
 * the referenced rows and never produces an orphan "tool" entry.
 */
export function deriveToolActivity(events: readonly HarnessEvent[]): ToolActivityRow[] {
  const rows = new Map<string, ToolActivityRow>();

  for (const event of events) {
    const status = TOOL_STATUS_BY_TYPE[event.type];
    if (!status) {
      continue;
    }

    const data = event.data ?? {};
    const toolUseId = readString(data.toolUseId) ?? readString(data.adapterToolUseId);

    if (!toolUseId && Array.isArray(data.precedingToolUseIds)) {
      // Summary-style completion: apply the status to each preceding row.
      for (const ref of readStringArray(data.precedingToolUseIds)) {
        markRowCompletion(rows, ref, status, event);
      }
      continue;
    }

    const key = toolUseId ?? event.eventId;
    const existing = rows.get(key);

    const inputMetadata = data.inputMetadata;
    const incomingPathFields =
      inputMetadata && typeof inputMetadata === 'object'
        ? readStringRecord((inputMetadata as Record<string, unknown>).pathFields)
        : {};

    // Map.set keeps the existing key's position, so rows stay in first-seen order.
    rows.set(key, {
      key,
      toolName:
        readString(data.toolName) ??
        readString(data.adapterToolName) ??
        existing?.toolName ??
        'tool',
      status,
      source: readString(data.source) ?? existing?.source,
      surface: readString(data.surface) ?? existing?.surface,
      pathFields: {
        ...(existing?.pathFields ?? {}),
        ...incomingPathFields
      },
      lastEventType: event.type,
      timestamp: event.timestamp,
      eventCount: (existing?.eventCount ?? 0) + 1
    });
  }

  return [...rows.values()];
}

function readNestedPathFields(data: Record<string, unknown>): Record<string, string> {
  // Path metadata lives at data.safeMetadata.inputMetadata.pathFields.
  const safeMetadata = data.safeMetadata;
  if (!safeMetadata || typeof safeMetadata !== 'object') {
    return {};
  }
  const inputMetadata = (safeMetadata as Record<string, unknown>).inputMetadata;
  if (!inputMetadata || typeof inputMetadata !== 'object') {
    return {};
  }
  return readStringRecord((inputMetadata as Record<string, unknown>).pathFields);
}

const PERMISSION_STATUS_BY_BEHAVIOR: Record<string, PermissionRequestStatus> = {
  ask: 'pending',
  allow: 'allowed',
  deny: 'denied'
};

/**
 * Collapse `tool.permission` events into one row per gated tool call, in
 * first-seen order. Only calls that entered the `ask` (pending) state are
 * surfaced — straight policy allows/denies are not operator-actionable. The
 * status reflects the latest behavior, so an `ask` followed by the operator's
 * `allow`/`deny` resolves the same row.
 */
export function derivePermissionRequests(events: readonly HarnessEvent[]): PermissionRequestRow[] {
  const rows = new Map<string, PermissionRequestRow>();

  for (const event of events) {
    if (event.type !== 'tool.permission') {
      continue;
    }

    const data = event.data ?? {};
    const behavior = readString(data.behavior);
    const status = behavior ? PERMISSION_STATUS_BY_BEHAVIOR[behavior] : undefined;
    if (!status) {
      continue;
    }

    const key =
      readString(data.toolUseId) ??
      readString(data.adapterToolUseId) ??
      readString(data.decisionId) ??
      event.eventId;
    const existing = rows.get(key);

    // Surface a row only once it has entered (or is entering) the pending state.
    if (!existing && status !== 'pending') {
      continue;
    }

    const pathFields = readNestedPathFields(data);

    rows.set(key, {
      key,
      toolName: readString(data.toolName) ?? existing?.toolName ?? 'tool',
      reason: readString(data.reason) ?? existing?.reason ?? '',
      status,
      mode: readString(data.mode) ?? existing?.mode,
      pathFields:
        Object.keys(pathFields).length > 0 ? pathFields : (existing?.pathFields ?? {}),
      timestamp: event.timestamp
    });
  }

  return [...rows.values()];
}

/**
 * Collapse the ordered subagent.* lifecycle events into one row per child run,
 * in first-seen order. Keyed by `taskId` — the SDK mapper sets `taskId` on
 * every subagent.* event, whereas `childRunId` is only present when a child-run
 * record was built (e.g. a `task_updated` completion with no output file omits
 * it). Keying on `taskId` keeps the completion collapsing onto the running row
 * instead of forking an orphan.
 */
export function deriveSubagentActivity(events: readonly HarnessEvent[]): SubagentActivityRow[] {
  const rows = new Map<string, SubagentActivityRow>();

  for (const event of events) {
    const status = SUBAGENT_STATUS_BY_TYPE[event.type];
    if (!status) {
      continue;
    }

    const data = event.data ?? {};
    const key =
      readString(data.taskId) ??
      readString(data.childRunId) ??
      readString(data.toolUseId) ??
      event.eventId;
    const existing = rows.get(key);

    // Map.set keeps the existing key's position, so rows stay in first-seen order.
    rows.set(key, {
      key,
      agentName:
        readString(data.agentName) ??
        readString(data.subagentType) ??
        existing?.agentName ??
        'subagent',
      status,
      description: readString(data.description) ?? existing?.description,
      summary: readString(data.summary) ?? existing?.summary,
      lastToolName: readString(data.lastToolName) ?? existing?.lastToolName,
      outputArtifactPath: readString(data.outputArtifactPath) ?? existing?.outputArtifactPath,
      lastEventType: event.type,
      timestamp: event.timestamp,
      eventCount: (existing?.eventCount ?? 0) + 1
    });
  }

  return [...rows.values()];
}
