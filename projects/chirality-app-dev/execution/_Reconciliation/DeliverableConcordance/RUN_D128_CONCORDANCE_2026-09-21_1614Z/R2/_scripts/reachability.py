#!/usr/bin/env python3
"""Evidence pack item 2: REACHABILITY.csv (CONVENTIONS §9, with the R1b brief corrections).

Usage: reachability.py --frozen <frozen-tree> --harness-caps <HARNESS_capabilities.csv> --out <REACHABILITY.csv>

Static import graph over the frozen tree (read-only file reads; no git):
- Nodes: .ts .tsx .js .jsx .mjs .cjs under frontend/{src,electron,packages,scripts} and
  projects/chirality-runtime/{packages/*/src,packages/*/test,tests}.
- Edges: `import ... from 'x'`, `export ... from 'x'`, side-effect `import 'x'`, and string-literal
  `import('x')` / `require('x')`. Type-only imports/exports (`import type`, `export type`, or a
  brace list whose every specifier is `type X`) are NOT runtime edges and are ignored.
- Resolution: relative specifiers (with .js->.ts mapping, extension probing, index files);
  `@chirality/runtime-*` and `@chirality/engine-*` via each package.json `exports`/`main`,
  mapped dist->src (the same mapping as frontend/scripts/build-electron.mjs runtimePackagePlugin);
  `@chirality/harness-contract[/sub]` via its package.json `exports` (source paths).
Reach, in precedence order:
- LIVE: reached from a product entry point: Next.js special files under frontend/src/app/**
  (page, layout, route, not-found, loading, error, template, default, global-error),
  frontend/electron/main.ts, frontend/electron/preload.ts (built as its own bundle by
  build-electron.mjs), and the Runtime bundles the App packages (build-electron.mjs):
  packages/daemon/src/standalone-bin.ts (runtime-service) and packages/cli/src/bin.ts (runtime-cli).
- LEGACY_ONLY: not LIVE; reached from a seed = a Paths entry of a HARNESS R0 capability row whose
  Notes carry `LEGACY-IN-PROCESS:` (re-verified: a seed reached from LIVE code is LIVE).
- TEST_ONLY: not LIVE/LEGACY; reached from a test file (frontend/src/__tests__/**, *.test.*,
  *.spec.*, runtime tests/**, packages/*/test/**).
- UNREACHED: none of the above (e.g. only reached from frontend/scripts/**, or from nothing).
Rows: one per non-test module under frontend/src/**, frontend/electron/**,
projects/chirality-runtime/packages/*/src/**. Test files themselves get no row.
ImportChain: shortest chain (multi-source BFS, sorted, deterministic) `entry>...>path`;
entry and path included; for UNREACHED it is `NONE`.
"""
import argparse
import csv
import io
import json
import os
import re
import sys
from collections import deque

APP = "projects/chirality-app-dev/frontend"
RT = "projects/chirality-runtime"
EXTS = (".ts", ".tsx", ".js", ".jsx", ".mjs", ".cjs")
SKIP_DIRS = {"node_modules", "dist", "dist-electron", "dist-runtime", ".next", "out"}
BASIS = "REACHABILITY(static)@00115c719"
NEXT_SPECIAL = {"page", "layout", "route", "not-found", "loading", "error", "template", "default", "global-error"}

STATIC_RE = re.compile(
    r"""(?ms)^[ \t]*(import|export)\s+(type\s+)?([^;'"`]*?)\s*from\s*['"]([^'"]+)['"]""")
SIDE_RE = re.compile(r"""(?m)^[ \t]*import\s*['"]([^'"]+)['"]""")
DYN_RE = re.compile(r"""(?<![\w.$])(import|require)\(\s*['"]([^'"]+)['"]\s*\)""")


def walk(root, rel):
    out = []
    base = os.path.join(root, rel)
    if not os.path.isdir(base):
        return out
    for d, dirs, files in os.walk(base):
        dirs[:] = sorted(x for x in dirs if x not in SKIP_DIRS)
        for f in sorted(files):
            if f.endswith(EXTS) and not f.endswith(".d.ts"):
                out.append(os.path.relpath(os.path.join(d, f), root).replace(os.sep, "/"))
    return out


def is_test(p):
    b = os.path.basename(p)
    return ("/__tests__/" in p or re.search(r"\.(test|spec)\.[cm]?[jt]sx?$", b) is not None
            or p.startswith(RT + "/tests/") or re.match(rf"^{RT}/packages/[^/]+/test/", p) is not None)


def type_only(kw, typ, clause):
    if typ:
        return True
    c = clause.strip()
    m = re.fullmatch(r"\{(.*)\}", c, re.S)
    if m:
        specs = [s.strip() for s in m.group(1).split(",") if s.strip()]
        return bool(specs) and all(s.startswith("type ") for s in specs)
    return False


def specifiers(text):
    out = []
    for m in STATIC_RE.finditer(text):
        kw, typ, clause, spec = m.groups()
        if not type_only(kw, typ, clause):
            out.append(spec)
    out += SIDE_RE.findall(text)
    for line in text.splitlines():
        s = line.lstrip()
        if s.startswith("//") or s.startswith("*") or s.startswith("/*"):
            continue
        for m in DYN_RE.finditer(line):
            out.append(m.group(2))
    return out


