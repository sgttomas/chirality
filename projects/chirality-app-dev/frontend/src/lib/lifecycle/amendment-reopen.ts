/**
 * Amendment check for reopening an `ISSUED` deliverable (`ISSUED -> IN_PROGRESS`;
 * repo-root `docs/SPEC.md` §3.3, D-GOV-50, D-GOV-51; App SPEC §4.3).
 *
 * This is a port of the Root checker `tools/validation/check_amendment_reopen.py`.
 * It keeps the same admission rules, refusal codes and containment:
 *
 * 1. **Group 3 accepted.** `checkpoint_snapshots/<ID>_GROUP-3_*` under the
 *    scope-change root holds `ACCEPTED_MANIFEST.csv` and a `DECISION.md` whose
 *    first heading reads `# <ID> checkpoint group 3 — accepted ...`.
 * 2. **Register bound by hash.** The amendment's group-2
 *    `ACCEPTED_MANIFEST.csv` binds one `Amendment_Actions*.csv` register inside
 *    the scope-change root, and the register's current SHA-256 equals the bound
 *    value.
 * 3. **Qualifying row.** A `DELIVERABLE` row names the deliverable with
 *    `MODIFY`, or `RECLASSIFY` with `ScopeChanging` `YES`. A legacy register
 *    without the `ScopeChanging` column admits `MODIFY` and refuses `RECLASSIFY`.
 *
 * Paths are resolved inside the project root, and the amendment records inside
 * the scope-change root, after symbolic links are resolved. Python path,
 * `realpath`, CSV, string-strip and `repr` behaviour is reproduced so both
 * checkers decide alike; the parity test
 * `src/__tests__/lib/amendment-reopen-parity.test.ts` compares them on shared
 * fixtures.
 *
 * Differences from the Python checker: the project root must be given (there is
 * no `git rev-parse` fallback), and paths containing a NUL character are a usage
 * error rather than an uncaught exception. The check reads recorded structure
 * and hashes only; it does not establish that a human act was genuine, and it
 * grants nothing (K-AUTH-1).
 */
import { createHash } from 'node:crypto';
import type { Stats } from 'node:fs';
import { lstat, readdir, readFile, readlink, realpath, stat } from 'node:fs/promises';
import nodePath from 'node:path';

export const AMENDMENT_REOPEN_ADMITTED = 'ADMITTED';

/** Refusal codes, identical to the Python checker's. */
export const AMENDMENT_REOPEN_REFUSAL_CODES = [
  'AMENDMENT_UNRESOLVED',
  'SCOPE_CHANGE_ROOT_NOT_FOUND',
  'PATH_ESCAPE',
  'AMENDMENT_OUTSIDE_DELIVERABLE_ROOT',
  'GROUP3_NOT_ACCEPTED',
  'GROUP2_MANIFEST_MISSING',
  'MANIFEST_SCHEMA',
  'REGISTER_NOT_BOUND',
  'REGISTER_AMBIGUOUS',
  'REGISTER_MISSING',
  'REGISTER_HASH_MISMATCH',
  'REGISTER_SCHEMA',
  'NO_DELIVERABLE_ACTION',
  'RECLASSIFY_LEGACY_REGISTER',
  'RECLASSIFY_NOT_SCOPE_CHANGING',
  'ACTION_NOT_AUTHORIZING'
] as const;

export type AmendmentReopenRefusalCode = (typeof AMENDMENT_REOPEN_REFUSAL_CODES)[number];
export type AmendmentReopenCode = typeof AMENDMENT_REOPEN_ADMITTED | AmendmentReopenRefusalCode;

/** The checker's decision; project-root-relative POSIX paths, as the Python checker reports them. */
export interface AmendmentReopenDecision {
  admitted: boolean;
  code: AmendmentReopenCode;
  reason: string;
  deliverableId: string;
  amendmentId: string;
  scopeChangeRoot: string;
  group3Snapshot: string;
  group3Decision: string;
  group2Manifest: string;
  registerPath: string;
  registerSha256: string;
  actionSeq: string;
  actionType: string;
  /** `null` for a legacy register without the `ScopeChanging` column. */
  scopeChanging: string | null;
  notes: string[];
}

export interface AmendmentReopenCheckOptions {
  /** Containment root (the Python checker's `--project-root`). Required. */
  projectRoot: string;
  /** The `_ScopeChange/` folder; found above the deliverable folder when omitted. */
  scopeChangeRoot?: string;
  /** Base for relative inputs (Python `cwd`). Defaults to the project root. */
  cwd?: string;
}

/** Unusable input or an operational failure (the Python checker's exit 2). */
export class AmendmentReopenUsageError extends Error {
  constructor(message: string) {
    super(message);
    this.name = 'AmendmentReopenUsageError';
  }
}

class Refusal extends Error {
  readonly code: AmendmentReopenRefusalCode;
  readonly reason: string;

  constructor(code: AmendmentReopenRefusalCode, reason: string) {
    super(reason);
    this.code = code;
    this.reason = reason;
  }
}

class RecordReadError extends Error {}

// ---------------------------------------------------------------------------
// Python string and regular-expression behaviour
// ---------------------------------------------------------------------------

