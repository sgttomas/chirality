/**
 * Recorded dependency register and supplier-judged blockers (repo-root SPEC
 * §5.2–§5.4, D-GOV-46 and D-GOV-49; App SPEC §5.2).
 *
 * This module is the App's TypeScript reading of the Root reference tools
 * `tools/coordination/dependency_evidence.py` (`parse_declarations`,
 * `union_register`, `recorded_register`, `resolve_accepted_dag`,
 * `check_currency`) and the project mode of
 * `tools/coordination/build_dev001_blocker_queue.py` (`build_project_queue`
 * without `--evidence`). It follows them rule for rule so that both give the
 * same result on the same files; the parity fixtures and their generator live
 * in `src/__tests__/fixtures/recorded-register/`.
 *
 * - A deliverable's recorded register is the union of the entries in the
 *   declared sections of its `_DEPENDENCIES.md` and the rows of its
 *   `Dependencies.csv`. A declared entry and an ACTIVE EXECUTION row with the
 *   same `Direction` and target are one edge. Where they disagree on required
 *   maturity the declaration governs and the disagreement is reported. A
 *   declaration without such a row becomes a synthesized `Origin=DECLARED`
 *   row; where the only matching row is RETIRED, the retired row is reported.
 * - Without an accepted project DAG, blockers come from the recorded
 *   registers: one edge per consumer-to-supplier arc (`DOWNSTREAM` rows
 *   reversed), arcs in a cycle held and non-gating, and each arc judged by its
 *   supplier's `_STATUS.md` state against the arc's required maturity (a
 *   declared maturity governs, then the rows, then the project default).
 * - With an accepted DAG named by `{EXECUTION_ROOT}/_DAG/_LATEST.md`, blockers
 *   come from that version's admitted edges. Deliverables whose local evidence
 *   departs from it are `DAG_PENDING` and get no verdict.
 *
 * Differences from the Python reference are limited to filesystem reach: this
 * module skips symbolic-link unit folders and reads only regular (non-link)
 * files, so a read never leaves the folders it inventories.
 */

import { lstat, readFile, readdir } from 'node:fs/promises';
import path from 'node:path';
import { parseCsv } from './csv-utils';

export const LIFECYCLE_ORDER = [
  'OPEN',
  'INITIALIZED',
  'SEMANTIC_READY',
  'IN_PROGRESS',
  'CHECKING',
  'ISSUED'
] as const;

/** project-setup Phase 1.3 recommended default, used when `_COORDINATION.md` records none. */
export const DEFAULT_MATURITY_FALLBACK = 'INITIALIZED';

export const BLOCKED = 'BLOCKED';
export const UNBLOCKED = 'UNBLOCKED';
export const DAG_PENDING = 'DAG_PENDING';
export const NOT_TRACKED = 'NOT_TRACKED';
export const NOT_ASSESSED = 'NOT_ASSESSED';
export const RECORDED_REGISTER_SOURCE = 'RECORDED_REGISTER';

const LIFECYCLE_DIRS = ['1_Working', '2_Checking', '3_Issued'];
const UNIT_PARTITIONS: Array<[string, string]> = [
  ['PKG-', 'DEL-'],
  ['CAT-', 'KTY-']
];

export type RegisterRow = Record<string, string>;

export type BlockerState =
  | typeof BLOCKED
  | typeof UNBLOCKED
  | typeof DAG_PENDING
  | typeof NOT_TRACKED;

// --- Section reading (materialize_local_dependencies.split_sections) ---------

const MODE = 'mode';
const UPSTREAM = 'upstream';
const DOWNSTREAM = 'downstream';
const DECLARED_LISTS = 'declared_lists';

const AGENT_SUFFIX = '(populated by task+dependency-extract)';

/** SPEC §5.2 headings and the legacy headings read as equivalent (lower case). */
const HEADING_KEYS: Record<string, string> = {
  'dependency tracking mode': MODE,
  'coordination (human-owned)': MODE,
  'coordination mode': MODE,
  'dependency tracking': MODE,
  'declared upstream (i need these before i can proceed)': UPSTREAM,
  'upstream (i need these before i can proceed) — human-owned declarations': UPSTREAM,
  'upstream (this deliverable depends on)': UPSTREAM,
  'upstream (i need these)': UPSTREAM,
  upstream: UPSTREAM,
  'declared upstream': UPSTREAM,
  'declared upstream dependencies': UPSTREAM,
  'declared downstream (these need me)': DOWNSTREAM,
  'downstream (these need me) — human-owned declarations': DOWNSTREAM,
  'downstream (informational; consumers of this deliverable)': DOWNSTREAM,
  downstream: DOWNSTREAM,
  'declared downstream': DOWNSTREAM,
  'declared downstream dependencies': DOWNSTREAM,
  'declared upstream/downstream lists': DECLARED_LISTS,
  'extracted dependency register': 'register',
  'lifecycle summary': 'lifecycle',
  'run notes': 'run_notes',
  'run history': 'run_history',
  'run notes & history': 'run_notes_history',
  'downstream handoff notes': 'handoff',
  'consumer handoff notes (optional)': 'handoff',
  'consumer handoff notes': 'handoff'
};

interface Section {
  heading: string | null;
  lines: string[];
  key: string | null;
}

/** Python `str.splitlines(keepends=True)`. */
function splitLinesKeepEnds(text: string): string[] {
  const lines: string[] = [];
  const boundary = /\r\n|[\n\r\v\f\x1c\x1d\x1e\x85\u2028\u2029]/g;
  let start = 0;
  let match: RegExpExecArray | null;
  while ((match = boundary.exec(text)) !== null) {
    const end = match.index + match[0].length;
    lines.push(text.slice(start, end));
    start = end;
  }
  if (start < text.length) {
    lines.push(text.slice(start));
  }
  return lines;
}

function sectionKey(headingLine: string): string | null {
  let title = headingLine.trim().slice(3).trim().toLowerCase();
  if (title.endsWith(AGENT_SUFFIX)) {
    title = title.slice(0, -AGENT_SUFFIX.length).trim();
  }
  return Object.prototype.hasOwnProperty.call(HEADING_KEYS, title) ? HEADING_KEYS[title] : null;
}

function splitSections(text: string): Section[] {
  const sections: Section[] = [{ heading: null, lines: [], key: null }];
  let inFence = false;
  for (const line of splitLinesKeepEnds(text)) {
    const leading = line.trimStart();
    if (leading.startsWith('```') || leading.startsWith('~~~')) {
      inFence = !inFence;
    }
    if (!inFence && line.startsWith('## ')) {
      sections.push({ heading: line, lines: [], key: sectionKey(line) });
    } else {
      sections[sections.length - 1].lines.push(line);
    }
  }
  return sections;
}

// --- Identifiers and values --------------------------------------------------

