#!/usr/bin/env python3
"""Reverse-pass area selection (manager brief step 6) and merged capability input.
Usage: areas.py <DEL-ID> [--write]
Areas = Area (R1_INVENTORY/IMPLEMENTATION_SURFACES.csv) of every code path cited in the sealed
ledger's ImplementationEvidence, plus the areas of R1_INVENTORY/HINTS/<DEL-ID>.csv hits.
A path maps to the Area of an exact IMPLEMENTATION_SURFACES row, else (non-test paths only) to the
majority Area of surfaces in its own directory; test files and unmapped paths add no area. --write concatenates the chosen R2/SURFACES/<AREA>_capabilities.csv data rows
(sorted area order) into <DEL-ID>/REVERSE_INPUT_capabilities.csv and writes <DEL-ID>/REVERSE_AREAS.md."""
import csv, os, re, sys, collections
PKG = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUN = os.path.dirname(os.path.dirname(PKG))
def rows(p):
    t = open(p, encoding="utf-8", newline="").read()
    r = list(csv.reader(t.splitlines(True) and __import__("io").StringIO(t)))
    if r and r[-1] == ["#END"]: r = r[:-1]
    return r
def dicts(p):
    r = rows(p); return [dict(zip(r[0], x)) for x in r[1:]]
surf = {d["Path"]: d["Area"] for d in dicts(os.path.join(RUN, "R1_INVENTORY", "IMPLEMENTATION_SURFACES.csv"))}
dirs = collections.defaultdict(collections.Counter)
for p, a in surf.items():
    parts = p.split("/")
    for i in range(1, len(parts)): dirs["/".join(parts[:i])][a] += 1
def area(p):
    if p in surf: return surf[p]
    if TEST.search(p): return None
    d = p.rsplit("/", 1)[0]
    return dirs[d].most_common(1)[0][0] if d in dirs else None
TEST = re.compile(r"(__tests__|/tests?/|\.test\.|\.spec\.)")
PATH = re.compile(r"(projects/chirality-(?:app-dev|runtime)/[A-Za-z0-9_./@\[\]()-]+\.(?:ts|tsx|mjs|js|cjs|json|yml|yaml))")
dl = sys.argv[1]; led = os.path.join(PKG, dl, f"{dl}_claims.csv")
ev = collections.Counter(); hint = collections.Counter(); unmapped = set()
for d in dicts(led):
    for p in PATH.findall(d["ImplementationEvidence"]):
        a = area(p)
        if a: ev[a] += 1
        else: unmapped.add(p)
for d in dicts(os.path.join(RUN, "R1_INVENTORY", "HINTS", f"{dl}.csv")):
    a = area(d["HitPath"])
    if a: hint[a] += 1
areas = sorted(set(ev) | set(hint))
print(dl, "areas:", areas); print(" from ledger evidence:", dict(ev)); print(" from hints:", dict(hint))
if unmapped: print(" unmapped evidence paths:", sorted(unmapped)[:10], len(unmapped))
if "--write" in sys.argv:
    out = os.path.join(PKG, dl, "REVERSE_INPUT_capabilities.csv"); hdr = None; data = []
    for a in areas:
        r = rows(os.path.join(RUN, "R2", "SURFACES", f"{a}_capabilities.csv"))
        hdr = hdr or r[0]; assert r[0] == hdr; data += r[1:]
    with open(out, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh, lineterminator="\n"); w.writerow(hdr); w.writerows(data); fh.write("#END\n")
    with open(os.path.join(PKG, dl, "REVERSE_AREAS.md"), "w") as fh:
        fh.write(f"# Reverse-pass areas — {dl}\n\nScript: `R2/PKG-08/_scripts/areas.py {dl} --write` (sealed ledger + R1 HINTS).\n\n")
        fh.write("| Area | Ledger evidence paths | HINTS hits |\n|---|---:|---:|\n")
        for a in areas: fh.write(f"| {a} | {ev.get(a,0)} | {hint.get(a,0)} |\n")
        fh.write(f"\nMerged capability rows: {len(data)} (`REVERSE_INPUT_capabilities.csv`).\n")
        if unmapped: fh.write(f"\nUnmapped evidence paths: {len(unmapped)} (no Area in IMPLEMENTATION_SURFACES).\n")
    print(" wrote", out, len(data), "rows")