// Characters Python's str.isspace() accepts (str.strip() and `\s`).
const PY_WS = '\\t\\n\\u000b\\f\\r\\u001c-\\u001f \\u0085\\u00a0\\u1680\\u2000-\\u200a\\u2028\\u2029\\u202f\\u205f\\u3000';
const PY_STRIP = new RegExp(`^[${PY_WS}]+|[${PY_WS}]+$`, 'gu');
// Python's `\w` for str patterns (letters, numbers, underscore); used for `\b`.
const PY_WORD = '[\\p{L}\\p{N}_]';

function pyStrip(value: string): string {
  return value.replace(PY_STRIP, '');
}

function escapeRegExp(value: string): string {
  // Syntax characters only: other identity escapes are errors in `u` mode.
  return value.replace(/[.*+?^${}()|[\]\\/]/g, '\\$&');
}

const NON_PRINTABLE = /[\p{Cc}\p{Cf}\p{Cs}\p{Co}\p{Cn}\p{Zl}\p{Zp}\p{Zs}]/u;

/** Python `repr()` of a str. */
function pyRepr(value: string): string {
  const quote = value.includes("'") && !value.includes('"') ? '"' : "'";
  let out = quote;
  for (const ch of value) {
    const cp = ch.codePointAt(0) ?? 0;
    if (ch === quote || ch === '\\') {
      out += `\\${ch}`;
    } else if (ch === '\t') {
      out += '\\t';
    } else if (ch === '\n') {
      out += '\\n';
    } else if (ch === '\r') {
      out += '\\r';
    } else if (ch === ' ' || (cp > 0x20 && cp < 0x7f) || (cp >= 0x7f && !NON_PRINTABLE.test(ch))) {
      out += ch;
    } else if (cp < 0x100) {
      out += `\\x${cp.toString(16).padStart(2, '0')}`;
    } else if (cp < 0x10000) {
      out += `\\u${cp.toString(16).padStart(4, '0')}`;
    } else {
      out += `\\U${cp.toString(16).padStart(8, '0')}`;
    }
  }
  return out + quote;
}

// Python `\d` matches every Unicode decimal digit; `$` also matches before a
// final newline, which only matters for names read from the filesystem.
const AMENDMENT_ID_RE = /^SCA-(?:[A-Z][A-Z0-9]*-)*\p{Nd}+\n?$/u;
const DELIVERABLE_ID_RE = /^DEL-[0-9A-Za-z]+(?:-[0-9A-Za-z]+)+\n?$/u;
const FOLDER_ID_RE = /^(SCA-(?:[A-Z][A-Z0-9]*-)*\p{Nd}+)_/u;
const GROUP_FOLDER_RE = /^(SCA-(?:[A-Z][A-Z0-9]*-)*\p{Nd}+)_GROUP-([123])_/u;
const REFUSING_WORDS_RE = new RegExp(
  `(?<!${PY_WORD})(?:not accepted|rejected|returned|withdrawn|refused)(?!${PY_WORD})`,
  'iu'
);
const REGISTER_NAME_RE = /^Amendment_Actions[^/]*\.csv\n?$/u;

function acceptedHeadingRe(amendmentId: string): RegExp {
  // Python: ^{ID}\s+checkpoint group 3\b.*\baccepted\b (IGNORECASE). `.` is
  // `[^\n]` because JavaScript's `.` also stops at U+2028 and U+2029.
  return new RegExp(
    `^${escapeRegExp(amendmentId)}[${PY_WS}]+checkpoint group 3(?!${PY_WORD})[^\\n]*(?<!${PY_WORD})accepted(?!${PY_WORD})`,
    'iu'
  );
}

function compareCodePoints(a: string, b: string): number {
  return Buffer.compare(Buffer.from(a, 'utf8'), Buffer.from(b, 'utf8'));
}

// ---------------------------------------------------------------------------
// Python pathlib / posixpath behaviour (POSIX)
// ---------------------------------------------------------------------------

/** `str(PurePosixPath(p))`: drops empty and `.` segments, keeps `..`. */
function pyPath(p: string): string {
  let root = '';
  if (p.startsWith('//') && !p.startsWith('///')) {
    root = '//';
  } else if (p.startsWith('/')) {
    root = '/';
  }
  const parts = p.split('/').filter((part) => part !== '' && part !== '.');
  const joined = root + parts.join('/');
  return joined === '' ? '.' : joined;
}

/** `Path(base) / rel`. */
function pyJoin(base: string, rel: string): string {
  return rel.startsWith('/') ? pyPath(rel) : pyPath(`${base}/${rel}`);
}

function pyIsAbsolute(p: string): boolean {
  return p.startsWith('/');
}

function pyName(p: string): string {
  const normalized = pyPath(p);
  if (normalized === '.' || normalized === '/' || normalized === '//') {
    return '';
  }
  return normalized.slice(normalized.lastIndexOf('/') + 1);
}

function pyParent(p: string): string {
  const normalized = pyPath(p);
  if (normalized === '.' || normalized === '/' || normalized === '//') {
    return normalized;
  }
  const index = normalized.lastIndexOf('/');
  if (index < 0) {
    return '.';
  }
  if (index === 0) {
    return '/';
  }
  if (index === 1 && normalized.startsWith('//')) {
    return '//';
  }
  return normalized.slice(0, index);
}

/** `posixpath.join(a, *parts)`. */
function posixJoin(a: string, ...parts: string[]): string {
  let result = a;
  for (const part of parts) {
    if (part.startsWith('/')) {
      result = part;
    } else if (!result || result.endsWith('/')) {
      result += part;
    } else {
      result += `/${part}`;
    }
  }
  return result;
}