const ID_PATTERN = /^((?:DEL|KTY)-\d{2,3}-\d{2,3}|(?:PKG|CAT)-\d{2,3})(?:_[^\n]+)?$/;
const ENTRY_ID = /^`?(?:[A-Za-z0-9_.-]+::)?((?:DEL|KTY)-\d{2,3}-\d{2,3})(?![0-9])([^`]*)`?([^\n]*)$/;
const ANY_ID = /(?:DEL|KTY)-\d{2,3}-\d{2,3}/;
const LEGACY_DIRECTION = /^(upstream|downstream)\s*[:—–-]\s*([^\n]*)$/i;
const MATURITY = /required maturity\s*:?\**\s*`?([A-Za-z_]+)/i;
const PAREN_STATE = new RegExp(`\\((${LIFECYCLE_ORDER.join('|')})\\)`);
const REASON_SEARCH = /reason\s*:\s*([^\n]*)$/i;
const REASON_AT_START = /^reason\s*:\s*([^\n]*)$/i;
const LOCATION = /^location\s*:\s*([^\n]*)$/i;
const MODE_VALUE = /mode[^A-Za-z\n]*?(NOT_TRACKED|DECLARED|FULL_GRAPH|TRACKED|TBD)\b/i;
const STATE_LINE = /Current State\W*([A-Z_]+)/;
const POINTER_LINE =
  /^\s*[-*]?\s*(?:\*\*)?Latest(?: DAG artifact)?(?:\*\*)?\s*:\s*(?:\*\*)?\s*`?([A-Za-z0-9_.-]+)`?\s*$/m;
const INFORMATIONAL_HEADING = /\binformational\b/i;
const SKIP_PREFIXES = [
  'none',
  'tbd',
  'n/a',
  '{',
  '(placeholder)',
  'dependencies coordinated externally'
];

const TYPE_BY_DIRECTION: Record<string, string> = {
  UPSTREAM: 'PREREQUISITE',
  DOWNSTREAM: 'ENABLES'
};

function clean(value: unknown): string {
  return value === undefined || value === null ? '' : String(value).trim();
}

function stripChars(value: string, chars: string, side: 'both' | 'start' = 'both'): string {
  let start = 0;
  let end = value.length;
  while (start < end && chars.includes(value[start])) {
    start += 1;
  }
  if (side === 'both') {
    while (end > start && chars.includes(value[end - 1])) {
      end -= 1;
    }
  }
  return value.slice(start, end);
}

export function normalizeId(raw: string | undefined): string {
  const value = stripChars(clean(raw), '`');
  const match = ID_PATTERN.exec(value);
  return match ? match[1] : value;
}

export function unitId(unitPath: string): string {
  return path.basename(unitPath).split('_')[0];
}

export function maturityValue(raw: string | undefined): string {
  const value = clean(raw).toUpperCase();
  return (LIFECYCLE_ORDER as readonly string[]).includes(value) ? value : 'TBD';
}

function lifecycleIndex(state: string): number {
  return (LIFECYCLE_ORDER as readonly string[]).indexOf(state);
}

/** True when `state` has reached `required` in the SPEC §3.2 order. */
export function maturityReached(state: string, required: string): boolean {
  const stateIndex = lifecycleIndex(state);
  const requiredIndex = lifecycleIndex(required);
  if (stateIndex < 0 || requiredIndex < 0) {
    return false;
  }
  return stateIndex >= requiredIndex;
}

function compareText(left: string, right: string): number {
  if (left < right) {
    return -1;
  }
  return left > right ? 1 : 0;
}

function compareArcs(left: Arc, right: Arc): number {
  return compareText(left[0], right[0]) || compareText(left[1], right[1]);
}

// --- Declared sections (SPEC §5.2 entry form) --------------------------------

export interface DeclaredEntry {
  direction: string;
  targetId: string;
  targetName: string;
  reason: string;
  requiredMaturity: string;
  location: string;
  heading: string;
  raw: string;
}

export interface Declarations {
  mode: string;
  entries: DeclaredEntry[];
  unread: string[];
}

interface EntryBlock {
  head: string;
  subs: string[];
  table: boolean;
}

function entryBlocks(lines: string[]): EntryBlock[] {
  const blocks: EntryBlock[] = [];
  for (const line of lines) {
    const text = line.replace(/\n+$/, '');
    if (/^[-*] /.test(text)) {
      blocks.push({ head: text.slice(2).trim(), subs: [], table: false });
    } else if (blocks.length > 0 && /^\s+[-*] /.test(text)) {
      blocks[blocks.length - 1].subs.push(text.trim().slice(2).trim());
    } else if (text.startsWith('|') && !/^\|[\s|:-]*\|?$/.test(text)) {
      blocks.push({ head: text, subs: [], table: true });
    }
  }
  return blocks;
}

function parseEntry(
  block: EntryBlock,
  sectionDirection: string | null,
  heading: string
): DeclaredEntry | string | null {
  const raw = block.head;
  if (block.table) {
    // Table rows are not in the §5.2 form; a row naming a deliverable is unread.
    return raw;
  }
  let head = block.head;
  const lowered = head.toLowerCase();
  if (!head || SKIP_PREFIXES.some((prefix) => lowered.startsWith(prefix))) {
    return null;
  }
  let direction = sectionDirection;
  if (direction === null) {
    const legacy = LEGACY_DIRECTION.exec(head);
    if (!legacy) {
      return raw;
    }
    direction = legacy[1].toUpperCase();
    head = legacy[2].trim();
  }
  const match = ENTRY_ID.exec(head);
  if (!match) {
    return raw;
  }
  const targetId = match[1];
  const rest = (match[2] + match[3]).trim();
  const reasonMatch = REASON_SEARCH.exec(rest);
  let name = reasonMatch ? rest.slice(0, reasonMatch.index) : rest;
  name = stripChars(stripChars(name.trim(), '_', 'start'), ' —–-').trim();
  let reason = reasonMatch ? reasonMatch[1].trim() : '';
  let required = 'TBD';
  let location = 'TBD';
  const inline = MATURITY.exec(head) ?? PAREN_STATE.exec(head);
  if (inline) {
    required = maturityValue(inline[1]);
  }
  for (const sub of block.subs) {
    const maturity = MATURITY.exec(sub);
    if (maturity) {
      required = maturityValue(maturity[1]);
      continue;
    }
    const locationMatch = LOCATION.exec(sub);
    if (locationMatch) {
      location = locationMatch[1].trim() || 'TBD';
      continue;
    }
    const subReason = REASON_AT_START.exec(sub);
    if (subReason && !reason) {
      reason = subReason[1].trim();
    }
  }
  return {
    direction,
    targetId,
    targetName: name,
    reason,
    requiredMaturity: required,
    location,
    heading,
    raw
  };
}

/**
 * Read the tracking mode and declared entries of a `_DEPENDENCIES.md` text.
 *
 * Only §5.2-form entries are read: a top-level bullet that starts with a
 * deliverable ID, with optional `Required maturity:` and `Location:` sub-lines.
 * Bullets saying none or TBD, template placeholders and the NOT_TRACKED text
 * are not entries. Other bullets and table rows that name a deliverable ID are
 * listed as unread; nothing is inferred from prose.
 */
