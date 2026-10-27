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

Prose is every line of a non-code file, and in code files (Python, PowerShell, TypeScript, Rust) only
comments, docstrings and test function names: code may implement the behaviour it needs. Fixture CSV data
counts as code. In tests and fixtures, observed tokens that carry a product name are blocked on every line.
Comment extraction outside Python is deliberately over-inclusive (quotes ignored, block nesting counted). Every
prose line, whatever its source, is matched as visible text: links keep their labels, and blockquote,
emphasis and code markers are removed. Names and markers match
regardless of case. Consecutive prose lines are read as one text, so a term wrapped across lines still matches; a change is screened in the context of its whole file, and a finding is reported
when a match involves an added line. Paths and file names are not screened for names and markers. Commit messages in `--base..--head` and any
`--file` given whole are prose too. In Markdown, the owner's verbatim words between `<!-- owner-words -->` and
`<!-- /owner-words -->` are not screened; an unpaired marker is an operational error.

The check is a lexical aid to review, not a proof that text is clean; review of the change remains the control.

Exit 1 on a finding, 2 on an operational error, 0 otherwise.
"""

from __future__ import annotations

import argparse
import ast
import html
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


def _normal(text: str) -> str:
    return " ".join(text.split())


def _word(term: str) -> re.Pattern[str]:
    # Identifier characters bound a term, so code paths and identifiers (`caepipe_mbf`) never match a name.
    return re.compile(r"(?<![A-Za-z0-9_])" + re.escape(_normal(term)) + r"(?![A-Za-z0-9_])", re.IGNORECASE)


# Paths and file names (`Design/x-notes.md`) are not prose; they are blanked, offsets kept, before names
# and markers are matched. Only a word that is clearly a path is blanked: after its surrounding punctuation
# is stripped it must end in a separator or a known file extension, or join path segments that hold an
# underscore. `Name/Other`, `Name/9.99` and sentence-final `Name/Other.` stay prose. Observed tokens are
# still matched on the unmasked text.
FILE_EXTENSION = re.compile(r"\.(?:md|py|json|ya?ml|txt|csv|mbf|ps1|rs|tsx?|js|toml|sh)$", re.IGNORECASE)
PATH_WORD = re.compile(r"[\w.-]+(?:[/\\][\w.-]+)*[/\\]?")
EDGE_PUNCTUATION = "`'\"()[]<>{}|,;:!?."


def _path(word: str) -> bool:
    if not PATH_WORD.fullmatch(word):
        return False
    separated = "/" in word or "\\" in word
    return bool(FILE_EXTENSION.search(word)) or word.endswith(("/", "\\")) or (separated and "_" in word)


def _unpathed(text: str) -> str:
    out = list(text)
    for match in re.finditer(r"\S+", text):
        word = match.group()
        lead = len(word) - len(word.lstrip(EDGE_PUNCTUATION))
        core = word.strip(EDGE_PUNCTUATION)
        if core and _path(core):
            start = match.start() + lead
            out[start:start + len(core)] = " " * len(core)
    return "".join(out)


COMMENT_CLOSER = re.compile(r"(?:\*+/|#>)\s*$")
COMMENT_OPENER = re.compile(r"^(?:<#|/\*+!?|//+!?|#+|\*+)")


def _strip_comment(text: str) -> str:
    """The words of one comment line, without its comment syntax, so wrapped comments join as prose.
    A closing delimiter is removed before an opening prefix, so a bare `#>` or `*/` leaves nothing."""

    return COMMENT_OPENER.sub("", COMMENT_CLOSER.sub("", text.strip())).strip()


def _phrase(term: str) -> re.Pattern[str]:
    return re.compile(re.escape(_normal(term)), re.IGNORECASE)


def python_prose_lines(text: str) -> dict[int, str]:
    """Comments, docstring-style strings and test function names of a Python source, by line number."""

    prose: dict[int, str] = {}
    try:
        tokens = list(tokenize.generate_tokens(io.StringIO(text).readline))
        ast.parse(text)
    except (tokenize.TokenError, IndentationError, SyntaxError, ValueError):
        return {number: line for number, line in enumerate(text.splitlines(), 1)}
    # Docstrings in any quoting (a one-line single-quoted docstring is not triple-quoted), as the span of
    # their expression, so every implicitly concatenated literal belongs to it. AST columns count UTF-8
    # bytes and tokenizer columns characters; spans are converted to characters.
    source = text.splitlines()

    def position(line: int, byte_column: int) -> tuple[int, int]:
        return line, len(source[line - 1].encode("utf-8")[:byte_column].decode("utf-8", errors="ignore"))

    docstrings = []
    for node in ast.walk(ast.parse(text)):
        if isinstance(node, (ast.Module, ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)) and node.body:
            first = node.body[0]
            if isinstance(first, ast.Expr) and isinstance(first.value, ast.Constant) \
                    and isinstance(first.value.value, str):
                docstrings.append((position(first.lineno, first.col_offset),
                                   position(first.end_lineno, first.end_col_offset)))
    previous = None
    for token in tokens:
        if token.type == tokenize.COMMENT:
            prose[token.start[0]] = prose.get(token.start[0], "") + " " + _strip_comment(token.string)
        elif token.type == tokenize.STRING and (any(low <= token.start and token.end <= high
                                                    for low, high in docstrings)
                                                or token.string.lstrip("rbuRBUfF").startswith(('"""', "'''"))):
            for offset, part in enumerate(_string_lines(token.string)):
                number = token.start[0] + offset
                prose[number] = prose.get(number, "") + ("" if part.startswith(GLUE) else " ") + part
        elif token.type == tokenize.NAME and previous is not None and previous.string == "def" \
                and token.string.startswith("test"):
            prose[token.start[0]] = prose.get(token.start[0], "") + " " + token.string.replace("_", " ")
        if token.type not in (tokenize.NL, tokenize.NEWLINE, tokenize.INDENT, tokenize.DEDENT):
            previous = token
    return prose