/** `posixpath.split(p)`. */
function posixSplit(p: string): [string, string] {
  const index = p.lastIndexOf('/') + 1;
  let head = p.slice(0, index);
  const tail = p.slice(index);
  if (head && head !== '/'.repeat(head.length)) {
    head = head.replace(/\/+$/, '');
  }
  return [head, tail];
}

/** `posixpath.normpath(p)`. */
function posixNormpath(p: string): string {
  if (p === '') {
    return '.';
  }
  const initial = p.startsWith('/') ? (p.startsWith('//') && !p.startsWith('///') ? 2 : 1) : 0;
  const out: string[] = [];
  for (const comp of p.split('/')) {
    if (comp === '' || comp === '.') {
      continue;
    }
    if (comp !== '..' || (!initial && out.length === 0) || (out.length > 0 && out[out.length - 1] === '..')) {
      out.push(comp);
    } else if (out.length > 0) {
      out.pop();
    }
  }
  const joined = '/'.repeat(initial) + out.join('/');
  return joined || '.';
}

function errorCode(error: unknown): string | undefined {
  const code = (error as { code?: unknown } | null)?.code;
  return typeof code === 'string' ? code : undefined;
}

// Errors pathlib's exists()/is_dir()/is_file()/is_symlink() treat as "no".
const IGNORED_STAT_ERRORS = new Set(['ENOENT', 'ENOTDIR', 'EBADF', 'ELOOP', 'ERR_INVALID_ARG_VALUE']);

async function pyStat(p: string, follow: boolean): Promise<Stats | null> {
  try {
    return follow ? await stat(p) : await lstat(p);
  } catch (error) {
    if (IGNORED_STAT_ERRORS.has(errorCode(error) ?? '')) {
      return null;
    }
    throw error;
  }
}

async function pyExists(p: string): Promise<boolean> {
  return (await pyStat(p, true)) !== null;
}

async function pyIsDir(p: string): Promise<boolean> {
  return (await pyStat(p, true))?.isDirectory() ?? false;
}

async function pyIsFile(p: string): Promise<boolean> {
  return (await pyStat(p, true))?.isFile() ?? false;
}

async function pyIsSymlink(p: string): Promise<boolean> {
  return (await pyStat(p, false))?.isSymbolicLink() ?? false;
}

/** Python 3.11 `posixpath._joinrealpath` (non-strict). */
async function joinRealpath(
  start: string,
  restInput: string,
  seen: Map<string, string | null>
): Promise<[string, boolean]> {
  let current = start;
  let rest = restInput;
  if (rest.startsWith('/')) {
    rest = rest.slice(1);
    current = '/';
  }
  while (rest) {
    const index = rest.indexOf('/');
    const name = index < 0 ? rest : rest.slice(0, index);
    rest = index < 0 ? '' : rest.slice(index + 1);
    if (!name || name === '.') {
      continue;
    }
    if (name === '..') {
      if (current) {
        const [head, tail] = posixSplit(current);
        current = tail === '..' ? posixJoin(head, '..', '..') : head;
      } else {
        current = '..';
      }
      continue;
    }
    const next = posixJoin(current, name);
    let isLink = false;
    try {
      isLink = (await lstat(next)).isSymbolicLink();
    } catch (error) {
      if (errorCode(error) === 'ERR_INVALID_ARG_VALUE') {
        throw error;
      }
      isLink = false;
    }
    if (!isLink) {
      current = next;
      continue;
    }
    if (seen.has(next)) {
      const cached = seen.get(next);
      if (cached !== null && cached !== undefined) {
        current = cached;
        continue;
      }
      return [posixJoin(next, rest), false];
    }
    seen.set(next, null);
    const [resolved, ok] = await joinRealpath(current, await readlink(next), seen);
    current = resolved;
    if (!ok) {
      return [posixJoin(current, rest), false];
    }
    seen.set(next, current);
  }
  return [current, true];
}

/** `os.path.realpath(p)` for an absolute path (resolves as far as the path exists). */
async function pyRealpath(p: string): Promise<string> {
  const [resolved] = await joinRealpath('', p, new Map());
  return posixNormpath(resolved);
}

function isInside(p: string, root: string): boolean {
  if (p === root) {
    return true;
  }
  if (root === '/') {
    return p.startsWith('/');
  }
  return p.startsWith(`${root}/`);
}

function pyRel(p: string, root: string): string {
  if (p === root) {
    return '.';
  }
  return isInside(p, root) ? p.slice(root === '/' ? 1 : root.length + 1) : p;
}

/** The real path of `p`; refused when it leaves `root`. */
async function contained(p: string, root: string, what: string): Promise<string> {
  const real = await pyRealpath(p);
  if (!isInside(real, root)) {
    throw new Refusal('PATH_ESCAPE', `${what} ${p} resolves outside ${root} (path or symlink escape)`);
  }
  return real;
}

// ---------------------------------------------------------------------------
// Record reading (utf-8-sig text, Python csv module, excel dialect)
// ---------------------------------------------------------------------------

async function readText(p: string): Promise<string> {
  const bytes = await readFile(p);
  try {
    // Strips one leading byte-order mark, as Python's utf-8-sig does.
    return new TextDecoder('utf-8', { fatal: true }).decode(bytes);
  } catch {
    throw new RecordReadError(`${p} is not valid UTF-8`);
  }
}

