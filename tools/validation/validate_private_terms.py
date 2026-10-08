#!/usr/bin/env python3
"""Private-term check for the files a change adds or modifies.

The repository is public. The owner's machine names (the Mac's network name,
its host names, earlier names it answered to) must never be committed, in any
form. This check keeps them out without publishing them: the terms come from
outside the repository, are never printed, and are matched in plain, split,
escaped and character-class forms (`Ex""ample`, `box[.]lan[.]example`), case
insensitively.

Terms (one per line; blank lines and `#` comments ignored) come from any of:
- the `PRIVATE_TERMS` environment variable (CI: the `PRIVATE_TERMS`
  repository secret);
- `--terms-file PATH` (a local file kept outside the repository);
- `--from-host` (this machine's own names, read at run time: `hostname`, and
  on macOS `scutil --get LocalHostName` and `ComputerName`).

What is scanned:
- each file added in `--base..--head` (or staged, with `--staged`), whole;
- each modified file's added lines only, so history is not re-scanned;
- `.gz` files decompressed, whole; other binary files are skipped.

Rules:
- BLOCK (exit 1): a private term, in any form. The finding names the file,
  the line and the term's position in the list, never the term.
- BLOCK (exit 1): a pytest junit `hostname` attribute with a real value in a
  run record (`_Coordination/AgentRuns/` or `_run_records/`). It needs no
  terms, so it runs even where the secret is unavailable. Remove the
  attribute before committing; `hostname=""` and `hostname="<host>"` pass.
- NOTE (exit 0): no terms configured (for example, a pull request from a fork,
  which receives no secrets). Only the junit rule ran.

Exit 2 on operational errors (refs unresolvable).
"""
from __future__ import annotations

import argparse
import gzip
import os
import re
import subprocess
import sys

RUN_RECORD_RE = re.compile(r'(^|/)(_Coordination/AgentRuns|_run_records)/')
BINARY_EXTENSIONS = ('.zip', '.png', '.jpg', '.jpeg', '.gif', '.webp', '.webm', '.sqlite3', '.bin', '.pdf',
                     '.ico', '.icns', '.woff', '.woff2', '.ttf', '.dmg', '.wasm')
# Up to six non-word characters may sit between any two characters of a term:
# quotes, brackets, backslashes, dots, hyphens, spaces and underscores.
JOINER = rb'[\W_]{0,6}'
MIN_TERM_CHARS = 6
JUNIT_HOST_RE = re.compile(rb'<testsuites?\b[^>]*?\shostname="(?!(?:|<host>)")[^"]*"')


def git(*args: str) -> bytes:
    return subprocess.check_output(['git', *args])


def term_pattern(term: str) -> re.Pattern[bytes] | None:
    """Every alphanumeric character of the term, in order, with joiners between them."""
    chars = [c for c in term if c.isalnum()]
    if len(chars) < MIN_TERM_CHARS:
        return None
    return re.compile(JOINER.join(re.escape(c.encode()) for c in chars), re.IGNORECASE)


def host_terms() -> list[str]:
    commands = [['hostname'], ['scutil', '--get', 'LocalHostName'], ['scutil', '--get', 'ComputerName']]
    terms = []
    for command in commands:
        try:
            value = subprocess.run(command, capture_output=True, text=True, check=False).stdout.strip()
        except OSError:
            continue
        if value:
            terms.append(value)
    return terms


def load_terms(args: argparse.Namespace) -> list[str]:
    raw = os.environ.get('PRIVATE_TERMS', '').splitlines()
    if args.terms_file:
        with open(args.terms_file, encoding='utf-8') as handle:
            raw += handle.read().splitlines()
    if args.from_host:
        raw += host_terms()
    terms = []
    for line in raw:
        line = line.strip()
        if line and not line.startswith('#') and line not in terms:
            terms.append(line)
    return terms


def changes(base: str | None, head: str, staged: bool) -> list[tuple[str, str]]:
    """(status, path) for each file added, modified or retyped."""
    span = ['--cached'] if staged else [base, head]
    fields = git('diff', '--name-status', '--no-renames', '--diff-filter=AMT', '-z', *span, '--').decode().split('\0')
    return [(status, path) for status, path in zip(fields[0::2], fields[1::2]) if path]


def blob(path: str, head: str, staged: bool) -> bytes:
    return git('show', f':{path}' if staged else f'{head}:{path}')


def added_lines(path: str, base: str | None, head: str, staged: bool) -> list[tuple[int, bytes]]:
    span = ['--cached'] if staged else [base, head]
    lines, number = [], 0
    for line in git('diff', '-U0', '--no-color', *span, '--', path).splitlines():
        hunk = re.match(rb'@@ -\S+ \+(\d+)', line)
        if hunk:
            number = int(hunk.group(1))
        elif line.startswith(b'+') and not line.startswith(b'+++'):
            lines.append((number, line[1:]))
            number += 1
    return lines


def units(status: str, path: str, base: str | None, head: str, staged: bool) -> list[tuple[int, bytes]]:
    """The numbered lines to scan for one changed file."""
    lower = path.lower()
    if lower.endswith(BINARY_EXTENSIONS):
        return []
    if lower.endswith('.gz'):
        try:
            return list(enumerate(gzip.decompress(blob(path, head, staged)).splitlines(), 1))
        except (OSError, EOFError):
            return []
    if status == 'M':
        return added_lines(path, base, head, staged)
    data = blob(path, head, staged)
    if b'\0' in data[:8192]:
        return []
    return list(enumerate(data.splitlines(), 1))


def findings(path: str, lines: list[tuple[int, bytes]], patterns: list[re.Pattern[bytes]]) -> list[str]:
    results = []
    run_record = bool(RUN_RECORD_RE.search(path))
    for number, text in lines:
        for index, pattern in enumerate(patterns, 1):
            if pattern.search(text):
                results.append(f'{path}:{number}: private term {index} (any form)')
        if run_record and JUNIT_HOST_RE.search(text):
            results.append(f'{path}:{number}: junit hostname attribute; remove it before committing')
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--base', help='base revision (required unless --staged)')
    parser.add_argument('--head', default='HEAD')
    parser.add_argument('--staged', action='store_true', help='scan the index against HEAD (for a pre-commit hook)')
    parser.add_argument('--terms-file', help='a file of private terms kept outside the repository')
    parser.add_argument('--from-host', action='store_true', help="also screen this machine's own names")
    args = parser.parse_args()
    if not args.staged and not args.base:
        parser.error('--base is required unless --staged')

    terms = load_terms(args)
    patterns, short = [], 0
    for term in terms:
        pattern = term_pattern(term)
        if pattern is None:
            short += 1
        else:
            patterns.append(pattern)
    try:
        changed = changes(args.base, args.head, args.staged)
        results = [f for status, path in changed
                   for f in findings(path, units(status, path, args.base, args.head, args.staged), patterns)]
    except subprocess.CalledProcessError as exc:
        print(f'ERROR: cannot read the change: {exc}', file=sys.stderr)
        return 2

    if not terms:
        print('NOTE: no private terms configured (PRIVATE_TERMS unset or empty); only the junit hostname rule ran.')
    if short:
        print(f'NOTE: {short} term(s) shorter than {MIN_TERM_CHARS} alphanumeric characters were not screened.')
    for message in results:
        print(f'BLOCK: {message}')
    print(f'{"BLOCK" if results else "PASS"}: {len(changed)} changed file(s) scanned against '
          f'{len(patterns)} private term(s); {len(results)} finding(s).')
    return 1 if results else 0


if __name__ == '__main__':
    raise SystemExit(main())
