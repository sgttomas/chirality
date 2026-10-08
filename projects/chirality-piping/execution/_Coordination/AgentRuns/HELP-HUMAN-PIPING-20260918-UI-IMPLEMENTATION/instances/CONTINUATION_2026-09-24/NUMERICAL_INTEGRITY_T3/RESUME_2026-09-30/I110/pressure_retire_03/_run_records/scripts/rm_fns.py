"""Remove named Rust functions (with their attributes and doc/line comments directly above) from a file.
Usage: rm_fns.py <file> name [name ...]. Brace matching skips strings, raw strings, chars and comments."""
import re, sys
path, names = sys.argv[1], sys.argv[2:]
src = open(path).read()

def body_end(s, i):
    # i: index of the opening '{'
    depth = 0; n = len(s)
    while i < n:
        c = s[i]
        if s.startswith('//', i):
            i = s.index('\n', i); continue
        if s.startswith('/*', i):
            i = s.index('*/', i) + 2; continue
        m = re.match(r'r(#*)"', s[i:]) if c == 'r' and (i == 0 or not (s[i-1].isalnum() or s[i-1] == '_')) else None
        if m:
            close = '"' + m.group(1); j = s.index(close, i + len(m.group(0))); i = j + len(close); continue
        if c == '"':
            j = i + 1
            while s[j] != '"':
                j += 2 if s[j] == '\\' else 1
            i = j + 1; continue
        if c == "'":
            m = re.match(r"'(\\.|[^\\'])'", s[i:]) or re.match(r"'\\u\{[0-9a-fA-F]+\}'", s[i:])
            if m: i += len(m.group(0)); continue
        if c == '{': depth += 1
        elif c == '}':
            depth -= 1
            if depth == 0: return i + 1
        i += 1
    raise SystemExit('unbalanced')

for name in names:
    m = list(re.finditer(r'^[ \t]*(pub(\([^)]*\))?\s+)?(fn|struct|enum) ' + re.escape(name) + r'\b', src, re.M))
    assert len(m) == 1, (name, len(m))
    start = m[0].start()
    # walk back over attributes and comments
    lines_before = src[:start].split('\n')
    k = len(lines_before) - 1  # last element is the partial line before fn (indent)
    j = k - 1
    while j >= 0 and re.match(r'\s*(#\[|///|//)', lines_before[j]):
        j -= 1
    start = len('\n'.join(lines_before[:j + 1])) + (1 if j >= 0 else 0)
    brace = src.index('{', m[0].end())
    end = body_end(src, brace)
    if src[end:end+1] == '\n': end += 1
    # drop one blank line left behind
    if src[end:end+1] == '\n' and (start == 0 or src[start-2:start] == '\n\n'): end += 1
    src = src[:start] + src[end:]
    print('removed', name)
open(path, 'w').write(src)