async function firstHeading(p: string): Promise<string> {
  const text = await readText(p);
  for (const line of text.replace(/\r\n?/g, '\n').split('\n')) {
    if (line.startsWith('# ')) {
      return pyStrip(line.slice(2));
    }
  }
  return '';
}

const CSV_FIELD_LIMIT = 131072;

/** Python `csv.reader` records (excel dialect, strict off) of text read with newline=''. */
function csvRecords(text: string): string[][] {
  const lines = text.match(/[^\r\n]*(?:\r\n|\r|\n)|[^\r\n]+$/g) ?? [];
  const records: string[][] = [];
  const EOL = null;
  type State = 'START_RECORD' | 'START_FIELD' | 'IN_FIELD' | 'IN_QUOTED_FIELD' | 'QUOTE_IN_QUOTED_FIELD' | 'EAT_CRNL';
  let fields: string[] | null = null;
  let state: State = 'START_RECORD';
  let field: string[] = [];

  const saveField = (): void => {
    fields?.push(field.join(''));
    field = [];
  };
  const addChar = (ch: string): void => {
    if (field.length >= CSV_FIELD_LIMIT) {
      throw new RecordReadError(`field larger than field limit (${CSV_FIELD_LIMIT})`);
    }
    field.push(ch);
  };
  const isLineBreak = (ch: string | null): boolean => ch === '\n' || ch === '\r' || ch === EOL;
  // Read through a function: \`processChar\` changes the state, which the
  // compiler's narrowing of the loop below does not see.
  const currentState = (): State => state;
  const processChar = (ch: string | null): void => {
    switch (state) {
      case 'START_RECORD':
        if (ch === EOL) {
          return;
        }
        if (ch === '\n' || ch === '\r') {
          state = 'EAT_CRNL';
          return;
        }
        // An ordinary character starts the first field.
        state = 'START_FIELD';
        processChar(ch);
        return;
      case 'START_FIELD':
        if (isLineBreak(ch)) {
          saveField();
          state = ch === EOL ? 'START_RECORD' : 'EAT_CRNL';
        } else if (ch === '"') {
          state = 'IN_QUOTED_FIELD';
        } else if (ch === ',') {
          saveField();
        } else {
          addChar(ch as string);
          state = 'IN_FIELD';
        }
        return;
      case 'IN_FIELD':
        if (isLineBreak(ch)) {
          saveField();
          state = ch === EOL ? 'START_RECORD' : 'EAT_CRNL';
        } else if (ch === ',') {
          saveField();
          state = 'START_FIELD';
        } else {
          addChar(ch as string);
        }
        return;
      case 'IN_QUOTED_FIELD':
        if (ch === EOL) {
          return;
        }
        if (ch === '"') {
          state = 'QUOTE_IN_QUOTED_FIELD';
        } else {
          addChar(ch);
        }
        return;
      case 'QUOTE_IN_QUOTED_FIELD':
        if (ch === '"') {
          addChar(ch);
          state = 'IN_QUOTED_FIELD';
        } else if (ch === ',') {
          saveField();
          state = 'START_FIELD';
        } else if (isLineBreak(ch)) {
          saveField();
          state = ch === EOL ? 'START_RECORD' : 'EAT_CRNL';
        } else {
          addChar(ch as string);
          state = 'IN_FIELD';
        }
        return;
      case 'EAT_CRNL':
        if (ch === '\n' || ch === '\r') {
          return;
        }
        if (ch === EOL) {
          state = 'START_RECORD';
          return;
        }
        throw new RecordReadError("new-line character seen in unquoted field - do you need to open the file with newline=''?");
    }
  };

  for (const line of lines) {
    if (fields === null) {
      fields = [];
      state = 'START_RECORD';
      field = [];
    }
    for (const ch of line) {
      processChar(ch);
    }
    processChar(EOL);
    if (currentState() === 'START_RECORD') {
      records.push(fields);
      fields = null;
    }
  }
  if (fields !== null && (field.length !== 0 || currentState() === 'IN_QUOTED_FIELD')) {
    saveField();
    records.push(fields);
  }
  return records;
}

type CsvRow = Map<string, string>;

/** `_read_csv`: DictReader rows with stripped keys and values, and the stripped header. */
async function readCsv(p: string): Promise<{ header: string[]; rows: CsvRow[] }> {
  const records = csvRecords(await readText(p));
  if (records.length === 0) {
    return { header: [], rows: [] };
  }
  const [fieldnames, ...rest] = records;
  const REST_KEY = Symbol('restkey');
  const rows: CsvRow[] = [];
  for (const record of rest) {
    if (record.length === 0) {
      continue;
    }
    const raw = new Map<string | symbol, string | string[] | null>();
    const count = Math.min(fieldnames.length, record.length);
    for (let index = 0; index < count; index += 1) {
      raw.set(fieldnames[index], record[index]);
    }
    if (fieldnames.length < record.length) {
      raw.set(REST_KEY, record.slice(fieldnames.length));
    } else if (fieldnames.length > record.length) {
      for (const key of fieldnames.slice(record.length)) {
        raw.set(key, null);
      }
    }
    const row: CsvRow = new Map();
    for (const [key, value] of raw) {
      row.set(typeof key === 'string' ? pyStrip(key) : '', typeof value === 'string' ? pyStrip(value) : '');
    }
    rows.push(row);
  }
  return { header: fieldnames.map(pyStrip), rows };
}

function cell(row: CsvRow, key: string): string {
  return row.get(key) ?? '';
}

