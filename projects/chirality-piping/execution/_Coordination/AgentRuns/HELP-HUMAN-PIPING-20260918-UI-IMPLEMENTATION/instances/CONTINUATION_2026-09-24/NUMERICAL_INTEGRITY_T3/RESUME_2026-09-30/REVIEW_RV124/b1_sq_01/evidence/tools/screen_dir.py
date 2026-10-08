"""RV124: apply t3_host_screen.py's patterns (strict path forms, junit host attribute, this machine's names) to
every file under a directory (.gz decompressed). Prints hits with the match replaced. Exit 1 on any hit."""
import gzip, os, re, sys
src = open("WT/tools/t3_host_screen.py").read()
src = src[: src.index("def git(")]          # the pattern-building part only
ns = {"__file__": "WT/tools/t3_host_screen.py"}
exec(compile(src, "t3_host_screen_patterns", "exec"), ns)
cre = ns["cre"]
hits = files = 0
for d, _, fs in os.walk(sys.argv[1]):
    for f in fs:
        p = os.path.join(d, f)
        if os.path.islink(p):
            print("SYMLINK", p); hits += 1; continue
        raw = open(p, "rb").read()
        if p.endswith(".gz"):
            raw = gzip.decompress(raw)
        files += 1
        for ln, text in enumerate(raw.splitlines(), 1):
            for label, c in cre.items():
                if c.search(text):
                    shown = text
                    for c2 in cre.values():
                        shown = c2.sub(b"<host>", shown)
                    print(f"HIT {os.path.relpath(p, sys.argv[1])}:{ln} [{label}] {shown.decode('utf-8','replace')[:160]}")
                    hits += 1
                    break
    if os.path.basename(d) == "build":
        print("FOLDER NAMED build:", d); hits += 1
print(f"files {files}, hits {hits}, names screened {len(ns['names'])}")
sys.exit(1 if hits else 0)
