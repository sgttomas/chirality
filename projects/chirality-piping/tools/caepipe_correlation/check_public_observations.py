#!/usr/bin/env python3
"""Lane-local check that public text added on a branch states no named observation of the external prover.

Owner ruling (2026-10-26): facts learned from running the external prover, from its outputs or its screens,
are written in public text generically ("the external prover", "the target tool"), with no product name,
vendor or version attached; the named detail lives in private observation notes. This check enforces it on
what a change adds. All terms come from a private terms file outside the repository and are never printed;
a finding names the place and the term's position in its list.

Terms file sections (one term per line, `#` comments and blank lines ignored):
- `[names]`: product, vendor and version strings;
- `[markers]`: words that mark an observation (blocked when a name sits within one line of one);
- `[tokens]`: distinctive observed strings, blocked wherever they appear in prose.

Prose is every added line of a non-code file, and in code files (Python, PowerShell, TypeScript, Rust) only
comments, docstrings and test function names: code may implement the behaviour it needs. Fixture CSV data
counts as code. In tests and fixtures, observed tokens that carry a product name are blocked on every line.
Paths are not screened. Commit messages in `--base..--head` and any `--file` given whole are prose too. In Markdown, the
owner's verbatim words between `<!-- owner-words -->` and `<!-- /owner-words -->` are not screened.

Exit 1 on a finding, 2 on an operational error, 0 otherwise.
"""

from __future__ import annotations

import argparse
import io
import re
import subprocess
import sys
import tokenize
from pathlib import Path

CODE_SUFFIXES = {".py", ".ps1", ".ts", ".tsx", ".js", ".rs"}
SECTIONS = ("names", "markers", "tokens")


def load_terms(path: Path) -> dict[str, list[str]]:
    terms: dict[str, list[str]] = {name: [] for name in SECTIONS}
    section = None
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("[") and line.endswith("]"):
            section = line[1:-1].strip()
            if section not in terms:
                raise ValueError("unknown section in terms file")
            continue
        if section is None:
            raise ValueError("term outside a section in terms file")
        terms[section].append(line)
    return terms


def _word(term: str, *, case: bool = False) -> re.Pattern[str]:
    # Identifier characters bound a term, so code paths and identifiers (`caepipe_mbf`) never match a name.
    return re.compile(r"(?<![A-Za-z0-9_])" + re.escape(term) + r"(?![A-Za-z0-9_])", 0 if case else re.IGNORECASE)


def python_prose_lines(text: str) -> dict[int, str]:
    """Comments, docstring-style strings and test function names of a Python source, by line number."""

    prose: dict[int, str] = {}
    try:
        tokens = list(tokenize.generate_tokens(io.StringIO(text).readline))
    except (tokenize.TokenError, IndentationError, SyntaxError):
        return {number: line for number, line in enumerate(text.splitlines(), 1)}
    previous = None
    for token in tokens:
        if token.type == tokenize.COMMENT:
            prose[token.start[0]] = prose.get(token.start[0], "") + " " + token.string
        elif token.type == tokenize.STRING and token.string.lstrip("rbuRBUfF").startswith(('"""', "'''")):
            for offset, part in enumerate(token.string.splitlines()):
                number = token.start[0] + offset
                prose[number] = prose.get(number, "") + " " + part
        elif token.type == tokenize.NAME and previous is not None and previous.string == "def" \
                and token.string.startswith("test"):
            prose[token.start[0]] = prose.get(token.start[0], "") + " " + token.string.replace("_", " ")
        if token.type not in (tokenize.NL, tokenize.NEWLINE, tokenize.INDENT, tokenize.DEDENT):
            previous = token
    return prose


def comment_prose_lines(text: str, suffix: str) -> dict[int, str]:
    """Comments of a PowerShell, TypeScript, JavaScript or Rust source, by line number (approximate)."""

    prose: dict[int, str] = {}
    block = False
    opener, closer, single = ("<#", "#>", "#") if suffix == ".ps1" else ("/*", "*/", "//")
    for number, line in enumerate(text.splitlines(), 1):
        if block:
            prose[number] = line
            if closer in line:
                block = False
            continue
        if opener in line:
            prose[number] = line[line.index(opener):]
            block = closer not in line[line.index(opener) + len(opener):]
            continue
        index = _comment_index(line, single)
        if index is not None:
            prose[number] = line[index:]
    return prose


def _comment_index(line: str, single: str) -> int | None:
    quote = None
    i = 0
    while i < len(line):
        char = line[i]
        if quote:
            if char == "\\":
                i += 2
                continue
            if char == quote:
                quote = None
        elif char in "\"'`":
            quote = char
        elif line.startswith(single, i):
            return i
        i += 1
    return None


OWNER_WORDS_OPEN = "<!-- owner-words -->"
OWNER_WORDS_CLOSE = "<!-- /owner-words -->"


def _without_owner_words(lines: dict[int, str]) -> dict[int, str]:
    """Drop lines between owner-words markers: the owner's verbatim words are quoted, not observations."""

    kept: dict[int, str] = {}
    inside = False
    for number in sorted(lines):
        line = lines[number]
        if OWNER_WORDS_OPEN in line:
            inside = True
        if not inside:
            kept[number] = line
        if OWNER_WORDS_CLOSE in line:
            inside = False
    return kept


