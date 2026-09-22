#!/usr/bin/env python3
"""Step 6: capability areas for a sealed PKG-00 ledger, and a combined capability file.
Areas = Area (R1_INVENTORY/IMPLEMENTATION_SURFACES.csv) of every code path cited in the sealed
ledger's ImplementationEvidence, plus the areas of R1_INVENTORY/HINTS/<DEL>.csv hits.
Writes <PKG>/<DEL>/REVERSE_INPUT/AREAS.md and COMBINED_capabilities.csv (header + all rows of the
selected R2/SURFACES/<AREA>_capabilities.csv files, in area order, + #END), used by the worker for
one reverse file and by the validator's single --capabilities argument.
Usage: areas.py <DEL-ID>"""
import csv, io, hashlib, os, re, sys, collections
PKG = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUN = os.path.dirname(os.path.dirname(PKG))
d = sys.argv[1]
def rows(p):
    t = open(p, encoding="utf-8").read().rstrip("\n")
    recs = list(csv.reader(io.StringIO(t)))
    hdr, body = recs[0], [r for r in recs[1:] if r and r != ["#END"]]
    return hdr, [dict(zip(hdr, r)) for r in body]
_, surf = rows(os.path.join(RUN, "R1_INVENTORY", "IMPLEMENTATION_SURFACES.csv"))
S = {r["Path"]: r["Area"] for r in surf}
led = os.path.join(PKG, d, f"{d}_claims.csv")
_, L = rows(led)
cited = collections.Counter(); unmapped = collections.Counter()
pat = re.compile(r"(projects/chirality-(?:app-dev|runtime)/[A-Za-z0-9_@./\-\[\]]+?\.(?:tsx?|mjs|cjs|js|json|py|sh|ya?ml))")
for r in L:
    for p in pat.findall(r["ImplementationEvidence"]):
        (cited.__setitem__(S[p], cited[S[p]] + 1) if p in S else unmapped.__setitem__(p, unmapped[p] + 1))
_, H = rows(os.path.join(RUN, "R1_INVENTORY", "HINTS", f"{d}.csv"))
hint = collections.Counter(S[r["HitPath"]] for r in H if r.get("HitPath") in S)
areas = sorted(set(cited) | set(hint))
out = os.path.join(PKG, d, "REVERSE_INPUT"); os.makedirs(out, exist_ok=True)
hdr = None; allrows = []
for a in areas:
    h, rs = rows(os.path.join(RUN, "R2", "SURFACES", f"{a}_capabilities.csv"))
    hdr = hdr or h; allrows += [[r[k] for k in h] for r in rs]
comb = os.path.join(out, "COMBINED_capabilities.csv")
with open(comb, "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh, lineterminator="\n"); w.writerow(hdr); w.writerows(allrows); fh.write("#END\n")
sha = hashlib.sha256(open(led, "rb").read()).hexdigest()
with open(os.path.join(out, "AREAS.md"), "w") as fh:
    fh.write(f"# Reverse-pass areas for {d}\n\n- Sealed ledger SHA-256: `{sha}`\n")
    fh.write(f"- Areas from ImplementationEvidence code paths: {dict(sorted(cited.items())) or 'none'}\n")
    fh.write(f"- Areas from HINTS hits: {dict(sorted(hint.items())) or 'none'}\n")
    fh.write(f"- Cited paths not in IMPLEMENTATION_SURFACES (no area): {len(unmapped)} distinct\n")
    for p, n in sorted(unmapped.items()): fh.write(f"  - `{p}` ({n})\n")
    fh.write(f"- **Selected areas:** {', '.join(areas)}; combined rows: {len(allrows)}\n")
    fh.write(f"- Combined file: `COMBINED_capabilities.csv` (SHA-256 `{hashlib.sha256(open(comb,'rb').read()).hexdigest()}`)\n")
print(areas, len(allrows), sha)
