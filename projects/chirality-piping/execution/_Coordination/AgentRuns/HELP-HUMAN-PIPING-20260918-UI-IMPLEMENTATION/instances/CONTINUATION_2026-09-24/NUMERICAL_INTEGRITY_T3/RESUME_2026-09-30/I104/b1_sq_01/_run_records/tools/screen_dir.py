"""I104: WT/tools/t3_host_screen.py's patterns (read from the tool, names read at run time and never printed), applied
to every file under a directory (.gz decompressed), for records ROOT has not yet staged. Usage: screen_dir.py <tool> <dir>"""
import gzip, os, sys
tool, root = sys.argv[1:3]
src = open(tool).read().rsplit("\nmain()", 1)[0]
g = {"__file__": tool, "__name__": "screen"}
exec(compile(src, tool, "exec"), g)
cre = g["cre"]; hits = files = 0
for d, _, fs in os.walk(root):
    for f in fs:
        p = os.path.join(d, f); raw = open(p, "rb").read()
        if f.endswith(".gz"): raw = gzip.decompress(raw)
        files += 1
        for ln, text in enumerate(raw.splitlines(), 1):
            for label, c in cre.items():
                if c.search(text):
                    print(f"HIT {os.path.relpath(p, root)}:{ln} [{label}]"); hits += 1; break
print(f"files {files}, hits {hits}, names screened {len(g['names'])}")
sys.exit(1 if hits else 0)
