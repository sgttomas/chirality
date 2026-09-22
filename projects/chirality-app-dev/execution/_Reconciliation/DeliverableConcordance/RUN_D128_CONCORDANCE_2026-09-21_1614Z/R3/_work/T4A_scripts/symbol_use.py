"""T4A (a): symbol-level consumers of barrel-re-exported contracts modules at the frozen basis.
Usage: python3 symbol_use.py <frozen_tree>. Prints, per module, exported symbols and every
non-test, non-contracts file that mentions each symbol as a word."""
import os, re, sys
F = sys.argv[1]
MODS = ["domain-profile", "operation-proposal", "engine-conformance", "tool-catalog",
        "tool-descriptor", "mcp/tool-names", "sdk-version"]
base = os.path.join(F, "projects/chirality-runtime/packages/contracts/src/harness")
roots = ["projects/chirality-app-dev/frontend/src", "projects/chirality-app-dev/frontend/electron",
         "projects/chirality-app-dev/frontend/scripts",
         "projects/chirality-runtime/packages"]
files = []
for r in roots:
    for d, ds, fs in os.walk(os.path.join(F, r)):
        ds[:] = [x for x in ds if x not in ("node_modules", "dist", "__tests__", ".next")]
        for f in fs:
            if re.search(r"\.(ts|tsx|mjs|js)$", f) and not re.search(r"\.test\.", f):
                p = os.path.relpath(os.path.join(d, f), F)
                if "packages/contracts/src" in p or "frontend/packages/harness-contract" in p:
                    continue
                files.append(p)
text = {p: open(os.path.join(F, p), encoding="utf-8", errors="replace").read() for p in files}
for m in MODS:
    src = open(os.path.join(base, m + ".ts"), encoding="utf-8").read()
    syms = sorted(set(re.findall(r"export\s+(?:declare\s+)?(?:const|function|class|type|interface|enum)\s+([A-Za-z0-9_]+)", src)))
    print(f"## {m}: {len(syms)} exported symbols")
    hit = False
    for s in syms:
        users = [p for p, t in text.items() if re.search(r"\b" + re.escape(s) + r"\b", t)]
        if users:
            hit = True
            print(f"  {s}: " + "; ".join(sorted(users)))
    if not hit:
        print("  (no non-test consumer outside contracts and the App facade)")
