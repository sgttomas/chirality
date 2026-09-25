#!/usr/bin/env python3
"""Leak check for the run records a change adds or modifies (D-GOV-45).

Run records are history and are not otherwise tested. This check scans only
the run-record files changed in `--base..--head` (a PR's complete diff, or the
commits a push added), because the repository is public: a credential in a
new run record is published the moment it merges.

- BLOCK (exit 1): a credential pattern in a changed text run record. Values
  that are self-evidently fake (containing EXAMPLE, DUMMY, FAKE, PLACEHOLDER,
  TEST) are ignored.
- WARN (exit 0): a changed run-record file larger than 5 MB. Keep traces,
  screenshots and archives as CI artifacts rather than committing them.

Reads file bytes from Git, so it works in sparse checkouts. Exit 2 on
operational errors (refs unresolvable).
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys

RUN_RECORD_RE = re.compile(r'(^|/)(_Coordination/AgentRuns|_run_records)/')
BINARY_EXTENSIONS = ('.zip', '.png', '.jpg', '.jpeg', '.gif', '.webp', '.webm', '.gz', '.sqlite3', '.bin', '.pdf')
LARGE_BYTES = 5_000_000
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
    'bearer-token': r'(?i)\bauthorization:\s*bearer\s+[A-Za-z0-9._~+/-]{32,}',
}
COMPILED = {name: re.compile(pattern) for name, pattern in PATTERNS.items()}


def git(*args: str) -> bytes:
    return subprocess.check_output(['git', *args])


def changed_run_records(base: str, head: str) -> list[str]:
    out = git('diff', '--name-only', '--no-renames', '--diff-filter=AM', '-z', base, head, '--').decode()
    return [p for p in out.split('\0') if p and RUN_RECORD_RE.search(p)]


def findings(path: str, data: bytes) -> list[tuple[str, str]]:
    results = []
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
    except subprocess.CalledProcessError as exc:
        print(f'ERROR: cannot diff {args.base}..{args.head}: {exc}', file=sys.stderr)
        return 2
    results = [f for p in paths for f in findings(p, git('show', f'{args.head}:{p}'))]
    for severity, message in results:
        print(f'{severity}: {message}')
    blocks = sum(severity == 'BLOCK' for severity, _ in results)
    print(f'{"BLOCK" if blocks else "PASS"}: {len(paths)} changed run-record file(s) scanned; '
          f'{blocks} possible credential(s).')
    return 1 if blocks else 0


if __name__ == '__main__':
    raise SystemExit(main())