def prose_of(path: str, text: str) -> dict[int, str]:
    suffix = Path(path).suffix.lower()
    if suffix == ".md":
        return _without_owner_words({number: line for number, line in enumerate(text.splitlines(), 1)})
    if suffix == ".py":
        return python_prose_lines(text)
    if suffix in CODE_SUFFIXES:
        return comment_prose_lines(text, suffix)
    return {number: line for number, line in enumerate(text.splitlines(), 1)}


def scan(label: str, lines: dict[int, str], terms: dict[str, list[str]]) -> list[str]:
    findings: list[str] = []
    tokens = [(index, term.lower()) for index, term in enumerate(terms["tokens"], 1)]
    names = [(index, _word(term, case=True)) for index, term in enumerate(terms["names"], 1)]
    markers = [(index, _word(term)) for index, term in enumerate(terms["markers"], 1)]
    numbers = sorted(lines)
    for number in numbers:
        text = lines[number]
        lowered = text.lower()
        for index, term in tokens:
            if term in lowered:
                findings.append(f"{label}:{number}: observed token #{index}")
        for name_index, pattern in names:
            if not pattern.search(text):
                continue
            window = " ".join(lines.get(n, "") for n in (number - 1, number, number + 1))
            for marker_index, marker in markers:
                if marker.search(window):
                    findings.append(f"{label}:{number}: name #{name_index} near observation marker #{marker_index}")
    return findings


def _git(repo: Path, *args: str) -> str:
    return subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True, check=True).stdout


def added_line_numbers(repo: Path, base: str, head: str) -> dict[str, set[int]]:
    diff = _git(repo, "diff", "--unified=0", "--no-color", "--no-renames", f"{base}...{head}")
    added: dict[str, set[int]] = {}
    path = None
    for line in diff.splitlines():
        if line.startswith("+++ "):
            path = None if line[4:] == "/dev/null" else line[6:]
        elif line.startswith("@@") and path is not None:
            match = re.match(r"@@ -\S+ \+(\d+)(?:,(\d+))? @@", line)
            start, count = int(match.group(1)), int(match.group(2) or "1")
            added.setdefault(path, set()).update(range(start, start + count))
    return added


def scan_named_tokens(label: str, lines: dict[int, str], terms: dict[str, list[str]]) -> list[str]:
    """Observed tokens that carry a product name, on every line: test data and fixtures may hold observed
    layouts, never the product's own label."""

    names = [_word(term, case=True) for term in terms["names"]]
    named = [(index, term.lower()) for index, term in enumerate(terms["tokens"], 1)
             if any(pattern.search(term) for pattern in names)]
    return [f"{label}:{number}: named observed token #{index}"
            for number in sorted(lines) for index, term in named if term in lines[number].lower()]


def _data_path(path: str) -> bool:
    parts = Path(path).parts
    return "tests" in parts or "fixtures" in parts


def check_range(repo: Path, base: str, head: str, terms: dict[str, list[str]],
                messages_base: str | None = None) -> list[str]:
    findings: list[str] = []
    for path, numbers in sorted(added_line_numbers(repo, base, head).items()):
        try:
            text = _git(repo, "show", f"{head}:{path}")
        except subprocess.CalledProcessError:
            continue
        # A fixture data file (CSV) is consumed by code like code itself; only the named-token rule applies.
        if not (_data_path(path) and Path(path).suffix.lower() == ".csv"):
            prose = prose_of(path, text)
            findings += scan(path, {n: prose[n] for n in numbers if n in prose}, terms)
        if _data_path(path):
            all_lines = dict(enumerate(text.splitlines(), 1))
            findings += scan_named_tokens(path, {n: all_lines[n] for n in numbers if n in all_lines}, terms)
    # Commit messages already published cannot change; a pre-push run screens only the new ones.
    for commit in _git(repo, "rev-list", f"{messages_base or base}..{head}").split():
        message = _git(repo, "log", "-1", "--format=%B", commit)
        findings += scan(f"commit {commit[:10]}", dict(enumerate(message.splitlines(), 1)), terms)
    return findings


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--terms-file", required=True, type=Path)
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    parser.add_argument("--base")
    parser.add_argument("--head", default="HEAD")
    parser.add_argument("--messages-base", help="screen commit messages only after this ref (default: --base)")
    parser.add_argument("--file", action="append", default=[], type=Path, help="a whole file to screen as prose")
    args = parser.parse_args(argv)
    try:
        terms = load_terms(args.terms_file)
        findings: list[str] = []
        if args.base:
            findings += check_range(args.repo, args.base, args.head, terms, args.messages_base)
        for path in args.file:
            findings += scan(str(path), prose_of(str(path), path.read_text(encoding="utf-8")), terms)
    except (OSError, ValueError, subprocess.CalledProcessError):
        print("check_public_observations: operational error (terms file, refs or files unreadable)", file=sys.stderr)
        return 2
    for finding in findings:
        print(finding)
    print(f"check_public_observations: {len(findings)} finding(s)")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
