#!/usr/bin/env python3
"""I109 round 2: which correct_norm call sites lie in the retained route's (D1) call graph.

Reads SQ's callgraph_g5.py edges (CG_EDGES_OUT: edges and node spans) built from the root
`run_linear_static_preview_value_with_retained_direct` over SQ's crate_dirs.txt, takes the
nodes reachable from the root, and maps every production `norm2(`/`norm3(` call (comments,
strings and test modules excluded by the graph's own lexing) to its enclosing fn node.
Usage: d1_norm_sites.py <P root> <edges.json> <out.json>"""
import json, os, re, sys
root_dir, edges_path, out_path = sys.argv[1:4]
g = json.load(open(edges_path))
edges, spans = g["edges"], g["spans"]
roots = [k for k in spans if k.endswith(":run_linear_static_preview_value_with_retained_direct")]
seen, todo = set(roots), list(roots)
while todo:
    v = todo.pop()
    for w in edges.get(v, []):
        if w not in seen:
            seen.add(w); todo.append(w)
norm_nodes = [k for k in spans if k.split(":")[0].endswith("correct_norm.rs")]
sites = []
call = re.compile(r"\bnorm[23]\s*\(")
texts = {}
for key, (path, start, end) in spans.items():
    if path.endswith("correct_norm.rs") or start is None or end is None:
        continue
    if path not in texts:
        texts[path] = open(os.path.join(root_dir, path), encoding="utf-8").read()
    text = texts[path]
    for m in call.finditer(text, start, end):
        line_start = text.rfind("\n", 0, m.start()) + 1
        if "//" in text[line_start:m.start()]:
            continue
        name = m.group(0).split("(")[0].strip()
        local = re.search(r"\bfn\s+" + name + r"\s*\(", text) is not None
        if local and not text[max(0, m.start() - 14):m.start()].endswith("correct_norm::"):
            continue  # a same-named local fn (formation_check's wide norm3, final_case's enclosure norm2)
        ln = text.count("\n", 0, m.start()) + 1
        sites.append({"site": f"{path}:{ln}", "fn": key, "in_d1": key in seen,
                      "calls_norm_edge": any(n in edges.get(key, []) for n in norm_nodes)})
sites.sort(key=lambda s: s["site"])
out = {"root": roots, "reachable_nodes": len(seen), "nodes": len(spans), "norm_fns_in_d1": [k for k in norm_nodes if k in seen], "sites": sites}
json.dump(out, open(out_path, "w"), indent=1)
for s in sites:
    print(("D1    " if s["in_d1"] else "not-D1") + "  " + s["site"] + "  " + s["fn"].split(":")[-1] + ("" if s["calls_norm_edge"] else "  (no edge?)"))
print(json.dumps({k: v for k, v in out.items() if k != "sites"}))
