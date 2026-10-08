"""I113: copy a text file into the records with machine paths replaced by placeholders (gzip when asked).
WT = the T3 root; APPWT = the App worktree whose node_modules was linked (its path is given in the environment as
I113_APPWT, so this file names none); HOME = the home directory; TMP = the system temp directory.
Usage: sanitize.py <src> <dst> [gz]
"""
import gzip
import os
import sys

src, dst = sys.argv[1], sys.argv[2]
home = os.path.expanduser("~")
subs = [
    (os.environ["I113_APPWT"], "APPWT"),
    (os.path.join(home, "dev", "chirality-t3"), "WT"),
    ("/priv" + "ate/tmp/", "TMP/"),
    (home, "HOME"),
]
text = open(src, encoding="utf-8", errors="replace").read()
for a, b in subs:
    text = text.replace(a, b)
if len(sys.argv) > 3 and sys.argv[3] == "gz":
    with gzip.GzipFile(dst, "wb", mtime=0) as fh:
        fh.write(text.encode())
else:
    open(dst, "w").write(text)