// ---------------------------------------------------------------------------
// Checker
// ---------------------------------------------------------------------------

async function normalizeDeliverable(deliverable: string, cwd: string): Promise<[string, string | null]> {
  const candidate = pyJoin(cwd, pyPath(deliverable));
  if (await pyIsDir(candidate)) {
    const name = pyName(await pyRealpath(candidate));
    const deliverableId = name.split('_')[0];
    if (!DELIVERABLE_ID_RE.test(deliverableId)) {
      throw new AmendmentReopenUsageError(`deliverable folder name does not start with a deliverable ID: ${name}`);
    }
    return [deliverableId, candidate];
  }
  const deliverableId = pyStrip(deliverable).split('_')[0];
  if (!DELIVERABLE_ID_RE.test(deliverableId)) {
    throw new AmendmentReopenUsageError(
      `--deliverable is neither a folder nor a deliverable ID: ${pyRepr(deliverable)}`
    );
  }
  return [deliverableId, null];
}

async function findScopeChangeRoot(start: string, projectRoot: string): Promise<string | null> {
  let current = await pyRealpath(start);
  while (isInside(current, projectRoot)) {
    const candidate = pyJoin(current, '_ScopeChange');
    if (await pyIsDir(candidate)) {
      return candidate;
    }
    if (current === projectRoot) {
      break;
    }
    current = pyParent(current);
  }
  return null;
}

async function resolveAmendment(
  amendment: string,
  cwd: string,
  projectRoot: string
): Promise<[string, string | null, string | null]> {
  const value = pyStrip(amendment);
  if (AMENDMENT_ID_RE.test(value)) {
    return [value, null, null];
  }
  const candidate = pyPath(value);
  const options = pyIsAbsolute(candidate)
    ? [candidate]
    : [pyJoin(cwd, candidate), pyJoin(projectRoot, candidate)];
  let target: string | null = null;
  for (const option of options) {
    if (await pyExists(option)) {
      target = option;
      break;
    }
  }
  if (target === null) {
    throw new Refusal(
      'AMENDMENT_UNRESOLVED',
      `--amendment is neither an amendment ID nor an existing path: ${pyRepr(amendment)}`
    );
  }
  let real = await contained(target, projectRoot, '--amendment path');
  if (await pyIsFile(real)) {
    if (pyName(real) !== 'DECISION.md') {
      throw new Refusal(
        'AMENDMENT_UNRESOLVED',
        `--amendment file must be a group-3 DECISION.md: ${pyRepr(amendment)}`
      );
    }
    real = pyParent(real);
  }
  const group = GROUP_FOLDER_RE.exec(pyName(real));
  if (group && pyName(pyParent(real)) === 'checkpoint_snapshots') {
    if (group[2] !== '3') {
      throw new Refusal(
        'GROUP3_NOT_ACCEPTED',
        `${pyName(real)} is a group-${group[2]} decision; only an accepted checkpoint-group-3 decision authorizes reopening`
      );
    }
    return [group[1], pyParent(pyParent(real)), real];
  }
  const folder = FOLDER_ID_RE.exec(pyName(real));
  if (folder && pyName(pyParent(real)) === '_ScopeChange') {
    return [folder[1], pyParent(real), null];
  }
  throw new Refusal(
    'AMENDMENT_UNRESOLVED',
    `--amendment path is not an amendment snapshot or group-3 decision folder under _ScopeChange/: ${pyRepr(amendment)}`
  );
}

async function groupFolders(root: string, amendmentId: string, group: string): Promise<string[]> {
  const snapshots = pyJoin(root, 'checkpoint_snapshots');
  if (!(await pyIsDir(snapshots))) {
    return [];
  }
  const names = (await readdir(snapshots)).sort(compareCodePoints);
  const found: string[] = [];
  for (const name of names) {
    const match = GROUP_FOLDER_RE.exec(name);
    const entry = pyJoin(snapshots, name);
    if (match && match[1] === amendmentId && match[2] === group && (await pyIsDir(entry))) {
      found.push(entry);
    }
  }
  return found;
}

async function acceptedGroup3(root: string, amendmentId: string, pinned: string | null): Promise<string> {
  const folders = pinned !== null ? [pinned] : await groupFolders(root, amendmentId, '3');
  const problems: string[] = [];
  const headingRe = acceptedHeadingRe(amendmentId);
  for (const folder of folders) {
    const real = await contained(folder, root, 'group-3 decision folder');
    const decision = pyJoin(real, 'DECISION.md');
    const manifest = pyJoin(real, 'ACCEPTED_MANIFEST.csv');
    if (!(await pyIsFile(decision)) || !(await pyIsFile(manifest))) {
      problems.push(`${pyName(folder)} lacks DECISION.md or ACCEPTED_MANIFEST.csv`);
      continue;
    }
    await contained(decision, root, 'group-3 DECISION.md');
    await contained(manifest, root, 'group-3 ACCEPTED_MANIFEST.csv');
    const heading = await firstHeading(decision);
    if (headingRe.test(heading) && !REFUSING_WORDS_RE.test(heading)) {
      return real;
    }
    problems.push(`${pyName(folder)}/DECISION.md heading does not record group-3 acceptance: ${pyRepr(heading)}`);
  }
  let detail: string;
  if (problems.length > 0) {
    detail = problems.join('; ');
  } else {
    const earlier: string[] = [];
    for (const group of ['1', '2']) {
      earlier.push(...(await groupFolders(root, amendmentId, group)).map(pyName));
    }
    detail =
      `no checkpoint_snapshots/${amendmentId}_GROUP-3_* decision snapshot` +
      (earlier.length > 0
        ? ` (only ${earlier.join(', ')}; a group-1 or group-2 decision does not authorize reopening)`
        : '');
  }
  throw new Refusal('GROUP3_NOT_ACCEPTED', detail);
}

