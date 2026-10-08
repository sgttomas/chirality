"""I104 SQ (PLAN_v2 §3.4): the deepest acyclic call chain from the Direct root on B1's call graph
(the G5 run's edges.json, written by callgraph_g5.py with B1's adjudicated rules). Recomputes the
SCC condensation as callgraph_g5.py does and prints one longest path, one component per frame.
Usage: python3 deepest_chain.py <edges.json> <root key>"""
import json, sys
sys.setrecursionlimit(100000)
E = {k: set(v) for k, v in json.load(open(sys.argv[1]))["edges"].items()}
root = sys.argv[2]
nodes = set(E) | {w for v in E.values() for w in v}
for v in nodes:
    E.setdefault(v, set())
index, low, onstack, stack, comp_of, sccs, idx = {}, {}, set(), [], {}, [], [0]
for v0 in sorted(nodes):
    if v0 in index:
        continue
    work = [(v0, iter(sorted(E[v0])))]
    index[v0] = low[v0] = idx[0]; idx[0] += 1; stack.append(v0); onstack.add(v0)
    while work:
        v, it = work[-1]
        adv = False
        for w in it:
            if w not in index:
                index[w] = low[w] = idx[0]; idx[0] += 1; stack.append(w); onstack.add(w)
                work.append((w, iter(sorted(E[w])))); adv = True; break
            elif w in onstack:
                low[v] = min(low[v], index[w])
        if adv:
            continue
        work.pop()
        if work:
            low[work[-1][0]] = min(low[work[-1][0]], low[v])
        if low[v] == index[v]:
            comp = []
            while True:
                w = stack.pop(); onstack.discard(w); comp.append(w)
                if w == v:
                    break
            for w in comp:
                comp_of[w] = len(sccs)
            sccs.append(sorted(comp))
C = {}
for v in nodes:
    for w in E[v]:
        if comp_of[v] != comp_of[w]:
            C.setdefault(comp_of[v], set()).add(comp_of[w])
memo, nxt = {}, {}
def depth(c):
    if c in memo:
        return memo[c]
    best, arg = 0, None
    for d in sorted(C.get(c, ())):
        x = 1 + depth(d)
        if x > best:
            best, arg = x, d
    memo[c], nxt[c] = best, arg
    return best
d = depth(comp_of[root])
path, c = [], comp_of[root]
while c is not None:
    path.append(sccs[c]); c = nxt.get(c)
print(json.dumps({"root": root, "depth_edges": d, "frames": len(path),
                  "chain": [p[0] if len(p) == 1 else f"SCC({len(p)}): {p[0]} ..." for p in path]}, indent=1))
