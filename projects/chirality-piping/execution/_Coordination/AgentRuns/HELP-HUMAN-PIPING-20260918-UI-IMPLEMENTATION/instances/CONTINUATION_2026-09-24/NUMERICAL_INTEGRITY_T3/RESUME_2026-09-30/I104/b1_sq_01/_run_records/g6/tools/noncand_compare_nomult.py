"""I104 SQ (QUAL §11 at C = 3): noncand_compare.py's match with the multiplicity dropped from the key.
At C = 3 every per-case site's multiplicity is c times RV87's (c = 1), so the original key reports
nearly every row as new; this compares the expressions themselves (file, enclosing fn, kind/spec, class,
expression prefix) and lists each new or absent one, with its multiplicity, to be read by type.
Usage: noncand_compare_nomult.py <rv87 rows> <run rows>"""
import json, sys, collections
rv = json.load(open(sys.argv[1]))["rows"]; run = json.load(open(sys.argv[2]))
def key(r):
    return (r["site"].rsplit(":", 1)[0].split("core/")[-1], (r["fn"] or "").rsplit(":", 1)[-1], r["kind_or_spec"], r["class"])
expr = lambda r: " ".join(r["expr"].split())
pool = collections.defaultdict(list)
for r in rv:
    pool[key(r)].append(r)
new, mult = [], collections.Counter()
for r in run:
    cands = pool.get(key(r), []); e = expr(r)
    hit = next((i for i, x in enumerate(cands) if expr(x) == e or e.startswith(expr(x)) or expr(x).startswith(e)), None)
    if hit is None:
        new.append(r)
    else:
        x = cands.pop(hit); mult[f"{x['mult']}->{r['mult']}"] += 1
gone = [x for xs in pool.values() for x in xs]
print(json.dumps({"rv87_rows": len(rv), "run_rows": len(run), "matched": len(run) - len(new), "multiplicity_changes": dict(mult),
                  "new_noncandidates": new, "rv87_rows_absent_now": gone}, indent=1))