async function manifestBinding(
  manifest: string,
  root: string,
  projectRoot: string
): Promise<[string, string] | null> {
  const { header, rows } = await readCsv(manifest);
  const lookup = new Map<string, string>();
  for (const name of header) {
    lookup.set(name.toLowerCase().replaceAll('-', ''), name);
  }
  const pathCol = lookup.get('path');
  const shaCol = lookup.get('sha256');
  const roleCol = lookup.get('role');
  if (!pathCol || !shaCol) {
    throw new Refusal('MANIFEST_SCHEMA', `${pyRel(manifest, projectRoot)} has no Path and SHA256 columns`);
  }
  let candidates = rows.filter((row) => REGISTER_NAME_RE.test(pyName(cell(row, pathCol))));
  if (candidates.length > 1 && roleCol) {
    const named = candidates.filter((row) => cell(row, roleCol).toLowerCase().includes('action register'));
    if (named.length === 1) {
      candidates = named;
    }
  }
  if (candidates.length === 0) {
    return null;
  }
  const distinct = new Set(candidates.map((row) => `${cell(row, pathCol)}\u0000${cell(row, shaCol).toLowerCase()}`));
  if (distinct.size > 1) {
    throw new Refusal(
      'REGISTER_AMBIGUOUS',
      `${pyRel(manifest, projectRoot)} binds several Amendment_Actions*.csv files and no single row's Role names the action register`
    );
  }
  const rawPath = cell(candidates[0], pathCol);
  const boundSha = cell(candidates[0], shaCol).toLowerCase();
  if (pyIsAbsolute(pyPath(rawPath))) {
    throw new Refusal('PATH_ESCAPE', `register path in ${pyRel(manifest, projectRoot)} is absolute: ${rawPath}`);
  }
  // Manifest paths are project-root relative; execution-root-parent relative
  // paths are accepted too. A missing file resolves to the in-root candidate so
  // the refusal names the missing register rather than an escape.
  const options = [pyJoin(projectRoot, rawPath), pyJoin(pyParent(pyParent(root)), rawPath)];
  const inside: string[] = [];
  for (const option of options) {
    if (isInside(await pyRealpath(option), root)) {
      inside.push(option);
    }
  }
  let target = (inside.length > 0 ? inside : options)[0];
  for (const option of options) {
    if ((await pyExists(option)) || (await pyIsSymlink(option))) {
      target = option;
      break;
    }
  }
  const real = await pyRealpath(target);
  if (!isInside(real, root)) {
    throw new Refusal(
      'PATH_ESCAPE',
      `register ${rawPath} bound in ${pyRel(manifest, projectRoot)} resolves outside the scope-change root (path or symlink escape)`
    );
  }
  return [real, boundSha];
}

async function boundRegister(
  root: string,
  amendmentId: string,
  projectRoot: string
): Promise<[string, string, string]> {
  const manifests: string[] = [];
  for (const folder of await groupFolders(root, amendmentId, '2')) {
    const manifest = pyJoin(folder, 'ACCEPTED_MANIFEST.csv');
    if (await pyIsFile(manifest)) {
      manifests.push(await contained(manifest, root, 'group-2 ACCEPTED_MANIFEST.csv'));
    }
  }
  if (manifests.length === 0) {
    throw new Refusal(
      'GROUP2_MANIFEST_MISSING',
      `no checkpoint_snapshots/${amendmentId}_GROUP-2_*/ACCEPTED_MANIFEST.csv binds the accepted register`
    );
  }
  const bindings: [string, string, string][] = [];
  for (const manifest of manifests) {
    const binding = await manifestBinding(manifest, root, projectRoot);
    if (binding !== null) {
      bindings.push([binding[0], binding[1], manifest]);
    }
  }
  if (bindings.length === 0) {
    throw new Refusal(
      'REGISTER_NOT_BOUND',
      `no group-2 ACCEPTED_MANIFEST.csv of ${amendmentId} binds an Amendment_Actions*.csv register`
    );
  }
  if (new Set(bindings.map(([register, sha]) => `${register}\u0000${sha}`)).size > 1) {
    throw new Refusal('REGISTER_AMBIGUOUS', `group-2 manifests of ${amendmentId} bind different registers or hashes`);
  }
  return bindings[0];
}

function matchesDeliverable(entityId: string, deliverableId: string): boolean {
  return entityId === deliverableId || entityId.startsWith(`${deliverableId}_`);
}