class Resolver:
    def __init__(self, root, files):
        self.root = root
        self.files = set(files)
        self.pkgs = {}
        for pdir in sorted(os.listdir(os.path.join(root, RT, "packages"))):
            pj = os.path.join(root, RT, "packages", pdir, "package.json")
            if os.path.exists(pj):
                d = json.load(open(pj))
                self.pkgs[d["name"]] = (f"{RT}/packages/{pdir}", d, True)
        hj = os.path.join(root, APP, "packages", "harness-contract", "package.json")
        if os.path.exists(hj):
            d = json.load(open(hj))
            self.pkgs[d["name"]] = (f"{APP}/packages/harness-contract", d, False)

    def probe(self, p):
        p = os.path.normpath(p).replace(os.sep, "/")
        cands = [p]
        stem, ext = os.path.splitext(p)
        if ext in (".js", ".jsx", ".mjs", ".cjs"):
            cands += [stem + ".ts", stem + ".tsx", stem + ".mts", stem + ".cts"]
        cands += [p + e for e in EXTS] + [p + "/index" + e for e in EXTS]
        for c in cands:
            if c in self.files:
                return c
        return None

    def dist_to_src(self, pdir, target, is_rt):
        t = target[2:] if target.startswith("./") else target
        if is_rt:
            if t.startswith("dist/"):
                t = t[5:]
            if t.startswith("src/"):
                t = t[4:]
            t = "src/" + t
        return self.probe(f"{pdir}/{t}")

    def resolve(self, frm, spec):
        if spec.startswith("."):
            return self.probe(os.path.join(os.path.dirname(frm), spec))
        m = re.match(r"^(@chirality/[^/]+)(?:/(.+))?$", spec)
        if not m or m.group(1) not in self.pkgs:
            return None
        name, sub = m.group(1), m.group(2)
        pdir, d, is_rt = self.pkgs[name]
        key = "." if not sub else "./" + sub
        exp = d.get("exports")
        target = None
        if isinstance(exp, dict) and key in exp:
            v = exp[key]
            if isinstance(v, dict):
                target = v.get("import") or v.get("default") or v.get("types")
            else:
                target = v
        elif key == "." and d.get("main"):
            target = d["main"]
        if target is None:
            return None
        return self.dist_to_src(pdir, target, is_rt)


def bfs(sources, graph):
    prev = {}
    q = deque()
    for s in sorted(sources):
        if s not in prev:
            prev[s] = None
            q.append(s)
    while q:
        u = q.popleft()
        for v in sorted(graph.get(u, ())):
            if v not in prev:
                prev[v] = u
                q.append(v)
    return prev


def chain(prev, n):
    out = []
    while n is not None:
        out.append(n)
        n = prev[n]
    return list(reversed(out))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--frozen", required=True)
    ap.add_argument("--harness-caps", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    root = a.frozen
    files = []
    for rel in (f"{APP}/src", f"{APP}/electron", f"{APP}/packages", f"{APP}/scripts"):
        files += walk(root, rel)
    for pdir in sorted(os.listdir(os.path.join(root, RT, "packages"))):
        files += walk(root, f"{RT}/packages/{pdir}/src")
        files += walk(root, f"{RT}/packages/{pdir}/test")
    files += walk(root, f"{RT}/tests")
    files = sorted(set(files))
    res = Resolver(root, files)
    graph = {}
    for f in files:
        text = open(os.path.join(root, f), encoding="utf-8", errors="replace").read()
        tg = set()
        for s in specifiers(text):
            r = res.resolve(f, s)
            if r and r != f:
                tg.add(r)
        graph[f] = tg

    entries = [f for f in files if f.startswith(f"{APP}/src/app/") and not is_test(f)
               and os.path.splitext(os.path.basename(f))[0] in NEXT_SPECIAL]
    entries += [f for f in (f"{APP}/electron/main.ts", f"{APP}/electron/preload.ts",
                            f"{RT}/packages/daemon/src/standalone-bin.ts", f"{RT}/packages/cli/src/bin.ts")
                if f in res.files]
    seeds = set()
    with open(a.harness_caps, encoding="utf-8", newline="") as fh:
        for r in csv.DictReader(fh):
            if (r.get("Notes") or "").find("LEGACY-IN-PROCESS:") >= 0:
                for p in (r.get("Paths") or "").split(";"):
                    p = p.strip()
                    if p in res.files:
                        seeds.add(p)
    tests = [f for f in files if is_test(f)]

    live = bfs(entries, graph)
    legacy = bfs(seeds, graph)
    test = bfs(tests, graph)

    def in_scope(f):
        return (f.startswith(f"{APP}/src/") or f.startswith(f"{APP}/electron/")
                or re.match(rf"^{RT}/packages/[^/]+/src/", f) is not None) and not is_test(f)

    rows = []
    for f in files:
        if not in_scope(f):
            continue
        if f in live:
            c = chain(live, f); reach = "LIVE"
        elif f in legacy:
            c = chain(legacy, f); reach = "LEGACY_ONLY"
        elif f in test:
            c = chain(test, f); reach = "TEST_ONLY"
        else:
            c = None; reach = "UNREACHED"
        rows.append([f, reach, c[0] if c else "NONE", ">".join(c) if c else "NONE", BASIS])
    rows.sort(key=lambda r: r[0])
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(["Path", "Reach", "EntryPoint", "ImportChain", "Basis"])
    w.writerows(rows)
    buf.write("#END\n")
    open(a.out, "w", encoding="utf-8", newline="").write(buf.getvalue())
    from collections import Counter
    print(f"entries={len(entries)} seeds={len(seeds)} tests={len(tests)} nodes={len(files)} rows={len(rows)}",
          dict(Counter(r[1] for r in rows)), file=sys.stderr)


if __name__ == "__main__":
    main()
