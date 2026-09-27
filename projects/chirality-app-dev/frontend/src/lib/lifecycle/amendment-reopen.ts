/**
 * Amendment check for reopening an `ISSUED` deliverable (`ISSUED -> IN_PROGRESS`;
 * repo-root `docs/SPEC.md` §3.3, D-GOV-50, D-GOV-51; App SPEC §4.3).
 *
 * This is a port of the working-tree mode of the Root checker
 * `tools/validation/check_amendment_reopen.py`. It keeps that mode's admission
 * rules, refusal codes and containment:
 *
 * 1. **Group 3 accepted.** A decision folder
 *    `checkpoint_snapshots/<ID>_GROUP-3_[AMENDMENT-<K>_]<YYYY-MM-DD>[_<N>]` under
 *    the scope-change root holds `ACCEPTED_MANIFEST.csv` and a `DECISION.md`
 *    whose first non-blank line is `# <ID> checkpoint group 3 — accepted`,
 *    with `accepted` followed by whitespace, `.`, `,`, `;` or the line end.
 * 2. **Register bound by hash.** The latest group-2 decision folder whose
 *    `ACCEPTED_MANIFEST.csv` binds an `Amendment_Actions*.csv` register governs;
 *    among several such rows the one whose `Role` is `action register` or
 *    `exact final action register` (optionally with a parenthesized note) is
 *    the register. It lies inside the scope-change root and its SHA-256 equals
 *    the bound value.
 * 3. **Qualifying row.** Rows naming the deliverable have `AmendmentID` equal to
 *    the amendment or blank; none is `REMOVE`; one is `MODIFY`, or
 *    `RECLASSIFY` with `ScopeChanging` `YES` (a legacy register without that
 *    column refuses `RECLASSIFY`). Relevant values are not stripped: stray
 *    whitespace is a schema error.
 * 4. **Not already used.** The deliverable's `_STATUS.md` history does not
 *    already record `reopened from ISSUED; amendment: <ID>`.
 *
 * The scope-change root is `<execution root>/_ScopeChange`, the execution root
 * being the deliverable's outermost ancestor folder named `execution`; an
 * adapter manifest (`_harness/adapter.yaml`) above the deliverable must imply
 * the same execution root. `resolveExecutionRoot` carries that rule and is
 * shared with the App's recorded-register read.
 *
 * The Root checker's at-commit mode (`--at-commit`: records read from the
 * approval commit through git; the commit must be reachable and an ancestor of
 * HEAD, refusal codes `APPROVAL_SHA_UNREACHABLE` and
 * `APPROVAL_SHA_NOT_ANCESTOR`) is not ported: the App runs no git process.
 * This check reads the working tree and is unanchored; `write_status.sh` is
 * the anchored check.
 *
 * Python path, `realpath`, `csv`, `str.strip`, `str.splitlines` and `repr`
 * behaviour is reproduced so both checkers decide alike; the parity test
 * `src/__tests__/lib/amendment-reopen-parity.test.ts` compares them. The
 * project root must be given (there is no `git rev-parse` fallback). Records
 * over `MAX_RECORD_BYTES` are refused as operational errors, and only the first
 * `DECISION_PREFIX_BYTES` of a group-3 `DECISION.md` are read (up to its last
 * complete line), so bytes beyond that prefix are not decoded. The check
 * reads recorded structure and hashes only; it grants nothing (K-AUTH-1).
 */
import { createHash } from 'node:crypto';
import type { Stats } from 'node:fs';
import { lstat, open, readdir, readlink, realpath, stat } from 'node:fs/promises';
import nodePath from 'node:path';

export const AMENDMENT_REOPEN_ADMITTED = 'ADMITTED';

/**
 * Refusal codes of the Root checker's working-tree mode, identical to its
 * `REFUSAL_CODES` less the two at-commit codes below.
 */
export const AMENDMENT_REOPEN_REFUSAL_CODES = [
  'AMENDMENT_UNRESOLVED',
  'SCOPE_CHANGE_ROOT_NOT_FOUND',
  'PATH_ESCAPE',
  'AMENDMENT_OUTSIDE_DELIVERABLE_ROOT',
  'AMENDMENT_ALREADY_USED',
  'GROUP3_NOT_ACCEPTED',
  'GROUP2_MANIFEST_MISSING',
  'MANIFEST_SCHEMA',
  'REGISTER_NOT_BOUND',
  'REGISTER_AMBIGUOUS',
  'REGISTER_MISSING',
  'REGISTER_HASH_MISMATCH',
  'REGISTER_SCHEMA',
  'NO_DELIVERABLE_ACTION',
  'DELIVERABLE_REMOVED',
  'RECLASSIFY_LEGACY_REGISTER',
  'RECLASSIFY_NOT_SCOPE_CHANGING',
  'ACTION_NOT_AUTHORIZING'
] as const;

/** Root-only refusal codes of the anchored at-commit mode, which needs git. */
export const ROOT_ONLY_REFUSAL_CODES = ['APPROVAL_SHA_UNREACHABLE', 'APPROVAL_SHA_NOT_ANCESTOR'] as const;

export type AmendmentReopenRefusalCode = (typeof AMENDMENT_REOPEN_REFUSAL_CODES)[number];
export type AmendmentReopenCode = typeof AMENDMENT_REOPEN_ADMITTED | AmendmentReopenRefusalCode;