export function parseDeclarations(text: string): Declarations {
  const result: Declarations = { mode: 'UNKNOWN', entries: [], unread: [] };
  for (const section of splitSections(text)) {
    if (section.key === MODE && result.mode === 'UNKNOWN') {
      const found = MODE_VALUE.exec(section.lines.join(''));
      if (found) {
        const value = found[1].toUpperCase();
        result.mode = value === 'TRACKED' ? 'FULL_GRAPH' : value;
      }
    }
    if (section.key !== UPSTREAM && section.key !== DOWNSTREAM && section.key !== DECLARED_LISTS) {
      continue;
    }
    const direction =
      section.key === UPSTREAM ? 'UPSTREAM' : section.key === DOWNSTREAM ? 'DOWNSTREAM' : null;
    const heading = (section.heading ?? '').trim();
    for (const block of entryBlocks(section.lines)) {
      const parsed = parseEntry(block, direction, heading);
      if (parsed !== null && typeof parsed === 'object') {
        result.entries.push(parsed);
      } else if (typeof parsed === 'string' && ANY_ID.test(parsed)) {
        result.unread.push(parsed);
      }
    }
  }
  return result;
}

// --- Recorded register: the union (SPEC §5.3) --------------------------------

export interface RegisterDisagreement {
  DeliverableID: string;
  Direction: string;
  TargetDeliverableID: string;
  DependencyID: string;
  Field: 'Status' | 'RequiredMaturity';
  Declared: string;
  Csv: string;
}

export interface RecordedRegister {
  deliverableId: string;
  path: string | null;
  mode: string;
  csvPresent: boolean;
  declarationsPresent: boolean;
  entries: DeclaredEntry[];
  /** CSV rows (copies), with a declared required maturity applied where the declaration governs. */
  rows: RegisterRow[];
  /** Synthesized `Origin=DECLARED` rows for declarations without an ACTIVE CSV row. */
  declaredOnly: RegisterRow[];
  disagreements: RegisterDisagreement[];
  unread: string[];
}

export function unionRows(register: RecordedRegister): RegisterRow[] {
  return [...register.rows, ...register.declaredOnly];
}

type Arc = [string, string];

function arcKey(item: Arc): string {
  return `${item[0]}\u0000${item[1]}`;
}

function keyArc(key: string): Arc {
  const [consumer, supplier] = key.split('\u0000');
  return [consumer, supplier];
}

/** Consumer-to-supplier arcs of a register's declared entries, with their stated maturities. */
function declaredArcs(register: RecordedRegister): Map<string, string[]> {
  const arcs = new Map<string, string[]>();
  for (const entry of register.entries) {
    const item: Arc =
      entry.direction === 'UPSTREAM'
        ? [register.deliverableId, entry.targetId]
        : [entry.targetId, register.deliverableId];
    const key = arcKey(item);
    const values = arcs.get(key) ?? [];
    values.push(entry.requiredMaturity);
    arcs.set(key, values);
  }
  return arcs;
}

/** A synthesized `Origin=DECLARED` row, following dependency-extract's mirror rows. */
export function declaredRow(deliverableId: string, entry: DeclaredEntry, ordinal: number): RegisterRow {
  const informational = INFORMATIONAL_HEADING.test(entry.heading);
  const words = entry.raw.split(/\s+/).filter((word) => word.length > 0);
  return {
    RegisterSchemaVersion: 'v3.1',
    DependencyID: `DECLARED-${deliverableId}-${String(ordinal).padStart(3, '0')}`,
    FromDeliverableID: deliverableId,
    DependencyClass: 'EXECUTION',
    AnchorType: 'NOT_APPLICABLE',
    Direction: entry.direction,
    DependencyType: TYPE_BY_DIRECTION[entry.direction],
    TargetType: 'DELIVERABLE',
    TargetDeliverableID: entry.targetId,
    TargetName: entry.targetName,
    TargetLocation: entry.location,
    Statement: entry.reason,
    EvidenceFile: '_DEPENDENCIES.md',
    SourceRef: `_DEPENDENCIES.md ${entry.heading}`.trim(),
    EvidenceQuote: words.slice(0, 30).join(' '),
    Explicitness: informational ? 'IMPLICIT' : 'EXPLICIT',
    RequiredMaturity: entry.requiredMaturity,
    SatisfactionStatus: 'TBD',
    Confidence: informational ? 'MEDIUM' : 'HIGH',
    Origin: 'DECLARED',
    Status: 'ACTIVE',
    Notes: 'declared_only=_DEPENDENCIES.md; type_from=section_heading'
  };
}

/**
 * Apply the union rule to one deliverable (`union_register`).
 *
 * Returns the CSV rows (copies, with a declared required maturity applied
 * where the declaration governs), the synthesized rows for declarations
 * without an ACTIVE CSV row, and the disagreements found.
 */
export function unionRegister(
  deliverableId: string,
  csvRows: RegisterRow[],
  declarations: Declarations
): { rows: RegisterRow[]; declaredOnly: RegisterRow[]; disagreements: RegisterDisagreement[] } {
  const rows = csvRows.map((row) => ({ ...row }));
  const index = new Map<string, RegisterRow[]>();
  const retired = new Map<string, RegisterRow[]>();
  for (const row of rows) {
    if (clean(row.DependencyClass) !== 'EXECUTION') {
      continue;
    }
    const key = arcKey([clean(row.Direction), normalizeId(row.TargetDeliverableID)]);
    const status = clean(row.Status);
    const bucket = status === 'ACTIVE' ? index : status === 'RETIRED' ? retired : null;
    if (bucket) {
      bucket.set(key, [...(bucket.get(key) ?? []), row]);
    }
  }
  const declaredOnly: RegisterRow[] = [];
  const disagreements: RegisterDisagreement[] = [];
  const seen = new Set<string>();
  for (const entry of declarations.entries) {
    const key = arcKey([entry.direction, entry.targetId]);
    if (seen.has(key)) {
      continue;
    }
    seen.add(key);
    const matches = index.get(key) ?? [];
    if (matches.length === 0) {
      declaredOnly.push(declaredRow(deliverableId, entry, declaredOnly.length + 1));
      for (const row of retired.get(key) ?? []) {
        disagreements.push({
          DeliverableID: deliverableId,
          Direction: entry.direction,
          TargetDeliverableID: entry.targetId,
          DependencyID: clean(row.DependencyID),
          Field: 'Status',
          Declared: 'ACTIVE',
          Csv: 'RETIRED'
        });
      }
      continue;
    }
    if (entry.requiredMaturity === 'TBD') {
      continue;
    }
    for (const row of matches) {
      const recorded = clean(row.RequiredMaturity);
      if (recorded !== entry.requiredMaturity) {
        disagreements.push({
          DeliverableID: deliverableId,
          Direction: entry.direction,
          TargetDeliverableID: entry.targetId,
          DependencyID: clean(row.DependencyID),
          Field: 'RequiredMaturity',
          Declared: entry.requiredMaturity,
          Csv: recorded
        });
        row.RequiredMaturity = entry.requiredMaturity;
      }
    }
  }
  return { rows, declaredOnly, disagreements };
}

