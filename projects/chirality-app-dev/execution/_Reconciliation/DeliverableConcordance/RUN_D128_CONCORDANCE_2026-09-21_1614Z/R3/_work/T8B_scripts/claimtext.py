"""Print frozen-tree claim text for ClaimKeys (T8B helper; read-only)."""
import csv, glob, os, sys

RUN = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
FROZEN = os.environ["FROZEN"]
APP = os.path.join(FROZEN, "projects", "chirality-app-dev")

idx = {}
by_file = {}
with open(os.path.join(RUN, "R1_INVENTORY", "CLAIM_INDEX.csv"), encoding="utf-8") as f:
    for r in csv.DictReader(f):
        if r["ClaimKey"] == "#END" or not r.get("SourceLine"):
            continue
        idx[r["ClaimKey"]] = r
        by_file.setdefault((r["DeliverableID"], r["SourceFile"]), []).append(int(r["SourceLine"]))


def folder(del_id):
    g = glob.glob(os.path.join(APP, "execution", "PKG-*", "1_Working", del_id + "_*"))
    return g[0]


for key in sys.argv[1:]:
    base = key.split("#")[0] + "#" + key.split("#")[1].split(".")[0]
    r = idx.get(base)
    if not r:
        print("### %s: not in index" % key)
        continue
    path = os.path.join(folder(r["DeliverableID"]), r["SourceFile"])
    lines = open(path, encoding="utf-8").read().split("\n")
    start = int(r["SourceLine"])
    later = sorted(l for l in by_file[(r["DeliverableID"], r["SourceFile"])] if l > start)
    end = later[0] - 1 if later else min(len(lines), start + 40)
    end = min(end, start + 60)
    print("### %s  %s:%d-%d  [%s | %s]" % (key, r["SourceFile"], start, end, r["Section"], r["SubItems"]))
    for i in range(start, end + 1):
        print("%d: %s" % (i, lines[i - 1][:700]))
