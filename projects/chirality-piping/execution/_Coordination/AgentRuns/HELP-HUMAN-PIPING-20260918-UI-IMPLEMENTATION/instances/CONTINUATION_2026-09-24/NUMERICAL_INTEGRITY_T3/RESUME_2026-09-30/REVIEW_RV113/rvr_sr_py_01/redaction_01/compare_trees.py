"""RV113: compare two record trees file by file: plain files byte for byte, .gz files by their decompressed bytes
(the gzip header's mtime is the time of writing). Usage: compare_trees.py <a> <b> [<ignored relative path> ...]"""
import gzip, os, sys
a, b, ignore = sys.argv[1], sys.argv[2], set(sys.argv[3:])
def files(root):
    return sorted(os.path.relpath(os.path.join(d, f), root) for d, _, fs in os.walk(root) for f in fs)
fa, fb = files(a), files(b)
same = differ = 0; out = []
if fa != fb: out.append(("file lists differ", sorted(set(fa) ^ set(fb))))
for p in sorted(set(fa) & set(fb)):
    x, y = open(os.path.join(a, p), "rb").read(), open(os.path.join(b, p), "rb").read()
    if p.endswith(".gz"): x, y = gzip.decompress(x), gzip.decompress(y)
    if x == y: same += 1
    elif p in ignore: out.append(("differs (expected)", p))
    else: differ += 1; out.append(("DIFFERS", p))
print(f"files {len(set(fa) & set(fb))}, identical {same}, unexpected differences {differ}")
for o in out: print(" ", o)
sys.exit(1 if differ or fa != fb else 0)