// --- Filesystem reading ------------------------------------------------------

/** A regular (non-link) file's text, or null when it is absent or not a regular file. */
async function readRegularFile(filePath: string): Promise<string | null> {
  try {
    const info = await lstat(filePath);
    if (!info.isFile()) {
      return null;
    }
    return await readFile(filePath, 'utf8');
  } catch (error) {
    const code = (error as NodeJS.ErrnoException | undefined)?.code;
    if (code === 'ENOENT' || code === 'ENOTDIR') {
      return null;
    }
    throw error;
  }
}

/** Rows of a CSV text keyed by its header, as Python's `csv.DictReader` reads them. */
export function readCsvRecords(text: string): RegisterRow[] {
  const parsed = parseCsv(text.replace(/^﻿/, ''));
  if (parsed.length === 0) {
    return [];
  }
  const [header, ...body] = parsed;
  return body.map((values) => {
    const record: RegisterRow = {};
    header.forEach((column, index) => {
      record[column] = values[index] ?? '';
    });
    return record;
  });
}

async function readCsvFile(filePath: string): Promise<RegisterRow[] | null> {
  const text = await readRegularFile(filePath);
  return text === null ? null : readCsvRecords(text);
}

/** The recorded register of one deliverable folder (`recorded_register`). */
export async function readRecordedRegister(unitPath: string): Promise<RecordedRegister> {
  const register: RecordedRegister = {
    deliverableId: unitId(unitPath),
    path: unitPath,
    mode: 'UNKNOWN',
    csvPresent: false,
    declarationsPresent: false,
    entries: [],
    rows: [],
    declaredOnly: [],
    disagreements: [],
    unread: []
  };
  const csvRows = await readCsvFile(path.join(unitPath, 'Dependencies.csv'));
  if (csvRows !== null) {
    register.csvPresent = true;
  }
  let declarations: Declarations = { mode: 'UNKNOWN', entries: [], unread: [] };
  const markdown = await readRegularFile(path.join(unitPath, '_DEPENDENCIES.md'));
  if (markdown !== null) {
    register.declarationsPresent = true;
    declarations = parseDeclarations(markdown);
  }
  register.mode = declarations.mode;
  register.entries = [...declarations.entries];
  register.unread = declarations.unread;
  const union = unionRegister(register.deliverableId, csvRows ?? [], declarations);
  register.rows = union.rows;
  register.declaredOnly = union.declaredOnly;
  register.disagreements = union.disagreements;
  return register;
}

async function childDirectories(directory: string, prefix: string): Promise<string[]> {
  try {
    const entries = await readdir(directory, { withFileTypes: true });
    return entries
      .filter((entry) => entry.isDirectory() && entry.name.startsWith(prefix))
      .map((entry) => entry.name);
  } catch (error) {
    const code = (error as NodeJS.ErrnoException | undefined)?.code;
    if (code === 'ENOENT' || code === 'ENOTDIR') {
      return [];
    }
    throw error;
  }
}

function compareParts(left: string[], right: string[]): number {
  const length = Math.min(left.length, right.length);
  for (let index = 0; index < length; index += 1) {
    const order = compareText(left[index], right[index]);
    if (order !== 0) {
      return order;
    }
  }
  return left.length - right.length;
}

/**
 * Live production units in every lifecycle folder (`audit_common.inventory`),
 * in path order. Archived copies are never read.
 */
export async function inventoryUnits(executionRoot: string): Promise<string[]> {
  const found: string[][] = [];
  for (const [partition, unitPrefix] of UNIT_PARTITIONS) {
    const packages = await childDirectories(executionRoot, partition);
    for (const folder of LIFECYCLE_DIRS) {
      for (const pkg of packages) {
        for (const unit of await childDirectories(path.join(executionRoot, pkg, folder), unitPrefix)) {
          found.push([pkg, folder, unit]);
        }
      }
    }
  }
  return found.sort(compareParts).map((parts) => path.join(executionRoot, ...parts));
}

/** Recorded registers of every live production unit, keyed by deliverable ID (first unit wins). */
export async function readProjectRegisters(executionRoot: string): Promise<Map<string, RecordedRegister>> {
  const registers = new Map<string, RecordedRegister>();
  for (const unit of await inventoryUnits(executionRoot)) {
    const id = unitId(unit);
    if (!registers.has(id)) {
      registers.set(id, await readRecordedRegister(unit));
    }
  }
  return registers;
}

/** The `Current State` recorded in a deliverable's `_STATUS.md`, or UNKNOWN. */
export async function readLifecycleState(unitPath: string | null): Promise<string> {
  if (unitPath === null) {
    return 'UNKNOWN';
  }
  const text = await readRegularFile(path.join(unitPath, '_STATUS.md'));
  if (text === null) {
    return 'UNKNOWN';
  }
  for (const line of splitLinesKeepEnds(text)) {
    const match = STATE_LINE.exec(line);
    if (match && (LIFECYCLE_ORDER as readonly string[]).includes(match[1])) {
      return match[1];
    }
  }
  return 'UNKNOWN';
}

export interface DefaultMaturity {
  value: string;
  source: 'COORDINATION_RECORD' | 'FALLBACK';
}

/**
 * The project's default maturity threshold from
 * `{EXECUTION_ROOT}/_Coordination/_COORDINATION.md` (`**Default maturity
 * threshold ...:** <STATE>`, project-setup Phase 1.3). When the record is
 * absent, names no lifecycle state, or still lists the template's choices,
 * the recommended default `INITIALIZED` applies and the source says so.
 */
export function parseDefaultMaturity(text: string | null): DefaultMaturity {
  const fallback: DefaultMaturity = { value: DEFAULT_MATURITY_FALLBACK, source: 'FALLBACK' };
  if (text === null) {
    return fallback;
  }
  const line = /default maturity threshold[^:\n]*:([^\n]*)/i.exec(text);
  if (!line) {
    return fallback;
  }
  const states = new Set(
    Array.from(line[1].matchAll(new RegExp(`\\b(${LIFECYCLE_ORDER.join('|')})\\b`, 'g')), (match) => match[1])
  );
  if (states.size !== 1) {
    return fallback;
  }
  return { value: [...states][0], source: 'COORDINATION_RECORD' };
}

export async function readDefaultMaturity(executionRoot: string): Promise<DefaultMaturity> {
  return parseDefaultMaturity(
    await readRegularFile(path.join(executionRoot, '_Coordination', '_COORDINATION.md'))
  );
}

// --- Accepted project DAG (SPEC §5.4) ----------------------------------------

