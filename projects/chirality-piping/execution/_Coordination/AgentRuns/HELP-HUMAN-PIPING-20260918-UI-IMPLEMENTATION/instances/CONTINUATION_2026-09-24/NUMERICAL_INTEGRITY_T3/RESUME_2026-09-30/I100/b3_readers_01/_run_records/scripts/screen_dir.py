"""I100: screen a records folder with the T3 host screen's own patterns (WT/tools/t3_host_screen.py: the strict
path forms, the junit hostname attribute, the model form and every name this machine answers to, read at run time
and never printed). Every file is read whole, .gz files decompressed. Also refuses symlinks and folders named
build. Usage: screen_dir.py <dir>"""
import gzip
import os
import sys

tool = "WT/tools/t3_host_screen.py"
src = open(tool).read()
src = src[: src.rindex("\nmain()")]
g = {"__name__": "t3_host_screen_lib", "__file__": tool}
exec(compile(src, tool, "exec"), g)
cre, names = g["cre"], g["names"]
root = sys.argv[1]
files = hits = bad = 0
for dirpath, dirnames, filenames in os.walk(root):
    for d in dirnames:
        if d == "build" or os.path.islink(os.path.join(dirpath, d)):
            print("BAD folder", os.path.relpath(os.path.join(dirpath, d), root)); bad += 1
    for f in filenames:
        p = os.path.join(dirpath, f)
        if os.path.islink(p):
            print("BAD symlink", os.path.relpath(p, root)); bad += 1
            continue
        raw = open(p, "rb").read()
        if f.endswith(".gz"):
            raw = gzip.decompress(raw)
        files += 1
        for ln, text in enumerate(raw.splitlines(), 1):
            for label, c in cre.items():
                if c.search(text):
                    print(f"HIT {os.path.relpath(p, root)}:{ln} [{label}]"); hits += 1
                    break
print(f"files {files}, hits {hits}, bad {bad}, names screened {len(names)}")
sys.exit(1 if hits or bad else 0)