GLUE = "\x00"  # marks a prose line that continues the previous one without a separator
STRING_OPENING = re.compile(r"[rbuRBUfF]*(\'\'\'|\"\"\"|\'|\")")


def _string_lines(literal: str) -> list[str]:
    """The text of a string literal by source line, without prefix and delimiters, so implicitly
    concatenated fragments (`'Widget ' 'overflow'`) join as prose."""

    if "\n" not in literal:
        try:
            value = ast.literal_eval(literal)
        except (ValueError, SyntaxError):
            value = None
        if isinstance(value, str):
            return [value]
    raw = literal.splitlines()
    opening = STRING_OPENING.match(literal)
    if opening:
        raw[0] = raw[0][len(opening.group(0)):]
        if raw[-1].endswith(opening.group(1)):
            raw[-1] = raw[-1][:-len(opening.group(1))]
    # An odd run of backslashes at a line end continues the string without a line break: the next line is
    # glued on (GLUE), so a word split across the continuation reads whole.
    parts, glue = [], False
    for part in raw:
        continued = (len(part) - len(part.rstrip("\\"))) % 2 == 1
        text = part[:-1] if continued else part
        parts.append((GLUE if glue else "") + text)
        # Whitespace before the backslash is text, so it still separates the next line's words.
        glue = continued and not text[-1:].isspace()
    return parts


def comment_prose_lines(text: str, suffix: str) -> dict[int, str]:
    """Comments of a PowerShell, TypeScript, JavaScript or Rust source, by line number.

    Deliberately over-inclusive rather than parsed: quotes are ignored, so a line is prose from its first
    comment opener on, and block comments count their nesting depth. A string, lifetime or regular
    expression that looks like a comment adds code to the prose; it never hides a comment."""

    prose: dict[int, str] = {}
    depth = 0
    opener, closer, single = ("<#", "#>", "#") if suffix == ".ps1" else ("/*", "*/", "//")
    for number, line in enumerate(text.splitlines(), 1):
        start = 0 if depth else None
        i = 0
        while i < len(line):
            if line.startswith(opener, i):
                start = i if start is None else start
                depth, i = depth + 1, i + len(opener)
            elif depth and line.startswith(closer, i):
                depth, i = depth - 1, i + len(closer)
            elif not depth and line.startswith(single, i):
                start = i if start is None else start
                break
            else:
                i += 1
        if start is not None:
            prose[number] = _strip_comment(line[start:])
    return prose


OWNER_WORDS_OPEN = "<!-- owner-words -->"
OWNER_WORDS_CLOSE = "<!-- /owner-words -->"


def _without_owner_words(lines: dict[int, str]) -> dict[int, str]:
    """Drop the text between owner-words markers: the owner's verbatim words are quoted, not observations.
    Text outside a marked span, on the marker lines too, is kept; an unpaired marker raises ValueError."""

    kept: dict[int, str] = {}
    inside = False
    for number in sorted(lines):
        line, out = lines[number], ""
        while line:
            marker = OWNER_WORDS_CLOSE if inside else OWNER_WORDS_OPEN
            other = OWNER_WORDS_OPEN if inside else OWNER_WORDS_CLOSE
            at, stray = line.find(marker), line.find(other)
            if stray != -1 and (at == -1 or stray < at):
                raise ValueError("unpaired owner-words marker")
            if at == -1:
                out += "" if inside else line
                break
            out += "" if inside else line[:at] + " "
            line, inside = line[at + len(marker):], not inside
        if out.strip():
            kept[number] = out
    if inside:
        raise ValueError("unpaired owner-words marker")
    return kept