const UNANCHORED_NOTE =
  'working-tree read: UNANCHORED; the records were read from the working tree, not from a commit, ' +
  'and may differ from any committed record; write_status.sh never uses this mode';

/** The checker's decision; project-root-relative POSIX paths, as the Python checker reports them. */
export interface AmendmentReopenDecision {
  admitted: boolean;
  code: AmendmentReopenCode;
  reason: string;
  deliverableId: string;
  amendmentId: string;
  /** Always `working-tree`: the App reads no commit. */
  mode: 'working-tree';
  anchored: false;
  atCommit: '';
  executionRoot: string;
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
  /** The `_ScopeChange/` folder; `<execution root>/_ScopeChange` of the deliverable folder when omitted. */
  scopeChangeRoot?: string;
  /** Base for relative inputs (Python `cwd`). Defaults to the project root. */
  cwd?: string;
  /** The deliverable's `_STATUS.md` content, checked for a prior reopening (`--status-file`). */
  statusText?: string;
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

/** Largest amendment record read whole (App precedent: 5 MiB). */
export const MAX_RECORD_BYTES = 5 * 1024 * 1024;
/** Bytes of a group-3 `DECISION.md` read for its first non-blank line. */
export const DECISION_PREFIX_BYTES = 64 * 1024;

// ---------------------------------------------------------------------------
// Python string and regular-expression behaviour
// ---------------------------------------------------------------------------

// Characters Python's str.isspace() accepts (str.strip() and `\s`).
const PY_WS = '\\t\\n\\u000b\\f\\r\\u001c-\\u001f \\u0085\\u00a0\\u1680\\u2000-\\u200a\\u2028\\u2029\\u202f\\u205f\\u3000';
const PY_STRIP = new RegExp(`^[${PY_WS}]+|[${PY_WS}]+$`, 'gu');
const PY_RSTRIP = new RegExp(`[${PY_WS}]+$`, 'u');
// Line boundaries of Python's str.splitlines().
const PY_LINE_BREAK = /\r\n|[\n\r\u000b\f\u001c\u001d\u001e\u0085\u2028\u2029]/u;

function pyStrip(value: string): string {
  return value.replace(PY_STRIP, '');
}

function pyRstrip(value: string): string {
  return value.replace(PY_RSTRIP, '');
}

function pySplitlines(text: string): string[] {
  if (text === '') {
    return [];
  }
  const lines = text.split(new RegExp(PY_LINE_BREAK.source, 'gu'));
  // A trailing line break does not open a further (empty) line.
  if (lines.length > 1 && lines[lines.length - 1] === '') {
    lines.pop();
  }
  return lines;
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

const DECIMAL_DIGIT = /^\p{Nd}$/u;

/** Python `int()` of a run of Unicode decimal digits (each Nd block starts at its zero). */
function pyInt(digits: string | undefined): number {
  let value = 0;
  for (const ch of digits ?? '') {
    const cp = ch.codePointAt(0) ?? 0;
    let start = cp;
    while (start > 0 && DECIMAL_DIGIT.test(String.fromCodePoint(start - 1))) {
      start -= 1;
    }
    value = value * 10 + ((cp - start) % 10);
  }
  return value;
}

// Python `\d` matches every Unicode decimal digit; `$` also matches before a
// final newline, which only matters for names read from the filesystem.
const ID = 'SCA-(?:[A-Z][A-Z0-9]*-)*\\p{Nd}+';
const AMENDMENT_ID_RE = new RegExp(`^${ID}\\n?$`, 'u');
const DELIVERABLE_ID_RE = /^DEL-[0-9A-Za-z]+(?:-[0-9A-Za-z]+)+\n?$/u;
const FOLDER_ID_RE = new RegExp(`^(${ID})_`, 'u');
// Anything named like a checkpoint folder, and the decision-snapshot names that count.
const GROUP_PREFIX_RE = new RegExp(`^(${ID})_GROUP-(\\p{Nd}+)_`, 'u');
const GROUP_FOLDER_RE = new RegExp(
  `^(${ID})_GROUP-([123])_(?:AMENDMENT-(\\p{Nd}+)_)?(\\p{Nd}{4}-\\p{Nd}{2}-\\p{Nd}{2})(?:_(\\p{Nd}+))?\\n?$`,
  'u'
);
const REGISTER_NAME_RE = /^Amendment_Actions[^/]*\.csv\n?$/u;
const REGISTER_ROLE_RE = /^(?:exact final )?action register(?: \([^()]*\))?\n?$/iu;
const REGISTER_COLUMNS = ['AmendmentID', 'ActionType', 'EntityType', 'EntityID', 'ScopeChanging'];

function headingRe(amendmentId: string): RegExp {
  // Python: ^#\s+{ID}\s+checkpoint group 3\s+[—–-]+\s+accepted(?:\s|$|[.,;]) (IGNORECASE).
  return new RegExp(
    `^#[${PY_WS}]+${escapeRegExp(amendmentId)}[${PY_WS}]+checkpoint group 3[${PY_WS}]+[—–-]+[${PY_WS}]+accepted(?:[${PY_WS}]|$|[.,;])`,
    'iu'
  );
}

function priorReopeningRe(amendmentId: string): RegExp {
  // Python: reopened from ISSUED; amendment: {ID}(?=[\s(;\]]|$)
  return new RegExp(`reopened from ISSUED; amendment: ${escapeRegExp(amendmentId)}(?=[${PY_WS}(;\\]]|$)`, 'u');
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

/** `Path(p).name`. */
function pyName(p: string): string {
  const normalized = pyPath(p);
  if (normalized === '.' || normalized === '/' || normalized === '//') {
    return '';
  }
  return normalized.slice(normalized.lastIndexOf('/') + 1);
}

/** `Path(p).parent`. */
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

/** `posixpath.basename(p)`. */
function posixBasename(p: string): string {
  return p.slice(p.lastIndexOf('/') + 1);
}

/** `posixpath.dirname(p)`. */
function posixDirname(p: string): string {
  return posixSplit(p)[0];
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

/** The checker's `_join`: non-empty parts joined with `/`. */
function relJoin(...parts: (string | null | undefined)[]): string {
  return parts.filter((part): part is string => Boolean(part)).join('/');
}

function errorCode(error: unknown): string | undefined {
  const code = (error as { code?: unknown } | null)?.code;
  return typeof code === 'string' ? code : undefined;
}

// Errors pathlib's exists()/is_dir()/is_file() treat as "no".
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

async function pyIsDir(p: string): Promise<boolean> {
  return (await pyStat(p, true))?.isDirectory() ?? false;
}

async function pyIsFile(p: string): Promise<boolean> {
  return (await pyStat(p, true))?.isFile() ?? false;
}

/** `os.path.lexists(p)`. */
async function pyLexists(p: string): Promise<boolean> {
  try {
    await lstat(p);
    return true;
  } catch (error) {
    if (errorCode(error) === 'ERR_INVALID_ARG_VALUE') {
      throw error;
    }
    return false;
  }
}

/** `Path.exists()`. */
async function pyExists(p: string): Promise<boolean> {
  return (await pyStat(p, true)) !== null;
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

/** `_inside`: `path == root or root in path.parents` for absolute paths. */
function isInside(p: string, root: string): boolean {
  if (p === root) {
    return true;
  }
  if (root === '/') {
    return p.startsWith('/');
  }
  return p.startsWith(`${root}/`);
}

/** `_inside_rel` for project-relative paths (`""` is the project root). */
function insideRel(p: string, root: string): boolean {
  return root === '' || p === root || p.startsWith(`${root}/`);
}

/** `Path(p).relative_to(root).as_posix()` for `p` inside `root`. */
function relativeTo(p: string, root: string): string {
  if (p === root) {
    return '.';
  }
  return p.slice(root === '/' ? 1 : root.length + 1);
}

// ---------------------------------------------------------------------------
// Record reading (utf-8-sig text, Python csv module, excel dialect)
// ---------------------------------------------------------------------------

/** `bytes.decode("utf-8-sig")`: strict, one leading byte-order mark removed. */
function decodeUtf8Sig(bytes: Uint8Array, what: string): string {
  try {
    return new TextDecoder('utf-8', { fatal: true }).decode(bytes);
  } catch {
    throw new RecordReadError(`${what} is not valid UTF-8`);
  }
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
  // Read through a function: `processChar` changes the state, which the
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
const REST_KEY = Symbol('restkey');

/**
 * `csv.DictReader` rows: `dict(zip(fieldnames, row))`, extra cells under the
 * rest key, missing cells as `None`. Returns the raw field names and rows.
 */
function dictReader(text: string): {
  fieldnames: string[] | null;
  rows: Map<string | symbol, string | string[] | null>[];
} {
  const records = csvRecords(text);
  if (records.length === 0) {
    return { fieldnames: null, rows: [] };
  }
  const [fieldnames, ...rest] = records;
  const rows: Map<string | symbol, string | string[] | null>[] = [];
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
    rows.push(raw);
  }
  return { fieldnames, rows };
}

/** `_read_manifest`: rows with stripped keys and values, and the stripped header. */
function readManifest(text: string): { header: string[]; rows: CsvRow[] } {
  const { fieldnames, rows } = dictReader(text);
  return {
    header: (fieldnames ?? []).map(pyStrip),
    rows: rows.map((raw) => {
      const row: CsvRow = new Map();
      for (const [key, value] of raw) {
        row.set(typeof key === 'string' ? pyStrip(key) : '', typeof value === 'string' ? pyStrip(value) : '');
      }
      return row;
    })
  };
}

/** `_qualifying_row`'s reading: raw keys and values, the rest key dropped. */
function readRegister(text: string): { header: string[]; rows: CsvRow[] } {
  const { fieldnames, rows } = dictReader(text);
  return {
    header: [...(fieldnames ?? [])],
    rows: rows.map((raw) => {
      const row: CsvRow = new Map();
      for (const [key, value] of raw) {
        if (typeof key === 'string') {
          row.set(key, typeof value === 'string' ? value : '');
        }
      }
      return row;
    })
  };
}

function cell(row: CsvRow, key: string): string {
  return row.get(key) ?? '';
}

// ---------------------------------------------------------------------------
// Working-tree store (the Python checker's `_WorkTree`)
// ---------------------------------------------------------------------------

interface Entry {
  /** Resolved, project-root-relative POSIX path (`""` is the project root). */
  path: string;
  kind: 'tree' | 'blob' | 'other';
}

function escapeRefusal(what: string, rel: string, within: string): Refusal {
  return new Refusal(
    'PATH_ESCAPE',
    `${what} ${rel || '.'} resolves outside ${within || 'the project root'} (path or symlink escape)`
  );
}

class WorkTree {
  constructor(private readonly proj: string) {}

  async resolve(rel: string, within: string, what: string): Promise<Entry | null> {
    const target = rel ? pyJoin(this.proj, rel) : this.proj;
    const real = await pyRealpath(target);
    const bound = within ? pyJoin(this.proj, within) : this.proj;
    if (!isInside(real, bound)) {
      throw escapeRefusal(what, rel, within);
    }
    let kind: Entry['kind'];
    if (await pyIsDir(real)) {
      kind = 'tree';
    } else if (await pyIsFile(real)) {
      kind = 'blob';
    } else if (!(await pyLexists(target)) && !(await pyExists(real))) {
      return null;
    } else {
      kind = 'other';
    }
    const resolved = relativeTo(real, this.proj);
    return { path: resolved === '.' ? '' : resolved, kind };
  }

  async children(rel: string): Promise<string[]> {
    return (await readdir(rel ? pyJoin(this.proj, rel) : this.proj)).sort(compareCodePoints);
  }

  /** The whole record; one over `MAX_RECORD_BYTES` is an operational error. */
  async read(entry: Entry): Promise<Buffer> {
    const handle = await open(entry.path ? pyJoin(this.proj, entry.path) : this.proj, 'r');
    try {
      const { size } = await handle.stat();
      if (size > MAX_RECORD_BYTES) {
        throw new RecordReadError(
          `${entry.path} is ${size} bytes; amendment records are read up to ${MAX_RECORD_BYTES} bytes`
        );
      }
      return await handle.readFile();
    } finally {
      await handle.close();
    }
  }

  /**
   * At most `limit` bytes from the start of the record, cut after the last
   * complete line when the record is longer: enough for a first line.
   */
  async readPrefix(entry: Entry, limit: number): Promise<Buffer> {
    const handle = await open(entry.path ? pyJoin(this.proj, entry.path) : this.proj, 'r');
    try {
      const buffer = Buffer.alloc(limit + 1);
      let filled = 0;
      while (filled < buffer.length) {
        const { bytesRead } = await handle.read(buffer, filled, buffer.length - filled, filled);
        if (bytesRead === 0) {
          break;
        }
        filled += bytesRead;
      }
      if (filled <= limit) {
        return buffer.subarray(0, filled);
      }
      return buffer.subarray(0, buffer.subarray(0, limit).lastIndexOf(0x0a) + 1);
    } finally {
      await handle.close();
    }
  }
}

// ---------------------------------------------------------------------------
// Checker
// ---------------------------------------------------------------------------

/** `_to_rel`: project-relative POSIX form of a path argument, or null outside. */
async function toRel(value: string, base: string, proj: string): Promise<string | null> {
  const raw = pyPath(value);
  const absolute = posixNormpath(pyIsAbsolute(raw) ? raw : pyJoin(base, raw));
  for (const candidate of [absolute, await pyRealpath(absolute)]) {
    if (isInside(candidate, proj)) {
      const rel = relativeTo(candidate, proj);
      return rel === '.' ? '' : rel;
    }
  }
  return null;
}

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

/** Where a deliverable's execution root is, or why it could not be resolved. */
export type ExecutionRootResolution =
  | {
      resolved: true;
      /** Project-relative POSIX path of the execution root. */
      executionRoot: string;
    }
  | {
      resolved: false;
      /** No `execution` ancestor, or an adapter manifest that implies another root. */
      problem: 'NOT_IN_EXECUTION_FOLDER' | 'ADAPTER_MANIFEST_DISAGREES';
      reason: string;
    };

/**
 * The Root checker's `_execution_root`, shared with the App's recorded-register
 * read (`dependencies/recorded-register.ts`): the deliverable's outermost
 * ancestor folder named `execution` below the project root. An adapter
 * manifest (`_harness/adapter.yaml`) found by walking up from the deliverable
 * to the project root must imply the same root (the manifest's folder when it
 * is named `execution`, else its `execution/` child).
 *
 * Both paths must be canonical (`realpath`) absolute POSIX paths, with
 * `deliverableReal` inside `proj`.
 */
export async function resolveExecutionRoot(
  deliverableReal: string,
  proj: string
): Promise<ExecutionRootResolution> {
  const relative = relativeTo(deliverableReal, proj);
  const parts = relative === '.' ? [] : relative.split('/');
  const index = parts.slice(0, -1).indexOf('execution');
  if (index < 0) {
    return {
      resolved: false,
      problem: 'NOT_IN_EXECUTION_FOLDER',
      reason: `${relative} is not inside an execution/ folder`
    };
  }
  const execRel = parts.slice(0, index + 1).join('/');
  let current = deliverableReal;
  for (;;) {
    const adapter = pyJoin(current, '_harness/adapter.yaml');
    if (await pyIsFile(adapter)) {
      const implied = pyName(current) === 'execution' ? current : pyJoin(current, 'execution');
      if (implied !== pyJoin(proj, execRel)) {
        return {
          resolved: false,
          problem: 'ADAPTER_MANIFEST_DISAGREES',
          reason:
            `adapter manifest ${relativeTo(adapter, proj)} implies execution root ` +
            `${isInside(implied, proj) ? relativeTo(implied, proj) : implied}, ` +
            `but the deliverable's execution root is ${execRel}`
        };
      }
      break;
    }
    // The second test only guards a caller that broke the precondition.
    if (current === proj || current === pyParent(current)) {
      break;
    }
    current = pyParent(current);
  }
  return { resolved: true, executionRoot: execRel };
}

/** `_execution_root` as the checker applies it: an unresolved root refuses the reopening. */
async function executionRoot(deliverableReal: string, proj: string): Promise<string> {
  const resolution = await resolveExecutionRoot(deliverableReal, proj);
  if (!resolution.resolved) {
    throw new Refusal(
      'SCOPE_CHANGE_ROOT_NOT_FOUND',
      resolution.problem === 'NOT_IN_EXECUTION_FOLDER'
        ? `${resolution.reason}; pass --scope-change-root`
        : resolution.reason
    );
  }
  return resolution.executionRoot;
}

async function resolveAmendment(
  store: WorkTree,
  amendment: string,
  base: string,
  proj: string
): Promise<[string, string | null, string | null]> {
  const value = pyStrip(amendment);
  if (AMENDMENT_ID_RE.test(value)) {
    return [value, null, null];
  }
  const raw = pyPath(value);
  const options = pyIsAbsolute(raw) ? [raw] : [pyJoin(base, raw), pyJoin(proj, raw)];
  const rels: string[] = [];
  for (const option of options) {
    const rel = await toRel(option, base, proj);
    if (rel !== null && !rels.includes(rel)) {
      rels.push(rel);
    }
  }
  if (rels.length === 0) {
    throw new Refusal('PATH_ESCAPE', `--amendment path ${pyRepr(amendment)} lies outside the project root`);
  }
  let entry: Entry | null = null;
  for (const rel of rels) {
    entry = await store.resolve(rel, '', '--amendment path');
    if (entry !== null) {
      break;
    }
  }
  if (entry === null) {
    throw new Refusal(
      'AMENDMENT_UNRESOLVED',
      `--amendment is neither an amendment ID nor an existing path: ${pyRepr(amendment)}`
    );
  }
  let entryPath = entry.path;
  if (entry.kind === 'blob') {
    if (posixBasename(entryPath) !== 'DECISION.md') {
      throw new Refusal('AMENDMENT_UNRESOLVED', `--amendment file must be a group-3 DECISION.md: ${pyRepr(amendment)}`);
    }
    entryPath = posixDirname(entryPath);
  }
  const name = posixBasename(entryPath);
  const parent = posixDirname(entryPath);
  if (posixBasename(parent) === 'checkpoint_snapshots') {
    const loose = GROUP_PREFIX_RE.exec(name);
    if (loose) {
      if (loose[2] !== '3') {
        throw new Refusal(
          'GROUP3_NOT_ACCEPTED',
          `${name} is a group-${loose[2]} decision; only an accepted checkpoint-group-3 decision authorizes reopening`
        );
      }
      if (!GROUP_FOLDER_RE.test(name)) {
        throw new Refusal(
          'GROUP3_NOT_ACCEPTED',
          `${name} is not a group-3 decision snapshot name (${loose[1]}_GROUP-3_[AMENDMENT-K_]YYYY-MM-DD[_N]); candidate folders do not count`
        );
      }
      return [loose[1], posixDirname(parent), entryPath];
    }
  }
  const folder = FOLDER_ID_RE.exec(name);
  if (folder && posixBasename(parent) === '_ScopeChange') {
    return [folder[1], parent, null];
  }
  throw new Refusal(
    'AMENDMENT_UNRESOLVED',
    `--amendment path is not an amendment snapshot or group-3 decision folder under _ScopeChange/: ${pyRepr(amendment)}`
  );
}

function firstLine(text: string): string {
  for (const line of pySplitlines(text)) {
    if (pyStrip(line)) {
      return pyRstrip(line);
    }
  }
  return '';
}

interface GroupFolder {
  key: [number, string, number];
  name: string;
  path: string;
}

function compareGroupFolders(a: GroupFolder, b: GroupFolder): number {
  return (
    a.key[0] - b.key[0] ||
    compareCodePoints(a.key[1], b.key[1]) ||
    a.key[2] - b.key[2] ||
    compareCodePoints(a.name, b.name) ||
    compareCodePoints(a.path, b.path)
  );
}

/** Decision-snapshot folders of one group, oldest first, and ignored look-alikes. */
async function groupFolders(
  store: WorkTree,
  root: string,
  amendmentId: string,
  group: string
): Promise<{ found: GroupFolder[]; ignored: string[] }> {
  const snapshots = await store.resolve(relJoin(root, 'checkpoint_snapshots'), root, 'checkpoint_snapshots');
  if (snapshots === null || snapshots.kind !== 'tree') {
    return { found: [], ignored: [] };
  }
  const found: GroupFolder[] = [];
  const ignored: string[] = [];
  for (const name of await store.children(snapshots.path)) {
    const loose = GROUP_PREFIX_RE.exec(name);
    if (!loose || loose[1] !== amendmentId || loose[2] !== group) {
      continue;
    }
    const match = GROUP_FOLDER_RE.exec(name);
    if (match === null) {
      ignored.push(name);
      continue;
    }
    const entry = await store.resolve(relJoin(snapshots.path, name), root, `group-${group} decision folder`);
    if (entry !== null && entry.kind === 'tree') {
      found.push({ key: [pyInt(match[3]), match[4], pyInt(match[5])], name, path: entry.path });
    }
  }
  return { found: found.sort(compareGroupFolders), ignored };
}

async function acceptedGroup3(
  store: WorkTree,
  root: string,
  amendmentId: string,
  pinned: string | null
): Promise<[string, string]> {
  let ignored: string[] = [];
  let folders: [string, string][];
  if (pinned !== null) {
    const entry = await store.resolve(pinned, root, 'group-3 decision folder');
    folders = entry && entry.kind === 'tree' ? [[posixBasename(pinned), entry.path]] : [];
  } else {
    const groups = await groupFolders(store, root, amendmentId, '3');
    ignored = groups.ignored;
    folders = groups.found.reverse().map((item) => [item.name, item.path]);
  }
  const heading = headingRe(amendmentId);
  const problems: string[] = [];
  for (const [name, folderPath] of folders) {
    const decision = await store.resolve(relJoin(folderPath, 'DECISION.md'), root, 'group-3 DECISION.md');
    const manifest = await store.resolve(relJoin(folderPath, 'ACCEPTED_MANIFEST.csv'), root, 'group-3 ACCEPTED_MANIFEST.csv');
    if (!(decision && decision.kind === 'blob' && manifest && manifest.kind === 'blob')) {
      problems.push(`${name} lacks DECISION.md or ACCEPTED_MANIFEST.csv`);
      continue;
    }
    // Only the first non-blank line counts, so a bounded prefix is read.
    const line = firstLine(decodeUtf8Sig(await store.readPrefix(decision, DECISION_PREFIX_BYTES), decision.path));
    if (heading.test(line)) {
      return [folderPath, decision.path];
    }
    problems.push(`${name}/DECISION.md first line does not record group-3 acceptance: ${pyRepr(line)}`);
  }
  if (ignored.length > 0) {
    problems.push(
      `ignored ${ignored.join(', ')} (not named ${amendmentId}_GROUP-3_[AMENDMENT-K_]YYYY-MM-DD[_N]; candidate folders do not count)`
    );
  }
  if (folders.length === 0) {
    const earlier: string[] = [];
    for (const group of ['1', '2']) {
      earlier.push(...(await groupFolders(store, root, amendmentId, group)).found.map((item) => item.name));
    }
    problems.unshift(
      `no checkpoint_snapshots/${amendmentId}_GROUP-3_* decision snapshot` +
        (earlier.length > 0
          ? ` (only ${earlier.join(', ')}; a group-1 or group-2 decision does not authorize reopening)`
          : '')
    );
  }
  throw new Refusal('GROUP3_NOT_ACCEPTED', problems.join('; '));
}

/** `_manifest_binding`: [register entry or null when missing, lexical path, bound SHA], or null when unbound. */
async function manifestBinding(
  store: WorkTree,
  manifest: Entry,
  root: string
): Promise<[Entry | null, string, string] | null> {
  const { header, rows } = readManifest(decodeUtf8Sig(await store.read(manifest), manifest.path));
  const lookup = new Map<string, string>();
  for (const name of header) {
    lookup.set(name.toLowerCase().replaceAll('-', ''), name);
  }
  const pathCol = lookup.get('path');
  const shaCol = lookup.get('sha256');
  const roleCol = lookup.get('role');
  if (!pathCol || !shaCol) {
    throw new Refusal('MANIFEST_SCHEMA', `${manifest.path} has no Path and SHA256 columns`);
  }
  let candidates = rows.filter((row) => REGISTER_NAME_RE.test(posixBasename(cell(row, pathCol))));
  if (candidates.length > 1 && roleCol) {
    const named = candidates.filter((row) => REGISTER_ROLE_RE.test(cell(row, roleCol)));
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
      `${manifest.path} binds several Amendment_Actions*.csv files and no single row's Role is the action register`
    );
  }
  const rawPath = cell(candidates[0], pathCol);
  const boundSha = cell(candidates[0], shaCol).toLowerCase();
  if (rawPath.startsWith('/')) {
    throw new Refusal('PATH_ESCAPE', `register path in ${manifest.path} is absolute: ${rawPath}`);
  }
  // Manifest paths are project-root relative; paths relative to the execution
  // root's parent are accepted too. A missing file resolves to the in-root
  // candidate so the refusal names the missing register, not an escape.
  const projectDir = posixDirname(posixDirname(root));
  const options: string[] = [];
  for (const option of [rawPath, relJoin(projectDir, rawPath)]) {
    const normal = posixNormpath(option);
    if (normal !== '..' && !normal.startsWith('../') && !options.includes(normal)) {
      options.push(normal);
    }
  }
  let escaped = false;
  let missing: string | null = null;
  for (const option of options) {
    let entry: Entry | null;
    try {
      entry = await store.resolve(option, '', 'register');
    } catch (error) {
      if (error instanceof Refusal) {
        escaped = true;
        continue;
      }
      throw error;
    }
    if (entry === null) {
      if (missing === null && insideRel(option, root)) {
        missing = option;
      }
      continue;
    }
    if (!insideRel(entry.path, root)) {
      escaped = true;
      continue;
    }
    return [entry, option, boundSha];
  }
  if (escaped || missing === null) {
    throw new Refusal(
      'PATH_ESCAPE',
      `register ${rawPath} bound in ${manifest.path} resolves outside the scope-change root (path or symlink escape)`
    );
  }
  return [null, missing, boundSha];
}

/** `_bound_register`: the binding of the latest group-2 decision snapshot that binds a register. */
async function boundRegister(
  store: WorkTree,
  root: string,
  amendmentId: string
): Promise<[Entry | null, string, string, string]> {
  const { found } = await groupFolders(store, root, amendmentId, '2');
  const manifests: Entry[] = [];
  for (const item of found) {
    const entry = await store.resolve(relJoin(item.path, 'ACCEPTED_MANIFEST.csv'), root, 'group-2 ACCEPTED_MANIFEST.csv');
    if (entry !== null && entry.kind === 'blob') {
      manifests.push(entry);
    }
  }
  if (manifests.length === 0) {
    throw new Refusal(
      'GROUP2_MANIFEST_MISSING',
      `no checkpoint_snapshots/${amendmentId}_GROUP-2_*/ACCEPTED_MANIFEST.csv binds the accepted register`
    );
  }
  for (const manifest of [...manifests].reverse()) {
    const binding = await manifestBinding(store, manifest, root);
    if (binding !== null) {
      return [binding[0], binding[1], binding[2], manifest.path];
    }
  }
  throw new Refusal(
    'REGISTER_NOT_BOUND',
    `no group-2 ACCEPTED_MANIFEST.csv of ${amendmentId} binds an Amendment_Actions*.csv register`
  );
}

function matchesDeliverable(entityId: string, deliverableId: string): boolean {
  return entityId === deliverableId || entityId.startsWith(`${deliverableId}_`);
}

function qualifyingRow(
  text: string,
  registerPath: string,
  amendmentId: string,
  deliverableId: string
): [CsvRow, boolean] {
  const { header, rows } = readRegister(text);
  const padded = header.filter((name) => name !== pyStrip(name) && REGISTER_COLUMNS.includes(pyStrip(name)));
  if (padded.length > 0) {
    throw new Refusal(
      'REGISTER_SCHEMA',
      `${registerPath} column name(s) carry stray whitespace: ${padded.map(pyRepr).join(', ')}`
    );
  }
  const missing = ['ActionType', 'EntityType', 'EntityID'].filter((column) => !header.includes(column));
  if (missing.length > 0) {
    throw new Refusal('REGISTER_SCHEMA', `${registerPath} lacks column(s) ${missing.join(', ')}`);
  }
  const hasScope = header.includes('ScopeChanging');
  rows.forEach((row, offset) => {
    if (pyStrip(cell(row, 'EntityType')).toUpperCase() !== 'DELIVERABLE') {
      return;
    }
    if (!matchesDeliverable(pyStrip(cell(row, 'EntityID')), deliverableId)) {
      return;
    }
    const paddedValues = REGISTER_COLUMNS.filter((column) => cell(row, column) !== pyStrip(cell(row, column)));
    if (paddedValues.length > 0) {
      throw new Refusal(
        'REGISTER_SCHEMA',
        `${registerPath} line ${offset + 2} (ActionSeq ${cell(row, 'ActionSeq') || '?'}) has stray whitespace in ` +
          paddedValues.map((column) => `${column} ${pyRepr(cell(row, column))}`).join(', ')
      );
    }
  });
  const named = rows.filter(
    (row) =>
      cell(row, 'EntityType').toUpperCase() === 'DELIVERABLE' &&
      matchesDeliverable(cell(row, 'EntityID'), deliverableId) &&
      (cell(row, 'AmendmentID') === '' || cell(row, 'AmendmentID') === amendmentId)
  );
  if (named.length === 0) {
    throw new Refusal('NO_DELIVERABLE_ACTION', `no ${amendmentId} register row names DELIVERABLE ${deliverableId}`);
  }
  const seqs = named.map((row) => `${cell(row, 'ActionSeq') || '?'} ${cell(row, 'ActionType') || '?'}`).join(', ');
  const removes = named.filter((row) => cell(row, 'ActionType').toUpperCase() === 'REMOVE');
  if (removes.length > 0) {
    throw new Refusal(
      'DELIVERABLE_REMOVED',
      `${amendmentId} removes ${deliverableId} (ActionSeq ${removes.map((row) => cell(row, 'ActionSeq') || '?').join(', ')}); ` +
        `a removed deliverable is not reopened, whatever other rows name it (${seqs})`
    );
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

function priorReopening(statusText: string, amendmentId: string): string | null {
  const pattern = priorReopeningRe(amendmentId);
  for (const line of pySplitlines(statusText)) {
    if (pattern.test(line)) {
      return pyStrip(line);
    }
  }
  return null;
}

function isOperationalError(error: unknown): boolean {
  return error instanceof RecordReadError || (!(error instanceof Refusal) && errorCode(error) !== undefined);
}

/**
 * Decide whether `amendment` authorizes reopening `deliverable` (a deliverable
 * folder or ID), reading the working tree. Throws `AmendmentReopenUsageError`
 * for unusable input or an unreadable record; every other outcome is a
 * decision whose `admitted` is true only when all checks pass.
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
  const cwd = pyPath(options.cwd ?? options.projectRoot);
  if (!pyIsAbsolute(cwd)) {
    throw new AmendmentReopenUsageError(`cwd must be absolute: ${options.cwd}`);
  }
  const base = await pyRealpath(cwd);
  const [deliverableId, deliverablePath] = await normalizeDeliverable(deliverable, base);
  const decision: AmendmentReopenDecision = {
    admitted: false,
    code: 'AMENDMENT_UNRESOLVED',
    reason: '',
    deliverableId,
    amendmentId: '',
    mode: 'working-tree',
    anchored: false,
    atCommit: '',
    executionRoot: '',
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
  decision.notes.push(UNANCHORED_NOTE);

  try {
    const store = new WorkTree(proj);
    let execRoot: string | null = null;
    if (deliverablePath !== null) {
      const deliverableReal = await pyRealpath(deliverablePath);
      if (!isInside(deliverableReal, proj)) {
        throw new Refusal(
          'PATH_ESCAPE',
          `deliverable folder ${deliverablePath} resolves outside ${proj} (path or symlink escape)`
        );
      }
      execRoot = await executionRoot(deliverableReal, proj);
      decision.executionRoot = execRoot;
    }

    const [amendmentId, derivedRoot, pinned] = await resolveAmendment(store, amendment, base, proj);
    decision.amendmentId = amendmentId;

    if (options.statusText !== undefined) {
      const prior = priorReopening(options.statusText, amendmentId);
      if (prior !== null) {
        throw new Refusal(
          'AMENDMENT_ALREADY_USED',
          `_STATUS.md already records a reopening under ${amendmentId} (${prior}); one tool-recorded ` +
            'reopening per accepted amendment; a further reopening needs a new amendment or a direct human record'
        );
      }
    }

    let root: string | null = null;
    if (options.scopeChangeRoot !== undefined) {
      const rel = await toRel(options.scopeChangeRoot, base, proj);
      if (rel === null) {
        throw new Refusal('PATH_ESCAPE', `--scope-change-root ${options.scopeChangeRoot} lies outside the project root`);
      }
      const entry = await store.resolve(rel, '', '--scope-change-root');
      if (entry === null || entry.kind !== 'tree') {
        throw new Refusal(
          'SCOPE_CHANGE_ROOT_NOT_FOUND',
          `--scope-change-root is not a directory: ${options.scopeChangeRoot}`
        );
      }
      root = entry.path;
    }
    if (derivedRoot !== null) {
      const entry = await store.resolve(derivedRoot, '', 'scope-change root');
      if (entry === null || entry.kind !== 'tree') {
        throw new Refusal('AMENDMENT_UNRESOLVED', `scope-change root ${derivedRoot} of --amendment is not a directory`);
      }
      if (root !== null && root !== entry.path) {
        throw new Refusal('AMENDMENT_UNRESOLVED', '--amendment path is not under --scope-change-root');
      }
      root = entry.path;
    }
    const expected = execRoot !== null ? relJoin(execRoot, '_ScopeChange') : null;
    if (root === null) {
      if (expected === null) {
        throw new Refusal(
          'SCOPE_CHANGE_ROOT_NOT_FOUND',
          'an amendment ID with a deliverable ID needs --scope-change-root or a deliverable folder'
        );
      }
      const entry = await store.resolve(expected, '', 'scope-change root');
      if (entry === null || entry.kind !== 'tree') {
        throw new Refusal('SCOPE_CHANGE_ROOT_NOT_FOUND', `no ${expected}/ beside the deliverable's execution root`);
      }
      root = entry.path;
    }
    decision.scopeChangeRoot = root;
    if (expected !== null && root !== expected) {
      throw new Refusal(
        'AMENDMENT_OUTSIDE_DELIVERABLE_ROOT',
        `${root} is not ${expected}, the scope-change root of the deliverable's execution root ${execRoot}`
      );
    }

    const [group3, group3Decision] = await acceptedGroup3(store, root, amendmentId, pinned);
    decision.group3Snapshot = group3;
    decision.group3Decision = group3Decision;

    const [register, lexical, boundSha, manifest] = await boundRegister(store, root, amendmentId);
    decision.group2Manifest = manifest;
    decision.registerPath = register !== null ? register.path : lexical;
    if (register === null || register.kind !== 'blob') {
      throw new Refusal('REGISTER_MISSING', `bound register ${decision.registerPath} does not exist`);
    }
    const data = await store.read(register);
    const actual = createHash('sha256').update(data).digest('hex');
    decision.registerSha256 = actual;
    if (actual !== boundSha) {
      throw new Refusal(
        'REGISTER_HASH_MISMATCH',
        `${decision.registerPath} SHA-256 ${actual} differs from ${boundSha} bound in ${decision.group2Manifest}`
      );
    }

    const [row, hasScope] = qualifyingRow(
      decodeUtf8Sig(data, decision.registerPath),
      decision.registerPath,
      amendmentId,
      deliverableId
    );
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
    `${decision.actionType} names ${deliverableId}; records read in the working tree (unanchored)`;
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
  /** The deliverable's current `_STATUS.md` content, checked for a prior reopening. */
  statusText?: string;
}

/**
 * Runs the checker the way `write_status.sh` runs the Root checker, less the
 * git anchoring: the Git work-tree top level is the project root (so
 * repository-relative manifest paths resolve), or the working root when it is
 * not inside a work tree. A relative amendment path is read from the working
 * root, then the project root. The App also requires the scope-change root to
 * lie inside the working root and refuses one outside it as `PATH_ESCAPE`.
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
    cwd: workingRoot,
    statusText: input.statusText
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
