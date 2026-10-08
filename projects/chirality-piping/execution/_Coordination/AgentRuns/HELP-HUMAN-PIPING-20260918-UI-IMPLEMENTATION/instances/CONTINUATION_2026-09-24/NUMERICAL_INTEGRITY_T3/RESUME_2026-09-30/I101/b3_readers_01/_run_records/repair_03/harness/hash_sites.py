"""I101 repair 03: candidate sites where an RE source iterates a hashed collection. Finds bindings whose value is a
HashMap/HashSet (constructor, collect turbofish or annotation, or a call to a helper returning one), function parameters
typed HashMap/HashSet, and every later line that iterates such a name (for-in, .iter/.keys/.values/.into_iter/.drain,
.iter().any/all etc.). A candidate list for review, not a verdict. Usage: hash_sites.py <src dir>"""
import os, re, sys
src = sys.argv[1]
HASH = r"(?:std::collections::)?Hash(?:Map|Set)"
for f in sorted(os.listdir(src)):
    if not f.endswith(".rs"): continue
    lines = open(os.path.join(src, f)).read().split("\n")
    helpers = set()
    for i, l in enumerate(lines):
        m = re.match(r"\s*(?:pub(?:\(crate\))?\s+)?fn\s+(\w+)[^{]*->[^{]*" + HASH, l)
        if m: helpers.add(m.group(1))
    names = {}
    for i, l in enumerate(lines):
        for m in re.finditer(r"let\s+(?:mut\s+)?(\w+)\s*(?::\s*[^=]*" + HASH + r"[^=]*)?=\s*(.*)", l):
            name, rhs = m.group(1), m.group(2)
            ann = re.search(r":\s*[^=]*" + HASH, l[m.start():m.start() + len(m.group(0)) - len(rhs)])
            window = " ".join(lines[i:i + 8])
            if ann or re.match(HASH + r"::new", rhs) or (re.search(r"collect::<(?:Result<)?" + HASH, window) and ";" not in rhs.split("collect")[0][-200:] and "collect" in window.split(";")[0]) \
               or any(re.match(r"\s*&?" + h + r"\(", rhs) for h in helpers):
                names.setdefault(name, []).append(i + 1)
        for m in re.finditer(r"(\w+)\s*:\s*&?(?:mut\s+)?" + HASH, l):
            if "fn " in l or l.strip().startswith(m.group(1)):
                names.setdefault(m.group(1), []).append(i + 1)
    for name, defs in sorted(names.items()):
        pat = re.compile(r"(?:for\s+[^;{]*\bin\s+&?(?:mut\s+)?" + name + r"\b(?!\s*\[)(?!\.\w*get)|\b" + name + r"\s*\.\s*(?:iter|keys|values|into_iter|drain|into_keys|into_values)\s*\()")
        hits = [i + 1 for i, l in enumerate(lines) if pat.search(l)]
        if hits:
            print(f"{f}: {name} (defined {defs}) iterated at {hits}")
    print(f"{f}: helpers returning hashed: {sorted(helpers)}")