MARKDOWN_QUOTE = re.compile(r"^(?:\s*>)+")
# Markdown and HTML syntax rewritten to the visible text, in order, over a whole paragraph so that a link or
# tag wrapped across lines is read as written. HTML comments are taken out and read as paragraphs of their
# own, inline links with balanced destinations keep their labels (`_unlinked`), break and block tags become
# spaces, and a rewrite below keeps a link's label (its first group) or substitutes a literal. Every
# character keeps the source line it came from.
HTML_COMMENT = re.compile(r"<!--(.*?)(?:-->|\Z)", re.DOTALL)
LINK_OPEN = re.compile(r"!?\[([^\[\]]*)\]\(")
TAG_BODY = r"""(?:[^<>"']|"[^"]*"|'[^']*')*>"""  # attributes, with `>` allowed inside quoted values
BLOCK_TAG = re.compile(r"</?(?:br|p|div|li|ul|ol|dl|dt|dd|tr|td|th|table|thead|tbody|h[1-6]|hr|blockquote|pre"
                       r"|section|details|summary)\b" + TAG_BODY, re.IGNORECASE)
VISIBLE_TEXT = (
    (re.compile(r"!?\[([^\[\]]*)\]\[[^\[\]]*\]"), 1),
    (re.compile(r"!?\[|\]"), ""),
    (BLOCK_TAG, " "),
    (re.compile(r"</?[A-Za-z]" + TAG_BODY + r"|<[a-z][a-z0-9+.-]*:[^<>\s]*>"), ""),
    (re.compile(r"&(?:#[0-9]+|#[xX][0-9a-fA-F]+|[A-Za-z][A-Za-z0-9]*);"), html.unescape),
    (re.compile(r"\\(?=\s|$)"), " "),  # a Markdown hard line break
    (re.compile(r"[*~`]+|(?<![A-Za-z0-9])_+|_+(?![A-Za-z0-9])"), ""),
    (re.compile(r"\s+"), " "),
)
SENTENCE_END = re.compile(r"[.!?](?=\s|$)")
# Abbreviations whose full stop does not end a sentence (compared without the final stop, lower case).
ABBREVIATIONS = {"i.e", "e.g", "etc", "vs", "cf", "approx", "incl", "excl", "resp", "viz", "al", "fig", "figs",
                 "eq", "eqs", "sec", "no", "nos", "ref", "refs", "vol", "ch", "p", "pp", "dr", "mr", "ms", "st"}
LAST_WORD = re.compile(r"[\w.]+$")


def prose_of(path: str, text: str) -> dict[int, str]:
    suffix = Path(path).suffix.lower()
    if suffix == ".md":
        return _without_owner_words({number: line for number, line in enumerate(text.splitlines(), 1)})
    if suffix == ".py":
        return python_prose_lines(text)
    if suffix in CODE_SUFFIXES:
        return comment_prose_lines(text, suffix)
    return {number: line for number, line in enumerate(text.splitlines(), 1)}


def _rewrite(pattern: re.Pattern[str], replacement, text: str, owners: list[int]) -> tuple[str, list[int]]:
    out: list[str] = []
    own: list[int] = []
    position = 0
    for match in pattern.finditer(text):
        out.append(text[position:match.start()])
        own.extend(owners[position:match.start()])
        if isinstance(replacement, int):
            out.append(match.group(replacement))
            own.extend(owners[match.start(replacement):match.end(replacement)])
        else:
            literal = replacement(match.group()) if callable(replacement) else replacement
            out.append(literal)
            own.extend([owners[match.start()]] * len(literal))
        position = match.end()
    out.append(text[position:])
    own.extend(owners[position:])
    return "".join(out), own


