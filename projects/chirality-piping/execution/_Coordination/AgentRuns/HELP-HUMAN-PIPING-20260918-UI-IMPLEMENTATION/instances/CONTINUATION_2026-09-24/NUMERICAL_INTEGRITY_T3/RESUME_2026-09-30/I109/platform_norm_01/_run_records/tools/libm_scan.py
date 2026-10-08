#!/usr/bin/env python3
"""I109 libm inventory scanner (scratch tool).

Lexes Rust, Python and TypeScript sources (comments and string literals removed,
line numbers kept), and lists every call of a function whose result is not
correctly rounded by IEEE 754: Rust `.name(` / `f64::name(` / `name(` for the
Rust list, Python `math.name(` / `**`, TypeScript `Math.name(` / `**`.
Each hit is tagged prod or test (tests/ trees, *_tests.rs / tests.rs files,
modules declared under #[cfg(test)], and #[cfg(test)] mod blocks).
Usage: libm_scan.py <P root> <out.tsv>
"""
import os
import re
import sys

RUST_FUNCS = [
    "hypot", "sin", "cos", "tan", "atan2", "asin", "acos", "atan", "exp", "exp2", "exp_m1",
    "ln", "ln_1p", "log", "log10", "log2", "powf", "powi", "cbrt", "to_radians", "to_degrees",
    "sinh", "cosh", "tanh", "asinh", "acosh", "atanh", "sin_cos",
]
PY_FUNCS = ["hypot", "sin", "cos", "tan", "atan2", "asin", "acos", "atan", "exp", "expm1", "log",
            "log1p", "log10", "log2", "pow", "cbrt", "dist", "radians", "degrees", "sinh", "cosh",
            "tanh", "fsum"]
TS_FUNCS = ["hypot", "sin", "cos", "tan", "atan2", "asin", "acos", "atan", "exp", "expm1", "log",
            "log1p", "log10", "log2", "pow", "cbrt", "sinh", "cosh", "tanh"]

SCOPE_RS = ["core/product_physics", "core/solver", "core/loads", "core/reporting/result_export"]
SCOPE_PY = ["core/analysis_runs"]
SCOPE_TS = ["apps/desktop/src/features/results"]


def blank(s):
    return "".join(c if c == "\n" else " " for c in s)


def lex_rust(src):
    out = []
    i, n = 0, len(src)
    while i < n:
        c = src[i]
        if src.startswith("//", i):
            j = src.find("\n", i)
            j = n if j < 0 else j
            out.append(blank(src[i:j])); i = j
        elif src.startswith("/*", i):
            depth, j = 1, i + 2
            while j < n and depth:
                if src.startswith("/*", j): depth += 1; j += 2
                elif src.startswith("*/", j): depth -= 1; j += 2
                else: j += 1
            out.append(blank(src[i:j])); i = j
        elif c == "r" and re.match(r'r#*"', src[i:i + 10]) and (i == 0 or not (src[i-1].isalnum() or src[i-1] == "_")):
            m = re.match(r'r(#*)"', src[i:])
            close = '"' + m.group(1)
            j = src.find(close, i + len(m.group(0)))
            j = n if j < 0 else j + len(close)
            out.append(blank(src[i:j])); i = j
        elif c == "b" and src.startswith('b"', i) and (i == 0 or not (src[i-1].isalnum() or src[i-1] == "_")):
            out.append(" "); i += 1
        elif c == '"':
            j = i + 1
            while j < n and src[j] != '"':
                j += 2 if src[j] == "\\" else 1
            out.append(blank(src[i:j + 1])); i = j + 1
        elif c == "'":
            m = re.match(r"'(\\.[^']*|[^\\'])'", src[i:])
            if m:
                out.append(blank(m.group(0))); i += len(m.group(0))
            else:
                out.append(c); i += 1
        else:
            out.append(c); i += 1
    return "".join(out)


def lex_py(src):
    out = []
    i, n = 0, len(src)
    while i < n:
        c = src[i]
        if c == "#":
            j = src.find("\n", i); j = n if j < 0 else j
            out.append(blank(src[i:j])); i = j
        elif src.startswith('"""', i) or src.startswith("'''", i):
            q = src[i:i + 3]; j = src.find(q, i + 3); j = n if j < 0 else j + 3
            out.append(blank(src[i:j])); i = j
        elif c in "\"'":
            j = i + 1
            while j < n and src[j] != c and src[j] != "\n":
                j += 2 if src[j] == "\\" else 1
            out.append(blank(src[i:j + 1])); i = j + 1
        else:
            out.append(c); i += 1
    return "".join(out)


def lex_ts(src):
    out = []
    i, n = 0, len(src)
    while i < n:
        c = src[i]
        if src.startswith("//", i):
            j = src.find("\n", i); j = n if j < 0 else j
            out.append(blank(src[i:j])); i = j
        elif src.startswith("/*", i):
            j = src.find("*/", i + 2); j = n if j < 0 else j + 2
            out.append(blank(src[i:j])); i = j
        elif c in "\"'`":
            j = i + 1
            while j < n and src[j] != c:
                j += 2 if src[j] == "\\" else 1
            out.append(blank(src[i:j + 1])); i = j + 1
        else:
            out.append(c); i += 1
    return "".join(out)