export class DagPointerError extends Error {
  constructor(message: string) {
    super(message);
    this.name = 'DagPointerError';
  }
}

export interface AcceptedDag {
  name: string;
  path: string;
  pointer: string;
  nodes: RegisterRow[];
  admitted: RegisterRow[];
  candidates: RegisterRow[];
  excluded: RegisterRow[];
}

function dagNodeIds(dag: AcceptedDag): Set<string> {
  const ids = new Set<string>();
  for (const row of dag.nodes) {
    if (clean(row.DeliverableID)) {
      ids.add(normalizeId(row.DeliverableID));
    }
  }
  return ids;
}

/** The version a `_LATEST.md` names: `Latest: DAG-NNN` or `Latest DAG artifact: DAG-NNN`. */
export function pointerTarget(text: string): string | null {
  const match = POINTER_LINE.exec(text);
  return match ? match[1] : null;
}

/** The accepted current version named by `{EXECUTION_ROOT}/_DAG/_LATEST.md`, or null when there is none. */
export async function resolveAcceptedDag(executionRoot: string): Promise<AcceptedDag | null> {
  const pointer = path.join(executionRoot, '_DAG', '_LATEST.md');
  const pointerText = await readRegularFile(pointer);
  if (pointerText === null) {
    return null;
  }
  const name = pointerTarget(pointerText);
  if (!name) {
    throw new DagPointerError(`${pointer}: no \`Latest:\` line naming a version`);
  }
  const version = path.join(executionRoot, '_DAG', name);
  const nodes = name.startsWith('_') ? null : await readCsvFile(path.join(version, 'DeliverableNodes.csv'));
  const edges = name.startsWith('_') ? null : await readCsvFile(path.join(version, 'DependencyEdges.csv'));
  if (nodes === null || edges === null) {
    throw new DagPointerError(
      `${pointer}: ${name} is not an accepted version folder with DependencyEdges.csv and DeliverableNodes.csv`
    );
  }
  const admitted = edges.filter((row) => clean(row.Status) === 'ACTIVE');
  const candidates = edges.filter((row) => clean(row.Status) === 'CANDIDATE');
  candidates.push(...((await readCsvFile(path.join(version, 'CandidateEdges.csv'))) ?? []));
  const excluded = (await readCsvFile(path.join(version, 'ExcludedRows.csv'))) ?? [];
  return { name, path: version, pointer, nodes, admitted, candidates, excluded };
}

/**
 * Consumer-to-supplier arc of an EXECUTION row with a deliverable target.
 * `ExcludedRows.csv` carries no `DependencyClass`; its rows are read with
 * `requireClass=false`.
 */
function rowArc(row: RegisterRow, requireClass = true): Arc | null {
  if (requireClass && clean(row.DependencyClass) !== 'EXECUTION') {
    return null;
  }
  if (clean(row.TargetType) !== 'DELIVERABLE') {
    return null;
  }
  const source = normalizeId(row.FromDeliverableID);
  const target = normalizeId(row.TargetDeliverableID);
  const direction = clean(row.Direction);
  if (!source || !target || (direction !== 'UPSTREAM' && direction !== 'DOWNSTREAM')) {
    return null;
  }
  return direction === 'UPSTREAM' ? [source, target] : [target, source];
}

function arcSet(rows: RegisterRow[], requireClass = true): Set<string> {
  const keys = new Set<string>();
  for (const row of rows) {
    const item = rowArc(row, requireClass);
    if (item) {
      keys.add(arcKey(item));
    }
  }
  return keys;
}

export interface Currency {
  result: 'DEPARTURE' | 'NO_DEPARTURE_FOUND';
  dagPendingCount: number;
  dagPending: Record<string, string[]>;
  addedArcs: Arc[];
  removedArcs: Arc[];
  addedDeliverables: string[];
  removedDeliverables: string[];
}

/**
 * Compare local evidence with the accepted version (`check_currency`, SPEC §5.4
 * departure). Endpoints of added and removed arcs, and deliverables present on
 * one side only, are `DAG pending`.
 */
export function checkCurrency(dag: AcceptedDag, registers: Map<string, RecordedRegister>): Currency {
  const admitted = arcSet(dag.admitted);
  const candidate = arcSet(dag.candidates);
  const excluded = arcSet(dag.excluded, false);
  const local = new Set<string>();
  const localCandidate = new Set<string>();
  for (const register of registers.values()) {
    for (const row of unionRows(register)) {
      const status = clean(row.Status);
      if (status !== 'ACTIVE' && status !== 'CANDIDATE') {
        continue;
      }
      const item = rowArc(row);
      if (!item) {
        continue;
      }
      (status === 'ACTIVE' ? local : localCandidate).add(arcKey(item));
    }
  }
  const added = [...local]
    .filter((key) => !admitted.has(key) && !candidate.has(key) && !excluded.has(key))
    .map(keyArc)
    .sort(compareArcs);
  const removedKeys = new Set<string>([...admitted].filter((key) => !local.has(key)));
  for (const key of candidate) {
    if (!local.has(key) && !localCandidate.has(key)) {
      removedKeys.add(key);
    }
  }
  const removed = [...removedKeys].map(keyArc).sort(compareArcs);
  const versionNodes = dagNodeIds(dag);
  const localNodes = new Set(registers.keys());
  const addedNodes = [...localNodes].filter((id) => !versionNodes.has(id)).sort(compareText);
  const removedNodes = [...versionNodes].filter((id) => !localNodes.has(id)).sort(compareText);
  const pending = new Map<string, string[]>();
  const note = (node: string, reason: string): void => {
    pending.set(node, [...(pending.get(node) ?? []), reason]);
  };
  for (const [consumer, supplier] of added) {
    for (const node of [consumer, supplier]) {
      note(node, `arc added: ${consumer} -> ${supplier}`);
    }
  }
  for (const [consumer, supplier] of removed) {
    for (const node of [consumer, supplier]) {
      note(node, `arc removed: ${consumer} -> ${supplier}`);
    }
  }
  for (const node of addedNodes) {
    note(node, `deliverable not in ${dag.name}`);
  }
  for (const node of removedNodes) {
    note(node, `deliverable of ${dag.name} not found locally`);
  }
  const dagPending: Record<string, string[]> = {};
  for (const key of [...pending.keys()].sort(compareText)) {
    dagPending[key] = pending.get(key) ?? [];
  }
  return {
    result: pending.size > 0 ? 'DEPARTURE' : 'NO_DEPARTURE_FOUND',
    dagPendingCount: pending.size,
    dagPending,
    addedArcs: added,
    removedArcs: removed,
    addedDeliverables: addedNodes,
    removedDeliverables: removedNodes
  };
}

// --- Project blockers (build_project_queue without --evidence) ---------------