def _link_end(text: str, index: int) -> int | None:
    """The index just past an inline link's closing parenthesis, given the index after its opening one:
    an optional `<...>` or balanced destination, then an optional quoted or parenthesized title, with
    backslash escapes honoured. None when the text is not a well-formed inline link."""

    size = len(text)

    def blank(at: int) -> int:
        while at < size and text[at].isspace():
            at += 1
        return at

    index = blank(index)
    if index < size and text[index] == "<":
        index += 1
        while index < size and text[index] != ">":
            index += 2 if text[index] == "\\" else 1
        index += 1
    else:
        depth = 0
        while index < size and not text[index].isspace():
            if text[index] == "\\":
                index += 2
                continue
            if text[index] == "(":
                depth += 1
            elif text[index] == ")":
                if depth == 0:
                    break
                depth -= 1
            index += 1
    index = blank(index)
    if index < size and text[index] in "\"'(":
        close = ")" if text[index] == "(" else text[index]
        index += 1
        while index < size and text[index] != close:
            index += 2 if text[index] == "\\" else 1
        index = blank(index + 1)
    return index + 1 if index < size and text[index] == ")" else None


def _unlinked(text: str, owners: list[int]) -> tuple[str, list[int]]:
    """Inline links and images reduced to their labels; the destination's parentheses are balanced."""

    out: list[str] = []
    own: list[int] = []
    position = 0
    for match in LINK_OPEN.finditer(text):
        if match.start() < position:
            continue
        index = _link_end(text, match.end())
        if index is None:
            continue
        out.append(text[position:match.start()])
        own.extend(owners[position:match.start()])
        out.append(match.group(1))
        own.extend(owners[match.start(1):match.end(1)])
        position = index
    out.append(text[position:])
    own.extend(owners[position:])
    return "".join(out), own


def _paragraphs(lines: dict[int, str], blank_breaks: bool = True) -> list[tuple[str, list[int], set[int]]]:
    """Consecutive prose lines read as one visible, whitespace-normalized text; a gap in line numbers ends a
    paragraph, and so does a blank line when `blank_breaks` (text, not code comments, whose delimiter-only
    lines are empty). Each character carries the source line it came from. In text, a table row and a line in
    a fenced code block are each a sentence of their own: the returned set holds the source lines that begin
    a sentence."""

    paragraphs: list[tuple[str, list[int], set[int]]] = []
    text, owners, last, fenced, starts = "", [], None, False, set()

    def flush() -> None:
        nonlocal text, owners, starts
        if text:
            comments = [(match.group(1), owners[match.start(1):match.end(1)]) for match in HTML_COMMENT.finditer(text)]
            text, owners = _rewrite(HTML_COMMENT, " ", text, owners)
            for part, part_owners in [(text, owners)] + comments:
                if not part.strip():
                    continue
                part, part_owners = _unlinked(part, part_owners)
                for pattern, replacement in VISIBLE_TEXT:
                    part, part_owners = _rewrite(pattern, replacement, part, part_owners)
                paragraphs.append((part, part_owners, starts))
        text, owners, starts = "", [], set()

    previous_hard = False
    for number in sorted(lines):
        line = lines[number]
        glue = line.startswith(GLUE)
        line = line[len(GLUE):] if glue else line
        raw = line.strip()
        fence = blank_breaks and raw.startswith(("```", "~~~"))
        hard = blank_breaks and (fenced or fence or raw.startswith("|"))
        if fence:
            fenced = not fenced
        piece = _normal(MARKDOWN_QUOTE.sub("", line))
        if last is not None and number != last + 1 or not piece and blank_breaks:
            flush()
            previous_hard = False
        last = number
        if not piece:
            continue
        if hard or previous_hard:
            starts.add(number)
        previous_hard = hard
        if text and not (glue and not line[:1].isspace()):
            text, owners = text + " ", owners + [number]
        text, owners = text + piece, owners + [number] * len(piece)
    flush()
    return paragraphs


def _span(owners: list[int], start: int, end: int) -> list[int]:
    return list(range(owners[start], owners[max(start, end - 1)] + 1))


def _sentences(text: str, owners: list[int], starts: set[int]) -> list[int]:
    """The sentence number of every character; a sentence ends at a full stop, question or exclamation
    mark, and before every line in `starts`."""

    ends = set()
    for match in SENTENCE_END.finditer(text):
        word = LAST_WORD.search(text, 0, match.start())
        if match.group() == "." and word and word.group().lower().rstrip(".") in ABBREVIATIONS:
            continue
        ends.add(match.end())
    numbers, current = [], 0
    for index in range(len(text)):
        if index in ends or index and owners[index] != owners[index - 1] and owners[index] in starts:
            current += 1
        numbers.append(current)
    return numbers


def _token_findings(label: str, lines: dict[int, str], tokens: list[tuple[int, str]], added: set[int] | None,
                    kind: str, blank_breaks: bool = True) -> list[str]:
    findings: list[str] = []
    for text, owners, _ in _paragraphs(lines, blank_breaks):
        for index, term in tokens:
            for match in _phrase(term).finditer(text):
                span = _span(owners, match.start(), match.end())
                if added is None or added.intersection(span):
                    findings.append(f"{label}:{span[0]}: {kind} #{index}")
    return findings