async function qualifyingRow(
  register: string,
  amendmentId: string,
  deliverableId: string,
  projectRoot: string
): Promise<[CsvRow, boolean]> {
  const { header, rows } = await readCsv(register);
  const missing = ['ActionType', 'EntityType', 'EntityID'].filter((column) => !header.includes(column));
  if (missing.length > 0) {
    throw new Refusal('REGISTER_SCHEMA', `${pyRel(register, projectRoot)} lacks column(s) ${missing.join(', ')}`);
  }
  const hasScope = header.includes('ScopeChanging');
  const named = rows.filter(
    (row) =>
      cell(row, 'EntityType').toUpperCase() === 'DELIVERABLE' &&
      matchesDeliverable(cell(row, 'EntityID'), deliverableId) &&
      (!cell(row, 'AmendmentID') || cell(row, 'AmendmentID') === amendmentId)
  );
  if (named.length === 0) {
    throw new Refusal('NO_DELIVERABLE_ACTION', `no ${amendmentId} register row names DELIVERABLE ${deliverableId}`);
  }
  for (const row of named) {
    const action = cell(row, 'ActionType').toUpperCase();
    if (action === 'MODIFY') {
      return [row, hasScope];
    }
    if (action === 'RECLASSIFY' && hasScope && cell(row, 'ScopeChanging').toUpperCase() === 'YES') {
      return [row, hasScope];
    }
  }
  const reclassify = named.filter((row) => cell(row, 'ActionType').toUpperCase() === 'RECLASSIFY');
  const seqs = named
    .map((row) => `${cell(row, 'ActionSeq') || '?'} ${cell(row, 'ActionType') || '?'}`)
    .join(', ');
  if (reclassify.length > 0 && !hasScope) {
    throw new Refusal(
      'RECLASSIFY_LEGACY_REGISTER',
      `${deliverableId} is named only by RECLASSIFY in a register without the ScopeChanging column (legacy); ` +
        'the human records a scope-changing reopening directly, citing the accepted snapshot'
    );
  }
  if (reclassify.length > 0) {
    const values = reclassify.map((row) => pyRepr(cell(row, 'ScopeChanging'))).join(', ');
    throw new Refusal(
      'RECLASSIFY_NOT_SCOPE_CHANGING',
      `${deliverableId} RECLASSIFY row(s) record ScopeChanging ${values}, not YES`
    );
  }
  throw new Refusal(
    'ACTION_NOT_AUTHORIZING',
    `rows naming ${deliverableId} (${seqs}) are not MODIFY or scope-changing RECLASSIFY`
  );
}

async function sha256File(p: string): Promise<string> {
  return createHash('sha256').update(await readFile(p)).digest('hex');
}

function isOperationalError(error: unknown): boolean {
  return error instanceof RecordReadError || (!(error instanceof Refusal) && errorCode(error) !== undefined);
}

/**
 * Decide whether `amendment` authorizes reopening `deliverable` (a deliverable
 * folder or ID). Throws `AmendmentReopenUsageError` for unusable input or an
 * unreadable record; every other outcome is a decision whose `admitted` is true
 * only when all checks pass.
 */
export async function checkAmendmentReopen(
  deliverable: string,
  amendment: string,
  options: AmendmentReopenCheckOptions
): Promise<AmendmentReopenDecision> {
  try {
    return await checkAmendmentReopenUnchecked(deliverable, amendment, options);
  } catch (error) {
    if (error instanceof AmendmentReopenUsageError) {
      throw error;
    }
    if (isOperationalError(error)) {
      throw new AmendmentReopenUsageError(
        `cannot read amendment records: ${error instanceof Error ? error.message : String(error)}`
      );
    }
    throw error;
  }
}