/** Arcs inside a non-trivial strongly connected component, and self-loops. */
function heldArcs(arcs: Arc[]): Set<string> {
  const graph = new Map<string, string[]>();
  const nodes = new Set<string>();
  for (const [consumer, supplier] of arcs) {
    graph.set(consumer, [...(graph.get(consumer) ?? []), supplier]);
    nodes.add(consumer);
    nodes.add(supplier);
  }
  const index = new Map<string, number>();
  const low = new Map<string, number>();
  const component = new Map<string, number>();
  const stack: string[] = [];
  const onStack = new Set<string>();
  let counter = 0;
  const visit = (node: string): void => {
    index.set(node, counter);
    low.set(node, counter);
    counter += 1;
    stack.push(node);
    onStack.add(node);
    for (const child of graph.get(node) ?? []) {
      if (!index.has(child)) {
        visit(child);
        low.set(node, Math.min(low.get(node) ?? 0, low.get(child) ?? 0));
      } else if (onStack.has(child)) {
        low.set(node, Math.min(low.get(node) ?? 0, index.get(child) ?? 0));
      }
    }
    if (low.get(node) === index.get(node)) {
      for (;;) {
        const member = stack.pop() as string;
        onStack.delete(member);
        component.set(member, index.get(node) ?? 0);
        if (member === node) {
          break;
        }
      }
    }
  };
  for (const node of [...nodes].sort(compareText)) {
    if (!index.has(node)) {
      visit(node);
    }
  }
  return new Set(
    arcs.filter(([consumer, supplier]) => component.get(consumer) === component.get(supplier)).map(arcKey)
  );
}

/** ACTIVE rows grouped by consumer-to-supplier arc, in first-seen order. */
function groupArcRows(rows: Iterable<RegisterRow>): Map<string, RegisterRow[]> {
  const grouped = new Map<string, RegisterRow[]>();
  for (const row of rows) {
    if (clean(row.Status) !== 'ACTIVE') {
      continue;
    }
    const item = rowArc(row);
    if (item) {
      const key = arcKey(item);
      grouped.set(key, [...(grouped.get(key) ?? []), row]);
    }
  }
  return grouped;
}

function highestStated(values: Iterable<string>): string | null {
  let best: string | null = null;
  for (const value of values) {
    const stated = maturityValue(value);
    if (stated === 'TBD') {
      continue;
    }
    if (best === null || lifecycleIndex(stated) > lifecycleIndex(best)) {
      best = stated;
    }
  }
  return best;
}

/** The arc's required maturity: a stated declaration governs, then the rows, then the default. */
export function requiredMaturity(rows: RegisterRow[], fallback: string, declared: string[] = []): string {
  return (
    highestStated(declared) ??
    highestStated(rows.map((row) => row.RequiredMaturity ?? '')) ??
    fallback
  );
}

function declaredMaturities(registers: Map<string, RecordedRegister>): Map<string, string[]> {
  const declared = new Map<string, string[]>();
  for (const register of registers.values()) {
    for (const [key, values] of declaredArcs(register)) {
      declared.set(key, [...(declared.get(key) ?? []), ...values.filter((value) => value !== 'TBD')]);
    }
  }
  return declared;
}

function sameDisagreement(left: RegisterDisagreement, right: RegisterDisagreement): boolean {
  return (
    left.DeliverableID === right.DeliverableID &&
    left.Direction === right.Direction &&
    left.TargetDeliverableID === right.TargetDeliverableID &&
    left.DependencyID === right.DependencyID &&
    left.Field === right.Field &&
    left.Declared === right.Declared &&
    left.Csv === right.Csv
  );
}

/** Rows whose stated maturity differs from the arc's declaration, across deliverables. */
function arcDisagreements(
  gating: Array<[Arc, RegisterRow[]]>,
  declared: Map<string, string[]>
): RegisterDisagreement[] {
  const found: RegisterDisagreement[] = [];
  for (const [item, rows] of gating) {
    const values = declared.get(arcKey(item));
    if (!values || values.length === 0) {
      continue;
    }
    const governing = requiredMaturity([], 'TBD', values);
    for (const row of rows) {
      const recorded = maturityValue(row.RequiredMaturity);
      if (recorded !== 'TBD' && recorded !== governing) {
        found.push({
          DeliverableID: normalizeId(row.FromDeliverableID),
          Direction: clean(row.Direction),
          TargetDeliverableID: normalizeId(row.TargetDeliverableID),
          DependencyID: clean(row.DependencyID),
          Field: 'RequiredMaturity',
          Declared: governing,
          Csv: recorded
        });
      }
    }
  }
  return found;
}

export interface ArcJudgement {
  consumer: string;
  supplier: string;
  requiredMaturity: string;
  supplierState: string;
  satisfied: boolean;
  dependencyIds: string[];
}

/** One deliverable's row, with the column names of the Python project queue. */
export interface ProjectQueueRow {
  DeliverableID: string;
  PackageID: string;
  DeliverableName: string;
  LifecycleState: string;
  ImplementationEvidenceState: string;
  EvidenceCommit: string;
  ActiveUpstreamCount: string;
  SatisfiedUpstreamCount: string;
  BlockingUpstreamCount: string;
  BlockerState: BlockerState;
  BlockingUpstreamDeliverables: string;
  BlockingEdgeIDs: string;
  TrackingMode: string;
  HeldEdgeIDs: string;
  DagPendingReasons: string;
}

export interface ProjectBlockerQueue {
  blockerSource: string;
  acceptedDag: { version: string; path: string; pointer: string } | null;
  currency: Currency | null;
  defaultMaturity: string;
  gatingArcCount: number;
  heldArcCount: number;
  declaredOnlyCount: number;
  declaredDisagreements: RegisterDisagreement[];
  unblockedCount: number;
  blockedCount: number;
  dagPendingCount: number;
  notTrackedCount: number;
  queueRows: ProjectQueueRow[];
  /** Gating arcs with their judgement, in (consumer, supplier) order. */
  arcs: ArcJudgement[];
  /** Held (non-gating) arcs, in (consumer, supplier) order. */
  heldArcs: Arc[];
  registers: Map<string, RecordedRegister>;
}

function unitPackage(unitPath: string | null): string {
  return unitPath === null ? '' : path.basename(path.dirname(path.dirname(unitPath))).split('_')[0];
}

function unitName(unitPath: string | null): string {
  if (unitPath === null) {
    return '';
  }
  const name = path.basename(unitPath);
  const separator = name.indexOf('_');
  return separator < 0 ? '' : name.slice(separator + 1).replace(/_/g, ' ');
}

/**
 * Blockers for a project (`build_project_queue` without `--evidence`): the
 * accepted current DAG version, or else the recorded registers. Each gating arc
 * is judged by its supplier's `_STATUS.md` state against the arc's required
 * maturity, whichever side's row (UPSTREAM or DOWNSTREAM) records it.
 *
 * Throws `DagPointerError` when `_DAG/_LATEST.md` exists but does not resolve.
 */
