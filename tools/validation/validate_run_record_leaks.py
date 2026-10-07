#!/usr/bin/env python3
"""Leak check for the run records a change adds or modifies (D-GOV-45).

Run records are history and are not otherwise tested. This check scans only
the run-record files changed in `--base..--head` (a PR's complete diff, or the
commits a push added), because the repository is public: a credential in a
new run record is published the moment it merges.

- BLOCK (exit 1): a credential pattern in a changed text run record. Values
  that are self-evidently fake (containing EXAMPLE, DUMMY, FAKE, PLACEHOLDER,
  TEST) are ignored.
- BLOCK (exit 1): a changed run-record symlink whose target is absolute or
  resolves outside the repository. Such a link points into one machine's
  filesystem: it dangles everywhere else and carries no evidence bytes.
  Commit the bytes themselves. Links that stay inside the repository pass.
- WARN (exit 0): a changed run-record file larger than 5 MB. Keep traces,
  screenshots and archives as CI artifacts rather than committing them.

Reads file bytes from Git, so it works in sparse checkouts. Exit 2 on
operational errors (refs unresolvable).
"""
from __future__ import annotations

import argparse
import posixpath
import re
import subprocess
import sys

RUN_RECORD_RE = re.compile(r'(^|/)(_Coordination/AgentRuns|_run_records)/')
BINARY_EXTENSIONS = ('.zip', '.png', '.jpg', '.jpeg', '.gif', '.webp', '.webm', '.gz', '.sqlite3', '.bin', '.pdf')
LARGE_BYTES = 5_000_000
SYMLINK_MODE = '120000'
FAKE_RE = re.compile(r'(?i)example|dummy|fake|placeholder|test')
PATTERNS = {
    'aws-access-key': r'\b(?:AKIA|ASIA)[0-9A-Z]{16}\b',
    'github-token': r'\b(?:gh[pousr]_[A-Za-z0-9]{36,}|github_pat_[A-Za-z0-9_]{60,})\b',
    'anthropic-key': r'\bsk-ant-[A-Za-z0-9_-]{32,}',
    'openai-key': r'\bsk-(?!ant-)(?:proj-|svcacct-)?[A-Za-z0-9_-]{40,}',
    'slack-token': r'\bxox[abposr]-[A-Za-z0-9-]{10,}',
    'google-api-key': r'\bAIza[0-9A-Za-z_-]{35}\b',
    'stripe-live-key': r'\b[rs]k_live_[0-9A-Za-z]{20,}',
    'private-key': r'-----BEGIN (?:RSA |EC |DSA |OPENSSH |PGP |ENCRYPTED )?PRIVATE KEY(?: BLOCK)?-----',
    'bearer-token': r'(?i)\bauthorization["\']?\s*[:=]\s*["\']?bearer\s+[A-Za-z0-9._~+/-]{32,}',
    'jwt': r'\beyJ[A-Za-z0-9_-]{10,}\.eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{20,}',
    'aws-secret-key': r'(?i)aws_?secret_?access_?key["\']?\s*[:=]\s*["\']?[A-Za-z0-9/+]{40}\b',
    'gitlab-token': r'\bglpat-[A-Za-z0-9_-]{20,}',
    'huggingface-token': r'\bhf_[A-Za-z]{34,}\b',
    'npm-token': r'\bnpm_[A-Za-z0-9]{36}\b',
    'slack-webhook': r'https://hooks\.slack\.com/services/T[A-Z0-9]+/B[A-Z0-9]+/[A-Za-z0-9]{20,}',
}
COMPILED = {name: re.compile(pattern) for name, pattern in PATTERNS.items()}


def git(*args: str) -> bytes:
    return subprocess.check_output(['git', *args])


def changed_run_records(base: str, head: str) -> list[tuple[str, str]]:
    """(path, head mode) for each run record added, modified or retyped."""
    fields = git('diff', '--raw', '--no-renames', '--diff-filter=AMT', '-z', base, head, '--').decode().split('\0')
    # --raw -z alternates ':<old mode> <new mode> <old oid> <new oid> <status>' and the path.
    return [(path, meta.split()[1]) for meta, path in zip(fields[0::2], fields[1::2])
            if RUN_RECORD_RE.search(path)]


def escapes_repository(path: str, target: str) -> bool:
    if target.startswith(('/', '\\', '~')) or re.match(r'^[A-Za-z]:[\\/]', target):
        return True
    resolved = posixpath.normpath(posixpath.join(posixpath.dirname(path), target))
    return resolved == '..' or resolved.startswith('../')


def findings(path: str, data: bytes, mode: str = '100644') -> list[tuple[str, str]]:
    results = []
    if mode == SYMLINK_MODE:
        target = data.decode('utf-8', errors='replace')
        if escapes_repository(path, target):
            results.append(('BLOCK', f'{path}: symlink to a machine-local path ({target}); '
                                     'commit the evidence bytes, not a link'))
        return results
    if len(data) > LARGE_BYTES:
        results.append(('WARN', f'{path}: {len(data) / 1e6:.1f} MB run-record file; keep large evidence as CI artifacts'))
    if path.lower().endswith(BINARY_EXTENSIONS):
        return results
    text = data.decode('utf-8', errors='ignore')
    for name, pattern in COMPILED.items():
        for match in pattern.finditer(text):
            if not FAKE_RE.search(match.group(0)):
                line = text.count('\n', 0, match.start()) + 1
                results.append(('BLOCK', f'{path}:{line}: possible {name} ({match.group(0)[:8]}…)'))
                break
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--base', required=True)
    parser.add_argument('--head', default='HEAD')
    args = parser.parse_args()
    try:
        paths = changed_run_records(args.base, args.head)
        results = [f for p, mode in paths for f in findings(p, git('show', f'{args.head}:{p}'), mode)]
    except subprocess.CalledProcessError as exc:
        print(f'ERROR: cannot read {args.base}..{args.head}: {exc}', file=sys.stderr)
        return 2
    for severity, message in results:
        print(f'{severity}: {message}')
    blocks = sum(severity == 'BLOCK' for severity, _ in results)
    links = sum(severity == 'BLOCK' and 'symlink to' in message for severity, message in results)
    print(f'{"BLOCK" if blocks else "PASS"}: {len(paths)} changed run-record file(s) scanned; '
          f'{blocks - links} possible credential(s); {links} machine-local symlink(s).')
    return 1 if blocks else 0


if __name__ == '__main__':
    raise SystemExit(main())