async function checkAmendmentReopenUnchecked(
  deliverable: string,
  amendment: string,
  options: AmendmentReopenCheckOptions
): Promise<AmendmentReopenDecision> {
  if (!options.projectRoot) {
    throw new AmendmentReopenUsageError('cannot resolve the project root; pass projectRoot');
  }
  const base = pyPath(options.cwd ?? options.projectRoot);
  if (!pyIsAbsolute(base)) {
    throw new AmendmentReopenUsageError(`cwd must be absolute: ${options.cwd}`);
  }
  const [deliverableId, deliverablePath] = await normalizeDeliverable(deliverable, base);
  const decision: AmendmentReopenDecision = {
    admitted: false,
    code: 'AMENDMENT_UNRESOLVED',
    reason: '',
    deliverableId,
    amendmentId: '',
    scopeChangeRoot: '',
    group3Snapshot: '',
    group3Decision: '',
    group2Manifest: '',
    registerPath: '',
    registerSha256: '',
    actionSeq: '',
    actionType: '',
    scopeChanging: null,
    notes: []
  };

  let proj = pyJoin(base, pyPath(options.projectRoot));
  if (!(await pyIsDir(proj))) {
    throw new AmendmentReopenUsageError(`project root is not a directory: ${proj}`);
  }
  proj = await pyRealpath(proj);

  try {
    const deliverableReal =
      deliverablePath !== null ? await contained(deliverablePath, proj, 'deliverable folder') : null;
    const [amendmentId, derivedRoot, pinned] = await resolveAmendment(amendment, base, proj);
    decision.amendmentId = amendmentId;

    let root: string | null = null;
    if (options.scopeChangeRoot !== undefined) {
      const given = pyJoin(base, pyPath(options.scopeChangeRoot));
      if (!(await pyIsDir(given))) {
        throw new Refusal(
          'SCOPE_CHANGE_ROOT_NOT_FOUND',
          `--scope-change-root is not a directory: ${options.scopeChangeRoot}`
        );
      }
      root = await contained(given, proj, '--scope-change-root');
    }
    if (derivedRoot !== null) {
      const derivedReal = await contained(derivedRoot, proj, 'scope-change root');
      if (root !== null && root !== derivedReal) {
        throw new Refusal('AMENDMENT_UNRESOLVED', '--amendment path is not under --scope-change-root');
      }
      root = derivedReal;
    }
    if (root === null) {
      if (deliverableReal === null) {
        throw new Refusal(
          'SCOPE_CHANGE_ROOT_NOT_FOUND',
          'an amendment ID with a deliverable ID needs --scope-change-root or a deliverable folder'
        );
      }
      const found = await findScopeChangeRoot(deliverableReal, proj);
      if (found === null) {
        throw new Refusal(
          'SCOPE_CHANGE_ROOT_NOT_FOUND',
          `no _ScopeChange/ folder above ${pyRel(deliverableReal, proj)}`
        );
      }
      root = await contained(found, proj, 'scope-change root');
    }
    decision.scopeChangeRoot = pyRel(root, proj);
    if (deliverableReal !== null && !isInside(deliverableReal, pyParent(root))) {
      throw new Refusal(
        'AMENDMENT_OUTSIDE_DELIVERABLE_ROOT',
        `${decision.scopeChangeRoot} does not belong to the execution root of ${pyRel(deliverableReal, proj)}`
      );
    }

    const group3 = await acceptedGroup3(root, amendmentId, pinned);
    decision.group3Snapshot = pyRel(group3, proj);
    decision.group3Decision = pyRel(pyJoin(group3, 'DECISION.md'), proj);

    const [register, boundSha, manifest] = await boundRegister(root, amendmentId, proj);
    decision.group2Manifest = pyRel(manifest, proj);
    decision.registerPath = pyRel(register, proj);
    if (!(await pyIsFile(register))) {
      throw new Refusal('REGISTER_MISSING', `bound register ${decision.registerPath} does not exist`);
    }
    const actual = await sha256File(register);
    decision.registerSha256 = actual;
    if (actual !== boundSha) {
      throw new Refusal(
        'REGISTER_HASH_MISMATCH',
        `${decision.registerPath} SHA-256 ${actual} differs from ${boundSha} bound in ${decision.group2Manifest}`
      );
    }

    const [row, hasScope] = await qualifyingRow(register, amendmentId, deliverableId, proj);
    if (!hasScope) {
      decision.notes.push('legacy register without ScopeChanging: RECLASSIFY is not admitted by this tool');
    }
    decision.actionSeq = cell(row, 'ActionSeq');
    decision.actionType = cell(row, 'ActionType').toUpperCase();
    decision.scopeChanging = hasScope ? (row.get('ScopeChanging') ?? null) : null;
  } catch (error) {
    if (error instanceof Refusal) {
      decision.code = error.code;
      decision.reason = error.reason;
      return decision;
    }
    throw error;
  }

  decision.admitted = true;
  decision.code = AMENDMENT_REOPEN_ADMITTED;
  decision.reason =
    `${decision.amendmentId} accepted at group 3 (${decision.group3Snapshot}); register ` +
    `${decision.registerPath} matches its group-2 hash; ActionSeq ${decision.actionSeq || '?'} ` +
    `${decision.actionType} names ${deliverableId}`;
  return decision;
}

// ---------------------------------------------------------------------------
// App adapter
// ---------------------------------------------------------------------------

/**
 * The nearest folder at or above `start` holding a `.git` directory or file:
 * the Git work-tree top level in ordinary checkouts and worktrees. Found from
 * the filesystem; the App runs no git process.
 */
async function findWorkTreeTop(start: string): Promise<string | null> {
  let current = start;
  for (;;) {
    const entry = await pyStat(nodePath.join(current, '.git'), true);
    if (entry && (entry.isDirectory() || entry.isFile())) {
      return current;
    }
    const parent = nodePath.dirname(current);
    if (parent === current) {
      return null;
    }
    current = parent;
  }
}

export interface AmendmentForReopenInput {
  /** The App working root (`projectRoot` of the transition request). */
  workingRoot: string;
  /** The deliverable folder whose `_STATUS.md` is being reopened. */
  deliverablePath: string;
  /** Amendment ID (`SCA-NNN`, `SCA-APP-NNN`) or snapshot / group-3 decision path. */
  amendment: string;
}

/**
 * Runs the checker the way `write_status.sh` does, with the Git work-tree top
 * level as the project root (so repository-relative manifest paths resolve),
 * or the working root when it is not inside a work tree. A relative amendment
 * path is read from the working root, then the project root. The App also
 * requires the scope-change root to lie inside the working root and refuses
 * one outside it as `PATH_ESCAPE`.
 */
export async function checkAmendmentForReopen(
  input: AmendmentForReopenInput
): Promise<AmendmentReopenDecision> {
  let workingRoot: string;
  let projectRoot: string;
  try {
    workingRoot = await realpath(input.workingRoot);
    projectRoot = (await findWorkTreeTop(workingRoot)) ?? workingRoot;
  } catch (error) {
    throw new AmendmentReopenUsageError(
      `cannot resolve the working root: ${error instanceof Error ? error.message : String(error)}`
    );
  }
  const decision = await checkAmendmentReopen(input.deliverablePath, input.amendment, {
    projectRoot,
    cwd: workingRoot
  });
  if (decision.scopeChangeRoot) {
    const scopeRoot = nodePath.resolve(projectRoot, decision.scopeChangeRoot);
    if (!isInside(scopeRoot, workingRoot)) {
      return {
        ...decision,
        admitted: false,
        code: 'PATH_ESCAPE',
        reason: `scope-change root ${decision.scopeChangeRoot} lies outside the App working root`
      };
    }
  }
  return decision;
}