export async function buildProjectBlockerQueue(
  executionRoot: string,
  options: { defaultMaturity?: string } = {}
): Promise<ProjectBlockerQueue> {
  const defaultMaturity = options.defaultMaturity ?? DEFAULT_MATURITY_FALLBACK;
  const registers = await readProjectRegisters(executionRoot);
  const dag = await resolveAcceptedDag(executionRoot);

  let pending: Record<string, string[]> = {};
  let currency: Currency | null = null;
  const nodes = new Map<string, RegisterRow>();
  let source: string;
  let gating: Map<string, RegisterRow[]>;
  let held: Set<string>;
  if (dag !== null) {
    source = `ACCEPTED_DAG:${dag.name}`;
    gating = groupArcRows(dag.admitted);
    // Candidate arcs are held whatever their Status (a legacy version marks them CANDIDATE).
    held = arcSet(dag.candidates);
    currency = checkCurrency(dag, registers);
    pending = currency.dagPending;
    for (const row of dag.nodes) {
      const key = normalizeId(row.DeliverableID);
      if (key) {
        nodes.set(key, row);
      }
    }
  } else {
    source = RECORDED_REGISTER_SOURCE;
    const grouped = groupArcRows(
      (function* rowsOfRegisters() {
        for (const register of registers.values()) {
          yield* unionRows(register);
        }
      })()
    );
    held = heldArcs([...grouped.keys()].map(keyArc));
    gating = new Map([...grouped].filter(([key]) => !held.has(key)));
  }
  for (const key of registers.keys()) {
    if (!nodes.has(key)) {
      nodes.set(key, {});
    }
  }
  const declared = dag === null ? declaredMaturities(registers) : new Map<string, string[]>();
  const sortedGating: Array<[Arc, RegisterRow[]]> = [...gating]
    .map(([key, rows]): [Arc, RegisterRow[]] => [keyArc(key), rows])
    .sort((left, right) => compareArcs(left[0], right[0]));
  const disagreements: RegisterDisagreement[] = [];
  for (const register of registers.values()) {
    disagreements.push(...register.disagreements);
  }
  const registerDisagreements = [...disagreements];
  for (const item of arcDisagreements(sortedGating, declared)) {
    if (!registerDisagreements.some((existing) => sameDisagreement(existing, item))) {
      disagreements.push(item);
    }
  }

  const states = new Map<string, string>();
  const stateOf = async (id: string): Promise<string> => {
    if (!states.has(id)) {
      states.set(id, await readLifecycleState(registers.get(id)?.path ?? null));
    }
    return states.get(id) as string;
  };

  const blockers = new Map<string, ArcJudgement[]>();
  const upstreamCounts = new Map<string, number>();
  const satisfiedCounts = new Map<string, number>();
  const arcs: ArcJudgement[] = [];
  for (const [[consumer, supplier], rows] of sortedGating) {
    upstreamCounts.set(consumer, (upstreamCounts.get(consumer) ?? 0) + 1);
    const required = requiredMaturity(rows, defaultMaturity, declared.get(arcKey([consumer, supplier])) ?? []);
    const supplierState = await stateOf(supplier);
    const judgement: ArcJudgement = {
      consumer,
      supplier,
      requiredMaturity: required,
      supplierState,
      satisfied: maturityReached(supplierState, required),
      dependencyIds: rows.map((row) => clean(row.DependencyID))
    };
    arcs.push(judgement);
    if (judgement.satisfied) {
      satisfiedCounts.set(consumer, (satisfiedCounts.get(consumer) ?? 0) + 1);
    } else {
      blockers.set(consumer, [...(blockers.get(consumer) ?? []), judgement]);
    }
  }
  const heldList = [...held].map(keyArc).sort(compareArcs);
  const heldByConsumer = new Map<string, string[]>();
  for (const [consumer, supplier] of heldList) {
    heldByConsumer.set(consumer, [...(heldByConsumer.get(consumer) ?? []), supplier]);
  }

  const queueRows: ProjectQueueRow[] = [];
  for (const deliverableId of [...nodes.keys()].sort(compareText)) {
    const node = nodes.get(deliverableId) ?? {};
    const register = registers.get(deliverableId);
    const unit = register?.path ?? null;
    const mode = register?.mode ?? 'UNKNOWN';
    const blocking = blockers.get(deliverableId) ?? [];
    let state: BlockerState;
    if (Object.prototype.hasOwnProperty.call(pending, deliverableId)) {
      state = DAG_PENDING;
    } else if (dag === null && mode === NOT_TRACKED) {
      state = NOT_TRACKED;
    } else {
      state = blocking.length > 0 ? BLOCKED : UNBLOCKED;
    }
    const verdict = state === BLOCKED || state === UNBLOCKED;
    queueRows.push({
      DeliverableID: deliverableId,
      PackageID: clean(node.PackageID) || unitPackage(unit),
      DeliverableName: clean(node.DeliverableName) || unitName(unit),
      LifecycleState: await stateOf(deliverableId),
      ImplementationEvidenceState: '',
      EvidenceCommit: '',
      ActiveUpstreamCount: String(upstreamCounts.get(deliverableId) ?? 0),
      SatisfiedUpstreamCount: String(satisfiedCounts.get(deliverableId) ?? 0),
      BlockingUpstreamCount: verdict ? String(blocking.length) : '',
      BlockerState: state,
      BlockingUpstreamDeliverables: verdict ? blocking.map((item) => item.supplier).join(';') : '',
      BlockingEdgeIDs: verdict ? blocking.flatMap((item) => item.dependencyIds).join(';') : '',
      TrackingMode: mode,
      HeldEdgeIDs: (heldByConsumer.get(deliverableId) ?? [])
        .map((supplier) => `${deliverableId}->${supplier}`)
        .join(';'),
      DagPendingReasons: (pending[deliverableId] ?? []).join('; ')
    });
  }

  const count = (value: BlockerState): number => queueRows.filter((row) => row.BlockerState === value).length;
  return {
    blockerSource: source,
    acceptedDag: dag === null ? null : { version: dag.name, path: dag.path, pointer: dag.pointer },
    currency,
    defaultMaturity,
    gatingArcCount: gating.size,
    heldArcCount: held.size,
    declaredOnlyCount: [...registers.values()].reduce((total, register) => total + register.declaredOnly.length, 0),
    declaredDisagreements: disagreements,
    unblockedCount: count(UNBLOCKED),
    blockedCount: count(BLOCKED),
    dagPendingCount: count(DAG_PENDING),
    notTrackedCount: count(NOT_TRACKED),
    queueRows,
    arcs,
    heldArcs: heldList,
    registers
  };
}

// --- One deliverable's read (App dependency surfaces) ------------------------