def test_spans_rust(code):
    spans = []
    for m in re.finditer(r"#\[cfg\(test\)\]\s*(pub(\([^)]*\))?\s+)?mod\s+\w+\s*\{", code):
        start = m.end() - 1
        depth, j = 0, start
        while j < len(code):
            if code[j] == "{": depth += 1
            elif code[j] == "}":
                depth -= 1
                if depth == 0: break
            j += 1
        spans.append((m.start(), j))
    return spans


def test_module_files(root):
    """Files declared as `#[cfg(test)] mod x;` (or under such a directory)."""
    files = set()
    for dirpath, _, names in os.walk(root):
        for name in names:
            if not name.endswith(".rs"): continue
            path = os.path.join(dirpath, name)
            code = lex_rust(open(path, encoding="utf-8").read())
            for m in re.finditer(r"#\[cfg\(test\)\]\s*(#\[path\s*=\s*[^\]]*\]\s*)?(pub(\([^)]*\))?\s+)?mod\s+(\w+)\s*;", code):
                mod = m.group(4)
                base = dirpath if name in ("lib.rs", "mod.rs", "main.rs") else os.path.join(dirpath, name[:-3])
                for cand in (os.path.join(base, mod + ".rs"), os.path.join(base, mod)):
                    files.add(os.path.normpath(cand))
    return files


def scan(root, out):
    rows = []
    test_files = set()
    for d in SCOPE_RS:
        test_files |= test_module_files(os.path.join(root, d))

    def is_test_path(path):
        p = os.path.normpath(path)
        if "/tests/" in p or p.endswith("_tests.rs") or p.endswith("/tests.rs") or p.endswith(".test.ts") or p.endswith(".test.tsx"):
            return True
        return any(p == t or p.startswith(t + os.sep) for t in test_files)

    def walk(dirs, exts):
        for d in dirs:
            for dirpath, dirnames, names in os.walk(os.path.join(root, d)):
                dirnames[:] = sorted(x for x in dirnames if x not in ("target", "node_modules", "__pycache__"))
                for name in sorted(names):
                    if any(name.endswith(e) for e in exts):
                        yield os.path.join(dirpath, name)

    rs_re = re.compile(r"(?:\.\s*|\bf64::|\bf32::)(" + "|".join(RUST_FUNCS) + r")\s*\(")
    for path in walk(SCOPE_RS, [".rs"]):
        src = open(path, encoding="utf-8").read()
        code = lex_rust(src)
        spans = test_spans_rust(code)
        ftest = is_test_path(path)
        lines = src.split("\n")
        for m in rs_re.finditer(code):
            pre = code[max(0, m.start() - 1):m.start() + 1]
            tok = m.group(0)
            # require method-call form `.f(` or path form `f64::f(`; plain `f(` only if a local fn named so
            if not (tok.startswith(".") or "::" in tok):
                # plain call: a free function named like a libm function
                pass
            line = code.count("\n", 0, m.start()) + 1
            test = ftest or any(a <= m.start() <= b for a, b in spans)
            rows.append((os.path.relpath(path, root), line, m.group(1), "test" if test else "prod", "rs", lines[line - 1].strip()))
    py_re = re.compile(r"\bmath\.(" + "|".join(PY_FUNCS) + r")\s*\(|(?<=[A-Za-z0-9_)\]])\s*\*\*(?!\s*[A-Za-z_]+\s*[,)])")
    for path in walk(SCOPE_PY, [".py"]):
        src = open(path, encoding="utf-8").read()
        code = lex_py(src)
        lines = src.split("\n")
        for m in py_re.finditer(code):
            line = code.count("\n", 0, m.start()) + 1
            fn = m.group(1) or "**"
            rows.append((os.path.relpath(path, root), line, fn, "prod", "py", lines[line - 1].strip()))
    ts_re = re.compile(r"\bMath\.(" + "|".join(TS_FUNCS) + r")\s*\(|(?<=[A-Za-z0-9_)\]])\s*\*\*")
    for path in walk(SCOPE_TS, [".ts", ".tsx"]):
        src = open(path, encoding="utf-8").read()
        code = lex_ts(src)
        lines = src.split("\n")
        ftest = is_test_path(path)
        for m in ts_re.finditer(code):
            line = code.count("\n", 0, m.start()) + 1
            fn = m.group(1) or "**"
            rows.append((os.path.relpath(path, root), line, fn, "test" if ftest else "prod", "ts", lines[line - 1].strip()))
    with open(out, "w", encoding="utf-8") as f:
        f.write("path\tline\tfunction\tcontext\tlang\tsource\n")
        for r in rows:
            f.write("\t".join(str(x) for x in r[:5]) + "\t" + r[5].replace("\t", " ")[:240] + "\n")
    return rows


if __name__ == "__main__":
    rows = scan(sys.argv[1], sys.argv[2])
    from collections import Counter
    c = Counter((r[3], r[4]) for r in rows)
    print("total", len(rows), dict(c))
    print(Counter((r[3], r[2]) for r in rows if r[3] == "prod"))
