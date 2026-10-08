"""I107 SB round 2 (PR-N): the TEXT gate against SQ's recorded point, with every difference attributed to the norm.
Round 1's `text_sq` (R/I107/b1_passb_01/_run_records/tools/b1_checks.py) demanded equality; PR-N adds call-graph
nodes and edges, so this check keeps text_sq's equalities and admits only the norm's graph changes:
  - every text_budget variant complete and row-equal to SQ's (row-matched, line-agnostic), with equal TAV and D;
  - every other SQ file byte-equal (JSON-equal for summary.json), except:
  - edges.json (SQ's carried by the line map): SQ's nodes and edges all present; every added node a correct_norm.rs fn
    and every added edge touching one; site_loops equal with loop headers compared hypot/norm-free, plus added entries
    whose caller or callee is a correct_norm.rs fn; spans moved only within changed files, resized only for fns that enclose a
    reviewed delta row, new only for correct_norm.rs fns;
  - looplog.json: equal as a multiset with line numbers and hypot/norm spellings dropped;
  - cg.out.json: files +1, nodes and edges up by exactly the added ones, root depths and recursion lists equal.
Prints one JSON line; exit 0 if all hold, 6 otherwise (I65's "delta to read").
Usage: python3 text_pn.py <run dir> <SQ point dir> <text_row_diff.py|-> <mapped SQ dir|-> <delta_inventory.json> <rules linemap out json>
       <round 1's delta_inventory.json(.gz)>
The files whose spans may move are those the rules' line map saw change (57c92a7b33 -> the basis); the fns whose spans may
change length are those enclosing a row of this delta (B1 -> PR-N; every row classified) or a reviewed row of
round 1's (57c92a7b33 -> B1)."""
import collections, gzip, json, os, re, subprocess, sys
run, ref, rowdiff, mapped, inv_p, lm_p, r1_p = sys.argv[1:8]
load = lambda p: gzip.open(p + ".gz").read() if not os.path.exists(p) and os.path.exists(p + ".gz") else open(p, "rb").read()
CN = "/correct_norm.rs:"
nh = lambda s: re.sub(r"[^A-Za-z0-9_\[\]]", "", s.replace("hypot", "").replace("norm3", "").replace("norm2", ""))
nl = lambda s: re.sub(r":\d+", "", s)
inv = json.load(open(inv_p)); r1 = json.load(gzip.open(r1_p) if r1_p.endswith(".gz") else open(r1_p))
lm = json.load(open(lm_p)); lm = lm.get("summary", lm)
changed = set(lm["changed_production_rs"]) | {r["file"] for r in inv["rows"] if r["class"] != "not-d1"}
allowed = ({i["fn"] for r in inv["rows"] for i in r.get("fns", [])}                       # any row of this delta (every one classified)
           | {i["fn"] for r in r1["rows"] if r.get("reviewed") for i in r.get("fns", [])})   # round 1's reviewed rows
