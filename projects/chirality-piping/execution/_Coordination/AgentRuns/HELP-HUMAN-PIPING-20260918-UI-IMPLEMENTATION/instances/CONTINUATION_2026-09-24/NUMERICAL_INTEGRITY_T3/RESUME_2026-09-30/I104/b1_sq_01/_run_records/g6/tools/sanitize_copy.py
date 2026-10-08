"""I104: copy a file into the records with placeholder paths (R, NUM, WT, TMP), so no record names a home
or temporary-directory path. In this recorded copy the literal prefixes it replaces read as their placeholders. Usage: sanitize_copy.py <src> <dst>"""
import sys, os, re
src, dst = sys.argv[1:3]
t = open(src, encoding="utf-8", errors="replace").read()
R0 = "R"
for a, b in [(R0, "R"), ("NUM", "NUM"), ("WT", "WT"),
             (re.compile(r"TMP"']*"), "TMP"), (re.compile(r"TMP"']*"), "TMP"), ("HOME", "HOME")]:
    t = a.sub(b, t) if hasattr(a, "sub") else t.replace(a, b)
os.makedirs(os.path.dirname(dst), exist_ok=True)
open(dst, "w", encoding="utf-8").write(t)
