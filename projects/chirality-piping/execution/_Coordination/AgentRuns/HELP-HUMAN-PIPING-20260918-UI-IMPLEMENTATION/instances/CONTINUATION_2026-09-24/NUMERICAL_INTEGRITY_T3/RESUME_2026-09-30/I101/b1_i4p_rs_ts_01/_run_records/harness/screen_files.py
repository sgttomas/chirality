"""I101: screen record files (not a git range) with WT/tools/t3_host_screen.py's own patterns: the strict path
forms, the junit host attribute, and every name this machine answers to (read at run time, never printed).
The tool's pattern block (everything before `def git(`) is executed unchanged; .gz files are decompressed.
Also refuses symlinks and any folder named `build`. Usage: screen_files.py <tool> <records dir>
"""
import gzip
import os
import sys

tool, root = sys.argv[1], sys.argv[2]
src = open(tool).read()
ns = {"__file__": os.path.abspath(tool)}
exec(compile(src[: src.index("def git(")], tool, "exec"), ns)
cre, names = ns["cre"], ns["names"]
hits = files = 0
for d, dirs, fs in os.walk(root):
    for x in dirs:
        if x == "build" or os.path.islink(os.path.join(d, x)):
            print("HIT folder", os.path.relpath(os.path.join(d, x), root)); hits += 1
    for f in fs:
        p = os.path.join(d, f)
        if os.path.islink(p):
            print("HIT symlink", os.path.relpath(p, root)); hits += 1; continue
        raw = open(p, "rb").read()
        if f.endswith(".gz"):
            raw = gzip.decompress(raw)
        files += 1
        for ln, text in enumerate(raw.splitlines(), 1):
            for label, c in cre.items():
                if c.search(text):
                    shown = text
                    for c2 in cre.values():
                        shown = c2.sub(b"<host>", shown)
                    print(f"HIT {os.path.relpath(p, root)}:{ln} [{label}] {shown.decode('utf-8', 'replace')[:160]}")
                    hits += 1
                    break
print(f"files {files}, hits {hits}, names screened {len(names)}")
sys.exit(1 if hits else 0)