where = lambda f: next((p for p in (os.path.join(run, "work", f), os.path.join(run, f)) if os.path.exists(p)), None)
issues, compared, attributed = [], [], {}
names = sorted({f[:-3] if f.endswith(".gz") else f for f in os.listdir(ref)} - {"run_point.log", "audit_controls.out.json", "audit_controls.out.txt"})
mine_edges = json.load(open(os.path.join(run, "edges.json")))
for f in names:
    mine = where(f)
    if mine is None: issues.append({"missing_in_run": f}); continue
    if f.startswith("text_budget") and rowdiff != "-":
        t = json.load(open(mine))
        if not t["complete"] or t["unclassified_args"] or t["unmapped_loop_headers"]:
            issues.append({"file": f, "incomplete": t["unclassified_args"][:10], "unmapped": t["unmapped_loop_headers"][:5]})
        refp = os.path.join(run, "ref_" + f); open(refp, "wb").write(load(os.path.join(ref, f)))
        d = json.loads(subprocess.run([sys.executable, rowdiff, refp, mine], capture_output=True, text=True, check=True).stdout.split("\n")[0]); os.remove(refp)
        if d["changed"] or d["unmatched_positive_in_first"] or d["only_in_second"] or d["tav"][0] != d["tav"][1] or d["D"][0] != d["D"][1]:
            issues.append({"file": f, "rows": d})
        compared.append([f, "rows", d["rows"], d["tav"][1], d["D"][1]]); continue
    if f == "edges.json" and mapped != "-":
        x, y = json.load(open(os.path.join(mapped, f))), mine_edges
        ea, eb = x["edges"], y["edges"]
        new_nodes = sorted(set(eb) - set(ea)); lost_nodes = sorted(set(ea) - set(eb))
        lost = [(k, w) for k in ea for w in ea[k] if w not in eb.get(k, [])]
        added = [(k, w) for k in eb for w in eb[k] if w not in ea.get(k, [])]
        bad = lost_nodes + lost + [n for n in new_nodes if CN not in n] + [e for e in added if CN not in e[0] and CN not in e[1]]
        sl = lambda L: collections.Counter(json.dumps([e[0], e[1], [[nh(h) for h in p] for p in e[2]]]) for e in L)
        sa, sb = sl(x["site_loops"]), sl(y["site_loops"])
        sl_lost = list((sa - sb).elements()); sl_added = list((sb - sa).elements())
        bad += sl_lost + [e for e in sl_added if CN not in json.loads(e)[0] and CN not in json.loads(e)[1]]
        px, py = x["spans"], y["spans"]
        moved = [k for k in px if k in py and px[k] != py[k]]
        bad += [k for k in moved if px[k][0] != py[k][0] or not any(px[k][0].endswith(c) for c in changed)]
        resized = sorted({k.split("/src/")[-1] for k in moved if px[k][2] - px[k][1] != py[k][2] - py[k][1]})
        bad += [k for k in resized if k not in allowed]
        bad += [k for k in set(px) - set(py)] + [k for k in set(py) - set(px) if CN not in k]
        attributed["edges"] = {"new_nodes": [n.split("/src/")[-1] for n in new_nodes], "added_edges": len(added),
                               "added_site_loops": len(sl_added), "spans_moved": len(moved), "resized": resized, "bad": [str(b)[:200] for b in bad[:8]]}
        compared.append([f, "SQ's graph kept; additions are the norm's", not bad]); issues += [{"edges": str(b)[:200]} for b in bad[:8]]; continue
    if f == "looplog.json" and mapped != "-":
        c = lambda L: collections.Counter(json.dumps([nl(e[0]), nh(e[1])] + e[2:]) for e in L)
        a, b = c(json.load(open(os.path.join(mapped, f)))), c(json.load(open(mine)))
        diff = list((a - b).elements()) + [e for e in (b - a).elements() if CN not in e]
        attributed["looplog"] = {"entries": [sum(a.values()), sum(b.values())], "added_norm_entries": sum(1 for e in (b - a).elements() if CN in e)}
        compared.append([f, "multiset, lines and hypot/norm spellings dropped", not diff]); issues += [{"looplog": e[:200]} for e in diff[:6]]; continue
    if f == "cg.out.json":
        x, y = json.loads(load(os.path.join(ref, f))), json.load(open(mine))
        eb = mine_edges["edges"]; ea = json.load(open(os.path.join(mapped, "edges.json")))["edges"] if mapped != "-" else None
        n_new = sum(1 for k in eb if CN in k)
        exp_edges = sum(1 for k in eb for w in eb[k] if CN in k or CN in w)
        ok = (y["files"] == x["files"] + 1 and y["nodes"] == x["nodes"] + n_new and y["edges"] == x["edges"] + exp_edges
              and sorted(y["root_depths"].values()) == sorted(x["root_depths"].values())
              and all(x[k] == y[k] for k in x if k not in ("files", "nodes", "edges", "root_depths")))
        attributed["cg.out"] = {"files": [x["files"], y["files"]], "nodes": [x["nodes"], y["nodes"]], "edges": [x["edges"], y["edges"]],
                                "norm_nodes": n_new, "edges_touching_norm": exp_edges, "root_depths": [list(x["root_depths"].values()), list(y["root_depths"].values())]}
        compared.append([f, "counts up by the norm's nodes and edges; depths equal", ok])
        if not ok: issues.append({"differs": f}); continue
        continue
    if f == "summary.json":
        eq = json.loads(load(os.path.join(ref, f))) == json.load(open(mine))
    else:
        eq = load(os.path.join(ref, f)) == open(mine, "rb").read()
    compared.append([f, "json" if f.endswith("summary.json") else "bytes", eq])
    if not eq: issues.append({"differs": f})
s = json.load(open(os.path.join(run, "summary.json")))
print(json.dumps({"check": "text_pn", "code": 6 if issues else 0, "issues": issues, "attributed": attributed, "compared": compared,
                  "D": s.get("D"), "D_env": s.get("D_env"), "TAV": s.get("TAV"), "complete": s.get("text_complete"),
                  "E_mov_plus_R_chain": [s["sparse"]["E_mov_plus_R"], s["dense"]["E_mov_plus_R"]]}))
sys.exit(6 if issues else 0)
