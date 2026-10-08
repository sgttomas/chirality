"""I104 SQ G5: name fan-out from functions on B1-changed lines: every (caller, name) whose call edges reach more
than one same-named target, with each target's TEXT multiplicity at the run. Usage: fanout_b1.py <repo> <old> <new>
<edges json> <text_budget out> <loop inventory json>"""
import json, os, re, subprocess, sys, collections
repo, old, new, edges_p, tb_p, inv_p = sys.argv[1:7]
P = "projects/chirality-piping/"
env = dict(os.environ, GIT_OPTIONAL_LOCKS="0")
def git(*a): return subprocess.run(["git", "-C", repo, *a], capture_output=True, text=True, env=env, check=True).stdout
added = collections.defaultdict(set)
for f in json.load(open(inv_p))["files"]:
    for line in git("diff", "-U0", old, new, "--", P + f).split("\n"):
        m = re.match(r"@@ -\d+(?:,\d+)? \+(\d+)(?:,(\d+))? @@", line)
        if m:
            s, c = int(m.group(1)), int(m.group(2) or 1); added[f].update(range(s, s + c))
cg = json.load(open(edges_p)); E = cg["edges"]; SP = cg["spans"]; tb = json.load(open(tb_p)); M = tb["function_multiplicity"]
src = {}
def changed_fn(k):
    f, a, b = SP[k]
    if f not in added: return False
    if f not in src: src[f] = open(os.path.join(os.environ["PROOT"], f), encoding="utf-8").read()
    l0, l1 = src[f].count("\n", 0, a) + 1, src[f].count("\n", 0, b) + 1
    return any(l0 <= x <= l1 for x in added[f])
out = []
for a, ws in E.items():
    if a not in SP or not M.get(a) or not changed_fn(a): continue
    by = collections.defaultdict(list)
    for w in ws: by[w.rsplit(":", 1)[1]].append(w)
    for name, ts in by.items():
        if len(ts) > 1:
            out.append({"caller": a.split("/src/")[-1], "M_caller": M.get(a), "name": name,
                        "targets": [[t.split("/src/")[-1], M.get(t, 0)] for t in ts]})
out.sort(key=lambda x: -max(m for _, m in x["targets"]))
json.dump(out, sys.stdout, indent=1)