export interface DeliverableBlockerJudgement {
  /** BLOCKED/UNBLOCKED give a verdict; DAG_PENDING, NOT_TRACKED and NOT_ASSESSED give none. */
  blockerState: BlockerState | typeof NOT_ASSESSED;
  notAssessedReason?: string;
  blockerSource: string;
  acceptedDagVersion: string | null;
  defaultMaturity: DefaultMaturity;
  activeUpstreamCount: number;
  satisfiedUpstreamCount: number;
  /** Null when there is no verdict. */
  blockingUpstreamCount: number | null;
  blockingUpstreamDeliverables: string[];
  blockingEdgeIds: string[];
  /** This deliverable's gating arcs as consumer, each judged by its supplier. */
  upstreamArcs: ArcJudgement[];
  /** Suppliers of this deliverable's held (non-gating) arcs. */
  heldSuppliers: string[];
  dagPending: boolean;
  dagPendingReasons: string[];
}

export interface DeliverableRecordedRegister {
  deliverableId: string;
  executionRoot: string | null;
  trackingMode: string;
  csvPresent: boolean;
  declarationsPresent: boolean;
  declaredEntries: DeclaredEntry[];
  /** CSV rows with any governing declared maturity applied, then the synthesized declared rows. */
  unionRows: RegisterRow[];
  declaredOnlyRows: RegisterRow[];
  /** Disagreements naming this deliverable (its own register, or an arc it takes part in). */
  disagreements: RegisterDisagreement[];
  unreadDeclarations: string[];
  blockers: DeliverableBlockerJudgement;
}

/**
 * `{EXECUTION_ROOT}` of a deliverable folder: the folder two levels above its
 * lifecycle folder (`1_Working`, `2_Checking` or `3_Issued`), whose parent is a
 * `PKG-` package (for `DEL-` units) or a `CAT-` category (for `KTY-` units).
 * Null when the path has another shape.
 */
export function executionRootForDeliverable(deliverablePath: string): string | null {
  const folder = path.dirname(deliverablePath);
  const partition = path.dirname(folder);
  if (!LIFECYCLE_DIRS.includes(path.basename(folder))) {
    return null;
  }
  const name = path.basename(deliverablePath);
  const pkg = path.basename(partition);
  const matches = UNIT_PARTITIONS.some(
    ([partitionPrefix, unitPrefix]) => pkg.startsWith(partitionPrefix) && name.startsWith(unitPrefix)
  );
  return matches ? path.dirname(partition) : null;
}

function isWithin(root: string, candidate: string): boolean {
  const relative = path.relative(root, candidate);
  return relative === '' || (!relative.startsWith('..') && !path.isAbsolute(relative));
}

function notAssessed(reason: string, defaultMaturity: DefaultMaturity): DeliverableBlockerJudgement {
  return {
    blockerState: NOT_ASSESSED,
    notAssessedReason: reason,
    blockerSource: NOT_ASSESSED,
    acceptedDagVersion: null,
    defaultMaturity,
    activeUpstreamCount: 0,
    satisfiedUpstreamCount: 0,
    blockingUpstreamCount: null,
    blockingUpstreamDeliverables: [],
    blockingEdgeIds: [],
    upstreamArcs: [],
    heldSuppliers: [],
    dagPending: false,
    dagPendingReasons: []
  };
}

function splitList(value: string, separator: string): string[] {
  return value ? value.split(separator) : [];
}

/**
 * The recorded register of one deliverable and its supplier-judged blocker
 * verdict, computed over the execution root that contains it. The execution
 * root must lie inside `containmentRoot` (the App's project root); otherwise
 * only the deliverable's own register is read and no verdict is given.
 */
export async function readDeliverableRecordedRegister(input: {
  deliverablePath: string;
  containmentRoot: string;
}): Promise<DeliverableRecordedRegister> {
  const deliverableId = unitId(input.deliverablePath);
  const candidateRoot = executionRootForDeliverable(input.deliverablePath);
  const executionRoot =
    candidateRoot !== null && isWithin(input.containmentRoot, candidateRoot) ? candidateRoot : null;
  const defaultMaturity =
    executionRoot === null
      ? parseDefaultMaturity(null)
      : await readDefaultMaturity(executionRoot);

  let queue: ProjectBlockerQueue | null = null;
  let blockers: DeliverableBlockerJudgement;
  if (executionRoot === null) {
    blockers = notAssessed(
      candidateRoot === null
        ? 'EXECUTION_ROOT_NOT_RESOLVED: the deliverable is not at {EXECUTION_ROOT}/PKG-*/<lifecycle folder>/DEL-*'
        : 'EXECUTION_ROOT_OUTSIDE_PROJECT_ROOT: the execution root holding this deliverable is outside projectRoot',
      defaultMaturity
    );
  } else {
    try {
      queue = await buildProjectBlockerQueue(executionRoot, { defaultMaturity: defaultMaturity.value });
      blockers = notAssessed('DELIVERABLE_NOT_IN_INVENTORY', defaultMaturity);
    } catch (error) {
      if (!(error instanceof DagPointerError)) {
        throw error;
      }
      blockers = notAssessed(`DAG_POINTER_ERROR: ${error.message}`, defaultMaturity);
    }
  }

  let register = queue?.registers.get(deliverableId);
  if (!register || register.path !== input.deliverablePath) {
    register = await readRecordedRegister(input.deliverablePath);
  }
  const row = queue?.queueRows.find((item) => item.DeliverableID === deliverableId);
  if (queue !== null && row !== undefined && queue.registers.get(deliverableId)?.path === input.deliverablePath) {
    const verdict = row.BlockerState === BLOCKED || row.BlockerState === UNBLOCKED;
    blockers = {
      blockerState: row.BlockerState,
      blockerSource: queue.blockerSource,
      acceptedDagVersion: queue.acceptedDag?.version ?? null,
      defaultMaturity,
      activeUpstreamCount: Number(row.ActiveUpstreamCount),
      satisfiedUpstreamCount: Number(row.SatisfiedUpstreamCount),
      blockingUpstreamCount: verdict ? Number(row.BlockingUpstreamCount) : null,
      blockingUpstreamDeliverables: splitList(row.BlockingUpstreamDeliverables, ';'),
      blockingEdgeIds: splitList(row.BlockingEdgeIDs, ';'),
      upstreamArcs: queue.arcs.filter((item) => item.consumer === deliverableId),
      heldSuppliers: queue.heldArcs.filter(([consumer]) => consumer === deliverableId).map(([, supplier]) => supplier),
      dagPending: row.BlockerState === DAG_PENDING,
      dagPendingReasons: [...(queue.currency?.dagPending[deliverableId] ?? [])]
    };
  }

  const disagreements = queue
    ? queue.declaredDisagreements.filter(
        (item) => item.DeliverableID === deliverableId || item.TargetDeliverableID === deliverableId
      )
    : register.disagreements;
  return {
    deliverableId,
    executionRoot,
    trackingMode: register.mode,
    csvPresent: register.csvPresent,
    declarationsPresent: register.declarationsPresent,
    declaredEntries: register.entries,
    unionRows: unionRows(register),
    declaredOnlyRows: register.declaredOnly,
    disagreements,
    unreadDeclarations: register.unread,
    blockers
  };
}
