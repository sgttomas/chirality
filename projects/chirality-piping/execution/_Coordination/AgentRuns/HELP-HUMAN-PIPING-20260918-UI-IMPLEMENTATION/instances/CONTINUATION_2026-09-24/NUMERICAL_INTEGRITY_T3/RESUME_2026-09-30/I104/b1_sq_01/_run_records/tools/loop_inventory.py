"""I104 SQ G5: the inventory of every loop (brace loop or iterator-adapter closure, loopscan.py) whose
header lies on a line B1 added or changed, in the TEXT chain's production files (stdlib only; Git reads
only, GIT_OPTIONAL_LOCKS=0).

For each loop: file, header line, enclosing fn key (the call graph's spans), whether the fn is reached
from the D1 root and whether it is a TEXT ancestor (an ancestor of a function holding a text site, so its
loops enter the multiplicities), the rule the TEXT tool would apply (text_budget.py's loop_bound order:
array literal, the rules in order, a literal range) and that rule's bound and why, or UNMAPPED.
Also lists every existing rule's bound whose `why` names one case / D1.4 (the rebind candidates).
Usage: python3 loop_inventory.py <repo> <old rev> <new rev> <snapshot P root> <edges json> <loop_bounds json>
       <text_budget out json> <crate_dirs.txt> <chain dir (loopscan.py)> > out.json
"""
import json, os, re, subprocess, sys, collections
repo, old, new, proot, edges_p, lb_p, tb_p, crates_p, chain = sys.argv[1:10]
sys.path.insert(0, chain)
import loopscan
P = "projects/chirality-piping/"
env = dict(os.environ, GIT_OPTIONAL_LOCKS="0")
def git(*a):
    return subprocess.run(["git", "-C", repo, *a], capture_output=True, text=True, env=env, check=True).stdout
crates = open(crates_p).read().split()
files = [f[len(P):] for f in git("diff", "--name-only", old, new, "--", P + "core").split("\n") if f.endswith(".rs")]
files = [f for f in files if "/tests/" not in f and not f.endswith("_tests.rs") and any(f.startswith(c + "/") for c in crates)]
cg = json.load(open(edges_p)); edges = cg["edges"]; spans = cg["spans"]
LB = json.load(open(lb_p)); tb = json.load(open(tb_p))
COUNTS = dict(LB["counts"]["caps"])
rules = [(re.compile(r["re"]), r["bound"], r["why"], i) for i, r in enumerate(LB["loops"])]
# reachability and TEXT ancestors, as text_budget.py forms them
root = [k for k in edges if k.rsplit(":", 1)[1] == "run_linear_static_preview_value_with_retained_direct"]
reach, todo = set(root), list(root)
while todo:
    v = todo.pop()
    for w in edges.get(v, []):
        if w not in reach: reach.add(w); todo.append(w)
site_fns = set(tb["function_multiplicity"].keys())
rev = collections.defaultdict(set)
for v in reach:
    for w in edges.get(v, []):
        if w in reach: rev[w].add(v)
anc, todo = set(x for x in site_fns if x in reach), [x for x in site_fns if x in reach]
while todo:
    v = todo.pop()
    for u in rev[v]:
        if u not in anc: anc.add(u); todo.append(u)
def array_len(h):
    m = re.search(r"\bin\s*\[(.*)\]", h)
    if not m: return None
    body, d, n, cur = m.group(1), 0, 0, ""
    for ch in body:
        if ch in "([{": d += 1
        elif ch in ")]}": d -= 1
        if ch == "," and d == 0:
            if cur.strip(): n += 1
            cur = ""
        else: cur += ch
    if cur.strip(): n += 1
    return n
def rule_of(h):
    if re.match(r"for\s.*\bin\s*\[", h):
        a = array_len(h)
        if a is not None: return {"kind": "array literal", "bound": a}
    for rx, b, why, i in rules:
        if rx.search(h): return {"kind": "rule", "index": i, "re": rx.pattern, "bound": b, "why": why[:200]}
    m = re.search(r"\bin\s*\(?\s*(\d+)(?:usize)?\s*\.\.(=?)\s*(\d+)\b", h)
    if m: return {"kind": "literal range", "bound": max(0, int(m.group(3)) - int(m.group(1)) + (1 if m.group(2) else 0))}
    a = array_len(h)
    if a is not None: return {"kind": "array literal", "bound": a}
    return {"kind": "UNMAPPED"}
fspans = collections.defaultdict(list)
for k, (f, a, b) in spans.items():
    fspans[f].append((a, b, k))
out = []
for f in files:
    added = set()
    for line in git("diff", "-U0", old, new, "--", P + f).split("\n"):
        m = re.match(r"@@ -\d+(?:,\d+)? \+(\d+)(?:,(\d+))? @@", line)
        if m:
            s, c = int(m.group(1)), int(m.group(2) or 1)
            added.update(range(s, s + c))
    raw = open(os.path.join(proot, f), encoding="utf-8").read()
    bt = loopscan.blank(raw)
    offs, acc = [], 0
    for ln in bt.split("\n"):
        offs.append(acc); acc += len(ln) + 1
    def line_of(pos):
        lo, hi = 0, len(offs) - 1
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if offs[mid] <= pos: lo = mid
            else: hi = mid - 1
        return lo + 1
    found = []
    for m in loopscan.BRACE.finditer(bt):
        found.append((m.start(), " ".join(m.group(1).split())[:4000]))
    span_heads = {a: h for (a, b, h) in loopscan.loop_spans(bt)}
    for m in loopscan.ADAPT.finditer(bt):
        op = m.end() - 1
        if op in span_heads: found.append((m.start(), span_heads[op]))
    for pos, h in found:
        ln = line_of(pos)
        if ln not in added: continue
        fk = None
        for a, b, k in fspans.get(f, []):
            if a <= pos < b and (fk is None or a >= fspans_start): fk, fspans_start = k, a
        out.append({"file": f, "line": ln, "header": h[:300], "fn": fk, "reached": fk in reach if fk else False,
                    "text_ancestor": fk in anc if fk else False, "rule": rule_of(h)})
one_case = [{"index": i, "re": r["re"], "bound": r["bound"], "why": r["why"][:240]} for i, r in enumerate(LB["loops"])
            if re.search(r"one case|one load case|D1\.4|single case|the one call|the one group|one source|loads over", r["why"])]
json.dump({"files": files, "loops": out, "one_case_rules": one_case,
           "edge_per_call": LB.get("edge_per_call", []), "counts_caps": COUNTS}, sys.stdout, indent=1)