def scan(label: str, lines: dict[int, str], terms: dict[str, list[str]], added: set[int] | None = None,
         blank_breaks: bool = True) -> list[str]:
    """Findings in `lines` (the whole prose); with `added`, only matches that involve an added line. A name
    and an observation marker match when they share a sentence or lie within one line of each other."""

    findings = _token_findings(label, lines, list(enumerate(terms["tokens"], 1)), added, "observed token", blank_breaks)
    names = [(index, _word(term)) for index, term in enumerate(terms["names"], 1)]
    markers = [(index, _word(term)) for index, term in enumerate(terms["markers"], 1)]
    for text, owners, starts in _paragraphs(lines, blank_breaks):
        text = _unpathed(text)
        sentences = _sentences(text, owners, starts)
        marker_hits = [(index, _span(owners, match.start(), match.end()), sentences[match.start()])
                       for index, pattern in markers for match in pattern.finditer(text)]
        for name_index, pattern in names:
            for match in pattern.finditer(text):
                name_span = _span(owners, match.start(), match.end())
                sentence = sentences[match.start()]
                low, high = name_span[0] - 1, name_span[-1] + 1
                for marker_index, marker_span, marker_sentence in marker_hits:
                    near = not (marker_span[-1] < low or marker_span[0] > high)
                    if not (near or marker_sentence == sentence):
                        continue
                    if added is None or added.intersection(name_span + marker_span):
                        finding = f"{label}:{name_span[0]}: name #{name_index} near observation marker #{marker_index}"
                        if finding not in findings:
                            findings.append(finding)
    return findings


def _git(repo: Path, *args: str) -> str:
    return subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True, check=True).stdout


def added_line_numbers(repo: Path, base: str, head: str) -> dict[str, set[int]]:
    # Paths come NUL-separated and are passed back literally, so quoted or non-ASCII names are never misparsed.
    paths = [path for path in _git(repo, "diff", "-z", "--name-only", "--no-renames", "--diff-filter=d",
                                   f"{base}...{head}").split("\0") if path]
    added: dict[str, set[int]] = {}
    for path in paths:
        diff = _git(repo, "--literal-pathspecs", "diff", "--unified=0", "--no-color", "--no-renames",
                    f"{base}...{head}", "--", path)
        for line in diff.splitlines():
            match = re.match(r"@@ -\S+ \+(\d+)(?:,(\d+))? @@", line)
            if match:
                start, count = int(match.group(1)), int(match.group(2) or "1")
                added.setdefault(path, set()).update(range(start, start + count))
    return {path: numbers for path, numbers in added.items() if numbers}


def scan_named_tokens(label: str, lines: dict[int, str], terms: dict[str, list[str]],
                      added: set[int] | None = None) -> list[str]:
    """Observed tokens that carry a product name, on every line: test data and fixtures may hold observed
    layouts, never the product's own label."""

    names = [_word(term) for term in terms["names"]]
    named = [(index, term) for index, term in enumerate(terms["tokens"], 1)
             if any(pattern.search(_normal(term)) for pattern in names)]
    return _token_findings(label, lines, named, added, "named observed token")


def _data_path(path: str) -> bool:
    parts = Path(path).parts
    return "tests" in parts or "fixtures" in parts


def check_range(repo: Path, base: str, head: str, terms: dict[str, list[str]],
                messages_base: str | None = None) -> list[str]:
    findings: list[str] = []
    for path, numbers in sorted(added_line_numbers(repo, base, head).items()):
        text = _git(repo, "show", f"{head}:{path}")
        # A fixture data file (CSV) is consumed by code like code itself; only the named-token rule applies.
        if not (_data_path(path) and Path(path).suffix.lower() == ".csv"):
            findings += scan(path, prose_of(path, text), terms, numbers, Path(path).suffix.lower() not in CODE_SUFFIXES)
        if _data_path(path):
            findings += scan_named_tokens(path, dict(enumerate(text.splitlines(), 1)), terms, numbers)
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
            findings += scan(str(path), prose_of(str(path), path.read_text(encoding="utf-8")), terms,
                             blank_breaks=path.suffix.lower() not in CODE_SUFFIXES)
    except (OSError, ValueError, UnicodeDecodeError, subprocess.CalledProcessError):
        print("check_public_observations: operational error (terms file, refs or files unreadable)", file=sys.stderr)
        return 2
    for finding in findings:
        print(finding)
    print(f"check_public_observations: {len(findings)} finding(s)")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
