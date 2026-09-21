#!/usr/bin/env python3
"""Reverse-pass capability areas for one sealed ledger (brief step 6).
Areas = Area (R1_INVENTORY/IMPLEMENTATION_SURFACES.csv) of every code path cited in the sealed
ledger's ImplementationEvidence, plus the areas of R1_INVENTORY/HINTS/<DEL-ID>.csv hits.
Usage: areas.py <unit-folder>   -> prints JSON {unit, del, ledger_sha256, evidence_areas, hint_areas, areas, files}"""
import csv, hashlib, json, os, re, sys
pkg = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
run = os.path.dirname(os.path.dirname(pkg))
unit = sys.argv[1].rstrip("/"); d = os.path.join(pkg, os.path.basename(unit)); dl = os.path.basename(d).split("_")[0]
area = {r["Path"]: r["Area"] for r in csv.DictReader(open(os.path.join(run, "R1_INVENTORY", "IMPLEMENTATION_SURFACES.csv"))) if r.get("Area")}
led = os.path.join(d, dl + "_claims.csv")
txt = open(led, encoding="utf-8").read()
rows = list(csv.DictReader([l for l in txt.split("\n")] if False else __import__("io").StringIO(txt.rsplit("#END", 1)[0])))
PATH = re.compile(r"(projects/[A-Za-z0-9_@./\[\]()-]+?\.(?:tsx|ts|mjs|cjs|js|json|yml|yaml))")
ev = {}
for r in rows:
    for p in PATH.findall(r["ImplementationEvidence"]):
        if p in area: ev[area[p]] = ev.get(area[p], 0) + 1
hi = {}
for r in csv.DictReader(open(os.path.join(run, "R1_INVENTORY", "HINTS", dl + ".csv"))):
    a = area.get(r["HitPath"])
    if a: hi[a] = hi.get(a, 0) + 1
areas = sorted(set(ev) | set(hi))
print(json.dumps({"unit": os.path.basename(d), "del": dl, "ledger_rows": len(rows),
                  "ledger_sha256": hashlib.sha256(open(led, "rb").read()).hexdigest(),
                  "evidence_areas": ev, "hint_areas": hi, "areas": areas,
                  "files": [f"R2/SURFACES/{a}_capabilities.csv" for a in areas]}))
