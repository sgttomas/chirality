import {
  LifecycleState,
  ParsedStatusDocument,
  StatusField,
  StatusHistoryEntry,
  parseLifecycleState,
  parseStatusDocument
} from './status-parser';

const ISO_DATE_PATTERN = /^\d{4}-\d{2}-\d{2}$/;

export interface StatusWriterInput {
  title: string;
  currentState: LifecycleState;
  lastUpdated: string;
  history: StatusHistoryEntry[];
  extraFields?: StatusField[];
}

export interface StatusUpdateInput {
  targetState: LifecycleState;
  actor: string;
  date?: string;
  metadata?: Record<string, string>;
  /**
   * Field labels to remove, matched by their normalized form (for example
   * `Checking Approval SHA`). Removal applies after `metadata` is merged, so
   * `metadata` cannot restore a removed field.
   */
  removeFields?: string[];
  /** Optional history note, written as a `[...]` suffix on the appended history line. */
  notes?: string;
}

export class StatusWriteError extends Error {
  readonly code = 'INVALID_STATUS_FIELD';
  readonly details?: unknown;

  constructor(message: string, details?: unknown) {
    super(message);
    this.name = 'StatusWriteError';
    this.details = details;
  }
}

// Labels the writer emits itself. A field whose normalized label matches one of
// them could shadow the lifecycle state or open a forged history section.
const RESERVED_FIELD_LABELS = new Set(['currentstate', 'lastupdated', 'history']);
// A field is written as one `**Key:** value` line: the key is printable ASCII
// without markdown emphasis, heading or separator characters (so no look-alike
// letters), and the value may not contain anything a reader treats as a line
// break, including C1 controls and the Unicode line and paragraph separators.
const FORBIDDEN_FIELD_KEY = /[^\u0020-\u007e]|[*#:]/;
const FORBIDDEN_FIELD_VALUE = /[\u0000-\u001f\u007f-\u009f\u2028\u2029]/;

function normalizeFieldLabel(label: string): string {
  return label.toLowerCase().replace(/[^a-z0-9]/g, '');
}

function assertWritableField(key: string, value: string): void {
  if (FORBIDDEN_FIELD_KEY.test(key)) {
    throw new StatusWriteError(
      'Status field keys must be printable ASCII without `*`, `#` or `:`',
      { key }
    );
  }
  if (RESERVED_FIELD_LABELS.has(normalizeFieldLabel(key))) {
    throw new StatusWriteError(`Status field '${key}' is reserved for the lifecycle writer`, {
      key
    });
  }
  if (FORBIDDEN_FIELD_VALUE.test(value)) {
    throw new StatusWriteError(
      'Status field values must be one line without newlines or control characters',
      { key }
    );
  }
}

function assertIsoDate(value: string, field: string): void {
  if (!ISO_DATE_PATTERN.test(value)) {
    throw new Error(`${field} must be YYYY-MM-DD`);
  }
}

function toFieldLabel(key: string): string {
  const withSpaces = key
    .trim()
    .replace(/[_-]+/g, ' ')
    .replace(/([a-z0-9])([A-Z])/g, '$1 $2');

  return withSpaces
    .split(/\s+/)
    .filter(Boolean)
    .map((part) => {
      const upper = part.toUpperCase();
      if (upper === 'SHA') {
        return 'SHA';
      }
      return part.charAt(0).toUpperCase() + part.slice(1).toLowerCase();
    })
    .join(' ');
}

function mergeFields(
  existing: StatusField[],
  metadata: Record<string, string> | undefined
): StatusField[] {
  if (!metadata) {
    return existing;
  }

  const merged = [...existing];
  for (const [key, value] of Object.entries(metadata)) {
    // Validate the raw key and value before trimming, so a trailing newline or a
    // reserved label cannot slip through normalization.
    assertWritableField(key, value);
    const trimmedValue = value.trim();
    if (!trimmedValue) {
      continue;
    }

    const label = toFieldLabel(key);
    assertWritableField(label, trimmedValue);
    const existingIndex = merged.findIndex(
      (field) => field.key.trim().toLowerCase() === label.toLowerCase()
    );

    if (existingIndex >= 0) {
      merged[existingIndex] = { key: label, value: trimmedValue };
      continue;
    }

    merged.push({ key: label, value: trimmedValue });
  }

  return merged;
}

function formatHistoryEntry(entry: StatusHistoryEntry): string {
  const actor = entry.actor.trim() || 'UNKNOWN';
  const notesSuffix = entry.notes?.trim() ? ` [${entry.notes.trim()}]` : '';
  return `- ${entry.date} - State set to ${entry.state} (${actor})${notesSuffix}`;
}

export function writeStatusDocument(input: StatusWriterInput): string {
  parseLifecycleState(input.currentState);
  assertIsoDate(input.lastUpdated, 'Last Updated');

  const normalizedHistory = [...input.history];
  for (const entry of normalizedHistory) {
    parseLifecycleState(entry.state);
    assertIsoDate(entry.date, 'History date');
  }

  const lines: string[] = [];
  lines.push(`# ${input.title.trim()}`);
  lines.push('');
  lines.push(`**Current State:** ${input.currentState}`);
  lines.push(`**Last Updated:** ${input.lastUpdated}`);

  for (const field of input.extraFields ?? []) {
    const key = field.key.trim();
    if (!key || !field.value.trim()) {
      continue;
    }
    assertWritableField(key, field.value.trim());
    lines.push(`**${key}:** ${field.value.trim()}`);
  }

  lines.push('');
  lines.push('## History');
  if (normalizedHistory.length === 0) {
    lines.push('-');
  } else {
    lines.push(...normalizedHistory.map(formatHistoryEntry));
  }
  lines.push('');

  return lines.join('\n');
}

export function updateStatusDocument(
  content: string,
  input: StatusUpdateInput
): { content: string; parsed: ParsedStatusDocument } {
  const parsed = parseStatusDocument(content);
  const targetState = parseLifecycleState(input.targetState);
  const actor = input.actor.trim() || 'UNKNOWN';
  const date = input.date?.trim() || new Date().toISOString().slice(0, 10);
  assertIsoDate(date, 'Transition date');

  const notes = input.notes?.trim() || undefined;
  // The note is written inside `[...]` on one history line.
  if (notes && /[\u0000-\u001f\u007f-\u009f\u2028\u2029[\]]/.test(notes)) {
    throw new StatusWriteError(
      'History notes must be one line without brackets or control characters'
    );
  }
  const nextHistory: StatusHistoryEntry[] = [
    ...parsed.history,
    {
      date,
      state: targetState,
      actor,
      ...(notes ? { notes } : {}),
      source: 'list',
      raw: ''
    }
  ];

  const removed = new Set((input.removeFields ?? []).map(normalizeFieldLabel));
  const nextFields = mergeFields(parsed.extraFields, input.metadata).filter(
    (field) => !removed.has(normalizeFieldLabel(field.key))
  );

  const nextContent = writeStatusDocument({
    title: parsed.title,
    currentState: targetState,
    lastUpdated: date,
    history: nextHistory,
    extraFields: nextFields
  });

  return {
    content: nextContent,
    parsed: parseStatusDocument(nextContent)
  };
}
