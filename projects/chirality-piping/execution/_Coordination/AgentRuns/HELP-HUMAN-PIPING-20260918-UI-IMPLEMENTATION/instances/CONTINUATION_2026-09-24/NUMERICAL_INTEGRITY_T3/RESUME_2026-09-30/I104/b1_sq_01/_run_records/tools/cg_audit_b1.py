"""I104 SQ G5: the call graph's unresolved call tokens on lines B1 added (2007709549..57c92a7b33), with whether
the token's name is the name of a scanned function that is a TEXT ancestor (a dropped true call to it could
drop text). Usage: cg_audit_b1.py <repo> <old> <new> <audit json> <edges json> <text_budget out>"""
import json, os, re, subprocess, sys, collections
repo, old, new, audit_p, edges_p, tb_p = sys.argv[1:7]
P = "projects/chirality-piping/"
env = dict(os.environ, GIT_OPTIONAL_LOCKS="0")
def git(*a): return subprocess.run(["git", "-C", repo, *a], capture_output=True, text=True, env=env, check=True).stdout
added = collections.defaultdict(set)
for f in git("diff", "--name-only", old, new, "--", P + "core").split():
    if not f.endswith(".rs"): continue
    for line in git("diff", "-U0", old, new, "--", f).split("\n"):
        m = re.match(r"@@ -\d+(?:,\d+)? \+(\d+)(?:,(\d+))? @@", line)
        if m:
            s, c = int(m.group(1)), int(m.group(2) or 1); added[f[len(P):]].update(range(s, s + c))
a = json.load(open(audit_p)); cg = json.load(open(edges_p)); tb = json.load(open(tb_p))
edges = cg["edges"]
root = [k for k in edges if k.rsplit(":", 1)[1] == "run_linear_static_preview_value_with_retained_direct"]
reach, todo = set(root), list(root)
while todo:
    v = todo.pop()
    for w in edges.get(v, []):
        if w not in reach: reach.add(w); todo.append(w)
site_fns = set(tb["function_multiplicity"]); rev = collections.defaultdict(set)
for v in reach:
    for w in edges.get(v, []):
        if w in reach: rev[w].add(v)
anc, todo = set(x for x in site_fns if x in reach), [x for x in site_fns if x in reach]
while todo:
    v = todo.pop()
    for u in rev[v]:
        if u not in anc: anc.add(u); todo.append(u)
anc_names = collections.defaultdict(list)
for k in anc: anc_names[k.rsplit(":", 1)[1]].append(k.split("/src/")[-1])
all_names = collections.defaultdict(list)
for k in edges: all_names[k.rsplit(":", 1)[1]].append(k.split("/src/")[-1])
out = []
for r in a["rows"]:
    f, ln = r["line"].rsplit(":", 1)
    if int(ln) not in added.get(f, ()): continue
    out.append({"line": r["line"].split("/src/")[-1], "caller": r["caller"].split("/src/")[-1] if r["caller"] else None,
                "caller_reached": r["caller"] in reach, "name": r["name"], "reason": r["reason"],
                "text_ancestor_fns_of_that_name": anc_names.get(r["name"], []),
                "scanned_fns_of_that_name": len(all_names.get(r["name"], [])), "context": r["context"][:160]})
json.dump(out, sys.stdout, indent=1)
