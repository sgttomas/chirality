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

interface DocumentLine {
  text: string;
  /** The line terminator as found (`\n`, `\r\n`) or `''` for a final line without one. */
  eol: string;
}

function splitDocumentLines(content: string): DocumentLine[] {
  const lines: DocumentLine[] = [];
  const pattern = /([^\n]*?)(\r?\n|$)/g;
  let match: RegExpExecArray | null;
  while ((match = pattern.exec(content)) !== null) {
    if (match[0] === '' && pattern.lastIndex >= content.length) {
      break;
    }
    lines.push({ text: match[1], eol: match[2] });
    if (match[2] === '') {
      break;
    }
  }
  return lines;
}

function joinDocumentLines(lines: DocumentLine[]): string {
  return lines.map((line) => line.text + line.eol).join('');
}

const FIELD_LINE = /^\*\*([^*]+):\*\*\s*(.*?)\s*$/;
const HISTORY_HEADING = /^##\s+History\s*$/;
const SECTION_HEADING = /^##\s+/;

function formatTableHistoryRow(
  date: string,
  fromState: string,
  toState: string,
  actor: string,
  notes: string | undefined
): string | undefined {
  const cells = [date, fromState, toState, actor, notes ?? ''];
  if (cells.some((value) => value.includes('|'))) {
    return undefined;
  }
  return `| ${cells.join(' | ')} |`;
}

/**
 * Applies a lifecycle transition to an existing `_STATUS.md` without rebuilding
 * it. The writer owns only these parts:
 *
 * - the values of the first `**Current State:**` and `**Last Updated:**` lines;
 * - the metadata fields it sets, removes or updates among the field lines above
 *   `## History`;
 * - the one history line it appends at the end of the `## History` section (or
 *   in place of a lone `-` placeholder).
 *
 * Every other line — the title, other fields, every existing history line
 * (including lines the parser does not read), sections after `## History` and
 * any other content — is kept verbatim and in order, with its line endings.
 */
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

  const lines = splitDocumentLines(content);
  const docEol = lines.find((line) => line.eol !== '')?.eol ?? '\n';
  const historyIndex = lines.findIndex((line) => HISTORY_HEADING.test(line.text.trim()));
  if (historyIndex < 0) {
    throw new StatusWriteError("Missing '## History' section");
  }

  // Owned lifecycle fields: the first occurrences, which the parser reads.
  const currentIndex = lines.findIndex((line) => /^\*\*Current State:\*\*\s*(.+?)\s*$/.test(line.text));
  const updatedIndex = lines.findIndex((line) => /^\*\*Last Updated:\*\*\s*(.+?)\s*$/.test(line.text));
  if (currentIndex < 0 || updatedIndex < 0) {
    throw new StatusWriteError('Missing lifecycle fields');
  }
  lines[currentIndex] = { ...lines[currentIndex], text: `**Current State:** ${targetState}` };
  lines[updatedIndex] = { ...lines[updatedIndex], text: `**Last Updated:** ${date}` };

  // Metadata fields: updated in place or added after the last field line above
  // `## History`.
  let headerEnd = historyIndex;
  for (const [key, value] of Object.entries(input.metadata ?? {})) {
    // Validate the raw key and value before trimming, so a trailing newline or a
    // reserved label cannot slip through normalization.
    assertWritableField(key, value);
    const trimmedValue = value.trim();
    if (!trimmedValue) {
      continue;
    }
    const label = toFieldLabel(key);
    assertWritableField(label, trimmedValue);
    const text = `**${label}:** ${trimmedValue}`;
    const existing = lines
      .slice(0, headerEnd)
      .findIndex((line) => FIELD_LINE.exec(line.text)?.[1].trim().toLowerCase() === label.toLowerCase());
    if (existing >= 0) {
      lines[existing] = { ...lines[existing], text };
      continue;
    }
    let insertAt = -1;
    for (let index = 0; index < headerEnd; index += 1) {
      if (FIELD_LINE.test(lines[index].text)) {
        insertAt = index + 1;
      }
    }
    if (insertAt < 0) {
      insertAt = headerEnd;
    }
    lines.splice(insertAt, 0, { text, eol: docEol });
    headerEnd += 1;
  }

  // Removed fields (after metadata, so metadata cannot restore them).
  const removed = new Set((input.removeFields ?? []).map(normalizeFieldLabel));
  if (removed.size > 0) {
    for (let index = headerEnd - 1; index >= 0; index -= 1) {
      const field = FIELD_LINE.exec(lines[index].text);
      if (field && removed.has(normalizeFieldLabel(field[1]))) {
        lines.splice(index, 1);
        headerEnd -= 1;
      }
    }
  }

  // Append the history line at the end of the `## History` section, in the
  // section's format; every existing line stays.
  let sectionEnd = lines.length;
  for (let index = headerEnd + 1; index < lines.length; index += 1) {
    if (SECTION_HEADING.test(lines[index].text.trim())) {
      sectionEnd = index;
      break;
    }
  }
  let lastContent = headerEnd;
  for (let index = headerEnd + 1; index < sectionEnd; index += 1) {
    if (lines[index].text.trim() !== '') {
      lastContent = index;
    }
  }
  const tableFormat = parsed.history.length > 0 && parsed.history.every((entry) => entry.source === 'table');
  const listLine = formatHistoryEntry({
    date,
    state: targetState,
    actor,
    ...(notes ? { notes } : {}),
    source: 'list',
    raw: ''
  });
  const historyLine =
    (tableFormat
      ? formatTableHistoryRow(date, parsed.currentState, targetState, actor, notes)
      : undefined) ?? listLine;
  const sectionLines = lines.slice(headerEnd + 1, sectionEnd).filter((line) => line.text.trim() !== '');
  if (sectionLines.length === 1 && sectionLines[0].text.trim() === '-') {
    lines[lastContent] = { ...lines[lastContent], text: historyLine };
  } else {
    if (lines[lastContent].eol === '') {
      lines[lastContent] = { ...lines[lastContent], eol: docEol };
      lines.splice(lastContent + 1, 0, { text: historyLine, eol: '' });
    } else {
      lines.splice(lastContent + 1, 0, { text: historyLine, eol: docEol });
    }
  }

  const nextContent = joinDocumentLines(lines);
  return {
    content: nextContent,
    parsed: parseStatusDocument(nextContent)
  };
}
