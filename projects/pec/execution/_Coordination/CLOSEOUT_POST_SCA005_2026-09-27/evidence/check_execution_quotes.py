import csv, pathlib, sys
repo = pathlib.Path(sys.argv[1]); ex = repo/"projects/pec/execution"
n=v=0; sow=[]
for f in sorted(ex.glob("PKG-*/1_Working/DEL-*/Dependencies.csv")):
    for r in csv.DictReader(open(f, newline="", encoding="utf-8")):
        if (r["DependencyClass"], r["Status"]) != ("EXECUTION","ACTIVE"): continue
        n+=1; ev = repo/"projects/pec"/r["EvidenceFile"]
        ok = ev.is_file() and r["EvidenceQuote"] in ev.read_text(encoding="utf-8")
        v+=ok
        if not ok: print("MISS", r["DependencyID"], r["EvidenceFile"])
        if "ScopeOfWork.md" in r["EvidenceFile"] or "artifacts/" in r["EvidenceFile"]: sow.append((r["DependencyID"], r["EvidenceFile"], ok))
print(f"ACTIVE EXECUTION quotes verbatim {v}/{n}")
for s in sow: print("SOW-or-artifact-cited", *s)
