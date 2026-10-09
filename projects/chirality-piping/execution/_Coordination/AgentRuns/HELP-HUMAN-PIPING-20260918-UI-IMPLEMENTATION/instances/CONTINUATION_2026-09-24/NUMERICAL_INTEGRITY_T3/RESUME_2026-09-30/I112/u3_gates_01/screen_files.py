#!/usr/bin/env python3
"""I112: run WT/tools/t3_host_screen.py's patterns over files on disk (the tool screens Git ranges or the staged index, and a
TASK makes no Git writes). The tool's pattern block (everything before its `def git`) is executed unchanged, so the same names
and forms are screened, and nothing prints them. Usage: screen_files.py <dir>"""
import gzip
import os
import sys

src = open('WT/tools/t3_host_screen.py').read()
ns = {'__file__': 'WT/tools/t3_host_screen.py'}
exec(compile(src[:src.index('\ndef git(')], 't3_host_screen.py', 'exec'), ns)
cre = ns['cre']
hits = files = 0
for dp, dn, fn in os.walk(sys.argv[1]):
    for f in sorted(fn):
        p = os.path.join(dp, f)
        raw = open(p, 'rb').read()
        if f.endswith('.gz'):
            raw = gzip.decompress(raw)
        files += 1
        for ln, text in enumerate(raw.splitlines(), 1):
            for label, c in cre.items():
                if c.search(text):
                    print('HIT %s:%d [%s]' % (os.path.relpath(p, sys.argv[1]), ln, label))
                    hits += 1
                    break
print('files %d, hits %d, names screened %d' % (files, hits, len(ns['names'])))
sys.exit(1 if hits else 0)
